"""Current scholarly content must retain complete primary and blind review coverage."""

from pathlib import Path

from tools.current_review import check


def test_current_knowledge_has_complete_review_coverage():
    result = check(Path(__file__).parents[1])
    assert result["all_support"]
    assert result["counts"]["chapter-complete"] == 4
    assert result["counts"]["distillate-complete"] >= 61
    assert result["counts"]["assertion-complete"] >= 120
    assert not result["human_verified"]
