"""Unit checks for the optional, attributed editorial provenance profile."""

import copy
import hashlib
import json
from pathlib import Path

import pytest

from tools.models.abstract_text import (
    COLLECTIONS, check_revision, propose_reanchor, validate_model,
)
from tools.models.editorial_profile import (
    BASE_MODEL_VERSION, DERIVED_FROM, PROFILE_VERSION, RESERVED_CONCEPTS,
    SUPERSEDES, check_profile_revision, current_derivations, validate_profile,
)


def version(identifier, content="alpha", parents=None):
    return {"id": identifier, "content": content,
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "parents": [] if parents is None else parents}


def claim(identifier, target="v1", subject="v3", agent="a"):
    return {"id": identifier, "type": DERIVED_FROM, "source": subject,
            "target": target, "agent": agent}


def supersedes(identifier, source, target, agent="a"):
    return {"id": identifier, "type": SUPERSEDES, "source": source,
            "target": target, "agent": agent}


def package():
    model = {kind: [] for kind in COLLECTIONS}
    model.update(model_version="0.1", agents=[{"id": "a", "label": "Editor A"},
                                             {"id": "b", "label": "Editor B"}],
                 concepts=copy.deepcopy(list(RESERVED_CONCEPTS)),
                 versions=[version("v1"), version("v2", "beta"),
                           version("v3", parents=["v1"])],
                 selections=[{"id": "s", "version": "v3", "selector": {
                     "kind": "ranges", "segments": [{"start": 0, "end": 5, "quote": "alpha"}]}}],
                 relations=[claim("old")])
    return model


def correction():
    model = package()
    model["relations"].extend([claim("new", "v2"), supersedes("revision", "new", "old")])
    return model


def codes(result):
    return {item["code"] for item in result["diagnostics"]}


def test_constants_match_frozen_contract():
    path = Path(__file__).resolve().parents[2] / "experiments/editorial_cases/profile.json"
    contract = json.loads(path.read_text(encoding="utf-8"))
    assert list(RESERVED_CONCEPTS) == contract["concepts"]
    assert PROFILE_VERSION == contract["profile_version"]
    assert BASE_MODEL_VERSION == contract["base_model_version"]


def test_optional_profile_does_not_change_core_acceptance_or_resolution():
    model = package()
    expected = validate_model(model)
    assert validate_profile(model) == {"valid": True, "diagnostics": []}
    assert validate_model(model) == expected
    model["concepts"] = []
    model["relations"] = []
    assert validate_model(model)["valid"]
    assert codes(validate_profile(model)) == {"E_PROFILE_CONCEPT"}


@pytest.mark.parametrize("field,value", [
    ("label", "Other label"), ("definition", "Another meaning"), ("applies_to", "node"),
])
def test_exact_reserved_concept_records_required(field, value):
    model = package()
    model["relations"] = []
    model["concepts"][0][field] = value
    assert codes(validate_profile(model)) == {"E_PROFILE_CONCEPT"}


def test_unrelated_concepts_and_relations_keep_base_semantics():
    model = package()
    model["concepts"].append({"id": "link", "label": "Link", "definition": "Arbitrary relation",
                              "applies_to": "relation"})
    model["relations"].append({"id": "other", "type": "link", "source": "other",
                               "target": "s", "agent": "a"})
    assert validate_profile(model)["valid"]
    assert [item["id"] for item in current_derivations(model)] == ["old"]


@pytest.mark.parametrize("endpoint,target", [("source", "a"), ("target", "s"), ("target", "old")])
def test_derivation_endpoints_must_be_versions(endpoint, target):
    model = package()
    model["relations"][0][endpoint] = target
    assert validate_model(model)["valid"]
    assert codes(validate_profile(model)) == {"E_PROFILE_ENDPOINT"}


def test_hypothesis_cycles_and_contradictions_do_not_establish_truth():
    model = package()
    model["relations"].extend([claim("reverse", "v3", "v1"), claim("self", "v3"),
                                claim("contradiction", "v2", agent="b")])
    assert validate_profile(model)["valid"]
    assert len(current_derivations(model)) == 4


