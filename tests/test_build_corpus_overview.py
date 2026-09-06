"""Tests for the deterministic primary-data overview generator."""

import subprocess
import sys
from pathlib import Path

import pytest

from tools.build_corpus_overview import build_page, prepare_sources
from tools.sitegen.assets import read_asset
from tools.sitegen.chrome import render_footer, render_header
from tools.sitegen.source_data import resolve_repo_file

REPO = Path(__file__).parents[1]


def test_overview_uses_one_table_row_pair_per_primary_source_family() -> None:
    page = build_page(REPO, "2026-09-05")

    assert "<title>Materials · TEI P6 Research</title>" in page
    assert '<span id="result-count">17</span> sources' in page
    assert page.count('<tr class="source-row" data-source-row') == 17
    assert page.count('<tr class="detail-row"') == 17
    assert "summary-card" not in page
    assert "source-card" not in page
    assert "tei-p5-literature" not in page
    assert '<html lang="en">' in page


def test_overview_is_a_plain_white_work_surface() -> None:
    page = build_page(REPO, "2026-09-05")

    assert "background: var(--paper)" in page
    assert "--paper: #fff" in page
    assert "<h1 id=\"page-title\">Materials</h1>" in page
    assert "This overview shows" not in page
    assert "supporting workbench" not in page
    assert "Register status" not in page
    assert '<table class="source-table">' in page
    assert 'role="status" aria-live="polite"' in page
    assert "Full-text search" in page
    assert 'id="status-filter"' in page
    assert 'id="material-filter"' in page
    assert page.count('class="sort-button"') == 4
    assert render_header("materials") in page
    assert 'aria-current="page">Materials</a>' in page
    assert '<a href="project.html">About</a>' in page
    assert render_footer("2026-09-05") in page
    assert "Commits all observed refs" not in page
    assert "External links inventoried" not in page
    assert "Bugs enumerated" not in page
    for former_german_label in (
        "Materialien",
        "Quellen",
        "Volltextsuche",
        "Erfasst",
        "Teilbestände",
        "Offene Punkte",
        "Technische Angaben",
    ):
        assert former_german_label not in page


def test_overview_names_materials_from_completed_runs() -> None:
    page = build_page(REPO, "2026-09-05")

    assert "Git tree inventory" in page
    assert "Web page census" in page
    assert "Release archive" in page
    assert "ZIP member inventory" in page
    assert "Ticket and discussion records" in page
    assert "Run <code>2026-09-04-tei-legacy-sourceforge</code>" in page
    assert "Run <code>2026-09-04-tei-legacy-sourceforge-r2</code>" in page
    assert "Run <code>2026-09-05-tei-legacy-sourceforge-r3</code>" in page
    assert "Run <code>2026-09-06-github-teic-tei-relations</code>" in page
    assert "Normative P5 baseline" in page
    assert "File and directory structure of a pinned Git state." in page


def test_hosted_overview_resolves_control_links_without_javascript() -> None:
    base = "https://github.com/example/tei-p6-research/blob/abc123"
    page = build_page(REPO, "2026-09-05", repository_base=base)

    assert f'<a href="{base}/sources/locks/github-teic-tei.yaml">Source Lock</a>' in page
    assert "../sources/" not in page
    assert "../corpus/" not in page
    assert "data-repo-path" not in page
    assert f"{base}/sources/registry.yaml" not in page
    assert f"{base}/corpus/COMPLETENESS.md" not in page


@pytest.mark.parametrize("base", ["http://example.org/", "//example.org/", "https://example.org/?query=1"])
def test_overview_rejects_an_unusable_repository_base(base: str) -> None:
    with pytest.raises(ValueError):
        build_page(REPO, "2026-09-05", repository_base=base)


def test_overview_exposes_status_scope_gaps_and_control_links() -> None:
    page = build_page(REPO, "2026-09-05")

    assert "Acquired" in page
    assert "GitHub acquisition is waiting for authenticated read access" not in page
    assert "authenticated-github-api-session-unavailable" not in page
    assert "The published-HTML run is partial" not in page
    assert "Reconciliation between the published Guidelines and the release archive is pending" in page
    assert '<a href="../sources/locks/github-teic-tei.yaml">Source Lock</a>' in page
    assert "../sources/registry.yaml" not in page
    assert "../corpus/COMPLETENESS.md" not in page
    assert ">About</a>" in page


def test_overview_rejects_registry_lock_status_drift(tmp_path: Path) -> None:
    (tmp_path / "sources" / "locks").mkdir(parents=True)
    (tmp_path / "sources" / "registry.yaml").write_text(
        """
sources:
  - source_id: sample
    title: Sample
    family: sample
    authority: primary-record
    lock: sources/locks/sample.yaml
    completion_target: observable-complete
    retrieval_status: partial
""",
        encoding="utf-8",
    )
    (tmp_path / "sources" / "locks" / "sample.yaml").write_text(
        """
source_id: sample
retrieval_status: observable-complete
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="retrieval_status mismatch"):
        prepare_sources(tmp_path)


def test_overview_inlines_its_source_assets() -> None:
    page = build_page(REPO, "2026-09-05")

    assert f'<style>\n{read_asset("workbench.css")}\n{read_asset("materials.css")}</style>' in page
    assert f'<script>\n{read_asset("materials.js")}</script>' in page
    assert '<link rel="stylesheet"' not in page
    assert '<script src="' not in page


def test_overview_uses_plain_holding_lists_and_distinguishes_literature() -> None:
    page = build_page(REPO, "2026-09-05")
    assert page.count("<table ") == 1
    assert '<ul class="holding-list">' in page
    assert '<li class="holding-item">' in page
    assert 'class="holding-status"' in page
    assert '>Data</a>' in page and '>Manifest</a>' in page
    assert "Source families and recorded holdings." in page
    assert "Individual raw files are not enumerated here." in page
    assert '<a href="knowledge.html">Knowledge</a>' in page
    assert '<aside class="literature-note" id="literature">' in page
    assert '<a href="../sources/locks/literature.yaml">' in page
    assert page.count('<tr class="source-row" data-source-row') == 17
    for asset in ("workbench.css", "materials.css"):
        assert "border-top:" not in read_asset(asset)
        assert "border-bottom:" not in read_asset(asset)


def test_overview_rejects_unsafe_or_unexpected_repository_paths() -> None:
    with pytest.raises(ValueError, match="unsafe local overview link"):
        resolve_repo_file(REPO, "../README.md")
    with pytest.raises(ValueError, match="unexpected local overview link"):
        resolve_repo_file(REPO, "README.md")


def test_overview_build_is_deterministic() -> None:
    first = build_page(REPO, "2026-09-05")
    second = build_page(REPO, "2026-09-05")

    assert first == second


def test_overview_cli_remains_compatible(tmp_path: Path) -> None:
    output = tmp_path / "corpus.html"
    result = subprocess.run(
        [
            sys.executable,
            str(REPO / "tools" / "build_corpus_overview.py"),
            "--date",
            "2026-09-05",
            "--root",
            str(REPO),
            "--output",
            str(output),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout.startswith(f"OK: {output}")
    assert output.read_text(encoding="utf-8") == build_page(REPO, "2026-09-05")
