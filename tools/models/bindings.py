"""Lossless reference bindings for the independent Abstract Text Model 0.1.

These are project-defined encodings, not official TEI syntax or P5 converters.
Every public operation validates the core package and does not mutate inputs.
See docs/p6/serialization-bindings-v0.1.md for the accepted lexical subset.
"""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from typing import Any

import yaml

from tools.models.abstract_text import COLLECTIONS, validate_model


BINDINGS = ("json", "xml", "yaml")
XML_NAMESPACE = "urn:tei-p6-research:abstract-text:0.1"
BINDING_VERSION = "0.1"
_RECORD_NAMES = dict(zip(COLLECTIONS, (
    "agent", "concept", "text", "version", "continuity", "selection",
    "reading", "annotation", "relation",
)))
_ARRAY_NAMES = {"nodes": "node", "segments": "segment"}
_INTEGER = re.compile(r"-?(?:0|[1-9][0-9]*)\Z")
_FIELD = re.compile(r"[a-z][a-z_0-9]*\Z")
_SPACE = " \t\r\n"
_XML_DECLARATION = re.compile(
    r'''<\?xml\s+version\s*=\s*(['"])1\.0\1'''
    r'''(?:\s+encoding\s*=\s*(['"])UTF-8\2)?'''
    r'''(?:\s+standalone\s*=\s*(['"])(?:yes|no)\3)?\s*\?>''', re.IGNORECASE,
)


def _fail(message: str) -> None:
    raise ValueError(message)


def _binding(binding: str) -> None:
    if type(binding) is not str or binding not in BINDINGS:
        _fail("Unsupported binding; expected json, xml, or yaml")


def _tree(value: Any, active: set[int] | None = None, depth: int = 0) -> None:
    """Reject non-model Python types, cycles, and impossible depth."""
    if depth > 32:
        _fail("Binding nesting exceeds the closed model shape")
    if value is None or type(value) is int:
        return
    if type(value) is str:
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as error:
            raise ValueError("Strings must contain Unicode scalar values") from error
        return
    if type(value) not in (dict, list):
        _fail("Only model objects, arrays, strings, integers, and null are allowed")
    active = set() if active is None else active
    if id(value) in active:
        _fail("Cyclic containers are not model data")
    active.add(id(value))
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            _fail("Object keys must be strings")
        children = value.values()
    else:
        children = value
    for child in children:
        _tree(child, active, depth + 1)
    active.remove(id(value))


def _validate(package: Any) -> dict:
    _tree(package)
    result = validate_model(package)
    if not result["valid"]:
        raise ValueError(result["diagnostics"])
    return package


def _pairs(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        if type(key) is not str or key in result:
            _fail("Object keys must be unique strings")
        result[key] = value
    return result


def _json(text: str) -> Any:
    return json.loads(text, object_pairs_hook=_pairs,
                      parse_constant=lambda value: _fail("Non-finite JSON number"))


class _Loader(yaml.SafeLoader):
    """Small YAML scalar vocabulary; no aliases, merge interpretation, or tags."""

    yaml_implicit_resolvers: dict = {}

    def compose_node(self, parent, index):
        event = self.peek_event()
        if isinstance(event, yaml.AliasEvent) or getattr(event, "anchor", None):
            _fail("YAML anchors and aliases are outside this binding")
        return super().compose_node(parent, index)

    def construct_object(self, node, deep=False):
        if node.tag not in {
            "tag:yaml.org,2002:str", "tag:yaml.org,2002:int",
            "tag:yaml.org,2002:null", "tag:yaml.org,2002:map",
            "tag:yaml.org,2002:seq",
        }:
            _fail("YAML tag is outside the reference binding")
        return super().construct_object(node, deep=deep)

    def construct_mapping(self, node, deep=False):
        if not isinstance(node, yaml.MappingNode):
            _fail("Expected a YAML mapping")
        return _pairs([(self.construct_object(key, deep=True),
                        self.construct_object(value, deep=True))
                       for key, value in node.value])


def _yaml_int(loader, node):
    value = loader.construct_scalar(node)
    if _INTEGER.fullmatch(value) is None:
        _fail("YAML integers use decimal JSON notation")
    return int(value)


def _yaml_null(loader, node):
    if loader.construct_scalar(node) != "null":
        _fail("YAML null is spelled null")
    return None


_Loader.add_implicit_resolver("tag:yaml.org,2002:int", _INTEGER, list("-0123456789"))
_Loader.add_implicit_resolver("tag:yaml.org,2002:null", re.compile(r"null\Z"), ["n"])
# Recognize JSON booleans and non-integer numbers so they fail as unsupported
# model types rather than silently becoming strings in labels or model_version.
_Loader.add_implicit_resolver("tag:yaml.org,2002:bool", re.compile(r"(?:true|false)\Z"), list("tf"))
_Loader.add_implicit_resolver("tag:yaml.org,2002:float", re.compile(
    r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+(?:[eE][+-]?[0-9]+)?|[eE][+-]?[0-9]+)\Z"
), list("-0123456789"))
_Loader.add_constructor("tag:yaml.org,2002:int", _yaml_int)
_Loader.add_constructor("tag:yaml.org,2002:null", _yaml_null)


class _Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _yaml_string(dumper, value):
    # Quote every value/key: strings such as null, 01, yes and dates stay strings
    # even for readers using a broader YAML schema. Double quotes preserve CR.
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style='"')


_Dumper.add_representer(str, _yaml_string)


def _xml_string(value: str) -> bool:
    return all(character != "\r" and (
        character in "\t\n" or 0x20 <= ord(character) <= 0xD7FF
        or 0xE000 <= ord(character) <= 0xFFFD
        or 0x10000 <= ord(character) <= 0x10FFFF
    ) for character in value)


