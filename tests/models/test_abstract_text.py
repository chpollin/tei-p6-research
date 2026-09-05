"""Implementation-unit checks; independent scenario expectations live elsewhere."""

import copy
import hashlib
import json

import pytest

from tools.models.abstract_text import (
    COLLECTIONS, canonical_bytes, check_revision, equivalent, propose_reanchor,
    validate_model,
)


def version(identifier="v1", content="alpha beta alpha", parents=None):
    return {"id": identifier, "content": content,
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "parents": [] if parents is None else parents}


def package(content="alpha beta alpha"):
    result = {kind: [] for kind in COLLECTIONS}
    result.update(model_version="0.1", agents=[{"id": "a", "label": "Editor"}],
                  texts=[{"id": "t", "label": "Text"}], versions=[version(content=content)],
                  continuities=[{"id": "c", "text": "t", "versions": ["v1"],
                                 "agent": "a", "criterion": "Same editorial work"}])
    return result


def selection(identifier, start, end, content="alpha beta alpha", version_id="v1"):
    return {"id": identifier, "version": version_id, "selector": {
        "kind": "ranges", "segments": [{"start": start, "end": end, "quote": content[start:end]}]}}


def reading_package():
    result = package()
    result["concepts"] = [{"id": "section", "label": "Section", "definition": "A section",
                           "applies_to": "node"}]
    result["selections"] = [selection("whole", 0, 16), selection("first", 0, 5), selection("last", 11, 16)]
    result["readings"] = [{"id": "reading", "version": "v1", "agent": "a", "label": "Structure",
                           "nodes": [{"id": "root", "type": "section", "selection": "whole", "parent": None},
                                     {"id": "n1", "type": "section", "selection": "first", "parent": "root"},
                                     {"id": "n2", "type": "section", "selection": "last", "parent": "root"}]}]
    return result


def codes(result):
    return {item["code"] for item in result["diagnostics"]}


def test_empty_package_is_valid_without_claiming_editorial_adequacy():
    result = validate_model({"model_version": "0.1", **{kind: [] for kind in COLLECTIONS}})
    assert result == {"valid": True, "all_selections_resolved": True,
                      "diagnostics": [], "resolutions": {}}


@pytest.mark.parametrize("malformed", [None, [], True, 1, "package", {"model_version": "0.1"}])
def test_nonpackages_return_shape_diagnostic(malformed):
    assert codes(validate_model(malformed)) == {"E_SHAPE"}
    with pytest.raises(ValueError):
        canonical_bytes(malformed)


@pytest.mark.parametrize("path,value", [
    (("agents",), {}), (("agents", 0), []), (("agents", 0, "label"), "\ud800"),
    (("versions", 0, "content"), "\udfff"), (("versions", 0, "parents"), [False]),
    (("versions", 0, "parents"), [{}]), (("versions", 0, "parents"), "v1"),
    (("versions", 0, "sha256"), []), (("agents", 0, "id"), {}),
    (("agents", 0, "id"), "a\n"), (("continuities", 0, "versions"), []),
    (("continuities", 0, "versions"), ["v1", "v1"]),
    (("continuities", 0, "agent"), ["a"]), (("model_version",), 0.1),
])
def test_malformed_fields_do_not_raise_or_mutate(path, value):
    model = package()
    destination = model
    for key in path[:-1]:
        destination = destination[key]
    destination[path[-1]] = value
    before = copy.deepcopy(model)
    result = validate_model(model)
    assert not result["valid"]
    assert not result["all_selections_resolved"]
    assert result["resolutions"] == {}
    assert model == before


def test_cyclic_python_objects_are_rejected_without_recursion():
    model = package()
    model["selections"].append({"id": "s", "version": "v1", "selector": model})
    assert not validate_model(model)["valid"]


def test_unknown_fields_rejected_at_every_record_level():
    model = reading_package()
    for record in [model, *model["agents"], *model["readings"], *model["readings"][0]["nodes"]]:
        record["unexpected"] = True
        assert "E_SHAPE" in codes(validate_model(model))
        del record["unexpected"]


