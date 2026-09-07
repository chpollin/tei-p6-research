"""Exercise ontology policy against the real core with adverse local mutations.

The fixture's one synthetic mapping is a structural specimen without evidential
weight; the repository integration test separately checks the maintained register.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

from tools.check_ontology import (
    LOCAL,
    ROOT,
    build,
    main,
    serialize_jsonld,
    serialize_xml,
    validate_core,
    validate_mappings,
)


@pytest.fixture
def fixture_root(tmp_path: Path) -> Path:
    folder = tmp_path / "ontology"
    folder.mkdir()
    shutil.copyfile(ROOT / "ontology/core.ttl", folder / "core.ttl")
    (folder / "alignment-candidates.ttl").write_text(
        """@prefix : <https://example.org/tei-p6-research/ontology/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
:MappingCandidate a owl:Class .
:localTerm a owl:AnnotationProperty .
:externalTerm a owl:AnnotationProperty .
:relation a owl:AnnotationProperty .
:sourceDocument a owl:AnnotationProperty .
:rationale a owl:AnnotationProperty .
:reviewState a owl:AnnotationProperty .
:testMapping a :MappingCandidate ;
    :localTerm :Record ; :externalTerm <https://example.net/ExternalRecord> ;
    :sourceDocument <https://example.net/specification> ;
    :relation "comparison only" ; :rationale "Synthetic structural specimen." ;
    :reviewState "candidate" .
