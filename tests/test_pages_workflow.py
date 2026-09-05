"""Checks for the static GitHub Pages publication contract."""

from pathlib import Path

REPO = Path(__file__).parents[1]


def test_pages_workflow_publishes_generated_material_overview() -> None:
    workflow = (REPO / ".github" / "workflows" / "pages.yml").read_text(
        encoding="utf-8"
    )

    assert "python tools/validate.py ." in workflow
    assert "python -m tools.corpus.validate_control_plane ." in workflow
    assert "python tools/build_corpus_overview.py" in workflow
    assert '--repository-base "${REPOSITORY_BASE}"' in workflow
    assert "cp docs/corpus.html _site/index.html" in workflow
    assert "cp docs/index.html _site/project.html" in workflow
    assert "actions/upload-pages-artifact@v3" in workflow
    assert "actions/deploy-pages@v4" in workflow
