"""Read a repository Markdown document with its YAML frontmatter."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

WIKI = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def read_document(root: Path, path: str) -> tuple[dict, str]:
    """Return frontmatter and body, refusing anything outside the repository."""
    file = (root / path).resolve()
    if not file.is_relative_to(Path(root).resolve()):
        raise ValueError(f"Document escapes repository: {path}")
    if not file.is_file():
        raise FileNotFoundError(f"Missing document: {path}")
    text = file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text.strip()
    pieces = text.split("---\n", 2)
    if len(pieces) != 3:
        raise ValueError(f"Incomplete frontmatter: {path}")
    meta = yaml.safe_load(pieces[1]) or {}
    if not isinstance(meta, dict):
        raise ValueError(f"Invalid frontmatter: {path}")
    return meta, pieces[2].strip()
