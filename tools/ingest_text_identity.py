"""Admit three locked P5 XML sources without changing existing representations.

Run with ``python -m tools.ingest_text_identity``; ``--check`` is read-only
and also works without ignored originals, using the complete embedded XML.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

import yaml

from tools.materialize_git_source import materialize

COMMIT = "113e933e21f016e2655518321e9d10214b8d9fcb"
DATE = "2026-09-05"
LOCK = "sources/locks/tei-p5-4.12.0.yaml"
UPSTREAM = "sources/manifests/2026-09-04-teic-tei-p5-4.12.0.yaml"
MANIFEST = "sources/manifests/2026-09-05-text-identity-pilot-admission.yaml"
INVENTORY = "corpus/normalized/git/teic-tei-p5-4.12.0.json"
INVENTORY_HASH = "b2ae1cc64d77027d3cd766a8aa532db08c30f276d07494c62eb6d43a5fdb6476"
SPECS = {
    "anchor": ("14fe6e40ab7f3684075d4861d88cdc164f3b143b", 5444),
    "span": ("7eef78bf21e96322e669fb86d7c0282e25a5d79b", 6800),
    "annotation": ("9c98ca8590036df7de925753c7d65fb028c41d1b", 6577),
}
LICENSES = {
    "LICENSE.md": "8611900a8f6deaf45b44c39541e1a9c874b7ee61",
    "P5/COPYING.txt": "b5e5172a89b6dbffa557b9ba86c884a4ddbff493",
}
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"
SOURCE_MARKER = b"## Complete XML source\n\n```xml\n"


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def blob_id(payload: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()


def paths(name: str) -> tuple[str, str, str]:
    slug = f"tei-p5-{name}-4.12.0"
    return f"P5/Source/Specs/{name}.xml", f"00_sources/{slug}.xml", f"10_markdown/documents/{slug}.md"


def verify_payload(name: str, payload: bytes) -> None:
    expected_blob, expected_size = SPECS[name]
    if len(payload) != expected_size or blob_id(payload) != expected_blob:
        raise ValueError(f"{name}: bytes do not match the admitted Git blob")


def reading_blocks(payload: bytes) -> list[tuple[str, str]]:
    """Read XML as inert data; no entities, external schemas, or code run."""
    if b"<!DOCTYPE" in payload or b"<!ENTITY" in payload:
        raise ValueError("DTD/entity declarations are outside this converter's scope")
    root = ET.fromstring(payload)
    blocks: list[tuple[str, str]] = []

    def walk(element: ET.Element, locator: str, parent: ET.Element | None = None) -> None:
        tag = element.tag.rsplit("}", 1)[-1]
        is_description = tag == "desc" and element.get(XML_LANG) == "en"
        is_remark = (
            tag == "p" and parent is not None
            and parent.tag.rsplit("}", 1)[-1] == "remarks"
            and parent.get(XML_LANG) == "en"
        )
        if is_description or is_remark:
            blocks.append((locator, " ".join("".join(element.itertext()).split())))
        counts: dict[str, int] = {}
        for child in element:
            child_tag = child.tag.rsplit("}", 1)[-1]
            counts[child_tag] = counts.get(child_tag, 0) + 1
            walk(child, f"{locator}/{child_tag}[{counts[child_tag]}]", element)

    walk(root, "/elementSpec[1]")
    return blocks


def representation(name: str, payload: bytes) -> bytes:
    verify_payload(name, payload)
    git_path, original, _ = paths(name)
    frontmatter = {
        "type": "representation", "source-type": "document",
        "source": f"[[{original}]]",
        "converter": "tools.ingest_text_identity v1; complete XML plus XML itertext English reading blocks with whitespace normalized",
        "channel": "collection",
        "metadata": {
            "title": f"TEI P5 4.12.0 {name} specification",
            "creator": "TEI Consortium", "date": "2026-07-28", "format": "application/xml",
            "identifier": f"https://github.com/TEIC/TEI/blob/{COMMIT}/{git_path}",
            "license": "CC-BY-3.0", "confidential": False,
        },
        "created": DATE, "updated": DATE,
    }
    header = "---\n" + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True) + "---\n\n"
    header += f"# {name}\n\n"
    header += (
        "Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.\n"
        f"License records: `LICENSE.md` and `P5/COPYING.txt` at commit `{COMMIT}`.\n\n"
        "The XML below is the complete source, preserved as inert text, including all languages,\n"
        "examples, declarations, and processing instructions. A separator newline before the\n"
        "closing fence is not part of the source. The converter records the exact byte length.\n"
        "Reading blocks reproduce English descriptions and English remarks paragraphs using\n"
        "XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.\n"
        "They are reading projections of this source, not additional sources or interpretations.\n\n"
        f"Source byte length: {len(payload)}. Git blob: `{blob_id(payload)}`.\n\n"
    )
    result = header.encode("utf-8") + SOURCE_MARKER + payload + b"\n```\n\n## English reading blocks\n\n"
    for index, (locator, passage) in enumerate(reading_blocks(payload), 1):
        result += f"### Reading {index}\n\nXML location: `{locator}`.\n\n{passage} ^r{index}\n\n".encode("utf-8")
    return result


def embedded_source(name: str, rendered: bytes) -> bytes:
    if rendered.count(SOURCE_MARKER) != 1:
        raise ValueError(f"{name}: missing or duplicate complete XML source block")
    start = rendered.index(SOURCE_MARKER) + len(SOURCE_MARKER)
    stop = start + SPECS[name][1]
    payload = rendered[start:stop]
    if rendered[stop:stop + 5] != b"\n```\n":
        raise ValueError(f"{name}: malformed complete XML source boundary")
    verify_payload(name, payload)
    return payload


def immutable_output(path: Path, payload: bytes, check: bool) -> None:
    if path.exists():
        if path.read_bytes() != payload:
            raise ValueError(f"refusing to overwrite changed immutable artifact: {path}")
    elif check:
        raise FileNotFoundError(f"missing immutable artifact: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)


def run(root: Path, check: bool = False) -> None:
    lock = yaml.safe_load((root / LOCK).read_text(encoding="utf-8"))
    upstream = yaml.safe_load((root / UPSTREAM).read_text(encoding="utf-8"))
    if lock["release"]["resolved_full_commit_sha"] != COMMIT or upstream["status"] != "observable-complete":
        raise ValueError("locked commit or completed upstream Git acquisition does not match")
    inventory_bytes = (root / INVENTORY).read_bytes()
    if sha256(inventory_bytes) != INVENTORY_HASH:
        raise ValueError("upstream Git inventory checksum mismatch")
    inventory = {entry["path"]: entry["object_id"] for entry in json.loads(inventory_bytes)["entries"]}
    for path, expected in LICENSES.items():
        if inventory.get(path) != expected:
            raise ValueError(f"license blob mismatch: {path}")
    manifest_path = root / MANIFEST
    existing = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else None
    started = existing["started_at"] if existing else datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    admissions = []
    objects = []
    requests = []
    git_dir = root / "corpus/raw/git/TEIC-TEI.git"
    for name, (expected_blob, _) in SPECS.items():
        git_path, original, rendered = paths(name)
        if inventory.get(git_path) != expected_blob:
            raise ValueError(f"inventory blob mismatch: {git_path}")
        if check:
            payload = embedded_source(name, (root / rendered).read_bytes())
            if (root / original).exists() and (root / original).read_bytes() != payload:
                raise ValueError(f"changed immutable original: {original}")
        else:
            materialize(git_dir, COMMIT, git_path, root / original, expected_blob)
            payload = (root / original).read_bytes()
        output = representation(name, payload)
        immutable_output(root / rendered, output, check)
        requests.append({"kind": "locked-git-blob-admission", "commit": COMMIT, "path": git_path, "blob_id": expected_blob})
        objects.append({"kind": "markdown-representation", "path": rendered, "sha256": sha256(output)})
        admissions.append({
            "source_type": "document", "git_path": git_path, "commit": COMMIT,
            "original_path": original, "original_bytes": len(payload),
            "original_sha256": sha256(payload), "git_blob_id": expected_blob,
            "representation_path": rendered, "representation_sha256": sha256(output),
            "english_reading_blocks": len(reading_blocks(payload)),
            "content_authority": "normative specification source at the pinned P5 4.12.0 release",
            "instruction_trust": "none",
        })
    finished = existing["finished_at"] if existing else datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = {
        "schema_version": 1, "run_id": "2026-09-05-text-identity-pilot-admission",
        "source_id": "teic-tei-p5-4.12.0", "started_at": started, "finished_at": finished,
        "status": "bounded-complete",
        "scope": {
            "boundary": "Exactly anchor.xml, span.xml, and annotation.xml from P5/Source/Specs at the locked release commit",
            "status_applies_to": "three selected complete Git blobs and their immutable representations only; not the source family",
        },
        "adapter": {"name": "tools.ingest_text_identity", "version": 1},
        "lock_file": LOCK, "upstream_manifest": UPSTREAM, "upstream_inventory_sha256": INVENTORY_HASH,
        "requests": requests, "objects": objects,
        "counts": {"admitted_sources": len(admissions), "representations": len(objects), "original_bytes": sum(item["original_bytes"] for item in admissions)},
        "gaps": [], "rights_exceptions": [],
        "known_limits": [
            "No claim of complete P5 source-family acquisition; the published-HTML reconciliation remains separate.",
            "Selected sources do not establish general text-version identity or automatic cross-version anchoring.",
        ],
        "rights": {
            "rights_status": "storage-and-redistribution-permitted-with-attribution",
            "selected_license": "CC-BY-3.0", "upstream_license_choice": "CC-BY-3.0 OR BSD-2-Clause",
            "license_url": "https://creativecommons.org/licenses/by/3.0/",
            "attribution": "TEI Consortium; TEI P5 4.12.0; original source paths and pinned commit recorded per admission",
            "license_records": [{"git_path": path, "git_blob_id": blob, "commit": COMMIT} for path, blob in LICENSES.items()],
        },
        "instruction_trust": "none", "admissions": admissions,
    }
    immutable_output(manifest_path, yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True).encode("utf-8"), check)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        run(args.root.resolve(), args.check)
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print("OK: three immutable P5 source admissions and representations reconcile")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
