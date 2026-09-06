"""Generate the source inventory and the navigation regions of a Grounded Vault.

The inventory used to be kept by hand and checked by the validator, which made
it a second record of what the vault holds and let it drift away from the files.
The files are the record; this script reads them and writes the generated blocks.

The source inventory carries one row per source, in the shape
`knowledge/state.md` declares:
Source | Type | Channel | Markdown representation | Distillate | Status.
The processing status follows from what is present: an original without a
Markdown representation is `new`, a representation without a distillate is
`ingested`, and a distillate makes the source `distilled`. Type and channel come
from the frontmatter of the representation; a publication has no representation,
so its row is built from the CSL record in `references/` and carries the import
channel.

The navigation regions are built from frontmatter. A topic map lists the
distillates of its topic, which are the ones its assertions ground in together
with the ones whose own `topics` names the map, and the assertions whose `topics`
names it; a glossary entry lists the assertions that declare it in `phenomena`,
with their grounding anchors. Each block stands between its own markers, and
everything outside them is hand-written and stays untouched, so the lead and the
open questions of a map remain a person's text.

`00_sources/` is gitignored and may be absent on a clone. It is read when it is
there, so an original that has not been ingested yet shows up as a `new` row, and
skipped when it is not, in which case that state is simply invisible.

Usage:
    python tools/inventory.py <vault-root> [--write | --check]

Without a flag the table goes to stdout, followed by the regions that would
change. `--write` writes every generated region, `--check` exits non-zero when
one of them is out of date.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

STATE = "knowledge/state.md"

INVENTORY = "inventory"
DISTILLATES = "distillates"
ASSERTIONS = "assertions"
EXAMPLES = "examples"


def begin(name: str) -> str:
    return f"<!-- {name}:begin -->"


def end(name: str) -> str:
    return f"<!-- {name}:end -->"


BEGIN = begin(INVENTORY)
END = end(INVENTORY)

REPRESENTATION_FOLDERS = ("10_markdown/documents", "10_markdown/data")
DISTILLATE_FOLDER = "20_distillates"
SOURCE_FOLDER = "00_sources"
REFERENCE_FOLDER = "references"
ASSERTION_FOLDER = "30_assertions"
GLOSSARY_FOLDER = "glossary"

DISTILLATE_HEADING = "## Sources and distillates"
ASSERTION_HEADING = "## Assertions"
EXAMPLE_HEADING = "## Examples"
OPEN_QUESTIONS = "## Open questions"
NO_EXAMPLE = "- No assertion declares this phenomenon yet."

COLUMNS = (
    "Source",
    "Type",
    "Channel",
    "Markdown representation",
    "Distillate",
    "Status",
)
EMPTY = "—"

WIKILINK = re.compile(r"\[\[([^\]#|]+?)(?:#\^[A-Za-z0-9-]+)?(?:\|[^\]]*)?\]\]")
# The link as the document writes it, block anchor included, for a generated line
# that has to reproduce the anchor rather than the document it points into.
WRITTEN_LINK = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
H1 = re.compile(r"^#\s+(.*)$", re.MULTILINE)


@dataclass
class Row:
    source: str
    type: str
    channel: str
    representation: str
    distillate: str
    status: str

    def cells(self) -> tuple[str, ...]:
        return (
            self.source,
            self.type,
            self.channel,
            self.representation,
            self.distillate,
            self.status,
        )


@dataclass(frozen=True)
class Region:
    """One generated block of a document, delimited by its own markers.

    `heading` names the section the block belongs under and is what lets the
    generator insert a region a document does not carry yet. The inventory has
    none, because its place in the state document is fixed by hand.
    """

    name: str
    body: str
    heading: str | None = None


@dataclass(frozen=True)
class Assertion:
    """What the navigation regions read out of one assertion."""

    rel: str
    title: str
    topics: tuple[str, ...]
    phenomena: tuple[str, ...]
    grounding: tuple[str, ...]


def _read(path: Path) -> tuple[dict, str]:
    """The YAML block and the body of a Markdown file, an empty map without one."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    stop = text.find("\n---", 4)
    if stop < 0:
        return {}, text
    try:
        loaded = yaml.safe_load(text[4:stop])
    except yaml.YAMLError:
        return {}, text[stop + 4 :]
    return (loaded if isinstance(loaded, dict) else {}), text[stop + 4 :]


