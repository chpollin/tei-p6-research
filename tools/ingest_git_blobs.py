"""Admit locked Git blobs of a pinned mirror as immutable Markdown representations.

One admission list drives the whole chain, so the pilot in
``tools.ingest_text_identity`` and every later topic run share this code. Run with
``python -m tools.ingest_git_blobs``; ``--check`` is read-only and works without
the ignored originals and without the mirror, because it reads the complete
source back out of the representation it checks. ``--run`` selects one of the
admission runs in ``RUNS``; without it the first entity run is reconciled.

Three source forms are represented. A Spec file carries the complete XML plus
English reading blocks. A Guidelines chapter and a Test document carry the
complete XML plus one verbatim source block per unit, a heading or paragraph in
the chapter and a record or body element in the test document, so that a
distillate can anchor a statement to a single unit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from collections.abc import Callable
from dataclasses import dataclass, field, replace
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
GUIDELINES_CONTAINERS = frozenset({BLOCK_CONTAINER})
# In a P5 test document these elements only group. Every other child of one is a
# unit, so a person or nym record and a body paragraph are separately anchorable.
TEST_CONTAINERS = frozenset({
    "TEI", "teiHeader", "fileDesc", "titleStmt", "editionStmt", "publicationStmt",
    "sourceDesc", "text", "body", "front", "back", "group", "div",
    "listNym", "listPerson", "listPlace", "listOrg", "listEvent", "listRelation",
})
QUOTES = (0x22, 0x27)
TAG_CLOSE = 0x3E


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def blob_id(payload: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()


def _local(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def reading_blocks(payload: bytes, *, identified: bool = False) -> list[tuple[str, str]]:
    """Read XML as inert data; no entities, external schemas, or code run.

    With ``identified`` the locator names an element carrying an ``ident``
    attribute by that ident instead of by position, so a reading block of an
    attribute definition says which attribute it describes.
    """
    if b"<!DOCTYPE" in payload or b"<!ENTITY" in payload:
        raise ValueError("DTD/entity declarations are outside this converter's scope")
    root = ET.fromstring(payload)
    blocks: list[tuple[str, str]] = []

    def step(element: ET.Element, tag: str, position: int) -> str:
        ident = element.get("ident") if identified else None
        return f"{tag}[@ident='{ident}']" if ident else f"{tag}[{position}]"

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
            walk(child, f"{locator}/{step(child, child_tag, counts[child_tag])}", element)

    walk(root, f"/{step(root, _local(root.tag), 1)}")
    return blocks


def identified_reading_blocks(payload: bytes) -> list[tuple[str, str]]:
    return reading_blocks(payload, identified=True)


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


def source_blocks(
    payload: bytes, containers: frozenset[str] = GUIDELINES_CONTAINERS
) -> list[tuple[str, str]]:
    """Block-level units of one source file, each as its verbatim source slice.

    Byte offsets come from the expat parser, so a block is the exact source text
    of its unit rather than a re-serialization that would normalize namespaces,
    entities and attribute whitespace. A unit is a child of a container whose own
    ancestors are all containers and which is not itself a container, so in the
    Guidelines it is one heading or one paragraph-level element and in a test
    document one record or one body element. Nested examples and lists stay
    inside the unit that carries them, and a container inside a unit mints no
    unit of its own, so the units are disjoint and cover the file once.
    """
    parser = expat.ParserCreate(namespace_separator="}")
    def reject_declaration(*args: object) -> None:
        raise ValueError("DTD/entity declarations are outside this converter's scope")

    parser.StartDoctypeDeclHandler = reject_declaration
    parser.EntityDeclHandler = reject_declaration
    stack: list[_Open] = []
    root_counts: dict[str, int] = {}
    found: list[tuple[int, str, str]] = []

    def start(name: str, attributes: dict[str, str]) -> None:
        tag = _local(name)
        parent = stack[-1] if stack else None
        counts = parent.counts if parent else root_counts
        counts[tag] = counts.get(tag, 0) + 1
        locator = f"{parent.locator if parent else ''}/{tag}[{counts[tag]}]"
        structural = tag in containers and (parent is None or parent.structural)
        stack.append(_Open(tag, parser.CurrentByteIndex, locator, structural))

    def end(name: str) -> None:
        unit = stack.pop()
        if unit.tag in containers or not stack or not stack[-1].structural:
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


def record_blocks(payload: bytes) -> list[tuple[str, str]]:
    return source_blocks(payload, TEST_CONTAINERS)


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

# Converter version 2 of the specification form: locators name identified
# elements by their ident, so a reading block of an attribute definition says
# which attribute it describes without recourse to the complete XML.
SPEC_IDENTIFIED = replace(
    SPEC,
    converter=(
        "complete XML plus XML itertext English reading blocks with whitespace normalized "
        "and identified locators"
    ),
    explanation=SPEC.explanation
    + (
        "A locator names an element that carries an `ident` attribute by that ident, so the\n"
        "reading block of an attribute definition states which attribute it describes.\n"
    ),
    blocks=identified_reading_blocks,
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

# A P5 test document has no div at all, so the chapter form would find no unit in
# it. The unit is the record or the body element the document's grouping elements
# hold, which is what a distillate of encoded practice anchors a statement to.
TEST_DOCUMENT = replace(
    CHAPTER,
    converter="complete XML plus verbatim source blocks for every record and body unit",
    explanation=(
        "The XML below is the complete source, preserved as inert text, including all encoded\n"
        "records, declarations, and processing instructions. A separator newline before the closing\n"
        "fence is not part of the source. The converter records the exact byte length. Source blocks\n"
        "repeat the verbatim bytes of every unit the grouping elements of the document hold, one\n"
        "block per record of a list and per element of the body in document order, so that a\n"
        "distillate can anchor a statement to a single encoded record or paragraph. A nested list\n"
        "stays inside the record that carries it. The blocks locate passages of this source and\n"
        "carry no interpretation.\n"
    ),
    authority=(
        "test document of the pinned P5 4.12.0 release; encoded practice of the release, "
        "not a normative specification or Guidelines statement"
    ),
    blocks=record_blocks,
)

FORMS = {
    "spec": SPEC,
    "spec-identified": SPEC_IDENTIFIED,
    "chapter": CHAPTER,
    "test-document": TEST_DOCUMENT,
}


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
    rights_note: str = ""  # per-file rights review, where the run recorded one

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
    version=2,
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
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/name.xml",
            blob="57c610d9430e9a48113d4e9f994bc0bbb9ca2486",
            size=4047,
            slug="tei-p5-name-4.12.0",
            heading="name",
            title="TEI P5 4.12.0 name specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/rs.xml",
            blob="77fb7d96af0c2294b541237bf17193fb7aa17c4f",
            size=3384,
            slug="tei-p5-rs-4.12.0",
            heading="rs",
            title="TEI P5 4.12.0 rs specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/person.xml",
            blob="8aff4c8dd02eb6b8d5609f62eb9e6e03000fcd4d",
            size=13105,
            slug="tei-p5-person-4.12.0",
            heading="person",
            title="TEI P5 4.12.0 person specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/nym.xml",
            blob="16a0f11f5fa5202048d2b93e204e60bd0e03530f",
            size=4085,
            slug="tei-p5-nym-4.12.0",
            heading="nym",
            title="TEI P5 4.12.0 nym specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/att.canonical.xml",
            blob="2682bdddfa0d9223aeffd45566b825f895b050c5",
            size=9162,
            slug="tei-p5-att.canonical-4.12.0",
            heading="att.canonical",
            title="TEI P5 4.12.0 att.canonical specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/att.naming.xml",
            blob="43887df614b32c49625a2fabfd7ecb4e6521c8ad",
            size=5936,
            slug="tei-p5-att.naming-4.12.0",
            heading="att.naming",
            title="TEI P5 4.12.0 att.naming specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/relation.xml",
            blob="5500905fd424e5f31a8199b62d72793f91e1f2de",
            size=11422,
            slug="tei-p5-relation-4.12.0",
            heading="relation",
            title="TEI P5 4.12.0 relation specification",
            form="spec-identified",
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


ENTITIES_RUN2 = Run(
    run_id="2026-09-06-entities-run2-admission",
    date="2026-09-06",
    adapter="tools.ingest_git_blobs",
    version=2,
    manifest="sources/manifests/2026-09-06-entities-run2-admission.yaml",
    boundary=(
        "Exactly att.personal.xml, att.global.responsibility.xml, att.global.source.xml, "
        "att.editLike.xml, att.datable.xml, idno.xml, place.xml and state.xml from "
        "P5/Source/Specs, and testnames.xml from P5/Test, at the locked release commit"
    ),
    status_applies_to=(
        "nine selected complete Git blobs and their immutable representations only; "
        "neither the source family nor the topic Metadata and Entities"
    ),
    known_limits=(
        "No claim of complete P5 source-family acquisition; the published-HTML reconciliation "
        "remains separate.",
        "The nine admitted files do not exhaust the P5 sources bearing on metadata and entities; "
        "org.xml, trait.xml, event.xml, placeName.xml, orgName.xml, att.datable.w3c.xml, "
        "testplace.xml, names-demo-en.xml, testnym.odd and the CE, HD and CO chapters stand "
        "deferred under the admission budget of the run.",
        "The three GitHub threads of the same run are citation-only publications and enter "
        "through sources/manifests/2026-09-06-entities-run2-citations.yaml, not through this "
        "manifest.",
        "A test document records encoded practice of the release. It states no rule, and its "
        "usage establishes neither a Guidelines statement nor editorial practice outside the "
        "release.",
    ),
    admissions=(
        Admission(
            git_path="P5/Source/Specs/att.personal.xml",
            blob="da9ebd55d9ee07a9ecc0f5d7c6d066f9981585cd",
            size=8885,
            slug="tei-p5-att.personal-4.12.0",
            heading="att.personal",
            title="TEI P5 4.12.0 att.personal specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/att.global.responsibility.xml",
            blob="65688b68bc20ebdc18452ae2b285d581542e2363",
            size=6738,
            slug="tei-p5-att.global.responsibility-4.12.0",
            heading="att.global.responsibility",
            title="TEI P5 4.12.0 att.global.responsibility specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/att.global.source.xml",
            blob="99eff95e2ef18a407b64fb7f59932bc23334e664",
            size=6791,
            slug="tei-p5-att.global.source-4.12.0",
            heading="att.global.source",
            title="TEI P5 4.12.0 att.global.source specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/att.editLike.xml",
            blob="125dd51d6ec3328982d02edc0740d71638ccfa2e",
            size=8092,
            slug="tei-p5-att.editlike-4.12.0",
            heading="att.editLike",
            title="TEI P5 4.12.0 att.editLike specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/att.datable.xml",
            blob="0e2c292bc3d894906785e91eed96c327c3f06ef2",
            size=6953,
            slug="tei-p5-att.datable-4.12.0",
            heading="att.datable",
            title="TEI P5 4.12.0 att.datable specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/idno.xml",
            blob="2566cd875ae59e472cefee625ba5cb3602c61464",
            size=9600,
            slug="tei-p5-idno-4.12.0",
            heading="idno",
            title="TEI P5 4.12.0 idno specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/place.xml",
            blob="04fd590ffcf6f1ecd9e40d227b78407fdc1e0774",
            size=2848,
            slug="tei-p5-place-4.12.0",
            heading="place",
            title="TEI P5 4.12.0 place specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Source/Specs/state.xml",
            blob="b9e91d5cb159d59dfbd3ea9a6c08a9a395bc3f5b",
            size=5895,
            slug="tei-p5-state-4.12.0",
            heading="state",
            title="TEI P5 4.12.0 state specification",
            form="spec-identified",
        ),
        Admission(
            git_path="P5/Test/testnames.xml",
            blob="caee4124268148fd7504df39fb42f7760a568d20",
            size=73926,
            slug="tei-p5-test-testnames-4.12.0",
            heading="testnames",
            title="TEI P5 4.12.0 test document testnames.xml",
            form="test-document",
            rights_note=(
                "Per-file review of 2026-09-06: the file carries no notice of its own and stands "
                "inside the release the two license records cover, so the release rights apply "
                "to it; its person, nym and place records are the release's own test material "
                "and name no rights holder beyond the TEI Consortium."
            ),
        ),
    ),
)

RUNS = {"entities": ENTITIES, "entities-run2": ENTITIES_RUN2}


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
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_bytes(payload)
        temporary.replace(path)


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
        entry = {
            "source_type": "document", "git_path": admission.git_path, "commit": COMMIT,
            "original_path": admission.original, "original_bytes": len(payload),
            "original_sha256": sha256(payload), "git_blob_id": admission.blob,
            "representation_path": admission.rendered, "representation_sha256": sha256(output),
            form.count_field: len(form.blocks(payload)),
            "content_authority": form.authority,
            "instruction_trust": "none",
        }
        if admission.rights_note:
            entry["rights_review"] = admission.rights_note
        admissions.append(entry)
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


def cli(run: Run, description: str | None, runs: dict[str, Run] | None = None) -> int:
    """One admission run; ``runs`` offers --run and ``run`` stays the default."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("root", nargs="?", type=Path, default=Path())
    parser.add_argument("--check", action="store_true")
    if runs:
        parser.add_argument("--run", choices=sorted(runs), help="admission run to reconcile")
    args = parser.parse_args()
    selected = runs[args.run] if runs and args.run else run
    try:
        admit(args.root.resolve(), selected, args.check)
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(
        f"OK: {len(selected.admissions)} immutable source admissions and representations "
        f"reconcile for {selected.run_id}"
    )
    return 0


def main() -> int:
    return cli(ENTITIES, __doc__, RUNS)


if __name__ == "__main__":
    raise SystemExit(main())
