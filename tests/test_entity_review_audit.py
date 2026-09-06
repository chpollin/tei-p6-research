"""The recorded entity-topic review binds the current pairs of its scope."""

from pathlib import Path

from tools.review import Pair, check_support_review

ROOT = Path(__file__).resolve().parents[1]
AUDIT = Path("workbench/reviews/2026-09-06-entities")
ENTITY_DISTILLATES = {
    "persname", "name", "rs", "person", "nym", "att.canonical", "att.naming", "relation", "guidelines-nd",
}


def in_scope(pair: Pair) -> bool:
    if pair.kind == "source":
        slug = pair.document.rsplit("/", 1)[-1]
        return any(slug == f"tei-p5-{name}-4.12.0" for name in ENTITY_DISTILLATES)
    return pair.kind == "assertion" and pair.anchor.split("#")[0].rsplit("/", 1)[-1].startswith(
        tuple(f"tei-p5-{name}-4.12.0" for name in ENTITY_DISTILLATES)
    )


def test_the_recorded_entity_review_binds_the_current_pairs():
    audit = check_support_review(ROOT, ROOT / AUDIT, in_scope)
    assert audit.pairs == 137
    assert audit.without_reviewer == ()


RUN2 = Path("workbench/reviews/2026-09-06-entities-run2")
RUN2_DISTILLATES = {
    "documents/tei-p5-att.personal-4.12.0",
    "documents/tei-p5-att.global.responsibility-4.12.0",
    "documents/tei-p5-att.global.source-4.12.0",
    "documents/tei-p5-att.editlike-4.12.0",
    "documents/tei-p5-att.datable-4.12.0",
    "documents/tei-p5-idno-4.12.0",
    "documents/tei-p5-place-4.12.0",
    "documents/tei-p5-state-4.12.0",
    "documents/tei-p5-test-testnames-4.12.0",
    "publications/teic-tei-issue-337",
    "publications/teic-tei-issue-2739",
    "publications/teic-tei-issue-1414",
}


def in_run2_scope(pair: Pair) -> bool:
    """Source pairs of the twelve run-2 distillates; assertion pairs anchored in them."""
    if pair.kind == "source":
        return pair.document.removeprefix("20_distillates/") in RUN2_DISTILLATES
    anchor = pair.anchor.split("#")[0].removeprefix("20_distillates/")
    return pair.kind == "assertion" and anchor in RUN2_DISTILLATES


def test_the_recorded_run2_review_binds_the_current_pairs():
    audit = check_support_review(ROOT, ROOT / RUN2, in_run2_scope)
    assert audit.pairs == 142
    assert audit.without_reviewer == ()
