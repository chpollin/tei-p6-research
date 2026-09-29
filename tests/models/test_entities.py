"""Unit checks for the entity extension 0.2; independent case expectations live elsewhere."""

import copy
import hashlib
import json
from pathlib import Path

import pytest

from tools.models.abstract_text import COLLECTIONS
from tools.models.entities import (
    ALIGNMENT_RELATIONS,
    CERTAINTIES,
    CLAIM_STATUSES,
    DIAGNOSTICS,
    ENTITY_KINDS,
    EXTENSION_DIAGNOSTICS,
    MENTION_CONCEPTS,
    MODEL_VERSION,
    NAME_PART_KINDS,
    NEW_COLLECTIONS,
    STATEMENT_KINDS,
    canonical_bytes,
    check_claim_revision,
    denotations_of,
    equivalent,
    names_of,
    validate_extension,
)

CONTENT = "Ada met Bea in Lyon"
INSTANT = "2026-09-06T10:00:00Z"
EXAMPLE = Path(__file__).resolve().parents[2] / "experiments/entities_v02/examples/statements-and-revision.json"


def version(identifier="v1", content=CONTENT, parents=None):
    return {"id": identifier, "content": content,
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "parents": [] if parents is None else parents}


def selection(identifier, start, end):
    return {"id": identifier, "version": "v1", "selector": {
        "kind": "ranges", "segments": [{"start": start, "end": end, "quote": CONTENT[start:end]}]}}


def claim(**fields):
    return {"agent": "a", "created": INSTANT, "status": "asserted", **fields}


def package():
    """A valid 0.2 package with three mentions, three entities and every new collection filled."""
    result = {kind: [] for kind in (*COLLECTIONS, *NEW_COLLECTIONS)}
    result["model_version"] = MODEL_VERSION
    result["agents"] = [{"id": "a", "label": "Editor Ada"}, {"id": "b", "label": "Editor Bea"}]
    result["concepts"] = [*copy.deepcopy(MENTION_CONCEPTS),
                          {"id": "residence", "label": "Residence",
                           "definition": "Where an entity resides.", "applies_to": "statement"}]
    result["versions"] = [version()]
    result["selections"] = [selection("s-ada", 0, 3), selection("s-bea", 8, 11),
                            selection("s-lyon", 15, 19)]
    result["readings"] = [{"id": "r", "version": "v1", "agent": "a", "label": "Mentions", "nodes": [
        {"id": "m-ada", "type": "en-proper-noun", "selection": "s-ada", "parent": None},
        {"id": "m-bea", "type": "en-pronoun", "selection": "s-bea", "parent": None},
        {"id": "m-lyon", "type": "en-referring-string", "selection": "s-lyon", "parent": None}]}]
    result["entities"] = [
        {"id": "e-ada", "label": "Ada", "kind": "person", "alignments": [
            claim(id="al-ada", iri="https://example.org/ada", relation="exact")]},
        {"id": "e-bea", "label": "Bea", "kind": "person"},
        {"id": "e-lyon", "label": "Lyon", "kind": "place"}]
    result["names"] = [claim(id="n-ada", entity="e-ada", form="Ada", language="en",
                             parts=[{"kind": "forename", "form": "Ada"}])]
    result["denotations"] = [claim(id="d-ada", mention="m-ada", entity="e-ada"),
                             claim(id="d-bea", mention="m-bea", entity="e-bea"),
                             claim(id="d-lyon", mention="m-lyon", entity="e-lyon")]
    result["statements"] = [claim(id="st-residence", kind="state", type="residence", participants=[
        {"entity": "e-ada", "role": "subject"}, {"entity": "e-lyon", "role": "place"}], value="Lyon")]
    return result


def diagnostics(result):
    return {(item["code"], item["path"]) for item in result["diagnostics"]}


def codes(result):
    return {item["code"] for item in result["diagnostics"]}


def assign(model, path, value):
    destination = model
    for key in path[:-1]:
        destination = destination[key]
    destination[path[-1]] = value
    return model


def test_the_reference_package_is_valid_and_keeps_the_v01_result_shape():
    result = validate_extension(package())
    assert result["valid"] and result["all_selections_resolved"]
    assert result["diagnostics"] == []
    assert set(result) == {"valid", "all_selections_resolved", "diagnostics", "resolutions"}
    assert set(result["resolutions"]) == {"s-ada", "s-bea", "s-lyon"}


def test_a_v01_package_becomes_valid_by_declaring_the_version_and_empty_collections():
    model = {kind: [] for kind in COLLECTIONS} | {"model_version": "0.1"}
    assert not validate_extension(model)["valid"]
    model["model_version"] = MODEL_VERSION
    assert diagnostics(validate_extension(model)) == {("E_SHAPE", "")}
    model.update({kind: [] for kind in NEW_COLLECTIONS})
    assert validate_extension(model)["valid"]
    model["model_version"] = "0.1"
    assert diagnostics(validate_extension(model)) == {("E_SHAPE", "/model_version")}


