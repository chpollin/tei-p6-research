"""Fixture tests for the deterministic parts of tools/review.py.

Covered are pair cutting, prompt construction, verdict parsing, the booking of
checked.machine-review and the audit of a recorded review, all against
tests/fixtures/minimal. The judging mechanism itself is not exercised here: no
test calls a model, and the batch path is driven with hand-written verdicts.
"""

import json
import shutil
from pathlib import Path

import pytest

from tools.review import (
    VERDICTS,
    Pair,
    _block_locations,
    audit_record,
    book_results,
    build_prompt,
    check_review_records,
    check_support_review,
    cut_pairs,
    parse_verdict,
    prompt_hash,
    read_jsonl,
    run_claude,
    select_pairs,
    set_checked_date,
)
from tools.validate import Doc

REPO = Path(__file__).parents[1]
MINIMAL = REPO / "tests" / "fixtures" / "minimal"

DOC_DISTILLATE = "20_distillates/documents/report-garden-water-2026"
DATA_DISTILLATE = "20_distillates/data/water-readings-2025"
PUB_DISTILLATE = "20_distillates/publications/example-2024-metering"
ASSERTION = "30_assertions/metering-reduces-water-use"


@pytest.fixture(scope="module")
def pairs():
    return cut_pairs(MINIMAL)


def _by_id(pairs, pair_id):
    found = [p for p in pairs if p.id == pair_id]
    assert len(found) == 1, f"{pair_id} not cut exactly once: {len(found)}"
    return found[0]


def test_every_statement_and_every_grounding_becomes_one_pair(pairs) -> None:
    source_pairs = [p for p in pairs if p.kind == "source"]
    assertion_pairs = [p for p in pairs if p.kind == "assertion"]
    assert len(source_pairs) == 5  # 3 document, 1 data, 1 publication statements
    assert len(assertion_pairs) == 3  # one per grounding anchor of the assertion
    assert len({p.id for p in pairs}) == len(pairs)


def test_pair_cutting_is_deterministic() -> None:
    first = cut_pairs(MINIMAL)
    second = cut_pairs(MINIMAL)
    assert [p.id for p in first] == [p.id for p in second]
    assert [p.location for p in first] == [p.location for p in second]


def test_document_pair_is_block_plus_heading_path(pairs) -> None:
    pair = _by_id(pairs, f"{DOC_DISTILLATE}#^s1")
    assert pair.anchor == "10_markdown/documents/report-garden-water-2026#^a1b2"
    assert "Annual Water Report of the Example Community Garden 2026" in pair.location
    assert (
        "Water meters were installed on all forty plots in January 2025."
        in pair.location
    )
    assert pair.claim == "Water meters were installed on all plots in January 2025."


def test_publication_pair_is_the_verbatim_quotation(pairs) -> None:
    pair = _by_id(pairs, f"{PUB_DISTILLATE}#^s1")
    assert (
        '"Metering alone reduced irrigation volumes in nine of eleven surveyed gardens."'
        in pair.location
    )
    assert "example2024metering, p. 4" in pair.location
    assert pair.claim.startswith("In the surveyed gardens, metering alone")


def test_data_pair_is_the_computation_and_its_result(pairs) -> None:
    pair = _by_id(pairs, f"{DATA_DISTILLATE}#^s1")
    assert "python tools/analysis/reduction.py" in pair.location
    assert "31.4" in pair.location
    assert pair.claim == "Water use in 2025 was 31.4 percent below 2024."


def test_assertion_pair_holds_statement_and_assertion_sentence(pairs) -> None:
    pair = _by_id(pairs, f"{ASSERTION}<-{DATA_DISTILLATE}#^s1")
    assert pair.location == "Water use in 2025 was 31.4 percent below 2024."
    assert pair.claim == (
        "Plot metering coincided with a water use reduction of roughly a third"
    )
    assert pair.document == ASSERTION


def test_anti_anchoring_keeps_the_producing_reasoning_out(pairs) -> None:
    """Nothing but location and claim enters the pair, so no link, anchor or Support text."""
    for pair in pairs:
        assert "[[" not in pair.location and "[[" not in pair.claim
        assert "^s" not in pair.claim
        assert "## Support" not in pair.prompt
        assert "what this anchor contributes" not in pair.prompt
    contribution = "the readings reproduce the drop as 31.4 percent"
    assert all(contribution not in pair.prompt for pair in pairs)


