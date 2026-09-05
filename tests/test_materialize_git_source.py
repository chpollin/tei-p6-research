"""Tests for immutable source materialization from Git."""

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from materialize_git_source import materialize  # noqa: E402


def git(worktree: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(worktree), *arguments],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def test_materializes_exact_blob_and_refuses_changed_output(tmp_path: Path) -> None:
    worktree = tmp_path / "worktree"
    worktree.mkdir()
    git(worktree, "init")
    git(worktree, "config", "user.email", "test@example.invalid")
    git(worktree, "config", "user.name", "Test")
    source = worktree / "source.md"
    source.write_bytes(b"line one\nline two\n")
    git(worktree, "add", "source.md")
    git(worktree, "commit", "-m", "Add source")
    commit = git(worktree, "rev-parse", "HEAD")
    blob = git(worktree, "rev-parse", f"{commit}:source.md")
    output = tmp_path / "materialized" / "source.md"

    actual_blob, size = materialize(
        worktree / ".git", commit, "source.md", output, blob
    )

    assert actual_blob == blob
    assert size == 18
    assert output.read_bytes() == b"line one\nline two\n"

    output.write_bytes(b"changed\n")
    with pytest.raises(FileExistsError, match="refusing to overwrite"):
        materialize(worktree / ".git", commit, "source.md", output, blob)
