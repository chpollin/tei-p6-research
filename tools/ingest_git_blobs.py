"""Admit locked Git blobs of a pinned mirror as immutable Markdown representations.

One admission list drives the whole chain, so the pilot in
``tools.ingest_text_identity`` and every later topic run share this code. Run with
``python -m tools.ingest_git_blobs``; ``--check`` is read-only and works without
the ignored originals and without the mirror, because it reads the complete
source back out of the representation it checks.

Two source forms are represented. A Spec file carries the complete XML plus
English reading blocks. A Guidelines chapter carries the complete XML plus one
verbatim source block per block-level unit, so that a distillate can anchor a
statement to a single heading or paragraph.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from xml.parsers import expat

import yaml

from tools.materialize_git_source import materialize

COMMIT = "113e933e21f016e2655518321e9d10214b8d9fcb"
SOURCE_ID = "teic-tei-p5-4.12.0"
SOURCE_DATE = "2026-07-28"
GIT_DIR = "corpus/raw/git/TEIC-TEI.git"
LOCK = "sources/locks/tei-p5-4.12.0.yaml"
UPSTREAM = "sources/manifests/2026-09-04-teic-tei-p5-4.12.0.yaml"
INVENTORY = "corpus/normalized/git/teic-tei-p5-4.12.0.json"
INVENTORY_HASH = "b2ae1cc64d77027d3cd766a8aa532db08c30f276d07494c62eb6d43a5fdb6476"
LICENSES = {
    "LICENSE.md": "8611900a8f6deaf45b44c39541e1a9c874b7ee61",
    "P5/COPYING.txt": "b5e5172a89b6dbffa557b9ba86c884a4ddbff493",
}
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"
SOURCE_MARKER = b"## Complete XML source\n\n```xml\n"
# In the Guidelines a div holds the block-level units; every other child is one.
BLOCK_CONTAINER = "div"
QUOTES = (0x22, 0x27)
TAG_CLOSE = 0x3E


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def blob_id(payload: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()


def _local(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def reading_blocks(payload: bytes) -> list[tuple[str, str]]:
    """Read XML as inert data; no entities, external schemas, or code run."""
    if b"<!DOCTYPE" in payload or b"<!ENTITY" in payload:
        raise ValueError("DTD/entity declarations are outside this converter's scope")
    root = ET.fromstring(payload)
    blocks: list[tuple[str, str]] = []

    def walk(element: ET.Element, locator: str, parent: ET.Element | None = None) -> None:
        tag = _local(element.tag)
        is_description = tag == "desc" and element.get(XML_LANG) == "en"
        is_remark = (
            tag == "p" and parent is not None
            and _local(parent.tag) == "remarks"
            and parent.get(XML_LANG) == "en"
        )
        if is_description or is_remark:
            blocks.append((locator, " ".join("".join(element.itertext()).split())))
        counts: dict[str, int] = {}
        for child in element:
            child_tag = _local(child.tag)
            counts[child_tag] = counts.get(child_tag, 0) + 1
            walk(child, f"{locator}/{child_tag}[{counts[child_tag]}]", element)

    walk(root, f"/{_local(root.tag)}[1]")
    return blocks


def _tag_end(payload: bytes, start: int) -> int:
    """Offset just past the tag opening at `start`; an attribute value may hold '>'."""
    quote = 0
    for index in range(start, len(payload)):
        byte = payload[index]
        if quote:
            if byte == quote:
                quote = 0
        elif byte in QUOTES:
            quote = byte
        elif byte == TAG_CLOSE:
            return index + 1
    raise ValueError("unterminated XML tag")


@dataclass
class _Open:
    """One element the block reader has entered but not yet closed."""

    tag: str
    begin: int
    locator: str
    structural: bool  # a div of the chapter itself, so its children are units
    counts: dict[str, int] = field(default_factory=dict)


def source_blocks(payload: bytes) -> list[tuple[str, str]]:
    """Block-level units of a Guidelines chapter, each as its verbatim source slice.

    Byte offsets come from the expat parser, so a block is the exact source text
    of its unit rather than a re-serialization that would normalize namespaces,
    entities and attribute whitespace. A unit is a non-div child of a div whose
    own ancestors are all divs, which in the Guidelines is one heading or one
    paragraph-level element. Nested examples and lists stay inside the paragraph
    that carries them, and a div inside an encoded example mints no unit of its
    own, so the units are disjoint and cover the chapter once.
    """
    if b"<!DOCTYPE" in payload or b"<!ENTITY" in payload:
        raise ValueError("DTD/entity declarations are outside this converter's scope")
    parser = expat.ParserCreate(namespace_separator="}")
    stack: list[_Open] = []
    root_counts: dict[str, int] = {}
    found: list[tuple[int, str, str]] = []

    def start(name: str, attributes: dict[str, str]) -> None:
        tag = _local(name)
        parent = stack[-1] if stack else None
        counts = parent.counts if parent else root_counts
        counts[tag] = counts.get(tag, 0) + 1
        locator = f"{parent.locator if parent else ''}/{tag}[{counts[tag]}]"
        structural = tag == BLOCK_CONTAINER and (parent is None or parent.structural)
        stack.append(_Open(tag, parser.CurrentByteIndex, locator, structural))

    def end(name: str) -> None:
        unit = stack.pop()
        if unit.tag == BLOCK_CONTAINER or not stack or not stack[-1].structural:
            return
        opened = _tag_end(payload, unit.begin)
        # Empty-element syntax ends with its own start tag; expat reports the end
        # tag position only where one was written.
        stop = (
            opened
            if payload[opened - 2 : opened] == b"/>"
            else _tag_end(payload, parser.CurrentByteIndex)
        )
        text = payload[unit.begin : stop].decode("utf-8")
        if not text.startswith("<") or not text.endswith((f"{unit.tag}>", "/>")):
            raise ValueError(f"block boundary does not enclose <{unit.tag}>: {text[:40]!r}")
        found.append((unit.begin, unit.locator, f"```xml\n{text}\n```\n"))

    parser.StartElementHandler = start
    parser.EndElementHandler = end
    parser.Parse(payload, True)
    found.sort()
    return [(locator, body) for _, locator, body in found]


@dataclass(frozen=True)
class Form:
    """How one kind of P5 source file is read and written as a representation."""

    converter: str  # conversion half of the representation's converter field
    explanation: str
    section: str  # heading of the block section
    label: str  # heading of one block
    id_prefix: str
    id_separator: str  # what stands between a block body and its block ID
    count_field: str  # manifest field naming what the blocks count
    authority: str
    blocks: Callable[[bytes], list[tuple[str, str]]]


SPEC = Form(
    converter="complete XML plus XML itertext English reading blocks with whitespace normalized",
    explanation=(
        "The XML below is the complete source, preserved as inert text, including all languages,\n"
        "examples, declarations, and processing instructions. A separator newline before the\n"
        "closing fence is not part of the source. The converter records the exact byte length.\n"
        "Reading blocks reproduce English descriptions and English remarks paragraphs using\n"
        "XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.\n"
        "They are reading projections of this source, not additional sources or interpretations.\n"
    ),
    section="English reading blocks",
    label="Reading",
    id_prefix="r",
    id_separator=" ",
    count_field="english_reading_blocks",
    authority="normative specification source at the pinned P5 4.12.0 release",
    blocks=reading_blocks,
)

CHAPTER = Form(
    converter="complete XML plus verbatim source blocks for every block-level unit",
    explanation=(
        "The XML below is the complete source, preserved as inert text, including all examples,\n"
        "declarations, processing instructions, and unresolved XInclude references. A separator\n"
        "newline before the closing fence is not part of the source. The converter records the\n"
        "exact byte length. Source blocks repeat the verbatim bytes of every block-level unit,\n"
        "one block per heading and per paragraph-level element in document order, so that a\n"
        "distillate can anchor a statement to a single unit. A nested example, list, or\n"
        "specification list stays inside the paragraph that carries it. The blocks locate\n"
        "passages of this source and carry no interpretation.\n"
    ),
    section="Source blocks",
    label="Block",
    id_prefix="b",
    id_separator="\n",
    count_field="source_blocks",
    authority="normative Guidelines prose chapter at the pinned P5 4.12.0 release",
    blocks=source_blocks,
)

FORMS = {"spec": SPEC, "chapter": CHAPTER}


@dataclass(frozen=True)
class Admission:
    """One locked Git blob and the immutable representation it becomes."""

    git_path: str
    blob: str
    size: int
    slug: str
    heading: str  # H1 of the representation, taken from the source
    title: str
    form: str

    @property
    def original(self) -> str:
        return f"00_sources/{self.slug}.xml"

    @property
    def rendered(self) -> str:
        return f"10_markdown/documents/{self.slug}.md"


@dataclass(frozen=True)
class Run:
    """One admission run, its manifest identity and the sources it admits."""

    run_id: str
    date: str
    adapter: str
    version: int
    manifest: str
    boundary: str
    status_applies_to: str
    known_limits: tuple[str, ...]
    admissions: tuple[Admission, ...]


ENTITIES = Run(
    run_id="2026-09-06-entities-admission",
    date="2026-09-06",
    adapter="tools.ingest_git_blobs",
    version=1,
    manifest="sources/manifests/2026-09-06-entities-admission.yaml",
    boundary=(
        "Exactly persName.xml, name.xml, rs.xml, person.xml, nym.xml, att.canonical.xml, "
        "att.naming.xml and relation.xml from P5/Source/Specs, and ND-NamesDates.xml from "
        "P5/Source/Guidelines/en, at the locked release commit"
    ),
    status_applies_to=(
        "nine selected complete Git blobs and their immutable representations only; "
        "neither the source family nor the topic Metadata and Entities"
    ),
    known_limits=(
        "No claim of complete P5 source-family acquisition; the published-HTML reconciliation "
        "remains separate.",
        "The nine admitted files do not exhaust the P5 sources bearing on metadata and entities; "
        "further specs, classes and chapters remain unadmitted.",
        "The Guidelines chapter keeps its XInclude references unresolved, so every specification "
        "it pulls in is a separate admission with its own representation.",
    ),
    admissions=(
        Admission(
            git_path="P5/Source/Specs/persName.xml",
            blob="ffbe47c37070e255c1c7fa0238bbdcaf7aa97646",
            size=4600,
            slug="tei-p5-persname-4.12.0",
            heading="persName",
            title="TEI P5 4.12.0 persName specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/name.xml",
            blob="57c610d9430e9a48113d4e9f994bc0bbb9ca2486",
            size=4047,
            slug="tei-p5-name-4.12.0",
            heading="name",
            title="TEI P5 4.12.0 name specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/rs.xml",
            blob="77fb7d96af0c2294b541237bf17193fb7aa17c4f",
            size=3384,
            slug="tei-p5-rs-4.12.0",
            heading="rs",
            title="TEI P5 4.12.0 rs specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/person.xml",
            blob="8aff4c8dd02eb6b8d5609f62eb9e6e03000fcd4d",
            size=13105,
            slug="tei-p5-person-4.12.0",
            heading="person",
            title="TEI P5 4.12.0 person specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/nym.xml",
            blob="16a0f11f5fa5202048d2b93e204e60bd0e03530f",
            size=4085,
            slug="tei-p5-nym-4.12.0",
            heading="nym",
            title="TEI P5 4.12.0 nym specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/att.canonical.xml",
            blob="2682bdddfa0d9223aeffd45566b825f895b050c5",
            size=9162,
            slug="tei-p5-att.canonical-4.12.0",
            heading="att.canonical",
            title="TEI P5 4.12.0 att.canonical specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/att.naming.xml",
            blob="43887df614b32c49625a2fabfd7ecb4e6521c8ad",
            size=5936,
            slug="tei-p5-att.naming-4.12.0",
            heading="att.naming",
            title="TEI P5 4.12.0 att.naming specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/relation.xml",
            blob="5500905fd424e5f31a8199b62d72793f91e1f2de",
            size=11422,
            slug="tei-p5-relation-4.12.0",
            heading="relation",
            title="TEI P5 4.12.0 relation specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Guidelines/en/ND-NamesDates.xml",
            blob="dffadd4774bec9cfa6337b089446e3c94c3b0c2a",
            size=208781,
            slug="tei-p5-guidelines-nd-4.12.0",
            heading="Names, Dates, People, and Places",
            title="TEI P5 4.12.0 Guidelines chapter Names, Dates, People, and Places",
            form="chapter",
        ),
    ),
)


def verify_payload(admission: Admission, payload: bytes) -> None:
    if len(payload) != admission.size or blob_id(payload) != admission.blob:
        raise ValueError(f"{admission.slug}: bytes do not match the admitted Git blob")


def representation(run: Run, admission: Admission, payload: bytes) -> bytes:
    verify_payload(admission, payload)
    form = FORMS[admission.form]
    frontmatter = {
        "type": "representation", "source-type": "document",
        "source": f"[[{admission.original}]]",
        "converter": f"{run.adapter} v{run.version}; {form.converter}",
        "channel": "collection",
        "metadata": {
            "title": admission.title,
            "creator": "TEI Consortium", "date": SOURCE_DATE, "format": "application/xml",
            "identifier": f"https://github.com/TEIC/TEI/blob/{COMMIT}/{admission.git_path}",
            "license": "CC-BY-3.0", "confidential": False,
        },
        "created": run.date, "updated": run.date,
    }
    header = "---\n" + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True) + "---\n\n"
    header += f"# {admission.heading}\n\n"
    header += (
        "Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.\n"
        f"License records: `LICENSE.md` and `P5/COPYING.txt` at commit `{COMMIT}`.\n\n"
        f"{form.explanation}\n"
        f"Source byte length: {len(payload)}. Git blob: `{blob_id(payload)}`.\n\n"
    )
    result = header.encode("utf-8") + SOURCE_MARKER + payload
    result += f"\n```\n\n## {form.section}\n\n".encode()
    for index, (locator, body) in enumerate(form.blocks(payload), 1):
        result += (
            f"### {form.label} {index}\n\nXML location: `{locator}`.\n\n"
            f"{body}{form.id_separator}^{form.id_prefix}{index}\n\n"
        ).encode()
    return result


def embedded_source(admission: Admission, rendered: bytes) -> bytes:
    if rendered.count(SOURCE_MARKER) != 1:
        raise ValueError(f"{admission.slug}: missing or duplicate complete XML source block")
    start = rendered.index(SOURCE_MARKER) + len(SOURCE_MARKER)
    stop = start + admission.size
    payload = rendered[start:stop]
    if rendered[stop:stop + 5] != b"\n```\n":
        raise ValueError(f"{admission.slug}: malformed complete XML source boundary")
    verify_payload(admission, payload)
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


def pinned_inventory(root: Path) -> dict[str, str]:
    """The pinned upstream Git inventory, after the lock and license checks."""
    lock = yaml.safe_load((root / LOCK).read_text(encoding="utf-8"))
    upstream = yaml.safe_load((root / UPSTREAM).read_text(encoding="utf-8"))
    if lock["release"]["resolved_full_commit_sha"] != COMMIT or upstream["status"] != "observable-complete":
        raise ValueError("locked commit or completed upstream Git acquisition does not match")
    payload = (root / INVENTORY).read_bytes()
    if sha256(payload) != INVENTORY_HASH:
        raise ValueError("upstream Git inventory checksum mismatch")
    inventory = {entry["path"]: entry["object_id"] for entry in json.loads(payload)["entries"]}
    for path, expected in LICENSES.items():
        if inventory.get(path) != expected:
            raise ValueError(f"license blob mismatch: {path}")
    return inventory


def _now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def admit(root: Path, run: Run, check: bool = False) -> None:
    inventory = pinned_inventory(root)
    manifest_path = root / run.manifest
    existing = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else None
    started = existing["started_at"] if existing else _now()
    admissions = []
    objects = []
    requests = []
    git_dir = root / GIT_DIR
    for admission in run.admissions:
        form = FORMS[admission.form]
        if inventory.get(admission.git_path) != admission.blob:
            raise ValueError(f"inventory blob mismatch: {admission.git_path}")
        original, rendered = root / admission.original, root / admission.rendered
        if check:
            payload = embedded_source(admission, rendered.read_bytes())
            if original.exists() and original.read_bytes() != payload:
                raise ValueError(f"changed immutable original: {admission.original}")
        else:
            materialize(git_dir, COMMIT, admission.git_path, original, admission.blob)
            payload = original.read_bytes()
        output = representation(run, admission, payload)
        immutable_output(rendered, output, check)
        requests.append({"kind": "locked-git-blob-admission", "commit": COMMIT, "path": admission.git_path, "blob_id": admission.blob})
        objects.append({"kind": "markdown-representation", "path": admission.rendered, "sha256": sha256(output)})
        admissions.append({
            "source_type": "document", "git_path": admission.git_path, "commit": COMMIT,
            "original_path": admission.original, "original_bytes": len(payload),
            "original_sha256": sha256(payload), "git_blob_id": admission.blob,
            "representation_path": admission.rendered, "representation_sha256": sha256(output),
            form.count_field: len(form.blocks(payload)),
            "content_authority": form.authority,
            "instruction_trust": "none",
        })
    finished = existing["finished_at"] if existing else _now()
    manifest = {
        "schema_version": 1, "run_id": run.run_id,
        "source_id": SOURCE_ID, "started_at": started, "finished_at": finished,
        "status": "bounded-complete",
        "scope": {"boundary": run.boundary, "status_applies_to": run.status_applies_to},
        "adapter": {"name": run.adapter, "version": run.version},
        "lock_file": LOCK, "upstream_manifest": UPSTREAM, "upstream_inventory_sha256": INVENTORY_HASH,
        "requests": requests, "objects": objects,
        "counts": {"admitted_sources": len(admissions), "representations": len(objects), "original_bytes": sum(item["original_bytes"] for item in admissions)},
        "gaps": [], "rights_exceptions": [],
        "known_limits": list(run.known_limits),
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


def cli(run: Run, description: str | None) -> int:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("root", nargs="?", type=Path, default=Path())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        admit(args.root.resolve(), run, args.check)
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(f"OK: {len(run.admissions)} immutable source admissions and representations reconcile")
    return 0


def main() -> int:
    return cli(ENTITIES, __doc__)


if __name__ == "__main__":
    raise SystemExit(main())
