"""One-way RDF export of a validated entity-extension 0.2 package.

Section 14.5 of knowledge/text-model.md states the direction of the mapping and
section 13 the identifier policy and the claim pattern; the contract this module
implements is knowledge/text-model-rdf-binding.md. Unlike the JSON, XML and YAML
bindings there is no decoder: the export carries record identity, the claim
structure and every reference edge, and it drops version content and selection
resolution, so no round trip is claimed.

Every record IRI is the package base followed by the record's local ID, without
escaping, as section 13 requires, so a package without `base` cannot be
exported. Every claim stays a first-class node that carries its agent, instant,
status, certainty, validity and supersession; the plain vocabulary triple beside
it, such as `skos:exactMatch`, is the interoperability surface and loses those
fields. The module asserts no inference, and the entailments a consumer draws
from the external vocabularies are the consumer's.
"""

from __future__ import annotations

import itertools
import re
from typing import Any

from tools.models.abstract_text import COLLECTIONS as BASE_COLLECTIONS
from tools.models.entities import (
    NEW_COLLECTIONS,
    V01_CLAIM_COLLECTIONS,
    validate_extension,
)

CRM = "http://www.cidoc-crm.org/cidoc-crm/"
DCTERMS = "http://purl.org/dc/terms/"
OA = "http://www.w3.org/ns/oa#"
PROV = "http://www.w3.org/ns/prov#"
RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
SKOS = "http://www.w3.org/2004/02/skos/core#"
TEI6 = "urn:tei-p6-research:rdf:0.2:"
XSD = "http://www.w3.org/2001/XMLSchema#"
PREFIXES = (
    ("crm", CRM), ("dcterms", DCTERMS), ("oa", OA), ("prov", PROV), ("rdf", RDF),
    ("rdfs", RDFS), ("skos", SKOS), ("tei6", TEI6), ("xsd", XSD),
)
BINDING_VERSION = "0.2"
PACKAGE_KIND = "package"
NODE_KIND = "nodes"
CLAIM_KINDS = (*V01_CLAIM_COLLECTIONS, "names", "denotations", "statements",
               "alignments", "former_bases")
ENTITY_CLASSES = {
    "person": CRM + "E21_Person",
    "group": CRM + "E74_Group",
    "place": CRM + "E53_Place",
    "event": CRM + "E5_Event",
    "object": CRM + "E22_Human-Made_Object",
    "other": CRM + "E1_CRM_Entity",
}
ALIGNMENT_PREDICATES = {
    "exact": SKOS + "exactMatch",
    "close": SKOS + "closeMatch",
    "broader": SKOS + "broadMatch",
    "narrower": SKOS + "narrowMatch",
}
# The one predicate that carries each reference field of each record kind. The
# export writes an edge only through this predicate, so describe() inverts the
# table; a vocabulary triple that repeats an edge, such as P1 from an entity to
# its name claim, is not listed and is read back as decoration.
EDGE_PREDICATES: dict[tuple[str, str], str] = {
    ("versions", "parents"): TEI6 + "versionParent",
    ("continuities", "text"): TEI6 + "subject",
    ("continuities", "versions"): TEI6 + "continuityVersion",
    ("selections", "version"): OA + "hasSource",
    ("readings", "version"): OA + "hasTarget",
    (NODE_KIND, "reading"): TEI6 + "inReading",
    (NODE_KIND, "type"): OA + "hasBody",
    (NODE_KIND, "selection"): OA + "hasTarget",
    (NODE_KIND, "parent"): TEI6 + "nodeParent",
    ("annotations", "selection"): OA + "hasTarget",
    ("annotations", "concept"): OA + "hasBody",
    ("relations", "source"): CRM + "P140_assigned_attribute_to",
    ("relations", "target"): CRM + "P141_assigned",
    ("relations", "type"): CRM + "P177_assigned_property_of_type",
    ("names", "entity"): TEI6 + "subject",
    ("denotations", "mention"): OA + "hasTarget",
    ("denotations", "entity"): OA + "hasBody",
    ("statements", "participants"): CRM + "P140_assigned_attribute_to",
    ("statements", "type"): CRM + "P177_assigned_property_of_type",
    ("alignments", "carrier"): TEI6 + "subject",
    ("former_bases", "package"): TEI6 + "subject",
    **{(kind, "agent"): DCTERMS + "creator" for kind in CLAIM_KINDS},
    **{(kind, "supersedes"): PROV + "wasRevisionOf" for kind in CLAIM_KINDS},
}

