"""Admission of locked Git blobs, driven against inert synthetic XML.

The mirror is stubbed at `git_output`, the way `test_materialize_git_source.py`
does it, so the admission chain runs end to end without a repository. The XML
fixtures are synthetic because the checks here are about the converter's own
boundaries, which the released P5 sources do not exercise.
"""

import json
from pathlib import Path

import pytest
import yaml

from tools import ingest_git_blobs as ingest
from tools import materialize_git_source
from tools.ingest_git_blobs import Admission, Run

SPEC_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://example.invalid/never-fetch"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="anchor">
  <desc xml:lang="fr">Texte conservé.</desc>
  <desc xml:lang="en">One  <att>xml:id</att>\n    point.</desc>
  <remarks xml:lang="en"><p>Keep <code>α</code> unchanged.</p></remarks>
  <egXML><anchor xml:id="example"/></egXML>
</elementSpec>'''.encode()

CHAPTER_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<div xmlns="http://www.tei-c.org/ns/1.0" xmlns:xi="http://www.w3.org/2001/XInclude" type="div1" xml:id="SY">
  <head>Synthetic chapter</head>
  <p>First paragraph, with an <egXML xmlns="http://www.tei-c.org/ns/Examples"><div><head>Example head</head><p>Example prose.</p></div></egXML> example inside it.</p>
  <div type="div2" xml:id="SYSUB">
    <head>Nested heading</head>
    <p>Second paragraph, with a list.<list><item>α</item></list></p>
    <xi:include href="never-resolved.xml"/>
  </div>
  <egXML xmlns="http://www.tei-c.org/ns/Examples"><persName ref="a &gt; b">Standalone</persName></egXML>
</div>'''.encode()

SPEC = Admission(
    git_path="P5/Source/Specs/anchor.xml",
    blob=ingest.blob_id(SPEC_XML),
    size=len(SPEC_XML),
    slug="tei-p5-anchor-9.9.9",
    heading="anchor",
    title="Synthetic anchor specification",
    form="spec",
)
CHAPTER = Admission(
    git_path="P5/Source/Guidelines/en/SY-Synthetic.xml",
    blob=ingest.blob_id(CHAPTER_XML),
    size=len(CHAPTER_XML),
    slug="tei-p5-guidelines-sy-9.9.9",
    heading="Synthetic chapter",
    title="Synthetic Guidelines chapter",
    form="chapter",
)
RUN = Run(
    run_id="9999-01-01-synthetic-admission",
    date="9999-01-01",
    adapter="tools.ingest_git_blobs",
    version=1,
    manifest="sources/manifests/9999-01-01-synthetic-admission.yaml",
    boundary="Two synthetic blobs",
    status_applies_to="the two synthetic blobs only",
    known_limits=("Synthetic fixture.",),
    admissions=(SPEC, CHAPTER),
)
PAYLOADS = {SPEC.blob: SPEC_XML, CHAPTER.blob: CHAPTER_XML}