@pytest.mark.parametrize("malformed", [None, [], True, 1, "package", {"model_version": MODEL_VERSION}])
def test_nonpackages_return_one_shape_diagnostic_without_raising(malformed):
    assert diagnostics(validate_extension(malformed)) == {("E_SHAPE", "")}
    with pytest.raises(ValueError):
        canonical_bytes(malformed)


def test_base_defects_are_reported_before_the_extension_reads_references():
    model = package()
    model["versions"][0]["sha256"] = "0" * 64
    result = validate_extension(model)
    assert codes(result) == {"E_HASH"}
    assert result["resolutions"] == {}


def undenoted(model):
    """Drop the claim on the pronoun mention, leaving one mention without denotation."""
    model["denotations"] = [item for item in model["denotations"] if item["id"] != "d-bea"]
    return model


def spare(model, **fields):
    """Append an entity no claim references, so a defect in it cascades nowhere."""
    model["entities"].append({"id": "e-spare", "label": "Spare", "kind": "other"} | fields)
    return model


MUTATIONS = {
    "entity-kind": (lambda m: assign(m, ("entities", 0, "kind"), "city"),
                    ("E_ENTITY_KIND", "/entities/0/kind")),
    "entity-label": (lambda m: spare(m, label=""), ("E_SHAPE", "/entities/3/label")),
    "entity-unknown-field": (lambda m: spare(m, note="x"), ("E_SHAPE", "/entities/3")),
    "entity-id": (lambda m: spare(m, id="1bad"), ("E_ID", "/entities/3/id")),
    "entity-node-id-clash": (lambda m: spare(m, id="m-ada"),
                             ("E_DUPLICATE_ID", "/entities/3/id")),
    "statement-kind": (lambda m: assign(m, ("statements", 0, "kind"), "opinion"),
                       ("E_STATEMENT_KIND", "/statements/0/kind")),
    "statement-type-role": (lambda m: assign(m, ("statements", 0, "type"), "en-proper-noun"),
                            ("E_TYPE", "/statements/0/type")),
    "statement-type-missing": (lambda m: assign(m, ("statements", 0, "type"), "absent"),
                               ("E_REFERENCE", "/statements/0/type")),
    "participants-empty": (lambda m: assign(m, ("statements", 0, "participants"), []),
                           ("E_PARTICIPANTS", "/statements/0/participants")),
    "participants-repeated": (lambda m: assign(m, ("statements", 0, "participants", 1),
                                               {"entity": "e-ada", "role": "subject"}),
                              ("E_PARTICIPANTS", "/statements/0/participants/1")),
    "participant-role": (lambda m: assign(m, ("statements", 0, "participants", 0, "role"), ""),
                         ("E_PARTICIPANTS", "/statements/0/participants/0")),
    "participant-entity": (lambda m: assign(m, ("statements", 0, "participants", 0, "entity"), "absent"),
                           ("E_REFERENCE", "/statements/0/participants/0/entity")),
    "language": (lambda m: assign(m, ("names", 0, "language"), "english!"),
                 ("E_LANGUAGE", "/names/0/language")),
    "part-kind": (lambda m: assign(m, ("names", 0, "parts", 0, "kind"), "nickname"),
                  ("E_NAME_PART", "/names/0/parts/0/kind")),
    "part-form": (lambda m: assign(m, ("names", 0, "parts", 0, "form"), ""),
                  ("E_NAME_PART", "/names/0/parts/0/form")),
    "part-shape": (lambda m: assign(m, ("names", 0, "parts", 0), {"form": "Ada"}),
                   ("E_NAME_PART", "/names/0/parts/0")),
    "name-entity": (lambda m: assign(m, ("names", 0, "entity"), "absent"),
                    ("E_REFERENCE", "/names/0/entity")),
    "denotation-entity-category": (lambda m: assign(m, ("denotations", 0, "entity"), "en-pronoun"),
                                   ("E_REFERENCE", "/denotations/0/entity")),
    "denotation-entity-iri": (lambda m: assign(m, ("denotations", 0, "entity"), "https://example.org/ada"),
                              ("E_REFERENCE", "/denotations/0/entity")),
    "denotation-mention-category": (lambda m: assign(m, ("denotations", 0, "mention"), "e-ada"),
                                    ("E_REFERENCE", "/denotations/0/mention")),
    "reserved-concept": (lambda m: assign(m, ("concepts", 0, "label"), "Name"),
                         ("E_MENTION", "/concepts/0")),
    "alignment-iri": (lambda m: assign(m, ("entities", 0, "alignments", 0, "iri"), "example.org/ada"),
                      ("E_ALIGNMENT", "/entities/0/alignments/0/iri")),
    "alignment-relation": (lambda m: assign(m, ("entities", 0, "alignments", 0, "relation"), "same"),
                           ("E_ALIGNMENT", "/entities/0/alignments/0/relation")),
    "created-calendar": (lambda m: assign(m, ("names", 0, "created"), "2026-02-30T00:00:00Z"),
                         ("E_CLAIM_FIELD", "/names/0/created")),
    "created-form": (lambda m: assign(m, ("names", 0, "created"), "2026-09-06 10:00:00"),
                     ("E_CLAIM_FIELD", "/names/0/created")),
    "status": (lambda m: assign(m, ("names", 0, "status"), "retracted"),
               ("E_CLAIM_FIELD", "/names/0/status")),
    "certainty": (lambda m: assign(m, ("names", 0, "certainty"), "certain"),
                  ("E_CLAIM_FIELD", "/names/0/certainty")),
    "valid-empty": (lambda m: assign(m, ("names", 0, "valid"), {}),
                    ("E_CLAIM_FIELD", "/names/0/valid")),
    "valid-order": (lambda m: assign(m, ("names", 0, "valid"), {"from": "2020", "until": "2019"}),
                    ("E_CLAIM_FIELD", "/names/0/valid")),
    "valid-form": (lambda m: assign(m, ("names", 0, "valid"), {"from": "20-20"}),
                   ("E_CLAIM_FIELD", "/names/0/valid/from")),
    "supersedes-kind": (lambda m: assign(m, ("names", 0, "supersedes"), ["d-ada"]),
                        ("E_CLAIM_SUPERSESSION", "/names/0/supersedes")),
    "supersedes-unknown": (lambda m: assign(m, ("names", 0, "supersedes"), ["absent"]),
                           ("E_REFERENCE", "/names/0/supersedes/0")),
    "withdrawn-without-supersedes": (lambda m: assign(m, ("names", 0, "status"), "withdrawn"),
                                     ("E_CLAIM_SUPERSESSION", "/names/0/supersedes")),
    "self-supersession": (lambda m: assign(m, ("names", 0, "supersedes"), ["n-ada"]),
                          ("E_CLAIM_CYCLE", "/names")),
    "base": (lambda m: assign(m, ("base",), "example.org/"), ("E_BASE", "/base")),
    "former-base": (lambda m: assign(m, ("former_bases",),
                                     [claim(id="fb", base="https://example.org/old?x=1")]),
                    ("E_BASE", "/former_bases/0/base")),
    "annotation-concept-missing": (lambda m: assign(m, ("annotations",), [
        {"id": "an", "agent": "a", "selection": "s-ada", "body": "Note", "concept": "absent"}]),
        ("E_REFERENCE", "/annotations/0/concept")),
    "annotation-concept-role": (lambda m: assign(m, ("annotations",), [
        {"id": "an", "agent": "a", "selection": "s-ada", "body": "Note", "concept": "residence"}]),
        ("E_TYPE", "/annotations/0/concept")),
    "node-statement-concept": (lambda m: assign(m, ("readings", 0, "nodes", 0, "type"), "residence"),
                               {("E_TYPE", "/readings/0/nodes/0/type"),
                                ("E_MENTION", "/denotations/0/mention")}),
    "undenoted-mention": (undenoted, ("W_UNDENOTED", "/readings/0/nodes/1")),
}


