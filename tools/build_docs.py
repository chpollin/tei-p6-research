"""Generate the About page docs/project.html from the repository's own documents.

Data flow: README.md and the knowledge documents are read in a
fixed order, their YAML frontmatter is stripped, their Markdown is converted to
HTML and the sections are wrapped in one self-contained page with inline CSS.
Repository-relative links are resolved against each source document. Without a
configured remote they point back into the local checkout; `--repository-url`
turns them into canonical repository links for a deployed page.

The Markdown subset covers what these documents actually use: headings,
paragraphs, lists (nested, with block content in an item), tables, blockquotes,
fenced code, inline code, bold, italic, ordinary links and wikilinks. Complete
CommonMark coverage is deliberately out of scope; a document that needs more
syntax is the wrong input for this page.

The generation date is a required argument rather than the system date, so that
a rebuild of an older state stays reproducible.

Usage: python tools/build_docs.py --date 2026-09-04
"""

from __future__ import annotations

import argparse
import html
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # direct script run

from tools.sitegen.assets import read_asset
from tools.sitegen.chrome import render_footer, render_header

PROJECT_TITLE = "TEI P6 Research"
PROJECT_TAGLINE = (
    "Project scope, research method, and repository contracts."
)
REPOSITORY_URL: str | None = None
REPOSITORY_REVISION = "main"

# (anchor id, section title, source file relative to the vault root)
SECTIONS = [
    ("start", "Start", "README.md"),
    ("project", "Project", "knowledge/project.md"),
    ("specification", "Specification", "knowledge/specification.md"),
    ("data", "Material", "knowledge/data.md"),
    ("concept", "Concept", "knowledge/methodology.md"),
    ("terminology", "Terminology", "knowledge/INDEX.md"),
    ("architecture", "Architecture", "knowledge/architecture.md"),
    ("design", "Interface design", "knowledge/design.md"),
    ("schema", "Schema", "knowledge/schema.md"),
    ("operations", "Operations", "knowledge/operations.md"),
    ("verification", "Verification", "knowledge/verification.md"),
    ("testing", "Testing", "knowledge/testing.md"),
    ("governance", "Governance", "knowledge/governance.md"),
    ("plan", "Plan", "knowledge/plan.md"),
    ("state", "State", "knowledge/state.md"),
    ("journal", "Journal", "knowledge/journal.md"),
]

CHAIN = [
    ("00_sources", "the originals exactly as they arrived"),
    ("10_markdown", "one Markdown form per source, carrying block IDs"),
    ("20_distillates", "one distillate per source, anchored into it"),
    ("30_assertions", "atomic statements grounded in distillates"),
    ("40_output", "chapters footnoted to assertions"),
]

_FRONTMATTER = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
_CODE_SPAN = re.compile(r"`([^`]+)`")
_WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_ITEM = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")
_TABLE_RULE = re.compile(r"^\s*\|[\s:|-]+\|\s*$")


def _repository_href(href: str, source: Path) -> str:
    """Resolve a relative Markdown target from its source document."""
    target = html.unescape(href)
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
        return href
    resolved = posixpath.normpath((source.parent / parsed.path).as_posix())
    if REPOSITORY_URL:
        repository_path = f"{REPOSITORY_URL}/blob/{quote(REPOSITORY_REVISION, safe='')}/{quote(resolved, safe='/')}"
    else:
        repository_path = f"../{quote(resolved, safe='/')}"
    return html.escape(
        urlunsplit(("", "", repository_path, parsed.query, parsed.fragment)),
        quote=True,
    )


def _inline(text: str, source: Path) -> str:
    """Convert inline Markdown, keeping code spans free of further markup."""
    parts = _CODE_SPAN.split(text)
    out = []
    for index, part in enumerate(parts):
        if index % 2:
            out.append(f"<code>{html.escape(part)}</code>")
            continue
        piece = html.escape(part)
        piece = _WIKILINK.sub(lambda m: f"<code>{m.group(1)}</code>", piece)
        piece = _LINK.sub(
            lambda m: (
                f'<a href="{_repository_href(m.group(2), source)}">{m.group(1)}</a>'
            ),
            piece,
        )
        piece = _BOLD.sub(r"<strong>\1</strong>", piece)
        piece = _ITALIC.sub(r"<em>\1</em>", piece)
        out.append(piece)
    return "".join(out)