_ABSOLUTE = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*:")
_IRI_FORBIDDEN = re.compile(r"[\x00-\x20<>\"{}|\\^`\x7f]")
_PN_LOCAL = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*")
_ESCAPES = {"\\": "\\\\", '"': '\\"', "\n": "\\n", "\r": "\\r", "\t": "\\t"}


def _fail(message: str) -> None:
    raise ValueError(message)


def _escape(value: str) -> str:
    """N-Triples literal escaping; other characters stay literal UTF-8."""
    parts = []
    for character in value:
        if character in _ESCAPES:
            parts.append(_ESCAPES[character])
        elif ord(character) < 0x20 or ord(character) == 0x7F:
            parts.append(f"\\u{ord(character):04X}")
        else:
            parts.append(character)
    return "".join(parts)


def _iri_term(iri: str) -> str:
    """An absolute IRI in N-Triples form; a character needing escaping is refused.

    Section 13 admits no escaping in either direction, so a base, an ID or an
    alignment IRI that would need it is a defect of the package, not of the term.
    """
    if type(iri) is not str or _ABSOLUTE.match(iri) is None or _IRI_FORBIDDEN.search(iri):
        _fail(f"Not an absolute IRI writable without escaping: {iri!r}")
    return "<" + iri + ">"


def _string(value: str) -> str:
    return '"' + _escape(value) + '"'


def _typed(value: str, datatype: str) -> str:
    return _string(value) + "^^" + _iri_term(datatype)


def _tagged(value: str, language: str) -> str:
    return _string(value) + "@" + language


def _integer(value: int) -> str:
    return _typed(str(value), XSD + "nonNegativeInteger")


def _derived(iri: str, *steps: str) -> str:
    """A non-record IRI below a record IRI; local IDs contain no slash, so it collides with none."""
    return "/".join((iri, *steps))


def _local_ids(package: dict) -> list[str]:
    """Every record ID of the package, reading nodes and nested alignment claims included."""
    identifiers = []
    for kind in (*BASE_COLLECTIONS, *NEW_COLLECTIONS, "former_bases"):
        for record in package.get(kind, []):
            identifiers.append(record["id"])
            identifiers.extend(item["id"] for item in record.get("alignments", []))
            if kind == "readings":
                identifiers.extend(node["id"] for node in record["nodes"])
    return sorted(identifiers)


