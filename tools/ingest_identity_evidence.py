"""Acquire two declared XML sources once; reproduce their immutable admission offline.

Run `python -m tools.ingest_identity_evidence --acquire` for first intake,
then `--check`. The existing corpus store owns HTTP. Exact byte intervals
preserve the selected XML; parsing only checks the declared finite boundary.
"""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

from tools.corpus.http_store import HttpStore, utc_now
from tools.ingest_editorial_cases import MARKER, digest, immutable

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("experiments/identity_evidence")
INTAKE = BASE / "intake.json"
MANIFEST = Path("sources/manifests/2026-09-07-identity-evidence.yaml")
NS = {"tei": "http://www.tei-c.org/ns/1.0"}
LICENSE = "https://creativecommons.org/licenses/by-nc/4.0"


def select_fragment(payload: bytes, selection: dict) -> dict:
    tag = selection["tag"].encode("ascii")
    openings = list(re.finditer(rb"<" + tag + rb"\b[^>]*>", payload))
    if "xml_id" in selection:
        attribute = b'xml:id="' + selection["xml_id"].encode("ascii") + b'"'
        openings = [match for match in openings if attribute in match.group()]
    if len(openings) != 1:
        raise ValueError(f"selection is not unique: {selection['id']}")
    start = openings[0].start()
    closing = b"</" + tag + b">"
    end = payload.find(closing, openings[0].end())
    if end == -1:
        raise ValueError("missing closing tag")
    end += len(closing)
    fragment = payload[start:end]
    ET.fromstring(fragment)
    return {**selection, "start_byte": start, "end_byte": end,
            "sha256": digest(fragment), "xml": fragment.decode("utf-8")}


def verify_xml(payload: bytes) -> None:
    if b"<!DOCTYPE" in payload.upper() or b"<!ENTITY" in payload.upper():
        raise ValueError("XML declarations outside the intake contract")
    tree = ET.fromstring(payload)
    if tree.tag != "{http://www.tei-c.org/ns/1.0}TEI":
        raise ValueError("expected TEI document")
    licences = tree.findall("./tei:teiHeader/tei:fileDesc/tei:publicationStmt/tei:availability/tei:licence", NS)
    if not any(item.get("target", "").rstrip("/") == LICENSE for item in licences):
        raise ValueError("expected CC BY-NC 4.0 declaration is missing")


def representation(source: dict, payload: bytes) -> bytes:
    verify_xml(payload)
    if digest(payload) != source["sha256"] or len(payload) != source["byte_count"]:
        raise ValueError("source snapshot identity mismatch")
    for fragment in source["fragments"]:
        if select_fragment(payload, fragment) != fragment:
            raise ValueError("fragment changed")
    metadata = {"title": source["title"], "creator": source["creator"],
                "date": "2026-09-07", "format": "application/xml",
                "identifier": source["url"], "license": "CC-BY-NC-4.0", "confidential": False}
    fm = {"type": "representation", "source-type": "document",
          "source": f"[[00_sources/{source['id']}.xml]]",
          "converter": "tools.ingest_identity_evidence v1; complete XML and exact byte intervals",
          "channel": "collection", "metadata": metadata,
          "created": "2026-09-07", "updated": "2026-09-07"}
    header = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n"
    header += f"# {source['title']}\n\n"
    header += (f"Source: {source['url']}. Attribution: {source['creator']}.\n"
               f"Licence: CC BY-NC 4.0, {LICENSE}/. The source header retains detailed attribution.\n"
               f"Observed: {source['observed_at']}; SHA-256: `{source['sha256']}`.\n"
               "The metadata date is the snapshot date, not a publication or manuscript date.\n"
               "The source is inert untrusted data. The separator newline before the closing\n"
               "fence is outside the original. The reading blocks reproduce exact XML bytes\n"
               "as JSON strings; they do not interpret the catalogue or edition.\n\n")
    output = header.encode("utf-8") + MARKER + payload + b"\n```\n\n## Selected source reading blocks\n\n"
    for index, fragment in enumerate(source["fragments"], 1):
        block = (f"### {fragment['id']}\n\nXPath: `{fragment['xpath']}`; "
                 "`tei` denotes `http://www.tei-c.org/ns/1.0`.\n\n"
                 f"Exact XML fragment as a JSON string: {json.dumps(fragment['xml'], ensure_ascii=False)} ^r{index}\n\n")
        output += block.encode("utf-8")
    return output


