"""GraphQL relations stage: offline runs against a fake GraphQL endpoint.

The fake answers POST bodies rather than URLs, because every request of this
stage goes to the single GraphQL endpoint. It reads the aliases out of the query
text, so batching, the typed-field fallback and cursor pagination are all
observable in the recorded requests.
"""

import io
import json
import re
from pathlib import Path
from typing import Any

import pytest

from tools.corpus import github_relations
from tools.corpus.github_relations import (
    build_query,
    build_variables,
    collect,
    read_work_item_numbers,
)

ALIAS_PATTERN = re.compile(r"(item\d+): (issue|pullRequest|issueOrPullRequest)\(number: (\d+)\)")
RESET_AT = "2026-09-06T12:00:00Z"
ACTOR = {"__typename": "User", "id": "U_actor", "login": "person"}
REPOSITORY = {"nameWithOwner": "o/r"}
OTHER_REPOSITORY = {"nameWithOwner": "other/repo"}
EMPTY_PAGE = {"hasNextPage": False, "endCursor": None}


class FakeResponse:
    def __init__(self, body: bytes) -> None:
        self._stream = io.BytesIO(body)
        self.status = 200
        self.headers = {"Content-Type": "application/json"}

    def read(self, size: int | None = None) -> bytes:
        return self._stream.read() if size is None else self._stream.read(size)

    def geturl(self) -> str:
        return github_relations.GRAPHQL_ENDPOINT

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_: object) -> None:
        return None


class FakeGraphQL:
    """Serve fixture nodes for the aliases of one GraphQL POST.

    A fixture paginates one connection at a time, so the page index is the
    highest cursor the request carries.
    """

    def __init__(self) -> None:
        self.pages: dict[int, list[dict[str, Any] | None]] = {}
        self.missing: set[int] = set()
        self.typed_missing: set[int] = set()
        self.errors: list[dict[str, Any]] = []
        self.without_data = False
        self.rate_limit: dict[str, Any] = {"remaining": 4999, "resetAt": RESET_AT, "cost": 1}
        self.rate_limit_after: dict[str, Any] | None = None
        self.requests: list[dict[str, Any]] = []

    def serve(self, number: int, *pages: dict[str, Any] | None) -> None:
        self.pages[number] = list(pages)

    def node(self, field: str, number: int, index: int) -> dict[str, Any] | None:
        if number in self.missing:
            return None
        if field != "issueOrPullRequest" and number in self.typed_missing:
            return None
        pages = self.pages.get(number) or [None]
        return pages[index] if index < len(pages) else None

    def open(self, request: Any, timeout: int | None = None) -> FakeResponse:
        payload = json.loads(request.data.decode("utf-8"))
        variables = payload["variables"]
        self.requests.append(
            {
                "query": payload["query"],
                "variables": variables,
                "headers": {key.lower(): value for key, value in request.headers.items()},
                "method": request.get_method(),
            }
        )
        index = max(
            (int(variables[key]) for key in github_relations.CURSOR_KEYS if variables.get(key)),
            default=0,
        )
        container = {
            alias: self.node(field, int(number), index)
            for alias, field, number in ALIAS_PATTERN.findall(payload["query"])
        }
        limit = self.rate_limit if len(self.requests) == 1 else self.rate_limit_after
        body: dict[str, Any] = {"data": None}
        if not self.without_data:
            body = {"data": {"rateLimit": limit or self.rate_limit, "repository": container}}
        if self.errors:
            body["errors"] = self.errors
        return FakeResponse(json.dumps(body).encode("utf-8"))

    def numbers_requested(self) -> list[int]:
        return [
            int(number)
            for request in self.requests
            for _alias, _field, number in ALIAS_PATTERN.findall(request["query"])
        ]


@pytest.fixture
def graphql(monkeypatch) -> FakeGraphQL:
    fake = FakeGraphQL()
    monkeypatch.setattr(github_relations.urllib.request, "urlopen", fake.open)
    monkeypatch.setattr(github_relations.time, "sleep", lambda _seconds: None)
    monkeypatch.setattr(github_relations, "resolve_github_token", lambda: "test-token")
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    return fake


def event(type_name: str, **fields: Any) -> dict[str, Any]:
    return {
        "__typename": type_name,
        "createdAt": "2020-01-01T00:00:00Z",
        "actor": ACTOR,
        **fields,
    }


