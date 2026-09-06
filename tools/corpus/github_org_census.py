"""Inventory every public repository exposed by a GitHub organization."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from tools.corpus.github_snapshot import (
    GitHubCollector,
    RateLimitStop,
    resolve_github_token,
)
from tools.corpus.http_store import utc_now
from tools.corpus.manifest import (
    build_manifest,
    report_status,
    sha256_file,
    status_from,
    write_jsonl,
    write_yaml,
)


def repository_metadata(value: dict[str, Any]) -> dict[str, Any]:
    license_value = value.get("license") or {}
    return {
        "schema_version": 1,
        "object_type": "github-repository",
        "id": value.get("id"),
        "node_id": value.get("node_id"),
        "name": value.get("name"),
        "full_name": value.get("full_name"),
        "html_url": value.get("html_url"),
        "clone_url": value.get("clone_url"),
        "fork": bool(value.get("fork", False)),
        "archived": bool(value.get("archived", False)),
        "disabled": bool(value.get("disabled", False)),
        "visibility": value.get("visibility"),
        "default_branch": value.get("default_branch"),
        "created_at": value.get("created_at"),
        "updated_at": value.get("updated_at"),
        "pushed_at": value.get("pushed_at"),
        "license_spdx_id": license_value.get("spdx_id"),
        "open_issues_count": value.get("open_issues_count"),
        "topics": value.get("topics") or [],
    }


def census(
    *,
    organization: str,
    source_id: str,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
) -> dict[str, object]:
    started_at = utc_now()
    collector = GitHubCollector(raw_root, token=resolve_github_token())
    url = (
        f"https://api.github.com/orgs/{organization}/repos"
        "?type=all&sort=full_name&direction=asc&per_page=100"
    )
    gaps: list[dict[str, object]] = []
    repositories: list[dict[str, Any]] = []
    try:
        repositories = collector.paginate(url)
    except RateLimitStop as error:
        gaps.append({"code": "rate-limit-stop", "detail": str(error)})
    except RuntimeError as error:
        gaps.append({"code": "collection-error", "detail": str(error)})
    records = sorted(
        (repository_metadata(repository) for repository in repositories),
        key=lambda row: str(row["full_name"]).lower(),
    )
    write_jsonl(normalized_output, records)
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=source_id,
        adapter="tools.corpus.github_org_census",
        started_at=started_at,
        finished_at=utc_now(),
        status=status_from(gaps),
        requests=collector.requests,
        objects=[
            {
                "kind": "github-organization-repository-census",
                "path": normalized_output.as_posix(),
                "sha256": sha256_file(normalized_output),
            }
        ],
        counts={
            "repositories": len(records),
            "archived": sum(bool(row["archived"]) for row in records),
            "forks": sum(bool(row["fork"]) for row in records),
            "http_requests": len(collector.requests),
            "gaps": len(gaps),
        },
        gaps=gaps,
    )
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--organization", required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = census(
        organization=args.organization,
        source_id=args.source_id,
        raw_root=args.raw_root,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
    )
    return report_status(manifest, f"{manifest['counts']['repositories']} repositories")


if __name__ == "__main__":
    raise SystemExit(main())
