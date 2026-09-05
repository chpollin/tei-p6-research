"""Independent fidelity checks for the actual comparison catalogue.

These checks exercise the published examples, not a mocked page fixture.
P5 fragments remain authored illustrations; parsing is not ODD validation.
"""
import copy
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

from tools.models.abstract_text import COLLECTIONS, equivalent, validate_model
from tools.models.bindings import decode_model
from tools.sitegen import comparison_view as comparisons


ROOT = Path(__file__).resolve().parents[1]
CASE_IDS = {
    "overlap", "discontinuous", "ambiguous-target", "identity-reanchoring",
    "equal-extents", "editorial-notes", "page-foliation",
}
REAL_CASES = {
    "equal-extents": "case-1-hierarchy",
    "editorial-notes": "case-2-interrupted-heading",
    "page-foliation": "case-3-holdout-media",
}


@pytest.fixture(scope="module")
def catalogue():
    return comparisons.build_comparisons(ROOT)


def by_id(catalogue):
    return {case["id"]: case for case in catalogue["cases"]}


def records(package):
    for collection in COLLECTIONS:
        yield from package[collection]
    for reading in package["readings"]:
        yield from reading["nodes"]


def test_all_declared_examples_exist_once(catalogue):
    assert {case["id"] for case in catalogue["cases"]} == CASE_IDS
    assert len(catalogue["cases"]) == len(CASE_IDS)


@pytest.mark.parametrize("identifier", sorted(CASE_IDS - {"page-foliation"}))
def test_every_binding_contains_the_same_valid_model_and_displayed_text(catalogue, identifier):
    case = by_id(catalogue)[identifier]
    payloads = case["candidate"]["serializations"]
    assert set(payloads) == {"json", "xml", "yaml"}
    packages = [decode_model(payload, binding) for binding, payload in payloads.items()]
    for package in packages:
        assert validate_model(package)["valid"]
        assert equivalent(packages[0], package)
        assert case["primary_text"] in [version["content"] for version in package["versions"]]
        assert case["candidate"]["validation"] == validate_model(package)
        for version in package["versions"]:
            assert version["sha256"] == hashlib.sha256(version["content"].encode("utf-8")).hexdigest()


def test_crossing_intervals_really_select_the_claimed_german_words(catalogue):
    case = by_id(catalogue)["overlap"]
    model = decode_model(case["candidate"]["serializations"]["json"], "json")
    assert model["versions"][0]["content"] == "Der alte Baum steht."
    intervals = [selection["selector"]["segments"][0] for selection in model["selections"]]
    assert {(part["start"], part["end"], part["quote"]) for part in intervals} == {
        (0, 13, "Der alte Baum"), (9, 20, "Baum steht."),
    }
    assert len({reading["agent"] for reading in model["readings"]}) == 2
    assert not model["relations"]  # Coexisting structures need not disagree.


@pytest.mark.parametrize("identifier", sorted(REAL_CASES))
def test_real_xml_is_the_exact_admitted_fragment(catalogue, identifier):
    source_cases = json.loads((ROOT / "experiments/editorial_cases/cases.json").read_text(encoding="utf-8"))
    original = next(case for case in source_cases["cases"] if case["case_id"] == REAL_CASES[identifier])
    case = by_id(catalogue)[identifier]
    assert len(case["p5"]) == 1
    assert case["p5"][0]["xml"] == original["original_xml"]
    assert case["primary_text"] == original["primary_text"]
    assert "CC BY-SA 4.0" in case["p5"][0]["notes"]
    assert "7d174637d0b2cf56edaacac3b5e7e283e8ba8245" in json.dumps(case["p5"][0]["sources"])
    source_urls = [source["url"] for source in case["p5"][0]["sources"]]
    assert any(url.endswith(f'#L{original["start_line"]}-L{original["end_line"]}') for url in source_urls)
    assert any(url.startswith("knowledge.html#doc-30-assertions-humboldt-") for url in source_urls)


def test_holdout_refusal_never_claims_a_model_serialization_or_instance_graph(catalogue):
    case = by_id(catalogue)["page-foliation"]
    assert not case["candidate"]["validation"]["valid"]
    assert case["candidate"]["validation"]["diagnostics"]
    assert not case["candidate"]["serializations"]
    assert not case["graph"]["nodes"] and not case["graph"]["edges"]
    assert "not a successful migration" in case["candidate"]["notes"]
    assert "tei-fragment-0.1" not in " ".join(case["formal"] + case["limits"])


def test_note_relationship_explanation_matches_the_actual_metadata_binding(catalogue):
    case = by_id(catalogue)["editorial-notes"]
    package = decode_model(case["candidate"]["serializations"]["json"], "json")
    assert package["relations"] == []
    bodies = [json.loads(annotation["body"]) for annotation in package["annotations"]]
    notes = [body for body in bodies if body["kind"] == "note"]
    assert len(notes) == 2
    assert all(body["binding"] == "tei-fragment-0.1" for body in notes)
    assert any(body["parent"] in {note["element"] for note in notes} for body in notes)
    explanation = " ".join(case["formal"])
    assert "annotation bodies" in explanation and "tei-fragment-0.1" in explanation
    assert "not core Relation records" in explanation
    assert "not shown as relationships in the core instance diagram" in explanation