def reference(type_name: str, node_id: str, number: int) -> dict[str, Any]:
    return {"__typename": type_name, "id": node_id, "number": number, "repository": REPOSITORY}


ALL_EVENTS = [
    event("CrossReferencedEvent", source=reference("Issue", "I_9", 9)),
    event("ReferencedEvent", commit={"id": "C_1", "oid": "abc123"}, commitRepository=OTHER_REPOSITORY),
    event("ConnectedEvent", subject=reference("PullRequest", "PR_2", 2)),
    event("DisconnectedEvent", subject=reference("PullRequest", "PR_2", 2)),
    event("MarkedAsDuplicateEvent", canonical=reference("Issue", "I_5", 5)),
    event("UnmarkedAsDuplicateEvent", canonical=reference("Issue", "I_5", 5)),
    event("ClosedEvent", closer=reference("PullRequest", "PR_2", 2)),
    event("MentionedEvent"),
]


def connection(nodes: list[dict[str, Any]], page: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"pageInfo": dict(page or EMPTY_PAGE), "nodes": nodes}


def issue_node(
    number: int, node_id: str, events: list[dict[str, Any]], page: dict[str, Any] | None = None
) -> dict[str, Any]:
    return {
        "__typename": "Issue",
        "id": node_id,
        "number": number,
        "timelineItems": connection(events, page),
    }


def review_thread(node_id: str, *, resolved: bool = True, line: int | None = 12) -> dict[str, Any]:
    return {
        "id": node_id,
        "isResolved": resolved,
        "isOutdated": False,
        "path": "Source/Guidelines/en/CO.xml",
        "line": line,
        "comments": {
            "totalCount": 3,
            "nodes": [
                {
                    "id": "PRRC_1",
                    "databaseId": 41,
                    "createdAt": "2021-02-03T10:00:00Z",
                    "author": ACTOR,
                    "body": "untrusted review prose",
                }
            ],
        },
    }


def pull_node(
    number: int,
    node_id: str,
    *,
    events: list[dict[str, Any]] | None = None,
    threads: list[dict[str, Any]] | None = None,
    closing: list[dict[str, Any]] | None = None,
    thread_page: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "__typename": "PullRequest",
        "id": node_id,
        "number": number,
        "timelineItems": connection(events or []),
        "reviewThreads": connection(threads or [], thread_page),
        "closingIssuesReferences": connection(closing or []),
    }


def write_work_items(path: Path, issues: list[int], pulls: list[int]) -> Path:
    rows: list[dict[str, Any]] = [{"kind": "repository", "id": 1}]
    for number in issues:
        rows.append({"kind": "issue", "number": number, "node_id": f"I_{number}"})
        rows.append({"kind": "work-item-detail", "number": number})
    for number in pulls:
        rows.append({"kind": "pull-request-summary", "number": number, "node_id": f"PR_{number}"})
        rows.append({"kind": "pull-request", "number": number})
        rows.append({"kind": "work-item-detail", "number": number})
    rows.append({"kind": "timeline-event", "parent_number": issues[0] if issues else 1})
    path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8"
    )
    return path


def serve_repository(fake: FakeGraphQL) -> None:
    """Two issues and one pull request, with every relation type present once."""

    fake.serve(1, issue_node(1, "I_1", ALL_EVENTS))
    fake.serve(3, issue_node(3, "I_3", []))
    fake.serve(
        2,
        pull_node(
            2,
            "PR_2",
            threads=[review_thread("PRT_1"), review_thread("PRT_2", resolved=False, line=None)],
            closing=[reference("Issue", "I_9", 9)],
        ),
    )


def run(tmp_path: Path, **overrides: Any) -> dict[str, Any]:
    arguments: dict[str, Any] = {
        "owner": "o",
        "repository": "r",
        "source_id": "github-teic-tei-work-items",
        "work_items": write_work_items(tmp_path / "work-items.jsonl", [1, 3], [2]),
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "relations.jsonl",
        "manifest_output": tmp_path / "2026-09-06-relations.yaml",
        "batch_size": 2,
    }
    return collect(**(arguments | overrides))


