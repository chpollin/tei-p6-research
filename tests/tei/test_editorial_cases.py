"""Mapping checks authored against the frozen bounded fragment policy."""

import copy
import json

import pytest

from tools.models.abstract_text import validate_model
from tools.tei.editorial_cases import (
    BINDING,
    MAPPING_RULES,
    candidate_observations,
    compare_fragment,
)


def body_annotation(package, element):
    return next(item for item in package["annotations"]
                if json.loads(item["body"])["element"] == element)


def change_body(package, element, change):
    annotation = body_annotation(package, element)
    body = json.loads(annotation["body"])
    change(body)
    annotation["body"] = json.dumps(body)


def test_nested_equal_extents_are_distinct_actual_nodes_and_values_survive():
    xml = '<head><date when="1790" calendar="#gregorian"><hi rendition="#u">A <hi rendition="#aq"><placeName ref="urn:place:1 urn:place:2">town</placeName></hi></hi></date></head>'
    result = compare_fragment(xml)
    assert result["observations_equal"]
    observation = result["candidate"]["observations"]
    assert observation["text"] == "A town"
    assert [(item["tag"], item["extent"]) for item in observation["elements"]] == [
        ("head", [0, 6]), ("date", [0, 6]), ("hi", [0, 6]), ("hi", [2, 6]), ("placeName", [2, 6])]
    nodes = result["candidate"]["package"]["readings"][0]["nodes"]
    assert len(nodes) == 5
    assert [(item["id"], item["parent"]) for item in nodes] == [
        ("n-e0", None), ("n-e0.0", "n-e0"), ("n-e0.0.0", "n-e0.0"),
        ("n-e0.0.0.0", "n-e0.0.0"), ("n-e0.0.0.0.0", "n-e0.0.0.0")]
    assert observation["elements"][-1]["attributes"] == {"ref": "urn:place:1 urn:place:2"}
    assert validate_model(result["candidate"]["package"])["valid"]


def test_note_exclusion_preserves_refs_nested_notes_pointer_values_and_lb():
    xml = '<head>Journey. <date when="1790">1790</date>. <lb/><note hand="#unknown"><ref xml:id="ref1" corresp="#note1" type="editorialNote">6255</ref><note xml:id="note1" corresp="#ref1" type="editorial" resp="#CT #DE">An editorial\n  explanation.</note> </note> <placeName ref="urn:place">England</placeName>.</head>'
    result = compare_fragment(xml)
    assert result["observations_equal"]
    observations = result["candidate"]["observations"]
    assert observations["text"] == "Journey. 1790. England."
    assert observations["breaks"] == [{"id": "e0.1", "parent": "e0", "attributes": {}, "offset": 15}]
    assert observations["notes"] == [
        {"id": "e0.2", "parent": "e0", "attributes": {"hand": "#unknown"}, "own_text": "6255", "refs": [
            {"id": "e0.2.0", "parent": "e0.2", "attributes": {
                "xml:id": "ref1", "corresp": "#note1", "type": "editorialNote"}, "text": "6255"}]},
        {"id": "e0.2.1", "parent": "e0.2", "attributes": {
            "xml:id": "note1", "corresp": "#ref1", "type": "editorial", "resp": "#CT #DE"},
         "own_text": "An editorial explanation.", "refs": []},
    ]
    assert {item["value"] for item in observations["pointers"]} >= {"#unknown", "#ref1", "#note1", "#CT #DE"}
    assert len(result["candidate"]["package"]["versions"]) == 1
    assert len(result["baseline"]["representation"]["stand_off"]) == 3


def test_tree_retains_parsed_text_tail_and_attributes_before_projection():
    result = compare_fragment('<p a="1"> A\n <hi rendition="#u">B &amp; C</hi>  D </p>')
    tree = result["baseline"]["representation"]["tree"]
    assert tree["text"] == " A\n "
    assert tree["attributes"] == {"a": "1"}
    assert tree["children"][0]["text"] == "B & C"
    assert tree["children"][0]["tail"] == "  D "
    assert result["candidate"]["observations"]["text"] == "A B & C D"
    assert result["candidate"]["observations"]["elements"][1]["extent"] == [2, 7]


def test_projection_codepoint_coordinates_and_empty_elements():
    result = compare_fragment('<p> \t😀 <hi> e\u0301 </hi> <name/> Z\n</p>')
    assert result["observations_equal"]
    assert result["candidate"]["observations"]["text"] == "😀 e\u0301 Z"
    assert [(item["tag"], item["extent"]) for item in result["candidate"]["observations"]["elements"]] == [
        ("p", [0, 6]), ("hi", [2, 4]), ("name", [5, 5])]
    assert len(result["candidate"]["package"]["readings"][0]["nodes"]) == 2
    assert compare_fragment("<head/>")["candidate"]["observations"]["text"] == ""


