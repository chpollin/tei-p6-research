"""Reject silent input loss and preserve literal identity across binding versions."""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
from rdflib import Graph, Literal
from rdflib.namespace import RDF, XSD

from tools.hsa_case.bindings import json_data, parse_json, parse_xml, xml_data
from tools.hsa_case.config import CASE, COMPACT_BINDING, P6, PROFILE, XML_BINDING


@pytest.fixture
def graph():
    graph = Graph()
    graph.add((CASE.example, RDF.type, P6.RepresentationRecord))
    graph.add(
        (
            CASE.example,
            P6.content,
            Literal(" A\r\nΩ 😀 <&> ", datatype=XSD.string, normalize=False),
        )
    )
    return graph


@pytest.mark.parametrize("binding", [1, 2])
def test_exact_literal_and_language_preservation(graph, binding):
    graph.add((CASE.example, P6.preferredLabel, Literal(" Österreich ", lang="de")))
    graph.add(
        (
            CASE.example,
            P6.start,
            Literal("007", datatype=XSD.nonNegativeInteger, normalize=False),
        )
    )
    data = json_data(graph, binding=binding)
    assert set(parse_json(json.dumps(data).encode())) == set(graph)
    assert set(parse_xml(xml_data(data))) == set(graph)
    assert str(parse_xml(xml_data(data)).value(CASE.example, P6.start)) == "007"


def test_independently_written_legacy_binding_is_readable():
    data = {
        "profile": PROFILE,
        "package": str(CASE.package),
        "records": [
            {
                "id": str(CASE.example),
                "type": str(P6.PropositionRecord),
                "properties": {
                    str(P6.propositionObjectLiteral): [
                        {"value": "1878-04-17", "datatype": str(XSD.date)}
                    ]
                },
            }
        ],
    }
    expected = {
        (CASE.example, RDF.type, P6.PropositionRecord),
        (
            CASE.example,
            P6.propositionObjectLiteral,
            Literal("1878-04-17", datatype=XSD.date),
        ),
    }
    assert set(parse_json(json.dumps(data).encode())) == expected
    xml = f'<case xmlns="{XML_BINDING}" profile="{PROFILE}" package="{CASE.package}"><record id="{CASE.example}" type="{P6.PropositionRecord}"><property iri="{P6.propositionObjectLiteral}"><literal datatype="{XSD.date}" xml:space="preserve">1878-04-17</literal></property></record></case>'
    assert set(parse_xml(xml.encode())) == expected


@pytest.mark.parametrize(
    "mutation",
    [
        "unknown-envelope",
        "unknown-record",
        "unknown-reference",
        "ambiguous-reference",
        "untyped-literal",
        "language-and-datatype",
        "numeric-literal",
        "unknown-value",
        "duplicate-id",
        "duplicate-triple",
        "empty-property",
        "object-as-values",
        "array-as-properties",
        "array-as-record",
        "unknown-prefix",
        "bad-iri",
        "extra-type",
        "aliased-property",
        "unknown-binding",
        "unknown-component",
        "bad-language",
    ],
)
def test_json_rejects_lossy_or_ambiguous_input(graph, mutation):
    data = json_data(graph)
    entry = data["records"][0]
    key = "p6:content"
    value = entry["properties"][key][0]
    if mutation == "unknown-envelope":
        data["ignored"] = "lost input"
    elif mutation == "unknown-record":
        entry["ignored"] = True
    elif mutation in {"unknown-reference", "ambiguous-reference"}:
        entry["properties"][key] = [
            {
                "ref": "case:example",
                "ignored" if mutation == "unknown-reference" else "value": "lost input",
            }
        ]
    elif mutation == "untyped-literal":
        del value["datatype"]
    elif mutation == "language-and-datatype":
        value["lang"] = "de"
    elif mutation == "numeric-literal":
        value["value"] = 42
    elif mutation == "unknown-value":
        value["ignored"] = True
    elif mutation == "duplicate-id":
        data["records"].append(entry.copy())
    elif mutation == "duplicate-triple":
        entry["properties"][key].append(value.copy())
    elif mutation == "empty-property":
        entry["properties"][key] = []
    elif mutation == "object-as-values":
        entry["properties"][key] = value
    elif mutation == "array-as-properties":
        entry["properties"] = []
    elif mutation == "array-as-record":
        data["records"][0] = []
    elif mutation == "unknown-prefix":
        entry["id"] = "unknown:example"
    elif mutation == "bad-iri":
        entry["id"] = "case:example with space"
    elif mutation == "extra-type":
        entry["properties"]["rdf:type"] = [{"ref": "p6:Record"}]
    elif mutation == "aliased-property":
        entry["properties"][str(P6.content)] = [value.copy()]
    elif mutation == "unknown-binding":
        data["binding"] = COMPACT_BINDING + "x"
    elif mutation == "unknown-component":
        data["component"] = "unknown"
    else:
        value.pop("datatype")
        value["lang"] = " "
    with pytest.raises(ValueError):
        parse_json(json.dumps(data).encode())


