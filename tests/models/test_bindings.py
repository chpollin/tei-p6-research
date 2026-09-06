"""Binding fidelity across the independent model fixtures and hostile syntax."""

import copy
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from tools.models.abstract_text import COLLECTIONS, canonical_bytes, validate_model
from tools.models.bindings import BINDINGS, XML_NAMESPACE, decode_model, encode_model

ROOT = Path(__file__).resolve().parents[2]


def _fixtures():
    models = {}
    for path in (ROOT / "experiments/abstract_text_v01/cases.json",
                 ROOT / "experiments/editorial_cases/identity-cases.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        models.update({path.parent.name + "/" + key: value
                       for key, value in data["models"].items()})
    for path in (ROOT / "experiments/abstract_text_v01/examples").glob("*.json"):
        models[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return models


MODELS = _fixtures()
VALID = {key: model for key, model in MODELS.items() if validate_model(model)["valid"]}
INVALID = {key: model for key, model in MODELS.items() if not validate_model(model)["valid"]}


def package(content="Text"):
    result = {"model_version": "0.1", **{kind: [] for kind in COLLECTIONS}}
    result["agents"] = [{"id": "a", "label": "Editor"}]
    result["versions"] = [{"id": "v", "content": content,
                           "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                           "parents": []}]
    return result


def _xml_change(model, change):
    root = ET.fromstring(encode_model(model, "xml"))
    change(root)
    return ET.tostring(root, encoding="unicode")


def _find(root, path):
    return root.find("/".join("{" + XML_NAMESPACE + "}" + name for name in path.split("/")))


@pytest.mark.parametrize("name", VALID)
@pytest.mark.parametrize("binding", BINDINGS)
def test_all_valid_existing_models_preserve_exact_data_and_semantics(name, binding):
    model = VALID[name]
    before = copy.deepcopy(model)
    encoded = encode_model(model, binding)
    decoded = decode_model(encoded, binding)
    assert decoded == model
    assert canonical_bytes(decoded) == canonical_bytes(model)
    assert model == before
    assert encode_model(decoded, binding) == encoded
    # Every incoming binding also survives both alternative outgoing bindings.
    for other in BINDINGS:
        assert decode_model(encode_model(decoded, other), other) == model


@pytest.mark.parametrize("name", INVALID)
@pytest.mark.parametrize("binding", BINDINGS)
def test_all_invalid_existing_models_are_rejected_before_encoding(name, binding):
    model = INVALID[name]
    before = copy.deepcopy(model)
    with pytest.raises(ValueError):
        encode_model(model, binding)
    assert model == before


@pytest.mark.parametrize("binding", BINDINGS)
@pytest.mark.parametrize("content", [
    "", " ", "\t\n  \n\t", "a\r\nb\rc\n", "\x00\x01\x0b\x1f",
    "\u0085\u2028\u2029", "😀e\u0301é\ufffe\uffff\U0010ffff",
    '<tag attr="x"> & entities &#13; </tag>', '"quoted" \\ \\u0000',
])
def test_exact_string_edge_cases_in_content_and_metadata(binding, content):
    model = package(content)
    model["agents"][0]["label"] = content or "Empty content"
    if content:
        model["selections"] = [{"id": "s", "version": "v", "selector": {
            "kind": "ranges", "segments": [{"start": 0, "end": len(content), "quote": content}]}}]
        model["annotations"] = [{"id": "a1", "agent": "a", "selection": "s", "body": content}]
    assert decode_model(encode_model(model, binding), binding) == model


def test_xml_exposes_named_records_and_escapes_only_individual_strings():
    text = encode_model(package("A\r\nB\x00"), "xml")
    assert '<model xmlns="' + XML_NAMESPACE + '"' in text
    assert '<version type="object">' in text
    assert '<content type="string" encoding="json-string">"A\\r\\nB\\u0000"</content>' in text
    assert '<parents type="array" />' in text
    assert "base64" not in text
    assert "\r" not in text


@pytest.mark.parametrize("binding", BINDINGS)
@pytest.mark.parametrize("invalid", [None, True, 3.5, [], {"model_version": "0.1"}])
def test_nonmodels_fail_consistently(binding, invalid):
    with pytest.raises(ValueError):
        encode_model(invalid, binding)


@pytest.mark.parametrize("binding", BINDINGS)
def test_bad_hash_and_unknown_field_and_unresolved_reference_fail_on_decode(binding):
    model = package()
    text = encode_model(model, binding)
    bad_hash = text.replace(model["versions"][0]["sha256"], "0" * 64)
    with pytest.raises(ValueError):
        decode_model(bad_hash, binding)
    if binding == "xml":
        unknown = _xml_change(model, lambda root: ET.SubElement(root, "unknown"))
        reference = _xml_change(model, lambda root: _find(root, "versions/version/parents").append(
            ET.fromstring('<item xmlns="' + XML_NAMESPACE + '" type="string">missing</item>')))
    else:
        unknown_model = {**model, "unknown": []}
        ref_model = copy.deepcopy(model)
        ref_model["versions"][0]["parents"] = ["missing"]
        # JSON text is also in the accepted YAML syntax subset.
        unknown, reference = json.dumps(unknown_model), json.dumps(ref_model)
    for malformed in (unknown, reference):
        with pytest.raises(ValueError):
            decode_model(malformed, binding)


@pytest.mark.parametrize("binding", BINDINGS)
def test_scalar_types_cannot_be_coerced(binding):
    model = package()
    model["selections"] = [{"id": "s", "version": "v", "selector": {"kind": "point", "offset": 0}}]
    if binding == "xml":
        text = _xml_change(model, lambda root: _find(root, "selections/selection/selector/offset").set("type", "string"))
    else:
        model["selections"][0]["selector"]["offset"] = "0"
        text = json.dumps(model)
    with pytest.raises(ValueError):
        decode_model(text, binding)


@pytest.mark.parametrize("text", [
    '{"model_version":"0.1","model_version":"0.1"}',
    '{"x":NaN}', '{"x":Infinity}', '{"x":1.5}', '{"x":true}',
    '{"x":"\\ud800"}', '[]', '{} {}',
])
def test_json_rejects_duplicate_keys_nonmodel_numbers_and_malformed_shapes(text):
    with pytest.raises(ValueError):
        decode_model(text, "json")


@pytest.mark.parametrize("addition", [
    '<!DOCTYPE model [<!ENTITY a "expanded">]>',
    '<!DOCTYPE model SYSTEM "file:///private-file">',
    '<!-- comment -->', '<?instruction value?>',
])
def test_xml_rejects_dtd_entities_comments_and_processing_instructions(addition):
    with pytest.raises(ValueError):
        decode_model(addition + encode_model(package(), "xml"), "xml")


@pytest.mark.parametrize("change", [
    lambda root: root.set("binding_version", "2"),
    lambda root: root.set("model_version", "2"),
    lambda root: root.set("extra", "value"),
    lambda root: root.append(copy.deepcopy(root[0])),
    lambda root: root.remove(root[-1]),
    lambda root: _find(root, "agents/agent").append(copy.deepcopy(_find(root, "agents/agent/label"))),
    lambda root: _find(root, "agents/agent/label").set("encoding", "base64"),
    lambda root: _find(root, "agents/agent/label").set("extra", "value"),
    lambda root: _find(root, "agents/agent/label").set("type", "float"),
    lambda root: setattr(_find(root, "agents/agent"), "text", "unexpected mixed text"),
    lambda root: setattr(_find(root, "agents/agent/id"), "tail", "unexpected tail"),
    lambda root: setattr(_find(root, "agents/agent/id"), "tag", "id"),
    lambda root: _find(root, "agents/agent/id").append(ET.Element("child")),
    lambda root: _find(root, "versions/version/parents").append(ET.fromstring(
        '<wrong xmlns="' + XML_NAMESPACE + '" type="string">v</wrong>')),
])
def test_xml_rejects_altered_vocabulary_and_structure(change):
    with pytest.raises(ValueError):
        decode_model(_xml_change(package(), change), "xml")


def test_xml_literal_cr_is_rejected_and_reference_cr_is_preserved():
    text = encode_model(package(), "xml")
    with pytest.raises(ValueError):
        decode_model(text.replace("Editor", "E\rditor"), "xml")
    assert decode_model(text.replace("Editor", "E&#13;ditor"), "xml")["agents"][0]["label"] == "E\rditor"


@pytest.mark.parametrize("declaration", [
    '<?xml version="1.1"?>', '<?xml version="1.0" encoding="ISO-8859-1"?>',
    '<?xml version="1.0" encoding="UTF-16"?>',
])
def test_xml_declaration_cannot_change_the_binding_character_contract(declaration):
    with pytest.raises(ValueError):
        decode_model(declaration + encode_model(package(), "xml"), "xml")


@pytest.mark.parametrize("declaration", [
    '<?xml version="1.0"?>', "<?xml version='1.0' encoding='utf-8'?>",
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
])
def test_xml_accepts_an_optional_utf8_declaration(declaration):
    model = package("é")
    assert decode_model(declaration + encode_model(model, "xml"), "xml") == model


@pytest.mark.parametrize("value", ['"\\ud800"', "42", "null", "{}", '"unterminated'])
def test_xml_encoded_string_requires_a_valid_unicode_json_string(value):
    def change(root):
        label = _find(root, "agents/agent/label")
        label.set("encoding", "json-string")
        label.text = value
    with pytest.raises(ValueError):
        decode_model(_xml_change(package(), change), "xml")


@pytest.mark.parametrize("text", [
    'model_version: "0.1"\nmodel_version: "0.1"',
    'x: !!python/object/apply:os.system ["echo must-not-run"]',
    'x: &anchor []\ny: *anchor', 'x: &loop [*loop]',
    'x: !!timestamp 2026-09-05', 'x: !!binary SGVsbG8=', 'x: !!set {}',
    'x: !!int 01', 'x: !!int 0x12', 'x: !!null ~',
    'x: true', 'x: false', 'x: 1.2', 'x: 1e2',
    '---\n{}\n---\n{}', '1: value', 'x: {a: 1, a: 2}',
    'x: {<<: {id: a}}', 'x: "\\uD800"',
])
def test_yaml_rejects_unsafe_ambiguous_or_nonmodel_input(text):
    with pytest.raises(ValueError):
        decode_model(text, "yaml")


@pytest.mark.parametrize("label", ["yes", "on", "off", "2026-09-05", "null", "true", "01", "1.2", "~"])
def test_yaml_generated_strings_keep_their_types_under_standard_safe_loader(label):
    import yaml
    model = package()
    model["agents"][0]["label"] = label
    text = encode_model(model, "yaml")
    assert yaml.safe_load(text) == model
    assert decode_model(text, "yaml") == model


@pytest.mark.parametrize("binding", BINDINGS)
def test_nontext_input_cycles_and_lone_surrogates_fail(binding):
    for text in (b"bytes", None, 1, "\ud800"):
        with pytest.raises(ValueError):
            decode_model(text, binding)
    cyclic = package()
    cyclic["agents"] = [cyclic]
    with pytest.raises(ValueError):
        encode_model(cyclic, binding)


@pytest.mark.parametrize("binding", ["XML", "rdf", "", None, []])
def test_binding_names_are_explicit(binding):
    with pytest.raises(ValueError):
        encode_model(package(), binding)
    with pytest.raises(ValueError):
        decode_model("{}", binding)