@pytest.mark.parametrize("selector,expected", [
    ({"kind": "point", "offset": True}, "E_SELECTOR"),
    ({"kind": "point", "offset": 1.0}, "E_SELECTOR"),
    ({"kind": "point", "offset": -1}, "E_BOUNDS"),
    ({"kind": "point", "offset": 17}, "E_BOUNDS"),
    ({"kind": "point", "offset": 0, "extra": 1}, "E_SELECTOR"),
    ({"kind": []}, "E_SELECTOR"),
    ({"kind": "quote", "exact": "alpha", "match": []}, "E_SELECTOR"),
    ({"kind": "quote", "exact": "", "match": "one"}, "E_QUOTE"),
    ({"kind": "quote", "exact": "alpha", "match": "all", "prefix": "\ud800"}, "E_QUOTE"),
    ({"kind": "ranges", "segments": []}, "E_SELECTOR"),
    ({"kind": "ranges", "segments": [{"start": False, "end": 1, "quote": "a"}]}, "E_SELECTOR"),
    ({"kind": "ranges", "segments": [{"start": 0, "end": 1, "quote": "x"}]}, "E_QUOTE"),
    ({"kind": "ranges", "segments": [{"start": 1, "end": 1, "quote": "a"}]}, "E_BOUNDS"),
])
def test_selector_rejections(selector, expected):
    model = package()
    model["selections"] = [{"id": "s", "version": "v1", "selector": selector}]
    result = validate_model(model)
    assert codes(result) == {expected}
    assert result["resolutions"] == {}


def test_utf8_hash_codepoint_coordinates_and_literal_normalization():
    content = "😀e\u0301\r\nÉ"
    model = package(content)
    model["selections"] = [selection("emoji", 0, 1, content), selection("decomposed", 1, 3, content),
                           {"id": "precomposed", "version": "v1", "selector": {
                               "kind": "quote", "exact": "é", "match": "all"}}]
    result = validate_model(model)
    assert result["valid"]
    assert codes(result) == {"W_ABSENT"}
    assert result["resolutions"]["emoji"]["targets"][0]["segments"] == [{"start": 0, "end": 1}]
    model["versions"][0]["sha256"] = "0" * 64
    assert codes(validate_model(model)) == {"E_HASH"}


def test_empty_version_allows_only_zero_point():
    model = package("")
    model["selections"] = [{"id": "s", "version": "v1", "selector": {"kind": "point", "offset": 0}}]
    assert validate_model(model)["valid"]
    model["selections"][0]["selector"]["offset"] = 1
    assert codes(validate_model(model)) == {"E_BOUNDS"}


def test_unresolved_annotations_are_valid_and_plural_overlap_is_intentional():
    model = package("aaaa")
    model["selections"] = [{"id": mode, "version": "v1", "selector": {
        "kind": "quote", "exact": "aa", "match": mode}} for mode in ("one", "all")]
    model["annotations"] = [{"id": "annotation", "agent": "a", "selection": "one", "body": "Open question"}]
    result = validate_model(model)
    assert result["valid"] and not result["all_selections_resolved"]
    assert codes(result) == {"W_AMBIGUOUS"}
    ambiguous, plural = result["resolutions"]["one"], result["resolutions"]["all"]
    assert ambiguous["targets"] == [] and len(ambiguous["candidates"]) == 3
    assert ambiguous["candidates"] == plural["targets"]
    assert plural["candidates"] == []


def test_literal_adjacent_quote_context():
    model = package()
    model["selections"] = [{"id": "s", "version": "v1", "selector": {
        "kind": "quote", "exact": "alpha", "match": "one", "prefix": "beta ", "suffix": ""}}]
    result = validate_model(model)["resolutions"]["s"]
    assert result["status"] == "resolved"
    assert result["targets"][0]["segments"] == [{"start": 11, "end": 16}]


def test_discontinuity_is_one_region_and_adjacent_segmentation_is_preserved():
    model = reading_package()
    model["selections"][0]["selector"]["segments"] = [
        {"start": 0, "end": 5, "quote": "alpha"}, {"start": 5, "end": 16, "quote": " beta alpha"}]
    result = validate_model(model)
    assert result["valid"]
    assert len(result["resolutions"]["whole"]["targets"][0]["segments"]) == 2
    model["selections"][0]["selector"]["segments"][1].update(start=6, quote="beta alpha")
    assert "E_READING_TARGET" in codes(validate_model(model))
    model["readings"] = []
    assert len(validate_model(model)["resolutions"]["whole"]["targets"]) == 1


