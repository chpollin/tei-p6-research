"""RDF export fidelity for the entity extension, over the independent 0.2 cases.

The preservation law is identity and structure: the record IRIs by kind and every
reference edge, taken from the triples alone, equal the same projection taken
directly from the package. The package projection below is written from the
record contract of sections 13 and 14 rather than imported from the binding, so
a shared mistake in one table cannot make the comparison pass.
"""

import copy
import hashlib
import json
import re
from pathlib import Path

import pytest

from tools.models.entities import validate_extension
from tools.models.rdf_binding import (
    CRM,
    OA,
    PROV,
    RDF,
    RDFS,
    SKOS,
    TEI6,
    XSD,
    describe,
    to_triples,
    to_turtle,
)

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "experiments/entities_v02"
TEST_BASE = "https://example.org/rdf-binding-test/"
CLAIM_KINDS = ("continuities", "readings", "annotations", "relations", "names",
               "denotations", "statements", "alignments", "former_bases")


def _cases() -> dict[str, dict]:
    """Every case package the 0.2 validator accepts, plus both standalone examples."""
    suite = json.loads((EXPERIMENT / "cases.json").read_text(encoding="utf-8"))
    packages = {case["id"]: case["package"] for case in suite["cases"] if case["expect"]["valid"]}
    for path in sorted((EXPERIMENT / "examples").glob("*.json")):
        packages[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return {name: package for name, package in packages.items()
            if validate_extension(package)["valid"]}


def _with_base(package: dict) -> dict:
    """A base is a publication fact, so a case without one receives the test base."""
    return package if "base" in package else {**copy.deepcopy(package), "base": TEST_BASE}


CASES = {name: _with_base(package) for name, package in _cases().items()}
EXAMPLES = sorted(path.stem for path in (EXPERIMENT / "examples").glob("*.json"))


def _package_projection(package: dict) -> dict:
    """Record IRIs by kind and every reference edge, read directly from the package."""
    base = package["base"]
    records: dict[str, list[str]] = {"package": ["<" + base + ">"]}
    edges: set[tuple[str, str, str]] = set()

    def ref(identifier: str) -> str:
        return "<" + base + identifier + ">"

    def add(kind: str, record: dict) -> str:
        records.setdefault(kind, []).append(ref(record["id"]))
        return ref(record["id"])

    def claim(node: str, record: dict) -> None:
        edges.add((node, "agent", ref(record["agent"])))
        for target in record.get("supersedes", []):
            edges.add((node, "supersedes", ref(target)))

    for kind in ("agents", "concepts", "entities"):
        for record in package[kind]:
            add(kind, record)
            for alignment in record.get("alignments", []):
                node = add("alignments", alignment)
                edges.add((node, "carrier", ref(record["id"])))
                claim(node, alignment)
    for record in package["texts"]:
        add("texts", record)
    for record in package["versions"]:
        node = add("versions", record)
        edges.update((node, "parents", ref(parent)) for parent in record["parents"])
    for record in package["continuities"]:
        node = add("continuities", record)
        edges.add((node, "text", ref(record["text"])))
        edges.update((node, "versions", ref(version)) for version in record["versions"])
        claim(node, record)
    for record in package["selections"]:
        edges.add((add("selections", record), "version", ref(record["version"])))
    for reading in package["readings"]:
        node = add("readings", reading)
        edges.add((node, "version", ref(reading["version"])))
        claim(node, reading)
        for item in reading["nodes"]:
            child = add("nodes", item)
            edges.add((child, "reading", ref(reading["id"])))
            edges.add((child, "type", ref(item["type"])))
            edges.add((child, "selection", ref(item["selection"])))
            if item["parent"] is not None:
                edges.add((child, "parent", ref(item["parent"])))
    for record in package["annotations"]:
        node = add("annotations", record)
        edges.add((node, "selection", ref(record["selection"])))
        if "concept" in record:
            edges.add((node, "concept", ref(record["concept"])))
        claim(node, record)
    for record in package["relations"]:
        node = add("relations", record)
        for field in ("source", "target", "type"):
            edges.add((node, field, ref(record[field])))
        claim(node, record)
    for record in package["names"]:
        node = add("names", record)
        edges.add((node, "entity", ref(record["entity"])))
        claim(node, record)
    for record in package["denotations"]:
        node = add("denotations", record)
        edges.add((node, "mention", ref(record["mention"])))
        edges.add((node, "entity", ref(record["entity"])))
        claim(node, record)
    for record in package["statements"]:
        node = add("statements", record)
        edges.add((node, "type", ref(record["type"])))
        edges.update((node, "participants", ref(entity)) for entity in
                     {item["entity"] for item in record["participants"]})
        claim(node, record)
    for record in package.get("former_bases", []):
        node = add("former_bases", record)
        edges.add((node, "package", "<" + base + ">"))
        claim(node, record)
    return {"records": {kind: sorted(iris) for kind, iris in sorted(records.items())},
            "edges": sorted(edges)}


def _turtle_defects(text: str) -> list[str]:
    """Minimal syntax check: balanced statements, absolute IRIs, escaped controls."""
    defects = []
    if any(ord(character) < 0x20 and character != "\n" for character in text):
        defects.append("unescaped control character")
    masked = re.sub(r'"(?:[^"\\\n]|\\.)*"', '""', text)
    if masked.count('"') % 2:
        defects.append("unterminated literal")
    for iri in re.findall(r"<([^<>]*)>", masked):
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9+.-]*:\S*", iri) is None:
            defects.append(f"IRI without a scheme: {iri}")
    blocks = masked.strip("\n").split("\n\n")
    for line in blocks[0].splitlines():
        if not line.startswith("@prefix ") or not line.endswith(" ."):
            defects.append(f"malformed prefix line: {line}")
    for block in blocks[1:]:
        lines = block.splitlines()
        if sum(line.endswith(" .") for line in lines) != 1 or not lines[-1].endswith(" ."):
            defects.append(f"unbalanced statement: {lines[0]}")
        if any(not line.endswith(" ;") for line in lines[:-1]):
            defects.append(f"missing predicate separator: {lines[0]}")
    return defects


