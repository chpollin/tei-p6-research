"""Collect the GitHub relations and review threads the REST snapshot cannot see.

This is step 6 of the GitHub bootstrap in ``knowledge/operations.md``. The REST
stage (``tools.corpus.github_snapshot``) records issues, pull requests and their
children; cross-references, connections, duplicate marks, closers and
pull-request review threads exist only in the GraphQL schema. This adapter reads
the item numbers of the completed REST run from its normalized stream, asks the
GraphQL API for exactly those items, and writes one relation and review-thread
stream plus one run manifest.

Design decisions:

- Issues and pull requests are batched through separate fields (``issue`` and
  ``pullRequest``) rather than the union field, because the point cost of a
  query follows the nodes it may request and the union would charge every issue
  for the pull-request branch as well. A number the typed field does not return
  is retried once through ``issueOrPullRequest``, so an item converted between
  the two families is not misreported as missing.
- Review-thread comments are requested but never paginated. ``totalCount``
  settles ``comment_count`` and the first comment settles the thread's creation
  time, which are the only two comment-derived fields of the row.
- Labels and the milestone are requested for cross-checking against the REST
  snapshot. They stay in the raw response; the normalized stream carries
  relations and review threads only.
- A project board is never read. The ``ProjectV2`` branch of the ``Closer``
  union needs the ``read:project`` token scope, which the read-only repository
  session does not carry, and requesting it fails every query (live smoke run,
  2026-09-06). An item closed by a project therefore keeps its ``closed-by``
  row with the event's time and actor and without a target, and the closing
  project stays uncollected.

Bodies and author logins never leave the raw store. Every value read from the
API is data: it is stored, truncated and counted, never followed.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from tools.corpus.github_snapshot import RateLimitStop, resolve_github_token
from tools.corpus.http_store import FetchResult, HttpStore, canonical_url, utc_now
from tools.corpus.manifest import (
    build_manifest,
    read_jsonl,
    report_status,
    sha256_file,
    status_from,
    write_jsonl,
    write_yaml,
)

GRAPHQL_ENDPOINT = "https://api.github.com/graphql"
TRANSIENT_STATUS = {429, 500, 502, 503, 504}
ERROR_DETAIL_LIMIT = 200

# Page sizes travel as variables so the query text stays a readable constant.
PAGE_VARIABLES = {
    "labelFirst": 20,
    "timelineFirst": 100,
    "threadFirst": 20,
    "commentFirst": 5,
    "closingFirst": 20,
}
CURSOR_KEYS = ("timelineCursor", "threadCursor", "closingCursor")
CONNECTION_OF_CURSOR = {
    "timelineCursor": "timelineItems",
    "threadCursor": "reviewThreads",
    "closingCursor": "closingIssuesReferences",
}

ISSUE_KINDS = {"issue"}
PULL_REQUEST_KINDS = {"pull-request", "pull-request-summary"}

ACTOR_FRAGMENT = """
fragment ActorId on Actor {
  __typename
  ... on User { id }
  ... on Bot { id }
  ... on Organization { id }
  ... on Mannequin { id }
}
"""

REFERENCE_FRAGMENTS = """
fragment ReferencedSubjectRef on ReferencedSubject {
  __typename
  ... on Issue { id number repository { nameWithOwner } }
  ... on PullRequest { id number repository { nameWithOwner } }
}

fragment IssueOrPullRequestRef on IssueOrPullRequest {
  __typename
  ... on Issue { id number repository { nameWithOwner } }
  ... on PullRequest { id number repository { nameWithOwner } }
}

fragment CloserRef on Closer {
  __typename
  ... on Commit { id oid repository { nameWithOwner } }
  ... on PullRequest { id number repository { nameWithOwner } }
}
"""

TIMELINE_SELECTION = """  timelineItems(first: $timelineFirst, after: $timelineCursor, itemTypes: [
    CROSS_REFERENCED_EVENT
    REFERENCED_EVENT
    CONNECTED_EVENT
    DISCONNECTED_EVENT
    MARKED_AS_DUPLICATE_EVENT
    UNMARKED_AS_DUPLICATE_EVENT
    CLOSED_EVENT
    MENTIONED_EVENT
  ]) {
    pageInfo { hasNextPage endCursor }
    nodes {
      __typename
      ... on CrossReferencedEvent { createdAt actor { ...ActorId } source { ...ReferencedSubjectRef } }
      ... on ReferencedEvent { createdAt actor { ...ActorId } commit { id oid } commitRepository { nameWithOwner } }
      ... on ConnectedEvent { createdAt actor { ...ActorId } subject { ...ReferencedSubjectRef } }
      ... on DisconnectedEvent { createdAt actor { ...ActorId } subject { ...ReferencedSubjectRef } }
      ... on MarkedAsDuplicateEvent { createdAt actor { ...ActorId } canonical { ...IssueOrPullRequestRef } }
      ... on UnmarkedAsDuplicateEvent { createdAt actor { ...ActorId } canonical { ...IssueOrPullRequestRef } }
      ... on ClosedEvent { createdAt actor { ...ActorId } closer { ...CloserRef } }
      ... on MentionedEvent { createdAt actor { ...ActorId } }
    }
  }