@pytest.mark.parametrize("parts", [
    [{"start": 0, "end": 5, "quote": "alpha"}, {"start": 0, "end": 5, "quote": "alpha"}],
    [{"start": 11, "end": 16, "quote": "alpha"}, {"start": 0, "end": 5, "quote": "alpha"}],
])
def test_valid_individual_bounds_but_overlapping_or_descending_segments_are_selector_errors(parts):
    model = package()
    model["selections"] = [{"id": "s", "version": "v1", "selector": {"kind": "ranges", "segments": parts}}]
    assert codes(validate_model(model)) == {"E_SELECTOR"}


def test_duplicate_identity_including_nodes_is_globally_rejected():
    model = reading_package()
    model["readings"][0]["nodes"][0]["id"] = "a"
    assert "E_DUPLICATE_ID" in codes(validate_model(model))


def test_category_reference_and_type_role_checks():
    model = reading_package()
    model["annotations"] = [{"id": "ann", "agent": "v1", "selection": "whole", "body": "Claim"}]
    assert "E_REFERENCE" in codes(validate_model(model))
    model["annotations"] = []
    model["concepts"][0]["applies_to"] = "relation"
    assert codes(validate_model(model)) == {"E_TYPE"}


def test_relation_cycles_and_self_reference_are_allowed():
    model = package()
    model["concepts"] = [{"id": "link", "label": "Link", "definition": "Arbitrary relation", "applies_to": "relation"}]
    model["relations"] = [{"id": "rel1", "type": "link", "source": "rel1", "target": "rel2", "agent": "a"},
                          {"id": "rel2", "type": "link", "source": "rel2", "target": "rel1", "agent": "a"}]
    assert validate_model(model)["valid"]


def test_continuity_not_inferred_from_version_parentage():
    model = package()
    model["continuities"] = []
    assert codes(validate_model(model)) == {"E_CONTINUITY"}
    model["texts"] = []
    assert validate_model(model)["valid"]


def test_version_cycle_is_rejected_but_long_acyclic_history_works():
    model = package()
    model["versions"] = [version(f"v{i}", "", [] if i == 0 else [f"v{i - 1}"]) for i in range(1500)]
    assert validate_model(model)["valid"]
    model["versions"][0]["parents"] = ["v1499"]
    assert codes(validate_model(model)) == {"E_VERSION_CYCLE"}


@pytest.mark.parametrize("change,expected", [
    ("cycle", "E_READING_CYCLE"), ("missing-parent", "E_READING_PARENT"),
    ("containment", "E_CONTAINMENT"), ("sibling-overlap", "E_SIBLING_OVERLAP"),
    ("root-overlap", "E_SIBLING_OVERLAP"), ("empty-nodes", "E_SHAPE"),
])
def test_reading_forest_constraints(change, expected):
    model = reading_package()
    nodes = model["readings"][0]["nodes"]
    if change == "cycle":
        nodes[0]["parent"] = "n1"
    elif change == "missing-parent":
        nodes[0]["parent"] = "a"
    elif change == "containment":
        nodes[0]["selection"] = "first"
    elif change == "sibling-overlap":
        nodes[2]["selection"] = "first"
    elif change == "root-overlap":
        nodes[1]["parent"] = None
    else:
        model["readings"][0]["nodes"] = []
    assert expected in codes(validate_model(model))


def test_unresolved_reading_suppresses_every_resolution_but_retains_warning():
    model = reading_package()
    model["selections"][0]["selector"] = {"kind": "quote", "exact": "missing", "match": "one"}
    result = validate_model(model)
    assert codes(result) == {"W_ABSENT", "E_READING_TARGET"}
    assert result["resolutions"] == {} and not result["all_selections_resolved"]


def test_canonical_order_equivalence_and_nonmutation():
    model = reading_package()
    model["versions"].extend([version("v2", "", ["v1"]), version("v3", "", ["v1", "v2"])])
    model["continuities"][0]["versions"] = ["v1", "v2", "v3"]
    reordered = copy.deepcopy(model)
    for collection in COLLECTIONS:
        reordered[collection].reverse()
    reordered["readings"][0]["nodes"].reverse()
    reordered["versions"][0]["parents"].reverse()
    reordered["continuities"][0]["versions"].reverse()
    before = copy.deepcopy(reordered)
    assert equivalent(model, reordered)
    assert json.loads(canonical_bytes(model)) == json.loads(canonical_bytes(reordered))
    assert reordered == before
    reordered["agents"][0]["label"] = "Another editor"
    assert not equivalent(model, reordered)
    with pytest.raises(ValueError):
        equivalent(model, None)


