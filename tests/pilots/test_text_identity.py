"""Adversarial checks for the bounded hypothesis, not universal TEI claims."""

import json
from copy import deepcopy
from pathlib import Path

import pytest

import tools.pilots.text_identity as pilot
from tools.pilots.text_identity import (
    INPUTS,
    ROOT,
    build_report,
    evaluate_case,
    propose_reanchor,
    quote_candidates,
    report_bytes,
    text_hash,
    validate_model,
)


def base_model():
    return {
        "texts": [{"id": "t"}],
        "versions": [{"id": "v", "text": "t", "content": "red red", "sha256": text_hash("red red")}],
        "regions": [{"id": "r", "version": "v", "selector": {"kind": "A", "start": 0, "end": 3, "quote": "red"}}],
        "annotations": [{"id": "a", "region": "r", "body": "Synthetic interpretation"}],
    }


def codes(result):
    return {row["code"] for row in result["diagnostics"]}


def test_declared_counterexamples_and_resolutions():
    report = build_report()
    assert report["summary"]["cases"] >= 30
    assert all(case["passed"] for case in report["cases"]), report["cases"]
    required = {"insertion-stale-position", "insertion-quotation", "repeated-quotation", "repeated-position", "normalization-quotation", "normalization-position", "reanchor-deletion", "version-parent-cycle"}
    assert required <= {case["id"] for case in report["cases"]}


@pytest.mark.parametrize("bad", [None, [], "v", True, 4])
def test_malformed_model_is_diagnostic(bad):
    assert codes(validate_model(bad)) == {"E_SHAPE"}


@pytest.mark.parametrize("bad", [None, [], {}, False, 1, "missing"])
def test_malformed_references_are_not_python_exceptions(bad):
    for collection, field in (("versions", "text"), ("regions", "version"), ("annotations", "region")):
        model = base_model()
        model[collection][0][field] = bad
        assert "E_REFERENCE" in codes(validate_model(model))


@pytest.mark.parametrize("bad", [None, [], {}, "0", 0.0, True, False, -1, 8])
def test_bounds_are_actual_integers_and_in_range(bad):
    model = base_model()
    model["regions"][0]["selector"]["start"] = bad
    assert codes(validate_model(model)) == {"E_BOUNDS"}


@pytest.mark.parametrize("selector", [None, [], "A", {}, {"kind": [], "quote": "red"}, {"kind": "B", "quote": "red", "prefix": False}, {"kind": "B", "quote": "red", "start": 0}])
def test_malformed_selectors_fail_closed(selector):
    model = base_model()
    model["regions"][0]["selector"] = selector
    assert codes(validate_model(model)) == {"E_SELECTOR"}


def test_overlapping_occurrences_and_immediate_context():
    assert quote_candidates("banana", "ana") == [{"start": 1, "end": 4}, {"start": 3, "end": 6}]
    assert quote_candidates("L red R red", "red", "L ", " R") == [{"start": 2, "end": 5}]
    assert quote_candidates("L red", "red", "L") == []
    assert quote_candidates("Red", "red") == []


def test_long_ancestry_and_cycle_do_not_depend_on_recursion_limit():
    model = base_model()
    previous = "v"
    for index in range(1500):
        identifier = f"v{index}"
        model["versions"].append({"id": identifier, "text": "t", "content": "", "sha256": text_hash(""), "parent": previous})
        previous = identifier
    assert not validate_model(model)["diagnostics"]
    model["versions"][0]["parent"] = previous
    assert codes(validate_model(model)) == {"E_CYCLE"}


def test_lone_surrogate_content_and_quote_are_diagnostic():
    model = base_model()
    model["versions"][0]["content"] = "\ud800"
    assert codes(validate_model(model)) == {"E_SHAPE"}
    model = base_model()
    model["regions"][0]["selector"]["quote"] = "\ud800"
    assert codes(validate_model(model)) == {"E_SELECTOR"}
    model = base_model()
    model["texts"][0]["id"] = "\ud800"
    assert codes(validate_model(model)) == {"E_ID"}


def test_unknown_fields_and_wrong_reference_category_are_diagnostic():
    model = base_model()
    model["regions"][0]["version"] = "t"
    assert codes(validate_model(model)) == {"E_REFERENCE"}
    model = base_model()
    model["versions"][0]["mutable"] = True
    assert codes(validate_model(model)) == {"E_SHAPE"}


