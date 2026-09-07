"""Check the bounded HSA case against its complete real admitted source.

Adverse graph mutations distinguish preservation, import reporting and source
context errors. The clean fixture copies tracked inputs without any raw store.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest
from rdflib import Graph, Literal
from rdflib.namespace import OWL, RDF, XSD

from tools.build_hsa_case import (
    BASE,
    CASE,
    P6,
    REPRESENTATION,
    ROOT,
    SHA256,
    VOC,
    build,
    create_case,
    parse_json,
    parse_xml,
    source_bytes,
    validate_case,
)
from tools.hsa_case.bindings import json_data, xml_data
from tools.hsa_case.components import split_graph


@pytest.fixture
def fixture_root(tmp_path: Path) -> Path:
    for path in (REPRESENTATION, Path("ontology/core.ttl")):
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, target)
    return tmp_path


@pytest.fixture
def case() -> tuple[Graph, bytes]:
    payload = source_bytes()
    graph, _ = create_case(payload)
    return graph, payload


def test_repository_case_reproduces() -> None:
    assert build(check=True)["counts"]["editorial_notes"] == 11


def test_clean_checkout_needs_no_raw_source(fixture_root: Path) -> None:
    assert not (fixture_root / "00_sources").exists()
    build(fixture_root)
    folder = fixture_root / BASE
    first = {path.name: path.read_bytes() for path in folder.iterdir()}
    build(fixture_root, check=True)
    build(fixture_root)
    assert {path.name: path.read_bytes() for path in folder.iterdir()} == first
    assert hashlib.sha256(first["p5.xml"]).hexdigest() == SHA256
    json_graph = parse_json(first["p6.json"])
    xml_graph = parse_xml(first["p6.xml"])
    rdf_graph = Graph().parse(data=first["p6.ttl"], format="turtle")
    assert set(json_graph) == set(xml_graph) == set(rdf_graph)
    validate_case(rdf_graph, first["p5.xml"], fixture_root, semantic=True)
    for parser, extension in (
        (parse_json, "json"),
        (parse_xml, "xml"),
        (lambda data: Graph().parse(data=data, format="turtle"), "ttl"),
    ):
        complete = rdf_graph + parser(first["preservation." + extension])
        validate_case(complete, first["p5.xml"], fixture_root)
        expected, _ = create_case(first["p5.xml"])
        assert set(complete) == set(expected)


def test_typed_literals_survive_all_bindings() -> None:
    folder = ROOT / BASE
    for graph in (
        parse_json((folder / "p6.json").read_bytes()),
        parse_xml((folder / "p6.xml").read_bytes()),
        Graph().parse(folder / "p6.ttl", format="turtle"),
    ):
        date = graph.value(CASE["proposition-origin-date"], P6.propositionObjectLiteral)
        assert date == Literal("1878-04-17", datatype=XSD.date)
        year = graph.value(
            CASE["proposition-publication-year"], P6.propositionObjectLiteral
        )
        assert year == Literal("2022", datatype=XSD.gYear)
        assert all(
            value.datatype == RDF.JSON
            for value in graph.objects(None, VOC.xmlAttributes)
        )


def test_notes_are_separate_and_tails_remain(case: tuple[Graph, bytes]) -> None:
    graph, _ = case
    letter = str(graph.value(CASE["representation-letter"], P6.content))
    for number, punctuation in (("10", "?"), ("11", ".")):
        selection = CASE["selection-note-insertion-" + number]
        start = int(graph.value(selection, P6.start))
        assert graph.value(selection, P6.start) == graph.value(selection, P6.end)
        assert letter[start] == punctuation
    start_two = int(graph.value(CASE["selection-note-insertion-02"], P6.start))
    assert letter[start_two:].startswith(" Spuren wahrer Freundschaft")
    assert "G.L. Frollo" not in letter
    assert "G.L. Frollo" in str(graph.value(CASE["representation-note-08"], P6.content))
    assert letter.count("+") == 2
    assert not list(graph.objects(CASE["representation-note-08"], P6.language))


def test_exact_forms_and_distinct_mentions(case: tuple[Graph, bytes]) -> None:
    graph, _ = case
    assert str(graph.value(CASE["selection-mention-diez"], P6.quote)) == "\nDiez"
    assert str(graph.value(CASE["form-diez"], P6.form)) == "\nDiez"
    assert str(graph.value(CASE["form-frollo"], P6.form)) == "Frollo"
    assert str(graph.value(CASE["form-frollo-note"], P6.form)) == "G.L. Frollo"
    assert (
        graph.value(CASE["selection-mention-frollo-note"], P6.representation)
        == CASE["representation-note-08"]
    )
    assert str(graph.value(CASE["form-signature"], P6.form)) == "H. Schuchardt"


def test_source_anomalies_remain_observations(case: tuple[Graph, bytes]) -> None:
    graph, _ = case
    for name, value in (
        ("source-pid", "o:hsa.letter.4493"),
        ("source-div-id", "L.4492"),
        ("carrier-repository", "Unbekannt"),
        ("geo-lexical", "15.45,47.06667"),
        ("dateline", " Graz 17. 4. 78. "),
    ):
        assert (
            str(graph.value(CASE["proposition-" + name], P6.propositionObjectLiteral))
            == value
        )
    attributes = [
        json.loads(str(value)) for value in graph.objects(None, VOC.xmlAttributes)
    ]
    assert {"rend": "unknown", "rendition": "#none"} in attributes
    assert not list(graph.triples((None, OWL.sameAs, None)))
    assert not any("received-date" in str(subject) for subject in graph.subjects())


def test_text_document_carrier_are_connected_by_responsible_constructions(
    case: tuple[Graph, bytes],
) -> None:
    graph, _ = case
    for name, subject, obj in (
        ("text-document", "text-letter", "letter"),
        ("document-carrier", "letter", "carrier"),
    ):
        proposition = CASE["proposition-" + name]
        claim = CASE["claim-" + name]
        assert graph.value(proposition, P6.propositionSubject) == CASE[subject]
        assert graph.value(proposition, P6.propositionObjectReference) == CASE[obj]
        assert graph.value(proposition, P6.context) == CASE["context-construction"]
        assert str(graph.value(claim, P6.stance)) == "assert"
        assert graph.value(claim, P6.claimAgent) == CASE.importer
        assert graph.value(claim, VOC.construction)
        assert graph.value(claim, VOC.sourceLocation)


def test_referent_expectations_are_local_concepts(case: tuple[Graph, bytes]) -> None:
    graph, _ = case
    for referent in graph.subjects(RDF.type, P6.ReferentRecord):
        expected = graph.value(referent, P6.expectedReferentType)
        assert (expected, RDF.type, P6.ConceptRecord) in graph
        assert graph.value(expected, P6.definition)
        assert list(graph.objects(referent, RDF.type)) == [P6.ReferentRecord]
    assert (
        graph.value(CASE["person-schuchardt"], P6.expectedReferentType)
        == CASE["concept-Person"]
    )
    assert graph.value(CASE.carrier, P6.expectedReferentType) != graph.value(
        CASE.letter, P6.expectedReferentType
    )


def test_changed_date_context_fails(case: tuple[Graph, bytes]) -> None:
    graph, payload = case
    graph.set((CASE["proposition-origin-date"], P6.context, CASE["context-sending"]))
    with pytest.raises(ValueError, match="source mapping mismatch"):
        validate_case(graph, payload)


def test_changed_reported_date_fails(case: tuple[Graph, bytes]) -> None:
    graph, payload = case
    graph.set(
        (
            CASE["proposition-origin-date"],
            P6.propositionObjectLiteral,
            Literal("1878-04-18", datatype=XSD.date),
        )
    )
    with pytest.raises(ValueError, match="reported literal differs"):
        validate_case(graph, payload)


def test_flattened_note_fails(case: tuple[Graph, bytes]) -> None:
    graph, payload = case
    graph.set((CASE["note-08"], P6.annotationBody, CASE["representation-letter"]))
    with pytest.raises(ValueError, match="flattened or redirected note"):
        validate_case(graph, payload)


def test_note_content_in_letter_fails(case: tuple[Graph, bytes]) -> None:
    graph, payload = case
    content = str(graph.value(CASE["representation-letter"], P6.content))
    content += str(graph.value(CASE["representation-note-08"], P6.content))
    graph.set(
        (
            CASE["representation-letter"],
            P6.content,
            Literal(content, datatype=XSD.string),
        )
    )
    with pytest.raises(ValueError, match="letter/note projection mismatch"):
        validate_case(graph, payload)


def test_wrong_range_fails_even_with_self_consistent_quote(
    case: tuple[Graph, bytes],
) -> None:
    graph, payload = case
    selection = CASE["selection-mention-diez"]
    start = int(graph.value(selection, P6.start)) + 1
    graph.set((selection, P6.start, Literal(start, datatype=XSD.nonNegativeInteger)))
    graph.set((selection, P6.quote, Literal("Diez", datatype=XSD.string)))
    with pytest.raises(ValueError, match="mention differs from checked source"):
        validate_case(graph, payload)


def test_missing_claim_source_fails(case: tuple[Graph, bytes]) -> None:
    graph, payload = case
    graph.remove((CASE["claim-origin-date"], VOC.sourceLocation, None))
    with pytest.raises(ValueError, match=r"expected exactly one .*sourceLocation"):
        validate_case(graph, payload)


def test_broken_record_reference_fails(case: tuple[Graph, bytes]) -> None:
    graph, payload = case
    graph.set((CASE["claim-origin-date"], P6.claimAgent, CASE.missing))
    with pytest.raises(ValueError, match="unresolved record reference"):
        validate_case(graph, payload)


def test_source_tree_reparenting_fails(case: tuple[Graph, bytes]) -> None:
    graph, payload = case
    graph.set((CASE["source-node-005"], VOC.parent, CASE["source-node-000"]))
    with pytest.raises(ValueError, match="preserved source hierarchy"):
        validate_case(graph, payload)


def test_tampered_snapshot_fails(fixture_root: Path) -> None:
    path = fixture_root / REPRESENTATION
    path.write_bytes(
        path.read_bytes().replace(b'when="1878-04-17"', b'when="1878-04-18"', 1)
    )
    with pytest.raises(ValueError, match="source snapshot hash mismatch"):
        build(fixture_root)


@pytest.mark.parametrize(
    "filename",
    [
        "p5.xml",
        "p6.json",
        "p6.xml",
        "p6.ttl",
        "vocabulary.ttl",
        "instance.mmd",
        "coverage.json",
        "preservation.json",
        "preservation.xml",
        "preservation.ttl",
    ],
)
def test_check_detects_stale_output_without_rewriting(
    fixture_root: Path, filename: str
) -> None:
    build(fixture_root)
    target = fixture_root / BASE / filename
    changed = target.read_bytes() + b"\n"
    target.write_bytes(changed)
    with pytest.raises(ValueError, match="stale generated case file"):
        build(fixture_root, check=True)
    assert target.read_bytes() == changed


@pytest.mark.parametrize(
    "subject,predicate,value",
    [
        ("proposition-sender", P6.propositionObjectReference, CASE["person-hasdeu"]),
        (
            "proposition-recipient",
            P6.propositionObjectReference,
            CASE["person-schuchardt"],
        ),
        ("proposition-sending-date", P6.propositionPredicate, CASE["predicate-author"]),
        (
            "proposition-sending-date",
            P6.propositionObjectLiteral,
            Literal("1878-04-17", datatype=XSD.string),
        ),
        ("proposition-sending-place", P6.propositionSubject, CASE.carrier),
        (
            "proposition-denotation-frollo",
            P6.propositionObjectReference,
            CASE["person-diez"],
        ),
        ("claim-sender", P6.stance, Literal("assert", datatype=XSD.string)),
        ("claim-sender", P6.lifecycle, Literal("withdrawn", datatype=XSD.string)),
        (
            "claim-text-document",
            VOC.construction,
            Literal("Unjustified replacement", datatype=XSD.string),
        ),
        (
            "predicate-sender",
            P6.subjectInterpretation,
            Literal("record", datatype=XSD.string),
        ),
        ("form-diez", P6.form, Literal("Diez", datatype=XSD.string)),
        ("mention-frollo", P6.annotationClaim, CASE["claim-denotation-diez"]),
    ],
)
def test_semantic_mutations_fail_in_both_component_modes(
    case, subject, predicate, value
):
    graph, payload = case
    graph.set((CASE[subject], predicate, value))
    with pytest.raises(ValueError):
        validate_case(graph, payload)
    semantic, _ = split_graph(graph)
    with pytest.raises(ValueError):
        validate_case(semantic, payload, semantic=True)


@pytest.mark.parametrize(
    "subject,predicate,value",
    [
        ("person-schuchardt", P6.expectedReferentType, CASE["concept-MaterialCarrier"]),
        (
            "context-sending",
            P6.scope,
            Literal("source-carrier-origin", datatype=XSD.string),
        ),
        (
            "concept-Person",
            P6.definition,
            Literal("A material object", datatype=XSD.string),
        ),
    ],
)
def test_changed_referent_and_context_meaning_fails(case, subject, predicate, value):
    graph, payload = case
    graph.set((CASE[subject], predicate, value))
    with pytest.raises(ValueError):
        validate_case(graph, payload)


def test_self_consistent_redirect_to_equal_date_source_fails(case):
    graph, payload = case
    support = graph.value(CASE["claim-origin-date"], VOC.sourceLocation)
    for name in ("claim-sending-date", "proposition-sending-date"):
        graph.set((CASE[name], VOC.sourceLocation, support))
    with pytest.raises(ValueError, match="source mapping location"):
        validate_case(graph, payload)


@pytest.mark.parametrize(
    "mutation",
    [
        "extra-object",
        "extra-type",
        "missing-predicate",
        "wrong-object-kind",
        "wrong-range-datatype",
        "unexpected-property",
    ],
)
def test_closed_record_shapes_reject_ambiguous_graphs(case, mutation):
    graph, payload = case
    if mutation == "extra-object":
        graph.add(
            (
                CASE["proposition-sender"],
                P6.propositionObjectLiteral,
                Literal("Schuchardt", datatype=XSD.string),
            )
        )
    elif mutation == "extra-type":
        graph.add((CASE["person-schuchardt"], RDF.type, P6.AgentRecord))
    elif mutation == "missing-predicate":
        graph.remove((CASE["proposition-sender"], P6.propositionPredicate, None))
    elif mutation == "wrong-object-kind":
        graph.set(
            (
                CASE["claim-sender"],
                P6.claimAgent,
                Literal("importer", datatype=XSD.string),
            )
        )
    elif mutation == "wrong-range-datatype":
        graph.set(
            (
                CASE["selection-mention-diez"],
                P6.start,
                Literal("244", datatype=XSD.string),
            )
        )
    else:
        graph.add(
            (CASE["person-schuchardt"], P6.language, Literal("de", datatype=XSD.string))
        )
    with pytest.raises(ValueError):
        validate_case(graph, payload)


def test_complete_and_semantic_preservation_guarantees_are_distinct(case):
    graph, payload = case
    semantic, preservation = split_graph(graph)
    assert set(semantic) | set(preservation) == set(graph)
    assert not list(semantic.objects(None, VOC.xmlAttributes))
    assert not list(semantic.objects(None, VOC.sourceValue))
    assert not list(semantic.objects(CASE["representation-source-xml"], P6.content))
    validate_case(semantic, payload, semantic=True)
    with pytest.raises(ValueError):
        validate_case(semantic, payload)
    for binding in (1, 2):
        data = json_data(graph, binding=binding)
        assert set(parse_json(json.dumps(data).encode())) == set(graph)
        assert set(parse_xml(xml_data(data))) == set(graph)


def test_compact_union_is_smaller_than_full_legacy_bindings(case):
    graph, _ = case
    semantic, preservation = split_graph(graph)
    old = json_data(graph, binding=1)
    parts = [json_data(part) for part in (semantic, preservation)]
    assert (
        sum(len(json.dumps(part, indent=2)) for part in parts)
        < len(json.dumps(old, indent=2)) * 0.8
    )
    assert sum(len(xml_data(part)) for part in parts) < len(xml_data(old)) * 0.8
