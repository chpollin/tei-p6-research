"""The 0.2 experiment gate must reject bad expectations, stale inputs, mutation and a missing suite."""

import copy
import hashlib
import json
import shutil

import pytest

from tools import check_entities_v02 as check
from tools.models import entities as model
from tools.models.abstract_text import COLLECTIONS

CONTENT = "Ada Lovelace"
INSTANT = "2026-09-06T10:00:00Z"


@pytest.fixture
def experiment(tmp_path):
    for relative in ("experiments/entities_v02", "tools/models"):
        shutil.copytree(check.ROOT / relative, tmp_path / relative)
    for relative in ("tools/check_entities_v02.py", "knowledge/text-model.md"):
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(check.ROOT / relative, target)
    return tmp_path


def claim(identifier, **fields):
    return {"id": identifier, "agent": "ag", "created": INSTANT, "status": "asserted", **fields}


def package():
    """One mention, one entity and one denotation, enough for both reference operations."""
    result = {kind: [] for kind in (*COLLECTIONS, *model.NEW_COLLECTIONS)}
    result["model_version"] = model.MODEL_VERSION
    result["agents"] = [{"id": "ag", "label": "Editor"}]
    result["concepts"] = [dict(model.MENTION_CONCEPTS[0])]
    result["versions"] = [{"id": "v1", "content": CONTENT, "parents": [],
                           "sha256": hashlib.sha256(CONTENT.encode("utf-8")).hexdigest()}]
    result["selections"] = [{"id": "sel", "version": "v1", "selector": {"kind": "ranges", "segments": [
        {"start": 0, "end": 3, "quote": "Ada"}]}}]
    result["readings"] = [{"id": "rd", "version": "v1", "agent": "ag", "label": "Mentions", "nodes": [
        {"id": "nd", "type": "en-proper-noun", "selection": "sel", "parent": None}]}]
    result["entities"] = [{"id": "ent", "label": "Ada Lovelace", "kind": "person"}]
    result["names"] = [claim("nm", entity="ent", form="Ada Lovelace", language="en")]
    result["denotations"] = [claim("dn", mention="nd", entity="ent")]
    return result


def suite(cases):
    return {"format_version": 1, "model_version": "0.2",
            "authority": "Synthetic suite of the unit tests; no independent authorship.", "cases": cases}


def synthetic_cases():
    return [
        {"id": "valid", "description": "A minimal denoted mention.", "package": package(),
         "expect": {"valid": True, "diagnostics": []},
         "operations": [
             {"name": "denotations_of", "arguments": {"mention_id": "nd"},
              "expect": {"diagnostics": [], "denotations": [
                  claim("dn", mention="nd", entity="ent") | {"label": "Ada Lovelace", "kind": "person"}]}},
             {"name": "names_of", "arguments": {"entity_id": "ent", "include_withdrawn": False},
              "expect": {"diagnostics": [], "names": [claim("nm", entity="ent", form="Ada Lovelace",
                                                            language="en")]}}]},
        {"id": "invalid", "description": "An entity kind outside the closed set.",
         "package": {**package(), "entities": [{"id": "ent", "label": "Ada", "kind": "city"}]},
         "expect": {"valid": False, "diagnostics": [{"code": "E_ENTITY_KIND", "path": "/entities/0/kind"}]}},
    ]


def store(root, cases):
    (root / check.CASES).write_bytes(check.json_bytes(suite(cases)))


def test_independent_suite_passes_and_reproduces():
    report = check.build_report()
    assert report["summary"]["passed"]
    assert report["summary"]["cases_present"]
    assert report["summary"]["case_passes"] == report["summary"]["cases"] > 0
    assert report["summary"]["operations_covered"] == sorted(check.OPERATIONS)
    assert all(case["nonmutating"] for case in report["cases"])
    assert check.json_bytes(report) == check.json_bytes(check.build_report())


def test_every_standalone_example_is_a_valid_package():
    report = check.build_report()
    assert 0 < len(report["examples"]) <= 2
    assert all(item["passed"] and item["diagnostics"] == [] for item in report["examples"])
    assert all(item["passed"] for item in report["canonical_checks"])