class _Export:
    """Emit the triples of one valid package; every method reads, none mutates."""

    def __init__(self, package: dict, resolutions: dict) -> None:
        self.package = package
        self.resolutions = resolutions
        self.base = package["base"]
        self.identifiers = _local_ids(package)
        self.triples: list[tuple[str, str, str]] = []

    def record_iri(self, identifier: str) -> str:
        return self.base + identifier

    def add(self, subject: str, predicate: str, obj: str) -> None:
        """Subject and predicate are bare IRIs, the object an N-Triples term."""
        self.triples.append((_iri_term(subject), _iri_term(predicate), obj))

    def record(self, identifier: str, kind: str, classes: tuple[str, ...] = ()) -> str:
        iri = self.record_iri(identifier)
        for class_iri in classes:
            self.add(iri, RDF + "type", _iri_term(class_iri))
        self.add(iri, TEI6 + "recordKind", _string(kind))
        return iri

    def edge(self, source: str, kind: str, field: str, target: str) -> None:
        self.add(source, EDGE_PREDICATES[(kind, field)], _iri_term(self.record_iri(target)))

    def claim_fields(self, node: str, kind: str, record: dict) -> None:
        """The section 13 pattern fields, written once for every claim kind."""
        self.edge(node, kind, "agent", record["agent"])
        if "created" in record:
            self.add(node, PROV + "generatedAtTime", _typed(record["created"], XSD + "dateTime"))
        if "status" in record:
            self.add(node, TEI6 + "status", _string(record["status"]))
        if "certainty" in record:
            self.add(node, TEI6 + "certainty", _string(record["certainty"]))
        for key, predicate in (("from", TEI6 + "validFrom"), ("until", TEI6 + "validUntil")):
            if key in record.get("valid", {}):
                self.add(node, predicate, _string(record["valid"][key]))
        for target in record.get("supersedes", []):
            self.edge(node, kind, "supersedes", target)

    def alignments(self, carrier: dict) -> None:
        for record in carrier.get("alignments", []):
            node = self.record(record["id"], "alignments", (TEI6 + "AlignmentClaim",))
            self.edge(node, "alignments", "carrier", carrier["id"])
            self.add(node, TEI6 + "alignmentRelation", _string(record["relation"]))
            self.add(node, TEI6 + "alignmentTarget", _iri_term(record["iri"]))
            self.add(self.record_iri(carrier["id"]),
                     ALIGNMENT_PREDICATES[record["relation"]], _iri_term(record["iri"]))
            self.claim_fields(node, "alignments", record)

    def package_node(self) -> None:
        self.add(self.base, RDF + "type", _iri_term(TEI6 + "Package"))
        self.add(self.base, TEI6 + "recordKind", _string(PACKAGE_KIND))
        self.add(self.base, TEI6 + "modelVersion", _string(self.package["model_version"]))
        self.add(self.base, TEI6 + "bindingVersion", _string(BINDING_VERSION))

    def agents(self) -> None:
        for record in self.package["agents"]:
            node = self.record(record["id"], "agents", (PROV + "Agent",))
            self.add(node, RDFS + "label", _string(record["label"]))
            self.alignments(record)

    def concepts(self) -> None:
        for record in self.package["concepts"]:
            node = self.record(record["id"], "concepts", (SKOS + "Concept",))
            self.add(node, SKOS + "prefLabel", _string(record["label"]))
            self.add(node, SKOS + "definition", _string(record["definition"]))
            self.add(node, TEI6 + "conceptRole", _string(record["applies_to"]))
            self.alignments(record)

    def texts(self) -> None:
        for record in self.package["texts"]:
            node = self.record(record["id"], "texts", (TEI6 + "Text",))
            self.add(node, RDFS + "label", _string(record["label"]))

    def versions(self) -> None:
        for record in self.package["versions"]:
            node = self.record(record["id"], "versions", (TEI6 + "Version",))
            self.add(node, TEI6 + "contentHash", _string(record["sha256"]))
            for parent in record["parents"]:
                self.edge(node, "versions", "parents", parent)

    def continuities(self) -> None:
        for record in self.package["continuities"]:
            node = self.record(record["id"], "continuities", (TEI6 + "ContinuityClaim",))
            self.edge(node, "continuities", "text", record["text"])
            for version in record["versions"]:
                self.edge(node, "continuities", "versions", version)
            self.add(node, TEI6 + "criterion", _string(record["criterion"]))
            self.claim_fields(node, "continuities", record)

    def position(self, node: str, segment: dict) -> None:
        self.add(node, RDF + "type", _iri_term(OA + "TextPositionSelector"))
        self.add(node, OA + "start", _integer(segment["start"]))
        self.add(node, OA + "end", _integer(segment["end"]))
        if "quote" in segment:
            self.add(node, TEI6 + "segmentQuote", _string(segment["quote"]))

    def selector(self, node: str, selector: dict) -> None:
        target = _derived(node, "selector")
        self.add(node, OA + "hasSelector", _iri_term(target))
        if selector["kind"] == "point":
            # A point is the position selector whose start and end coincide.
            self.position(target, {"start": selector["offset"], "end": selector["offset"]})
        elif selector["kind"] == "ranges" and len(selector["segments"]) == 1:
            self.position(target, selector["segments"][0])
        elif selector["kind"] == "ranges":
            # One aggregate target whose ordered parts must survive without a collection.
            self.add(target, RDF + "type", _iri_term(OA + "List"))
            for index, segment in enumerate(selector["segments"], start=1):
                part = _derived(target, str(index))
                self.add(target, OA + "items", _iri_term(part))
                self.position(part, segment)
                self.add(part, TEI6 + "segmentIndex", _integer(index))
        else:
            self.add(target, RDF + "type", _iri_term(OA + "TextQuoteSelector"))
            self.add(target, OA + "exact", _string(selector["exact"]))
            for key in ("prefix", "suffix"):
                if key in selector:
                    self.add(target, OA + key, _string(selector[key]))
            self.add(target, TEI6 + "matchPolicy", _string(selector["match"]))

    def selections(self) -> None:
        for record in self.package["selections"]:
            node = self.record(record["id"], "selections", (OA + "SpecificResource",))
            self.edge(node, "selections", "version", record["version"])
            self.selector(node, record["selector"])
            resolution = self.resolutions.get(record["id"])
            if resolution is None:
                continue
            self.add(node, TEI6 + "resolutionStatus", _string(resolution["status"]))
            if resolution["candidates"]:
                self.add(node, TEI6 + "unresolvedCandidates",
                         _integer(len(resolution["candidates"])))

    def readings(self) -> None:
        for reading in self.package["readings"]:
            node = self.record(reading["id"], "readings", (OA + "Annotation",))
            self.add(node, OA + "motivatedBy", _iri_term(OA + "classifying"))
            self.edge(node, "readings", "version", reading["version"])
            self.add(node, RDFS + "label", _string(reading["label"]))
            self.claim_fields(node, "readings", reading)
            for item in reading["nodes"]:
                child = self.record(item["id"], NODE_KIND, (OA + "Annotation",))
                self.add(child, OA + "motivatedBy", _iri_term(OA + "classifying"))
                self.edge(child, NODE_KIND, "reading", reading["id"])
                self.edge(child, NODE_KIND, "type", item["type"])
                self.edge(child, NODE_KIND, "selection", item["selection"])
                if item["parent"] is not None:
                    self.edge(child, NODE_KIND, "parent", item["parent"])

    def annotations(self) -> None:
        for record in self.package["annotations"]:
            node = self.record(record["id"], "annotations", (OA + "Annotation",))
            self.edge(node, "annotations", "selection", record["selection"])
            body = _derived(node, "body")
            self.add(node, OA + "hasBody", _iri_term(body))
            self.add(body, RDF + "type", _iri_term(OA + "TextualBody"))
            self.add(body, RDF + "value", _string(record["body"]))
            if "concept" in record:
                self.edge(node, "annotations", "concept", record["concept"])
                self.add(node, OA + "motivatedBy", _iri_term(OA + "classifying"))
            self.claim_fields(node, "annotations", record)

    def relations(self) -> None:
        for record in self.package["relations"]:
            node = self.record(record["id"], "relations", (CRM + "E13_Attribute_Assignment",))
            self.edge(node, "relations", "source", record["source"])
            self.edge(node, "relations", "target", record["target"])
            self.edge(node, "relations", "type", record["type"])
            self.claim_fields(node, "relations", record)

    def entities(self) -> None:
        for record in self.package["entities"]:
            node = self.record(record["id"], "entities", (ENTITY_CLASSES[record["kind"]],))
            self.add(node, RDFS + "label", _string(record["label"]))
            self.add(node, TEI6 + "entityKind", _string(record["kind"]))
            self.alignments(record)

    def names(self) -> None:
        for record in self.package["names"]:
            node = self.record(record["id"], "names", (CRM + "E41_Appellation",))
            self.edge(node, "names", "entity", record["entity"])
            self.add(self.record_iri(record["entity"]),
                     CRM + "P1_is_identified_by", _iri_term(node))
            self.add(node, RDFS + "label", _tagged(record["form"], record["language"]))
            for index, part in enumerate(record.get("parts", []), start=1):
                item = _derived(node, "part", str(index))
                self.add(node, TEI6 + "hasNamePart", _iri_term(item))
                self.add(item, TEI6 + "namePartKind", _string(part["kind"]))
                self.add(item, TEI6 + "namePartForm", _string(part["form"]))
                self.add(item, TEI6 + "namePartIndex", _integer(index))
            self.claim_fields(node, "names", record)

    def denotations(self) -> None:
        for record in self.package["denotations"]:
            node = self.record(record["id"], "denotations", (OA + "Annotation",))
            self.add(node, OA + "motivatedBy", _iri_term(OA + "identifying"))
            self.edge(node, "denotations", "mention", record["mention"])
            self.edge(node, "denotations", "entity", record["entity"])
            self.claim_fields(node, "denotations", record)

    def statements(self) -> None:
        for record in self.package["statements"]:
            node = self.record(record["id"], "statements", (CRM + "E13_Attribute_Assignment",))
            self.add(node, TEI6 + "statementKind", _string(record["kind"]))
            self.edge(node, "statements", "type", record["type"])
            # Participants compare as a set under R11, so the part IRIs follow that order.
            ordered = sorted(record["participants"], key=lambda item: (item["entity"], item["role"]))
            for index, participant in enumerate(ordered, start=1):
                part = _derived(node, "participant", str(index))
                self.add(node, TEI6 + "hasParticipant", _iri_term(part))
                self.add(part, TEI6 + "participantEntity",
                         _iri_term(self.record_iri(participant["entity"])))
                self.add(part, TEI6 + "participantRole", _string(participant["role"]))
            for entity in sorted({item["entity"] for item in ordered}):
                self.edge(node, "statements", "participants", entity)
            if "value" in record:
                self.add(node, CRM + "P141_assigned", _string(record["value"]))
            self.claim_fields(node, "statements", record)

    def former_bases(self) -> None:
        for record in self.package.get("former_bases", []):
            node = self.record(record["id"], "former_bases", (TEI6 + "FormerBaseClaim",))
            self.add(node, EDGE_PREDICATES[("former_bases", "package")], _iri_term(self.base))
            self.add(node, TEI6 + "formerBase", _iri_term(record["base"]))
            self.claim_fields(node, "former_bases", record)
            for identifier in self.identifiers:
                self.add(record["base"] + identifier, PROV + "alternateOf",
                         _iri_term(self.record_iri(identifier)))

    def run(self) -> list[tuple[str, str, str]]:
        self.package_node()
        self.agents()
        self.concepts()
        self.texts()
        self.versions()
        self.continuities()
        self.selections()
        self.readings()
        self.annotations()
        self.relations()
        self.entities()
        self.names()
        self.denotations()
        self.statements()
        self.former_bases()
        return self.triples