@pytest.mark.parametrize("change", ["version-endpoint", "edge-endpoint", "claim-agent", "edge-agent", "subject"])
def test_supersession_requires_derivations_same_agent_and_subject(change):
    model = correction()
    if change == "version-endpoint":
        model["relations"][2]["source"] = "v3"
    elif change == "edge-endpoint":
        model["relations"][2]["target"] = "revision"
    elif change == "claim-agent":
        model["relations"][1]["agent"] = "b"
    elif change == "edge-agent":
        model["relations"][2]["agent"] = "b"
    else:
        model["relations"][1]["source"] = "v2"
    assert validate_model(model)["valid"]
    assert codes(validate_profile(model)) == {"E_PROFILE_SUPERSESSION"}


def test_supersession_self_edge_and_cycle_rejected():
    model = correction()
    model["relations"].append(supersedes("back", "old", "new"))
    assert codes(validate_profile(model)) == {"E_PROFILE_CYCLE"}
    model = package()
    model["relations"].append(supersedes("self", "old", "old"))
    assert codes(validate_profile(model)) == {"E_PROFILE_SUPERSESSION", "E_PROFILE_CYCLE"}


def test_forks_concurrent_agents_and_subject_filters_keep_all_survivors():
    model = correction()
    model["relations"].extend([
        claim("alternative", "v1"), supersedes("fork", "alternative", "old"),
        claim("other-agent", "v2", agent="b"), claim("other-subject", "v1", "v2"),
    ])
    assert [item["id"] for item in current_derivations(model)] == [
        "alternative", "new", "other-agent", "other-subject"]
    assert [item["id"] for item in current_derivations(model, agent="a", subject="v3")] == [
        "alternative", "new"]
    assert [item["id"] for item in current_derivations(model, agent="b")] == ["other-agent"]
    assert [item["id"] for item in current_derivations(model, subject="v2")] == ["other-subject"]
    assert current_derivations(model, subject="v1") == []
    model["relations"].reverse()
    assert [item["id"] for item in current_derivations(model, agent="a", subject="v3")] == [
        "alternative", "new"]


def test_long_supersession_history_does_not_recurse():
    model = package()
    model["relations"] = [claim(f"claim-{i}") for i in range(1500)]
    model["relations"].extend(supersedes(f"edge-{i}", f"claim-{i}", f"claim-{i - 1}")
                                for i in range(1, 1500))
    assert validate_profile(model)["valid"]
    assert [item["id"] for item in current_derivations(model)] == ["claim-1499"]


@pytest.mark.parametrize("name,value", [
    ("agent", "missing"), ("agent", "v3"), ("agent", []), ("agent", {}), ("agent", True),
    ("agent", 1), ("agent", ""), ("subject", "missing"), ("subject", "a"),
    ("subject", []), ("subject", {}), ("subject", 1.0), ("subject", "s"),
])
def test_unknown_and_wrong_type_filters_reject_with_value_error(name, value):
    with pytest.raises(ValueError):
        current_derivations(package(), **{name: value})


def test_correction_preserves_version_selection_and_technical_parentage():
    before, after = package(), correction()
    assert check_profile_revision(before, after) == {"valid": True, "diagnostics": []}
    assert after["versions"] == before["versions"]
    assert after["selections"] == before["selections"]
    assert validate_model(after)["resolutions"] == validate_model(before)["resolutions"]
    assert [item["id"] for item in current_derivations(after)] == ["new"]
    assert codes(propose_reanchor(after, "s", "v2", "missing")) == {"E_REANCHOR"}
    after["versions"][2]["parents"] = ["v2"]
    assert codes(check_profile_revision(before, after)) == {"E_VERSION_REWRITE"}


def test_content_rewrite_still_rejected_with_correct_hash():
    before, after = package(), package()
    after["versions"][0] = version("v1", "changed")
    assert codes(check_profile_revision(before, after)) == {"E_VERSION_REWRITE"}


