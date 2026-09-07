"""Byte-exact clone exports and rejection of unsafe or incompatible destinations."""

import json
import shutil
import stat
from pathlib import Path
from types import SimpleNamespace

import pytest

from tools import export_guidelines as exporter
from tools import ingest_git_blobs as shared
from tools import ingest_guidelines as baseline

ROOT = Path(__file__).parents[1]


@pytest.fixture(scope="module")
def clean_inputs(tmp_path_factory):
    root = tmp_path_factory.mktemp("export-inputs")
    for relative in (shared.LOCK, shared.UPSTREAM, shared.INVENTORY, baseline.MANIFEST,
                     baseline.MEMBERS, baseline.MEMBERS_MANIFEST):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, path)
    for relative in ("10_markdown/documents", "20_distillates/documents"):
        shutil.copytree(ROOT / relative, root / relative)
    return root


def test_complete_export_without_mirror_and_repeat_check(clean_inputs, tmp_path):
    assert not (clean_inputs / shared.GIT_DIR).exists()
    assert not (clean_inputs / "00_sources").exists()
    output = tmp_path / "xml"
    inventory = exporter.export(clean_inputs, output)
    assert len(inventory["files"]) == 888
    assert inventory["not_exported_dependencies"]
    assert json.loads((output / exporter.INVENTORY).read_text(encoding="utf-8")) == inventory
    for entry in inventory["files"]:
        data = (output / entry["path"]).read_bytes()
        assert shared.sha256(data) == entry["sha256"]
        assert shared.blob_id(data) == entry["git_blob_id"]
    assert exporter.export(clean_inputs, output) == inventory
    assert exporter.export(clean_inputs, output, check=True) == inventory


@pytest.fixture
def small_payloads(monkeypatch):
    """Filesystem edge cases need only two products after the admission boundary."""
    monkeypatch.setattr(exporter, "checked_payloads", lambda root: (
        {"files": ["P5/a.xml", "P5/z.xml"]},
        {"P5/a.xml": b"<a/>\n", "P5/z.xml": b"<z/>\n"},
    ))


def test_conflict_preflight_writes_nothing(small_payloads, tmp_path):
    (tmp_path / "P5").mkdir()
    conflict = tmp_path / "P5/z.xml"
    conflict.write_bytes(b"user data")
    with pytest.raises(ValueError, match="incompatible"):
        exporter.export(ROOT, tmp_path)
    assert conflict.read_bytes() == b"user data"
    assert not (tmp_path / "P5/a.xml").exists()
    assert not (tmp_path / exporter.INVENTORY).exists()


def test_check_does_not_create_missing_output(small_payloads, tmp_path):
    target = tmp_path / "absent"
    with pytest.raises(FileNotFoundError):
        exporter.export(ROOT, target, check=True)
    assert not target.exists()


@pytest.mark.parametrize("relative", ["../escape.xml", "/absolute.xml", "C:/escape.xml", "P5/../../escape.xml", "P5\\escape.xml"])
def test_unsafe_paths_rejected(tmp_path, relative):
    with pytest.raises(ValueError, match="unsafe"):
        exporter.safe_destination(tmp_path, relative)


def test_symlink_destination_rejected(small_payloads, tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    target = tmp_path / "link"
    try:
        target.symlink_to(outside, target_is_directory=True)
    except OSError:
        pytest.skip("Platform does not permit symlink creation")
    with pytest.raises(ValueError, match="symlink"):
        exporter.export(ROOT, target)
    assert not list(outside.iterdir())


def test_reparse_destination_rejected(tmp_path, monkeypatch):
    """Exercise Windows junction rejection even without symlink privileges."""
    target = tmp_path / "junction"
    original = Path.lstat
    monkeypatch.setattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 1024, raising=False)
    monkeypatch.setattr(Path, "lstat", lambda path: SimpleNamespace(
        st_mode=stat.S_IFDIR, st_file_attributes=1024
    ) if path == target else original(path))
    with pytest.raises(ValueError, match="reparse"):
        exporter.safe_destination(target, "P5/a.xml")


def test_file_as_parent_rejected_before_writes(small_payloads, tmp_path):
    (tmp_path / "P5").write_bytes(b"user file")
    with pytest.raises(ValueError, match="non-directory"):
        exporter.export(ROOT, tmp_path)
    assert (tmp_path / "P5").read_bytes() == b"user file"
    assert not (tmp_path / exporter.INVENTORY).exists()


@pytest.mark.parametrize("missing", [False, True])
def test_corrupt_or_missing_input_fails_before_export(clean_inputs, tmp_path, missing):
    path = clean_inputs / "10_markdown/documents/tei-p5-guidelines-use-4.12.0.md"
    original = path.read_bytes()
    try:
        if missing:
            path.unlink()
        else:
            path.write_bytes(original.replace(b"<", b"!", 1))
        with pytest.raises((ValueError, FileNotFoundError)):
            exporter.export(clean_inputs, tmp_path / "export")
        assert not (tmp_path / "export").exists()
    finally:
        path.write_bytes(original)


def test_cli_check_failure_returns_nonzero(small_payloads, tmp_path, monkeypatch):
    monkeypatch.setattr("sys.argv", ["export_guidelines", "--output", str(tmp_path), "--check"])
    assert exporter.main() == 1