def package(**collections) -> dict:
    """A minimal valid 0.2 package with a base, extended by the given collections."""
    result = {"model_version": "0.2", "base": TEST_BASE,
              "agents": [{"id": "ag", "label": "Editor"}],
              "concepts": [], "texts": [], "versions": [], "continuities": [],
              "selections": [], "readings": [], "annotations": [], "relations": [],
              "entities": [], "names": [], "denotations": [], "statements": []}
    return {**result, **collections}


def version(content: str, identifier: str = "v1") -> dict:
    return {"id": identifier, "content": content, "parents": [],
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest()}


def claim(identifier: str, **fields) -> dict:
    return {"id": identifier, "agent": "ag", "created": "2026-09-06T09:00:00Z",
            "status": "asserted", **fields}


@pytest.mark.parametrize("name", sorted(CASES))
def test_records_and_edges_survive_the_export_for_every_valid_case(name):
    source = CASES[name]
    before = copy.deepcopy(source)
    assert describe(to_triples(source)) == _package_projection(source)
    assert source == before


@pytest.mark.parametrize("name", sorted(CASES))
def test_the_export_is_deterministic_and_well_formed(name):
    source = CASES[name]
    assert to_turtle(source) == to_turtle(source)
    assert to_triples(source) == sorted(set(to_triples(source)))
    assert _turtle_defects(to_turtle(source)) == []


@pytest.mark.parametrize("name", EXAMPLES)
def test_the_committed_turtle_examples_reproduce(name):
    source = json.loads((EXPERIMENT / f"examples/{name}.json").read_text(encoding="utf-8"))
    committed = (EXPERIMENT / f"examples/{name}.ttl").read_text(encoding="utf-8")
    assert committed == to_turtle(source)


def test_a_package_without_a_base_cannot_be_exported():
    without = package()
    del without["base"]
    assert validate_extension(without)["valid"]
    for export in (to_triples, to_turtle):
        with pytest.raises(ValueError, match="base"):
            export(without)


