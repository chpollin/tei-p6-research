"""Shared parsing preserves source context and exposes malformed metadata."""

import pytest

from tools.vault_documents import parse_frontmatter


@pytest.mark.parametrize("newline", ["\n", "\r\n"])
@pytest.mark.parametrize("prefix", ["", "\ufeff"])
def test_frontmatter_preserves_body_whitespace(newline: str, prefix: str) -> None:
    text = "---\ntitle: Example\n---\n\n# Source\n  exact passage  \n"
    parsed = parse_frontmatter(prefix + text.replace("\n", newline))
    assert parsed.metadata == {"title": "Example"}
    assert parsed.body == "\n\n# Source\n  exact passage  \n"
    assert parsed.error is None


@pytest.mark.parametrize(("text", "problem"), [
    ("# No metadata\n", "missing frontmatter"),
    ("---\ntitle: Example\n", "unterminated frontmatter"),
    ("---\n- item\n---\nbody", "not a map"),
    ("---\nbroken: [\n---\nbody", "not valid YAML"),
    ("---\ntitle: Example\n---not-a-delimiter\nbody", "unterminated"),
])
def test_invalid_frontmatter_reports_the_problem(text: str, problem: str) -> None:
    parsed = parse_frontmatter(text)
    assert problem in parsed.error
    assert parsed.metadata == {}