def expectation(name):
    expected = MUTATIONS[name][1]
    return expected if type(expected) is set else {expected}


@pytest.mark.parametrize("name", sorted(MUTATIONS))
def test_one_malformed_record_yields_exactly_its_diagnostic(name):
    expected = expectation(name)
    model = MUTATIONS[name][0](package())
    before = copy.deepcopy(model)
    result = validate_extension(model)
    assert diagnostics(result) == expected
    assert result["valid"] is all(code.startswith("W_") for code, _ in expected)
    assert model == before


def test_every_declared_diagnostic_is_reachable_from_the_table_or_the_revision_check():
    covered = {code for name in MUTATIONS for code, _ in expectation(name)}
    revised = {code for name in REVISIONS for code, _ in REVISIONS[name][2]}
    assert covered | revised >= set(EXTENSION_DIAGNOSTICS)
    assert set(EXTENSION_DIAGNOSTICS) < set(DIAGNOSTICS)


@pytest.mark.parametrize("kind", ENTITY_KINDS)
def test_every_entity_kind_is_accepted(kind):
    model = package()
    model["entities"][1]["kind"] = kind
    assert validate_extension(model)["valid"]


@pytest.mark.parametrize("kind", STATEMENT_KINDS)
def test_every_statement_kind_is_accepted(kind):
    model = package()
    model["statements"][0]["kind"] = kind
    assert validate_extension(model)["valid"]