def to_triples(package: Any) -> list[tuple[str, str, str]]:
    """Export a valid 0.2 package as sorted unique N-Triples terms.

    An invalid package and a package without `base` raise ValueError, because
    without the base no record IRI exists under the identifier policy.
    """
    result = validate_extension(package)
    if not result["valid"]:
        _fail(f"RDF export needs a valid 0.2 package: {result['diagnostics']}")
    if "base" not in package:
        _fail("RDF export needs the package field base; every record IRI is base plus local ID")
    for _, namespace in PREFIXES:
        if package["base"].startswith(namespace) or namespace.startswith(package["base"]):
            _fail(f"The package base collides with the reserved namespace {namespace}")
    return sorted(set(_Export(package, result["resolutions"]).run()))


def _compact(term: str) -> str:
    """Abbreviate a reserved-namespace IRI where the local part is a legal Turtle name."""
    if term.startswith('"') and term.endswith(">") and "^^<" in term:
        # A datatype IRI contains no "^", so the last "^^" separates it from the literal.
        literal, _, datatype = term.rpartition("^^")
        return literal + "^^" + _compact(datatype)
    if not term.startswith("<"):
        return term
    iri = term[1:-1]
    for prefix, namespace in PREFIXES:
        if not iri.startswith(namespace):
            continue
        local = iri[len(namespace):]
        if _PN_LOCAL.fullmatch(local) and not local.endswith("."):
            return prefix + ":" + local
    return term


