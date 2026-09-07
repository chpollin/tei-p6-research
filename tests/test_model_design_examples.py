"""Check the three manually maintained views in ``knowledge/model-examples.md``.

The tests parse XML, JSON, and Turtle independently, compare their complete
record content, and enforce the bounded illustrative contract documented next
to the examples. They deliberately do not provide a general model validator.
"""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest
from rdflib import RDF, Graph, Literal, Namespace, URIRef

DOCUMENT = Path(__file__).resolve().parents[1] / "knowledge" / "model-examples.md"
DESIGN = Namespace("https://example.org/tei-design/")
CASE_BASE = "https://example.org/tei-design/cases/"
XML_NAMESPACE = "https://example.org/tei-design/"

EXPECTED_CASE_IDS = {
    "atlantis-example",
    "claim-stance-example",
    "letter-example",
    "name-use-example",
    "olympus-example",
    "organization-example",
}
RESOURCE_REFERENCE_FIELDS = {"claim", "selection", "source", "version"}
INTEGER_FIELDS = {"end", "start"}
ARGUMENT_MODES = {"concept", "proposition", "record", "referent"}
STANCES = {"assert", "deny", "question", "report"}
LIFECYCLES = {"active", "withdrawn"}
SCOPES = {
    "assessment",
    "constructed-scenario",
    "geographic-hypothesis",
    "narrative",
    "text-interpretation",
    "tradition-report",
}

SECTION_PATTERN = re.compile(
    r"^### (?P<title>.+?)\n(?P<body>.*?)(?=^### |^## |\Z)", re.MULTILINE | re.DOTALL
)
FENCE_PATTERN = re.compile(
    r"```(?P<language>xml|json|turtle)\n(?P<body>.*?)```", re.DOTALL
)


@dataclass(frozen=True)
class ExampleViews:
    """One example represented by its three independently parsed views."""

    xml: dict[str, Any]
    json: dict[str, Any]
    rdf: Graph


def _xml_record(element: ET.Element) -> dict[str, Any]:
    record: dict[str, Any] = dict(element.attrib)
    for field in INTEGER_FIELDS & record.keys():
        record[field] = int(record[field])
    return record


def _parse_xml(source: str) -> dict[str, Any]:
    root = ET.fromstring(source)
    prefix = f"{{{XML_NAMESPACE}}}"
    assert root.tag == f"{prefix}example"
    return {
        **root.attrib,
        "resources": [
            _xml_record(element)
            for element in root.findall(f"{prefix}resources/{prefix}resource")
        ],
        "propositions": [
            _xml_record(element)
            for element in root.findall(f"{prefix}propositions/{prefix}proposition")
        ],
        "claims": [
            _xml_record(element)
            for element in root.findall(f"{prefix}claims/{prefix}claim")
        ],
    }


def _parse_examples() -> dict[str, ExampleViews]:
    text = DOCUMENT.read_text(encoding="utf-8")
    examples: dict[str, ExampleViews] = {}
    for section in SECTION_PATTERN.finditer(text):
        matches = list(FENCE_PATTERN.finditer(section.group("body")))
        fences = {match.group("language"): match.group("body") for match in matches}
        if not fences:
            continue
        assert len(matches) == 3, section.group("title")
        assert set(fences) == {"json", "turtle", "xml"}, section.group("title")
        xml = _parse_xml(fences["xml"])
        json_view = json.loads(fences["json"])
        assert xml["id"] == json_view["id"], section.group("title")
        assert xml["id"] not in examples, xml["id"]
        graph = Graph().parse(data=fences["turtle"], format="turtle")
        examples[xml["id"]] = ExampleViews(xml=xml, json=json_view, rdf=graph)
    return examples


@pytest.fixture(scope="module")
def examples() -> dict[str, ExampleViews]:
    return _parse_examples()