@pytest.mark.parametrize("kind", NAME_PART_KINDS)
def test_every_name_part_kind_is_accepted(kind):
    model = package()
    model["names"][0]["parts"] = [{"kind": kind, "form": "Ada"}]
    assert validate_extension(model)["valid"]


@pytest.mark.parametrize("relation", ALIGNMENT_RELATIONS)
def test_every_alignment_relation_is_accepted_on_every_carrier(relation):
    model = package()
    alignment = claim(id="al-x", iri="https://example.org/x", relation=relation)
    model["entities"][0]["alignments"] = [alignment]
    model["concepts"][3]["alignments"] = [claim(id="al-c", iri="https://example.org/c", relation=relation)]
    model["agents"][0]["alignments"] = [claim(id="al-a", iri="https://example.org/a", relation=relation)]
    assert validate_extension(model)["valid"]


@pytest.mark.parametrize("concept", MENTION_CONCEPTS)
def test_every_reserved_mention_concept_carries_a_denotation_subject(concept):
    model = package()
    model["readings"][0]["nodes"][0]["type"] = concept["id"]
    assert validate_extension(model)["valid"]
    assert concept["applies_to"] == "node"


@pytest.mark.parametrize("status", CLAIM_STATUSES)
@pytest.mark.parametrize("certainty", [*CERTAINTIES, None])
def test_status_and_certainty_sets_are_accepted(status, certainty):
    model = package()
    revision = claim(id="d-ada-2", mention="m-ada", entity="e-bea",
                     status=status, supersedes=["d-ada"])
    if certainty is not None:
        revision["certainty"] = certainty
    model["denotations"].append(revision)
    assert validate_extension(model)["valid"]


def test_optional_pattern_fields_on_v01_claims_are_validated_but_never_required():
    model = package()
    assert validate_extension(model)["valid"]
    model["annotations"] = [{"id": "an", "agent": "a", "selection": "s-ada", "body": "Note"}]
    assert validate_extension(model)["valid"]
    model["annotations"][0].update(created=INSTANT, status="asserted", certainty="low",
                                   valid={"from": "1850"}, supersedes=[])
    assert validate_extension(model)["valid"]
    model["annotations"][0]["status"] = "believed"
    assert diagnostics(validate_extension(model)) == {("E_CLAIM_FIELD", "/annotations/0/status")}


def test_supersession_stays_within_kind_agent_and_subject():
    model = package()
    model["denotations"].append(claim(id="d-ada-2", mention="m-ada", entity="e-bea",
                                      supersedes=["d-ada"]))
    assert validate_extension(model)["valid"]
    model["denotations"][3]["agent"] = "b"
    assert diagnostics(validate_extension(model)) == {
        ("E_CLAIM_SUPERSESSION", "/denotations/3/supersedes")}
    model["denotations"][3]["agent"] = "a"
    model["denotations"][3]["mention"] = "m-bea"
    assert diagnostics(validate_extension(model)) == {
        ("E_CLAIM_SUPERSESSION", "/denotations/3/supersedes")}


def test_statement_supersession_compares_the_participant_set_not_the_roles():
    model = package()
    revision = claim(id="st-2", kind="state", type="residence", supersedes=["st-residence"],
                     participants=[{"entity": "e-lyon", "role": "subject"},
                                   {"entity": "e-ada", "role": "place"}])
    model["statements"].append(revision)
    assert validate_extension(model)["valid"]
    revision["participants"] = [{"entity": "e-ada", "role": "subject"}]
    assert diagnostics(validate_extension(model)) == {
        ("E_CLAIM_SUPERSESSION", "/statements/1/supersedes")}


def test_withdrawal_requires_a_superseded_claim_and_a_cycle_is_rejected():
    model = package()
    model["names"].append(claim(id="n-ada-2", entity="e-ada", form="Ada L.", language="en",
                                status="withdrawn", supersedes=["n-ada"]))
    assert validate_extension(model)["valid"]
    model["names"][1]["supersedes"] = []
    assert diagnostics(validate_extension(model)) == {("E_CLAIM_SUPERSESSION", "/names/1/supersedes")}
    model["names"][1].update(status="asserted", supersedes=["n-ada"])
    model["names"][0]["supersedes"] = ["n-ada-2"]
    assert codes(validate_extension(model)) == {"E_CLAIM_CYCLE"}


