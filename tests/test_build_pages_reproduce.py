"""Every committed page must reproduce from its own recorded build date.

The date is read from the page, so rebuilding on any day stays reproducible
and the check never blocks a documented regeneration.
"""

import re
from collections.abc import Callable
from pathlib import Path

import pytest

from tools.build_corpus_overview import build_page as build_corpus
from tools.build_docs import build_page as build_project
from tools.build_home import build_page as build_home
from tools.build_knowledge import build_page as build_knowledge
from tools.build_model_reference import build_page as build_model

REPO = Path(__file__).parents[1]
FOOTER = re.compile(r'<footer class="wb-footer">.*?<span>Build (\d{4}-\d{2}-\d{2})</span></footer>')
PAGES = {
    "index.html": build_home,
    "corpus.html": build_corpus,
    "knowledge.html": build_knowledge,
    "model.html": build_model,
    "project.html": build_project,
}


def build_date(page: str, name: str) -> str:
    match = FOOTER.search(page)
    if match is None:
        raise AssertionError(f"docs/{name} has no build date in its footer")
    return match.group(1)


@pytest.mark.parametrize("name", sorted(PAGES))
def test_committed_page_reproduces_from_its_recorded_build_date(name: str) -> None:
    build: Callable[[Path, str], str] = PAGES[name]
    committed = (REPO / "docs" / name).read_text(encoding="utf-8")

    assert committed == build(REPO, build_date(committed, name))


def test_no_generated_page_is_published_beside_the_five_builders() -> None:
    published = {path.name for path in (REPO / "docs").glob("*.html")}

    assert published == set(PAGES)