def to_turtle(package: Any) -> str:
    """Export a valid 0.2 package as deterministic Turtle with the fixed prefix block."""
    triples = to_triples(package)
    lines = [f"@prefix {prefix}: <{namespace}> ." for prefix, namespace in PREFIXES]
    for subject, group in itertools.groupby(triples, key=lambda triple: triple[0]):
        ordered = sorted(((predicate, obj) for _, predicate, obj in group),
                         key=lambda pair: (pair[0] != _iri_term(RDF + "type"), pair))
        rendered = [("a" if predicate == _iri_term(RDF + "type") else _compact(predicate),
                     _compact(obj)) for predicate, obj in ordered]
        body = " ;\n    ".join(f"{predicate} {obj}" for predicate, obj in rendered)
        lines.append("")
        lines.append(f"{_compact(subject)} {body} .")
    return "\n".join(lines) + "\n"


def describe(triples: Any) -> dict:
    """Reconstruct record IRIs by kind and every reference edge from the triples alone.

    This is the projection the preservation law of the contract document compares
    with the same projection taken directly from the package. It reads only the
    record-kind markers and the designated edge predicates, so a vocabulary triple
    that repeats an edge and every derived node stay out of it.
    """
    kinds: dict[str, str] = {}
    for subject, predicate, obj in triples:
        if predicate == _iri_term(TEI6 + "recordKind"):
            if not obj.startswith('"') or not obj.endswith('"'):
                _fail(f"Malformed record-kind literal: {obj!r}")
            kinds[subject] = obj[1:-1]
    inverse = {(kind, _iri_term(predicate)): field
               for (kind, field), predicate in EDGE_PREDICATES.items()}
    records: dict[str, list[str]] = {}
    for iri, kind in kinds.items():
        records.setdefault(kind, []).append(iri)
    edges = {(subject, inverse[(kinds[subject], predicate)], obj)
             for subject, predicate, obj in triples
             if subject in kinds and obj in kinds
             and (kinds[subject], predicate) in inverse}
    return {"records": {kind: sorted(iris) for kind, iris in sorted(records.items())},
            "edges": sorted(edges)}
