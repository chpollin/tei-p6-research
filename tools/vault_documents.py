"""Parse Markdown frontmatter once for validation, navigation and inventory."""

from __future__ import annotations

import re
from dataclasses import dataclass

import yaml


@dataclass(frozen=True)
class MarkdownDocument:
    metadata: dict
    body: str
    error: str | None = None
    has_frontmatter: bool = True


def parse_frontmatter(text: str) -> MarkdownDocument:
    """Preserve body whitespace and return diagnostics without choosing a policy."""
    text = text.removeprefix("\ufeff").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return MarkdownDocument({}, text, "missing frontmatter", False)
    closing = re.search(r"^---[ \t]*(?=\n|\Z)", text[4:], re.M)
    if closing is None:
        return MarkdownDocument({}, text, "unterminated frontmatter")
    body = text[4 + closing.end():]
    try:
        metadata = yaml.safe_load(text[4:4 + closing.start()])
    except yaml.YAMLError as exc:
        return MarkdownDocument({}, body, f"frontmatter is not valid YAML: {exc}")
    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict):
        return MarkdownDocument(
            {}, body, f"frontmatter is a {type(metadata).__name__}, not a map of fields",
        )
    return MarkdownDocument(metadata, body)
