"""Organization-wide mirror run: one bad repository may not discard the run."""

import json

import pytest
import yaml

from tools.corpus import github_org_git_snapshot
from tools.corpus.github_org_git_snapshot import snapshot_organization


def census_file(tmp_path, rows: list[dict]) -> "object":
    path = tmp_path / "census.jsonl"
    path.write_text(
        "".join(json.dumps(row) + "\n" for row in rows),
        encoding="utf-8",
    )
    return path


def install_fake_snapshot(monkeypatch) -> list[str]:
    mirrored: list[str] = []

    def fake_snapshot(*, repo_url, source_id, ref, raw_root, normalized_output, manifest_output):
        mirrored.append(repo_url)
        return {
            "run_id": manifest_output.stem,
            "requests": [{"resolved_commit": "cccccccccccccccccccccccccccccccccccccccc"}],
            "counts": {"tree_entries": 2, "commits_all_refs": 5},
        }

    monkeypatch.setattr(github_org_git_snapshot, "snapshot", fake_snapshot)
    return mirrored


def run(tmp_path, rows: list[dict]) -> dict:
    return snapshot_organization(
        source_id="teic-public-git-repositories",
        census=census_file(tmp_path, rows),
        workers=1,
        raw_root=tmp_path / "raw",
        normalized_root=tmp_path / "normalized",
        manifest_root=tmp_path / "manifests",
        manifest_output=tmp_path / "run.yaml",
    )


def test_a_complete_run_is_observable_complete(tmp_path, monkeypatch) -> None:
    install_fake_snapshot(monkeypatch)

    manifest = run(
        tmp_path,
        [{"full_name": "TEIC/TEI", "clone_url": "https://github.com/TEIC/TEI.git"}],
    )

    assert manifest["status"] == "observable-complete"
    assert manifest["gaps"] == []
    assert manifest["repositories"][0]["run_manifest"] == (
        (tmp_path / "manifests" / "run-teic-tei.yaml").as_posix()
    )


@pytest.mark.parametrize(
    "broken",
    [
        {"full_name": "TEIC/Broken", "clone_url": "https://github.com/Broken.git"},
        {"full_name": "TEIC/Broken"},
    ],
)
def test_one_unusable_clone_url_becomes_a_gap(tmp_path, monkeypatch, broken) -> None:
    mirrored = install_fake_snapshot(monkeypatch)

    manifest = run(
        tmp_path,
        [{"full_name": "TEIC/TEI", "clone_url": "https://github.com/TEIC/TEI.git"}, broken],
    )

    assert mirrored == ["https://github.com/TEIC/TEI.git"]
    assert manifest["status"] == "partial"
    assert [gap["code"] for gap in manifest["gaps"]] == ["git-snapshot-failed"]
    assert manifest["gaps"][0]["repository"] == "TEIC/Broken"
    assert manifest["counts"] == {
        "repositories_requested": 2,
        "repositories_mirrored": 1,
        "tree_entries": 2,
        "commits_all_refs_sum": 5,
        "gaps": 1,
    }
    written = yaml.safe_load((tmp_path / "run.yaml").read_text(encoding="utf-8"))
    assert written["status"] == "partial"
    assert len(written["repositories"]) == 1


def test_a_failed_mirror_becomes_a_gap(tmp_path, monkeypatch) -> None:
    def failing_snapshot(**kwargs):
        raise RuntimeError("git command failed (128): fatal: repository not found")

    monkeypatch.setattr(github_org_git_snapshot, "snapshot", failing_snapshot)

    manifest = run(
        tmp_path,
        [{"full_name": "TEIC/TEI", "clone_url": "https://github.com/TEIC/TEI.git"}],
    )

    assert manifest["status"] == "partial"
    assert "repository not found" in manifest["gaps"][0]["detail"]