def test_p5_illustrations_are_namespace_bound_and_link_pinned_primary_specs(catalogue):
    for case in catalogue["cases"]:
        for variant in case["p5"]:
            tree = ET.fromstring(f'<examples xmlns="{comparisons.TEI}">{variant["xml"]}</examples>')
            assert all(element.tag.startswith("{" + comparisons.TEI + "}") for element in tree.iter())
            if case["id"] not in REAL_CASES:
                assert "illustration" in variant["status"] and "no full ODD" in variant["status"]
                assert variant["sources"]
                assert all(comparisons.P5_COMMIT in source["url"] for source in variant["sources"])


def test_instance_graph_contains_every_identified_core_object_and_reference():
    # This fixture includes relations, concepts and technical lineage even when
    # a particular rendered example happens not to use all three.
    package = json.loads((ROOT / "experiments/abstract_text_v01/examples/competing-readings.json").read_text(encoding="utf-8"))
    derived = copy.deepcopy(package["versions"][0])
    derived.update(id="derived", parents=["v1"])
    package["versions"].append(derived)
    assert validate_model(package)["valid"]
    graph = comparisons.graph_for(package)
    graph_ids = {node["id"] for node in graph["nodes"]}
    assert graph_ids == {record["id"] for record in records(package)}
    edges = {(edge["source"], edge["target"]) for edge in graph["edges"]}
    for record in records(package):
        for field in ("version", "agent", "selection", "text", "type", "source", "target", "parent"):
            if field in record and record[field] is not None:
                assert (record["id"], record[field]) in edges, (record["id"], field)
        for target in record.get("parents", []) + record.get("versions", []):
            assert (record["id"], target) in edges
    assert all(source in graph_ids and target in graph_ids for source, target in edges)


@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate"])
def test_incomplete_or_duplicate_editorial_input_cannot_silently_truncate(monkeypatch, mutation):
    original_reader = comparisons.read_json

    def read(root, path):
        data = original_reader(root, path)
        if path == "experiments/editorial_cases/cases.json":
            if mutation == "missing":
                data["cases"].pop()
            elif mutation == "extra":
                data["cases"].append({**data["cases"][0], "case_id": "unexpected"})
            else:
                data["cases"][1] = copy.deepcopy(data["cases"][0])
        return data

    monkeypatch.setattr(comparisons, "read_json", read)
    with pytest.raises(ValueError):
        comparisons.build_comparisons(ROOT)


def test_editorial_case_order_cannot_change_which_case_is_the_holdout(monkeypatch):
    original_reader = comparisons.read_json

    def read(root, path):
        data = original_reader(root, path)
        if path == "experiments/editorial_cases/cases.json":
            data["cases"].reverse()
        return data

    monkeypatch.setattr(comparisons, "read_json", read)
    try:
        result = comparisons.build_comparisons(ROOT)
    except ValueError:
        return  # Rejecting reordered controlled input is also safe.
    cases = by_id(result)
    assert not cases["page-foliation"]["candidate"]["serializations"]
    assert cases["equal-extents"]["candidate"]["serializations"]


def test_changed_holdout_role_cannot_be_published_as_the_original_study(monkeypatch):
    original_reader = comparisons.read_json

    def read(root, path):
        data = original_reader(root, path)
        if path == "experiments/editorial_cases/cases.json":
            data["cases"][-1]["holdout"] = False
        return data

    monkeypatch.setattr(comparisons, "read_json", read)
    with pytest.raises(ValueError, match="holdout"):
        comparisons.build_comparisons(ROOT)


def test_missing_required_source_input_fails_closed(tmp_path):
    with pytest.raises(FileNotFoundError):
        comparisons.build_comparisons(tmp_path)


def test_source_fragment_drift_fails_before_display(monkeypatch):
    original_reader = comparisons.read_json

    def read(root, path):
        data = original_reader(root, path)
        if path == "experiments/editorial_cases/cases.json":
            data["cases"][0]["original_xml"] += " "
        return data

    monkeypatch.setattr(comparisons, "read_json", read)
    with pytest.raises(ValueError, match="source drift"):
        comparisons.build_comparisons(ROOT)


def test_build_does_not_mutate_model_or_editorial_inputs(monkeypatch):
    original_reader = comparisons.read_json
    inputs = {}

    def read(root, path):
        if path not in inputs:
            inputs[path] = original_reader(root, path)
        return inputs[path]

    monkeypatch.setattr(comparisons, "read_json", read)
    first = comparisons.build_comparisons(ROOT)
    snapshot = copy.deepcopy(inputs)
    second = comparisons.build_comparisons(ROOT)
    assert inputs == snapshot
    assert first == second
