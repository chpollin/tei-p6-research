"""Unit checks for the entity extension 0.2; independent case expectations live elsewhere."""

import copy
import hashlib
import json

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
    assert covered | {"E_CLAIM_REWRITE"} >= set(EXTENSION_DIAGNOSTICS)
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
    assert codes(check_claim_revision(before, after)) == {"E_VERSION_REWRITE"}
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
