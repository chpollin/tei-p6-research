"""Regression gates distinguish source support, structural checks, and migration."""

import copy
import hashlib
import json
import shutil

import pytest

from tools import check_editorial_cases as check


@pytest.fixture
def experiment(tmp_path):
    shutil.copytree(check.ROOT / check.BASE, tmp_path / check.BASE)
    paths = ["tools/ingest_editorial_cases.py", "tools/check_editorial_cases.py",
             "tools/models/abstract_text.py", "tools/models/editorial_profile.py",
             "tools/tei/editorial_cases.py", "10_markdown/documents/humboldt-h0017682-7d174637.md"]
    for relative in paths:
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(check.ROOT / relative, target)
    return tmp_path


def write_json(path, value):
    path.write_bytes(check.json_bytes(value))


def test_finite_comparison_reproduces_and_holdout_refusal_is_not_migration(experiment):
    report = check.build_report(experiment)
    assert report["summary"]["passed"]
    assert report["summary"]["successful_bounded_mappings"] == 2
    assert report["summary"]["holdout_migration_success"] is False
    holdout = next(item for item in report["editorial"] if item["role"] == "holdout")
    assert holdout["passed"] is True
    assert holdout["migration_success"] is False
    assert holdout["baseline_primary_text_matches"] is False
    assert set(holdout["comparison"]["candidate"]["unsupported"]) == {"fw", "pb"}
    assert holdout["comparison"]["candidate"]["observations"] is None
    assert all(item["nonmutating"] for item in report["identity"])
    assert check.json_bytes(report) == check.json_bytes(check.build_report(experiment))


@pytest.mark.parametrize("change", ["fragment-hash", "fragment-text", "fragment-boundary", "case-boundary"])
def test_case_source_drift_and_boundary_change_fail_closed(experiment, change):
    path = experiment / check.BASE / "cases.json"
    cases = check.read_json(path)
    if change == "fragment-hash":
        cases["cases"][0]["fragment_sha256"] = "0" * 64
    elif change == "fragment-text":
        cases["cases"][0]["original_xml"] += "changed"
    elif change == "fragment-boundary":
        cases["cases"][0]["start_byte"] += 1
    else:
        cases["cases"].append(copy.deepcopy(cases["cases"][0]))
    write_json(path, cases)
    with pytest.raises(ValueError, match="fragment drift|boundary changed"):
        check.build_report(experiment)


def test_wrong_development_expectation_fails_without_rewriting_oracle(experiment):
    path = experiment / check.BASE / "cases.json"
    cases = check.read_json(path)
    cases["cases"][0]["primary_text"] = "A deliberately incorrect expectation"
    write_json(path, cases)
    snapshot = path.read_bytes()
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    row = next(item for item in report["editorial"] if item["id"] == "case-1-hierarchy")
    assert not row["baseline_checks"]["primary_text"]
    assert not row["candidate_checks"]["primary_text"]
    assert path.read_bytes() == snapshot


def test_holdout_silent_flattening_cannot_pass_the_evaluation_gate(experiment, monkeypatch):
    original = check.compare_fragment

    def flatten(xml):
        result = original(xml)
        if "<pb " in xml:
            result["candidate"].update(valid=True, package={}, unsupported=[],
                                       observations=result["baseline"]["observations"])
        return result

    monkeypatch.setattr(check, "compare_fragment", flatten)
    report = check.build_report(experiment)
    assert not report["summary"]["passed"]
    assert not next(item for item in report["editorial"] if item["role"] == "holdout")["passed"]


def test_missing_unsupported_diagnostic_does_not_count_as_honest_refusal(experiment, monkeypatch):
    original = check.compare_fragment

    def silent_failure(xml):
        result = original(xml)
        if "<pb " in xml:
            result["candidate"]["unsupported"] = []
        return result

    monkeypatch.setattr(check, "compare_fragment", silent_failure)
    assert not check.build_report(experiment)["summary"]["passed"]


