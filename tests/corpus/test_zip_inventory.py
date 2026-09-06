"""ZIP member inventory, including an archive that cannot be read."""

import json
from zipfile import ZipFile

from tools.corpus.zip_inventory import inventory


def build_archive(path) -> None:
    with ZipFile(path, "w") as archive:
        archive.writestr("release/", "")
        archive.writestr("release/guidelines.xml", "<TEI/>")
        archive.writestr("release/readme.txt", "notes")


def run(tmp_path, archive) -> dict:
    return inventory(
        source_id="tei-p5-4.12.0-release-members",
        archive=archive,
        normalized_output=tmp_path / "members.json",
        manifest_output=tmp_path / "run.yaml",
    )


def test_a_readable_archive_is_observable_complete(tmp_path) -> None:
    archive = tmp_path / "release.zip"
    build_archive(archive)

    manifest = run(tmp_path, archive)

    assert manifest["status"] == "observable-complete"
    assert manifest["gaps"] == []
    assert manifest["counts"]["members"] == 3
    assert manifest["counts"]["files"] == 2
    assert manifest["counts"]["directories"] == 1
    assert manifest["counts"]["suffixes"] == {".txt": 1, ".xml": 1}
    normalized = json.loads((tmp_path / "members.json").read_text(encoding="utf-8"))
    assert [entry["path"] for entry in normalized["entries"]] == [
        "release/",
        "release/guidelines.xml",
        "release/readme.txt",
    ]


def test_a_truncated_archive_is_a_partial_manifest_with_a_gap(tmp_path) -> None:
    archive = tmp_path / "release.zip"
    build_archive(archive)
    archive.write_bytes(archive.read_bytes()[: len(archive.read_bytes()) // 2])

    manifest = run(tmp_path, archive)

    assert manifest["status"] == "partial"
    assert [gap["code"] for gap in manifest["gaps"]] == ["archive-unreadable"]
    assert manifest["counts"]["members"] == 0
    assert (tmp_path / "members.json").exists()
    assert (tmp_path / "run.yaml").exists()
