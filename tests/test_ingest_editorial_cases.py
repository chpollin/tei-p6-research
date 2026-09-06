"""Finite integrity and immutable-admission checks with inert synthetic inputs."""

import copy
import json

import pytest
import yaml

from tools import ingest_editorial_cases as ingest

XML = '<TEI xmlns="http://www.tei-c.org/ns/1.0"><text><head>Un café</head><p>A  B.</p><p>C.</p></text></TEI>'.encode()
FRAGMENTS = ["<head>Un café</head>", "<p>A  B.</p>", "<p>C.</p>"]


def configuration(payload=XML):
    bodies = [b"Licensed sample.", b"Sample citation.", payload, b"<grammar/>"]
    roles = ["license-and-context", "citation", "edition-xml", "project-schema"]
    paths = ["README.md", "CITATION.cff", "data/travel-journal/H0017682.xml", "schema.rng"]
    sources = [{"role": role, "path": path, "raw_path": "objects/" + str(i),
                "sha256": ingest.digest(body), "byte_count": len(body),
                "requested_url": "https://example.invalid/" + path,
                "observed_at": f"2026-09-05T12:00:0{i}Z", "status": 200}
               for i, (body, role, path) in enumerate(zip(bodies, roles, paths, strict=True))]
    fragments = []
    if payload == XML:
        for i, fragment in enumerate(FRAGMENTS):
            encoded = fragment.encode("utf-8")
            start = payload.index(encoded)
            fragments.append({"case_id": f"case-{i + 1}", "start_byte": start,
                              "end_byte": start + len(encoded), "fragment_sha256": ingest.digest(encoded),
                              "original_xml": fragment, "xpath": f"/*/*/*[{i + 1}]"})
    return {"sources": sources, "fragments": fragments, "commit": "a" * 40,
            "edition_url": "https://example.invalid/edition", "attribution": "Synthetic test source",
            "license_url": "https://example.invalid/license", "finished_at": "2026-09-05T12:01:00Z",
            "known_limits": ["Inert synthetic fixture, not editorial evidence"]}, bodies