def test_identity_operations_are_measured_for_mutation_not_trusted(experiment, monkeypatch):
    path = experiment / check.BASE / "identity-cases.json"
    suite = check.read_json(path)
    suite["cases"] = [next(case for case in suite["cases"] if case["operation"] == "validate")]
    write_json(path, suite)
    snapshot = path.read_bytes()
    original = check.profile.validate_profile

    def mutating(package):
        result = original(package)
        package["agents"][0]["label"] += " mutated"
        return result

    monkeypatch.setattr(check.profile, "validate_profile", mutating)
    results = check.identity_results(experiment)
    assert results[0]["actual"] == results[0]["expected"]
    assert results[0]["nonmutating"] is False
    assert results[0]["passed"] is False
    assert path.read_bytes() == snapshot


@pytest.mark.parametrize("change", ["duplicate", "unknown-operation", "wrong-version", "empty"])
def test_identity_suite_scope_is_checked(experiment, change):
    path = experiment / check.BASE / "identity-cases.json"
    suite = check.read_json(path)
    if change == "duplicate":
        suite["cases"].append(copy.deepcopy(suite["cases"][0]))
    elif change == "unknown-operation":
        suite["cases"][0]["operation"] = "approve-truth"
    elif change == "wrong-version":
        suite["profile_version"] = "another-profile"
    else:
        suite["cases"] = []
    write_json(path, suite)
    with pytest.raises(ValueError):
        check.identity_results(experiment)


@pytest.fixture
def review(tmp_path, monkeypatch):
    pairs = [{"id": f"source-pair-{i}", "prompt": f"Source-support prompt {i}"} for i in range(6)]
    path = tmp_path / check.AUDIT
    path.mkdir(parents=True)
    verdicts = [{"id": pair["id"], "verdict": "fully supports",
                 "prompt_sha256": hashlib.sha256(pair["prompt"].encode("utf-8")).hexdigest()}
                for pair in pairs]
    for name, values in (("pairs", pairs), ("verdicts", verdicts)):
        (path / f"{name}.jsonl").write_text("".join(json.dumps(item) + "\n" for item in values), encoding="utf-8")
    monkeypatch.setattr(check, "current_pairs", lambda root: copy.deepcopy(pairs))
    return tmp_path, pairs, verdicts


def test_all_six_fresh_hash_bound_verdicts_are_required(review):
    root, _, _ = review
    check.check_review(root)


@pytest.mark.parametrize("change", ["duplicate", "unknown", "nonpassing", "stale-hash", "missing", "stale-pair"])
def test_review_rejects_nonpassing_duplicate_missing_or_stale_bindings(review, change):
    root, pairs, verdicts = review
    if change == "duplicate":
        verdicts[1] = copy.deepcopy(verdicts[0])
    elif change == "unknown":
        verdicts[0]["id"] = "unknown"
    elif change == "nonpassing":
        verdicts[0]["verdict"] = "partially supports"
    elif change == "stale-hash":
        verdicts[0]["prompt_sha256"] = "0" * 64
    elif change == "missing":
        verdicts.pop()
    else:
        # Change current source context while retaining the stored pairs/verdicts.
        pairs[0]["prompt"] += " New source context."
    (root / check.AUDIT / "verdicts.jsonl").write_text(
        "".join(json.dumps(item) + "\n" for item in verdicts), encoding="utf-8")
    with pytest.raises(ValueError):
        check.check_review(root)


def test_current_pair_scope_requires_six_pairs_and_all_four_documents(monkeypatch):
    class Pair:
        def __init__(self, identifier, document):
            self.identifier, self.document = identifier, document

        def to_dict(self):
            return {"id": self.identifier, "document": self.document, "prompt": "Synthetic support context"}

    documents = sorted(check.DOCUMENTS)
    pairs = [Pair(f"p{i}", document) for i, document in enumerate(documents + documents[:2])]
    monkeypatch.setattr(check, "cut_pairs", lambda root, errors: pairs)
    assert len(check.current_pairs()) == 6
    pairs.pop()
    with pytest.raises(ValueError, match="scope is incomplete"):
        check.current_pairs()
    pairs.append(Pair("outside", "an-unrelated-document"))
    with pytest.raises(ValueError, match="scope is incomplete"):
        check.current_pairs()