def test_segmentation_and_selector_mode_affect_canonical_identity():
    left = package()
    left["selections"] = [selection("s", 0, 16)]
    right = copy.deepcopy(left)
    right["selections"][0]["selector"]["segments"] = [
        {"start": 0, "end": 5, "quote": "alpha"}, {"start": 5, "end": 16, "quote": " beta alpha"}]
    assert not equivalent(left, right)
    right["selections"][0]["selector"] = {"kind": "quote", "exact": "alpha beta alpha", "match": "one"}
    assert not equivalent(left, right)


def test_revision_detects_content_and_parent_rewrites_but_allows_removal():
    before = package()
    after = copy.deepcopy(before)
    after["versions"][0] = version(content="changed")
    assert codes(check_revision(before, after)) == {"E_VERSION_REWRITE"}
    before["versions"].append(version("v2", "", ["v1"]))
    after = copy.deepcopy(before)
    after["versions"][1]["parents"] = []
    assert codes(check_revision(before, after)) == {"E_VERSION_REWRITE"}
    after["versions"].pop()
    assert check_revision(before, after)["valid"]
    assert not check_revision(before, None)["valid"]


def reanchor_package(target="before alpha after"):
    model = package()
    model["versions"].append(version("v2", target, ["v1"]))
    model["continuities"][0]["versions"].append("v2")
    model["selections"] = [selection("s", 0, 5)]
    return model


@pytest.mark.parametrize("target,status,warning", [
    ("before alpha after", "resolved", None), ("alpha alpha", "ambiguous", "W_AMBIGUOUS"),
    ("deleted", "absent", "W_ABSENT"),
])
def test_reanchor_proposes_without_accepting_or_mutating(target, status, warning):
    model = reanchor_package(target)
    before = copy.deepcopy(model)
    result = propose_reanchor(model, "s", "v2", "c")
    assert codes(result) == ({warning} if warning else set())
    assert result["proposal"]["accepted"] is False
    assert result["proposal"]["resolution"]["status"] == status
    assert model == before
    result["proposal"]["resolution"]["targets"].append({"external": True})
    assert model == before


def test_reanchor_requires_explicit_grouping_and_resolved_source():
    model = reanchor_package()
    model["continuities"][0]["versions"].remove("v2")
    assert codes(propose_reanchor(model, "s", "v2", "c")) == {"E_REANCHOR"}
    model["continuities"][0]["versions"].append("v2")
    model["selections"][0]["selector"] = {"kind": "quote", "exact": "alpha", "match": "one"}
    assert codes(propose_reanchor(model, "s", "v2", "c")) == {"E_REANCHOR"}
    assert codes(propose_reanchor(model, {}, [], None)) == {"E_REANCHOR"}


def test_reanchor_does_not_carry_unrelated_warnings_and_preserves_quote_context():
    model = reanchor_package("beta alpha alpha")
    model["selections"] = [
        {"id": "s", "version": "v1", "selector": {"kind": "quote", "exact": "alpha", "match": "one", "prefix": "beta "}},
        {"id": "unrelated", "version": "v1", "selector": {"kind": "quote", "exact": "absent", "match": "one"}},
    ]
    result = propose_reanchor(model, "s", "v2", "c")
    assert result["diagnostics"] == []
    assert result["proposal"]["resolution"]["targets"][0]["segments"] == [{"start": 5, "end": 10}]


def test_reanchor_invalid_package_preserves_complete_validation_diagnostics():
    model = reading_package()
    model["selections"][0]["selector"] = {"kind": "quote", "exact": "missing", "match": "one"}
    result = propose_reanchor(model, "first", "v1", "c")
    assert result["proposal"] is None
    assert result["diagnostics"] == validate_model(model)["diagnostics"]
    assert codes(result) == {"E_READING_TARGET", "W_ABSENT"}


@pytest.mark.parametrize("selector", [
    {"kind": "point", "offset": 0},
    {"kind": "ranges", "segments": [{"start": 0, "end": 1, "quote": "a"}, {"start": 1, "end": 5, "quote": "lpha"}]},
])
def test_reanchor_point_and_multisegment_are_explicitly_unsupported(selector):
    model = reanchor_package()
    model["selections"][0]["selector"] = selector
    result = propose_reanchor(model, "s", "v2", "c")
    assert codes(result) == {"E_REANCHOR_UNSUPPORTED"} and result["proposal"] is None