"""

ISSUE_FRAGMENT = (
    """
fragment IssueRelations on Issue {
  id
  number
  labels(first: $labelFirst) { nodes { id name } }
  milestone { id number }
"""
    + TIMELINE_SELECTION
    + "}\n"
)

PULL_REQUEST_FRAGMENT = (
    """
fragment PullRequestRelations on PullRequest {
  id
  number
  labels(first: $labelFirst) { nodes { id name } }
  milestone { id number }
"""
    + TIMELINE_SELECTION
    + """  reviewThreads(first: $threadFirst, after: $threadCursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      isResolved
      isOutdated
      path
      line
      comments(first: $commentFirst) {
        totalCount
        nodes { id databaseId createdAt author { ...ActorId } }
      }
    }
  }
  closingIssuesReferences(first: $closingFirst, after: $closingCursor) {
    pageInfo { hasNextPage endCursor }
    nodes { id number repository { nameWithOwner } }
  }
}
"""
)

VARIABLE_TYPES = {
    "owner": "String!",
    "name": "String!",
    "labelFirst": "Int!",
    "timelineFirst": "Int!",
    "timelineCursor": "String",
    "threadFirst": "Int!",
    "threadCursor": "String",
    "commentFirst": "Int!",
    "closingFirst": "Int!",
    "closingCursor": "String",
}
ISSUE_VARIABLE_NAMES = ("owner", "name", "labelFirst", "timelineFirst", "timelineCursor")
PULL_REQUEST_VARIABLE_NAMES = (
    *ISSUE_VARIABLE_NAMES,
    "threadFirst",
    "threadCursor",
    "commentFirst",
    "closingFirst",
    "closingCursor",
)


@dataclass(frozen=True)
class QueryShape:
    """The parts of one GraphQL document that depend on the queried field.

    GraphQL rejects a document with an unused variable or an unused fragment, so
    an issue-only query declares neither the review-thread cursors nor the
    pull-request fragment.
    """

    selection: str
    variable_names: tuple[str, ...]
    fragments: str


QUERY_SHAPES = {
    "issue": QueryShape(
        selection="{ __typename ...IssueRelations }",
        variable_names=ISSUE_VARIABLE_NAMES,
        fragments=ACTOR_FRAGMENT + REFERENCE_FRAGMENTS + ISSUE_FRAGMENT,
    ),
    "pullRequest": QueryShape(
        selection="{ __typename ...PullRequestRelations }",
        variable_names=PULL_REQUEST_VARIABLE_NAMES,
        fragments=ACTOR_FRAGMENT + REFERENCE_FRAGMENTS + PULL_REQUEST_FRAGMENT,
    ),
    "issueOrPullRequest": QueryShape(
        selection="{ __typename ...IssueRelations ...PullRequestRelations }",
        variable_names=PULL_REQUEST_VARIABLE_NAMES,
        fragments=ACTOR_FRAGMENT + REFERENCE_FRAGMENTS + ISSUE_FRAGMENT + PULL_REQUEST_FRAGMENT,
    ),
}

# Timeline event type to relation name and the field holding its target.
TIMELINE_RELATIONS = {
    "CrossReferencedEvent": ("cross-referenced", "source"),
    "ReferencedEvent": ("referenced", "commit"),
    "ConnectedEvent": ("connected", "subject"),
    "DisconnectedEvent": ("disconnected", "subject"),
    "MarkedAsDuplicateEvent": ("duplicate-of", "canonical"),
    "UnmarkedAsDuplicateEvent": ("duplicate-cleared", "canonical"),
    "ClosedEvent": ("closed-by", "closer"),
    "MentionedEvent": ("mentioned", None),
}


def build_query(field: str, numbers: Sequence[int]) -> str:
    """Assemble the batched relations query for one field of the repository."""

    shape = QUERY_SHAPES[field]
    header = ", ".join(f"${name}: {VARIABLE_TYPES[name]}" for name in shape.variable_names)
    aliases = "\n".join(
        f"    item{index}: {field}(number: {number}) {shape.selection}"
        for index, number in enumerate(numbers)
    )
    return (
        f"query WorkItemRelations({header}) {{\n"
        "  rateLimit { remaining resetAt cost }\n"
        "  repository(owner: $owner, name: $name) {\n"
        f"{aliases}\n"
        "  }\n"
        "}\n"
        f"{shape.fragments}"
    )


def build_variables(
    field: str, owner: str, name: str, cursors: dict[str, str | None]
) -> dict[str, Any]:
    """Return exactly the variables the field's document declares."""

    values: dict[str, Any] = {
        "owner": owner,
        "name": name,
        **PAGE_VARIABLES,
        **dict.fromkeys(CURSOR_KEYS),
        **cursors,
    }
    return {name_: values[name_] for name_ in QUERY_SHAPES[field].variable_names}