@pytest.fixture
def admitted(tmp_path):
    config, bodies = configuration()
    root, raw = tmp_path / "vault", tmp_path / "raw"
    config_path = root / ingest.CONFIG
    config_path.parent.mkdir(parents=True)
    config_path.write_text(json.dumps(config, ensure_ascii=False), encoding="utf-8")
    for item, body in zip(config["sources"], bodies, strict=True):
        path = raw / item["raw_path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
    ingest.run(root, raw_root=raw)
    return root, raw


def test_exact_source_and_reading_fragments_survive_repeated_admission(admitted):
    root, raw = admitted
    assert ingest.embedded_source(root) == XML
    representation = (root / ingest.REP).read_bytes()
    for i, fragment in enumerate(FRAGMENTS, 1):
        assert (json.dumps(fragment, ensure_ascii=False) + f" ^r{i}").encode("utf-8") in representation
    before = {relative: (root / relative).read_bytes()
              for relative in (ingest.REP, ingest.ORIGINAL, ingest.NORMALIZED, ingest.MANIFEST)}
    ingest.run(root, raw_root=raw)
    ingest.run(root, check=True)
    assert before == {relative: (root / relative).read_bytes() for relative in before}


def test_check_works_without_ignored_original_and_never_recreates_it(admitted):
    root, _ = admitted
    original = root / ingest.ORIGINAL
    original.unlink()
    manifest = (root / ingest.MANIFEST).read_bytes()
    ingest.run(root, check=True)
    assert not original.exists()
    assert (root / ingest.MANIFEST).read_bytes() == manifest


def test_immutable_refusal_preserves_existing_bytes(tmp_path):
    path = tmp_path / "source.xml"
    path.write_bytes(b"original")
    with pytest.raises(ValueError, match="immutable artifact mismatch"):
        ingest.immutable(path, b"changed")
    assert path.read_bytes() == b"original"
    missing = tmp_path / "absent.xml"
    with pytest.raises(ValueError, match="missing immutable artifact"):
        ingest.immutable(missing, b"new", check=True)
    assert not missing.exists()


@pytest.mark.parametrize("change", ["original", "embedded-source", "reading-block", "source-end", "duplicate-marker"])
def test_embedded_source_detects_all_checked_integrity_boundaries(admitted, change):
    root, _ = admitted
    if change == "original":
        (root / ingest.ORIGINAL).write_bytes(XML.replace(b"C.", b"D."))
    else:
        path = root / ingest.REP
        content = path.read_bytes()
        if change == "embedded-source":
            content = content.replace(XML, XML.replace(b"C.", b"D."), 1)
        elif change == "reading-block":
            content = content.replace(b" ^r1", b" edited ^r1", 1)
        elif change == "source-end":
            content = content.replace(XML + b"\n```\n", XML + b"\n~~~\n", 1)
        else:
            content += ingest.MARKER
        path.write_bytes(content)
    with pytest.raises(ValueError):
        ingest.embedded_source(root)


@pytest.mark.parametrize("change", ["hash", "length", "fragment-bytes", "fragment-hash", "fragment-string"])
def test_verify_rejects_source_or_fragment_drift_without_mutation(change):
    config, _ = configuration()
    if change == "hash":
        config["sources"][2]["sha256"] = "0" * 64
    elif change == "length":
        config["sources"][2]["byte_count"] += 1
    elif change == "fragment-bytes":
        config["fragments"][0]["start_byte"] += 1
    elif change == "fragment-hash":
        config["fragments"][0]["fragment_sha256"] = "0" * 64
    else:
        config["fragments"][0]["original_xml"] += "altered"
    snapshot = copy.deepcopy(config)
    with pytest.raises(ValueError):
        ingest.verify(config, XML)
    assert config == snapshot


def test_dtd_entity_declarations_are_rejected_even_when_hashes_match():
    payload = b'<!DOCTYPE TEI [<!ENTITY e "expanded">]><TEI>&e;</TEI>'
    config, _ = configuration(payload)
    with pytest.raises(ValueError, match="declarations"):
        ingest.verify(config, payload)


def test_acquired_response_drift_does_not_overwrite_immutable_outputs(admitted):
    root, raw = admitted
    before = (root / ingest.REP).read_bytes()
    (raw / "objects/0").write_bytes(b"changed source")
    with pytest.raises(ValueError, match="hash or length mismatch"):
        ingest.run(root, raw_root=raw)
    assert (root / ingest.REP).read_bytes() == before


def test_raw_path_escape_is_rejected_before_read(admitted):
    root, raw = admitted
    path = root / ingest.CONFIG
    config = json.loads(path.read_text(encoding="utf-8"))
    config["sources"][0]["raw_path"] = "../outside"
    path.write_text(json.dumps(config), encoding="utf-8")
    with pytest.raises(ValueError, match="escaped its cache"):
        ingest.run(root, raw_root=raw)


def test_normalized_output_drift_is_rejected(admitted):
    root, _ = admitted
    (root / ingest.NORMALIZED).write_bytes(b"changed")
    with pytest.raises(ValueError, match="checksum mismatch"):
        ingest.run(root, check=True)


@pytest.mark.parametrize("change", ["missing", "duplicate", "unknown"])
def test_check_requires_exact_admission_manifest_output_scope(admitted, change):
    root, _ = admitted
    path = root / ingest.MANIFEST
    manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
    if change == "missing":
        manifest["objects"] = []
    elif change == "duplicate":
        manifest["objects"].append(copy.deepcopy(manifest["objects"][0]))
    else:
        manifest["objects"].append({"path": ingest.CONFIG.as_posix(),
                                    "sha256": ingest.digest((root / ingest.CONFIG).read_bytes())})
    path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
    with pytest.raises(ValueError, match="scope"):
        ingest.run(root, check=True)