def _frontmatter(path: Path) -> dict:
    """The YAML block of a Markdown file, empty when it carries none."""
    return _read(path)[0]


def _link_target(value: object) -> str | None:
    match = WIKILINK.search(str(value))
    return match.group(1).strip() if match else None


def _title(fm: dict, fallback: str) -> str:
    metadata = fm.get("metadata")
    if isinstance(metadata, dict) and str(metadata.get("title") or "").strip():
        return str(metadata["title"]).strip()
    return fallback


def _link(rel: str) -> str:
    return f"[[{rel}]]"


def _escape(cell: str) -> str:
    return cell.replace("|", "\\|")


def _markdown_files(root: Path, folder: str) -> list[Path]:
    directory = root / folder
    return sorted(directory.rglob("*.md")) if directory.is_dir() else []


def _representations(root: Path) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for folder in REPRESENTATION_FOLDERS:
        for path in _markdown_files(root, folder):
            rel = path.relative_to(root).with_suffix("").as_posix()
            found[rel] = _frontmatter(path)
    return found


def _distillates(root: Path) -> dict[str, list[tuple[str, dict]]]:
    """Distillates grouped by what they hang on, a representation or a reference id.

    A distillate that names neither is grouped under its own path, so it stays a
    row of its own rather than disappearing from the inventory. The grouping is
    a list because two distillates may name the same source, which is a state
    the schema forbids and the inventory must still show.
    """
    found: dict[str, list[tuple[str, dict]]] = {}
    for path in _markdown_files(root, DISTILLATE_FOLDER):
        rel = path.relative_to(root).with_suffix("").as_posix()
        fm = _frontmatter(path)
        key = (
            _link_target(fm.get("representation") or "")
            or str(fm.get("reference") or "").strip()
        )
        found.setdefault(key or rel, []).append((rel, fm))
    return found


def _references(root: Path) -> dict[str, str]:
    """CSL record id to its title, over every JSON file in references/."""
    found: dict[str, str] = {}
    directory = root / REFERENCE_FOLDER
    if not directory.is_dir():
        return found
    for path in sorted(directory.glob("*.json")):
        try:
            records = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for record in records if isinstance(records, list) else [records]:
            if isinstance(record, dict) and record.get("id"):
                found[str(record["id"])] = str(record.get("title") or record["id"])
    return found


