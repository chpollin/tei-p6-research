"""Challenge evidence integrity, attribution and revision on the acquired sample."""

import copy

import pytest

from tools.check_identity_evidence import (
    build_dossier,
    outputs,
    synthetic_identity_cases,
)
from tools.ingest_identity_evidence import ROOT, check, snapshots, verify_xml
from tools.models import identity_evidence as profile


@pytest.fixture
def sample():
    intake, originals = snapshots()
    return build_dossier(intake), originals


def test_real_dossier_preserves_source_qualification(sample):
    dossier, originals = sample
    before = copy.deepcopy(dossier)
    assert profile.validate_profile(dossier, originals)["valid"]
    card = profile.inspect_claim(dossier, "szd-hand", originals)
    assert card["qualifications"][0]["annotation"]["body"] == "(?)"
    assert "certainty" not in card["claim"]
    assert card["record_agent"]["id"] == "ie-importer"
    assert card["assessments"] == []
    assert card["source_support_review"] == "not-established-by-this-operation"
    card["claim"]["value"] = "Changed outside the model"
    assert dossier == before


@pytest.mark.parametrize(("mutation", "code"), [
    (lambda d: d["sources"][0].update(sha256="0" * 64), "E_SOURCE_HASH"),
    (lambda d: d["sources"][0].update(start_byte=-1), "E_SOURCE_BOUNDS"),
    (lambda d: d["sources"][0].update(start_byte=True), "E_SOURCE_SHAPE"),
    (lambda d: d["sources"][0].update(end_byte=d["sources"][0]["end_byte"] - 1), "E_SOURCE_CONTENT"),
    (lambda d: d["sources"].append(copy.deepcopy(d["sources"][0])), "E_SOURCE_REFERENCE"),
    (lambda d: d["sources"].pop(), "E_SOURCE_COVERAGE"),
    (lambda d: d["sources"][0].update(uri="relative/path"), "E_SOURCE_URI"),
    (lambda d: d["package"]["concepts"][0].update(definition="changed"), "E_PROFILE_CONCEPT"),
    (lambda d: d["package"]["annotations"][0].update(body="not the quote"), "E_EVIDENCE_LITERAL"),
    (lambda d: d["package"]["statements"][2].update(certainty="low"), "E_REPORTED_CERTAINTY"),
    (lambda d: d["package"]["relations"].pop(0), "E_EVIDENCE_REQUIRED"),
    (lambda d: d["package"]["relations"][0].update(target="person-lotte"), "E_EVIDENCE_ENDPOINT"),
    (lambda d: d["package"]["statements"][0]["participants"][1].update(entity="artifact-w22"), "E_WORK_PARTICIPANTS"),
    (lambda d: d["package"]["relations"][4].update(source="szd-work-4"), "E_QUALIFICATION_SCOPE"),
])
def test_invalid_source_or_evidence_is_rejected(sample, mutation, code):
    dossier, originals = sample
    mutation(dossier)
    result = profile.validate_profile(dossier, originals)
    assert not result["valid"]
    assert code in {item["code"] for item in result["diagnostics"]}


def test_missing_source_is_not_a_success(sample):
    dossier, originals = sample
    originals.pop(next(iter(originals)))
    result = profile.validate_profile(dossier, originals)
    assert not result["valid"]
    assert "E_SOURCE_HASH" in {item["code"] for item in result["diagnostics"]}


def test_unresolved_quotation_is_not_source_evidence(sample):
    dossier, originals = sample
    dossier["package"]["selections"][0]["selector"] = {
        "kind": "quote", "exact": "This text is absent from the source", "match": "one"}
    result = profile.validate_profile(dossier, originals)
    assert not result["valid"]
    assert "E_EVIDENCE_TARGET" in {item["code"] for item in result["diagnostics"]}


def test_matching_quote_does_not_establish_truth(sample):
    dossier, originals = sample
    dossier["package"]["statements"][2]["value"] = "A fabricated historical conclusion."
    assert profile.validate_profile(dossier, originals)["valid"]
    assert profile.inspect_claim(dossier, "szd-hand", originals)["source_support_review"] == "not-established-by-this-operation"


