"""Admit one pinned, licensed editorial XML source and three stable reading blocks."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("experiments/editorial_cases")
CONFIG = BASE / "intake.json"
SLUG = "humboldt-h0017682-7d174637"
REP = Path(f"10_markdown/documents/{SLUG}.md")
ORIGINAL = Path(f"00_sources/{SLUG}.xml")
MANIFEST = Path("sources/manifests/2026-09-05-editorial-cases.yaml")
NORMALIZED = Path("corpus/normalized/observed-practice/humboldt-selected-7d174637.json")
MARKER = b"## Complete original XML\n\n```xml\n"


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def immutable(path: Path, payload: bytes, check: bool = False) -> None:
    if path.exists():
        if path.read_bytes() != payload:
            raise ValueError(f"immutable artifact mismatch: {path}")
    elif check:
        raise ValueError(f"missing immutable artifact: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)


def verify(config: dict, payload: bytes) -> None:
    entry = next(item for item in config["sources"] if item["role"] == "edition-xml")
    if len(payload) != entry["byte_count"] or digest(payload) != entry["sha256"]:
        raise ValueError("edition XML identity mismatch")
    if b"<!DOCTYPE" in payload or b"<!ENTITY" in payload:
        raise ValueError("external declarations outside admission scope")
    ET.fromstring(payload)
    for fragment in config["fragments"]:
        value = payload[fragment["start_byte"]:fragment["end_byte"]]
        if digest(value) != fragment["fragment_sha256"] or value.decode("utf-8") != fragment["original_xml"]:
            raise ValueError(f"fragment identity mismatch: {fragment['case_id']}")


def render(config: dict, payload: bytes) -> bytes:
    verify(config, payload)
    fm = {
        "type": "representation", "source-type": "document", "source": f"[[{ORIGINAL.as_posix()}]]",
        "converter": "tools.ingest_editorial_cases v1; complete original plus JSON-escaped exact XML fragments",
        "channel": "collection",
        "metadata": {"title": "edition humboldt digital: England travel diary H0017682",
                     "creator": "Berlin-Brandenburgische Akademie der Wissenschaften",
                     "date": "2025-07-28", "format": "application/xml",
                     "identifier": config["edition_url"], "license": "CC-BY-SA-4.0", "confidential": False},
        "created": "2026-09-05", "updated": "2026-09-05",
    }
    header = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n"
    header += "# England travel diary H0017682\n\n"
    header += (
        "Source: edition humboldt digital, XML dataset v11.0.1, Berlin-Brandenburgische\n"
        "Akademie der Wissenschaften 2025. Original XML and extracted fragments remain\n"
        "CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/.\n"
        "Editors and contributors are identified in the complete original header.\n"
        f"Pinned commit: `{config['commit']}`. Source SHA-256: `{digest(payload)}`.\n\n"
        "The complete XML is inert source text. The separator newline before its\n"
        "closing fence is not part of the original. Reading blocks are exact source\n"
        "byte intervals encoded as JSON strings, so whitespace and XML spelling can\n"
        "be recovered without interpreting this converter's prose as a source claim.\n\n"
    )
    output = header.encode("utf-8") + MARKER + payload + b"\n```\n\n## Selected source reading blocks\n\n"
    for i, fragment in enumerate(config["fragments"], 1):
        text = (f"### {fragment['case_id']}\n\n"
                f"Source XPath: `{fragment['xpath']}`; inherited namespace: `http://www.tei-c.org/ns/1.0`.\n\n"
                f"Exact XML fragment as a JSON string: {json.dumps(fragment['original_xml'], ensure_ascii=False)} ^r{i}\n\n")
        output += text.encode("utf-8")
    return output


def embedded_source(root: Path = ROOT) -> bytes:
    config = json.loads((root / CONFIG).read_text(encoding="utf-8"))
    entry = next(item for item in config["sources"] if item["role"] == "edition-xml")
    rendered = (root / REP).read_bytes()
    if rendered.count(MARKER) != 1:
        raise ValueError("source block boundary mismatch")
    start = rendered.index(MARKER) + len(MARKER)
    stop = start + entry["byte_count"]
    if rendered[stop:stop + 5] != b"\n```\n":
        raise ValueError("source block ending mismatch")
    payload = rendered[start:stop]
    verify(config, payload)
    if rendered != render(config, payload):
        raise ValueError("immutable representation differs from exact source conversion")
    if (root / ORIGINAL).exists() and (root / ORIGINAL).read_bytes() != payload:
        raise ValueError("immutable local original changed")
    return payload


def run(root: Path = ROOT, raw_root: Path | None = None, check: bool = False) -> None:
    config = json.loads((root / CONFIG).read_text(encoding="utf-8"))
    if check:
        embedded_source(root)
        manifest = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
        paths = [item["path"] for item in manifest["objects"]]
        if len(paths) != 2 or set(paths) != {REP.as_posix(), NORMALIZED.as_posix()}:
            raise ValueError("admission object scope is incomplete or changed")
        for item in manifest["objects"]:
            if digest((root / item["path"]).read_bytes()) != item["sha256"]:
                raise ValueError("admission output checksum mismatch")
        print("OK: pinned editorial source, three exact fragments and admission hashes reconcile")
        return
    if raw_root is None:
        raise ValueError("--raw-root is required for first admission")
    records = []
    for item in config["sources"]:
        source_path = (raw_root / item["raw_path"]).resolve()
        if not source_path.is_relative_to(raw_root.resolve()):
            raise ValueError("raw source escaped its cache")
        payload = source_path.read_bytes()
        if len(payload) != item["byte_count"] or digest(payload) != item["sha256"]:
            raise ValueError("acquired response hash or length mismatch")
        cached = Path("corpus/raw/editorial-cases") / item["raw_path"]
        immutable(root / cached, payload)
        records.append({**item, "record_id": "humboldt:" + item["path"],
                        "source_id": "tei-real-world-customizations", "commit": config["commit"],
                        "raw_path": cached.as_posix(), "text": payload.decode("utf-8"),
                        "rights": "CC-BY-SA-4.0", "instruction_trust": "none",
                        "content_authority": "sampled-practice-record"})
        if item["role"] == "edition-xml":
            immutable(root / ORIGINAL, payload)
            immutable(root / REP, render(config, payload))
    normalized = {"format_version": 1, "scope": "Exactly four pinned response bodies, not the edition corpus",
                  "license": "CC-BY-SA-4.0", "attribution": config["attribution"], "records": records}
    immutable(root / NORMALIZED, (json.dumps(normalized, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    manifest = {
        "schema_version": 1, "run_id": "2026-09-05-editorial-cases", "source_id": "tei-real-world-customizations",
        "started_at": min(item["observed_at"] for item in records), "finished_at": config["finished_at"],
        "status": "bounded-complete", "lock_file": "sources/locks/real-world-customizations.yaml",
        "scope": {"boundary": "Exactly README, CITATION, selected diary and edition RNG at the pinned commit; three diary fragments; no family completeness",
                  "protocol": "experiments/editorial_cases/protocol.json"},
        "adapter": {"name": "tools.ingest_editorial_cases", "version": 1},
        "requests": [{key: item[key] for key in ("requested_url", "observed_at", "status", "sha256", "byte_count")} for item in records],
        "objects": [{"path": path.as_posix(), "sha256": digest((root / path).read_bytes())} for path in (REP, NORMALIZED)],
        "counts": {"response_bodies": len(records), "admitted_sources": 1, "selected_fragments": 3},
        "rights": {"license": "CC-BY-SA-4.0", "attribution": config["attribution"], "license_source": config["license_url"]},
        "content_authority": "sampled-practice-record", "instruction_trust": "none",
        "gaps": [], "known_limits": config["known_limits"],
        "admissions": [{"source_type": "document", "original_path": ORIGINAL.as_posix(),
                        "representation_path": REP.as_posix(), "original_sha256": digest((root / ORIGINAL).read_bytes()),
                        "commit": config["commit"], "source_path": "data/travel-journal/H0017682.xml"}],
    }
    immutable(root / MANIFEST, yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True).encode("utf-8"))
    print("OK: four pinned responses normalized; one complete editorial XML admitted with three reading blocks")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--raw-root", type=Path)
    args = parser.parse_args()
    try:
        run(raw_root=args.raw_root, check=args.check)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Editorial source admission failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