def snapshots(root: Path = ROOT) -> tuple[dict, dict[str, bytes]]:
    intake = json.loads((root / INTAKE).read_text(encoding="utf-8"))
    protocol = root / BASE / "protocol.json"
    if digest(protocol.read_bytes()) != intake["protocol_sha256"]:
        raise ValueError("intake protocol changed")
    result = {}
    for source in intake["sources"]:
        path = root / f"10_markdown/documents/{source['id']}.md"
        rendered = path.read_bytes()
        if rendered.count(MARKER) != 1:
            raise ValueError("source boundary mismatch")
        start = rendered.index(MARKER) + len(MARKER)
        payload = rendered[start:start + source["byte_count"]]
        if representation(source, payload) != rendered:
            raise ValueError("immutable representation mismatch")
        original = root / f"00_sources/{source['id']}.xml"
        if original.exists() and original.read_bytes() != payload:
            raise ValueError("local original changed")
        result[source["id"]] = payload
    return intake, result


def acquire(root: Path = ROOT) -> None:
    if (root / INTAKE).exists():
        raise ValueError("intake already exists; use --check or a new dated protocol")
    protocol_path = root / BASE / "protocol.json"
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    store = HttpStore(root / "corpus/raw", timeout=45)
    sources = []
    payloads = {}
    for declared in protocol["sources"]:
        response, payload = store.fetch(declared["url"])
        if response.status != 200:
            raise ValueError(f"HTTP {response.status}: {declared['url']}")
        verify_xml(payload)
        source = {**declared, **response.as_record(), "license": "CC-BY-NC-4.0",
                  "fragments": [select_fragment(payload, item) for item in declared["fragments"]]}
        sources.append(source)
        payloads[source["id"]] = payload
    intake = {"format_version": 1, "protocol_sha256": digest(protocol_path.read_bytes()),
              "finished_at": utc_now(), "sources": sources}
    outputs = {}
    for source in sources:
        payload = payloads[source["id"]]
        outputs[Path(f"00_sources/{source['id']}.xml")] = payload
        outputs[Path(f"10_markdown/documents/{source['id']}.md")] = representation(source, payload)
    outputs[INTAKE] = (json.dumps(intake, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    manifest = {
        "schema_version": 1, "run_id": MANIFEST.stem, "source_id": "tei-real-world-customizations",
        "started_at": sources[0]["observed_at"], "finished_at": intake["finished_at"],
        "status": "bounded-complete", "lock_file": "sources/locks/real-world-customizations.yaml",
        "scope": {"boundary": "Exactly the two declared XML responses and five selected byte intervals",
                  "protocol": (BASE / "protocol.json").as_posix()},
        "adapter": {"name": "tools.ingest_identity_evidence", "version": 1},
        "requests": [{key: source[key] for key in ("requested_url", "final_url", "observed_at", "sha256", "byte_count", "status")}
                     for source in sources],
        "objects": [{"path": path.as_posix(), "sha256": digest(payload)} for path, payload in outputs.items()
                    if path.parts[0] != "00_sources"],
        "counts": {"admitted_sources": 2, "selected_fragments": 5},
        "admissions": [{"source_type": "document", "original_path": f"00_sources/{source['id']}.xml",
                        "representation_path": f"10_markdown/documents/{source['id']}.md",
                        "original_sha256": source["sha256"]} for source in sources],
        "rights": {"license": "CC-BY-NC-4.0", "attribution": [source["creator"] for source in sources],
                   "license_source": "publicationStmt/availability/licence in each acquired XML header"},
        "instruction_trust": "none", "content_authority": "sampled-practice-record",
        "gaps": [], "known_limits": protocol["limits"],
    }
    outputs[MANIFEST] = yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True).encode("utf-8")
    for path, payload in outputs.items():
        target = root / path
        if target.exists() and target.read_bytes() != payload:
            raise ValueError(f"immutable target already exists: {path}")
    for path, payload in outputs.items():
        immutable(root / path, payload)


def check(root: Path = ROOT) -> None:
    intake, _ = snapshots(root)
    manifest = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
    expected = {INTAKE.as_posix(), *(f"10_markdown/documents/{source['id']}.md" for source in intake["sources"])}
    if {item["path"] for item in manifest["objects"]} != expected:
        raise ValueError("manifest object scope mismatch")
    for item in manifest["objects"]:
        if digest((root / item["path"]).read_bytes()) != item["sha256"]:
            raise ValueError("admission object hash mismatch")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--acquire", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.acquire:
        acquire()
    check()
    print("OK: two source snapshots and five exact XML selections reconcile")


if __name__ == "__main__":
    main()