def add_synthetic_assessment(dossier):
    package = dossier["package"]
    package["agents"].append({"id": "synthetic-reviewer", "label": "Invented test reviewer"})
    original = next(item for item in package["annotations"] if item["id"] == "passage-szd-hand")
    package["annotations"].append({**original, "id": "synthetic-assessment", "agent": "synthetic-reviewer",
                                   "concept": profile.ASSESSMENT, "certainty": "high",
                                   "body": "Synthetic judgment of copying fidelity only; no handwriting comparison."})
    package["relations"].append({"id": "synthetic-assesses", "type": profile.ASSESSES,
                                 "source": "synthetic-assessment", "target": "szd-hand",
                                 "agent": "synthetic-reviewer", "created": original["created"], "status": "asserted"})


def test_separate_assessment_preserves_report_and_revision(sample):
    before, originals = sample
    after = copy.deepcopy(before)
    add_synthetic_assessment(after)
    assert profile.check_profile_revision(before, after, originals)["valid"]
    card = profile.inspect_claim(after, "szd-hand", originals)
    assert "certainty" not in card["claim"]
    assert card["qualifications"][0]["annotation"]["body"] == "(?)"
    assert card["assessments"][0]["agent"]["id"] == "synthetic-reviewer"
    assert card["assessments"][0]["annotation"]["certainty"] == "high"


def test_assessment_link_cannot_impersonate_another_agent(sample):
    dossier, originals = sample
    add_synthetic_assessment(dossier)
    dossier["package"]["relations"][-1]["agent"] = "ie-importer"
    result = profile.validate_profile(dossier, originals)
    assert not result["valid"]
    assert "E_EVIDENCE_AGENT" in {item["code"] for item in result["diagnostics"]}


@pytest.mark.parametrize("change", ["claim", "origin", "removed-qualification"])
def test_revision_cannot_rewrite_prior_evidence(sample, change):
    before, originals = sample
    after = copy.deepcopy(before)
    if change == "claim":
        after["package"]["statements"][2]["value"] = "Rewritten"
    elif change == "origin":
        after["sources"][0]["uri"] = "https://example.org/another-source"
    else:
        after["package"]["relations"] = [item for item in after["package"]["relations"] if item["id"] != "qualifies-hand"]
        after["package"]["annotations"] = [item for item in after["package"]["annotations"] if item["id"] != "qualification-hand"]
    result = profile.check_profile_revision(before, after, originals)
    assert not result["valid"]
    assert {item["code"] for item in result["diagnostics"]} & {"E_CLAIM_REWRITE", "E_SOURCE_REWRITE"}


def test_source_admission_and_generated_outputs_reproduce():
    check()
    first = outputs()
    assert first == outputs()
    for path, wanted in first.items():
        assert (ROOT / path).read_bytes() == wanted


def test_synthetic_identity_policies_are_not_acquired_facts():
    cases = synthetic_identity_cases()
    assert len(cases) == 4 and all(case["passed"] and case["synthetic"] for case in cases)
    ungrouped = cases[2]["package"]
    assert ungrouped["versions"][0]["content"] == ungrouped["versions"][1]["content"]
    assert ungrouped["continuities"] == []


def test_external_xml_declarations_are_rejected():
    with pytest.raises(ValueError, match="declarations"):
        verify_xml(b'<!DOCTYPE TEI [<!ENTITY x SYSTEM "file:///secret">]><TEI/>')


def test_revision_cannot_change_the_kind_of_an_unchanged_claim_subject(sample):
    before, originals = sample
    after = copy.deepcopy(before)
    person = next(item for item in after["package"]["entities"] if item["id"] == "person-lotte")
    person["kind"] = "object"
    assert profile.validate_profile(after, originals)["valid"]
    result = profile.check_profile_revision(before, after, originals)
    assert not result["valid"]
    assert "E_IDENTITY_REWRITE" in {item["code"] for item in result["diagnostics"]}