""",
        encoding="utf-8",
    )
    return tmp_path


def _core() -> Graph:
    return Graph().parse(ROOT / "ontology/core.ttl", format="turtle")


def test_repository_artifacts_reproduce() -> None:
    build(ROOT, check=True)


def test_serializations_reproduce_and_preserve_graph(fixture_root: Path) -> None:
    count = build(fixture_root)
    folder = fixture_root / "ontology"
    first = {path.name: path.read_bytes() for path in folder.iterdir()}
    assert build(fixture_root, check=True) == count
    build(fixture_root)
    assert {path.name: path.read_bytes() for path in folder.iterdir()} == first
    turtle = Graph().parse(folder / "core.ttl", format="turtle")
    assert set(Graph().parse(folder / "core.rdf", format="xml")) == set(turtle)
    assert set(Graph().parse(folder / "core.jsonld", format="json-ld")) == set(turtle)


def test_serializers_preserve_literal_lexical_content() -> None:
    graph = _core()
    graph.add(
        (
            LOCAL.Record,
            RDFS.label,
            Literal('Überlieferung <α> & "Zitat"\r\n', lang="de"),
        )
    )
    graph.add(
        (LOCAL.Record, RDFS.comment, Literal("Typed\tcontent", datatype=XSD.string))
    )
    assert set(Graph().parse(data=serialize_xml(graph), format="xml")) == set(graph)
    assert set(Graph().parse(data=serialize_jsonld(graph), format="json-ld")) == set(
        graph
    )


def test_cli_reports_invalid_turtle(
    fixture_root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
) -> None:
    (fixture_root / "ontology/core.ttl").write_text("@prefix broken", encoding="utf-8")
    monkeypatch.setattr(
        "sys.argv", ["check_ontology.py", "--root", str(fixture_root), "--check"]
    )
    assert main() == 1
    assert "FEHLER:" in capsys.readouterr().err


@pytest.mark.parametrize("name", ["core.rdf", "core.jsonld", "record-hierarchy.mmd"])
def test_stale_output_fails(fixture_root: Path, name: str) -> None:
    build(fixture_root)
    path = fixture_root / "ontology" / name
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="Stale generated artifact"):
        build(fixture_root, check=True)


def test_remote_jsonld_context_rejected_before_parsing(
    fixture_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    build(fixture_root)
    (fixture_root / "ontology/core.jsonld").write_text(
        '{"@context":"https://example.net/remote-context"}', encoding="utf-8"
    )
    original_parse = Graph.parse

    def local_parse(self: Graph, *args: object, **kwargs: object) -> Graph:
        assert kwargs.get("format") == "turtle", (
            "Untrusted generated JSON-LD must not reach the parser"
        )
        return original_parse(self, *args, **kwargs)

    monkeypatch.setattr(Graph, "parse", local_parse)
    with pytest.raises(ValueError, match="Stale generated artifact"):
        build(fixture_root, check=True)


@pytest.mark.parametrize(
    "predicate",
    [
        OWL.imports,
        OWL.equivalentClass,
        OWL.sameAs,
        OWL.hasKey,
        OWL.propertyChainAxiom,
        OWL.disjointWith,
    ],
)
def test_entailment_constructs_fail(predicate: URIRef) -> None:
    graph = _core()
    graph.add((LOCAL.Record, predicate, URIRef("https://example.net/ForeignClass")))
    with pytest.raises(ValueError, match="Prohibited core predicate"):
        validate_core(graph)


@pytest.mark.parametrize("predicate", [RDFS.subClassOf, RDFS.domain, RDFS.range])
def test_foreign_class_edges_fail(predicate: URIRef) -> None:
    graph = _core()
    subject = LOCAL.ReferentRecord if predicate == RDFS.subClassOf else LOCAL.member
    graph.add((subject, predicate, URIRef("https://example.net/Person")))
    with pytest.raises(ValueError, match="Foreign or undeclared class"):
        validate_core(graph)


def test_foreign_class_declaration_fails() -> None:
    graph = _core()
    graph.add((URIRef("https://example.net/Person"), RDF.type, OWL.Class))
    with pytest.raises(ValueError, match="Foreign declaration"):
        validate_core(graph)


def test_record_cannot_be_typed_as_a_foreign_person() -> None:
    graph = _core()
    graph.add((LOCAL.ReferentRecord, RDF.type, URIRef("https://example.net/Person")))
    with pytest.raises(ValueError, match="Prohibited core class membership"):
        validate_core(graph)


def test_undefined_local_reference_fails() -> None:
    graph = _core()
    graph.set((LOCAL.member, RDFS.range, LOCAL.MissingRecord))
    with pytest.raises(ValueError, match="Undefined local reference"):
        validate_core(graph)


def test_hierarchy_cycle_fails() -> None:
    graph = _core()
    graph.set((LOCAL.AnnotationRecord, RDFS.subClassOf, LOCAL.MentionRecord))
    with pytest.raises(ValueError, match="Class hierarchy cycle"):
        validate_core(graph)


def test_package_cannot_become_a_record() -> None:
    graph = _core()
    graph.add((LOCAL.Package, RDFS.subClassOf, LOCAL.Record))
    with pytest.raises(ValueError, match="separate hierarchy roots"):
        validate_core(graph)


@pytest.mark.parametrize("predicate", [RDFS.label, RDFS.comment])
def test_missing_class_definition_fails(predicate: URIRef) -> None:
    graph = _core()
    graph.remove((LOCAL.PropositionRecord, predicate, None))
    with pytest.raises(ValueError, match="Missing or invalid"):
        validate_core(graph)


def test_object_property_cannot_use_literal_range() -> None:
    graph = _core()
    graph.set((LOCAL.propositionObjectReference, RDFS.range, RDFS.Literal))
    with pytest.raises(ValueError, match="Foreign or undeclared class"):
        validate_core(graph)


def test_literal_property_cannot_classify_world_object() -> None:
    graph = _core()
    graph.set((LOCAL.propositionObjectLiteral, RDFS.range, LOCAL.ReferentRecord))
    with pytest.raises(ValueError, match="Unsupported literal range"):
        validate_core(graph)


def test_mapping_missing_rationale_fails(fixture_root: Path) -> None:
    graph = Graph().parse(
        fixture_root / "ontology/alignment-candidates.ttl", format="turtle"
    )
    graph.remove((LOCAL.testMapping, LOCAL.rationale, None))
    with pytest.raises(ValueError, match=r"requires exactly one .*rationale"):
        validate_mappings(graph, _core())


def test_mapping_cannot_activate_equivalence(fixture_root: Path) -> None:
    graph = Graph().parse(
        fixture_root / "ontology/alignment-candidates.ttl", format="turtle"
    )
    graph.add((LOCAL.Record, OWL.equivalentClass, URIRef("https://example.net/Record")))
    with pytest.raises(ValueError, match="Prohibited mapping entailment"):
        validate_mappings(graph, _core())


def test_mapping_field_cannot_be_an_object_property(fixture_root: Path) -> None:
    graph = Graph().parse(
        fixture_root / "ontology/alignment-candidates.ttl", format="turtle"
    )
    graph.set((LOCAL.externalTerm, RDF.type, OWL.ObjectProperty))
    with pytest.raises(ValueError, match="must be an annotation property"):
        validate_mappings(graph, _core())


def test_mapping_cannot_claim_acceptance(fixture_root: Path) -> None:
    graph = Graph().parse(
        fixture_root / "ontology/alignment-candidates.ttl", format="turtle"
    )
    graph.set((LOCAL.testMapping, LOCAL.reviewState, Literal("accepted")))
    with pytest.raises(ValueError, match="must remain candidate"):
        validate_mappings(graph, _core())
