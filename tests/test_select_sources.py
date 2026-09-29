"""Declared selection queries reproduce recorded runs and expose their gaps."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest

from tools import select_sources
from tools.select_sources import STREAMS, select

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/retrieval"
# Declared expressions of workbench/selections/2026-09-06-text-and-document-structures-run1.md.
B = {
    "B1": r"overlap|hierarch|concurrent|OHCO",
    "B2": r"milestone|\bpb\b|\blb\b|\bcb\b|\bgb\b|page ?break|line ?break|column ?break|\bfw\b|foliation|att\.breaking|@break",
    "B3": r"fragmentable|@part\b|\bjoin\b|joinGrp|discontinu|@next|@prev|aggregat",
    "B4": r"stand-?off|listAnnotation|\bannotation\b|\bspan\b|spanGrp|\banchor\b|att\.spanning|spanTo|xpointer|@target",
    "B5": r"floatingText|sourceDoc|\bzone\b|\bsurface\b|<line>|facsimile|@facs|embedded transcription|documentary|genetic",
    "B6": r"<div>|<ab>|<seg>|<p>|<head>|<body>|<text>|<group>|<front>|<back>|<note>|att\.divLike|content model of div|\bstructures?\b",
}
TEI_L = (r"overlap|hierarch|structure|page|milestone|stand-?off|interlinear|support|\bdiv\b|\bp\b|\bseg\b|\bnote\b"
         r"|facsimile|zone|surface|dictionary-entries|damage")


def test_kind_filter_counts_issue_1505_once() -> None:
    result = select(FIXTURE, [{"id": "pointers", "stream": "github", "pattern": "next and prev"}])
    query = result["queries"][0]
    assert [match["identity"] for match in query["matches"]] == ["github:TEIC/TEI:issue:1505", "github:TEIC/TEI:pr:1600"]
    info = result["snapshot"]["streams"]["github"]
    assert (info["records_total"], info["records_of_kind"], info["record_kind"]) == (11, 4, "work-item-detail")
    issue = query["matches"][0]
    assert issue["relations"] == {"status": "recorded", "manifest": STREAMS["github-relations"].manifest,
                                  "items": [{"relation": "cross-referenced", "target_number": 1600,
                                             "target_node_id": "PR_1600", "created_at": "2017-05-01T00:00:00Z"}],
                                  "untargeted_events": 1}
    assert issue["duplicate_identity"] is False and query["declaration"]["ignore_case"] is True


def test_snapshot_hashes_and_control_plane_gaps() -> None:
    result = select(FIXTURE, [{"stream": "github", "label": "Status: Reconsider for P6"},
                              {"stream": "sourceforge", "pattern": "migrated"},
                              {"stream": "tei-l", "pattern": "next"}])
    streams = result["snapshot"]["streams"]
    records = (FIXTURE / STREAMS["github"].records).read_bytes()
    assert streams["github"]["records_sha256"] == hashlib.sha256(records).hexdigest()
    assert streams["github"]["manifest_status"] == "partial"
    assert streams["github"]["manifest_run_id"] == "2026-09-06-github-teic-tei-work-items"
    assert streams["github"]["manifest_listed_in_lock"] is True
    codes = {(gap["stream"], gap["code"]) for gap in result["snapshot"]["gaps"]}
    assert {("github", "run-not-complete"), ("sourceforge", "manifest-not-listed-in-lock"),
            ("tei-l", "raw-availability-unknown")} <= codes
    reconsider, tickets, messages = result["queries"]
    assert [match["number"] for match in reconsider["matches"]] == [1400] and reconsider["id"] == "q1"
    ticket = tickets["matches"][0]
    assert ticket["identity"] == "sourceforge:tei:bugs:8" and ticket["migration"]["status"] == "unknown"
    assert "reported_by" not in ticket and ticket["raw_availability"] == "unknown"
    assert messages["count"] == 2
    assert messages["subject_groups"] == [{"subject_key": "question on next and prev", "messages": 2, "months": ["2601"]}]
    assert "raw-body-sentinel" not in json.dumps(result).casefold()


def test_missing_stream_and_duplicate_ids_are_gaps(tmp_path: Path) -> None:
    root = tmp_path / "root"
    shutil.copytree(FIXTURE, root)
    (root / STREAMS["tei-l"].records).unlink()
    stream = root / STREAMS["github"].records
    text = stream.read_text(encoding="utf-8")
    detail = next(line for line in text.splitlines() if "work-item-detail" in line and "1505" in line)
    stream.write_text(text + detail + "\n", encoding="utf-8", newline="\n")
    result = select(root, [{"stream": "tei-l", "pattern": "next"}, {"stream": "github", "pattern": "next and prev"}])
    missing, github = result["queries"]
    assert (missing["count"], missing["matches"]) == (None, None)
    assert missing["gaps"][0]["code"] == "stream-missing"
    duplicates = [gap for gap in result["snapshot"]["gaps"] if gap["code"] == "duplicate-upstream-id"]
    assert {gap["identity"] for gap in duplicates} == {"node_id", "number"}
    assert [(match["number"], match["duplicate_identity"]) for match in github["matches"]] == [
        (1505, True), (1600, False), (1505, True)]


def test_selection_checks_stream_bytes_against_the_manifest(tmp_path: Path) -> None:
    root = tmp_path / "root"
    shutil.copytree(FIXTURE, root)
    stream = STREAMS["github"]
    records = root / stream.records
    manifest = root / stream.manifest
    digest = hashlib.sha256(records.read_bytes()).hexdigest()
    manifest.write_text(manifest.read_text(encoding="utf-8")
                        + f"objects:\n- path: {stream.records}\n  sha256: {digest}\n", encoding="utf-8")
    query = [{"stream": "github", "pattern": "next"}]
    first = select(root, query)
    assert first["snapshot"]["streams"]["github"]["records_sha256_matches_manifest"] is True
    records.write_bytes(records.read_bytes() + b"\n")
    changed = select(root, query)
    assert changed["snapshot"]["streams"]["github"]["records_sha256_matches_manifest"] is False
    assert any(gap["code"] == "stream-hash-mismatch" for gap in changed["snapshot"]["gaps"])


def test_atlas_lookups_respect_declared_kinds() -> None:
    result = select(FIXTURE, [{"stream": "atlas", "member_of": "att.fragment"},
                              {"stream": "atlas", "attribute": "part"},
                              {"stream": "atlas", "ident": "p", "category": "classSpec"},
                              {"stream": "atlas", "member_of": "p"},
                              {"stream": "atlas", "member_of": "att.missing"}])
    members, attribute, wrong_kind, not_class, undeclared = result["queries"]
    assert [match["ident"] for match in members["matches"]] == ["ab", "p"]
    assert attribute["matches"][0]["attribute_locators"] == ["/classSpec[1]/attList[1]/attDef[1]"]
    assert wrong_kind["count"] == 0
    assert not_class["count"] == 1 and not_class["gaps"][0]["code"] == "membership-target-not-a-class"
    assert undeclared["count"] == 0 and undeclared["gaps"][0]["code"] == "membership-target-not-declared"
    assert result["snapshot"]["streams"]["atlas"]["declared_manifest_sha256_matches"] is True


@pytest.mark.parametrize("query", [
    {"stream": "github"},
    {"stream": "github", "pattern": "x", "label": "y"},
    {"stream": "tei-l", "label": "x"},
    {"stream": "github", "field": "body", "pattern": "x"},
    {"stream": "atlas", "ident": "p", "attribute": "q"},
    {"stream": "raw", "pattern": "x"},
    {"stream": "github", "pattern": "("},
    {"stream": "github", "pattern": "x", "admit": True},
])
def test_undeclared_query_shapes_fail(query: dict) -> None:
    with pytest.raises(ValueError):
        select(FIXTURE, [query])


def test_cli_records_the_declaration(tmp_path: Path) -> None:
    queries = tmp_path / "queries.yaml"
    queries.write_text("queries:\n  - id: pointers\n    stream: github\n    pattern: next and prev\n", encoding="utf-8")
    output = tmp_path / "selection.json"
    arguments = ["--root", str(FIXTURE), "--queries", str(queries), "--atlas-member", "att.fragment", "--output", str(output)]
    assert select_sources.main(arguments) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert [query["id"] for query in payload["queries"]] == ["pointers", "atlas-member-1"]
    assert payload["declaration"]["sha256"] == hashlib.sha256(queries.read_bytes()).hexdigest()
    assert payload["use"].startswith("selection candidates")


@pytest.fixture(scope="module")
def recorded() -> dict:
    queries = [{"id": name, "stream": "github", "pattern": pattern} for name, pattern in B.items()]
    queries += [{"id": f"SF-{name}", "stream": "sourceforge", "pattern": pattern} for name, pattern in B.items()]
    queries += [{"id": "reconsider", "stream": "github", "label": "Status: Reconsider for P6"},
                {"id": "wontfix", "stream": "github", "label": "Status: Wontfix"},
                {"id": "tei-l", "stream": "tei-l", "pattern": TEI_L},
                {"id": "fragmentable", "stream": "atlas", "member_of": "att.fragmentable"},
                {"id": "part", "stream": "atlas", "attribute": "part"},
                {"id": "target", "stream": "atlas", "attribute": "target"}]
    return select(ROOT, queries)


def test_recorded_selection_counts_reproduce(recorded: dict) -> None:
    """Counts of the 2026-09-06 selection records on the tracked snapshot."""
    queries = {query["id"]: query for query in recorded["queries"]}
    assert {name: queries[name]["count"] for name in ("B2", "B6", "reconsider", "wontfix")} == {
        "B2": 29, "B6": 50, "reconsider": 17, "wontfix": 32}
    assert [queries[f"B{n}"]["count"] for n in range(1, 7)] == [5, 29, 8, 48, 46, 50]
    assert [queries[f"SF-B{n}"]["count"] for n in range(1, 7)] == [3, 19, 3, 19, 20, 27]
    assert (queries["tei-l"]["count"], len(queries["tei-l"]["subject_groups"])) == (55, 8)
    assert [match["ident"] for match in queries["fragmentable"]["matches"]] == [
        "ab", "att.divLike", "att.segLike", "l", "p", "post"]
    assert [match["ident"] for match in queries["part"]["matches"]] == ["att.fragmentable"]
    assert queries["target"]["count"] == 13
    b3 = [match["identity"] for match in queries["B3"]["matches"]]
    assert b3.count("github:TEIC/TEI:issue:1505") == 1 and len(b3) == len(set(b3))
    github = recorded["snapshot"]["streams"]["github"]
    assert github["record_kind"] == "work-item-detail"
    assert github["manifest_run_id"] == "2026-09-06-github-teic-tei-work-items"
    assert len(github["records_sha256"]) == len(github["manifest_sha256"]) == 64
    assert all(match["migration"]["status"] == "unknown" for n in range(1, 7) for match in queries[f"SF-B{n}"]["matches"])
