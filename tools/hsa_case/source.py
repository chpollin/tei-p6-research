"""Read and project the admitted snapshot with indexed source locations."""

from __future__ import annotations

import hashlib
import xml.etree.ElementTree as ET
from pathlib import Path

from tools.hsa_case.config import NS, REPRESENTATION, ROOT, SHA256, TEI
from tools.ingest_editorial_cases import MARKER
from tools.ingest_identity_evidence import verify_xml


def source_bytes(root: Path = ROOT) -> bytes:
    rendered = (root / REPRESENTATION).read_bytes()
    if rendered.count(MARKER) != 1:
        raise ValueError("source representation boundary mismatch")
    payload, separator, _ = rendered.split(MARKER, 1)[1].partition(b"\n```\n")
    if not separator or hashlib.sha256(payload).hexdigest() != SHA256:
        raise ValueError("source snapshot hash mismatch")
    original = root / "00_sources/hsa-letter-4493-2026-09-07.xml"
    if original.exists() and original.read_bytes() != payload:
        raise ValueError("local source snapshot differs from admitted bytes")
    verify_xml(payload)
    return payload


def source_tree(payload: bytes) -> tuple[ET.Element, dict[ET.Element, str]]:
    tree = ET.fromstring(payload)
    paths = {}

    def walk(element: ET.Element, path: str) -> None:
        if not element.tag.startswith("{" + TEI + "}"):
            raise ValueError("unexpected source namespace")
        paths[element] = path
        counts = {}
        for child in element:
            tag = child.tag.split("}", 1)[1]
            counts[tag] = counts.get(tag, 0) + 1
            walk(child, f"{path}/tei:{tag}[{counts[tag]}]")

    walk(tree, "/tei:TEI[1]")
    body = one(tree, "./tei:text/tei:body")
    div = one(body, "./tei:div")
    if (
        len(body) != 1
        or div.get("{http://www.w3.org/XML/1998/namespace}id") != "L.4492"
    ):
        raise ValueError("unexpected source letter structure or identifier")
    notes = list(div.iter("{" + TEI + "}note"))
    if [note.get("n") for note in notes] != list(map(str, range(1, 12))):
        raise ValueError("expected eleven separately numbered editorial notes")
    if any(
        note.get("type") != "editorial" or note.get("place") != "foot" for note in notes
    ):
        raise ValueError("unexpected note kind")
    if len(list(div.iter("{" + TEI + "}persName"))) != 4:
        raise ValueError("unexpected named mention boundary")
    return tree, paths


def one(element: ET.Element, path: str) -> ET.Element:
    found = element.findall(path, NS)
    if len(found) != 1:
        raise ValueError(f"expected one source location: {path}; found {len(found)}")
    return found[0]


def resolve(tree: ET.Element, xpath: str) -> str:
    path, marker, attribute = xpath.partition("/@")
    if not path.startswith("/tei:TEI[1]"):
        raise ValueError("source XPath outside TEI root")
    relative = "." + path[len("/tei:TEI[1]") :]
    element = one(tree, relative) if relative != "." else tree
    if marker:
        if attribute.startswith("xml:"):
            attribute = "{" + NS["xml"] + "}" + attribute[4:]
        if attribute not in element.attrib:
            raise ValueError(f"missing source attribute: {xpath}")
        return element.attrib[attribute]
    return "".join(element.itertext())


def project(
    div: ET.Element,
) -> tuple[dict[str, str], dict[ET.Element, tuple[str, int, int]], dict[str, int]]:
    buffers = {"representation-letter": []}
    lengths = {"representation-letter": 0}
    spans = {}
    anchors = {}

    def append(identifier: str, text: str | None) -> None:
        buffers[identifier].append(text or "")
        lengths[identifier] += len(text or "")

    def visit(element: ET.Element, identifier: str) -> None:
        start = lengths[identifier]
        append(identifier, element.text)
        for child in element:
            if child.tag == "{" + TEI + "}note":
                number = f"{int(child.attrib['n']):02}"
                anchors[number] = lengths[identifier]
                note_id = "representation-note-" + number
                buffers[note_id], lengths[note_id] = [], 0
                visit(child, note_id)
            else:
                visit(child, identifier)
            append(identifier, child.tail)
        spans[element] = (identifier, start, lengths[identifier])

    visit(div, "representation-letter")
    return {key: "".join(value) for key, value in buffers.items()}, spans, anchors