@pytest.fixture
def vault(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A root carrying the control-plane inputs the admission reconciles against."""
    inventory = {"entries": [
        {"path": SPEC.git_path, "object_id": SPEC.blob},
        {"path": CHAPTER.git_path, "object_id": CHAPTER.blob},
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

    def fake_git(git_dir: Path, *arguments: str) -> bytes:
        if arguments[0] == "rev-parse":
            path = arguments[1].split(":", 1)[1]
            blob = next(a.blob for a in RUN.admissions if a.git_path == path)
            return blob.encode("ascii") + b"\n"
        return PAYLOADS[arguments[2]]

    monkeypatch.setattr(materialize_git_source, "git_output", fake_git)
    return tmp_path


def test_both_forms_are_admitted_and_reconcile_without_the_mirror(vault: Path) -> None:
    ingest.admit(vault, RUN)
    manifest = yaml.safe_load((vault / RUN.manifest).read_text(encoding="utf-8"))
    assert [entry["representation_path"] for entry in manifest["admissions"]] == [
        SPEC.rendered, CHAPTER.rendered
    ]
    assert manifest["admissions"][0]["english_reading_blocks"] == 2
    assert manifest["admissions"][1]["source_blocks"] == 6
    assert manifest["counts"]["original_bytes"] == len(SPEC_XML) + len(CHAPTER_XML)

    for admission in RUN.admissions:
        rendered = (vault / admission.rendered).read_bytes()
        assert ingest.embedded_source(admission, rendered) == PAYLOADS[admission.blob]
        (vault / admission.original).unlink()
    before = (vault / RUN.manifest).read_bytes()
    ingest.admit(vault, RUN, check=True)
    assert (vault / RUN.manifest).read_bytes() == before
    assert not (vault / SPEC.original).exists()


def test_a_tampered_representation_fails_the_check(vault: Path) -> None:
    ingest.admit(vault, RUN)
    rendered = vault / CHAPTER.rendered
    rendered.write_bytes(rendered.read_bytes().replace(b"Synthetic chapter", b"Rewritten chapter"))
    with pytest.raises(ValueError, match="admitted Git blob"):
        ingest.admit(vault, RUN, check=True)


def test_a_changed_representation_is_never_overwritten(vault: Path) -> None:
    ingest.admit(vault, RUN)
    rendered = vault / SPEC.rendered
    rendered.write_bytes(rendered.read_bytes().replace(b"One xml:id point. ^r1", b"Wrong. ^r1"))
    with pytest.raises(ValueError, match="refusing to overwrite"):
        ingest.admit(vault, RUN)


def test_the_complete_source_and_normalized_readings_survive() -> None:
    output = ingest.representation(RUN, SPEC, SPEC_XML)
    assert ingest.embedded_source(SPEC, output) == SPEC_XML
    assert b"One xml:id point. ^r1" in output
    assert "Keep α unchanged. ^r2".encode() in output
    assert "Texte conservé.".encode() in output
    assert b"https://example.invalid/never-fetch" in output
    assert ingest.reading_blocks(SPEC_XML) == [
        ("/elementSpec[1]/desc[2]", "One xml:id point."),
        ("/elementSpec[1]/remarks[1]/p[1]", "Keep α unchanged."),
    ]


def test_a_class_specification_locates_its_readings_under_its_own_root() -> None:
    """The pilot only admitted elementSpec files, so the root tag is read, not assumed."""
    payload = SPEC_XML.replace(b"elementSpec", b"classSpec")
    assert [locator for locator, _ in ingest.reading_blocks(payload)] == [
        "/classSpec[1]/desc[2]",
        "/classSpec[1]/remarks[1]/p[1]",
    ]


def test_chapter_units_are_headings_and_paragraphs_in_document_order() -> None:
    blocks = ingest.source_blocks(CHAPTER_XML)
    assert [locator for locator, _ in blocks] == [
        "/div[1]/head[1]",
        "/div[1]/p[1]",
        "/div[1]/div[1]/head[1]",
        "/div[1]/div[1]/p[1]",
        "/div[1]/div[1]/include[1]",
        "/div[1]/egXML[1]",
    ]
    bodies = [body for _, body in blocks]
    assert bodies[0] == "```xml\n<head>Synthetic chapter</head>\n```\n"
    # A div inside an encoded example mints no unit; its prose stays in the
    # paragraph that carries the example, so the units stay disjoint.
    assert bodies[1].count("Example head") == 1
    assert not any("Example head" in body for body in bodies if body is not bodies[1])
    assert bodies[3].endswith("<list><item>α</item></list></p>\n```\n")
    assert bodies[4] == '```xml\n<xi:include href="never-resolved.xml"/>\n```\n'
    assert '<persName ref="a &gt; b">Standalone</persName>' in bodies[5]


def test_every_chapter_unit_is_the_verbatim_source_slice() -> None:
    """Each block must be findable in the source exactly as it stands."""
    for _, body in ingest.source_blocks(CHAPTER_XML):
        unit = body.removeprefix("```xml\n").removesuffix("\n```\n").encode()
        assert CHAPTER_XML.count(unit) == 1


def test_xml_entity_declarations_are_rejected_by_both_readers() -> None:
    payload = b'<!DOCTYPE x [<!ENTITY e "bad">]><x>&e;</x>'
    for reader in (ingest.reading_blocks, ingest.source_blocks):
        with pytest.raises(ValueError, match="DTD/entity"):
            reader(payload)


def test_check_requires_the_representation_without_creating_it(tmp_path: Path) -> None:
    target = tmp_path / "missing.md"
    with pytest.raises(FileNotFoundError):
        ingest.immutable_output(target, b"new", check=True)
    assert not target.exists()