@pytest.mark.parametrize("xml,unsupported", [
    ("<p>A <seg>B</seg> C</p>", ["seg"]),
    ('<p xmlns:x="urn:foreign"><x:hi>A</x:hi></p>', ["{urn:foreign}hi"]),
    ("<p>A<!--remark--> B</p>", ["#comment"]),
    ("<p><?process data?>A</p>", ["#processing-instruction"]),
    ("<p>A<note><hi>B</hi></note></p>", ["note/hi"]),
    ("<p>A<note><ref><hi>B</hi></ref></note></p>", ["note/ref-children"]),
    ("<p>A<lb>B</lb></p>", ["lb/content"]),
])
def test_unsupported_constructs_are_retained_in_tree_and_refuse_candidate(xml, unsupported):
    result = compare_fragment(xml)
    assert result["baseline"]["representation"]["tree"]
    assert result["candidate"]["package"] is None
    assert result["candidate"]["observations"] is None
    assert result["candidate"]["valid"] is False
    assert result["candidate"]["unsupported"] == unsupported
    assert result["observations_equal"] is False


@pytest.mark.parametrize("xml", [
    None, [], 3, "", "text", "<p>", "<p/><head/>", "before<p/>", "<p/>after",
    '<!DOCTYPE p [<!ENTITY x "value">]><p>&x;</p>',
    '<!ENTITY x SYSTEM "file:///private"><p/>', '<?xml version="1.0"?><p/>',
    '<p>&unbound;</p>', '<p xmlns="broken>',
])
def test_malformed_xml_and_declarations_reject(xml):
    with pytest.raises(ValueError):
        compare_fragment(xml)


@pytest.mark.parametrize("change", ["missing-node-metadata", "missing-note-metadata", "missing-attributes", "extra-field", "wrong-type", "wrong-parent", "malformed-json"])
def test_decoder_detects_missing_or_inconsistent_scoped_metadata(change):
    model = compare_fragment('<head><hi>A</hi><note hand="#x">Note</note></head>')["candidate"]["package"]
    if change == "missing-node-metadata":
        model["annotations"].remove(body_annotation(model, "e0.0"))
    elif change == "missing-note-metadata":
        model["annotations"].remove(body_annotation(model, "e0.1"))
    elif change == "missing-attributes":
        change_body(model, "e0.0", lambda body: body.pop("attributes"))
    elif change == "extra-field":
        change_body(model, "e0.0", lambda body: body.update(unknown=True))
    elif change == "wrong-type":
        change_body(model, "e0.0", lambda body: body.update(tag="date"))
    elif change == "wrong-parent":
        model["readings"][0]["nodes"][1]["parent"] = None
    else:
        body_annotation(model, "e0.0")["body"] = "not JSON"
    with pytest.raises(ValueError):
        candidate_observations(model)


def test_same_extent_parent_mutation_is_checked_using_actual_reading_nodes():
    model = compare_fragment("<head><hi><date>A</date></hi></head>")["candidate"]["package"]
    model["readings"][0]["nodes"][2]["parent"] = "n-e0"
    assert not validate_model(model)["valid"]
    with pytest.raises(ValueError):
        candidate_observations(model)


def test_base_valid_hierarchy_change_still_disagrees_with_binding():
    model = compare_fragment("<head>A<hi>B<date>C</date></hi></head>")["candidate"]["package"]
    # Make the root extent's metadata claim the date is its direct child while
    # retaining the actual base-model hierarchy unchanged.
    change_body(model, "e0.0.0", lambda body: body.update(parent="e0"))
    assert validate_model(model)["valid"]
    with pytest.raises(ValueError, match="parent metadata"):
        candidate_observations(model)


def test_results_reproduce_and_decoder_never_mutates_input():
    xml = '<p>A <persName ref="#person">B</persName><note>Comment</note><lb/> C.</p>'
    first, second = compare_fragment(xml), compare_fragment(xml)
    assert first == second
    model = first["candidate"]["package"]
    snapshot = copy.deepcopy(model)
    observations = candidate_observations(model)
    observations["elements"][1]["attributes"]["ref"] = "changed"
    observations["notes"].clear()
    assert model == snapshot
    assert candidate_observations(model) == second["candidate"]["observations"]
    assert json.dumps(first, sort_keys=True, ensure_ascii=False) == json.dumps(second, sort_keys=True, ensure_ascii=False)


def test_binding_dependency_is_explicit_and_versioned():
    result = compare_fragment("<p>A</p>")
    assert MAPPING_RULES["version"] == BINDING
    assert any("binding" in item for item in result["candidate"]["limitations"])
    assert all(json.loads(item["body"])["binding"] == BINDING for item in result["candidate"]["package"]["annotations"])


def test_duplicate_note_reference_identity_is_rejected():
    model = compare_fragment("<p>A<note><ref>1</ref><ref>2</ref></note></p>")["candidate"]["package"]
    change_body(model, "e0.0", lambda body: body["refs"][1].update(id=body["refs"][0]["id"]))
    assert validate_model(model)["valid"]
    with pytest.raises(ValueError, match="reference metadata"):
        candidate_observations(model)
