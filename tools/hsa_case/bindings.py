"""Strict case bindings; graph shape and source meaning are checked separately."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape, quoteattr

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

from tools.hsa_case.config import (
    CASE,
    COMPACT_BINDING,
    NS,
    P6,
    PROFILE,
    VOC,
    XML_BINDING,
)


def turtle(graph: Graph) -> bytes:
    prefixes = (
        ("p6", P6),
        ("case", CASE),
        ("v", VOC),
        ("xsd", XSD),
        ("rdf", RDF),
        ("rdfs", RDFS),
        ("owl", OWL),
    )
    for name, namespace in prefixes:
        graph.bind(name, namespace, replace=True)
    namespaces = graph.namespace_manager
    declarations = "\n".join(
        f"@prefix {name}: <{namespace}> ." for name, namespace in sorted(prefixes)
    )
    lines = sorted(
        " ".join(term.n3(namespace_manager=namespaces) for term in triple) + " ."
        for triple in graph
    )
    return (declarations + "\n\n" + "\n".join(lines) + "\n").encode("utf-8")


PREFIXES = {
    "case": str(CASE),
    "p6": str(P6),
    "v": str(VOC),
    "xsd": str(XSD),
    "rdf": str(RDF),
}
COMPONENTS = {"complete", "semantic", "preservation"}


def _iri(value, *, compact: bool) -> URIRef:
    if (
        not isinstance(value, str)
        or not value
        or re.search(r'[\s<>"{}|\\^\x00-\x1f]', value)
    ):
        raise ValueError("invalid binding IRI")
    prefix, separator, suffix = value.partition(":")
    if compact and prefix in PREFIXES and suffix:
        return URIRef(PREFIXES[prefix] + suffix)
    if not separator or prefix not in {"http", "https", "urn"} or not suffix:
        raise ValueError("unsupported IRI or undeclared prefix")
    return URIRef(value)


def _short(value: URIRef, binding: int) -> str:
    if binding == 2:
        for prefix, namespace in PREFIXES.items():
            if str(value).startswith(namespace):
                return prefix + ":" + str(value)[len(namespace) :]
    return str(value)


def _keys(value, expected: set[str], label: str) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        raise ValueError(f"unexpected {label} fields")


def _unique_object(pairs: list[tuple]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _literal(value: dict, *, compact: bool) -> Literal:
    if set(value) not in ({"value", "datatype"}, {"value", "lang"}):
        raise ValueError("literal requires exactly one datatype or language")
    content = value["value"]
    if not isinstance(content, str):
        raise ValueError("literal value must be a string")
    try:
        content.encode("utf-8")
    except UnicodeError as exc:
        raise ValueError("literal must contain valid Unicode") from exc
    if "lang" in value:
        lang = value["lang"]
        if not isinstance(lang, str) or not re.fullmatch(
            r"[a-zA-Z]+(?:-[a-zA-Z0-9]+)*", lang
        ):
            raise ValueError("invalid language tag")
        return Literal(content, lang=lang, normalize=False)
    return Literal(
        content, datatype=_iri(value["datatype"], compact=compact), normalize=False
    )


def json_data(graph: Graph, *, binding: int = 2, component: str = "complete") -> dict:
    if (
        binding not in (1, 2)
        or component not in COMPONENTS
        or (binding == 1 and component != "complete")
    ):
        raise ValueError("unsupported binding or component")
    records = []
    for subject in sorted(set(graph.subjects()), key=str):
        kinds = list(graph.objects(subject, RDF.type))
        if len(kinds) != 1:
            raise ValueError(f"record requires one documentary type: {subject}")
        properties = {}
        for predicate, obj in sorted(
            graph.predicate_objects(subject),
            key=lambda pair: tuple(term.n3() for term in pair),
        ):
            if predicate == RDF.type:
                continue
            if isinstance(obj, URIRef):
                value = {"ref": _short(obj, binding)}
            elif isinstance(obj, Literal):
                value = {"value": str(obj)}
                if obj.language:
                    value["lang"] = obj.language
                elif obj.datatype:
                    value["datatype"] = _short(obj.datatype, binding)
                else:
                    raise ValueError("untyped literal outside the binding")
            else:
                raise ValueError("blank nodes outside the binding")
            properties.setdefault(_short(predicate, binding), []).append(value)
        records.append(
            {
                "id": _short(subject, binding),
                "type": _short(kinds[0], binding),
                "properties": properties,
            }
        )
    result = {
        "profile": PROFILE,
        "package": _short(CASE.package, binding),
        "records": records,
    }
    if binding == 2:
        result.update(binding=COMPACT_BINDING, component=component)
    return result


def graph_from_data(data: dict) -> Graph:
    compact = isinstance(data, dict) and "binding" in data
    _keys(
        data,
        {"profile", "package", "records"}
        | ({"binding", "component"} if compact else set()),
        "envelope",
    )
    if compact and (
        data["binding"] != COMPACT_BINDING
        or not isinstance(data["component"], str)
        or data["component"] not in COMPONENTS
    ):
        raise ValueError("unsupported binding or component")
    if (
        data["profile"] != PROFILE
        or _iri(data["package"], compact=compact) != CASE.package
    ):
        raise ValueError("unexpected case binding profile")
    if not isinstance(data["records"], list) or not data["records"]:
        raise ValueError("records must be a nonempty array")
    graph, seen = Graph(), set()
    for entry in data["records"]:
        _keys(entry, {"id", "type", "properties"}, "record")
        subject = _iri(entry["id"], compact=compact)
        if subject in seen:
            raise ValueError("duplicate record identifier")
        seen.add(subject)
        graph.add((subject, RDF.type, _iri(entry["type"], compact=compact)))
        if not isinstance(entry["properties"], dict):
            raise ValueError("record properties must be an object")
        predicates = set()
        for name, values in entry["properties"].items():
            predicate = _iri(name, compact=compact)
            if predicate == RDF.type or predicate in predicates:
                raise ValueError("duplicate property or rdf:type inside properties")
            predicates.add(predicate)
            if not isinstance(values, list) or not values:
                raise ValueError("property values must be a nonempty array")
            for value in values:
                if not isinstance(value, dict):
                    raise ValueError("invalid value object")
                if "ref" in value:
                    _keys(value, {"ref"}, "reference")
                    obj = _iri(value["ref"], compact=compact)
                else:
                    obj = _literal(value, compact=compact)
                if (subject, predicate, obj) in graph:
                    raise ValueError("duplicate property value")
                graph.add((subject, predicate, obj))
    return graph


def parse_json(payload: bytes) -> Graph:
    return graph_from_data(json.loads(payload, object_pairs_hook=_unique_object))


def xml_data(data: dict) -> bytes:
    graph_from_data(data)
    compact = "binding" in data
    namespace = COMPACT_BINDING if compact else XML_BINDING
    attributes = f" component={quoteattr(data['component'])}" if compact else ""
    lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        f'<case xmlns="{namespace}" profile="{PROFILE}" package={quoteattr(data["package"])}{attributes}>',
    ]
    for entry in data["records"]:
        lines.append(
            f"  <record id={quoteattr(entry['id'])} type={quoteattr(entry['type'])}>"
        )
        for predicate, values in entry["properties"].items():
            lines.append(f"    <property iri={quoteattr(predicate)}>")
            for value in values:
                if "ref" in value:
                    lines.append(f"      <ref iri={quoteattr(value['ref'])}/>")
                else:
                    attributes = (
                        f" datatype={quoteattr(value['datatype'])}"
                        if "datatype" in value
                        else f" xml:lang={quoteattr(value['lang'])}"
                    )
                    content = escape(value["value"]).replace("\r", "&#13;")
                    lines.append(
                        f'      <literal{attributes} xml:space="preserve">{content}</literal>'
                    )
            lines.append("    </property>")
        lines.append("  </record>")
    return ("\n".join([*lines, "</case>"]) + "\n").encode("utf-8")


def _container(element: ET.Element, tag: str, attributes: set[str]) -> None:
    if element.tag != tag or set(element.attrib) != attributes:
        raise ValueError("unexpected XML element or attributes")
    if (element.text or "").strip() or any(
        (child.tail or "").strip() for child in element
    ):
        raise ValueError("unexpected XML container text")


def parse_xml(payload: bytes) -> Graph:
    decoded = payload.decode("utf-8")
    if "<!DOCTYPE" in decoded.upper() or "<!ENTITY" in decoded.upper():
        raise ValueError("XML declarations outside the case binding")
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True, insert_pis=True))
    root = ET.fromstring(decoded, parser=parser)
    compact = root.tag == "{" + COMPACT_BINDING + "}case"
    namespace = "{" + (COMPACT_BINDING if compact else XML_BINDING) + "}"
    _container(
        root,
        namespace + "case",
        {"profile", "package"} | ({"component"} if compact else set()),
    )
    data = {
        "profile": root.get("profile"),
        "package": root.get("package"),
        "records": [],
    }
    if compact:
        data.update(binding=COMPACT_BINDING, component=root.get("component"))
    for entry in root:
        _container(entry, namespace + "record", {"id", "type"})
        record = {"id": entry.get("id"), "type": entry.get("type"), "properties": {}}
        for prop in entry:
            _container(prop, namespace + "property", {"iri"})
            name = prop.get("iri")
            if name in record["properties"]:
                raise ValueError("duplicate XML property")
            values = []
            for value in prop:
                if len(value):
                    raise ValueError("unexpected child inside XML value")
                if value.tag == namespace + "ref":
                    if set(value.attrib) != {"iri"} or value.text:
                        raise ValueError("unexpected XML reference content")
                    values.append({"ref": value.get("iri")})
                elif value.tag == namespace + "literal":
                    space, lang = "{" + NS["xml"] + "}space", "{" + NS["xml"] + "}lang"
                    if (
                        set(value.attrib) not in ({space, "datatype"}, {space, lang})
                        or value.get(space) != "preserve"
                    ):
                        raise ValueError("unexpected XML literal attributes")
                    literal = {"value": value.text or ""}
                    if "datatype" in value.attrib:
                        literal["datatype"] = value.get("datatype")
                    else:
                        literal["lang"] = value.get(lang)
                    values.append(literal)
                else:
                    raise ValueError("unexpected XML value kind")
            record["properties"][name] = values
        data["records"].append(record)
    return graph_from_data(data)