def test_coexisting_denotations_by_two_agents_and_two_certainties_stay_valid():
    model = package()
    model["denotations"].extend([
        claim(id="d-ada-b", agent="b", mention="m-ada", entity="e-bea", certainty="high"),
        claim(id="d-ada-low", mention="m-ada", entity="e-lyon", certainty="low")])
    result = validate_extension(model)
    assert result["valid"] and result["diagnostics"] == []
    listed = denotations_of(model, "m-ada")["denotations"]
    assert [item["id"] for item in listed] == ["d-ada", "d-ada-low", "d-ada-b"]
    assert [item["entity"] for item in listed] == ["e-ada", "e-lyon", "e-bea"]


def test_a_name_needs_no_mention_and_an_entity_needs_no_claim():
    model = package()
    model["entities"].append({"id": "e-nym", "label": "Unmentioned", "kind": "other"})
    model["names"].append(claim(id="n-nym", entity="e-nym", form="Lugdunum", language="la"))
    assert validate_extension(model)["valid"]
    model["names"] = []
    model["denotations"] = []
    model["statements"] = []
    assert codes(validate_extension(model)) == {"W_UNDENOTED"}
    assert validate_extension(model)["valid"]


def test_alignments_entail_nothing_between_two_entities_sharing_one_iri():
    model = package()
    shared = "https://example.org/ada"
    model["entities"][1]["alignments"] = [claim(id="al-bea", iri=shared, relation="exact")]
    result = validate_extension(model)
    assert result["valid"]
    assert len({item["id"] for item in model["entities"]}) == 3
    assert denotations_of(model, "m-ada")["denotations"][0]["entity"] == "e-ada"


def test_canonical_bytes_ignore_registry_order_but_keep_declared_distinctions():
    model = package()
    model["base"] = "https://example.org/package/"
    model["entities"][0]["alignments"].append(
        claim(id="al-ada-2", iri="https://example.org/ada2", relation="close"))
    model["denotations"].append(claim(id="d-ada-alt", mention="m-ada", entity="e-lyon"))
    model["denotations"].append(claim(id="d-ada-2", mention="m-ada", entity="e-bea",
                                      supersedes=["d-ada", "d-ada-alt"]))
    reordered = copy.deepcopy(model)
    for collection in (*COLLECTIONS, *NEW_COLLECTIONS):
        reordered[collection].reverse()
    reordered["readings"][0]["nodes"].reverse()
    reordered["statements"][0]["participants"].reverse()
    reordered["denotations"][0]["supersedes"].reverse()
    for entity in reordered["entities"]:
        entity.get("alignments", []).reverse()
    before = copy.deepcopy(reordered)
    assert equivalent(model, reordered)
    assert json.loads(canonical_bytes(model)) == json.loads(canonical_bytes(reordered))
    assert reordered == before
    assert canonical_bytes(model) == canonical_bytes(model)


@pytest.mark.parametrize("change", ["parts-order", "absent-optional", "role", "base", "language"])
def test_declared_distinctions_survive_canonical_comparison(change):
    left = package()
    left["names"][0]["parts"] = [{"kind": "forename", "form": "Ada"},
                                 {"kind": "surname", "form": "Byron"}]
    left["base"] = "https://example.org/package/"
    right = copy.deepcopy(left)
    if change == "parts-order":
        right["names"][0]["parts"].reverse()
    elif change == "absent-optional":
        del right["names"][0]["parts"]
    elif change == "role":
        right["statements"][0]["participants"][0]["role"] = "resident"
    elif change == "base":
        right["base"] = "https://example.org/package#"
    else:
        right["names"][0]["language"] = "en-GB"
    assert not equivalent(left, right)


def test_canonical_bytes_reject_an_invalid_package_and_do_not_mutate():
    model = package()
    before = copy.deepcopy(model)
    canonical_bytes(model)
    assert model == before
    model["entities"][0]["kind"] = "city"
    with pytest.raises(ValueError):
        canonical_bytes(model)


def test_denotations_of_reports_the_entity_and_hides_withdrawn_claims_by_default():
    model = package()
    model["denotations"].append(claim(id="d-ada-2", mention="m-ada", entity="e-bea",
                                      status="withdrawn", supersedes=["d-ada"]))
    before = copy.deepcopy(model)
    result = denotations_of(model, "m-ada")
    assert result == {"diagnostics": [], "denotations": []}
    result = denotations_of(model, "m-ada", include_withdrawn=True)
    assert [item["id"] for item in result["denotations"]] == ["d-ada-2"]
    assert result["denotations"][0]["label"] == "Bea" and result["denotations"][0]["kind"] == "person"
    result["denotations"][0]["label"] = "changed"
    assert model == before
    listed = denotations_of(model, "m-bea")["denotations"]
    assert [item["id"] for item in listed] == ["d-bea"]
    assert listed[0]["label"] == "Bea"