def _originals(root: Path, representations: dict[str, dict]) -> list[str]:
    """Files in 00_sources/ that no representation names.

    The folder is gitignored, so its absence says nothing and is not a finding.
    """
    directory = root / SOURCE_FOLDER
    if not directory.is_dir():
        return []
    claimed = {
        target
        for fm in representations.values()
        for field in ("source", "data")
        if (target := _link_target(fm.get(field) or ""))
    }
    found = []
    for path in sorted(directory.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if not path.is_file() or path.name.startswith(".") or path.name == "README.md":
            continue
        if rel not in claimed:
            found.append(rel)
    return found


def rows(root: Path) -> list[Row]:
    representations = _representations(root)
    distillates = _distillates(root)
    references = _references(root)
    collected: list[Row] = []

    for rel, fm in representations.items():
        source = _title(fm, rel.rsplit("/", 1)[-1])
        doctype = str(fm.get("source-type") or EMPTY)
        channel = str(fm.get("channel") or EMPTY)
        for distillate, _ in distillates.get(rel, [(None, {})]):
            collected.append(
                Row(
                    source=source,
                    type=doctype,
                    channel=channel,
                    representation=_link(rel),
                    distillate=_link(distillate) if distillate else EMPTY,
                    status="distilled" if distillate else "ingested",
                )
            )

    for reference, title in references.items():
        for distillate, _ in distillates.get(reference, [(None, {})]):
            collected.append(
                Row(
                    source=title,
                    type="publication",
                    channel="import",
                    representation=EMPTY,
                    distillate=_link(distillate) if distillate else EMPTY,
                    status="distilled" if distillate else "new",
                )
            )

    keyed = set(representations) | set(references)
    for key, group in distillates.items():
        if key in keyed:
            continue
        for rel, fm in group:
            collected.append(
                Row(
                    source=rel.rsplit("/", 1)[-1],
                    type=str(fm.get("source-type") or EMPTY),
                    channel=EMPTY,
                    representation=EMPTY,
                    distillate=_link(rel),
                    status="distilled",
                )
            )

    for rel in _originals(root, representations):
        collected.append(
            Row(
                source=rel.rsplit("/", 1)[-1],
                type=EMPTY,
                channel=EMPTY,
                representation=EMPTY,
                distillate=EMPTY,
                status="new",
            )
        )

    return sorted(
        collected, key=lambda row: (row.type, row.source.lower(), row.distillate)
    )


def render(rows: list[Row]) -> str:
    lines = [
        "| " + " | ".join(COLUMNS) + " |",
        "|" + "---|" * len(COLUMNS),
    ]
    for row in rows:
        lines.append("| " + " | ".join(_escape(cell) for cell in row.cells()) + " |")
    return "\n".join(lines)


def _written_links(value: object) -> list[str]:
    """The link targets of a value, each as the document writes it."""
    return [m.group(1).strip() for m in WRITTEN_LINK.finditer(str(value))]


def _field_links(fm: dict, name: str) -> tuple[str, ...]:
    raw = fm.get(name) or []
    values = raw if isinstance(raw, list) else [raw]
    return tuple(target for value in values for target in _written_links(value))


def _h1(body: str) -> str:
    """The title line of a document, which is what a generated list shows."""
    found = H1.search(body)
    return found.group(1).strip() if found else ""


def _notes(root: Path, folder: str) -> list[tuple[Path, dict, str]]:
    return [(path, *_read(path)) for path in _markdown_files(root, folder)]


def _topics(fm: dict) -> tuple[str, ...]:
    """The topics a document declares; a field of another shape declares none."""
    raw = fm.get("topics")
    if not isinstance(raw, list):
        return ()
    return tuple(str(value).strip("[] ") for value in raw)


def _assertions(root: Path, notes: list[tuple[Path, dict, str]]) -> list[Assertion]:
    """Every assertion of the vault, sorted by slug, which is the list order."""
    found = []
    for path, fm, body in notes:
        if fm.get("type") != "assertion":
            continue
        rel = path.relative_to(root).with_suffix("").as_posix()
        found.append(
            Assertion(
                rel=rel,
                title=_h1(body),
                topics=_topics(fm),
                phenomena=_field_links(fm, "phenomena"),
                grounding=_field_links(fm, "grounding"),
            )
        )
    return sorted(found, key=lambda one: one.rel.rsplit("/", 1)[-1])


def _topic_regions(
    topic: str,
    assertions: list[Assertion],
    registered: list[tuple[str, tuple[str, ...]]],
) -> tuple[Region, ...]:
    """The two lists of one topic map.

    A distillate belongs to the topic through an assertion that grounds in it and
    through its own `topics` alike, because a source can be registered under a
    topic before any assertion rests on it.
    """
    of_topic = [one for one in assertions if topic in one.topics]
    distillates = sorted(
        {anchor.split("#")[0] for one in of_topic for anchor in one.grounding}
        | {rel for rel, topics in registered if topic in topics}
    )
    return (
        Region(
            DISTILLATES,
            "\n".join(f"- [[{target}]]" for target in distillates),
            DISTILLATE_HEADING,
        ),
        Region(
            ASSERTIONS,
            "\n".join(f"- [[{one.rel}]] — {one.title}" for one in of_topic),
            ASSERTION_HEADING,
        ),
    )


def _example_region(entry: str, assertions: list[Assertion]) -> Region:
    lines: list[str] = []
    for one in assertions:
        if entry not in one.phenomena:
            continue
        lines.append(f"- [[{one.rel}]] — {one.title}")
        lines += [f"  - [[{anchor}]]" for anchor in one.grounding]
    return Region(EXAMPLES, "\n".join(lines or [NO_EXAMPLE]), EXAMPLE_HEADING)


def regions(root: Path) -> dict[Path, tuple[Region, ...]]:
    """Every generated region of the vault, by the file that carries it.

    The state document is included only where it exists, so a vault without one
    reports no drift over a file it does not have.
    """
    notes = _notes(root, ASSERTION_FOLDER)
    assertions = _assertions(root, notes)
    registered = [
        (path.relative_to(root).with_suffix("").as_posix(), _topics(fm))
        for path, fm, _ in _notes(root, DISTILLATE_FOLDER)
        if fm.get("type") == "distillate"
    ]
    found: dict[Path, tuple[Region, ...]] = {}
    if (state := root / STATE).is_file():
        found[state] = (Region(INVENTORY, render(rows(root))),)
    for path, fm, _ in notes:
        if fm.get("type") == "moc":
            found[path] = _topic_regions(
                str(fm.get("topic") or ""), assertions, registered
            )
    for path, fm, _ in _notes(root, GLOSSARY_FOLDER):
        if fm.get("type") == "glossary":
            rel = path.relative_to(root).with_suffix("").as_posix()
            found[path] = (_example_region(rel, assertions),)
    return found


def extract(text: str, name: str) -> str | None:
    """The current content between a region's markers, None where they are absent."""
    start, stop = text.find(begin(name)), text.find(end(name))
    if start < 0 or stop < start:
        return None
    inner = text[start + len(begin(name)) : stop]
    return inner.removeprefix("\n").removesuffix("\n")


def drift(text: str, region: Region) -> str | None:
    """What is wrong with the region in this text, None when it is current."""
    current = extract(text, region.name)
    if current is None:
        return f"generated region {region.name} is missing"
    if current != region.body:
        return f"generated region {region.name} is out of date"
    return None


def _insert(text: str, heading: str, block: str) -> str:
    """The text with a region added, under its heading and above the open questions.

    A heading a document already carries keeps everything standing under it and
    receives the region at its top, so no hand-written line is lost and no second
    heading of the same name appears.
    """
    lines = text.splitlines()
    if heading in lines:
        at, added = lines.index(heading) + 1, block.splitlines()
    else:
        at = lines.index(OPEN_QUESTIONS) if OPEN_QUESTIONS in lines else len(lines)
        added = [heading, "", *block.splitlines()]
    before, after = lines[:at], lines[at:]
    if before and before[-1].strip():
        added = ["", *added]
    if after and after[0].strip():
        added = [*added, ""]
    return "\n".join([*before, *added, *after]) + ("\n" if text.endswith("\n") else "")


def _apply(text: str, region: Region, rel: str) -> str:
    block = f"{begin(region.name)}\n{region.body}\n{end(region.name)}"
    start, stop = text.find(begin(region.name)), text.find(end(region.name))
    if start >= 0 and stop > start:
        return text[:start] + block + text[stop + len(end(region.name)) :]
    if region.heading is None:
        raise SystemExit(
            f"{rel} carries no {region.name} markers; add the two lines "
            f"{begin(region.name)} and {end(region.name)} around the generated block"
        )
    return _insert(text, region.heading, block)


def _rewrite(path: Path, rel: str, wanted: tuple[Region, ...]) -> bool:
    """Write the regions into one file and report whether that changed it."""
    text = path.read_text(encoding="utf-8")
    updated = text
    for region in wanted:
        updated = _apply(updated, region, rel)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def _state(root: Path) -> Path:
    path = root / STATE
    if not path.is_file():
        raise SystemExit(f"no {STATE} to write into: {path}")
    return path


def write(root: Path, table: str) -> None:
    """Replace the source inventory in the state document."""
    _rewrite(_state(root), STATE, (Region(INVENTORY, table),))


def regenerate(root: Path) -> list[str]:
    """Write every generated region of the vault and report the files that changed."""
    _state(root)  # a vault without a state document has nowhere to put the inventory
    changed = []
    for path, wanted in sorted(regions(root).items()):
        rel = path.relative_to(root).as_posix()
        if _rewrite(path, rel, wanted):
            changed.append(rel)
    return changed


def outdated(root: Path) -> list[tuple[str, str]]:
    """Every generated region that is missing or differs, as file and finding."""
    found = []
    for path, wanted in sorted(regions(root).items()):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        found += [(rel, note) for r in wanted if (note := drift(text, r))]
    return found


def _report(stale: list[tuple[str, str]]) -> None:
    for rel, note in stale:
        print(f"{rel}: {note}")
    print(f"{len(stale)} generated region(s) out of date")


def main() -> None:
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", type=Path, help="vault root directory")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--write",
        action="store_true",
        help="write every generated region instead of printing",
    )
    mode.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero when a generated region is out of date",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if args.write:
        changed = regenerate(root)
        for rel in changed:
            print(f"wrote {rel}")
        print(f"{len(changed)} file(s) written")
        return
    stale = outdated(root)
    if args.check:
        _report(stale)
        sys.exit(1 if stale else 0)
    print(render(rows(root)))
    print()
    _report(stale)


if __name__ == "__main__":
    main()