@pytest.mark.parametrize("invalid", [
    None, [], "package", {"model_version": "0.2"},
    package(entities=[{"id": "e1", "label": "X", "kind": "unicorn"}]),
    package(names=[claim("nm", entity="missing", form="X", language="en")]),
])
def test_an_invalid_package_is_refused_before_any_triple(invalid):
    for export in (to_triples, to_turtle):
        with pytest.raises(ValueError):
            export(invalid)


@pytest.mark.parametrize("base", [
    "http://www.w3.org/ns/oa#", "urn:tei-p6-research:rdf:0.2:records/", "http://www.w3.org/",
])
def test_a_base_inside_a_reserved_namespace_is_refused(base):
    with pytest.raises(ValueError, match="reserved namespace"):
        to_triples({**package(), "base": base})


def test_name_forms_keep_their_language_tag_and_ordered_parts():
    source = package(
        entities=[{"id": "ent", "label": "Ada Lovelace", "kind": "person"}],
        names=[claim("nm-en", entity="ent", form="Ada Lovelace", language="en",
                     parts=[{"kind": "forename", "form": "Ada"},
                            {"kind": "surname", "form": "Lovelace"}]),
               claim("nm-la", entity="ent", form="Augusta Ada", language="la-x-old"),
               claim("nm-und", entity="ent", form="A. L.", language="und")])
    triples = to_triples(source)
    labels = {obj for _, predicate, obj in triples if predicate == f"<{RDFS}label>"}
    assert '"Ada Lovelace"@en' in labels
    assert '"Augusta Ada"@la-x-old' in labels
    assert '"A. L."@und' in labels
    parts = [(subject, obj) for subject, predicate, obj in triples
             if predicate == f"<{TEI6}namePartForm>"]
    assert parts == [(f"<{TEST_BASE}nm-en/part/1>", '"Ada"'),
                     (f"<{TEST_BASE}nm-en/part/2>", '"Lovelace"')]
    assert (f"<{TEST_BASE}ent>", f"<{CRM}P1_is_identified_by>", f"<{TEST_BASE}nm-en>") in triples


def test_several_alignments_of_one_entity_become_several_mapping_triples():
    relations = ("exact", "close", "broader", "narrower")
    source = package(entities=[{
        "id": "ent", "label": "Ada Lovelace", "kind": "person",
        "alignments": [claim(f"al-{relation}", iri=f"https://example.org/authority/{relation}",
                             relation=relation) for relation in relations]}])
    triples = to_triples(source)
    mapped = {(predicate, obj) for subject, predicate, obj in triples
              if subject == f"<{TEST_BASE}ent>" and predicate.startswith(f"<{SKOS}")}
    assert mapped == {
        (f"<{SKOS}exactMatch>", "<https://example.org/authority/exact>"),
        (f"<{SKOS}closeMatch>", "<https://example.org/authority/close>"),
        (f"<{SKOS}broadMatch>", "<https://example.org/authority/broader>"),
        (f"<{SKOS}narrowMatch>", "<https://example.org/authority/narrower>"),
    }
    # Each mapping triple keeps a claim node that carries what it drops.
    claims = describe(triples)["records"]["alignments"]
    assert claims == sorted(f"<{TEST_BASE}al-{relation}>" for relation in relations)
    assert all((node, f"<{TEI6}subject>", f"<{TEST_BASE}ent>") in triples for node in claims)


def test_a_superseded_claim_becomes_a_revision():
    source = package(
        entities=[{"id": "ent", "label": "Ada Lovelace", "kind": "person"},
                  {"id": "ent-other", "label": "A learned society", "kind": "group"}],
        names=[claim("nm-first", entity="ent", form="Ada Byron", language="en"),
               claim("nm-second", entity="ent", form="Ada Lovelace", language="en",
                     supersedes=["nm-first"]),
               claim("nm-third", entity="ent", form="Ada Lovelace", language="en",
                     status="withdrawn", supersedes=["nm-second"])])
    triples = to_triples(source)
    revisions = {(subject, obj) for subject, predicate, obj in triples
                 if predicate == f"<{PROV}wasRevisionOf>"}
    assert revisions == {(f"<{TEST_BASE}nm-second>", f"<{TEST_BASE}nm-first>"),
                         (f"<{TEST_BASE}nm-third>", f"<{TEST_BASE}nm-second>")}
    assert (f"<{TEST_BASE}nm-third>", f"<{TEI6}status>", '"withdrawn"') in triples
    assert describe(triples)["edges"] == _package_projection(source)["edges"]