def _write_field(parent: ET.Element, name: str, value: Any) -> None:
    element = ET.SubElement(parent, name)
    if value is None:
        element.set("type", "null")
    elif type(value) is str:
        element.set("type", "string")
        if _xml_string(value):
            element.text = value
        else:
            element.set("encoding", "json-string")
            element.text = json.dumps(value, ensure_ascii=True)
    elif type(value) is int:
        element.set("type", "integer")
        element.text = str(value)
    elif type(value) is list:
        element.set("type", "array")
        for item in value:
            _write_field(element, _ARRAY_NAMES.get(name, "item"), item)
    else:
        element.set("type", "object")
        for key, item in value.items():
            _write_field(element, key, item)


def _encode_xml(package: dict) -> str:
    root = ET.Element("model", {
        "xmlns": XML_NAMESPACE, "binding_version": BINDING_VERSION, "model_version": "0.1",
    })
    for name in COLLECTIONS:
        collection = ET.SubElement(root, name)
        for item in package[name]:
            _write_field(collection, _RECORD_NAMES[name], item)
    # Indent only structural whitespace; ElementTree never rewrites scalar text.
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="unicode") + "\n"


class _XMLTree(ET.TreeBuilder):
    def doctype(self, name, pubid, system):
        _fail("XML DTD declarations are outside this binding")

    def comment(self, text):
        _fail("XML comments are outside this binding")

    def pi(self, target, text):
        _fail("XML processing instructions are outside this binding")


def _name(element: ET.Element) -> str:
    prefix = "{" + XML_NAMESPACE + "}"
    if type(element.tag) is not str or not element.tag.startswith(prefix):
        _fail("Every XML element must use the model namespace")
    name = element.tag[len(prefix):]
    if _FIELD.fullmatch(name) is None:
        _fail("Invalid model XML element name")
    return name


def _structure(element: ET.Element) -> None:
    if (element.text or "").strip(_SPACE):
        _fail("Text is not allowed between structured XML fields")
    if any((child.tail or "").strip(_SPACE) for child in element):
        _fail("Text is not allowed after structured XML fields")


def _read_field(element: ET.Element, depth: int = 0) -> Any:
    if depth > 32:
        _fail("Binding nesting exceeds the closed model shape")
    name = _name(element)
    kind = element.get("type")
    allowed = {"type", "encoding"} if kind == "string" else {"type"}
    if not set(element.attrib).issubset(allowed) or kind is None:
        _fail("Unknown or missing XML field attribute")
    if kind in ("object", "array"):
        _structure(element)
        if kind == "object":
            return _pairs([(_name(child), _read_field(child, depth + 1)) for child in element])
        expected = _ARRAY_NAMES.get(name, "item")
        if any(_name(child) != expected for child in element):
            _fail("Unexpected XML array item element")
        return [_read_field(child, depth + 1) for child in element]
    if len(element):
        _fail("Scalar XML fields cannot contain elements")
    value = element.text or ""
    if kind == "null":
        if value:
            _fail("XML null has no text")
        return None
    if kind == "integer":
        if _INTEGER.fullmatch(value) is None:
            _fail("XML integer uses decimal JSON notation")
        return int(value)
    if kind == "string":
        if "encoding" not in element.attrib:
            return value
        if element.get("encoding") != "json-string":
            _fail("Unknown XML string encoding")
        decoded = _json(value)
        if type(decoded) is not str:
            _fail("An encoded XML string must decode to a string")
        return decoded
    _fail("Unknown XML field type")


def _decode_xml(text: str) -> dict:
    if "\r" in text:
        _fail("Literal XML carriage returns would be normalized; use an encoded string")
    declaration_input = text.removeprefix("\ufeff")
    if declaration_input.startswith("<?xml") and not _XML_DECLARATION.match(declaration_input):
        _fail("An XML declaration must specify XML 1.0 and, if present, UTF-8")
    root = ET.fromstring(text, parser=ET.XMLParser(target=_XMLTree()))
    if _name(root) != "model" or root.attrib != {
        "binding_version": BINDING_VERSION, "model_version": "0.1",
    }:
        _fail("Wrong XML model root, binding version, or model version")
    _structure(root)
    package = {"model_version": "0.1"}
    for collection in root:
        name = _name(collection)
        if name not in COLLECTIONS or name in package or collection.attrib:
            _fail("Unknown, duplicate, or attributed XML collection")
        _structure(collection)
        if any(_name(record) != _RECORD_NAMES[name] for record in collection):
            _fail("Unexpected XML record element")
        package[name] = [_read_field(record) for record in collection]
    return package


def encode_model(package: dict, binding: str) -> str:
    """Encode a valid package without normalization; raise ValueError otherwise."""
    _binding(binding)
    _validate(package)
    if binding == "json":
        return json.dumps(package, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if binding == "yaml":
        return yaml.dump(package, Dumper=_Dumper, allow_unicode=True,
                         sort_keys=False, width=100, line_break="\n")
    return _encode_xml(package)


def decode_model(text: str, binding: str) -> dict:
    """Decode and validate; malformed syntax and invalid models raise ValueError."""
    _binding(binding)
    if type(text) is not str:
        _fail("Binding input must be Unicode text")
    try:
        _tree(text)
        if binding == "json":
            package = _json(text)
        elif binding == "yaml":
            package = yaml.load(text, Loader=_Loader)
        else:
            package = _decode_xml(text)
        return _validate(package)
    except (ET.ParseError, yaml.YAMLError, RecursionError) as error:
        raise ValueError("Malformed " + binding + " binding: " + str(error)) from error