def read_rows(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def test_read_work_item_numbers_splits_the_stream_by_kind(tmp_path) -> None:
    path = write_work_items(tmp_path / "work-items.jsonl", [1, 3], [2])

    issues, pulls = read_work_item_numbers(path)

    assert issues == {1, 3}
    assert pulls == {2}


def test_build_query_declares_only_the_variables_and_fragments_it_uses() -> None:
    """GraphQL rejects a document with an unused variable or fragment."""

    issue_query = build_query("issue", [7, 8])
    pull_query = build_query("pullRequest", [9])

    assert "item0: issue(number: 7)" in issue_query
    assert "item1: issue(number: 8)" in issue_query
    assert "$threadCursor" not in issue_query
    assert "PullRequestRelations" not in issue_query
    assert "fragment IssueRelations on Issue" in issue_query
    assert "IssueRelations" not in pull_query.replace("PullRequestRelations", "")
    assert set(build_variables("issue", "o", "r", {})) == set(
        github_relations.ISSUE_VARIABLE_NAMES
    )
    assert build_variables("pullRequest", "o", "r", {"threadCursor": "c"})["threadCursor"] == "c"


def test_a_clean_run_over_every_item_is_observable_complete(tmp_path, graphql) -> None:
    serve_repository(graphql)

    manifest = run(tmp_path)

    assert manifest["gaps"] == []
    assert manifest["status"] == "observable-complete"
    assert manifest["counts"]["items_requested"] == 3
    assert manifest["counts"]["items_resolved"] == 3
    assert manifest["adapter"] == {"name": "tools.corpus.github_relations", "version": 2}
    # Two issues in one batch of two, the pull request in its own batch.
    assert len(graphql.requests) == 2
    assert sorted(graphql.numbers_requested()) == [1, 2, 3]
    assert graphql.requests[0]["method"] == "POST"
    assert graphql.requests[0]["headers"]["authorization"] == "Bearer test-token"
    assert graphql.requests[0]["headers"]["x-github-api-version"] == "2022-11-28"


def test_every_relation_type_reaches_the_stream_once(tmp_path, graphql) -> None:
    serve_repository(graphql)

    manifest = run(tmp_path)

    rows = read_rows(tmp_path / "relations.jsonl")
    relations = [row for row in rows if row["kind"] == "relation"]
    assert manifest["counts"]["relations_by_kind"] == {
        "closed-by": 1,
        "closes": 1,
        "connected": 1,
        "cross-referenced": 1,
        "disconnected": 1,
        "duplicate-cleared": 1,
        "duplicate-of": 1,
        "mentioned": 1,
        "referenced": 1,
        "review-thread": 2,
    }
    cross_referenced = next(row for row in relations if row["relation"] == "cross-referenced")
    assert cross_referenced == {
        "kind": "relation",
        "source_number": 1,
        "source_node_id": "I_1",
        "relation": "cross-referenced",
        "created_at": "2020-01-01T00:00:00Z",
        "actor_node_id": "U_actor",
        "target_node_id": "I_9",
        "target_number": 9,
    }
    referenced = next(row for row in relations if row["relation"] == "referenced")
    assert referenced["target_node_id"] == "C_1"
    assert referenced["target_repository"] == "other/repo"
    assert "target_number" not in referenced
    mentioned = next(row for row in relations if row["relation"] == "mentioned")
    assert "target_node_id" not in mentioned


def test_a_project_closer_keeps_the_event_without_a_target(tmp_path, graphql) -> None:
    """Reading a ProjectV2 needs the read:project scope, so the query omits it."""

    graphql.serve(
        1,
        issue_node(1, "I_1", [event("ClosedEvent", closer={"__typename": "ProjectV2"})]),
    )
    graphql.serve(3, issue_node(3, "I_3", []))
    graphql.serve(2, pull_node(2, "PR_2"))

    manifest = run(tmp_path)

    assert "ProjectV2" not in build_query("issue", [1])
    assert manifest["status"] == "observable-complete"
    assert read_rows(tmp_path / "relations.jsonl") == [
        {
            "kind": "relation",
            "source_number": 1,
            "source_node_id": "I_1",
            "relation": "closed-by",
            "created_at": "2020-01-01T00:00:00Z",
            "actor_node_id": "U_actor",
        }
    ]


def test_review_threads_carry_metadata_and_an_own_relation(tmp_path, graphql) -> None:
    serve_repository(graphql)

    run(tmp_path)

    rows = read_rows(tmp_path / "relations.jsonl")
    threads = {row["thread_node_id"]: row for row in rows if row["kind"] == "review-thread"}
    assert threads["PRT_1"] == {
        "kind": "review-thread",
        "pull_number": 2,
        "thread_node_id": "PRT_1",
        "is_resolved": True,
        "is_outdated": False,
        "path": "Source/Guidelines/en/CO.xml",
        "line": 12,
        "comment_count": 3,
        "created_at": "2021-02-03T10:00:00Z",
    }
    # An outdated thread reports no line, and the row omits what the API omits.
    assert threads["PRT_2"] == {
        "kind": "review-thread",
        "pull_number": 2,
        "thread_node_id": "PRT_2",
        "is_resolved": False,
        "is_outdated": False,
        "path": "Source/Guidelines/en/CO.xml",
        "comment_count": 3,
        "created_at": "2021-02-03T10:00:00Z",
    }
    thread_relations = [
        row for row in rows if row["kind"] == "relation" and row["relation"] == "review-thread"
    ]
    assert {row["target_node_id"] for row in thread_relations} == {"PRT_1", "PRT_2"}


def test_no_row_carries_a_body_or_a_login(tmp_path, graphql) -> None:
    """The fixtures supply both; the publication boundary keeps them raw-only."""

    serve_repository(graphql)

    run(tmp_path)

    written = (tmp_path / "relations.jsonl").read_text(encoding="utf-8")
    assert "body" not in written
    assert "login" not in written
    assert "person" not in written
    assert "untrusted" not in written


def test_pagination_follows_the_cursor_of_a_connection(tmp_path, graphql) -> None:
    graphql.serve(
        1,
        issue_node(1, "I_1", ALL_EVENTS[:1], {"hasNextPage": True, "endCursor": "1"}),
        issue_node(1, "I_1", ALL_EVENTS[1:2], {"hasNextPage": False, "endCursor": "2"}),
    )
    graphql.serve(3, issue_node(3, "I_3", []))
    graphql.serve(2, pull_node(2, "PR_2"))

    manifest = run(tmp_path)

    assert manifest["status"] == "observable-complete"
    assert manifest["counts"]["relations_by_kind"] == {"cross-referenced": 1, "referenced": 1}
    follow_up = next(
        request
        for request in graphql.requests
        if "item0: issueOrPullRequest(number: 1)" in request["query"]
    )
    assert follow_up["variables"]["timelineCursor"] == "1"


def test_a_stalled_cursor_stops_the_item_with_a_gap(tmp_path, graphql) -> None:
    graphql.serve(
        1,
        issue_node(1, "I_1", ALL_EVENTS[:1], {"hasNextPage": True, "endCursor": "1"}),
        issue_node(1, "I_1", ALL_EVENTS[1:2], {"hasNextPage": True, "endCursor": None}),
    )
    graphql.serve(3, issue_node(3, "I_3", []))
    graphql.serve(2, pull_node(2, "PR_2"))

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["pagination-stall"]
    assert manifest["status"] == "partial"


def test_an_item_the_api_does_not_return_is_a_gap(tmp_path, graphql) -> None:
    serve_repository(graphql)
    graphql.missing = {3}

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["item-not-found"]
    assert manifest["gaps"][0]["number"] == 3
    assert manifest["status"] == "partial"
    assert manifest["counts"]["items_resolved"] == 2
    assert manifest["counts"]["items_requested"] == 3


def test_a_converted_item_is_recovered_through_the_union_field(tmp_path, graphql) -> None:
    """An item the typed field misses is retried once as issueOrPullRequest."""

    serve_repository(graphql)
    graphql.typed_missing = {3}

    manifest = run(tmp_path)

    assert manifest["gaps"] == []
    assert manifest["status"] == "observable-complete"
    assert any(
        "item0: issueOrPullRequest(number: 3)" in request["query"]
        for request in graphql.requests
    )


def test_a_graphql_error_is_recorded_truncated(tmp_path, graphql) -> None:
    serve_repository(graphql)
    graphql.errors = [{"message": "x" * 400, "path": ["repository", "item1"], "type": "NOT_FOUND"}]

    manifest = run(tmp_path)

    error_gaps = [gap for gap in manifest["gaps"] if gap["code"] == "graphql-error"]
    assert error_gaps
    assert len(error_gaps[0]["detail"]) == github_relations.ERROR_DETAIL_LIMIT + 3
    assert error_gaps[0]["path"] == "repository.item1"
    assert manifest["status"] == "partial"


def test_a_batch_without_data_is_recorded_once_instead_of_per_item(tmp_path, graphql) -> None:
    """The per-item fallback would repeat the same failure for every number."""

    serve_repository(graphql)
    graphql.without_data = True
    graphql.errors = [{"message": "Something went wrong while executing your query."}]

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["graphql-error"] * 4
    assert graphql.errors[0]["message"] in [gap["detail"] for gap in manifest["gaps"]]
    assert "no repository data for items 1 to 3" in [gap["detail"] for gap in manifest["gaps"]]
    assert manifest["counts"]["items_resolved"] == 0
    assert len(graphql.requests) == 2


def test_the_rate_limit_stops_the_run_with_a_gap(tmp_path, graphql) -> None:
    serve_repository(graphql)
    graphql.rate_limit = {"remaining": 5, "resetAt": RESET_AT, "cost": 1}

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["rate-limit-stop"]
    assert manifest["status"] == "partial"
    assert manifest["counts"]["items_resolved"] == 0


def test_a_rate_limit_stop_keeps_the_rows_of_the_items_already_resolved(tmp_path, graphql) -> None:
    serve_repository(graphql)
    graphql.rate_limit_after = {"remaining": 5, "resetAt": RESET_AT, "cost": 1}

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["rate-limit-stop"]
    assert manifest["counts"]["items_resolved"] == 2
    assert {row["source_number"] for row in read_rows(tmp_path / "relations.jsonl")} == {1}


def test_wait_for_reset_sleeps_past_the_reset_instant(tmp_path, graphql, monkeypatch) -> None:
    serve_repository(graphql)
    graphql.rate_limit = {"remaining": 5, "resetAt": RESET_AT, "cost": 2}
    slept: list[float] = []
    monkeypatch.setattr(github_relations.time, "sleep", slept.append)
    monkeypatch.setattr(
        github_relations.time, "time", lambda: github_relations.reset_epoch(RESET_AT) - 60.0
    )

    manifest = run(tmp_path, wait_for_reset=True)

    assert slept == [65.0, 65.0]
    assert manifest["gaps"] == []
    assert manifest["counts"]["graphql_points"] == 4


def test_resume_skips_items_present_in_a_prior_output(tmp_path, graphql) -> None:
    serve_repository(graphql)
    first = run(tmp_path)
    prior = tmp_path / "relations.jsonl"
    graphql.requests.clear()

    manifest = run(tmp_path, resume_from=prior, normalized_output=tmp_path / "second.jsonl")

    assert first["counts"]["items_reused_from_prior_run"] == 0
    assert manifest["counts"]["items_reused_from_prior_run"] == 2
    # Issue 3 produced no row, so a resumed run cannot know it was done.
    assert graphql.numbers_requested() == [3]
    assert manifest["status"] == "observable-complete"
    assert read_rows(tmp_path / "second.jsonl") == read_rows(prior)


def test_an_unauthenticated_run_is_refused(tmp_path, graphql, monkeypatch) -> None:
    monkeypatch.setattr(github_relations, "resolve_github_token", lambda: None)

    with pytest.raises(RuntimeError, match="rejects unauthenticated requests"):
        run(tmp_path)


def test_main_exit_code_and_status_line_follow_the_run(tmp_path, graphql, monkeypatch, capsys) -> None:
    serve_repository(graphql)
    work_items = write_work_items(tmp_path / "work-items.jsonl", [1, 3], [2])
    monkeypatch.setattr(
        "sys.argv",
        [
            "github_relations",
            "--owner",
            "o",
            "--repository",
            "r",
            "--source-id",
            "github-teic-tei-work-items",
            "--work-items",
            str(work_items),
            "--raw-root",
            str(tmp_path / "raw"),
            "--normalized-output",
            str(tmp_path / "relations.jsonl"),
            "--manifest-output",
            str(tmp_path / "run.yaml"),
        ],
    )

    exit_code = github_relations.main()

    assert exit_code == 0
    assert capsys.readouterr().out.startswith(
        "observable-complete: github-teic-tei-work-items -> 3/3 items"
    )