def truncate(value: str, limit: int = ERROR_DETAIL_LIMIT) -> str:
    """Shorten an API-supplied message before it is recorded as a gap detail."""

    text = " ".join(value.split())
    return text if len(text) <= limit else f"{text[:limit]}..."


def reset_epoch(value: str) -> float:
    """Convert the GraphQL ``resetAt`` timestamp to seconds since the epoch."""

    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def read_work_item_numbers(path: Path) -> tuple[set[int], set[int]]:
    """Split the REST work-item stream into issue and pull-request numbers.

    The stream is tens of megabytes, so it is read line by line. Rows of kind
    ``work-item-detail`` repeat both families and are ignored; a number seen as
    a pull request never counts as an issue.
    """

    issues: set[int] = set()
    pulls: set[int] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            number = row.get("number")
            kind = row.get("kind")
            if number is None:
                continue
            if kind in PULL_REQUEST_KINDS:
                pulls.add(int(number))
            elif kind in ISSUE_KINDS:
                issues.add(int(number))
    return issues - pulls, pulls


def item_number(row: dict[str, Any]) -> int | None:
    """Return the work-item number a normalized row belongs to."""

    value = row.get("source_number", row.get("pull_number"))
    return int(value) if value is not None else None


def batches(numbers: Sequence[int], size: int) -> Iterator[list[int]]:
    for start in range(0, len(numbers), size):
        yield list(numbers[start : start + size])


def without_none(row: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in row.items() if value is not None}


def page_state(node: dict[str, Any]) -> tuple[dict[str, str | None], bool]:
    """Return the next cursor of every connection and whether a page remains."""

    cursors: dict[str, str | None] = {}
    more = False
    for cursor_key, connection in CONNECTION_OF_CURSOR.items():
        info = (node.get(connection) or {}).get("pageInfo") or {}
        cursors[cursor_key] = info.get("endCursor")
        more = more or bool(info.get("hasNextPage"))
    return cursors, more


def target_fields(value: dict[str, Any] | None, repository_full_name: str) -> dict[str, Any]:
    """Return the identity of a referenced object, dropping what the API omits."""

    if not value:
        return {}
    fields: dict[str, Any] = {"target_node_id": value.get("id")}
    number = value.get("number")
    if number is not None:
        fields["target_number"] = int(number)
    full_name = (value.get("repository") or {}).get("nameWithOwner")
    if full_name and full_name.lower() != repository_full_name.lower():
        fields["target_repository"] = full_name
    return without_none(fields)


