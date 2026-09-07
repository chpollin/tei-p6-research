"""Check and reproduce the documentary ontology defined in knowledge/ontology.md.

Run `python tools/check_ontology.py`, then `--check`; `--root` selects fixtures.
The hand-authored Turtle is authoritative. Deterministic serializers support
this deliberately blank-node-free vocabulary. These checks establish a local
structural policy and RDF graph equality, without OWL reasoning or data validation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

ROOT = Path(__file__).resolve().parents[1]
LOCAL = Namespace("https://example.org/tei-p6-research/ontology/")
PREFIXES = {"owl": str(OWL), "rdf": str(RDF), "rdfs": str(RDFS), "xsd": str(XSD)}
DECLARATIONS = {
    OWL.Class,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
}
CORE_PREDICATES = {
    RDF.type,
    RDFS.label,
    RDFS.comment,
    RDFS.subClassOf,
    RDFS.domain,
    RDFS.range,
    OWL.versionIRI,
    OWL.versionInfo,
}
MAPPING_FIELDS = (
    LOCAL.localTerm,
    LOCAL.externalTerm,
    LOCAL.relation,
    LOCAL.sourceDocument,
    LOCAL.rationale,
    LOCAL.reviewState,
)


def _local(term: URIRef) -> bool:
    return isinstance(term, URIRef) and str(term).startswith(str(LOCAL))


def _defined(graph: Graph) -> set[URIRef]:
    return {
        subject
        for subject, kind in graph.subject_objects(RDF.type)
        if kind in DECLARATIONS
    }


def _literal_definition(graph: Graph, term: URIRef, predicate: URIRef) -> None:
    values = list(graph.objects(term, predicate))
    if not values or any(
        not isinstance(value, Literal) or not str(value).strip() for value in values
    ):
        raise ValueError(f"Missing or invalid {predicate} on {term}")


def validate_core(graph: Graph) -> None:
    """Reject axioms outside the narrow documentary declaration contract."""
    declared = _defined(graph)
    classes = set(graph.subjects(RDF.type, OWL.Class))
    if LOCAL.Record not in classes or LOCAL.Package not in classes:
        raise ValueError("Core must declare Record and Package classes")
    ontology = URIRef(LOCAL)
    if set(graph.subjects(RDF.type, OWL.Ontology)) != {ontology}:
        raise ValueError("Core must declare exactly the local ontology")
    versions = list(graph.objects(ontology, OWL.versionIRI))
    if len(versions) != 1 or not re.fullmatch(
        re.escape(str(LOCAL)) + r"\d{4}-\d{2}-\d{2}", str(versions[0])
    ):
        raise ValueError("Core requires one dated local version IRI")
    for subject, predicate, obj in graph:
        if any(isinstance(term, BNode) for term in (subject, predicate, obj)):
            raise ValueError("Blank nodes are outside the core policy")
        if predicate not in CORE_PREDICATES:
            raise ValueError(
                f"Prohibited core predicate or entailment construct: {predicate}"
            )
        if not _local(subject):
            raise ValueError(f"Foreign declaration: {subject}")
        for term in (subject, predicate, obj):
            if _local(term) and term not in declared | {ontology, *versions}:
                raise ValueError(f"Undefined local reference: {term}")
        if predicate == RDF.type and obj not in DECLARATIONS | {OWL.Ontology}:
            raise ValueError(f"Prohibited core class membership: {obj}")
        if predicate == RDFS.subClassOf and (
            subject not in classes or obj not in classes
        ):
            raise ValueError("Foreign or undeclared class in subclass edge")
        if predicate in {RDFS.domain, RDFS.range}:
            kinds = set(graph.objects(subject, RDF.type))
            if predicate == RDFS.range and OWL.DatatypeProperty in kinds:
                if obj not in {RDFS.Literal, XSD.string, XSD.nonNegativeInteger}:
                    raise ValueError(f"Unsupported literal range: {obj}")
            elif obj not in classes:
                raise ValueError(f"Foreign or undeclared class in domain/range: {obj}")
            if not kinds & {OWL.ObjectProperty, OWL.DatatypeProperty}:
                raise ValueError(f"Domain/range on a non-property: {subject}")
    for term in declared | {ontology}:
        _literal_definition(graph, term, RDFS.label)
        _literal_definition(graph, term, RDFS.comment)
        if len(set(graph.objects(term, RDF.type))) != 1:
            raise ValueError(f"Multiple declaration kinds: {term}")
        if (term, RDF.type, OWL.ObjectProperty) in graph and not list(
            graph.objects(term, RDFS.range)
        ):
            raise ValueError(f"Object property lacks documentary range: {term}")
        if (term, RDF.type, OWL.DatatypeProperty) in graph and not list(
            graph.objects(term, RDFS.range)
        ):
            raise ValueError(f"Datatype property lacks literal range: {term}")
    for term in classes:
        parents = list(graph.objects(term, RDFS.subClassOf))
        if term in {LOCAL.Record, LOCAL.Package}:
            if parents:
                raise ValueError("Record and Package must be separate hierarchy roots")
        elif len(parents) != 1:
            raise ValueError(f"Documentary class requires one parent: {term}")
        visited = set()
        cursor = term
        while parents := list(graph.objects(cursor, RDFS.subClassOf)):
            if cursor in visited:
                raise ValueError(f"Class hierarchy cycle at {cursor}")
            visited.add(cursor)
            cursor = parents[0]
        if term != LOCAL.Package and cursor != LOCAL.Record:
            raise ValueError(f"Class lies outside the Record hierarchy: {term}")


def validate_mappings(graph: Graph, core: Graph) -> None:
    """Require complete non-entailing annotations for every mapping candidate."""
    allowed = {RDF.type, RDFS.label, RDFS.comment, *MAPPING_FIELDS}
    candidates = set(graph.subjects(RDF.type, LOCAL.MappingCandidate))
    if not candidates:
        raise ValueError("Mapping register contains no candidates")
    if (LOCAL.MappingCandidate, RDF.type, OWL.Class) not in graph:
        raise ValueError("Mapping register must declare MappingCandidate")
    for field in MAPPING_FIELDS:
        if (field, RDF.type, OWL.AnnotationProperty) not in graph:
            raise ValueError(f"Mapping field must be an annotation property: {field}")
    declared = _defined(core) | _defined(graph) | candidates
    for subject, predicate, obj in graph:
        if any(isinstance(term, BNode) for term in (subject, predicate, obj)):
            raise ValueError("Blank nodes are outside the mapping policy")
        if predicate not in allowed:
            raise ValueError(f"Prohibited mapping entailment or predicate: {predicate}")
        if not _local(subject):
            raise ValueError(f"Foreign mapping subject: {subject}")
        if predicate == RDF.type:
            expected = (
                LOCAL.MappingCandidate
                if subject in candidates
                else (
                    OWL.Class
                    if subject == LOCAL.MappingCandidate
                    else OWL.AnnotationProperty
                )
            )
            if obj != expected or subject not in {
                LOCAL.MappingCandidate,
                *MAPPING_FIELDS,
                *candidates,
            }:
                raise ValueError(f"Unexpected mapping declaration: {subject} {obj}")
        for term in (subject, predicate, obj):
            if _local(term) and term not in declared:
                raise ValueError(f"Undefined local mapping reference: {term}")
        if predicate in MAPPING_FIELDS and subject not in candidates:
            raise ValueError(f"Mapping annotation outside a candidate: {subject}")
    for candidate in candidates:
        values = {}
        for field in MAPPING_FIELDS:
            objects = list(graph.objects(candidate, field))
            if len(objects) != 1:
                raise ValueError(
                    f"Mapping candidate requires exactly one {field}: {candidate}"
                )
            values[field] = objects[0]
        if values[LOCAL.localTerm] not in _defined(core):
            raise ValueError(
                f"Mapping localTerm is not a declared core term: {candidate}"
            )
        for field in (LOCAL.externalTerm, LOCAL.sourceDocument):
            value = values[field]
            if (
                not isinstance(value, URIRef)
                or not str(value).startswith(("https://", "http://"))
                or _local(value)
            ):
                raise ValueError(
                    f"Mapping {field} requires an external HTTP(S) IRI: {candidate}"
                )
        for field in (LOCAL.relation, LOCAL.rationale, LOCAL.reviewState):
            if not isinstance(values[field], Literal) or not str(values[field]).strip():
                raise ValueError(
                    f"Mapping {field} requires a nonempty literal: {candidate}"
                )
        if str(values[LOCAL.reviewState]) != "candidate":
            raise ValueError(f"Mapping reviewState must remain candidate: {candidate}")


def _triples(triples: Iterable[tuple]) -> list[tuple]:
    return sorted(triples, key=lambda triple: tuple(term.n3() for term in triple))


def serialize_xml(graph: Graph) -> bytes:
    """Use explicit stable ordering; all supported predicates have fixed prefixes."""
    namespaces = " ".join(
        f"xmlns:{prefix}={quoteattr(uri)}" for prefix, uri in sorted(PREFIXES.items())
    )
    lines = ['<?xml version="1.0" encoding="utf-8"?>', f"<rdf:RDF {namespaces}>"]
    for subject in sorted(set(graph.subjects()), key=str):
        lines.append(f"  <rdf:Description rdf:about={quoteattr(str(subject))}>")
        for _, predicate, obj in _triples(graph.triples((subject, None, None))):
            prefix, namespace = next(
                (p, n) for p, n in PREFIXES.items() if str(predicate).startswith(n)
            )
            tag = prefix + ":" + str(predicate)[len(namespace) :]
            if isinstance(obj, URIRef):
                lines.append(f"    <{tag} rdf:resource={quoteattr(str(obj))}/>")
            else:
                attribute = ""
                if obj.language:
                    attribute = f" xml:lang={quoteattr(obj.language)}"
                elif obj.datatype:
                    attribute = f" rdf:datatype={quoteattr(str(obj.datatype))}"
                value = escape(str(obj)).replace("\r", "&#13;")
                lines.append(f"    <{tag}{attribute}>{value}</{tag}>")
        lines.append("  </rdf:Description>")
    return ("\n".join([*lines, "</rdf:RDF>"]) + "\n").encode("utf-8")


def serialize_jsonld(graph: Graph) -> bytes:
    nodes = []
    for subject in sorted(set(graph.subjects()), key=str):
        node = {"@id": str(subject)}
        for _, predicate, obj in _triples(graph.triples((subject, None, None))):
            if isinstance(obj, URIRef):
                value = {"@id": str(obj)}
            else:
                value = {"@value": str(obj)}
                if obj.language:
                    value["@language"] = obj.language
                elif obj.datatype:
                    value["@type"] = str(obj.datatype)
            node.setdefault(str(predicate), []).append(value)
        nodes.append(node)
    return (
        json.dumps(
            {"@context": PREFIXES, "@graph": nodes},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def serialize_hierarchy(graph: Graph) -> bytes:
    lines = [
        "%% Generated from ontology/core.ttl by tools/check_ontology.py",
        "classDiagram",
    ]
    for subject in sorted(graph.subjects(RDF.type, OWL.Class), key=str):
        name = str(subject)[len(str(LOCAL)) :]
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", name):
            raise ValueError(f"Class name is not a safe Mermaid identifier: {name}")
        lines.append(f"    class {name}")
    for child, parent in sorted(
        graph.subject_objects(RDFS.subClassOf), key=lambda pair: tuple(map(str, pair))
    ):
        lines.append(
            f"    {str(parent)[len(str(LOCAL)) :]} <|-- {str(child)[len(str(LOCAL)) :]}"
        )
    return ("\n".join(lines) + "\n").encode("utf-8")


def build(root: Path = ROOT, *, check: bool = False) -> int:
    folder = root / "ontology"
    core = Graph().parse(data=(folder / "core.ttl").read_bytes(), format="turtle")
    mappings = Graph().parse(
        data=(folder / "alignment-candidates.ttl").read_bytes(), format="turtle"
    )
    validate_core(core)
    validate_mappings(mappings, core)
    outputs = {
        "core.rdf": serialize_xml(core),
        "core.jsonld": serialize_jsonld(core),
        "record-hierarchy.mmd": serialize_hierarchy(core),
    }
    for name, content in outputs.items():
        if check and (
            not (folder / name).exists() or (folder / name).read_bytes() != content
        ):
            raise ValueError(
                f"Stale generated artifact: ontology/{name}; run tools/check_ontology.py"
            )
    # Only generated, byte-matched payloads reach parsers that could resolve links.
    for name, format_name in (("core.rdf", "xml"), ("core.jsonld", "json-ld")):
        parsed = Graph().parse(data=outputs[name], format=format_name)
        if set(parsed) != set(core):
            raise ValueError(f"Serialized RDF graph differs from core: {name}")
    if not check:
        for name, content in outputs.items():
            destination = folder / name
            temporary = destination.with_suffix(destination.suffix + ".tmp")
            temporary.write_bytes(content)
            temporary.replace(destination)
    return len(core)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        count = build(args.root, check=args.check)
    except (OSError, SyntaxError, ValueError) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1
    print(
        f"OK: ontology policy and RDF graph equality ({count} triples); generated artifacts {'reproduced' if args.check else 'written'}. No OWL reasoning performed."
    )
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
