"""Navigation joins retain their finite source boundary and declared meaning."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from tools.build_guidelines_navigation import ATLAS, COVERAGE, OUTPUT, build, serialized
from tools.sitegen.knowledge_page import _guidelines

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def navigation() -> dict:
    return build(ROOT)


def test_complete_boundary_and_existing_topics(navigation: dict) -> None:
    rows = navigation["sources"]
    assert len(rows) == 888
    specs = [r for r in rows if r["ident"]]
    assert len(specs) == 846
    assert len({r["representation"] for r in rows}) == 888
    assert navigation["use"] == "navigation-only; never grounding"
    for row in rows:
        assert row["topic_suggestions"] or row["unclassified_reason"]
        assert "status" not in row and "grounding" not in row
        for suggestion in row["topic_suggestions"]:
            assert suggestion["rule"]
            assert navigation["topics"][suggestion["topic"]] == suggestion["moc"]
            assert (ROOT / suggestion["moc"]).is_file()


def test_edges_preserve_atlas_and_reverse_navigation(navigation: dict) -> None:
    rows = {r["representation"]: r for r in navigation["sources"]}
    atlas = json.loads((ROOT / ATLAS).read_text(encoding="utf-8"))
    assert sum(len(r["references"]) for r in rows.values()) == sum(len(r["references"]) for r in atlas["records"])
    unresolved = 0
    for row in rows.values():
        for edge in row["references"]:
            assert edge.get("anchor") or edge["anchor_reason"]
            if edge["target_representation"]:
                target = rows[edge["target_representation"]]
                assert any(back["representation"] == row["representation"] and back["xml_location"] == edge["xml_location"] and back["relation"] == edge["relation"] for back in target["referenced_by"])
            else:
                unresolved += 1
                assert edge["resolution"] == "unresolved" and edge["reason"]
    assert unresolved == len(atlas["unresolved_references"])


def test_tracked_only_reproduction(tmp_path: Path, navigation: dict) -> None:
    for relative in navigation["inputs"]:
        destination = tmp_path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
    assert not (tmp_path / "00_sources").exists()
    assert not (tmp_path / "corpus/raw").exists()
    assert serialized(build(tmp_path)) == serialized(navigation)
    assert (ROOT / OUTPUT).read_bytes() == serialized(navigation).encode("utf-8")
    coverage = json.loads((tmp_path / COVERAGE).read_text(encoding="utf-8"))
    coverage["commit"] = "0" * 40
    (tmp_path / COVERAGE).write_text(json.dumps(coverage), encoding="utf-8")
    with pytest.raises(ValueError, match="release identities"):
        build(tmp_path)


def test_navigation_escapes_source_fields(navigation: dict) -> None:
    row = json.loads(json.dumps(next(r for r in navigation["sources"] if r["references"])))
    row["module"] = '<script>alert("module")</script>'
    row["references"][0]["xml_location"] = '<img src=x onerror="bad()">'
    text = _guidelines(row, None)
    assert '<script>' not in text and '<img' not in text
    assert '&lt;script&gt;' in text and '&lt;img' in text
    assert 'no scholarly classification' in text


def test_known_classification_is_attributed(navigation: dict) -> None:
    rows = {r["source"]: r for r in navigation["sources"]}
    app = rows["P5/Source/Specs/app.xml"]
    assert {s["rule"] for s in app["topic_suggestions"]} == {"spec-category:elementSpec", "declared-module:textcrit"}
    chapter = rows["P5/Source/Guidelines/en/TC-CriticalApparatus.xml"]
    assert chapter["topic_suggestions"][0]["rule"] == "chapter-module-map:textcrit"
