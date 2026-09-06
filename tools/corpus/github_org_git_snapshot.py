"""Mirror every repository in a normalized GitHub organization census."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from tools.corpus.git_snapshot import repository_slug, snapshot
from tools.corpus.http_store import utc_now
from tools.corpus.manifest import (
    build_manifest,
    read_jsonl,
    report_status,
    status_from,
    write_yaml,
)


def mirror_repository(
    repository: dict[str, Any],
    source_id: str,
    raw_root: Path,
    normalized_root: Path,
    manifest_root: Path,
    run_prefix: str,
) -> dict[str, object]:
    url = repository.get("clone_url")
    if not url:
        raise ValueError(f"census row has no clone_url: {repository.get('full_name')}")
    url = str(url)
    slug = repository_slug(url).lower()
    return snapshot(
        repo_url=url,
        source_id=source_id,
        ref="HEAD",
        raw_root=raw_root,
        normalized_output=normalized_root / f"{slug}.json",
        manifest_output=manifest_root / f"{run_prefix}-{slug}.yaml",
    )


def snapshot_organization(
    *,
    source_id: str,
    census: Path,
    workers: int,
    raw_root: Path,
    normalized_root: Path,
    manifest_root: Path,
    manifest_output: Path,
) -> dict[str, object]:
    started_at = utc_now()
    repositories = read_jsonl(census)
    run_prefix = manifest_output.stem
    completed: list[dict[str, object]] = []
    gaps: list[dict[str, object]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                mirror_repository,
                repository,
                source_id,
                raw_root,
                normalized_root,
                manifest_root,
                run_prefix,
            ): repository
            for repository in repositories
        }
        for future in as_completed(futures):
            repository = futures[future]
            try:
                run = future.result()
            except (RuntimeError, ValueError) as error:
                # One unusable repository is a per-repository gap; the run keeps
                # every repository it did mirror.
                gaps.append(
                    {
                        "code": "git-snapshot-failed",
                        "repository": repository.get("full_name"),
                        "detail": str(error),
                    }
                )
                continue
            request = run["requests"][0]  # type: ignore[index]
            counts = run["counts"]  # type: ignore[assignment]
            completed.append(
                {
                    "repository": repository.get("full_name"),
                    "resolved_commit": request["resolved_commit"],  # type: ignore[index]
                    "tree_entries": counts["tree_entries"],  # type: ignore[index]
                    "commits_all_refs": counts["commits_all_refs"],  # type: ignore[index]
                    "run_manifest": (manifest_root / f"{run['run_id']}.yaml").as_posix(),
                }
            )
    completed.sort(key=lambda row: str(row["repository"]).lower())
    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=source_id,
        adapter="tools.corpus.github_org_git_snapshot",
        started_at=started_at,
        finished_at=utc_now(),
        status=status_from(gaps, expected=len(repositories), observed=len(completed)),
        requests={
            "repository_census": census.as_posix(),
            "requested_repositories": len(repositories),
            "workers": workers,
        },
        counts={
            "repositories_requested": len(repositories),
            "repositories_mirrored": len(completed),
            "tree_entries": sum(int(row["tree_entries"]) for row in completed),
            "commits_all_refs_sum": sum(int(row["commits_all_refs"]) for row in completed),
            "gaps": len(gaps),
        },
        gaps=gaps,
        rights_exceptions=[
            "Local mirrors are ignored; redistribution follows each repository's license and file-level exceptions."
        ],
        extra={"repositories": completed},
    )
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", default="teic-public-git-repositories")
    parser.add_argument("--census", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-root", type=Path, required=True)
    parser.add_argument("--manifest-root", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.workers < 1 or args.workers > 8:
        raise SystemExit("workers must be between 1 and 8")
    manifest = snapshot_organization(
        source_id=args.source_id,
        census=args.census,
        workers=args.workers,
        raw_root=args.raw_root,
        normalized_root=args.normalized_root,
        manifest_root=args.manifest_root,
        manifest_output=args.manifest_output,
    )
    counts = manifest["counts"]
    return report_status(
        manifest,
        f"{counts['repositories_mirrored']}/{counts['repositories_requested']} repositories",
    )


if __name__ == "__main__":
    raise SystemExit(main())
