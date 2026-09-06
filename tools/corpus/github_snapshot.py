"""Acquire an auditable GitHub issue and pull-request snapshot via REST."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import urllib.parse
from pathlib import Path
from typing import Any

from tools.corpus.http_store import HttpStore, utc_now
from tools.corpus.manifest import (
    build_manifest,
    report_status,
    sha256_file,
    status_from,
    write_jsonl,
    write_yaml,
)

LINK_PATTERN = re.compile(r'<([^>]+)>;\s*rel="([^"]+)"')


class RateLimitStop(RuntimeError):
    pass


def next_link(value: str | None) -> str | None:
    if not value:
        return None
    relations = {relation: url for url, relation in LINK_PATTERN.findall(value)}
    return relations.get("next")


def metadata(kind: str, value: dict[str, Any]) -> dict[str, Any]:
    user = value.get("user") or {}
    base = {
        "kind": kind,
        "id": value.get("id"),
        "node_id": value.get("node_id"),
        "number": value.get("number"),
        "url": value.get("url"),
        "html_url": value.get("html_url"),
        "state": value.get("state"),
        "title": value.get("title"),
        "created_at": value.get("created_at"),
        "updated_at": value.get("updated_at"),
        "closed_at": value.get("closed_at"),
        "merged_at": value.get("merged_at"),
        "author_node_id": user.get("node_id"),
        "comments": value.get("comments"),
        "commits": value.get("commits"),
        "review_comments": value.get("review_comments"),
        "changed_files": value.get("changed_files"),
        "labels": [label.get("name") for label in value.get("labels", [])],
        "milestone_node_id": (value.get("milestone") or {}).get("node_id"),
    }
    return {key: item for key, item in base.items() if item is not None}


class GitHubCollector:
    def __init__(
        self,
        raw_root: Path,
        *,
        minimum_remaining: int = 10,
        token: str | None = None,
    ):
        self.store = HttpStore(raw_root, github_token=token)
        self.requests: list[dict[str, object]] = []
        self.minimum_remaining = minimum_remaining

    def get_json(self, url: str) -> tuple[Any, dict[str, object]]:
        payload, record = self.store.fetch_json(url, journal=self.requests)
        remaining = record["headers"].get("x-ratelimit-remaining")  # type: ignore[union-attr]
        if remaining and int(remaining) < self.minimum_remaining:
            raise RateLimitStop(f"GitHub rate limit remaining={remaining}")
        return payload, record

    def paginate(self, url: str) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        current: str | None = url
        while current:
            payload, record = self.get_json(current)
            if not isinstance(payload, list):
                raise RuntimeError(f"expected list from {current}")
            items.extend(payload)
            current = next_link(record["headers"].get("link"))  # type: ignore[union-attr]
        return items


def api_url(owner: str, repository: str, path: str, **query: object) -> str:
    base = f"https://api.github.com/repos/{owner}/{repository}/{path.lstrip('/')}"
    return f"{base}?{urllib.parse.urlencode(query)}" if query else base


def resolve_github_token() -> str | None:
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        completed = subprocess.run(
            ["gh", "auth", "token"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except OSError:
        return None
    return completed.stdout.strip() if completed.returncode == 0 else None


def collect(
    *,
    owner: str,
    repository: str,
    source_id: str,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
    max_items: int | None,
    allow_unauthenticated: bool,
) -> dict[str, object]:
    token = resolve_github_token()
    if not token and not allow_unauthenticated:
        raise RuntimeError(
            "an authenticated GitHub session is required for a complete snapshot; "
            "run gh auth login with read-only public-repository access"
        )

    started_at = utc_now()
    collector = GitHubCollector(raw_root, token=token)
    rows: list[dict[str, Any]] = []
    gaps: list[dict[str, object]] = []

    try:
        repository_record, _ = collector.get_json(api_url(owner, repository, ""))
        rows.append(metadata("repository", repository_record))
        for kind, endpoint, parameters in (
            ("label", "labels", {"per_page": 100}),
            ("milestone", "milestones", {"state": "all", "per_page": 100}),
            ("release", "releases", {"per_page": 100}),
        ):
            for item in collector.paginate(api_url(owner, repository, endpoint, **parameters)):
                rows.append(metadata(kind, item))

        work_items = collector.paginate(
            api_url(
                owner,
                repository,
                "issues",
                state="all",
                sort="created",
                direction="asc",
                per_page=100,
            )
        )
        if max_items is not None and len(work_items) > max_items:
            work_items = work_items[:max_items]
            gaps.append({"code": "max-items-limit", "limit": max_items})

        for work_item in work_items:
            number = int(work_item["number"])
            is_pull_request = "pull_request" in work_item
            rows.append(metadata("pull-request-summary" if is_pull_request else "issue", work_item))

            issue_detail, _ = collector.get_json(api_url(owner, repository, f"issues/{number}"))
            rows.append(metadata("work-item-detail", issue_detail))
            for item in collector.paginate(
                api_url(owner, repository, f"issues/{number}/comments", per_page=100)
            ):
                rows.append(metadata("issue-comment", item) | {"parent_number": number})
            for item in collector.paginate(
                api_url(owner, repository, f"issues/{number}/timeline", per_page=100)
            ):
                rows.append(metadata("timeline-event", item) | {"parent_number": number})

            if is_pull_request:
                pull_detail, _ = collector.get_json(api_url(owner, repository, f"pulls/{number}"))
                rows.append(metadata("pull-request", pull_detail))
                for child_kind, endpoint in (
                    ("review", "reviews"),
                    ("review-comment", "comments"),
                    ("pull-commit", "commits"),
                    ("changed-file", "files"),
                ):
                    for item in collector.paginate(
                        api_url(owner, repository, f"pulls/{number}/{endpoint}", per_page=100)
                    ):
                        rows.append(metadata(child_kind, item) | {"parent_number": number})
    except RateLimitStop as error:
        gaps.append({"code": "rate-limit-stop", "detail": str(error)})
    except RuntimeError as error:
        gaps.append({"code": "collection-error", "detail": str(error)})

    rows.sort(
        key=lambda row: (
            str(row.get("kind", "")),
            int(row.get("number") or row.get("parent_number") or 0),
            int(row.get("id") or 0),
        )
    )
    write_jsonl(normalized_output, rows)
    normalized_hash = sha256_file(normalized_output)
    counts: dict[str, int] = {}
    for row in rows:
        kind = str(row["kind"])
        counts[kind] = counts.get(kind, 0) + 1

    # The GraphQL stage of the bootstrap is not implemented, so every run of
    # this adapter is short of the declared boundary and stays partial.
    gaps.append(
        {
            "code": "graphql-relations-not-yet-collected",
            "detail": "Review-thread and GraphQL-only relationship fields require the second collector stage.",
        }
    )
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=source_id,
        adapter="tools.corpus.github_snapshot",
        started_at=started_at,
        finished_at=utc_now(),
        status=status_from(gaps),
        requests=collector.requests,
        objects=[
            {
                "kind": "github-metadata-stream",
                "path": normalized_output.as_posix(),
                "sha256": normalized_hash,
            }
        ],
        counts=counts | {"http_requests": len(collector.requests)},
        gaps=gaps,
        rights_exceptions=[
            "User-generated bodies are retained only in the ignored raw store; the normalized stream contains metadata."
        ],
    )
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    parser.add_argument("--max-items", type=int)
    parser.add_argument("--allow-unauthenticated", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = collect(
        owner=args.owner,
        repository=args.repository,
        source_id=args.source_id,
        raw_root=args.raw_root,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
        max_items=args.max_items,
        allow_unauthenticated=args.allow_unauthenticated,
    )
    return report_status(
        manifest,
        f"{manifest['counts']['http_requests']} requests, {len(manifest['gaps'])} gaps",
    )


if __name__ == "__main__":
    raise SystemExit(main())
