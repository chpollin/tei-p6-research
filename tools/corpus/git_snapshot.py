"""Mirror an upstream Git repository and emit a deterministic tree inventory."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from urllib.parse import urlsplit

from tools.corpus.http_store import utc_now
from tools.corpus.manifest import sha256_file, write_json, write_yaml


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
    path = urlsplit(url).path.rstrip("/")
    name = path.rsplit("/", 1)[-1]
    if name.endswith(".git"):
        name = name[:-4]
    owner = path.strip("/").split("/")[-2]
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
    mirror = raw_root / "git" / f"{repository_slug(repo_url)}.git"
    mirror.parent.mkdir(parents=True, exist_ok=True)

    if mirror.exists():
        if not (mirror / "HEAD").exists():
            raise RuntimeError(f"existing mirror path is not a bare repository: {mirror}")
        run_git(mirror, "remote", "set-url", "origin", repo_url)
        run_git(mirror, "remote", "update")
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
    run_git(mirror, "fsck", "--full", "--no-dangling")

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

    manifest: dict[str, object] = {
        "schema_version": 1,
        "run_id": manifest_output.stem,
        "source_id": source_id,
        "started_at": observed_started,
        "finished_at": finished,
        "status": "observable-complete",
        "adapter": {"name": "tools.corpus.git_snapshot", "version": 1},
        "requests": [
            {
                "kind": "git-mirror",
                "repository": repo_url,
                "action": action,
                "requested_ref": ref,
                "resolved_commit": resolved_ref,
            }
        ],
        "objects": [
            {
                "kind": "git-tree-inventory",
                "path": normalized_output.as_posix(),
                "sha256": normalized_hash,
                "root_tree": root_tree,
            }
        ],
        "counts": {
            "commits_all_refs": commit_count,
            "refs": len(refs),
            "tree_entries": len(entries),
        },
        "refs": refs,
        "gaps": [],
        "rights_exceptions": [
            "The local mirror is not committed; redistribution follows the upstream repository license."
        ],
        "raw_materialization": str(mirror),
    }
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
    print(
        f"OK: {manifest['source_id']} -> "
        f"{manifest['counts']['tree_entries']} tree entries, "  # type: ignore[index]
        f"{manifest['counts']['commits_all_refs']} commits"  # type: ignore[index]
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