def test_reanchor_is_a_nonmutating_proposal_and_retains_all_candidates():
    model = base_model()
    model["versions"].append({"id": "v2", "text": "t", "parent": "v", "content": "red red red", "sha256": text_hash("red red red")})
    request = {"region": "r", "target_version": "v2"}
    original, original_request = deepcopy(model), deepcopy(request)
    result = propose_reanchor(model, request)
    assert result["proposal"]["candidates"] == [{"start": 0, "end": 3}, {"start": 4, "end": 7}, {"start": 8, "end": 11}]
    assert result["proposal"]["status"] == "ambiguous"
    assert result["proposal"]["accepted"] is False
    assert model == original and request == original_request
    result["proposal"]["candidates"][0]["start"] = 99
    assert model == original


@pytest.mark.parametrize("proposal_request", [None, [], {}, {"region": [], "target_version": "v"}, {"region": "r", "target_version": "missing"}])
def test_invalid_reanchor_requests(proposal_request):
    assert propose_reanchor(base_model(), proposal_request) == {"diagnostics": ["E_REANCHOR"], "proposal": None}


def test_declared_expectation_change_fails_case():
    case = json.loads((ROOT / "experiments/text_identity/cases.json").read_text(encoding="utf-8"))["cases"][0]
    assert evaluate_case(case)["passed"]
    case["expected"]["resolutions"]["r1"]["start"] = 99
    assert not evaluate_case(case)["passed"]


def test_expected_boolean_cannot_replace_integer_position():
    suite = json.loads((ROOT / "experiments/text_identity/cases.json").read_text(encoding="utf-8"))
    case = next(case for case in suite["cases"] if case["id"] == "unicode-codepoints")
    assert evaluate_case(case)["passed"]
    assert case["expected"]["resolutions"]["r1"]["start"] == 1
    case["expected"]["resolutions"]["r1"]["start"] = True
    assert not evaluate_case(case)["passed"]


def test_expected_zero_cannot_replace_boolean_acceptance():
    suite = json.loads((ROOT / "experiments/text_identity/cases.json").read_text(encoding="utf-8"))
    case = next(case for case in suite["cases"] if case["id"] == "reanchor-insertion")
    assert evaluate_case(case)["passed"]
    assert case["expected"]["reanchor"]["proposal"]["accepted"] is False
    case["expected"]["reanchor"]["proposal"]["accepted"] = 0
    assert not evaluate_case(case)["passed"]


def test_report_reproduction_and_input_fingerprint_change(tmp_path: Path):
    for name in INPUTS:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / name).read_bytes())
    first = build_report(tmp_path)
    assert report_bytes(first) == report_bytes(build_report(tmp_path))
    contract = tmp_path / INPUTS[0]
    contract.write_bytes(contract.read_bytes() + b"\n")
    changed = build_report(tmp_path)
    assert first["inputs"][INPUTS[0]] != changed["inputs"][INPUTS[0]]
    assert first["cases"] == changed["cases"]


def test_case_suite_identity_is_validated(tmp_path: Path):
    for name in INPUTS:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / name).read_bytes())
    path = tmp_path / "experiments/text_identity/cases.json"
    suite = json.loads(path.read_text(encoding="utf-8"))
    suite["cases"].append(suite["cases"][0])
    path.write_text(json.dumps(suite), encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate case identity"):
        build_report(tmp_path)


def test_cli_generation_drift_and_failing_expectations(tmp_path: Path, monkeypatch):
    for name in INPUTS:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / name).read_bytes())
    monkeypatch.setattr(pilot, "ROOT", tmp_path)
    monkeypatch.setattr(pilot, "build_report", lambda: build_report(tmp_path))
    monkeypatch.setattr("sys.argv", ["text_identity"])
    assert pilot.main() == 0
    report_path = tmp_path / pilot.REPORT
    original = report_path.read_bytes()
    monkeypatch.setattr("sys.argv", ["text_identity", "--check"])
    assert pilot.main() == 0
    report_path.write_bytes(original + b"\n")
    assert pilot.main() == 1
    assert report_path.read_bytes() == original + b"\n"
    report_path.write_bytes(original)
    case_path = tmp_path / "experiments/text_identity/cases.json"
    cases = json.loads(case_path.read_text(encoding="utf-8"))
    cases["cases"][0]["expected"]["resolutions"]["r1"]["start"] = 99
    case_path.write_text(json.dumps(cases), encoding="utf-8")
    monkeypatch.setattr("sys.argv", ["text_identity"])
    assert pilot.main() == 1
    assert report_path.read_bytes() == original
    case_path.write_text("{invalid JSON", encoding="utf-8")
    assert pilot.main() == 1