def test_selectors_relations_and_unresolved_candidates_reach_the_export():
    content = "aaa bb aaa"
    source = package(
        concepts=[{"id": "cp-node", "label": "Word", "definition": "A word.",
                   "applies_to": "node"},
                  {"id": "cp-rel", "label": "Echo", "definition": "A repetition.",
                   "applies_to": "relation"}],
        versions=[version(content)],
        selections=[
            {"id": "sel-point", "version": "v1", "selector": {"kind": "point", "offset": 3}},
            {"id": "sel-parts", "version": "v1", "selector": {"kind": "ranges", "segments": [
                {"start": 0, "end": 3, "quote": "aaa"}, {"start": 7, "end": 10, "quote": "aaa"}]}},
            {"id": "sel-all", "version": "v1", "selector": {
                "kind": "quote", "exact": "aaa", "match": "all"}},
            {"id": "sel-one", "version": "v1", "selector": {
                "kind": "quote", "exact": "aaa", "prefix": "", "suffix": "", "match": "one"}},
        ],
        annotations=[{"id": "an-1", "agent": "ag", "selection": "sel-point", "body": "A point."},
                     {"id": "an-2", "agent": "ag", "selection": "sel-all", "body": "Both."}],
        relations=[claim("rel-1", type="cp-rel", source="an-1", target="an-2")])
    triples = to_triples(source)
    assert describe(triples) == _package_projection(source)
    assert (f"<{TEST_BASE}sel-parts/selector>", f"<{OA}items>",
            f"<{TEST_BASE}sel-parts/selector/1>") in triples
    assert (f"<{TEST_BASE}sel-parts/selector>", f"<{RDF}type>", f"<{OA}List>") in triples
    assert (f"<{TEST_BASE}sel-one>", f"<{TEI6}unresolvedCandidates>",
            f'"2"^^<{XSD}nonNegativeInteger>') in triples
    assert (f"<{TEST_BASE}sel-one>", f"<{TEI6}resolutionStatus>", '"ambiguous"') in triples
    assert (f"<{TEST_BASE}rel-1>", f"<{CRM}P140_assigned_attribute_to>",
            f"<{TEST_BASE}an-1>") in triples
    assert _turtle_defects(to_turtle(source)) == []


def test_former_bases_alias_every_record_and_stay_claims():
    source = package(
        entities=[{"id": "ent", "label": "Ada Lovelace", "kind": "person"}],
        former_bases=[claim("fb-1", base="https://old.example.org/p/")])
    triples = to_triples(source)
    aliases = {(subject, obj) for subject, predicate, obj in triples
               if predicate == f"<{PROV}alternateOf>"}
    assert aliases == {("<https://old.example.org/p/ag>", f"<{TEST_BASE}ag>"),
                       ("<https://old.example.org/p/ent>", f"<{TEST_BASE}ent>"),
                       ("<https://old.example.org/p/fb-1>", f"<{TEST_BASE}fb-1>")}
    assert (f"<{TEST_BASE}fb-1>", f"<{TEI6}subject>", f"<{TEST_BASE}>") in triples
    assert describe(triples)["records"]["package"] == [f"<{TEST_BASE}>"]


@pytest.mark.parametrize("hostile", [
    'A "quoted" body \\ with a backslash', "line\nbreak\ttab", "\x00\x01\x1f control",
    "combining é and 😀 and \U0010ffff", "trailing space ", " ",
])
def test_hostile_strings_stay_escaped_and_well_formed(hostile):
    source = package(
        versions=[version(hostile)],
        selections=[{"id": "sel", "version": "v1", "selector": {"kind": "ranges", "segments": [
            {"start": 0, "end": len(hostile), "quote": hostile}]}}],
        annotations=[{"id": "an", "agent": "ag", "selection": "sel", "body": hostile}])
    source["agents"][0]["label"] = hostile
    text = to_turtle(source)
    assert _turtle_defects(text) == []
    assert describe(to_triples(source)) == _package_projection(source)
