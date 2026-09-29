"""Offline integrity checks for the practice sample admission with inert synthetic sources."""

import copy
import json

import pytest
import yaml

from tools import ingest_practice_v1 as ingest

ODD = (b'<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron"><text><body>'
       b'<schemaSpec ident="demo" source="tei:4.12.0"><moduleRef key="core" include="p"/>'
       b'<elementSpec ident="p" mode="change"><constraintSpec ident="c" scheme="schematron"><constraint>'
       b'<sch:rule context="tei:p" role="warning"><sch:assert test="@n">n</sch:assert></sch:rule>'
       b'</constraint></constraintSpec></elementSpec>'
       b'<classSpec ident="att.demo" type="atts" mode="delete"/></schemaSpec></body></text></TEI>\n')
SCRIPT = b"# build\nrun --odd demo.odd out.rng\n"
INPUT = ('<?xml version="1.0"?>\n<?xml-model href="https://example.invalid/schema.rng"?>\n'
         '<TEI xmlns="http://www.tei-c.org/ns/1.0"><text><body><p n="1">Café</p></body></text></TEI>\n').encode()


def sources():
    common = {"case": "demo", "repository": "example/demo", "commit": "a" * 40, "date": "2026-09-11",
              "creator": "Synthetic fixture", "license": "CC0-1.0", "license_evidence": ["fixture"],
              "attribution": "Inert synthetic fixture, not practice evidence."}
    return [
        {**common, "slug": "practice-v1-demo-odd", "role": "odd", "path": "demo.odd", "language": "xml", "title": "Demo ODD",
         "fragments": [ingest.frag("r1", "module selection", "<schemaSpec", "/>", "interval"),
                       ingest.frag("r2", "changed element", '<elementSpec ident="p"', "</elementSpec>", "element")]},
        {**common, "slug": "practice-v1-demo-build", "role": "processing", "path": "build", "language": "sh", "title": "Demo build",
         "fragments": [ingest.frag("r1", "generation", "run --odd", "out.rng", "interval")]},
        {**common, "slug": "practice-v1-demo-input", "role": "input", "path": "input.xml", "language": "xml", "title": "Demo input",
         "fragments": [ingest.frag("r1", "schema association", "<?xml-model", "?>", "processing-instruction"),
                       ingest.frag("r2", "paragraph", "<p ", "</p>", "element")]},
    ]


def contexts():
    return [ingest.context("cmif-schema-rng", "demo", "example/demo", "a" * 40, "schema.rng", "CC0-1.0", "comparison"),
            ingest.context("csapi-check-rng", "demo", "example/service", "b" * 40, "schema copy.rng", "CC0-1.0", "comparison")]


def bodies():
    urls = ingest.declared_urls(sources(), contexts())
    return dict(zip(urls, [ODD, SCRIPT, INPUT, b"<grammar/>", b"<grammar />"], strict=True))


def fetcher(responses, status=200):
    def fetch(url):
        body = responses[url]
        digest = ingest.digest(body)
        return {"requested_url": url, "final_url": url, "observed_at": "2026-09-11T12:00:00Z", "status": status,
                "media_type": "text/plain", "byte_count": len(body), "sha256": digest,
                "raw_path": f"sha256/{digest[:2]}/{digest[2:]}"}, body
    return fetch


@pytest.fixture
def admitted(tmp_path):
    ingest.acquire(tmp_path, fetcher(bodies()), sources(), contexts())
    return tmp_path


def test_admission_is_exact_reproducible_and_checkable(admitted):
    root = admitted
    ingest.check(root, sources())
    for source, payload in zip(sources(), (ODD, SCRIPT, INPUT), strict=True):
        assert (root / ingest.original_path(source)).read_bytes() == payload
        assert ingest.embedded_source(root, source, len(payload)) == payload
    representation = (root / ingest.rep_path(sources()[2])).read_text(encoding="utf-8")
    assert json.dumps('<p n="1">Café</p>', ensure_ascii=False) + " ^r2" in representation
    manifest = yaml.safe_load((root / ingest.MANIFEST).read_text(encoding="utf-8"))
    assert manifest["counts"] == {"requests": 5, "admitted_sources": 3, "context_observations": 2, "reading_blocks": 5}
    assert manifest["instruction_trust"] == "none" and manifest["gaps"] == []
    assert ingest.reproduce(root, fetcher(bodies())) == []


