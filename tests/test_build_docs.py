"""Tests for the deterministic project-page generator."""

import subprocess
import sys
from pathlib import Path

from tools.build_docs import PROJECT_TITLE, SECTIONS, _inline, build_page
from tools.sitegen.assets import read_asset
from tools.sitegen.chrome import render_footer, render_header

REPO = Path(__file__).parents[1]


def test_relative_links_resolve_from_their_source_document() -> None:
    rendered = _inline(
        "Read [the specification](../knowledge/specification.md#scope).",
        Path("knowledge/schema.md"),
    )

    assert 'href="../knowledge/specification.md#scope"' in rendered


def test_external_and_fragment_links_remain_unchanged() -> None:
    rendered = _inline(
        "Use [the site](https://example.org/a) or [this section](#part).",
        Path("README.md"),
    )

    assert 'href="https://example.org/a"' in rendered
    assert 'href="#part"' in rendered


def test_deployed_source_link_preserves_revision_and_fragment(monkeypatch) -> None:
    from tools import build_docs

    revision = "c682eb51eef0d437300274447d22bc1ee6455871"
    monkeypatch.setattr(build_docs, "REPOSITORY_URL", "https://github.com/chpollin/tei-p6-research")
    monkeypatch.setattr(build_docs, "REPOSITORY_REVISION", revision)
    rendered = _inline("[Scope](../knowledge/specification.md#scope)", Path("knowledge/schema.md"))
    assert f'/blob/{revision}/knowledge/specification.md#scope"' in rendered
    assert "/blob/main/" not in rendered


def test_project_page_contains_promptotyping_project_documents() -> None:
    page = build_page(REPO, "2026-09-04")

    assert f"<title>About · {PROJECT_TITLE}</title>" in page
    assert '<html lang="en">' in page
    assert len(SECTIONS) == 15
    assert [anchor for anchor, _, _ in SECTIONS] == [
        "start", "project", "specification", "data", "terminology",
        "architecture", "design", "schema", "operations", "verification",
        "testing", "governance", "plan", "state", "journal",
    ]
    for anchor, _, _ in SECTIONS:
        assert f'id="{anchor}"' in page
    assert "docs/concept.md" not in [relative for _, _, relative in SECTIONS]
    assert render_header("about") in page
    assert render_footer("2026-09-04") in page
    assert '<nav class="project-toc" aria-label="Project documents">' in page


def test_project_page_inlines_its_source_stylesheet() -> None:
    page = build_page(REPO, "2026-09-05")

    assert PROJECT_TITLE == "TEI P6 Research"
    assert f'<style>\n{read_asset("workbench.css")}\n{read_asset("project.css")}</style>' in page
    assert '<link rel="stylesheet"' not in page
    assert "15px/1.6 var(--font)" in page
    assert "border-top:" not in read_asset("project.css")
    assert "border-bottom:" not in read_asset("project.css")
    assert "prefers-color-scheme: dark" not in page


def test_project_page_build_is_deterministic() -> None:
    assert build_page(REPO, "2026-09-05") == build_page(REPO, "2026-09-05")


def test_default_about_output_preserves_the_proposal_home(tmp_path: Path) -> None:
    for _, _, relative in SECTIONS:
        source = tmp_path / relative
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text("# Document\n\nA source paragraph.\n", encoding="utf-8")
    home = tmp_path / "docs" / "index.html"
    home.parent.mkdir(parents=True, exist_ok=True)
    home.write_text("proposal-home-sentinel", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(REPO / "tools/build_docs.py"), "--root", str(tmp_path),
         "--date", "2026-09-05"], check=True, capture_output=True, text=True,
    )
    about = tmp_path / "docs/project.html"
    assert str(about) in result.stdout
    assert about.is_file()
    assert render_header("about") in about.read_text(encoding="utf-8")
    assert home.read_text(encoding="utf-8") == "proposal-home-sentinel"
