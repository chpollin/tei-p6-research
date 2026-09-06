"""The acceptance audit must not silently reuse stale or incomplete reviews."""

import shutil
from copy import deepcopy
from pathlib import Path

import pytest

from tools.check_text_identity_pilot import check_review, current_pairs
from tools.review import prompt_hash


def records():
    pairs = [
        {
            "id": "pair-1",
            "document": "20_distillates/documents/a",
            "prompt": "PASSAGE: a. STATEMENT: a.",
        }
    ]
    verdicts = [{
        "id": "pair-1", "verdict": "fully supports", "reason": "The passage states a.",
        "reviewer": "independent-reviewer", "prompt_sha256": prompt_hash(pairs[0]),
    }]
    return pairs, deepcopy(pairs), verdicts


def test_current_complete_review_passes():
    audit = check_review(*records())
    assert (audit.pairs, audit.without_reviewer) == (1, ())


@pytest.mark.parametrize("mutation", [
    "stale-passage", "missing-verdict", "duplicate-verdict", "wrong-hash",
    "overreaches", "missing-reason", "unknown-pair",
])
def test_acceptance_rejects_invalid_review(mutation):
    pairs, stored, verdicts = records()
    if mutation == "stale-passage":
        pairs[0]["prompt"] = "A changed passage and claim."
    elif mutation == "missing-verdict":
        verdicts.clear()
    elif mutation == "duplicate-verdict":
        verdicts.append(deepcopy(verdicts[0]))
    elif mutation == "wrong-hash":
        verdicts[0]["prompt_sha256"] = "0" * 64
    elif mutation == "overreaches":
        verdicts[0]["verdict"] = "overreaches"
    elif mutation == "missing-reason":
        verdicts[0]["reason"] = ""
    else:
        verdicts[0]["id"] = "unrelated"
    with pytest.raises(ValueError):
        check_review(pairs, stored, verdicts)


def test_a_verdict_without_a_reviewer_passes_and_is_named():
    """Attribution is reported rather than required; one recorded review has none."""
    pairs, stored, verdicts = records()
    del verdicts[0]["reviewer"]
    assert check_review(pairs, stored, verdicts).without_reviewer == ("pair-1",)


def test_the_recorded_pilot_review_binds_the_current_pairs():
    """The audit of this repository, over its own vault and its own review files."""
    from tools.check_text_identity_pilot import AUDIT
    from tools.review import read_jsonl

    audit = check_review(
        current_pairs(),
        read_jsonl(AUDIT / "pairs.jsonl"),
        read_jsonl(AUDIT / "verdicts.jsonl"),
    )
    assert audit.without_reviewer == ()


def test_new_chapter_dependency_cannot_escape_review(tmp_path):
    root = Path(__file__).resolve().parents[1]
    for folder in ("10_markdown", "20_distillates", "30_assertions", "40_output"):
        shutil.copytree(root / folder, tmp_path / folder)
    current_pairs(tmp_path)
    original = tmp_path / "30_assertions/p5-anchor-identifies-a-textual-point.md"
    extra = tmp_path / "30_assertions/additional-anchor-requirement.md"
    extra.write_text(original.read_text(encoding="utf-8").replace("#^s1", "#^s2"), encoding="utf-8")
    chapter = tmp_path / "40_output/02-abstract-model.md"
    chapter.write_text(chapter.read_text(encoding="utf-8") +
                       "\nAdditional point requirement.[^extra]\n\n"
                       "[^extra]: Grounded in [[30_assertions/additional-anchor-requirement]].\n",
                       encoding="utf-8")
    with pytest.raises(ValueError, match="scope changed"):
        current_pairs(tmp_path)