def test_inventory_and_comparison_are_recorded_as_own_processing(admitted):
    normalized = json.loads((admitted / ingest.NORMALIZED).read_text(encoding="utf-8"))
    odd, _, source = normalized["admitted"]
    assert odd["odd_inventory"]["schemaSpec"] == {"ident": "demo", "source": "tei:4.12.0"}
    assert odd["odd_inventory"]["moduleRefs"] == [{"key": "core", "include": "p"}]
    assert odd["odd_inventory"]["spec_modes"]["classSpec mode=delete"] == 1
    assert odd["odd_inventory"]["schematron_roles"] == {"(absent)": 1, "warning": 1}
    assert source["input_inventory"]["prolog_xml_model"] == ['<?xml-model href="https://example.invalid/schema.rng"?>']
    assert normalized["self_executed"]["comparisons"][0]["byte_identical"] is False
    assert "RELAX NG validation" in normalized["not_executed"]


def test_reproduce_reports_changed_remote_bytes_without_writing(admitted):
    before = {path: path.read_bytes() for path in admitted.rglob("*") if path.is_file()}
    changed = bodies()
    changed[next(iter(changed))] = ODD.replace(b"demo", b"demx")
    assert ingest.reproduce(admitted, fetcher(changed)) == [next(iter(changed))]
    assert before == {path: path.read_bytes() for path in admitted.rglob("*") if path.is_file()}


def test_second_acquisition_refuses_to_overwrite(admitted):
    manifest = (admitted / ingest.MANIFEST).read_bytes()
    with pytest.raises(ValueError, match="manifest exists"):
        ingest.acquire(admitted, fetcher(bodies()), sources(), contexts())
    assert (admitted / ingest.MANIFEST).read_bytes() == manifest


def test_check_needs_no_ignored_original_and_never_recreates_it(admitted):
    original = admitted / ingest.original_path(sources()[0])
    original.unlink()
    ingest.check(admitted, sources())
    assert not original.exists()


@pytest.mark.parametrize("change", ["embedded-source", "reading-block", "normalized", "scope", "fragment-selector"])
def test_check_detects_every_integrity_boundary(admitted, change):
    configured = sources()
    if change == "embedded-source":
        path = admitted / ingest.rep_path(configured[1])
        path.write_bytes(path.read_bytes().replace(b"run --odd demo.odd", b"run --odd demx.odd", 1))
    elif change == "reading-block":
        path = admitted / ingest.rep_path(configured[0])
        path.write_bytes(path.read_bytes().replace(b" ^r2", b" edited ^r2", 1))
    elif change == "normalized":
        (admitted / ingest.NORMALIZED).write_bytes(b"{}")
    elif change == "scope":
        path = admitted / ingest.MANIFEST
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        manifest["objects"].append(copy.deepcopy(manifest["objects"][0]))
        path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
    else:
        configured[2]["fragments"][1]["end"] = "</body>"
    with pytest.raises(ValueError):
        ingest.check(admitted, configured)


def test_unusable_response_writes_no_tracked_output(tmp_path):
    with pytest.raises(ValueError, match="unusable response"):
        ingest.acquire(tmp_path, fetcher(bodies(), status=404), sources(), contexts())
    assert not any(tmp_path.rglob("*.md")) and not (tmp_path / ingest.MANIFEST).exists()


@pytest.mark.parametrize("payload", [ODD.replace(b"\n", b"\r\n"), ODD.replace(b"demo", b"[[demo]]"),
                                     SCRIPT + b"note ^r9\n", b'<!DOCTYPE TEI [<!ENTITY e "x">]>' + ODD])
def test_guard_rejects_payloads_that_cannot_stay_exact_or_inert(payload):
    source = sources()[0] if payload.lstrip().startswith((b"<", b"\xef")) else sources()[1]
    with pytest.raises(ValueError):
        ingest.render(source, payload)


def test_non_odd_and_broken_fragment_are_rejected():
    with pytest.raises(ValueError, match="exactly one schemaSpec"):
        ingest.odd_inventory(INPUT)
    fragment = ingest.frag("r1", "unbalanced", "<text>", "</schemaSpec>", "element")
    with pytest.raises(ValueError, match="well-formed element"):
        ingest.locate(ODD, fragment)
    with pytest.raises(ValueError, match="not well-formed"):
        ingest.render(sources()[2], INPUT.replace(b"</p>", b""))
    with pytest.raises(ValueError, match="start marker"):
        ingest.locate(ODD, ingest.frag("r1", "absent", "<absent", "/>", "interval"))