@pytest.mark.parametrize("target,code", [("e-ada", "E_MENTION"), ("absent", "E_MENTION"),
                                         (None, "E_MENTION"), ("r", "E_MENTION")])
def test_denotations_of_rejects_an_identifier_that_is_no_mention(target, code):
    result = denotations_of(package(), target)
    assert result == {"diagnostics": [{"code": code, "path": "/operation/mention"}],
                      "denotations": None}


def test_operations_return_validation_diagnostics_for_an_invalid_package():
    model = package()
    model["entities"][0]["kind"] = "city"
    expected = validate_extension(model)["diagnostics"]
    assert denotations_of(model, "m-ada") == {"diagnostics": expected, "denotations": None}
    assert names_of(model, "e-ada") == {"diagnostics": expected, "names": None}


def test_names_of_orders_by_validity_and_then_by_claim_id():
    model = package()
    model["names"] = [
        claim(id="n-4", entity="e-ada", form="Fourth", language="en", valid={"from": "1850-06"}),
        claim(id="n-2", entity="e-ada", form="Second", language="en", valid={"until": "1830"}),
        claim(id="n-1", entity="e-ada", form="First", language="en"),
        claim(id="n-5", entity="e-ada", form="Fifth", language="en", valid={"from": "1850-06-02"}),
        claim(id="n-3", entity="e-ada", form="Third", language="en",
              valid={"from": "1815", "until": "1852"}),
        claim(id="n-0", entity="e-ada", form="Zeroth", language="en"),
    ]
    before = copy.deepcopy(model)
    result = names_of(model, "e-ada")
    assert [item["id"] for item in result["names"]] == ["n-0", "n-1", "n-2", "n-3", "n-4", "n-5"]
    assert result["diagnostics"] == []
    result["names"][0]["form"] = "changed"
    assert model == before
    assert names_of(model, "e-bea")["names"] == []


def test_names_of_follows_supersession_and_shows_withdrawal_on_request():
    model = package()
    model["names"].append(claim(id="n-ada-2", entity="e-ada", form="Ada Lovelace", language="en",
                                supersedes=["n-ada"]))
    assert [item["id"] for item in names_of(model, "e-ada")["names"]] == ["n-ada-2"]
    model["names"].append(claim(id="n-ada-3", entity="e-ada", form="Ada Lovelace", language="en",
                                status="withdrawn", supersedes=["n-ada-2"]))
    assert names_of(model, "e-ada")["names"] == []
    assert [item["id"] for item in names_of(model, "e-ada", include_withdrawn=True)["names"]] == ["n-ada-3"]


@pytest.mark.parametrize("target", ["m-ada", "absent", None])
def test_names_of_rejects_an_identifier_that_is_no_entity(target):
    assert names_of(package(), target) == {
        "diagnostics": [{"code": "E_REFERENCE", "path": "/operation/entity"}], "names": None}


def test_claim_revision_rejects_a_removed_or_changed_claim_of_every_kind():
    before = package()
    after = copy.deepcopy(before)
    after["names"] = []
    assert check_claim_revision(before, after)["diagnostics"] == [
        {"code": "E_CLAIM_REWRITE", "path": "/before/names/0"}]
    after = copy.deepcopy(before)
    after["denotations"][1]["entity"] = "e-lyon"
    assert codes(check_claim_revision(before, after)) == {"E_CLAIM_REWRITE"}
    after = copy.deepcopy(before)
    after["entities"][0]["alignments"][0]["certainty"] = "low"
    assert codes(check_claim_revision(before, after)) == {"E_CLAIM_REWRITE"}
    after = copy.deepcopy(before)
    after["denotations"].append(claim(id="d-ada-2", mention="m-ada", entity="e-bea",
                                      supersedes=["d-ada"]))
    assert check_claim_revision(before, after)["valid"]


def test_claim_revision_keeps_the_v01_version_rewrite_check_and_reports_both_packages():
    before = package()
    after = copy.deepcopy(before)
    after["versions"][0] = version(content="Ada met Bea in Paris")
    assert codes(check_claim_revision(before, after)) == {"E_QUOTE"}
    after["selections"][2]["selector"]["segments"][0]["quote"] = "Pari"
    # The quote of the selection under a reading node changed together with the content.
    assert diagnostics(check_claim_revision(before, after)) == {
        ("E_VERSION_REWRITE", "/after/versions/0"), ("E_SELECTION_REWRITE", "/after/selections/2")}
    assert check_claim_revision(before, before)["valid"]
    assert not check_claim_revision(before, None)["valid"]


def test_public_operations_leave_their_inputs_unchanged():
    model = package()
    other = copy.deepcopy(model)
    before = copy.deepcopy(model)
    validate_extension(model)
    canonical_bytes(model)
    equivalent(model, other)
    check_claim_revision(model, other)
    denotations_of(model, "m-ada")
    names_of(model, "e-ada")
    assert model == before and other == before


