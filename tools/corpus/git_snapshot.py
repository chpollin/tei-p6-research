"""Mirror an upstream Git repository and emit a deterministic tree inventory."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from urllib.parse import urlsplit

from tools.corpus.http_store import utc_now
from tools.corpus.manifest import (
    build_manifest,
    report_status,
    sha256_file,
    status_from,
    write_json,
    write_yaml,
)


def run_git(repository: Path | None, *arguments: str) -> str:
    command = ["git"]
    if repository is not None:
        command.extend(["-C", str(repository)])
    command.extend(arguments)
    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if completed.returncode:
        raise RuntimeError(
            f"git command failed ({completed.returncode}): {' '.join(command)}\n"
            f"{completed.stderr.strip()}"
        )
    return completed.stdout


def repository_slug(url: str) -> str:
    """Return the ``owner-name`` mirror slug of a clone URL.

    A clone URL without both path segments cannot address a mirror directory,
    so it is a control error rather than a per-repository gap.
    """

    segments = [segment for segment in urlsplit(url).path.split("/") if segment]
    if len(segments) < 2:
        raise ValueError(f"clone URL names no owner and repository: {url}")
    owner, name = segments[-2], segments[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return f"{owner}-{name}"


def parse_tree(raw: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for item in raw.split("\0"):
        if not item:
            continue
        metadata, path = item.split("\t", 1)
        mode, object_type, object_id = metadata.split(" ", 2)
        entries.append(
            {
                "mode": mode,
                "object_type": object_type,
                "object_id": object_id,
                "path": path,
            }
        )
    return sorted(entries, key=lambda entry: entry["path"])


def _git_or_gap(
    gaps: list[dict[str, object]], code: str, repository: Path, *arguments: str
) -> str | None:
    """Run a git command whose failure degrades the run instead of ending it."""

    try:
        return run_git(repository, *arguments)
    except RuntimeError as error:
        gaps.append({"code": code, "detail": str(error)})
        return None


def snapshot(
    *,
    repo_url: str,
    source_id: str,
    ref: str,
    raw_root: Path,
    normalized_output: Path,
    manifest_output: Path,
) -> dict[str, object]:
    observed_started = utc_now()
    gaps: list[dict[str, object]] = []
    mirror = raw_root / "git" / f"{repository_slug(repo_url)}.git"
    mirror.parent.mkdir(parents=True, exist_ok=True)

    if mirror.exists():
        if not (mirror / "HEAD").exists():
            raise RuntimeError(f"existing mirror path is not a bare repository: {mirror}")
        run_git(mirror, "remote", "set-url", "origin", repo_url)
        # --prune removes refs deleted upstream; without it a re-run keeps them.
        _git_or_gap(gaps, "mirror-update-failed", mirror, "remote", "update", "--prune")
        action = "updated"
    else:
        run_git(None, "clone", "--mirror", repo_url, str(mirror))
        action = "cloned"

    resolved_ref = run_git(mirror, "rev-parse", f"{ref}^{{commit}}").strip()
    root_tree = run_git(mirror, "show", "-s", "--format=%T", resolved_ref).strip()
    entries = parse_tree(run_git(mirror, "ls-tree", "-r", "-z", "--full-tree", resolved_ref))
    commit_count = int(run_git(mirror, "rev-list", "--all", "--count").strip())
    refs = []
    for line in run_git(
        mirror,
        "for-each-ref",
        "--format=%(refname)%09%(objecttype)%09%(objectname)",
    ).splitlines():
        refname, object_type, object_id = line.split("\t", 2)
        refs.append({"name": refname, "object_type": object_type, "object_id": object_id})
    refs.sort(key=lambda item: item["name"])
    _git_or_gap(gaps, "fsck-failed", mirror, "fsck", "--full", "--no-dangling")

    normalized = {
        "schema_version": 1,
        "source_id": source_id,
        "repository": repo_url,
        "ref_requested": ref,
        "resolved_commit": resolved_ref,
        "root_tree": root_tree,
        "entries": entries,
    }
    write_json(normalized_output, normalized)
    normalized_hash = sha256_file(normalized_output)
    finished = utc_now()

    manifest = build_manifest(
        run_id=manifest_output.stem,
        source_id=source_id,
        adapter="tools.corpus.git_snapshot",
        started_at=observed_started,
        finished_at=finished,
        status=status_from(gaps),
        requests=[
            {
                "kind": "git-mirror",
                "repository": repo_url,
                "action": action,
                "requested_ref": ref,
                "resolved_commit": resolved_ref,
            }
        ],
        objects=[
            {
                "kind": "git-tree-inventory",
                "path": normalized_output.as_posix(),
                "sha256": normalized_hash,
                "root_tree": root_tree,
            }
        ],
        counts={
            "commits_all_refs": commit_count,
            "refs": len(refs),
            "tree_entries": len(entries),
        },
        gaps=gaps,
        rights_exceptions=[
            "The local mirror is not committed; redistribution follows the upstream repository license."
        ],
        extra={"refs": refs, "raw_materialization": str(mirror)},
    )
    write_yaml(manifest_output, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-url", required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--raw-root", type=Path, default=Path("corpus/raw"))
    parser.add_argument("--normalized-output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = snapshot(
        repo_url=args.repo_url,
        source_id=args.source_id,
        ref=args.ref,
        raw_root=args.raw_root,
        normalized_output=args.normalized_output,
        manifest_output=args.manifest_output,
    )
    counts = manifest["counts"]
    return report_status(
        manifest,
        f"{counts['tree_entries']} tree entries, {counts['commits_all_refs']} commits",
    )


if __name__ == "__main__":
    raise SystemExit(main())
