"""Materialize one immutable source file from a pinned Git commit."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def git_output(git_dir: Path, *arguments: str) -> bytes:
    result = subprocess.run(
        ["git", "--git-dir", str(git_dir), *arguments],
        check=True,
        capture_output=True,
    )
    return result.stdout


def materialize(
    git_dir: Path,
    commit: str,
    source_path: str,
    output: Path,
    expected_blob: str | None = None,
) -> tuple[str, int]:
    object_name = f"{commit}:{source_path}"
    blob = git_output(git_dir, "rev-parse", object_name).decode("ascii").strip()
    if expected_blob and blob != expected_blob:
        raise ValueError(
            f"blob mismatch for {object_name}: expected {expected_blob}, got {blob}"
        )
    payload = git_output(git_dir, "cat-file", "blob", blob)
    if output.exists():
        if output.read_bytes() != payload:
            raise FileExistsError(
                f"refusing to overwrite changed immutable source: {output}"
            )
        return blob, len(payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(payload)
    return blob, len(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-dir", type=Path, required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--path", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-blob")
    args = parser.parse_args()
    blob, size = materialize(
        args.git_dir.resolve(),
        args.commit,
        args.path,
        args.output.resolve(),
        args.expected_blob,
    )
    print(f"OK: {args.output} ({size} bytes, blob {blob})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
