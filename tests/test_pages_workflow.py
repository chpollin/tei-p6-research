"""Checks for the static GitHub Pages publication contract."""

from pathlib import Path

REPO = Path(__file__).parents[1]


def test_pages_workflow_publishes_canonical_proposal_home_and_materials() -> None:
    workflow = (REPO / ".github" / "workflows" / "pages.yml").read_text(
        encoding="utf-8"
    )

    assert "python tools/validate.py ." in workflow
    assert "python -m tools.corpus.validate_control_plane ." in workflow
    assert "python tools/build_corpus_overview.py" in workflow
    assert '--repository-base "${REPOSITORY_BASE}"' in workflow
    assert '--repository-revision "${GITHUB_SHA}"' in workflow
    assert "python tools/build_home.py" in workflow
    assert "tests/test_build_home.py" in workflow
    assert "python tools/build_knowledge.py" in workflow
    assert "python tools/build_model_reference.py" in workflow
    assert "cp -R docs/. _site/" in workflow
    assert "cp docs/index.html _site/project.html" not in workflow
    assert "actions/upload-pages-artifact@v3" in workflow
    assert "actions/deploy-pages@v4" in workflow