def _starts_block(line: str) -> bool:
    stripped = line.lstrip()
    return (
        not stripped
        or stripped.startswith(("```", ">", "|"))
        or bool(_HEADING.match(line))
        or bool(_ITEM.match(line))
    )


def _split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _dedent(lines: list[str]) -> list[str]:
    indents = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    cut = min(indents) if indents else 0
    return [line[cut:] if line.strip() else "" for line in lines]


def _render_fence(lines: list[str], start: int) -> tuple[str, int]:
    index = start + 1
    body = []
    while index < len(lines) and not lines[index].lstrip().startswith("```"):
        body.append(lines[index])
        index += 1
    code = html.escape("\n".join(_dedent(body)))
    return f"<pre><code>{code}</code></pre>", index + 1


def _render_table(lines: list[str], start: int, source: Path) -> tuple[str, int]:
    header = _split_row(lines[start])
    index = start + 2
    rows = []
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        rows.append(_split_row(lines[index]))
        index += 1
    head = "".join(f"<th>{_inline(cell, source)}</th>" for cell in header)
    body = "".join(
        "<tr>" + "".join(f"<td>{_inline(cell, source)}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    table = f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
    return f'<div class="scroll">{table}</div>', index


def _render_quote(lines: list[str], start: int, source: Path) -> tuple[str, int]:
    index = start
    body = []
    while index < len(lines) and lines[index].lstrip().startswith(">"):
        body.append(lines[index].lstrip()[1:].removeprefix(" "))
        index += 1
    return f"<blockquote>{_render_blocks(body, source)}</blockquote>", index


def _render_item(buffer: list[str], source: Path) -> str:
    first = _inline(buffer[0].strip(), source)
    rest = _dedent(buffer[1:])
    inner = _render_blocks(rest, source) if any(line.strip() for line in rest) else ""
    return f"<li>{first}{inner}</li>"


def _render_list(lines: list[str], start: int, source: Path) -> tuple[str, int]:
    match = _ITEM.match(lines[start])
    if match is None:
        raise ValueError(f"not a list item: {lines[start]!r}")
    base = len(match.group(1))
    ordered = match.group(2)[0].isdigit()
    index = start
    items: list[str] = []
    buffer: list[str] = []
    while index < len(lines):
        line = lines[index]
        item = _ITEM.match(line)
        indent = len(line) - len(line.lstrip())
        if item and indent == base:
            if buffer:
                items.append(_render_item(buffer, source))
            buffer = [item.group(3)]
        elif not line.strip():
            # A blank line ends the list unless an indented continuation or a
            # further item at the same level follows (loose list).
            following = next((x for x in lines[index + 1 :] if x.strip()), "")
            following_indent = len(following) - len(following.lstrip())
            continues = following_indent > base or (
                following_indent == base and _ITEM.match(following)
            )
            if not following or not continues:
                break
            buffer.append("")
        elif indent > base and buffer:
            buffer.append(line)
        else:
            break
        index += 1
    if buffer:
        items.append(_render_item(buffer, source))
    tag = "ol" if ordered else "ul"
    return f"<{tag}>{''.join(items)}</{tag}>", index


def _render_blocks(lines: list[str], source: Path) -> str:
    out: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
        elif line.lstrip().startswith("```"):
            block, index = _render_fence(lines, index)
            out.append(block)
        elif heading := _HEADING.match(line):
            level = min(len(heading.group(1)), 6)
            out.append(f"<h{level}>{_inline(heading.group(2), source)}</h{level}>")
            index += 1
        elif (
            line.lstrip().startswith("|")
            and index + 1 < len(lines)
            and _TABLE_RULE.match(lines[index + 1])
        ):
            block, index = _render_table(lines, index, source)
            out.append(block)
        elif line.lstrip().startswith(">"):
            block, index = _render_quote(lines, index, source)
            out.append(block)
        elif _ITEM.match(line):
            block, index = _render_list(lines, index, source)
            out.append(block)
        else:
            paragraph = [line.strip()]
            index += 1
            while index < len(lines) and not _starts_block(lines[index]):
                paragraph.append(lines[index].strip())
                index += 1
            out.append(f"<p>{_inline(' '.join(paragraph), source)}</p>")
    return "".join(out)


def _prepare(text: str) -> list[str]:
    """Strip frontmatter, drop the document H1 and demote the remaining headings."""
    body = _FRONTMATTER.sub("", text).replace("\r\n", "\n")
    lines = body.split("\n")
    out = []
    seen_title = False
    for line in lines:
        heading = _HEADING.match(line)
        if heading and len(heading.group(1)) == 1 and not seen_title:
            seen_title = True
            continue
        if heading:
            out.append("#" + line)
        else:
            out.append(line)
    return out


def _render_section(anchor: str, title: str, path: Path, source: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"source document missing: {path}")
    body = _render_blocks(_prepare(path.read_text(encoding="utf-8")), source)
    return (
        f'<section id="{anchor}">\n<h2>{html.escape(title)}</h2>\n{body}\n</section>\n'
    )


def _render_chain() -> str:
    steps = []
    for position, (name, note) in enumerate(CHAIN):
        if position:
            steps.append('<div class="chain-arrow" aria-hidden="true">&#8594;</div>')
        steps.append(
            f'<div class="chain-step"><span class="chain-name">{name}</span>'
            f'<span class="chain-note">{note}</span></div>'
        )
    return (
        '<div class="chain" role="img" aria-label="The chain of the five layers: '
        f'{"; ".join(name + ", " + note for name, note in CHAIN)}">'
        f"{''.join(steps)}</div>"
    )


CSS = "\n" + read_asset("workbench.css") + "\n" + read_asset("project.css")


def build_page(root: Path, date: str) -> str:
    nav = "".join(
        f'<li><a href="#{anchor}">{html.escape(title)}</a></li>'
        for anchor, title, _ in SECTIONS
    )
    sections = "".join(
        _render_section(anchor, title, root / relative, Path(relative))
        for anchor, title, relative in SECTIONS
    )
    if REPOSITORY_URL:
        source_label = (
            f'<a href="{html.escape(REPOSITORY_URL, quote=True)}">'
            "TEI P6 Research repository</a>"
        )
    else:
        source_label = "the local TEI P6 Research documents"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>About · {PROJECT_TITLE}</title>
<meta name="description" content="{PROJECT_TAGLINE}">
<style>{CSS}</style>
</head>
<body>
<a class="skip-link" href="#main">Skip to project documents</a>
{render_header("about")}
<main class="wb-main" id="main">
<header class="project-intro">
<h1>About</h1>
<p class="wb-description">{PROJECT_TAGLINE} Generated from {source_label}.</p>
</header>
<div class="project-layout">
<nav class="project-toc" aria-label="Project documents"><ul>{nav}</ul></nav>
<div class="project-content">
{_render_chain()}
{sections}</div></div></main>
{render_footer(date)}
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--date", required=True, help="generation date, ISO 8601")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="vault root (default: the repository this script lives in)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="target file (default: <root>/docs/project.html)",
    )
    parser.add_argument(
        "--repository-url",
        default=None,
        help="optional canonical repository URL used for source links",
    )
    parser.add_argument(
        "--repository-revision", default="main",
        help="Git revision for deployed source links (default: main)",
    )
    args = parser.parse_args()

    global REPOSITORY_URL, REPOSITORY_REVISION
    REPOSITORY_URL = args.repository_url.rstrip("/") if args.repository_url else None
    REPOSITORY_REVISION = args.repository_revision
    root: Path = args.root.resolve()
    output: Path = args.output or root / "docs" / "project.html"
    try:
        page = build_page(root, args.date)
    except FileNotFoundError as error:
        print(f"FEHLER: {error}", file=sys.stderr)
        return 1
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding="utf-8", newline="\n")
    print(f"OK: {output} ({len(page)} bytes, {len(SECTIONS)} sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