def test_prompts_follow_the_skeletons_of_operations_md(pairs) -> None:
    source = _by_id(pairs, f"{DOC_DISTILLATE}#^s1").prompt
    assertion = _by_id(pairs, f"{ASSERTION}<-{DATA_DISTILLATE}#^s1").prompt
    for prompt in (source, assertion):
        assert prompt.startswith("You are an adversarial reviewer.")
        for verdict in VERDICTS:
            assert verdict in prompt
    assert "PASSAGE:" in source and "STATEMENT:" in source
    assert "ASSERTION:" not in source
    assert "STATEMENT:" in assertion and "ASSERTION:" in assertion
    assert "PASSAGE:" not in assertion


def test_build_prompt_is_a_pure_function_of_the_pair(pairs) -> None:
    for pair in pairs:
        assert build_prompt(pair) == pair.prompt


@pytest.mark.parametrize(
    ("response", "expected"),
    [
        ("fully supports", "fully supports"),
        ("Fully supports. The passage states exactly this.", "fully supports"),
        ("**overreaches**\nThe statement widens the finding.", "overreaches"),
        (
            "Verdict: not in the text\nNothing in the passage says so.",
            "not in the text",
        ),
        ("  partially supports  ", "partially supports"),
        (
            "The passage names a different year, so the verdict is contradicts.",
            "contradicts",
        ),
    ],
)
def test_parse_verdict_accepts_the_vocabulary(response: str, expected: str) -> None:
    assert parse_verdict(response) == expected


@pytest.mark.parametrize(
    "response",
    [
        "",
        "supports",
        "yes",
        "mostly supports",
        "It fully supports the first half but overreaches on the second.",
    ],
)
def test_parse_verdict_rejects_everything_else(response: str) -> None:
    with pytest.raises(ValueError):
        parse_verdict(response)


def test_set_checked_date_keeps_the_rest_of_the_frontmatter() -> None:
    text = "---\ntype: distillate\nchecked:\n  quote: 2026-07-11\nupdated: 2026-07-11\n---\n\n# X\n"
    out = set_checked_date(text, "machine-review", "2026-08-09")
    assert "  quote: 2026-07-11\n" in out
    assert "  machine-review: 2026-08-09\n" in out
    assert out.count("checked:") == 1
    assert (
        set_checked_date(out, "machine-review", "2026-08-10").count("machine-review")
        == 1
    )


def test_set_checked_date_expands_an_empty_map() -> None:
    text = "---\ntype: assertion\nchecked: {}\nupdated: 2026-07-11\n---\n\n# X\n"
    out = set_checked_date(text, "machine-review", "2026-08-09")
    assert "checked:\n  machine-review: 2026-08-09\nupdated: 2026-07-11\n" in out


def test_set_checked_date_refuses_a_document_without_the_field() -> None:
    with pytest.raises(ValueError):
        set_checked_date("---\ntype: moc\n---\n\n# X\n", "machine-review", "2026-08-09")


def _all_fully_supports(pairs) -> dict[str, str]:
    return {p.id: "fully supports" for p in pairs}


