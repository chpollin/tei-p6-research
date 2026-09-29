"""Retrieval routes agents to tracked artifacts without inventing answers or evidence.

The fixture vault is fictional. The repository benchmark fixes routing
expectations with explicit top-k limits; it checks lexical routing only and
accepts no research result.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from tools import retrieval
from tools.retrieval import build_index, search

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/retrieval"
FRAGMENT = "10_markdown/documents/fixture-att.fragment-9.9.0.md"
DISTILLATE = "20_distillates/documents/fixture-att.fragment-9.9.0.md"
PUBLICATION = "20_distillates/publications/fixture-issue-7.md"
RELEASE_MANIFEST = "sources/manifests/2026-01-01-fixture-release-admission.yaml"
REUSE_MANIFEST = "sources/manifests/2026-01-02-fixture-release-readmission.yaml"


@pytest.fixture(scope="module")
def index() -> dict:
    return build_index(FIXTURE)


def record(index: dict, path: str) -> dict:
    return next(item for item in index["records"] if item["path"] == path)


def paths(results: list[dict]) -> list[str]:
    return [result["path"] for result in results]


def test_exact_ident_and_declared_attribute_rank_first(index: dict) -> None:
    top = search(index, "att.fragment")[0]
    assert top["path"] == FRAGMENT and top["reasons"][0] == "exact-ident:att.fragment"
    attribute = search(index, "@part")
    assert attribute[0]["path"] == FRAGMENT and "declares-attribute:part" in attribute[0]["reasons"]
    assert [result["rank"] for result in attribute] == list(range(1, len(attribute) + 1))
    passage = attribute[0]["passages"][0]
    assert passage["locator"] == f"{FRAGMENT}#^b2" and "part" in passage["matched_terms"]


def test_ties_follow_score_kind_and_path(index: dict) -> None:
    results = search(index, "fragment", limit=50)
    keys = [(-result["score"], retrieval.KIND_ORDER.index(result["kind"]), result["path"]) for result in results]
    assert keys == sorted(keys) and len(results) == len(set(paths(results)))


def test_release_and_proposal_records_stay_distinct(index: dict) -> None:
    release = search(index, "fragment", authority="primary-normative")
    assert FRAGMENT in paths(release) and DISTILLATE in paths(release)
    assert not any(path.startswith("knowledge/") for path in paths(release))
    proposal = search(index, "fragment", authority="project-proposal")
    assert paths(proposal) == ["knowledge/model-design.md"]
    assert proposal[0]["source"] is None and proposal[0]["evidence_chain"] is False
    kinds = {result["kind"] for result in search(index, "fragment", layer="knowledge")}
    assert kinds == {"project-contract", "project-proposal"}


def test_authority_is_never_inferred_from_a_file_name(index: dict) -> None:
    note = record(index, "10_markdown/documents/fixture-normative-guidelines-9.9.0.md")
    assert note["source"] is None and note["authorities"] == [] and note["versions"] == []
    assert any(gap["field"] == "source" for gap in note["gaps"])
    assert note["path"] in paths(search(index, "normative guidelines"))
    assert note["path"] not in paths(search(index, "normative guidelines", authority="primary-normative"))
    test_document = record(index, "10_markdown/documents/fixture-test-document-9.9.0.md")["source"]
    assert test_document["family_authority"] == "primary-normative"
    assert test_document["admission_authority"].endswith("not a normative specification")


def test_effective_provenance_follows_the_reuse_chain(index: dict) -> None:
    fragment = record(index, FRAGMENT)
    source = fragment["source"]
    assert source["admission_manifest"] == RELEASE_MANIFEST
    assert source["manifest_chain"] == [RELEASE_MANIFEST, REUSE_MANIFEST]
    assert (source["version"], source["commit"]) == ("9.9.0", "9" * 40)
    assert source["representation_sha256"] == fragment["file_sha256"] and fragment["gaps"] == []
    assert fragment["direct_links"] == [{"relation": "represents-local-original", "anchor": None,
                                         "path": "00_sources/fixture-att.fragment-9.9.0.xml"}]
    distillate = record(index, DISTILLATE)
    assert distillate["source"] is None and distillate["versions"] == ["9.9.0", "9" * 40]
    assert distillate["direct_links"] == [{"relation": "distills", "path": FRAGMENT, "anchor": None}]
    assert distillate["passages"][0]["cites"] == [f"{FRAGMENT}#^b1"]
    publication = record(index, PUBLICATION)
    assert publication["source"]["reference_id"] == "fixture-issue-7"
    assert publication["source"]["snapshots"] == [{"part": "issue-body", "sha256": "3" * 64,
                                                   "observed_at": "2026-01-04T00:00:00Z"}]
    assert publication["authorities"] == ["mixed-process-record"] and publication["versions"] == []
    assert RELEASE_MANIFEST in index["inputs"]
    assert "sources/manifests/2026-09-06-github-teic-tei-work-items.yaml" not in index["inputs"]


@pytest.mark.parametrize("kind", ["git-blob", "discussion"])
def test_only_an_explicit_git_blob_record_supplies_a_pinned_version(tmp_path, kind):
    import yaml

    root = tmp_path / "repo"
    shutil.copytree(FIXTURE, root)
    path = root / "sources/manifests/2026-01-04-fixture-citations.yaml"
    manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
    manifest["admissions"][0]["record"] = {
        "kind": kind, "commit": "a" * 40, "last_changing_commit": "b" * 40,
        "path": "slides.html", "blob": "c" * 40,
    }
    path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
    current = build_index(root)
    publication = record(current, PUBLICATION)
    assert publication["versions"] == (["a" * 40] if kind == "git-blob" else [])
    assert publication["source"]["git_path"] == ("slides.html" if kind == "git-blob" else None)
    assert bool(search(current, "issue", version="a" * 40)) == (kind == "git-blob")
    assert search(current, "issue", version="b" * 40) == []


def test_curated_topics_stay_apart_from_rule_suggestions(index: dict) -> None:
    fragment = record(index, FRAGMENT)
    assert fragment["topics"] == {
        "curated": [{"topic": "Fixture Structures", "basis": "distillate-topics", "distillate": DISTILLATE}],
        "suggested": [{"topic": "Fixture Issues", "rule": "declared-module:fixture", "projection": retrieval.NAVIGATION}],
    }
    assert fragment["ident"] == "att.fragment" and fragment["attributes"] == ["part"]
    assert fragment["navigation"]["projection"] == retrieval.NAVIGATION
    assert FRAGMENT in paths(search(index, "fragment", topic="Fixture Issues"))
    assert FRAGMENT in paths(search(index, "fragment", topic="[[MOC-Fixture Structures]]"))


def test_validated_filter_is_strict_and_contested_links_surface(index: dict) -> None:
    unreviewed = "30_assertions/fixture-fragment-part-without-review.md"
    validated = paths(search(index, "fragment", status="validated"))
    assert "30_assertions/fixture-fragment-class-marks-fragments.md" in validated
    assert unreviewed not in validated and unreviewed in paths(search(index, "fragment", layer="assertion"))
    same = search(index, "pointers same type", layer="assertion")[0]
    assert same["path"] == "30_assertions/fixture-fragment-pointers-same-type.md"
    assert same["contested_with"] == [{"path": "30_assertions/fixture-fragment-pointers-any-type.md",
                                       "title": "Fixture release 9.9.0 states no type restriction for fragment pointers",
                                       "status": "contested", "indexed": True}]
    assert same["direct_links"] == [{"relation": "grounding", "path": PUBLICATION, "anchor": "s1"}]
    assert search(index, "pointers", status="validated") == []


def test_unknown_and_invalid_queries_return_nothing_or_fail(index: dict) -> None:
    assert search(index, "zzqx-unindexed-term") == []
    assert search(index, "the of") == []
    for filters in ({"status": "accepted"}, {"layer": "50_answers"}, {"limit": 0}):
        with pytest.raises(ValueError):
            search(index, "fragment", **filters)
    with pytest.raises(ValueError, match="Empty query"):
        search(index, "   ")


def test_serialized_index_holds_no_raw_or_complete_body(index: dict) -> None:
    assert "RAW-ORIGINAL-SENTINEL" in (FIXTURE / "00_sources/fixture-att.fragment-9.9.0.xml").read_text(encoding="utf-8")
    assert "COMPLETE-XML-SENTINEL" in (FIXTURE / FRAGMENT).read_text(encoding="utf-8")
    text = json.dumps(index, ensure_ascii=False).casefold()
    for sentinel in ("raw-original-sentinel", "raw-body-sentinel", "complete-xml-sentinel"):
        assert sentinel not in text
    passages = [passage for item in index["records"] for passage in item["passages"]]
    assert passages and all(len(passage["snippet"]) <= retrieval.SNIPPET for passage in passages)
    assert index["use"] == "navigation-only; never grounding"
    assert index["scope"]["never_opened"] == ["00_sources", "corpus/raw"]
    assert all("grounding" not in item for item in index["records"])


def test_rebuild_is_deterministic_and_absent_navigation_stays_unknown(index: dict, tmp_path: Path) -> None:
    assert json.dumps(build_index(FIXTURE), sort_keys=True) == json.dumps(index, sort_keys=True)
    root = tmp_path / "root"
    shutil.copytree(FIXTURE, root)
    (root / retrieval.NAVIGATION).unlink()
    reduced = build_index(root)
    assert any(gap["path"] == retrieval.NAVIGATION for gap in reduced["gaps"])
    fragment = record(reduced, FRAGMENT)
    assert fragment["ident"] is None and fragment["topics"]["suggested"] == [] and fragment["topics"]["curated"]
    reasons = [reason for result in search(reduced, "att.fragment") for reason in result["reasons"]]
    assert not any(reason.startswith("exact-ident") for reason in reasons)


def test_admission_manifests_are_parsed_once(monkeypatch: pytest.MonkeyPatch) -> None:
    parsed = []
    original = retrieval._load_yaml
    monkeypatch.setattr(retrieval, "_load_yaml", lambda data: parsed.append(data) or original(data))
    built = build_index(FIXTURE)
    yaml_inputs = [path for path in built["inputs"] if path.endswith(".yaml")]
    assert len(parsed) == len(yaml_inputs) == len(set(parsed)) == 5


def test_cli_json_and_explicit_index_output(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    output = tmp_path / "index.json"
    arguments = ["@part", "--root", str(FIXTURE), "--json", "--limit", "2", "--index-output", str(output)]
    assert retrieval.main(arguments) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["results"][0]["path"] == FRAGMENT and len(payload["results"]) <= 2
    assert payload["use"] == "navigation-only; never grounding"
    assert json.loads(output.read_text(encoding="utf-8"))["generator"] == retrieval.GENERATOR
    assert retrieval.main(["zzqx-unindexed-term", "--root", str(FIXTURE)]) == 0
    assert "nothing is inferred" in capsys.readouterr().out


@pytest.fixture(scope="module")
def repository() -> dict:
    return build_index(ROOT)


# Routing expectations on the tracked vault: query, filters, top-k limit and expected path.
BENCHMARK = (
    ("att.fragmentable", {}, 1, "10_markdown/documents/tei-p5-att.fragmentable-4.12.0.md"),
    ("att.fragmentable", {}, 3, "20_distillates/documents/tei-p5-att.fragmentable-4.12.0.md"),
    ("@part", {}, 1, "10_markdown/documents/tei-p5-att.fragmentable-4.12.0.md"),
    ("Non-hierarchical Structures", {}, 1, "10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0.md"),
    ("Non-hierarchical Structures", {"layer": "distillate"}, 1,
     "20_distillates/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0.md"),
    ("issue 1505", {"layer": "distillate"}, 1, "20_distillates/publications/teic-tei-issue-1505.md"),
    ("text model", {"authority": "project-proposal"}, 1, "knowledge/text-model.md"),
    ("nymRef", {"layer": "assertion"}, 2,
     "30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named.md"),
)


@pytest.mark.parametrize(("query", "filters", "within", "expected"), BENCHMARK)
def test_repository_routing_benchmark(repository: dict, query: str, filters: dict, within: int, expected: str) -> None:
    """Lexical routing only: the expected path appears within the stated top-k."""
    assert expected in paths(search(repository, query, limit=within, **filters))


def test_repository_provenance_filters_and_contests(repository: dict) -> None:
    anchor = record(repository, "10_markdown/documents/tei-p5-anchor-4.12.0.md")["source"]
    assert anchor["manifest_chain"] == ["sources/manifests/2026-09-05-text-identity-pilot-admission.yaml",
                                        "sources/manifests/2026-09-07-guidelines-4.12.0-admission.yaml"]
    assert (anchor["version"], anchor["family_authority"]) == ("4.12.0", "primary-normative")
    for result in search(repository, "overlap", status="validated", limit=50):
        assert result["status"] == "validated"
        assert result["checked"]["validation"] and result["checked"]["machine-review"]
    assert all("4.12.0" in result["versions"] for result in search(repository, "fragment", version="4.12.0", limit=50))
    assert all(result["path"].startswith("knowledge/")
               for result in search(repository, "model", authority="project-proposal", limit=50))
    named = record(repository, "30_assertions/p5-att-naming-describes-nymref-through-the-object-named.md")
    assert [item["path"] for item in named["contested_with"]] == [
        "30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named.md"]
    fragmentable = record(repository, "10_markdown/documents/tei-p5-att.fragmentable-4.12.0.md")
    assert [topic["topic"] for topic in fragmentable["topics"]["curated"]] == ["Text and Document Structures",
                                                                              "Annotation and Overlap"]
    assert fragmentable["attributes"] == ["part"]
    assert "jenkins.tei-c.org" not in json.dumps(fragmentable)
