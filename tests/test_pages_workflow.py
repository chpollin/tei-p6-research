"""Checks for the static GitHub Pages publication contract."""

from pathlib import Path

REPO = Path(__file__).parents[1]
WORKFLOWS = REPO / ".github" / "workflows"


def read(name: str) -> str:
    return (WORKFLOWS / name).read_text(encoding="utf-8")


def test_pages_workflow_validates_before_it_regenerates_every_page() -> None:
    workflow = read("pages.yml")

    assert "python tools/validate.py ." in workflow
    assert "python -m tools.corpus.validate_control_plane ." in workflow
    assert "python -m pytest tests -q" in workflow
    for builder in (
        "python tools/build_docs.py",
        "python tools/build_corpus_overview.py",
        "python tools/build_home.py",
        "python tools/build_knowledge.py",
        "python tools/build_model_reference.py",
    ):
        assert builder in workflow
    assert '--repository-base "${REPOSITORY_BASE}"' in workflow
    assert '--repository-revision "${GITHUB_SHA}"' in workflow
    assert "cp -R docs/. _site/" in workflow
    assert "cp docs/index.html _site/project.html" not in workflow
    assert "docs/home.html" not in workflow
    assert "actions/upload-pages-artifact@v3" in workflow
    assert "actions/deploy-pages@v4" in workflow


def test_a_running_pages_deployment_is_never_cancelled() -> None:
    assert "cancel-in-progress: false" in read("pages.yml")
    assert "cancel-in-progress: true" not in read("pages.yml")


def test_checks_workflow_lints_validates_and_runs_the_suite() -> None:
    workflow = read("checks.yml")

    assert "uv sync --locked" in workflow
    assert "uv run --locked python -m pytest tests -q" in workflow
    assert "python -m ruff check ." in workflow
    assert "python tools/validate.py ." in workflow
    assert "python -m tools.corpus.validate_control_plane ." in workflow
    assert "python -m pytest tests -q" in workflow
    assert "python tools/check_text_identity_pilot.py" in workflow


def test_offline_handover_checks_precede_publication_and_preserve_review_boundary() -> None:
    for name in ("checks.yml", "pages.yml"):
        workflow = read(name)
        for command in (
            "python -m tools.build_guidelines_navigation --check",
            "python -m tools.ingest_text_structures --check",
            'python -m tools.export_guidelines --output "${RUNNER_TEMP}/guidelines-xml"',
        ):
            assert command in workflow
        assert '"${RUNNER_TEMP}/guidelines-xml" --check' in workflow
        assert "tools.check_text_structures" not in workflow
        assert "tools/check_text_structures.py" not in workflow
        if name == "pages.yml":
            assert workflow.index("tools.export_guidelines") < workflow.index("tools/build_docs.py")
