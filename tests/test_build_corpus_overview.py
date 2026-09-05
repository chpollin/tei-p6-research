"""Tests for the deterministic primary-data overview generator."""

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from build_corpus_overview import build_page, prepare_sources  # noqa: E402
from sitegen.assets import read_asset  # noqa: E402
from sitegen.source_data import resolve_repo_file  # noqa: E402


def test_overview_uses_one_table_row_pair_per_primary_source_family() -> None:
    page = build_page(REPO, "2026-09-05")

    assert "<title>Materials · TEI P6 Research</title>" in page
    assert '<span id="result-count">16</span> sources' in page
    assert page.count('<tr class="source-row" data-source-row') == 16
    assert page.count('<tr class="detail-row"') == 16
    assert "summary-card" not in page
    assert "source-card" not in page
    assert "tei-p5-literature" not in page
    assert '<html lang="en">' in page


def test_overview_is_a_plain_white_work_surface() -> None:
    page = build_page(REPO, "2026-09-05")

    assert "background: var(--paper)" in page
    assert "--paper: #ffffff" in page
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
    assert '<header class="site-header">' in page
    assert 'aria-current="page">Materials</a>' in page
    assert 'data-project-link>About</a>' in page
    assert '<footer class="site-footer">' in page
    assert "not officially affiliated with the TEI Consortium" in page
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
    assert "Not yet acquired" in page
    assert "Normative P5 baseline" in page
    assert "File and directory structure of a pinned Git state." in page


def test_hosted_overview_points_control_links_to_the_repository() -> None:
    page = build_page(
        REPO,
        "2026-09-05",
        repository_base="https://github.com/example/tei-p6-research/blob/abc123",
    )

    assert (
        '<meta name="repository-base" '
        'content="https://github.com/example/tei-p6-research/blob/abc123/">'
    ) in page
    assert 'data-repo-path="sources/locks/github-teic-tei.yaml"' in page
    assert 'data-repo-path="sources/registry.yaml"' not in page
    assert 'data-repo-path="corpus/COMPLETENESS.md"' not in page
    assert 'link.href = "project.html"' in page


def test_overview_exposes_status_scope_gaps_and_control_links() -> None:
    page = build_page(REPO, "2026-09-05")

    assert "Acquired" in page
    assert "GitHub acquisition is waiting for authenticated read access" in page
    assert "authenticated-github-api-session-unavailable" not in page
    assert "The published-HTML run is partial" not in page
    assert "Reconciliation between the published Guidelines and the release archive is pending" in page
    assert "../sources/locks/github-teic-tei.yaml" in page
    assert "../sources/registry.yaml" not in page
    assert "../corpus/COMPLETENESS.md" not in page
    assert ">About</a>" in page


def test_checked_in_overview_matches_the_generator() -> None:
    assert (REPO / "docs" / "corpus.html").read_text(
        encoding="utf-8"
    ) == build_page(REPO, "2026-09-05")


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

    assert f'<style>\n{read_asset("materials.css")}</style>' in page
    assert f'<script>\n{read_asset("materials.js")}</script>' in page
    assert '<link rel="stylesheet"' not in page
    assert '<script src="' not in page


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