def _indexed(records: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    materialized = list(records)
    indexed = {record["id"]: record for record in materialized}
    assert len(indexed) == len(materialized)
    return indexed


def _expected_graph(package: dict[str, Any]) -> Graph:
    graph = Graph()
    local = Namespace(f"{CASE_BASE}{package['id']}/")
    example = local[package["id"]]
    graph.add((example, RDF.type, DESIGN.Example))
    graph.add((example, DESIGN.agent, local[package["agent"]]))

    groups = (
        ("resources", DESIGN.Resource, DESIGN.hasResource),
        ("propositions", DESIGN.Proposition, DESIGN.hasProposition),
        ("claims", DESIGN.Claim, DESIGN.hasClaim),
    )
    for group, role, membership in groups:
        for record in package[group]:
            subject = local[record["id"]]
            graph.add((example, membership, subject))
            graph.add((subject, RDF.type, role))
            for field, value in record.items():
                if field == "id":
                    continue
                is_reference = (
                    group == "propositions"
                    or (group == "resources" and field in RESOURCE_REFERENCE_FIELDS)
                    or (group == "claims" and field in {"agent", "proposition"})
                )
                object_ = local[value] if is_reference else Literal(value)
                graph.add((subject, DESIGN[field], object_))
    return graph


def _proposition_by_predicate(
    package: dict[str, Any], predicate: str
) -> list[dict[str, Any]]:
    return [
        proposition
        for proposition in package["propositions"]
        if proposition["predicate"] == predicate
    ]


def test_document_contains_exactly_the_six_bounded_cases(
    examples: dict[str, ExampleViews],
) -> None:
    assert set(examples) == EXPECTED_CASE_IDS


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_xml_and_json_have_identical_complete_records(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    xml = examples[case_id].xml
    json_view = examples[case_id].json

    assert (
        set(xml)
        == set(json_view)
        == {
            "agent",
            "claims",
            "id",
            "propositions",
            "resources",
        }
    )
    assert {"id": xml["id"], "agent": xml["agent"]} == {
        "id": json_view["id"],
        "agent": json_view["agent"],
    }
    for group in ("resources", "propositions", "claims"):
        assert _indexed(xml[group]) == _indexed(json_view[group])


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_turtle_is_the_exact_rdf_projection_including_membership(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    actual = examples[case_id].rdf
    expected = _expected_graph(examples[case_id].json)
    assert set(actual) == set(expected), {
        "missing": set(expected) - set(actual),
        "unexpected": set(actual) - set(expected),
    }


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_identifiers_and_references_are_closed_and_typed(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    package = examples[case_id].json
    resources = _indexed(package["resources"])
    propositions = _indexed(package["propositions"])
    claims = _indexed(package["claims"])
    assert len(resources | propositions | claims) == sum(
        map(len, (resources, propositions, claims))
    )

    assert resources[package["agent"]]["kind"] == "AgentRecord"
    for resource in resources.values():
        for field in RESOURCE_REFERENCE_FIELDS & resource.keys():
            target = claims if field == "claim" else resources
            assert resource[field] in target

    for proposition in propositions.values():
        assert (
            proposition["subject"] in resources
            or proposition["subject"] in propositions
        )
        assert (
            proposition["object"] in resources or proposition["object"] in propositions
        )
        assert resources[proposition["predicate"]]["kind"] == "PredicateDefinition"
        assert resources[proposition["context"]]["kind"] == "ContextRecord"
        if "evidence" in proposition:
            assert resources[proposition["evidence"]]["kind"] == "SelectionRecord"

    for claim in claims.values():
        assert claim["proposition"] in propositions
        assert resources[claim["agent"]]["kind"] == "AgentRecord"


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_selections_use_exact_unicode_code_point_boundaries(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    resources = _indexed(examples[case_id].json["resources"])
    for selection in resources.values():
        if selection["kind"] != "SelectionRecord":
            continue
        representation = resources[selection["version"]]
        assert representation["kind"] == "RepresentationRecord"
        assert (
            representation["content"][selection["start"] : selection["end"]]
            == selection["quote"]
        )


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_argument_modes_stances_lifecycles_and_scopes_are_known(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    package = examples[case_id].json
    resources = _indexed(package["resources"])
    for resource in resources.values():
        if resource["kind"] == "PredicateDefinition":
            assert resource["subjectInterpretation"] in ARGUMENT_MODES
            assert resource["objectInterpretation"] in ARGUMENT_MODES
        if resource["kind"] == "ContextRecord":
            assert resource["scope"] in SCOPES
    for claim in package["claims"]:
        assert claim["stance"] in STANCES
        assert claim["lifecycle"] in LIFECYCLES

    assert STANCES.isdisjoint(LIFECYCLES)
    assert "deny" in STANCES
    assert "withdrawn" in LIFECYCLES


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_predicate_argument_modes_match_their_referenced_records(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    package = examples[case_id].json
    resources = _indexed(package["resources"])
    propositions = _indexed(package["propositions"])
    expected_kinds = {
        "concept": "ConceptDefinition",
        "referent": "ReferentRecord",
    }
    for proposition in propositions.values():
        predicate = resources[proposition["predicate"]]
        for field, mode_field in (
            ("subject", "subjectInterpretation"),
            ("object", "objectInterpretation"),
        ):
            target_id = proposition[field]
            mode = predicate[mode_field]
            if mode == "proposition":
                assert target_id in propositions
            elif mode in expected_kinds:
                assert resources[target_id]["kind"] == expected_kinds[mode]
            else:
                assert target_id in resources


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_rdf_contains_no_unqualified_domain_relations(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    graph = examples[case_id].rdf
    local_prefix = f"{CASE_BASE}{case_id}/"
    assert not {
        predicate
        for _, predicate, _ in graph
        if isinstance(predicate, URIRef) and str(predicate).startswith(local_prefix)
    }


def test_victoria_uses_one_form_for_two_occurrences_and_referents(
    examples: dict[str, ExampleViews],
) -> None:
    package = examples["name-use-example"].json
    resources = _indexed(package["resources"])

    realizations = _proposition_by_predicate(package, "realizes-name")
    assert {(item["subject"], item["object"]) for item in realizations} == {
        ("M1", "N1"),
        ("M2", "N1"),
    }
    denotations = _proposition_by_predicate(package, "denotes")
    assert {(item["subject"], item["object"]) for item in denotations} == {
        ("M1", "P1"),
        ("M2", "P2"),
    }
    classifications = _proposition_by_predicate(package, "name-use-type")
    assert {(item["subject"], item["object"]) for item in classifications} == {
        ("M1", "person-name-use"),
        ("M2", "place-name-use"),
    }
    assert resources["N1"] == {
        "id": "N1",
        "kind": "NameFormRecord",
        "form": "Victoria",
        "language": "und",
    }


def test_three_agents_take_distinct_stances_on_one_proposition(
    examples: dict[str, ExampleViews],
) -> None:
    package = examples["claim-stance-example"].json
    assert len(package["propositions"]) == 1
    assert {
        (claim["proposition"], claim["agent"], claim["stance"], claim["lifecycle"])
        for claim in package["claims"]
    } == {
        ("Q1", "A", "assert", "active"),
        ("Q1", "B", "report", "active"),
        ("Q1", "C", "deny", "active"),
    }


@pytest.mark.parametrize("case_id", sorted(EXPECTED_CASE_IDS))
def test_name_forms_have_no_intrinsic_referent_or_name_use_type(
    examples: dict[str, ExampleViews], case_id: str
) -> None:
    package = examples[case_id].json
    resources = _indexed(package["resources"])
    name_form_ids = {
        identifier
        for identifier, resource in resources.items()
        if resource["kind"] == "NameFormRecord"
    }
    for identifier in name_form_ids:
        assert set(resources[identifier]) == {"form", "id", "kind", "language"}
    assert not {
        proposition["id"]
        for proposition in package["propositions"]
        if proposition["predicate"] == "name-use-type"
        and proposition["subject"] in name_form_ids
    }