def test_review_counterexamples_on_the_published_example_are_rejected():
    """Replay the recorded entity counterexamples of the 2026-09-07 review on the committed example."""
    before = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    kind = copy.deepcopy(before)
    kind["entities"][0]["kind"] = "other"
    moved = copy.deepcopy(before)
    source = next(i for i, item in enumerate(moved["concepts"]) if "alignments" in item)
    target = next(i for i, item in enumerate(moved["concepts"]) if i > source and "alignments" not in item)
    moved["concepts"][target]["alignments"] = moved["concepts"][source].pop("alignments")
    for after, expected in (
            (kind, {"code": "E_ENTITY_REWRITE", "path": "/after/entities/0/kind"}),
            (moved, {"code": "E_CLAIM_REWRITE", "path": f"/before/concepts/{source}/alignments/0"})):
        assert validate_extension(after)["valid"]
        assert check_claim_revision(before, after) == {"valid": False, "diagnostics": [expected]}
    assert check_claim_revision(before, copy.deepcopy(before)) == {"valid": True, "diagnostics": []}


def keep(model):
    return model


def free(model):
    """Add a selection that no record references."""
    model["selections"].append(selection("s-free", 4, 7))
    return model


def annotated(model):
    """Let an annotation claim select the added selection."""
    free(model)
    model["annotations"].append({"id": "an", "agent": "a", "selection": "s-free", "body": "Note"})
    return model


def cited(model):
    """Let a relation claim name the added selection directly as its endpoint."""
    free(model)
    model["concepts"].append({"id": "cites", "label": "Cites", "applies_to": "relation",
                              "definition": "The source claim cites the target selection."})
    model["relations"].append({"id": "rel", "agent": "a", "type": "cites",
                               "source": "st-residence", "target": "s-free"})
    return model


def carrying_spare(model):
    """Add an unreferenced entity that carries one alignment claim."""
    return spare(model, alignments=[claim(id="al-spare", iri="https://example.org/spare", relation="close")])


def moved_alignment(collection, index):
    """Move the alignment of Ada, record unchanged, onto another carrier."""
    def mutate(model):
        model[collection][index].setdefault("alignments", []).extend(model["entities"][0].pop("alignments"))
        return model
    return mutate


def recarried(model):
    """Replace the spare entity by a concept of the same ID carrying the same alignment."""
    entity = model["entities"].pop(3)
    model["concepts"].append({"id": entity["id"], "label": "Spare", "applies_to": "node",
                              "definition": "A spare concept.", "alignments": entity["alignments"]})
    return model


def extent(identifier, start, end):
    """Give a selection another range whose quote matches."""
    def mutate(model):
        record = next(item for item in model["selections"] if item["id"] == identifier)
        record["selector"] = selection(identifier, start, end)["selector"]
        return model
    return mutate


def requoted(model):
    """Select the same extent through a quotation policy instead of a range."""
    model["selections"][0]["selector"] = {"kind": "quote", "exact": "Ada", "match": "one"}
    return model


def equal_content_version(model):
    """Point the selection at an equal-content version under another ID, as in the dossier counterexample."""
    model["versions"].append(version("v2"))
    model["selections"][3]["version"] = "v2"
    return model


def two_alignments(model):
    model["entities"][0]["alignments"].append(
        claim(id="al-ada-2", iri="https://example.org/ada2", relation="close"))
    return model


def reordered(model):
    """Registry order and alignment order within a carrier carry no identity."""
    for collection in ("entities", "selections", "denotations"):
        model[collection].reverse()
    model["entities"][-1]["alignments"].reverse()
    return model


def nodes_reordered(model):
    """Node order inside a reading belongs to the exact claim record, although R11 ignores it."""
    model["readings"][0]["nodes"].reverse()
    return model


def extended(model):
    """Supersede, withdraw and add claims and records without touching earlier ones."""
    model["denotations"].append(claim(id="d-ada-2", mention="m-ada", entity="e-bea", supersedes=["d-ada"]))
    model["names"].append(claim(id="n-ada-2", entity="e-ada", form="Ada", language="en",
                                status="withdrawn", supersedes=["n-ada"]))
    two_alignments(model)
    model["entities"].append({"id": "e-meeting", "label": "Meeting", "kind": "event"})
    model["selections"].append(selection("s-met", 4, 7))
    model["annotations"].append({"id": "an-met", "agent": "b", "selection": "s-met", "body": "Event",
                                 "concept": "en-referring-string"})
    model["denotations"].append(claim(id="d-met", agent="b", mention="an-met", entity="e-meeting"))
    return model


