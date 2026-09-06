"""Tests for immutable source materialization from Git.

The first test drives the real `git`, because the object names the tool asks for
are Git's own. The branches below it are exercised against a stub, so that a
refused overwrite, a blob mismatch and the command line are checked without a
repository that would only make the assertion harder to read.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from tools import materialize_git_source
from tools.materialize_git_source import materialize

PAYLOAD = b"line one\nline two\n"
BLOB = "0123456789abcdef0123456789abcdef01234567"


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
    source.write_bytes(PAYLOAD)
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
    assert output.read_bytes() == PAYLOAD

    output.write_bytes(b"changed\n")
    with pytest.raises(FileExistsError, match="refusing to overwrite"):
        materialize(worktree / ".git", commit, "source.md", output, blob)


@pytest.fixture
def stub_git(monkeypatch: pytest.MonkeyPatch) -> list[tuple[str, ...]]:
    """A `git` that answers `rev-parse` with BLOB and `cat-file` with PAYLOAD."""
    calls: list[tuple[str, ...]] = []

    def fake_output(git_dir: Path, *arguments: str) -> bytes:
        calls.append(arguments)
        if arguments[0] == "rev-parse":
            return BLOB.encode("ascii") + b"\n"
        return PAYLOAD

    monkeypatch.setattr(materialize_git_source, "git_output", fake_output)
    return calls


def test_a_blob_other_than_the_expected_one_is_never_written(
    tmp_path: Path, stub_git: list[tuple[str, ...]]
) -> None:
    """The pin is the identity of the source, so a mismatch writes nothing."""
    output = tmp_path / "source.md"
    with pytest.raises(ValueError, match="blob mismatch"):
        materialize(tmp_path / "git", "c0ffee", "source.md", output, "f" * 40)
    assert not output.exists()
    assert [call[0] for call in stub_git] == ["rev-parse"]


def test_materializing_the_same_bytes_again_changes_nothing(
    tmp_path: Path, stub_git: list[tuple[str, ...]]
) -> None:
    output = tmp_path / "nested" / "source.md"
    first = materialize(tmp_path / "git", "c0ffee", "source.md", output, BLOB)
    written = output.stat().st_mtime_ns
    second = materialize(tmp_path / "git", "c0ffee", "source.md", output, BLOB)
    assert first == second == (BLOB, len(PAYLOAD))
    assert output.stat().st_mtime_ns == written
    assert output.read_bytes() == PAYLOAD


def test_the_command_line_materializes_and_reports(
    tmp_path: Path, stub_git: list[tuple[str, ...]], capsys: pytest.CaptureFixture
) -> None:
    output = tmp_path / "source.md"
    argv = [
        "materialize_git_source.py",
        "--git-dir", str(tmp_path / "git"),
        "--commit", "c0ffee",
        "--path", "source.md",
        "--output", str(output),
        "--expected-blob", BLOB,
    ]
    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(sys, "argv", argv)
        assert materialize_git_source.main() == 0
    assert output.read_bytes() == PAYLOAD
    assert f"{len(PAYLOAD)} bytes, blob {BLOB}" in capsys.readouterr().out


def test_git_output_passes_the_git_directory_through(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The tool never runs in a working tree, so --git-dir carries the repository."""
    seen: dict[str, object] = {}

    class Result:
        stdout = b"out"

    def fake_run(command, **kwargs):
        seen["command"] = command
        seen["kwargs"] = kwargs
        return Result()

    monkeypatch.setattr(materialize_git_source.subprocess, "run", fake_run)
    assert materialize_git_source.git_output(Path("/repo.git"), "rev-parse", "x") == b"out"
    assert seen["command"][:3] == ["git", "--git-dir", str(Path("/repo.git"))]
    assert seen["kwargs"]["check"] is True
