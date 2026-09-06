"""Integrity and immutable-admission checks using inert synthetic XML."""

import json
from pathlib import Path

import pytest
import yaml

from tools import ingest_text_identity as ingest

XML = '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://example.invalid/never-fetch"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="anchor">
  <desc xml:lang="fr">Texte conservé.</desc>
  <desc xml:lang="en">One  <att>xml:id</att>\n    point.</desc>
  <remarks xml:lang="en"><p>Keep <code>α</code> unchanged.</p></remarks>
  <egXML><anchor xml:id="example"/></egXML>
</elementSpec>'''.encode()


@pytest.fixture
def small_spec(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ingest, "SPECS", {"anchor": (ingest.blob_id(XML), len(XML))})


def test_complete_xml_and_normalized_readings_survive(small_spec: None) -> None:
    output = ingest.representation("anchor", XML)
    assert ingest.embedded_source("anchor", output) == XML
    assert b"One xml:id point. ^r1" in output
    assert "Keep α unchanged. ^r2".encode() in output
    assert "Texte conservé.".encode() in output
    assert b"https://example.invalid/never-fetch" in output
    assert ingest.reading_blocks(XML) == [
        ("/elementSpec[1]/desc[2]", "One xml:id point."),
        ("/elementSpec[1]/remarks[1]/p[1]", "Keep α unchanged."),
    ]


def test_embedded_xml_tampering_is_rejected(small_spec: None) -> None:
    output = ingest.representation("anchor", XML).replace(b"One  ", b"Two  ")
    with pytest.raises(ValueError, match="admitted Git blob"):
        ingest.embedded_source("anchor", output)


def test_changed_immutable_file_is_never_overwritten(tmp_path: Path) -> None:
    target = tmp_path / "source.md"
    target.write_bytes(b"original")
    with pytest.raises(ValueError, match="refusing to overwrite"):
        ingest.immutable_output(target, b"changed", check=False)
    assert target.read_bytes() == b"original"


def test_xml_entity_declarations_are_rejected() -> None:
    with pytest.raises(ValueError, match="DTD/entity"):
        ingest.reading_blocks(b'<!DOCTYPE x [<!ENTITY e "bad">]><x>&e;</x>')


def test_admission_check_works_without_ignored_originals_and_detects_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, small_spec: None,
) -> None:
    inventory = {"entries": [
        {"path": "P5/Source/Specs/anchor.xml", "object_id": ingest.blob_id(XML)},
        *[{"path": path, "object_id": blob} for path, blob in ingest.LICENSES.items()],
    ]}
    inventory_bytes = json.dumps(inventory).encode()
    monkeypatch.setattr(ingest, "INVENTORY_HASH", ingest.sha256(inventory_bytes))
    inputs = {
        ingest.LOCK: yaml.safe_dump({"release": {"resolved_full_commit_sha": ingest.COMMIT}}).encode(),
        ingest.UPSTREAM: b"status: observable-complete\n",
        ingest.INVENTORY: inventory_bytes,
    }
    for relative, payload in inputs.items():
        destination = tmp_path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)

    def fake_materialize(git_dir, commit, source_path, output, expected_blob):
        assert commit == ingest.COMMIT
        assert expected_blob == ingest.blob_id(XML)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(XML)

    monkeypatch.setattr(ingest, "materialize", fake_materialize)
    ingest.run(tmp_path)
    _, original, representation = ingest.paths("anchor")
    before_manifest = (tmp_path / ingest.MANIFEST).read_bytes()
    (tmp_path / original).unlink()
    ingest.run(tmp_path, check=True)
    assert not (tmp_path / original).exists()
    assert (tmp_path / ingest.MANIFEST).read_bytes() == before_manifest

    rendered = tmp_path / representation
    rendered.write_bytes(rendered.read_bytes().replace(b"One xml:id point. ^r1", b"Wrong statement. ^r1"))
    with pytest.raises(ValueError, match="refusing to overwrite"):
        ingest.run(tmp_path, check=True)


def test_check_requires_representation_without_creating_it(tmp_path: Path) -> None:
    target = tmp_path / "missing.md"
    with pytest.raises(FileNotFoundError):
        ingest.immutable_output(target, b"new", check=True)
    assert not target.exists()