def rows_from_node(node: dict[str, Any], repository_full_name: str) -> list[dict[str, Any]]:
    """Turn one item node into its relation and review-thread rows.

    Only metadata is read. Comment and review bodies and author logins are never
    requested and therefore cannot reach a row.
    """

    number = int(node["number"])
    source = {"kind": "relation", "source_number": number, "source_node_id": node.get("id")}
    rows: list[dict[str, Any]] = []

    for event in (node.get("timelineItems") or {}).get("nodes") or []:
        mapping = TIMELINE_RELATIONS.get(str(event.get("__typename")))
        if mapping is None:
            continue
        relation, field = mapping
        target = event.get(field) if field else None
        if field == "commit" and target:
            # The repository of a referencing commit sits beside the commit.
            target = {**target, "repository": event.get("commitRepository")}
        rows.append(
            without_none(
                source
                | {
                    "relation": relation,
                    "created_at": event.get("createdAt"),
                    "actor_node_id": (event.get("actor") or {}).get("id"),
                }
                | target_fields(target, repository_full_name)
            )
        )

    for thread in (node.get("reviewThreads") or {}).get("nodes") or []:
        comments = thread.get("comments") or {}
        first_comment = next(iter(comments.get("nodes") or []), {})
        # A review thread carries no creation time of its own; its first comment
        # is the earliest page-one entry and establishes it.
        created_at = first_comment.get("createdAt")
        rows.append(
            without_none(
                {
                    "kind": "review-thread",
                    "pull_number": number,
                    "thread_node_id": thread.get("id"),
                    "is_resolved": bool(thread.get("isResolved")),
                    "is_outdated": bool(thread.get("isOutdated")),
                    "path": thread.get("path"),
                    "line": thread.get("line"),
                    "comment_count": int(comments.get("totalCount") or 0),
                    "created_at": created_at,
                }
            )
        )
        rows.append(
            without_none(
                source
                | {
                    "relation": "review-thread",
                    "target_node_id": thread.get("id"),
                    "created_at": created_at,
                }
            )
        )

    for issue in (node.get("closingIssuesReferences") or {}).get("nodes") or []:
        rows.append(
            without_none(source | {"relation": "closes"} | target_fields(issue, repository_full_name))
        )
    return rows


class GraphQLStore(HttpStore):
    """POST access to the GraphQL endpoint on the shared content-addressed store.

    ``HttpStore`` builds GET requests only. Headers, retry policy, raw storage
    and the request journal are inherited unchanged; only the method and the
    request body are added here.
    """

    def _post_once(self, requested: str, data: bytes) -> tuple[FetchResult, bytes]:
        request = urllib.request.Request(
            requested,
            data=data,
            headers=self._headers(requested) | {"Content-Type": "application/json"},
            method="POST",
        )
        observed_at = utc_now()
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return self._store(
                    requested,
                    canonical_url(response.geturl()),
                    observed_at,
                    response.status,
                    response.headers,
                    response.read(),
                )
        except urllib.error.HTTPError as error:
            body = error.read()
            if error.code in TRANSIENT_STATUS:
                raise
            return self._store(
                requested,
                canonical_url(error.geturl()),
                observed_at,
                error.code,
                error.headers,
                body,
            )

    def post_json(
        self,
        url: str,
        payload: dict[str, Any],
        journal: list[dict[str, object]] | None = None,
    ) -> tuple[Any, dict[str, object]]:
        """Post one JSON document, journal the response, and parse it."""

        data = json.dumps(payload, sort_keys=True).encode("utf-8")
        requested = canonical_url(url)
        last_error: Exception | None = None
        for attempt in range(self.retries):
            try:
                result, body = self._post_once(requested, data)
            except (OSError, urllib.error.URLError) as error:
                last_error = error
                self._back_off(attempt, 2**attempt)
                continue
            record = result.as_record()
            if journal is not None:
                journal.append(record)
            if result.status >= 400:
                raise RuntimeError(f"HTTP {result.status} for {result.canonical_url}")
            try:
                return json.loads(body), record
            except json.JSONDecodeError as error:
                raise RuntimeError(f"invalid JSON for {result.canonical_url}: {error}") from error
        raise RuntimeError(f"failed to post {requested}: {last_error}")