def test_booking_sets_the_date_only_on_a_clean_document(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    verdicts = _all_fully_supports(pairs)
    verdicts[f"{DOC_DISTILLATE}#^s3"] = "overreaches"

    outcome = book_results(vault, pairs, verdicts, "2026-08-09", apply=True)

    booked = {r.document for r in outcome.documents if r.booked}
    assert DOC_DISTILLATE not in booked
    assert {DATA_DISTILLATE, PUB_DISTILLATE, ASSERTION} <= booked
    assert [(d.pair_id, d.verdict) for d in outcome.deviations] == [
        (f"{DOC_DISTILLATE}#^s3", "overreaches")
    ]
    assert "machine-review: 2026-08-09" in (vault / f"{ASSERTION}.md").read_text(
        encoding="utf-8"
    )
    assert "machine-review" not in (vault / f"{DOC_DISTILLATE}.md").read_text(
        encoding="utf-8"
    )


def test_booking_without_apply_writes_nothing(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    before = (vault / f"{ASSERTION}.md").read_text(encoding="utf-8")

    outcome = book_results(
        vault, pairs, _all_fully_supports(pairs), "2026-08-09", apply=False
    )

    assert all(r.booked for r in outcome.documents)
    assert (vault / f"{ASSERTION}.md").read_text(encoding="utf-8") == before


def test_unjudged_pairs_block_the_booking_and_are_reported(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    verdicts = _all_fully_supports(pairs)
    del verdicts[f"{PUB_DISTILLATE}#^s1"]

    outcome = book_results(vault, pairs, verdicts, "2026-08-09", apply=True)

    assert outcome.unjudged == [f"{PUB_DISTILLATE}#^s1"]
    assert PUB_DISTILLATE not in {r.document for r in outcome.documents if r.booked}


def test_booking_keeps_the_line_endings_of_the_file(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    path = vault / f"{ASSERTION}.md"
    path.write_bytes(
        path.read_text(encoding="utf-8").replace("\n", "\r\n").encode("utf-8")
    )
    pairs = cut_pairs(vault)

    book_results(vault, pairs, _all_fully_supports(pairs), "2026-08-09", apply=True)

    raw = path.read_bytes()
    assert b"machine-review: 2026-08-09" in raw
    assert raw.count(b"\n") == raw.count(b"\r\n")


class _Result:
    returncode = 0
    stderr = ""
    stdout = "fully supports\nThe passage states exactly this."


def test_run_claude_passes_the_prompt_on_stdin(monkeypatch, pairs) -> None:
    """Windows caps a command line at ~32k characters, so no prompt goes into argv."""
    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs))
        return _Result()

    monkeypatch.setattr("tools.review.shutil.which", lambda name: "claude")
    monkeypatch.setattr("tools.review.subprocess.run", fake_run)

    long_pair = pairs[0].__class__(
        id="x",
        kind="source",
        document="d",
        anchor="a",
        location="L" * 40000,
        claim="C",
    )
    problems: list[str] = []
    records = run_claude([long_pair], "sonnet", problems)

    assert problems == []
    assert [r["verdict"] for r in records] == ["fully supports"]
    command, kwargs = calls[0]
    assert all(long_pair.prompt not in part for part in command)
    assert max(len(part) for part in command) < 4096
    assert kwargs["input"] == long_pair.prompt


def test_booked_vault_still_validates(tmp_path) -> None:
    from tools.validate import validate

    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    book_results(vault, pairs, _all_fully_supports(pairs), "2026-08-09", apply=True)
    assert validate(vault).errors == []


def _audit_records(vault: Path, scope) -> tuple[list[dict], list[dict]]:
    """The current pairs of `vault` in scope, with one passing verdict each."""
    pairs = [pair.to_dict() for pair in select_pairs(vault, scope)]
    verdicts = [
        {
            "id": pair["id"],
            "verdict": "fully supports",
            "reason": "The passage carries the statement.",
            "reviewer": "fixture reviewer",
            "prompt_sha256": prompt_hash(pair),
        }
        for pair in pairs
    ]
    return pairs, verdicts


def _write_review(directory: Path, pairs: list[dict], verdicts: list[dict]) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    for name, records in (("pairs", pairs), ("verdicts", verdicts)):
        (directory / f"{name}.jsonl").write_text(
            "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8"
        )
    return directory


IN_DISTILLATES = "20_distillates/"


def _distillate_scope(pair) -> bool:
    return pair.document.startswith(IN_DISTILLATES)


@pytest.fixture
def review(tmp_path):
    """A vault whose distillate pairs all carry a current passing verdict."""
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs, verdicts = _audit_records(vault, _distillate_scope)
    return vault, _write_review(tmp_path / "review", pairs, verdicts), pairs, verdicts


def test_a_complete_current_review_passes(review) -> None:
    vault, directory, pairs, _ = review
    audit = check_support_review(vault, directory, _distillate_scope, expected=len(pairs))
    assert audit.pairs == len(pairs)
    assert audit.documents == (DATA_DISTILLATE, DOC_DISTILLATE, PUB_DISTILLATE)
    assert audit.without_reviewer == ()


def test_a_changed_statement_makes_the_stored_review_stale(review) -> None:
    vault, directory, _, _ = review
    distillate = vault / f"{DATA_DISTILLATE}.md"
    distillate.write_text(
        distillate.read_text(encoding="utf-8").replace("31.4 percent", "a third"),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="stale against the current prompts"):
        check_support_review(vault, directory, _distillate_scope)


def test_a_new_statement_is_not_covered_by_the_stored_review(review) -> None:
    vault, directory, _, _ = review
    distillate = vault / f"{DOC_DISTILLATE}.md"
    distillate.write_text(
        distillate.read_text(encoding="utf-8").replace(
            "\n## Terms",
            "- A statement nobody reviewed."
            " [[10_markdown/documents/report-garden-water-2026#^e5f6]] ^s9\n\n## Terms",
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="pair coverage"):
        check_support_review(vault, directory, _distillate_scope)


def test_the_declared_scope_is_held_against_the_pairs(review) -> None:
    vault, directory, _, _ = review
    with pytest.raises(ValueError, match="declared documents"):
        check_support_review(
            vault, directory, _distillate_scope, documents={DOC_DISTILLATE}
        )


def test_a_review_of_another_size_than_declared_is_refused(review) -> None:
    vault, directory, _, _ = review
    with pytest.raises(ValueError, match="exactly 99 current pairs"):
        check_support_review(vault, directory, _distillate_scope, expected=99)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("unknown", "unknown pair"),
        ("duplicate", "recorded twice"),
        ("nonpassing", "nonpassing review verdict"),
        ("stale-hash", "stale review verdict prompt hash"),
        ("missing-reason", "missing reason"),
        ("missing-verdict", "coverage is incomplete"),
    ],
)
def test_the_audit_refuses_a_defective_verdict_set(review, mutation, message) -> None:
    vault, directory, pairs, verdicts = review
    if mutation == "unknown":
        verdicts[0]["id"] = "not-a-pair"
    elif mutation == "duplicate":
        verdicts[1] = dict(verdicts[0])
    elif mutation == "nonpassing":
        verdicts[0]["verdict"] = "overreaches"
    elif mutation == "stale-hash":
        verdicts[0]["prompt_sha256"] = "0" * 64
    elif mutation == "missing-reason":
        verdicts[0]["reason"] = "  "
    else:
        verdicts.pop()
    _write_review(directory, pairs, verdicts)
    with pytest.raises(ValueError, match=message):
        check_support_review(vault, directory, _distillate_scope)


def test_a_verdict_without_a_reviewer_passes_and_is_named(review) -> None:
    """The editorial review of 2026-09-05 records no reviewer, so it is reported."""
    vault, directory, pairs, verdicts = review
    del verdicts[0]["reviewer"]
    _write_review(directory, pairs, verdicts)
    audit = check_support_review(vault, directory, _distillate_scope)
    assert audit.without_reviewer == (verdicts[0]["id"],)


def test_a_reviewer_can_be_demanded_where_the_records_carry_one(review) -> None:
    vault, directory, pairs, verdicts = review
    del verdicts[0]["reviewer"]
    _write_review(directory, pairs, verdicts)
    with pytest.raises(ValueError, match="missing reviewer"):
        check_support_review(
            vault,
            directory,
            _distillate_scope,
            required_fields=("verdict", "reason", "prompt_sha256", "reviewer"),
        )


def test_a_blank_line_in_the_review_files_is_no_record(review) -> None:
    vault, directory, _, _ = review
    path = directory / "verdicts.jsonl"
    path.write_text(path.read_text(encoding="utf-8") + "\n\n", encoding="utf-8")
    assert check_support_review(vault, directory, _distillate_scope).pairs == len(
        read_jsonl(directory / "pairs.jsonl")
    )


def test_an_empty_review_scope_is_refused(review) -> None:
    vault, directory, _, _ = review
    with pytest.raises(ValueError, match="at least one current pair"):
        check_review_records([], [], [])
    assert check_support_review(vault, directory, _distillate_scope).pairs


def test_a_standalone_block_id_after_a_fence_keeps_the_block_text(tmp_path):
    """The chapter representation form puts the ID on its own line after the source fence."""
    body = chr(10).join([
        "# Chapter",
        "",
        "## Source blocks",
        "",
        "### Block 1",
        "",
        "XML location: `/div[1]/p[1]`.",
        "",
        "```xml",
        "<p>Hello block</p>",
        "```",
        "",
        "^b1",
        "",
        "Inline paragraph with its own id. ^b2",
    ])
    fm = {"metadata": {"title": "TEI P5 4.12.0 x specification"}}
    doc = Doc(path=tmp_path, rel="10_markdown/documents/x", fm=fm, body=body, blocks=["b1", "b2"])
    locations = _block_locations(doc)
    assert "<p>Hello block</p>" in locations["b1"]
    assert "XML location" in locations["b1"]
    assert "```" not in locations["b1"]
    assert locations["b2"].endswith("Inline paragraph with its own id.")
    assert locations["b1"].startswith("TEI P5 4.12.0 x specification > Chapter > Source blocks > Block 1")


def test_audit_record_binds_the_verdict_to_the_prompt_hash(tmp_path):
    pair = Pair(
        id="20_distillates/documents/x#^s1",
        kind="source",
        document="20_distillates/documents/x",
        anchor="10_markdown/documents/x#^r1",
        location="Heading > text",
        claim="The claim.",
    )
    response = "**Verdict: fully supports**" + chr(10) + chr(10) + "The passage says exactly that."
    record = audit_record(pair, response, "claude-fable-5-1")
    assert record["verdict"] == "fully supports"
    assert record["reason"] == "The passage says exactly that."
    assert record["prompt_sha256"] == prompt_hash(pair.to_dict())
    assert record["reviewer"].startswith("claude-fable-5-1; fresh context per pair")
