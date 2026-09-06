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
