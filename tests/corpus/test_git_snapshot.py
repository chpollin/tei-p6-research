"""Git mirror inventory and the organization-wide mirror run."""

import json
import subprocess

import pytest
import yaml

from tools.corpus import git_snapshot
from tools.corpus.git_snapshot import parse_tree, repository_slug, snapshot

REPO_URL = "https://github.com/TEIC/TEI.git"
GIT_OUTPUT = {
    "rev-parse": "113e933e21f016e2655518321e9d10214b8d9fcb\n",
    "show": "8b7fb47e3c8a40600d65dfd4bbf35e8612b4c254\n",
    "ls-tree": (
        "100644 blob aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\tz.xml\0"
        "100644 blob bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\ta.xml\0"
    ),
    "rev-list": "7449\n",
    "for-each-ref": "refs/heads/main\tcommit\tcccccccccccccccccccccccccccccccccccccccc\n",
}


class FakeGit:
    def __init__(self, failing: tuple[str, ...] = ()) -> None:
        self.calls: list[tuple[str, ...]] = []
        self.failing = failing

    def __call__(self, repository, *arguments: str) -> str:
        self.calls.append(arguments)
        command = " ".join(arguments)
        if any(command.startswith(prefix) for prefix in self.failing):
            raise RuntimeError(f"git command failed (1): git {command}")
        return GIT_OUTPUT.get(arguments[0], "")


def run(tmp_path, monkeypatch, failing: tuple[str, ...] = ()) -> tuple[dict, FakeGit]:
    fake = FakeGit(failing)
    monkeypatch.setattr(git_snapshot, "run_git", fake)
    manifest = snapshot(
        repo_url=REPO_URL,
        source_id="teic-tei",
        ref="HEAD",
        raw_root=tmp_path / "raw",
        normalized_output=tmp_path / "normalized.json",
        manifest_output=tmp_path / "manifest.yaml",
    )
    return manifest, fake


def existing_mirror(tmp_path) -> None:
    mirror = tmp_path / "raw" / "git" / "TEIC-TEI.git"
    mirror.mkdir(parents=True)
    (mirror / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")


def test_parse_git_tree_sorts_by_path() -> None:
    assert [entry["path"] for entry in parse_tree(GIT_OUTPUT["ls-tree"])] == ["a.xml", "z.xml"]


def test_repository_slug() -> None:
    assert repository_slug(REPO_URL) == "TEIC-TEI"
    assert repository_slug("https://github.com/TEIC/Stylesheets") == "TEIC-Stylesheets"


@pytest.mark.parametrize(
    "url", ["https://github.com/TEI.git", "https://github.com/", "not-a-url"]
)
def test_repository_slug_rejects_a_url_without_owner_and_name(url) -> None:
    with pytest.raises(ValueError, match="owner and repository"):
        repository_slug(url)


def test_clone_run_is_observable_complete(tmp_path, monkeypatch) -> None:
    manifest, fake = run(tmp_path, monkeypatch)

    assert manifest["status"] == "observable-complete"
    assert manifest["gaps"] == []
    assert manifest["requests"][0]["action"] == "cloned"
    assert ("clone", "--mirror", REPO_URL, str(tmp_path / "raw" / "git" / "TEIC-TEI.git")) in (
        fake.calls
    )
    normalized = json.loads((tmp_path / "normalized.json").read_text(encoding="utf-8"))
    assert [entry["path"] for entry in normalized["entries"]] == ["a.xml", "z.xml"]
    assert manifest["counts"] == {"commits_all_refs": 7449, "refs": 1, "tree_entries": 2}


def test_update_prunes_refs_deleted_upstream(tmp_path, monkeypatch) -> None:
    existing_mirror(tmp_path)

    manifest, fake = run(tmp_path, monkeypatch)

    assert ("remote", "update", "--prune") in fake.calls
    assert manifest["requests"][0]["action"] == "updated"
    assert manifest["status"] == "observable-complete"


def test_a_failed_update_is_a_gap_not_a_silent_success(tmp_path, monkeypatch) -> None:
    existing_mirror(tmp_path)

    manifest, _ = run(tmp_path, monkeypatch, failing=("remote update",))

    assert [gap["code"] for gap in manifest["gaps"]] == ["mirror-update-failed"]
    assert manifest["status"] == "partial"
    assert manifest["counts"]["tree_entries"] == 2
    written = yaml.safe_load((tmp_path / "manifest.yaml").read_text(encoding="utf-8"))
    assert written["status"] == "partial"


def test_a_failed_fsck_is_a_gap(tmp_path, monkeypatch) -> None:
    manifest, _ = run(tmp_path, monkeypatch, failing=("fsck",))

    assert [gap["code"] for gap in manifest["gaps"]] == ["fsck-failed"]
    assert manifest["status"] == "partial"


def test_a_failed_inventory_command_aborts_the_run(tmp_path, monkeypatch) -> None:
    with pytest.raises(RuntimeError, match="git command failed"):
        run(tmp_path, monkeypatch, failing=("rev-parse",))


def test_a_non_bare_mirror_path_is_refused(tmp_path, monkeypatch) -> None:
    (tmp_path / "raw" / "git" / "TEIC-TEI.git").mkdir(parents=True)

    with pytest.raises(RuntimeError, match="not a bare repository"):
        run(tmp_path, monkeypatch)


def test_run_git_reports_the_failing_command(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        git_snapshot.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(
            args, 128, stdout="", stderr="fatal: repository not found\n"
        ),
    )
    with pytest.raises(RuntimeError, match="repository not found"):
        git_snapshot.run_git(None, "clone", "--mirror", REPO_URL)