def relabeled(model):
    """Labels and local concept definitions stay deliberately revisable."""
    model["entities"][0]["label"] = "Ada Lovelace"
    model["agents"][0]["label"] = "Editor A."
    model["concepts"][3].update(label="Dwelling", definition="Where an entity dwells.")
    return model


MOVED_ALIGNMENT = {("E_CLAIM_REWRITE", "/before/entities/0/alignments/0")}
REVISIONS = {
    "alignment-to-another-entity": (keep, moved_alignment("entities", 1), MOVED_ALIGNMENT),
    "alignment-to-a-concept": (keep, moved_alignment("concepts", 3), MOVED_ALIGNMENT),
    "alignment-to-an-agent": (keep, moved_alignment("agents", 0), MOVED_ALIGNMENT),
    "alignment-carrier-collection": (carrying_spare, recarried,
                                     {("E_CLAIM_REWRITE", "/before/entities/3/alignments/0")}),
    "entity-kind-referenced": (keep, lambda m: assign(m, ("entities", 0, "kind"), "group"),
                               {("E_ENTITY_REWRITE", "/after/entities/0/kind")}),
    "entity-kind-unreferenced": (spare, lambda m: assign(m, ("entities", 3, "kind"), "place"),
                                 {("E_ENTITY_REWRITE", "/after/entities/3/kind")}),
    "node-selection-extent": (keep, extent("s-ada", 0, 2), {("E_SELECTION_REWRITE", "/after/selections/0")}),
    "node-selection-policy": (keep, requoted, {("E_SELECTION_REWRITE", "/after/selections/0")}),
    "annotation-selection": (annotated, extent("s-free", 8, 11),
                             {("E_SELECTION_REWRITE", "/after/selections/3")}),
    "relation-selection-version": (cited, equal_content_version,
                                   {("E_SELECTION_REWRITE", "/after/selections/3")}),
    "unreferenced-selection-revised": (free, extent("s-free", 8, 11), set()),
    "unreferenced-selection-removed": (free, lambda m: assign(m, ("selections",), m["selections"][:3]), set()),
    "unreferenced-entity-removed": (spare, lambda m: assign(m, ("entities",), m["entities"][:3]), set()),
    "reordered-records": (two_alignments, reordered, set()),
    "node-order-inside-a-reading": (keep, nodes_reordered, {("E_CLAIM_REWRITE", "/before/readings/0")}),
    "supersession-and-additions": (keep, extended, set()),
    "labels-and-definitions": (keep, relabeled, set()),
}


@pytest.mark.parametrize("name", sorted(REVISIONS))
def test_claim_revision_keeps_what_earlier_claims_depend_on(name):
    prepare, mutate, expected = REVISIONS[name]
    before = prepare(package())
    after = mutate(copy.deepcopy(before))
    assert validate_extension(before)["valid"] and validate_extension(after)["valid"]
    frozen = copy.deepcopy([before, after])
    result = check_claim_revision(before, after)
    assert diagnostics(result) == expected
    assert result["valid"] == (not expected)
    assert [before, after] == frozen


def anonymous(model):
    del model["entities"][0]["id"]
    return model


DAMAGED = {
    "none": lambda m: None,
    "list": lambda m: [],
    "empty": lambda m: {},
    "entities-not-list": lambda m: assign(m, ("entities",), 5),
    "entity-not-record": lambda m: assign(m, ("entities", 0), 5),
    "entity-without-id": anonymous,
    "entity-id-unhashable": lambda m: assign(m, ("entities", 0, "id"), ["e-ada"]),
    "alignments-not-list": lambda m: assign(m, ("entities", 0, "alignments"), "al-ada"),
    "alignment-id-unhashable": lambda m: assign(m, ("entities", 0, "alignments", 0, "id"), ["al-ada"]),
    "selector-missing": lambda m: assign(m, ("selections", 0, "selector"), None),
    "nodes-missing": lambda m: assign(m, ("readings", 0, "nodes"), None),
}


@pytest.mark.parametrize("side", ["before", "after"])
@pytest.mark.parametrize("name", sorted(DAMAGED))
def test_claim_revision_fails_safely_on_a_malformed_package(name, side):
    """Nothing raises, and no dependency rewrite is inferred from an invalid package."""
    damaged = DAMAGED[name](package())
    frozen = copy.deepcopy(damaged)
    result = check_claim_revision(*((damaged, package()) if side == "before" else (package(), damaged)))
    assert not result["valid"]
    assert all(item["path"].startswith(("/before", "/after")) for item in result["diagnostics"])
    assert {code for code in codes(result) if code.endswith("_REWRITE")} <= (
        {"E_CLAIM_REWRITE"} if side == "after" else set())
    assert damaged == frozen