@pytest.mark.parametrize("change", ["claim-target", "claim-agent", "claim-delete", "edge-delete", "edge-reverse", "change-type"])
def test_revision_protects_exact_records_of_all_old_reserved_relations(change):
    before = correction()
    after = copy.deepcopy(before)
    if change == "claim-target":
        after["relations"][0]["target"] = "v2"
    elif change == "claim-agent":
        after["relations"][0]["agent"] = "b"
    elif change == "claim-delete":
        after["relations"].pop(0)
    elif change == "edge-delete":
        after["relations"].pop()
    elif change == "edge-reverse":
        after["relations"][2].update(source="old", target="new")
    else:
        after["concepts"].append({"id": "link", "label": "Link", "definition": "Other relation",
                                  "applies_to": "relation"})
        after["relations"][0]["type"] = "link"
    assert "E_CLAIM_REWRITE" in codes(check_profile_revision(before, after))


def test_base_revision_alone_permits_profile_history_removal():
    before, after = correction(), correction()
    after["relations"] = []
    assert check_revision(before, after)["valid"]
    assert codes(check_profile_revision(before, after)) == {"E_CLAIM_REWRITE"}


def test_revision_validates_both_profiles_and_prefixes_diagnostics():
    before, after = package(), package()
    before["concepts"][0]["definition"] = "Changed definition"
    after["concepts"][1]["label"] = "Changed label"
    assert check_profile_revision(before, after) == {"valid": False, "diagnostics": [
        {"code": "E_PROFILE_CONCEPT", "path": "/after/concepts/1"},
        {"code": "E_PROFILE_CONCEPT", "path": "/before/concepts/0"},
    ]}


def test_relation_reordering_and_unrelated_changes_are_permitted():
    before, after = correction(), correction()
    after["relations"].reverse()
    after["agents"][0]["label"] = "Updated display label"
    assert check_profile_revision(before, after)["valid"]


def test_base_warning_retained_without_invalidating_profile():
    model = package()
    model["selections"][0]["selector"] = {"kind": "quote", "exact": "absent", "match": "one"}
    assert validate_profile(model) == {"valid": True, "diagnostics": [
        {"code": "W_ABSENT", "path": "/selections/0/selector"}]}
    assert current_derivations(model) == [claim("old")]
    assert len(check_profile_revision(model, model)["diagnostics"]) == 2


@pytest.mark.parametrize("malformed", [None, [], True, 1, "package", {"model_version": "0.1"}])
def test_malformed_packages_do_not_raise_except_current_view(malformed):
    assert not validate_profile(malformed)["valid"]
    assert not check_profile_revision(package(), malformed)["valid"]
    assert not check_profile_revision(malformed, package())["valid"]
    with pytest.raises(ValueError):
        current_derivations(malformed)


@pytest.mark.parametrize("path,value", [
    (("relations",), {}), (("relations", 0), []), (("relations", 0, "type"), []),
    (("relations", 0, "source"), {}), (("relations", 0, "agent"), True),
    (("concepts", 0, "id"), {}), (("versions", 0, "parents"), [False]),
])
def test_malformed_fields_are_nonmutating_and_diagnostic(path, value):
    model = package()
    target = model
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value
    snapshot = copy.deepcopy(model)
    assert not validate_profile(model)["valid"]
    assert not check_profile_revision(package(), model)["valid"]
    with pytest.raises(ValueError):
        current_derivations(model)
    assert model == snapshot


def test_all_operations_nonmutating_and_current_records_deep_copied():
    before, after = package(), correction()
    snapshots = copy.deepcopy((before, after))
    assert validate_profile(after)["valid"]
    assert check_profile_revision(before, after)["valid"]
    result = current_derivations(after)
    result[0]["target"] = "external-change"
    result.append(claim("external"))
    assert (before, after) == snapshots
    assert current_derivations(after) == [claim("new", "v2")]
