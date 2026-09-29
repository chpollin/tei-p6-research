"""Admit the purposive ODD and processing practice contrast sample of 2026-09-11.

Three public cases are pinned to full commits: DraCor, EpiDoc with the I.Sicily
corpus, and CMIF with correspSearch. Each contributes one ODD, one processing
context and one real input document as an immutable representation with exact
reading blocks. License and pipeline files are fetched into the ignored raw
store as context observations and are never admitted. Nothing fetched is
executed; XML is parsed only for well-formedness and a deterministic inventory.

``python -m tools.ingest_practice_v1`` acquires once, ``--reproduce`` refetches
every recorded request and compares hashes without writing tracked files, and
``--check`` reconciles the tracked admission offline. The selection record is
workbench/selections/2026-09-11-odd-practice.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from collections.abc import Callable
from pathlib import Path
from urllib.parse import quote

import yaml

from tools.corpus.http_store import HttpStore, utc_now
from tools.corpus.manifest import sha256_bytes as digest

ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "2026-09-11-practice-v1-admission"
SOURCE_ID = "tei-real-world-customizations"
DATE = "2026-09-11"
MANIFEST = Path(f"sources/manifests/{RUN_ID}.yaml")
NORMALIZED = Path("corpus/normalized/practice-v1/admission-2026-09-11.json")
SELECTION = "workbench/selections/2026-09-11-odd-practice.md"
ADAPTER = "tools.ingest_practice_v1"
TEI = "{http://www.tei-c.org/ns/1.0}"
SCH = "{http://purl.oclc.org/dsdl/schematron}"
XI = "{http://www.w3.org/2001/XInclude}"
WRAP = ('<fragment xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" '
        'xmlns:xi="http://www.w3.org/2001/XInclude" xmlns:rng="http://relaxng.org/ns/structure/1.0">')
BLOCK_LIKE = re.compile(rb"\^[A-Za-z0-9-]+[ \t]*$", re.MULTILINE)
XML_MODEL = re.compile(rb"<\?xml-model\s.*?\?>", re.DOTALL)

DRACOR, GERDRACOR = "dracor-org/dracor-schema", "dracor-org/gerdracor"
DRACOR_SHA, GERDRACOR_SHA = "c2f9e8140bf413cb3bce44abc818d563ddc92d88", "43fe19012bae4784689ce7ad5855dfdd643364e5"
EPIDOC, ISICILY = "EpiDoc/Source", "ISicily/ISicily"
EPIDOC_SHA, ISICILY_SHA = "e5b68eb8627ac1bc55a4f9f2bec94d8276ff74b3", "262784ad8b4d4ee5a203abc0a772ae3eea289997"
CMIF, CSAPI, CSSTORAGE = "TEI-Correspondence-SIG/CMIF", "correspSearch/csAPI", "correspSearch/csStorage"
CMIF_SHA, CSAPI_SHA = "d171133e2ca7a0b987ba0564577ec79077b8d908", "566b2d29233e3be332dc749266558cb7383cd31d"
CSSTORAGE_SHA = "9a7ebe3b68bb464be64d6e08fe1ed8672f90c00d"


def frag(identifier: str, label: str, start: str, end: str, kind: str, occurrence: int = 1) -> dict:
    return {"id": identifier, "label": label, "start": start, "end": end, "kind": kind, "occurrence": occurrence}


SOURCES: list[dict] = [
    {"slug": "practice-v1-dracor-odd-c2f9e814", "case": "dracor", "role": "odd", "repository": DRACOR,
     "commit": DRACOR_SHA, "path": "dracor.odd", "language": "xml", "date": "2026-08-03",
     "title": "DraCor ODD (dracor.odd)", "creator": "DraCor project (dracor-org)",
     "license": "CC-BY-4.0",
     "license_evidence": ["LICENSE and README.md section License at the pinned commit"],
     "attribution": "DraCor Schema, dracor.org, CC BY 4.0; ODD authors and guideline contributors are named in the source header.",
     "fragments": [
         frag("r1", "schemaSpec start and module selection", '<schemaSpec ident="dracor"',
              '<moduleRef key="transcr" include="addSpan damageSpan delSpan ellipsis space"/>', "interval"),
         frag("r2", "deleted attribute classes", '<classSpec module="core" type="atts" ident="att.datable.custom" mode="delete"/>',
              '<classSpec type="atts" ident="att.declarable" mode="delete"/>', "interval"),
         frag("r3", "Schematron constraint on schema association", '<constraintSpec ident="xml_model_or_type_dracor_on_root_tei_element"',
              "</constraintSpec>", "element"),
         frag("r4", "added corpus root element", '<elementSpec ident="dracorCorpus" mode="add">', "</elementSpec>", "element"),
     ]},
    {"slug": "practice-v1-dracor-build-c2f9e814", "case": "dracor", "role": "processing", "repository": DRACOR,
     "commit": DRACOR_SHA, "path": "build", "language": "sh", "date": "2026-08-03",
     "title": "DraCor schema build script (build)", "creator": "DraCor project (dracor-org)",
     "license": "CC-BY-4.0",
     "license_evidence": ["repository LICENSE at the pinned commit; README.md scopes CC BY 4.0 to the DraCor Schema"],
     "attribution": "DraCor Schema repository, dracor.org, CC BY 4.0.",
     "fragments": [
         frag("r1", "Stylesheets submodule location", "BIN=./Stylesheets/bin", "  git submodule update\nfi", "interval"),
         frag("r2", "Java XML entity limits", "# In JDK 24/25", '-Djdk.xml.totalEntitySizeLimit=0"', "interval"),
         frag("r3", "ODD, RELAX NG and Schematron generation", "# Generate full ODD",
              "$BIN/teitoschematron --odd dist/dracor.odd.tmp dist/dracor.sch", "interval"),
     ]},
    {"slug": "practice-v1-gerdracor-ger000260-43fe1901", "case": "dracor", "role": "input", "repository": GERDRACOR,
     "commit": GERDRACOR_SHA, "path": "tei/leisewitz-die-pfandung.xml", "language": "xml", "date": "2026-01-24",
     "title": "GerDraCor play ger000260 (tei/leisewitz-die-pfandung.xml)", "creator": "DraCor project (GerDraCor)",
     "license": "CC0-1.0",
     "license_evidence": ["README.md and CITATION.cff at the pinned commit", "publicationStmt/availability/licence in the file"],
     "attribution": "German Drama Corpus (GerDraCor), CC0 1.0; the file names its digital source and original print source.",
     "fragments": [
         frag("r1", "schema association processing instruction", '<?xml-model href="https://dracor.org/schema.rng"', "?>", "processing-instruction"),
         frag("r2", "file licence", "<availability>", "</availability>", "element"),
         frag("r3", "participant description", "<particDesc>", "</particDesc>", "element"),
         frag("r4", "first speech", '<sp who="#der_mann">', "</sp>", "element"),
     ]},
    {"slug": "practice-v1-epidoc-odd-e5b68eb8", "case": "epidoc", "role": "odd", "repository": EPIDOC,
     "commit": EPIDOC_SHA, "path": "schema/tei-epidoc.xml", "language": "xml", "date": "2026-01-26",
     "title": "EpiDoc ODD (schema/tei-epidoc.xml)", "creator": "EpiDoc community (EpiDoc/Source contributors)",
     "license": "GPL-2.0-or-later (file header); schema/LICENSE.txt states GPL-3.0-or-later",
     "license_evidence": ["license comment at the start of the file", "schema/LICENSE.txt and schema/README.txt at the pinned commit"],
     "attribution": "EpiDoc Schema, contributors listed in the source titleStmt and revisionDesc; GPL.",
     "fragments": [
         frag("r1", "license statement comment", "<!-- Start license statement", "-->", "comment"),
         frag("r2", "latest release alignment entry", '<change who="#SV" when="2026-01-26">', "</change>", "element"),
         frag("r3", "schemaSpec start and module selection", '<schemaSpec ident="tei-epidoc"',
              'superEntry syll tns usg xr"/>', "interval"),
         frag("r4", "changed gap element", '<elementSpec ident="gap" module="core" mode="change">', "</elementSpec>", "element"),
         frag("r5", "changed responsibility attribute class", '<classSpec type="atts" ident="att.responsibility" mode="change">',
              "</classSpec>", "element"),
     ]},
    {"slug": "practice-v1-epidoc-schema-readme-e5b68eb8", "case": "epidoc", "role": "processing", "repository": EPIDOC,
     "commit": EPIDOC_SHA, "path": "schema/README.txt", "language": "text", "date": "2026-01-26",
     "title": "README for the EpiDoc ODD and schema (schema/README.txt)", "creator": "EpiDoc community (EpiDoc/Source contributors)",
     "license": "GPL-3.0-or-later",
     "license_evidence": ["schema/LICENSE.txt, which the README names for license details"],
     "attribution": "EpiDoc Schema documentation, EpiDoc/Source; GPL.",
     "fragments": [
         frag("r1", "what it is", "What it is:", "from which it is generated.", "interval"),
         frag("r2", "license", "License:", "See LICENSE.txt for license details.", "interval"),
         frag("r3", "technical requirements", "Technical Requirements:", "processing environment to validate EpiDoc XML files.", "interval"),
         frag("r4", "generating a new schema version", "2. To generate a new version of the schema from the ODD:",
              '"RELAX NG Schema" to "Compiled ODD Document"', "interval"),
         frag("r5", "choosing a schema version", "3. How to decide which schema to use:",
              "which will be updated whenever a new schema is released.", "interval"),
     ]},
    {"slug": "practice-v1-isicily-isic000156-262784ad", "case": "epidoc", "role": "input", "repository": ISICILY,
     "commit": ISICILY_SHA, "path": "inscriptions/ISic000156.xml", "language": "xml", "date": "2026-07-29",
     "title": "I.Sicily inscription ISic000156 (inscriptions/ISic000156.xml)", "creator": "I.Sicily project, University of Oxford",
     "license": "CC-BY-4.0",
     "license_evidence": ["licence.txt at the pinned commit", "publicationStmt/availability/licence in the file"],
     "attribution": "I.Sicily, CC BY 4.0; editors and contributors are named in the source titleStmt.",
     "fragments": [
         frag("r1", "schema association processing instructions", '<?xml-model href="https://epidoc.stoa.org/schema/latest/tei-epidoc.rng"',
              'schematypens="http://purl.oclc.org/dsdl/schematron"?>', "interval"),
         frag("r2", "file licence", "<availability>", "</availability>", "element"),
         frag("r3", "date of origin", "<origDate", "</origDate>", "element"),
         frag("r4", "encoding description with XIncludes", "<encodingDesc>", "</encodingDesc>", "element"),
         frag("r5", "revision status", '<revisionDesc status="edited">', '<revisionDesc status="edited">', "start-tag"),
         frag("r6", "primary edition", '<div type="edition" subtype="primary"', "</div>", "element"),
     ]},
    {"slug": "practice-v1-cmif-odd-d171133e", "case": "cmif", "role": "odd", "repository": CMIF,
     "commit": CMIF_SHA, "path": "odd/cmi-customization.odd", "language": "xml", "date": "2025-02-26",
     "title": "CMIF ODD (odd/cmi-customization.odd)", "creator": "TEI Correspondence SIG",
     "license": "CC-BY-4.0 OR BSD-2-Clause",
     "license_evidence": ["LICENSE CC-BY, LICENSE BSD 2-Clause, README.md and CITATION.cff at the pinned commit"],
     "attribution": "Correspondence Metadata Interchange Format (CMIF) 1.1, TEI Correspondence SIG 2015-2025, CC BY 4.0 or BSD-2-Clause.",
     "fragments": [
         frag("r1", "schemaSpec start and module selection", '<schemaSpec ident="cmi-customization"',
              '<moduleRef key="namesdates" include="persName orgName placeName" />', "interval"),
         frag("r2", "replaced att.editLike", '<classSpec ident="att.editLike"', "</classSpec>", "element"),
         frag("r3", "changed correspAction", '<elementSpec ident="correspAction" mode="change" module="header">', "</elementSpec>", "element"),
         frag("r4", "replaced idno", '<elementSpec ident="idno" mode="replace" module="header">', "</elementSpec>", "element"),
         frag("r5", "changed persName", '<elementSpec ident="persName" mode="change" module="namesdates">', "</elementSpec>", "element"),
         frag("r6", "revision of 2025-02-26", '<change when="2025-02-26">', "</change>", "element"),
     ]},
    {"slug": "practice-v1-correspsearch-check-566b2d29", "case": "cmif", "role": "processing", "repository": CSAPI,
     "commit": CSAPI_SHA, "path": "api/v2.0/services/check/index.xql", "language": "xquery", "date": "2024-07-20",
     "title": "correspSearch CMIF check service (api/v2.0/services/check/index.xql)",
     "creator": "Berlin-Brandenburg Academy of Sciences and Humanities (correspSearch)",
     "license": "LGPL-3.0-or-later",
     "license_evidence": ["LICENSE, README.md section License and CITATION.cff at the pinned commit"],
     "attribution": "csAPI, correspSearch, Berlin-Brandenburg Academy of Sciences and Humanities 2024, LGPL-3.0-or-later.",
     "fragments": [
         frag("r1", "imported validation modules", "import module namespace schxslt", 'at "check-geonames.xql";', "interval"),
         frag("r2", "input from upload or URL", "let $xml-data :=", "else $xml-data", "interval"),
         frag("r3", "applied checks and rendering", "let $checks :=", "transform:transform($checks, doc('view.xsl'), ())", "interval"),
     ]},
    {"slug": "practice-v1-cmif-freieisen-stoeber-9a7ebe3b", "case": "cmif", "role": "input", "repository": CSSTORAGE,
     "commit": CSSTORAGE_SHA, "path": "freieisen-stoeber.xml", "language": "xml", "date": "2026-03-10",
     "title": "CMIF file in correspSearch storage (freieisen-stoeber.xml)", "creator": "correspSearch storage; publisher named in the source header",
     "license": "CC-BY-4.0",
     "license_evidence": ["publicationStmt/availability/licence in the file; the repository has no license file"],
     "attribution": "CMIF file freieisen-stoeber.xml, correspSearch storage, CC BY 4.0; publisher and cited print source are named in the source header.",
     "fragments": [
         frag("r1", "document start", '<TEI xmlns="http://www.tei-c.org/ns/1.0">', '<TEI xmlns="http://www.tei-c.org/ns/1.0">', "start-tag"),
         frag("r2", "file licence", "<availability>", "</availability>", "element"),
         frag("r3", "correspondence description", "<correspDesc", "</correspDesc>", "element"),
     ]},
]


def context(identifier: str, case: str, repository: str, commit: str, path: str, rights: str, reason: str) -> dict:
    return {"id": identifier, "case": case, "repository": repository, "commit": commit, "path": path,
            "rights": rights, "reason": reason}


CONTEXTS: list[dict] = [
    context("dracor-license", "dracor", DRACOR, DRACOR_SHA, "LICENSE", "CC-BY-4.0", "license evidence"),
    context("dracor-readme", "dracor", DRACOR, DRACOR_SHA, "README.md", "CC-BY-4.0", "license and build documentation"),
    context("dracor-test-workflow", "dracor", DRACOR, DRACOR_SHA, ".github/workflows/test.yml", "CC-BY-4.0",
            "observed CI configuration; kept local to limit the admission budget"),
    context("gerdracor-readme", "dracor", GERDRACOR, GERDRACOR_SHA, "README.md", "CC0-1.0 declared for the corpus", "license evidence"),
    context("gerdracor-validation-workflow", "dracor", GERDRACOR, GERDRACOR_SHA, ".github/workflows/validation.yml",
            "unclear: no repository license file; README declares CC0 for the corpus", "observed CI configuration; rights unclear, local only"),
    context("epidoc-schema-license", "epidoc", EPIDOC, EPIDOC_SHA, "schema/LICENSE.txt", "GPL-3.0-or-later", "license evidence"),
    context("epidoc-dev-schema-workflow", "epidoc", EPIDOC, EPIDOC_SHA, ".github/workflows/build-dev-schema.yml",
            "unclear: no repository-wide license file", "observed CI configuration; rights unclear, local only"),
    context("epidoc-ircyr-schematron", "epidoc", EPIDOC, EPIDOC_SHA, "schema/schematron/ircyr-checking.sch", "GPL-3.0-or-later",
            "comparison with the project copy"),
    context("isicily-licence", "epidoc", ISICILY, ISICILY_SHA, "licence.txt", "CC-BY-4.0", "license evidence"),
    context("isicily-ircyr-schematron", "epidoc", ISICILY, ISICILY_SHA, "schematron/ircyr-checking.sch", "CC-BY-4.0",
            "project Schematron named by the input document; comparison"),
    context("cmif-readme", "cmif", CMIF, CMIF_SHA, "README.md", "CC-BY-4.0 OR BSD-2-Clause", "license evidence"),
    context("cmif-license-cc-by", "cmif", CMIF, CMIF_SHA, "LICENSE CC-BY", "CC-BY-4.0 OR BSD-2-Clause", "license evidence"),
    context("cmif-schema-rng", "cmif", CMIF, CMIF_SHA, "schema/cmi-customization.rng", "CC-BY-4.0 OR BSD-2-Clause", "comparison"),
    context("cmif-schematron", "cmif", CMIF, CMIF_SHA, "odd/cmif.sch", "CC-BY-4.0 OR BSD-2-Clause", "comparison"),
    context("csapi-readme", "cmif", CSAPI, CSAPI_SHA, "README.md", "LGPL-3.0-or-later", "license evidence"),
    context("csapi-check-rng", "cmif", CSAPI, CSAPI_SHA, "api/v2.0/services/check/cmi-customization.rng", "LGPL-3.0-or-later",
            "schema copy used by the check service; comparison"),
    context("csapi-check-schematron", "cmif", CSAPI, CSAPI_SHA, "api/v2.0/services/check/cmif.sch", "LGPL-3.0-or-later",
            "Schematron copy used by the check service; comparison"),
]

COMPARISONS = [("cmif-schema-rng", "csapi-check-rng"), ("cmif-schematron", "csapi-check-schematron"),
               ("epidoc-ircyr-schematron", "isicily-ircyr-schematron")]

KNOWN_LIMITS = [
    "Purposive contrast sample of three community-published customizations reused by many projects; no single-project local ODD, no statistical representativeness and no family completeness.",
    "No catalogue case was examined; CMIF is a correspondence metadata interchange profile and is not treated as a catalogue.",
    "No ODD compilation, RELAX NG or Schematron validation was executed: TEI Stylesheets, Java, Jing, SchXslt and lxml are absent from the project environment. Validity of the three input documents is unknown.",
    "Observed pipeline configuration (build script, workflows, service code) is source text. This run executed only fetching, hashing, XML well-formedness parsing, a deterministic element inventory and byte comparisons.",
    "Schema locations named by the input documents were not fetched; the schema a processor applies to them at a given date is not established.",
    "Release assets, project websites, Docker images and the TEI Stylesheets submodule were not acquired.",
    "Workflow files of repositories without a repository-wide license are local context observations only.",
    "The EpiDoc ODD header states GPL-2.0-or-later while schema/LICENSE.txt states GPL-3.0-or-later; both are recorded without legal determination.",
    "Pinned states are development heads of 2026-09-11 except CMIF, whose head equals tag v1.1.0.",
    "Domain acceptance by drama, epigraphy and correspondence-edition experts has not taken place.",
]


def raw_url(repository: str, commit: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{repository}/{commit}/{quote(path)}"


def rep_path(source: dict) -> Path:
    return Path(f"10_markdown/documents/{source['slug']}.md")


def original_path(source: dict) -> Path:
    return Path(f"00_sources/documents/{source['slug']}{Path(source['path']).suffix or '.txt'}")


def immutable(path: Path, payload: bytes, check: bool = False) -> None:
    if path.exists():
        if path.read_bytes() != payload:
            raise ValueError(f"immutable artifact mismatch: {path}")
    elif check:
        raise ValueError(f"missing immutable artifact: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)


def guard(source: dict, payload: bytes) -> None:
    if b"\r" in payload:
        raise ValueError(f"{source['slug']}: carriage return would not survive LF normalization")
    if b"[[" in payload or BLOCK_LIKE.search(payload):
        raise ValueError(f"{source['slug']}: payload contains a Markdown anchor form")
    if source["language"] == "xml":
        if b"<!DOCTYPE" in payload or b"<!ENTITY" in payload:
            raise ValueError(f"{source['slug']}: DTD or entity declaration outside admission scope")
        try:
            ET.fromstring(payload)
        except ET.ParseError as exc:
            raise ValueError(f"{source['slug']}: XML is not well-formed: {exc}") from exc


def locate(payload: bytes, fragment: dict) -> dict:
    start_marker, end_marker = fragment["start"].encode("utf-8"), fragment["end"].encode("utf-8")
    positions, cursor = [], payload.find(start_marker)
    while cursor != -1:
        positions.append(cursor)
        cursor = payload.find(start_marker, cursor + 1)
    if len(positions) < fragment["occurrence"]:
        raise ValueError(f"start marker not found: {fragment['id']}")
    start = positions[fragment["occurrence"] - 1]
    end = payload.find(end_marker, start)
    if end == -1:
        raise ValueError(f"end marker not found: {fragment['id']}")
    end += len(end_marker)
    value = payload[start:end]
    wellformed = None
    if fragment["kind"] == "element":
        try:
            ET.fromstring(WRAP.encode("utf-8") + value + b"</fragment>")
        except ET.ParseError as exc:
            raise ValueError(f"reading block is not one well-formed element: {fragment['id']}: {exc}") from exc
        wellformed = True
    return {"id": fragment["id"], "label": fragment["label"], "kind": fragment["kind"],
            "occurrence": fragment["occurrence"], "occurrences": len(positions),
            "start_byte": start, "end_byte": end,
            "start_line": payload.count(b"\n", 0, start) + 1, "end_line": payload.count(b"\n", 0, end - 1) + 1,
            "sha256": digest(value), "wellformed_element": wellformed, "text": value.decode("utf-8")}


def fence_for(payload: bytes) -> str:
    longest = max((len(run) for run in re.findall(rb"`+", payload)), default=0)
    return "`" * max(3, longest + 1)


def marker(source: dict, payload: bytes) -> bytes:
    return f"## Complete original\n\n{fence_for(payload)}{source['language']}\n".encode()


def render(source: dict, payload: bytes) -> bytes:
    guard(source, payload)
    located = [locate(payload, fragment) for fragment in source["fragments"]]
    identifier = f"https://github.com/{source['repository']}/blob/{source['commit']}/{quote(source['path'])}"
    fm = {"type": "representation", "source-type": "document", "source": f"[[{original_path(source).as_posix()}]]",
          "converter": f"{ADAPTER} v1; complete original plus JSON-escaped exact source fragments",
          "channel": "collection",
          "metadata": {"title": source["title"], "creator": source["creator"], "date": source["date"],
                       "format": "application/xml" if source["language"] == "xml" else "text/plain",
                       "identifier": identifier, "license": source["license"], "confidential": False},
          "created": DATE, "updated": DATE}
    text = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n"
    text += f"# {source['title']}\n\n"
    text += (f"Source: `{source['path']}` in `{source['repository']}` at commit `{source['commit']}`.\n"
             f"Source SHA-256: `{digest(payload)}`, {len(payload)} bytes.\n"
             f"Rights: {source['license']}. {source['attribution']}\n"
             f"License evidence: {'; '.join(source['license_evidence'])}.\n\n"
             "The complete original is inert source text and is never executed. The\n"
             "separator newline before its closing fence is not part of the original.\n"
             "Reading blocks are exact source byte intervals encoded as JSON strings;\n"
             "their line and byte locators refer to the original.\n\n")
    fence = fence_for(payload)
    output = text.encode("utf-8") + marker(source, payload) + payload + f"\n{fence}\n\n".encode()
    output += b"## Selected source reading blocks\n\n"
    for item in located:
        block = (f"### {item['id']} {item['label']}\n\n"
                 f"Locator: lines {item['start_line']}-{item['end_line']}, bytes {item['start_byte']}-{item['end_byte']}, "
                 f"{item['kind']}, occurrence {item['occurrence']} of {item['occurrences']} of the start marker.\n\n"
                 f"Exact source fragment as a JSON string: {json.dumps(item['text'], ensure_ascii=False)} ^{item['id']}\n\n")
        output += block.encode("utf-8")
    return output


def embedded_source(root: Path, source: dict, byte_count: int) -> bytes:
    rendered = (root / rep_path(source)).read_bytes()
    head = b"## Complete original\n\n"
    if rendered.count(head) != 1:
        raise ValueError(f"{source['slug']}: source block boundary mismatch")
    fence_start = rendered.index(head) + len(head)
    fence_end = rendered.index(b"\n", fence_start) + 1
    payload = rendered[fence_end:fence_end + byte_count]
    if rendered[fence_start:fence_end] != marker(source, payload)[len(head):]:
        raise ValueError(f"{source['slug']}: source fence mismatch")
    if rendered != render(source, payload):
        raise ValueError(f"{source['slug']}: immutable representation differs from exact source conversion")
    original = root / original_path(source)
    if original.exists() and original.read_bytes() != payload:
        raise ValueError(f"{source['slug']}: immutable local original changed")
    return payload


def odd_inventory(payload: bytes) -> dict:
    root = ET.fromstring(payload)
    specs = list(root.iter(f"{TEI}schemaSpec"))
    if root.tag != f"{TEI}TEI" or len(specs) != 1:
        raise ValueError("an ODD must be a TEI document with exactly one schemaSpec")
    spec = specs[0]
    modes: Counter = Counter()
    for kind in ("elementSpec", "classSpec", "macroSpec", "dataSpec", "constraintSpec", "attDef", "valList"):
        for element in spec.iter(f"{TEI}{kind}"):
            modes[f"{kind} mode={element.get('mode', '(absent)')}"] += 1
    closures = Counter(f"valList type={element.get('type', '(absent)')}" for element in spec.iter(f"{TEI}valList"))
    schematron = Counter(element.tag.removeprefix(SCH) for element in spec.iter() if element.tag in {f"{SCH}rule", f"{SCH}assert", f"{SCH}report"})
    roles = Counter(element.get("role", "(absent)") for element in spec.iter() if element.tag in {f"{SCH}rule", f"{SCH}assert", f"{SCH}report"})
    return {"schemaSpec": {key: spec.get(key) for key in ("ident", "source", "start") if spec.get(key) is not None},
            "moduleRefs": [{key: element.get(key) for key in ("key", "include", "except", "url") if element.get(key) is not None}
                           for element in spec.iter(f"{TEI}moduleRef")],
            "spec_modes": dict(sorted(modes.items())), "valList_types": dict(sorted(closures.items())),
            "schematron_elements": dict(sorted(schematron.items())), "schematron_roles": dict(sorted(roles.items()))}


def input_inventory(payload: bytes) -> dict:
    root = ET.fromstring(payload)
    prolog = payload[:payload.index(b"<TEI")]
    names = Counter(element.tag.split("}")[-1] if element.tag.startswith(TEI) else element.tag for element in root.iter())
    return {"root": root.tag, "prolog_xml_model": [value.decode("utf-8") for value in XML_MODEL.findall(prolog)],
            "xinclude_elements": sum(1 for element in root.iter(f"{XI}include")),
            "element_counts": dict(sorted(names.items()))}


def admitted_record(source: dict, payload: bytes, request: dict) -> dict:
    located = [{key: value for key, value in locate(payload, fragment).items() if key != "text"} for fragment in source["fragments"]]
    record = {key: source[key] for key in ("slug", "case", "role", "repository", "commit", "path", "license",
                                           "license_evidence", "attribution")}
    record.update(url=raw_url(source["repository"], source["commit"], source["path"]), sha256=digest(payload),
                  byte_count=len(payload), raw_path=request["raw_path"], observed_at=request["observed_at"],
                  representation=rep_path(source).as_posix(), original=original_path(source).as_posix(),
                  fragments=located)
    if source["language"] == "xml":
        record["xml_wellformed"] = True
        record["odd_inventory" if source["role"] == "odd" else "input_inventory"] = (
            odd_inventory(payload) if source["role"] == "odd" else input_inventory(payload))
    return record


Fetch = Callable[[str], tuple[dict, bytes]]


def http_fetch(root: Path) -> Fetch:
    store = HttpStore(root / "corpus/raw", timeout=60, retries=3)

    def fetch(url: str) -> tuple[dict, bytes]:
        result, body = store.fetch(url)
        record = result.as_record()
        return {key: record[key] for key in ("requested_url", "final_url", "observed_at", "status", "media_type",
                                             "byte_count", "sha256", "raw_path")}, body
    return fetch


def declared_urls(sources: list[dict], contexts: list[dict]) -> list[str]:
    return [raw_url(item["repository"], item["commit"], item["path"]) for item in sources + contexts]


def acquire(root: Path, fetch: Fetch, sources: list[dict] = SOURCES, contexts: list[dict] = CONTEXTS) -> dict:
    if (root / MANIFEST).exists():
        raise ValueError("admission manifest exists; use --reproduce or --check")
    started = utc_now()
    responses: dict[str, tuple[dict, bytes]] = {}
    for url in declared_urls(sources, contexts):
        request, body = fetch(url)
        if request["status"] != 200 or request["sha256"] != digest(body) or request["byte_count"] != len(body):
            raise ValueError(f"unusable response for {url}: HTTP {request['status']}")
        responses[url] = (request, body)
    rendered = {source["slug"]: render(source, responses[raw_url(source["repository"], source["commit"], source["path"])][1])
                for source in sources}
    records, admissions = [], []
    for source in sources:
        request, payload = responses[raw_url(source["repository"], source["commit"], source["path"])]
        records.append(admitted_record(source, payload, request))
        admissions.append({"source_type": "document", "case": source["case"], "role": source["role"],
                           "original_path": original_path(source).as_posix(),
                           "representation_path": rep_path(source).as_posix(), "original_sha256": digest(payload),
                           "repository": source["repository"], "commit": source["commit"], "source_path": source["path"],
                           "license": source["license"]})
    observations = []
    for item in contexts:
        request, body = responses[raw_url(item["repository"], item["commit"], item["path"])]
        observations.append({**item, "url": request["requested_url"], "sha256": request["sha256"],
                             "byte_count": request["byte_count"], "raw_path": request["raw_path"], "admitted": False})
    by_id = {item["id"]: item for item in observations}
    comparisons = [{"left": left, "right": right, "left_bytes": by_id[left]["byte_count"],
                    "right_bytes": by_id[right]["byte_count"], "byte_identical": by_id[left]["sha256"] == by_id[right]["sha256"]}
                   for left, right in COMPARISONS if left in by_id and right in by_id]
    for source in sources:
        payload = responses[raw_url(source["repository"], source["commit"], source["path"])][1]
        immutable(root / original_path(source), payload)
        immutable(root / rep_path(source), rendered[source["slug"]])
    normalized = {"format_version": 1, "run_id": RUN_ID, "source_id": SOURCE_ID, "selection": SELECTION,
                  "scope": "Nine admitted files and seventeen context observations at pinned commits; not the families or corpora.",
                  "content_authority": "sampled-practice-record", "instruction_trust": "none",
                  "admitted": records, "context_observations": observations,
                  "self_executed": {"operations": ["HTTP GET of declared raw URLs into content-addressed raw storage",
                                                   "SHA-256 hashing", "Python ElementTree well-formedness parsing",
                                                   "deterministic ODD and input element inventory", "byte comparison of declared pairs"],
                                    "comparisons": comparisons},
                  "not_executed": ["ODD compilation", "RELAX NG validation", "Schematron validation",
                                   "any build script, workflow, XQuery or XSLT from the sources"]}
    immutable(root / NORMALIZED, (json.dumps(normalized, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    requests = [responses[url][0] for url in declared_urls(sources, contexts)]
    objects = [{"path": path.as_posix(), "sha256": digest((root / path).read_bytes())}
               for path in [rep_path(source) for source in sources] + [NORMALIZED]]
    manifest = {
        "schema_version": 1, "run_id": RUN_ID, "source_id": SOURCE_ID, "started_at": started, "finished_at": utc_now(),
        "status": "bounded-complete", "lock_file": "sources/locks/real-world-customizations.yaml",
        "scope": {"boundary": "Exactly the declared request list at pinned commits: nine admitted files for three cases and seventeen context observations; no family, corpus or project completeness",
                  "status_applies_to": "declared pinned request list of this purposive sample",
                  "selection": SELECTION},
        "adapter": {"name": ADAPTER, "version": 1},
        "requests": requests, "objects": objects,
        "counts": {"requests": len(requests), "admitted_sources": len(sources), "context_observations": len(contexts),
                   "reading_blocks": sum(len(source["fragments"]) for source in sources)},
        "rights": [{"representation_path": rep_path(source).as_posix(), "license": source["license"],
                    "license_evidence": source["license_evidence"], "attribution": source["attribution"]} for source in sources],
        "content_authority": "sampled-practice-record", "instruction_trust": "none",
        "gaps": [], "rights_exceptions": [f"{item['repository']}/{item['path']}: {item['rights']}; raw body local only"
                                          for item in contexts if item["rights"].startswith("unclear")],
        "known_limits": KNOWN_LIMITS, "admissions": admissions,
    }
    immutable(root / MANIFEST, yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True).encode("utf-8"))
    return manifest


def check(root: Path, sources: list[dict] = SOURCES) -> None:
    manifest = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
    expected = {rep_path(source).as_posix() for source in sources} | {NORMALIZED.as_posix()}
    paths = [item["path"] for item in manifest["objects"]]
    if len(paths) != len(expected) or set(paths) != expected:
        raise ValueError("admission object scope is incomplete or changed")
    for item in manifest["objects"]:
        if digest((root / item["path"]).read_bytes()) != item["sha256"]:
            raise ValueError(f"admission output checksum mismatch: {item['path']}")
    normalized = json.loads((root / NORMALIZED).read_text(encoding="utf-8"))
    records = {record["slug"]: record for record in normalized["admitted"]}
    admissions = {item["representation_path"]: item for item in manifest["admissions"]}
    if set(records) != {source["slug"] for source in sources} or set(admissions) != expected - {NORMALIZED.as_posix()}:
        raise ValueError("admission record scope is incomplete or changed")
    for source in sources:
        record = records[source["slug"]]
        payload = embedded_source(root, source, record["byte_count"])
        if digest(payload) != record["sha256"] or admissions[rep_path(source).as_posix()]["original_sha256"] != record["sha256"]:
            raise ValueError(f"{source['slug']}: source identity mismatch")
        located = [{key: value for key, value in locate(payload, fragment).items() if key != "text"} for fragment in source["fragments"]]
        if located != record["fragments"]:
            raise ValueError(f"{source['slug']}: reading block identity mismatch")


def reproduce(root: Path, fetch: Fetch) -> list[str]:
    manifest = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
    mismatches = []
    for request in manifest["requests"]:
        observed, body = fetch(request["requested_url"])
        if observed["status"] != 200 or digest(body) != request["sha256"] or len(body) != request["byte_count"]:
            mismatches.append(request["requested_url"])
    return mismatches


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--reproduce", action="store_true")
    args = parser.parse_args()
    try:
        if args.check:
            check(ROOT)
            print("OK: nine pinned practice sources, reading blocks and admission hashes reconcile")
        elif args.reproduce:
            mismatches = reproduce(ROOT, http_fetch(ROOT))
            if mismatches:
                print("FAILED: refetched bytes differ for " + ", ".join(mismatches), file=sys.stderr)
                raise SystemExit(1)
            print("OK: every recorded request refetched with identical SHA-256 and length")
        else:
            manifest = acquire(ROOT, http_fetch(ROOT))
            print(f"OK: {manifest['counts']['requests']} responses; {manifest['counts']['admitted_sources']} sources admitted "
                  f"with {manifest['counts']['reading_blocks']} reading blocks")
    except (OSError, ValueError, KeyError, RuntimeError, ET.ParseError) as exc:
        print(f"Practice sample admission failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