def test_duplicate_json_keys_fail_before_dictionary_collapse(graph):
    encoded = json.dumps(json_data(graph)).replace(
        '"profile":', '"profile": "ignored", "profile":', 1
    )
    with pytest.raises(ValueError, match="duplicate JSON key"):
        parse_json(encoded.encode())


def test_documented_fragments_match_each_other_and_the_case():
    root = Path(__file__).resolve().parents[1]
    document = (root / "knowledge/hsa-profile.md").read_text(encoding="utf-8")
    blocks = dict(re.findall(r"```(json|xml|turtle)\n(.*?)\n```", document, re.DOTALL))
    data = {
        "profile": PROFILE,
        "package": "case:package",
        "binding": COMPACT_BINDING,
        "component": "semantic",
        "records": [json.loads(blocks["json"])],
    }
    xml = f'<case xmlns="{COMPACT_BINDING}" profile="{PROFILE}" package="case:package" component="semantic">{blocks["xml"]}</case>'
    rdf = Graph().parse(data=blocks["turtle"], format="turtle")
    assert (
        set(parse_json(json.dumps(data).encode()))
        == set(parse_xml(xml.encode()))
        == set(rdf)
    )
    case = Graph().parse(root / "experiments/hsa_letter_4493/p6.ttl", format="turtle")
    assert set(rdf) <= set(case)


@pytest.mark.parametrize(
    "mutation",
    [
        "unknown-root-child",
        "unknown-record-child",
        "unknown-root-attribute",
        "unknown-record-attribute",
        "unknown-property-attribute",
        "unknown-literal-attribute",
        "literal-child",
        "mixed-text",
        "tail-text",
        "literal-type-and-language",
        "duplicate-id",
        "duplicate-property",
        "duplicate-value",
        "unknown-value",
        "empty-property",
        "comment-child",
        "pi-child",
        "doctype",
        "missing-space",
    ],
)
def test_xml_rejects_unconsumed_content(graph, mutation):
    root = ET.fromstring(xml_data(json_data(graph)))
    record, prop, literal = root[0], root[0][0], root[0][0][0]
    if mutation == "unknown-root-child":
        ET.SubElement(root, "unknown")
    elif mutation == "unknown-record-child":
        ET.SubElement(record, "unknown")
    elif mutation.startswith("unknown-") and mutation.endswith("-attribute"):
        target = {"root": root, "record": record, "property": prop, "literal": literal}[
            mutation.split("-")[1]
        ]
        target.set("ignored", "lost input")
    elif mutation == "literal-child":
        ET.SubElement(literal, "unknown").text = "lost input"
    elif mutation == "mixed-text":
        record.text = "lost input"
    elif mutation == "tail-text":
        literal.tail = "lost input"
    elif mutation == "literal-type-and-language":
        literal.set("{http://www.w3.org/XML/1998/namespace}lang", "de")
    elif mutation == "duplicate-id":
        root.append(record)
    elif mutation == "duplicate-property":
        record.append(prop)
    elif mutation == "duplicate-value":
        prop.append(literal)
    elif mutation == "unknown-value":
        literal.tag = "unknown"
    elif mutation == "empty-property":
        prop.remove(literal)
    elif mutation == "comment-child":
        root.append(ET.Comment("unconsumed"))
    elif mutation == "pi-child":
        root.append(ET.ProcessingInstruction("unconsumed", "data"))
    elif mutation == "missing-space":
        literal.attrib.pop("{http://www.w3.org/XML/1998/namespace}space")
    encoded = ET.tostring(root, encoding="utf-8")
    if mutation == "doctype":
        encoded = b'<!DOCTYPE case [<!ENTITY custom "lost input">]>' + encoded
    with pytest.raises(ValueError):
        parse_xml(encoded)
