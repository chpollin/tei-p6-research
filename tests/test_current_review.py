"""Coverage and blindness checks beyond individual seal integrity."""

import copy

import pytest

from tools import current_review
from tools.full_review import write_json


@pytest.fixture
def records(tmp_path, monkeypatch):
    judgments = [{"id": f"source::20_distillates/test#^s{i}", "verdict": "fully supports",
                  "model": "claude-opus-5", "requested_model": "opus", "outcome_sha256": "first"}
                 for i in range(30)]
    primary = {"scope_ids": None, "human_verified": False, "instrument_files": {"test": "fixture"},
               "unit_hashes": {v["id"]: str(i) for i, v in enumerate(judgments)}, "verdicts": judgments}
    selected = current_review.sample_ids(primary)
    second = {**copy.deepcopy(primary), "scope_ids": sorted(selected)}
    second["verdicts"] = [{**v, "outcome_sha256": "second"} for v in judgments if v["id"] in selected]
    second["unit_hashes"] = {k: v for k, v in primary["unit_hashes"].items() if k in selected}
    def seal_check(path, root):
        count = 30 if path.name == "primary-seal.json" else len(second["verdicts"])
        return {"all_support": True, "units": count, "bounded_contexts": {}, "boundary": "Offline fixture"}
    monkeypatch.setattr(current_review, "check_seal", seal_check)
    return tmp_path, primary, second


def save(records):
    root, primary, second = records
    write_json(root / current_review.PRIMARY, primary)
    write_json(root / current_review.SECOND, second)
    return root


def test_complete_primary_and_distinct_blind_sample_pass(records):
    result = current_review.check(save(records))
    assert result["primary_units"] == 30 and result["second_units"] == 3
    assert not result["human_verified"]


@pytest.mark.parametrize("change", ["partial", "sample", "reuse", "prompt", "response", "instrument", "model", "human"])
def test_invalid_coverage_or_blindness_fails_closed(records, change):
    _, primary, second = records
    identifier = second["scope_ids"][0]
    if change == "partial":
        primary["scope_ids"] = list(primary["unit_hashes"])
    elif change == "sample":
        second["scope_ids"].pop()
    elif change == "reuse":
        second["reused_packages"] = [{"package_sha256": "fixture"}]
    elif change == "prompt":
        second["unit_hashes"][identifier] = "changed"
    elif change == "response":
        second["verdicts"][0]["outcome_sha256"] = "first"
    elif change == "instrument":
        second["instrument_files"] = {"test": "changed"}
    elif change == "model":
        second["verdicts"][0]["requested_model"] = "default"
    else:
        second["human_verified"] = True
    with pytest.raises(ValueError):
        current_review.check(save(records))


def test_a_nonpassing_individual_seal_cannot_be_overridden(records, monkeypatch):
    monkeypatch.setattr(current_review, "check_seal", lambda *args: {"all_support": False})
    with pytest.raises(ValueError, match="nonpassing"):
        current_review.check(save(records))


def test_nonpassing_primary_units_are_always_in_the_second_sample(records):
    _, primary, _ = records
    primary["verdicts"][-1]["verdict"] = "overreaches"
    assert primary["verdicts"][-1]["id"] in current_review.sample_ids(primary)
