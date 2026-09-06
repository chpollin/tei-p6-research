"""The experiment gate must reject bad expectations, stale inputs, and mutation."""

import copy
import json
import shutil

import pytest

from tools import check_abstract_text_v01 as check


@pytest.fixture
def experiment(tmp_path):
    for relative in ("experiments/abstract_text_v01", "tools/models"):
        shutil.copytree(check.ROOT / relative, tmp_path / relative)
    for relative in ("tools/check_abstract_text_v01.py", "knowledge/text-model.md"):
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(check.ROOT / relative, target)
    return tmp_path


def load_suite(root):
    return check.read_json(root / check.BASE / "cases.json")


def store_suite(root, suite):
    (root / check.BASE / "cases.json").write_bytes(check.json_bytes(suite))


def test_independent_suite_passes_and_reproduces():
    report = check.build_report()
    assert report["summary"]["passed"]
    assert set(report["coverage"]) == {f"R{i:02}" for i in range(1, 14)}
    assert all(case["nonmutating"] for case in report["cases"])
    assert check.json_bytes(report) == check.json_bytes(check.build_report())


@pytest.mark.parametrize("change", ["duplicate_id", "unknown_rule", "unknown_model", "missing_rule", "bad_boolean", "missing_operation"])
def test_case_contract_fails_closed(experiment, change):
    suite = load_suite(experiment)
    if change == "duplicate_id":
        suite["cases"].append(copy.deepcopy(suite["cases"][0]))
    elif change == "unknown_rule":
        suite["cases"][0]["rules"] = ["R999"]
    elif change == "unknown_model":
        suite["cases"][0]["input"]["model"] = "missing"
    elif change == "missing_rule":
        suite["cases"] = [case for case in suite["cases"] if "R13" not in case["rules"]]
    elif change == "bad_boolean":
        suite["cases"][0]["expected"]["valid"] = 1
    elif change == "missing_operation":
        suite["cases"] = [case for case in suite["cases"] if case["operation"] != "revision"]
    store_suite(experiment, suite)
    with pytest.raises(ValueError):
        check.build_report(experiment)


def test_changed_expectation_fails_instead_of_self_approving(experiment):
    suite = load_suite(experiment)
    case = next(case for case in suite["cases"] if case["operation"] == "equivalent")
    case["expected"]["equivalent"] = not case["expected"]["equivalent"]
    store_suite(experiment, suite)
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    assert not next(row for row in report["cases"] if row["id"] == case["id"])["passed"]


def test_missing_standalone_example_is_rejected(experiment):
    (experiment / check.BASE / "examples/competing-readings.json").unlink()
    with pytest.raises(ValueError, match="standalone example missing"):
        check.build_report(experiment)


def test_standalone_example_drift_fails(experiment):
    path = experiment / check.BASE / "examples/competing-readings.json"
    example = check.read_json(path)
    example["agents"][0]["label"] += " altered"
    path.write_bytes(check.json_bytes(example))
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    assert any(not item["matches_case_model"] for item in report["examples"])


def test_mutating_operation_fails(monkeypatch):
    original = check.execute

    def mutation(case, packages):
        result = original(case, packages)
        packages.clear()
        return result

    monkeypatch.setattr(check, "execute", mutation)
    report = check.build_report()
    assert not report["summary"]["passed"]
    assert all(not case["nonmutating"] for case in report["cases"])


def test_operation_exception_is_a_failed_case(monkeypatch):
    def failure(case, packages):
        raise ValueError("intentional processor failure")

    monkeypatch.setattr(check, "execute", failure)
    report = check.build_report()
    assert not report["summary"]["passed"]
    assert all("intentional processor failure" in case["error"] for case in report["cases"])


def test_check_rejects_stale_contract_without_rewriting(experiment, monkeypatch):
    monkeypatch.setattr(check, "ROOT", experiment)
    # build_report's explicit default is the installed root, so provide the test root.
    original = check.build_report
    monkeypatch.setattr(check, "build_report", lambda: original(experiment))
    assert check.main([]) == 0
    path = experiment / check.REPORT
    old = path.read_bytes()
    assert check.main(["--check"]) == 0
    definition = experiment / "knowledge/text-model.md"
    definition.write_text(definition.read_text(encoding="utf-8") + "\nAn intentional edit.\n", encoding="utf-8")
    assert check.main(["--check"]) == 1
    assert path.read_bytes() == old


def test_checkout_line_endings_do_not_change_report(experiment):
    before = check.json_bytes(check.build_report(experiment))
    for relative in check.build_report(experiment)["inputs"]:
        path = experiment / relative
        content = path.read_text(encoding="utf-8")
        path.write_bytes(content.replace("\n", "\r\n").encode("utf-8"))
    assert before == check.json_bytes(check.build_report(experiment))


@pytest.mark.parametrize("content", ['{"id":1,"id":2}', '{"offset":NaN}', '{"offset":Infinity}'])
def test_non_json_or_duplicate_keys_rejected(tmp_path, content):
    path = tmp_path / "invalid.json"
    path.write_text(content, encoding="utf-8")
    assert check.main(["--validate", str(path)]) == 1


def test_validate_cli_returns_structural_result(tmp_path, capsys):
    path = tmp_path / "model.json"
    package = {"model_version": "0.1", **{key: [] for key in check.model.COLLECTIONS}}
    path.write_bytes(check.json_bytes(package))
    assert check.main(["--validate", str(path)]) == 0
    assert json.loads(capsys.readouterr().out)["valid"] is True
    package["unexpected"] = True
    path.write_bytes(check.json_bytes(package))
    assert check.main(["--validate", str(path)]) == 1
    assert json.loads(capsys.readouterr().out)["valid"] is False
