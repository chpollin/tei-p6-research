"""Tests for the deterministic project-page generator."""

import sys
from pathlib import Path

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from build_docs import PROJECT_TITLE, SECTIONS, _inline, build_page  # noqa: E402


def test_relative_links_resolve_from_their_source_document() -> None:
    rendered = _inline(
        "Read [the specification](../knowledge/specification.md#scope).",
        Path("docs/concept.md"),
    )

    assert 'href="../knowledge/specification.md#scope"' in rendered


def test_external_and_fragment_links_remain_unchanged() -> None:
    rendered = _inline(
        "Use [the site](https://example.org/a) or [this section](#part).",
        Path("README.md"),
    )

    assert 'href="https://example.org/a"' in rendered
    assert 'href="#part"' in rendered


def test_project_page_contains_promptotyping_project_documents() -> None:
    page = build_page(REPO, "2026-09-04")

    assert f"<title>{PROJECT_TITLE}</title>" in page
    assert '<html lang="en">' in page
    assert len(SECTIONS) == 9
    assert 'id="project"' in page
    assert 'id="design"' in page
    assert 'id="state"' in page
    assert 'id="journal"' in page
    assert '<a href="corpus.html">Primary data</a>' in page