class RelationCollector:
    """Run state of one GraphQL stage: store, request journal, gaps and quota."""

    def __init__(
        self,
        raw_root: Path,
        *,
        owner: str,
        name: str,
        token: str | None = None,
        minimum_remaining: int = 100,
        wait_for_reset: bool = False,
    ):
        self.store = GraphQLStore(raw_root, github_token=token)
        self.owner = owner
        self.name = name
        self.full_name = f"{owner}/{name}"
        self.minimum_remaining = minimum_remaining
        self.wait_for_reset = wait_for_reset
        self.requests: list[dict[str, object]] = []
        self.gaps: list[dict[str, Any]] = []
        self.rows: list[dict[str, Any]] = []
        self.resolved: set[int] = set()
        self.points = 0

    def execute(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        payload, _ = self.store.post_json(
            GRAPHQL_ENDPOINT, {"query": query, "variables": variables}, journal=self.requests
        )
        if not isinstance(payload, dict):
            raise RuntimeError("the GraphQL endpoint returned a non-object response")
        for error in payload.get("errors") or []:
            gap: dict[str, Any] = {
                "code": "graphql-error",
                "detail": truncate(str(error.get("message") or error)),
            }
            path = error.get("path")
            if path:
                gap["path"] = ".".join(str(part) for part in path)
            self.gaps.append(gap)
        self._observe_rate_limit((payload.get("data") or {}).get("rateLimit") or {})
        return payload

    def fetch_batch(self, field: str, numbers: list[int]) -> None:
        """Fetch one batch of items and every follow-up page they announce.

        Rows land in ``self.rows`` as they arrive, so a rate-limit stop or a
        request failure keeps the work of every item already resolved.
        """

        payload = self.execute(
            build_query(field, numbers), build_variables(field, self.owner, self.name, {})
        )
        container = (payload.get("data") or {}).get("repository")
        if container is None:
            # A batch without repository data resolves no item, and the per-item
            # fallback would only repeat the same failure once per number.
            self.gaps.append(
                {
                    "code": "graphql-error",
                    "detail": f"no repository data for items {numbers[0]} to {numbers[-1]}",
                }
            )
            return
        for index, number in enumerate(numbers):
            node = container.get(f"item{index}")
            if node is None:
                # The typed field misses an item converted between the families.
                node = self.fetch_item(number, {})
            if node is None:
                self.gaps.append({"code": "item-not-found", "number": number})
                continue
            self.rows.extend(rows_from_node(node, self.full_name))
            self._drain(number, node)
            self.resolved.add(number)

    def fetch_item(self, number: int, cursors: dict[str, str | None]) -> dict[str, Any] | None:
        payload = self.execute(
            build_query("issueOrPullRequest", [number]),
            build_variables("issueOrPullRequest", self.owner, self.name, cursors),
        )
        return ((payload.get("data") or {}).get("repository") or {}).get("item0")

    def _drain(self, number: int, node: dict[str, Any]) -> None:
        """Follow the cursors of one item until every connection is exhausted."""

        cursors, more = page_state(node)
        while more:
            page = self.fetch_item(number, cursors)
            if page is None:
                self.gaps.append({"code": "item-not-found", "number": number})
                break
            self.rows.extend(rows_from_node(page, self.full_name))
            advanced, more = page_state(page)
            # An exhausted connection answers with a null cursor; keeping the
            # previous one stops the next round from restarting at page one.
            advanced = {key: value or cursors[key] for key, value in advanced.items()}
            if advanced == cursors:
                self.gaps.append({"code": "pagination-stall", "number": number})
                break
            cursors = advanced

    def _observe_rate_limit(self, limit: dict[str, Any]) -> None:
        self.points += int(limit.get("cost") or 0)
        remaining = limit.get("remaining")
        if remaining is None or int(remaining) >= self.minimum_remaining:
            return
        reset_at = limit.get("resetAt")
        if not (self.wait_for_reset and reset_at):
            raise RateLimitStop(f"GitHub GraphQL rate limit remaining={remaining}")
        # Sleep past the documented reset instant; the next request starts a fresh window.
        time.sleep(max(0.0, reset_epoch(str(reset_at)) - time.time()) + 5.0)


def deduplicate(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Drop rows an overlapping cursor page repeated, keeping the first."""

    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for row in rows:
        key = json.dumps(row, ensure_ascii=False, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique


def count_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    relations_by_kind: dict[str, int] = {}
    rows_by_item: dict[int, int] = {}
    for row in rows:
        if row["kind"] == "relation":
            relation = str(row["relation"])
            relations_by_kind[relation] = relations_by_kind.get(relation, 0) + 1
        number = item_number(row)
        if number is not None:
            rows_by_item[number] = rows_by_item.get(number, 0) + 1
    return {
        "relations": sum(1 for row in rows if row["kind"] == "relation"),
        "review_threads": sum(1 for row in rows if row["kind"] == "review-thread"),
        "relations_by_kind": dict(sorted(relations_by_kind.items())),
        # Items without a single relation or review thread are absent here.
        "rows_by_item": dict(sorted(rows_by_item.items())),
    }


def collect(
    *,
    owner: str,
    repository: str,
    source_id: str,
    work_items: Path,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
    batch_size: int = 20,
    max_items: int | None = None,
    resume_from: Path | None = None,
    wait_for_reset: bool = False,
) -> dict[str, object]:
    token = resolve_github_token()
    if not token:
        raise RuntimeError(
            "the GitHub GraphQL API rejects unauthenticated requests; "
            "run gh auth login with read-only public-repository access"
        )

    started_at = utc_now()
    issues, pulls = read_work_item_numbers(work_items)
    collector = RelationCollector(
        raw_root, owner=owner, name=repository, token=token, wait_for_reset=wait_for_reset
    )
    if max_items is not None and len(issues) + len(pulls) > max_items:
        kept = set(sorted(issues | pulls)[:max_items])
        issues &= kept
        pulls &= kept
        collector.gaps.append({"code": "max-items-limit", "limit": max_items})
    requested = issues | pulls

    prior_rows = (
        read_jsonl(resume_from) if resume_from is not None and resume_from.exists() else []
    )
    # An item without a single relation leaves no row, so resume re-fetches it.
    covered = {number for number in (item_number(row) for row in prior_rows) if number is not None}
    reused = requested & covered
    collector.rows.extend(row for row in prior_rows if item_number(row) in requested)
    collector.resolved |= reused

    try:
        for field, numbers in (
            ("issue", sorted(issues - covered)),
            ("pullRequest", sorted(pulls - covered)),
        ):
            for chunk in batches(numbers, batch_size):
                collector.fetch_batch(field, chunk)
    except RateLimitStop as error:
        collector.gaps.append({"code": "rate-limit-stop", "detail": str(error)})
    except RuntimeError as error:
        collector.gaps.append({"code": "collection-error", "detail": truncate(str(error))})

    rows = deduplicate(collector.rows)
    rows.sort(
        key=lambda row: (
            str(row["kind"]),
            item_number(row) or 0,
            json.dumps(row, ensure_ascii=False, sort_keys=True),
        )
    )
    write_jsonl(normalized_output, rows)

    counts = {
        "items_requested": len(requested),
        "items_resolved": len(collector.resolved),
        "items_reused_from_prior_run": len(reused),
        **count_rows(rows),
        "graphql_requests": len(collector.requests),
        "graphql_points": collector.points,
    }
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=source_id,
        adapter="tools.corpus.github_relations",
        started_at=started_at,
        finished_at=utc_now(),
        status=status_from(
            collector.gaps,
            expected=counts["items_requested"],
            observed=counts["items_resolved"],
        ),
        requests=collector.requests,
        objects=[
            {
                "kind": "github-relation-stream",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        counts=counts,
        gaps=collector.gaps,
        rights_exceptions=[
            "Comment and review bodies stay in the ignored raw store; the normalized "
            "stream carries relation and review-thread metadata only.",
        ],
        extra={
            "scope": {
                "boundary": "github-graphql-relations-and-review-threads",
                "status_applies_to": "objects.work_items",
                "completion_rule": (
                    "Every issue and pull request of the REST work-item stream resolved "
                    "through the GraphQL API with its relationship timeline, review "
                    "threads and closing references."
                ),
            },
            "repository": {
                "owner": owner,
                "name": repository,
                "graphql_endpoint": GRAPHQL_ENDPOINT,
            },
            "inputs": {
                "work_items": work_items.as_posix(),
                "resume_from": resume_from.as_posix() if resume_from else None,
                "batch_size": batch_size,
            },
        },
    )
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument(
        "--work-items",
        type=Path,
        required=True,
        help="normalized stream of the REST run whose items this stage covers",
    )
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--max-items", type=int)
    parser.add_argument(
        "--resume-from",
        type=Path,
        help="normalized output of an interrupted run whose items are skipped",
    )
    parser.add_argument(
        "--wait-for-reset",
        action="store_true",
        help="sleep until the point budget resets instead of stopping with a gap",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.batch_size < 1 or args.batch_size > 50:
        raise SystemExit("--batch-size must be between 1 and 50")
    manifest = collect(
        owner=args.owner,
        repository=args.repository,
        source_id=args.source_id,
        work_items=args.work_items,
        raw_root=args.raw_root,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
        batch_size=args.batch_size,
        max_items=args.max_items,
        resume_from=args.resume_from,
        wait_for_reset=args.wait_for_reset,
    )
    counts = manifest["counts"]
    return report_status(
        manifest,
        f"{counts['items_resolved']}/{counts['items_requested']} items, "
        f"{counts['relations']} relations, {counts['review_threads']} review threads, "
        f"{len(manifest['gaps'])} gaps",
    )


if __name__ == "__main__":
    raise SystemExit(main())
