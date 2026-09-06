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
    return (
        pair.kind == "assertion"
        and pair.anchor.split("#")[0].rsplit("/", 1)[-1].startswith(
            tuple(f"tei-p5-{name}-4.12.0" for name in ENTITY_DISTILLATES)
        )
        and pair.document.removeprefix("30_assertions/") not in RUN2_ASSERTIONS
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


RUN2_ASSERTIONS = frozenset({
    "p5-att-datable-provides-attributes-for-normalization-of-elements-that-contain-dates-times-or-datable-events",
    "p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup",
    "p5-att-personal-provides-common-attributes-for-elements-forming-part-of-a-name",
    "p5-evidence-indicates-the-nature-of-the-evidence-supporting-an-intervention-or-interpretation",
    "p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people",
    "p5-guidelines-group-information-about-a-person-as-distinct-from-references-to-a-person-within-person",
    "p5-guidelines-state-that-interchange-is-improved-by-tag-uris-in-ref-instead-of-key",
    "p5-guidelines-use-generic-state-trait-and-event-customized-through-type-for-information-about-a-place",
    "p5-idno-serves-labels-that-identify-an-object-or-concept-in-a-cataloguing-system-or-a-distributed-system",
    "p5-idno-supplies-any-form-of-identifier-used-to-identify-some-object-in-a-standardized-way",
    "p5-key-remarks-propose-no-particular-syntax-because-its-form-depends-on-project-practice",
    "p5-nested-description-elements-inherit-type-and-responsibility-and-may-date-more-precisely",
    "p5-place-contains-data-about-a-geographic-location",
    "p5-resp-should-point-to-an-element-that-clarifies-the-agents-role-rather-than-to-a-person-or-org",
    "p5-source-specifies-the-source-from-which-some-aspect-of-an-element-is-drawn",
    "p5-state-attributes-a-status-or-quality-often-at-a-specific-time-or-for-a-date-range",
    "p5-state-describes-a-status-or-quality-attributed-to-a-person-place-or-organization",
    "p5-testnames-change-of-place-is-a-sequence-of-dated-residence-states-without-an-event",
    "p5-testnames-name-of-type-person-in-a-note-carries-a-key-and-no-ref",
    "p5-testnames-person-name-form-and-place-carry-three-separate-identifying-values",
    "p5-testnames-person-record-carries-id-sex-and-role-while-its-persname-carries-only-a-language",
    "p5-testnames-places-in-birth-and-death-are-named-without-identification-while-a-nationality-is-identified-by-key",
    "p5-testnames-relation-to-another-person-is-a-state-with-a-ref-to-a-relationship-and-no-relation-element",
    "teic-tei-issue-1414-author-proposes-ref-and-key-on-person-and-place",
    "teic-tei-issue-1414-author-proposes-that-a-record-entry-refer-through-ref-or-key-to-further-information-about-the-same-entity",
    "teic-tei-issue-1414-comment-of-2019-reports-that-person-place-org-and-bibl-allow-idno-while-event-and-nym-do-not",
    "teic-tei-issue-1414-commenter-summarizes-idno-as-a-first-child-of-the-record-elements-as-the-short-term-solution",
    "teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical",
    "teic-tei-issue-337-author-announces-an-interim-guidelines-change-telling-people-to-switch-to-ref",
    "teic-tei-issue-337-author-reports-a-wish-to-deprecate-key-held-back-by-its-wide-use",
    "teic-tei-issue-337-commenter-excepts-values-that-already-refer-to-an-external-vocabulary",
})


def in_run2_scope(pair: Pair) -> bool:
    """Source pairs of the twelve run-2 distillates and the pairs of the run-2 assertions."""
    if pair.kind == "source":
        return pair.document.removeprefix("20_distillates/") in RUN2_DISTILLATES
    return pair.kind == "assertion" and pair.document.removeprefix("30_assertions/") in RUN2_ASSERTIONS


def test_the_recorded_run2_review_binds_the_current_pairs():
    audit = check_support_review(ROOT, ROOT / RUN2, in_run2_scope)
    assert audit.pairs == 172
    assert audit.without_reviewer == ()
