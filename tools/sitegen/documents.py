"""Read a repository Markdown document with its YAML frontmatter."""
from __future__ import annotations

import re
from pathlib import Path

from tools.vault_documents import parse_frontmatter

WIKI = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def read_document(root: Path, path: str) -> tuple[dict, str]:
    """Return frontmatter and body, refusing anything outside the repository."""
    file = (root / path).resolve()
    if not file.is_relative_to(Path(root).resolve()):
        raise ValueError(f"Document escapes repository: {path}")
    if not file.is_file():
        raise FileNotFoundError(f"Missing document: {path}")
    parsed = parse_frontmatter(file.read_text(encoding="utf-8"))
    if parsed.has_frontmatter and parsed.error:
        label = "Incomplete" if parsed.error == "unterminated frontmatter" else "Invalid"
        raise ValueError(f"{label} frontmatter: {path}: {parsed.error}")
    return parsed.metadata, parsed.body.strip()


def first_table_rows(text: str) -> list[list[str]]:
    """Cells of the body rows of the first Markdown table in ``text``.

    Later tables (for example a mapping table in a subsequent section) must not
    feed a reader that expects the document's defining table.
    """

    rows: list[list[str]] = []
    started = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            started = True
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(set(cell) <= set("-: ") for cell in cells):
                continue
            rows.append(cells)
        elif started:
            break
    return rows