def test_every_valid_case_and_example_reaches_the_rdf_export():
    report = check.build_report()
    valid = [case for case in report["cases"] if case["expected"]["valid"]]
    assert report["summary"]["rdf_checks"] == len(valid) + len(report["examples"])
    assert report["summary"]["rdf_checks"] == report["summary"]["canonical_checks"]
    assert all(item["passed"] and len(item["sha256"]) == 64 for item in report["rdf_checks"])
    # A case package without a base is exported under the runner's test base.
    exported = {item["package"] for item in report["rdf_checks"]}
    assert {case["id"] for case in valid} <= exported


def test_a_tampered_turtle_example_fails_the_run(experiment):
    store(experiment, synthetic_cases())
    path = sorted((experiment / check.BASE / "examples").glob("*.ttl"))[0]
    path.write_text(path.read_text(encoding="utf-8") + '\n<urn:x:s> <urn:x:p> "o" .\n',
                    encoding="utf-8")
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    failed = [item for item in report["rdf_checks"] if not item["passed"]]
    assert [item["package"] for item in failed] == [path.with_suffix(".json").name]
    assert all(case["passed"] for case in report["cases"])


def test_spec_mirrors_the_module_constants():
    spec = check.read_json(check.ROOT / check.BASE / "spec.json")
    assert tuple(spec["diagnostics"]) == model.DIAGNOSTICS
    assert sorted(spec["extension_diagnostics"]) == sorted(model.EXTENSION_DIAGNOSTICS)
    assert spec["mention_concepts"] == [dict(concept) for concept in model.MENTION_CONCEPTS]
    for name, constant in (("entity_kind", model.ENTITY_KINDS), ("statement_kind", model.STATEMENT_KINDS),
                           ("name_part_kind", model.NAME_PART_KINDS),
                           ("alignment_relation", model.ALIGNMENT_RELATIONS),
                           ("claim_status", model.CLAIM_STATUSES), ("certainty", model.CERTAINTIES),
                           ("concept_role", model.CONCEPT_ROLES),
                           ("mention_concept", model.MENTION_CONCEPT_IDS)):
        assert tuple(spec["closed_sets"][name]) == constant


def test_a_missing_case_file_is_reported_without_a_case_row(experiment):
    (experiment / check.CASES).unlink()
    report = check.build_report(experiment)
    assert report["summary"]["passed"] is False
    assert report["summary"]["cases_present"] is False
    assert report["cases"] == [] and report["summary"]["operations_covered"] == []
    assert check.CASES.as_posix() not in report["inputs"]
    assert report["examples"] and all(item["passed"] for item in report["examples"])


def test_missing_case_file_exits_nonzero(experiment, monkeypatch, capsys):
    (experiment / check.CASES).unlink()
    original = check.build_report
    monkeypatch.setattr(check, "ROOT", experiment)
    monkeypatch.setattr(check, "build_report", lambda: original(experiment))
    assert check.main([]) == 1
    assert "No case suite" in capsys.readouterr().err


def test_synthetic_suite_passes_and_records_one_row_per_case(experiment):
    store(experiment, synthetic_cases())
    report = check.build_report(experiment)
    assert report["summary"]["passed"]
    assert [case["id"] for case in report["cases"]] == ["valid", "invalid"]
    assert all(case["codes_match"] for case in report["cases"])


@pytest.mark.parametrize("change", ["duplicate_id", "unknown_code", "missing_field", "bad_valid",
                                    "unknown_operation", "unknown_argument", "bad_envelope"])
def test_case_contract_fails_closed(experiment, change):
    cases = synthetic_cases()
    if change == "duplicate_id":
        cases.append(copy.deepcopy(cases[0]))
    elif change == "unknown_code":
        cases[1]["expect"]["diagnostics"] = [{"code": "E_INVENTED", "path": "/entities/0/kind"}]
    elif change == "missing_field":
        del cases[0]["description"]
    elif change == "bad_valid":
        cases[0]["expect"]["valid"] = 1
    elif change == "unknown_operation":
        cases[0]["operations"][0]["name"] = "entities_of"
    elif change == "unknown_argument":
        cases[0]["operations"][0]["arguments"] = {"mention": "nd"}
    if change == "bad_envelope":
        (experiment / check.CASES).write_bytes(check.json_bytes({"cases": cases}))
    else:
        store(experiment, cases)
    with pytest.raises(ValueError):
        check.build_report(experiment)


@pytest.mark.parametrize("change", ["validity", "path", "operation"])
def test_changed_expectation_fails_instead_of_self_approving(experiment, change):
    cases = synthetic_cases()
    if change == "validity":
        cases[1]["expect"]["valid"] = True
    elif change == "path":
        cases[1]["expect"]["diagnostics"] = [{"code": "E_ENTITY_KIND", "path": "/entities/0"}]
    else:
        cases[0]["operations"][0]["expect"]["denotations"] = []
    store(experiment, cases)
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    failed = [case for case in report["cases"] if not case["passed"]]
    assert len(failed) == 1
    # codes_match separates a disagreement about paths from one about diagnostics.
    assert failed[0]["codes_match"] is True


def test_an_uncovered_operation_fails_the_run(experiment):
    cases = synthetic_cases()
    cases[0]["operations"] = cases[0]["operations"][:1]
    store(experiment, cases)
    report = check.build_report(experiment)
    assert report["summary"]["operations_covered"] == ["denotations_of"]
    assert not report["summary"]["passed"]
    assert all(case["passed"] for case in report["cases"])


def test_a_mutating_validator_fails_every_case(experiment, monkeypatch):
    store(experiment, synthetic_cases())
    original = model.validate_extension

    def mutation(package):
        result = original(package)
        if type(package) is dict:
            package["entities"] = []
        return result

    monkeypatch.setattr(check.model, "validate_extension", mutation)
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    assert all(not case["nonmutating"] for case in report["cases"])


def test_an_operation_crash_is_a_failed_case(experiment, monkeypatch):
    store(experiment, synthetic_cases())

    def failure(*args, **kwargs):
        raise ValueError("intentional processor failure")

    monkeypatch.setattr(check.model, "names_of", failure)
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    assert "intentional processor failure" in report["cases"][0]["error"]


def test_check_rejects_a_stale_contract_without_rewriting(experiment, monkeypatch):
    store(experiment, synthetic_cases())
    monkeypatch.setattr(check, "ROOT", experiment)
    original = check.build_report
    monkeypatch.setattr(check, "build_report", lambda: original(experiment))
    assert check.main([]) == 0
    path = experiment / check.REPORT
    recorded = path.read_bytes()
    assert check.main(["--check"]) == 0
    definition = experiment / "knowledge/text-model.md"
    definition.write_text(definition.read_text(encoding="utf-8") + "\nAn intentional edit.\n",
                          encoding="utf-8")
    assert check.main(["--check"]) == 1
    assert path.read_bytes() == recorded


def test_checkout_line_endings_do_not_change_the_report(experiment):
    store(experiment, synthetic_cases())
    before = check.json_bytes(check.build_report(experiment))
    for relative in check.build_report(experiment)["inputs"]:
        path = experiment / relative
        path.write_bytes(path.read_text(encoding="utf-8").replace("\n", "\r\n").encode("utf-8"))
    assert before == check.json_bytes(check.build_report(experiment))


def test_validate_cli_returns_a_structural_result(tmp_path, capsys):
    path = tmp_path / "package.json"
    path.write_bytes(check.json_bytes(package()))
    assert check.main(["--validate", str(path)]) == 0
    assert json.loads(capsys.readouterr().out)["valid"] is True
    path.write_bytes(check.json_bytes({**package(), "entities": []}))
    assert check.main(["--validate", str(path)]) == 1
    assert json.loads(capsys.readouterr().out)["valid"] is False
