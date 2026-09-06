"""Tests for tools/inventory.py against the shipped fixture vaults.

The generator reads the files rather than a register, so the fixture vaults are
the subject: `minimal/` carries one source per source type, one topic map with
both generated regions and one glossary entry with its example region, and the
temporary vaults below add the states a conformant fixture cannot show, an
original that has not been ingested, a state document without the markers, and a
topic map whose regions still have to be inserted.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from tools.inventory import (
    BEGIN,
    END,
    Region,
    outdated,
    regenerate,
    regions,
    render,
    rows,
    write,
)

REPO = Path(__file__).parents[1]
MINIMAL = REPO / "tests" / "fixtures" / "minimal"

ASSERTION_TITLE = (
    "Plot metering coincided with a water use reduction of roughly a third"
)
GLOSSARY_ENTRY = "glossary/metering.md"
TOPIC_MAP = "30_assertions/MOC-Water.md"

STATE = f"""---
title: State
---

# State

## Source inventory

{BEGIN}
| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
| stale row that predates the last ingest | | | | | |
{END}

## Open work
"""


def _row(root: Path, source_starts_with: str):
    (found,) = [r for r in rows(root) if r.source.startswith(source_starts_with)]
    return found


def test_a_distilled_document_carries_both_links() -> None:
    row = _row(MINIMAL, "Annual Water Report")
    assert row.type == "document"
    assert row.channel == "handover"
    assert row.representation == "[[10_markdown/documents/report-garden-water-2026]]"
    assert row.distillate == "[[20_distillates/documents/report-garden-water-2026]]"
    assert row.status == "distilled"


def test_a_publication_row_comes_from_the_csl_record() -> None:
    row = _row(MINIMAL, "Water Metering in Community Gardens")
    assert (row.type, row.channel, row.representation) == (
        "publication",
        "import",
        "—",
    )
    assert row.distillate == "[[20_distillates/publications/example-2024-metering]]"
    assert row.status == "distilled"


def test_the_data_source_is_listed_with_its_type() -> None:
    row = _row(MINIMAL, "Quarterly water meter readings")
    assert (row.type, row.status) == ("data", "distilled")


def test_a_representation_without_a_distillate_is_ingested(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "20_distillates" / "documents" / "report-garden-water-2026.md").unlink()
    row = _row(root, "Annual Water Report")
    assert (row.distillate, row.status) == ("—", "ingested")


def test_an_original_that_no_representation_names_is_new(tmp_path: Path) -> None:
    """00_sources/ is gitignored, so this state exists only on a working copy."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "00_sources").mkdir()
    (root / "00_sources" / "README.md").write_text("ignored", encoding="utf-8")
    (root / "00_sources" / "new-handover.pdf").write_bytes(b"%PDF-")
    row = _row(root, "new-handover.pdf")
    assert (row.representation, row.distillate, row.status) == ("—", "—", "new")
    assert not [r for r in rows(root) if r.source == "README.md"]


def test_an_original_already_ingested_raises_no_second_row(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "00_sources").mkdir()
    (root / "00_sources" / "report-garden-water-2026.pdf").write_bytes(b"%PDF-")
    assert not [r for r in rows(root) if r.source.endswith(".pdf")]


def test_two_distillates_of_one_source_both_appear() -> None:
    """The schema forbids the state, so the inventory has to show it.

    The broken fixture hangs several distillates on one representation; keying
    the table by the representation alone would silently drop all but one.
    """
    broken = REPO / "tests" / "fixtures" / "broken"
    listed = [
        row.distillate
        for row in rows(broken)
        if row.representation == "[[10_markdown/documents/note]]"
    ]
    assert len(listed) == len(set(listed)) > 1


def test_a_missing_source_folder_is_no_finding() -> None:
    assert not (MINIMAL / "00_sources").exists()
    assert rows(MINIMAL)


def test_the_table_carries_the_declared_columns() -> None:
    table = render(rows(MINIMAL)).splitlines()
    assert table[0] == (
        "| Source | Type | Channel | Markdown representation | Distillate | Status |"
    )
    assert table[1] == "|---|---|---|---|---|---|"
    assert len(table) == 2 + len(rows(MINIMAL))


def test_the_generated_table_is_stable() -> None:
    assert render(rows(MINIMAL)) == render(rows(MINIMAL))


def test_write_replaces_the_marked_block(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "knowledge" / "state.md").write_text(STATE, encoding="utf-8")
    table = render(rows(root))
    write(root, table)
    text = (root / "knowledge" / "state.md").read_text(encoding="utf-8")
    assert f"{BEGIN}\n{table}\n{END}" in text
    assert "stale row that predates the last ingest" not in text
    assert text.startswith("---\ntitle: State\n---")
    assert text.rstrip().endswith("## Open work")


def test_write_is_idempotent(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "knowledge" / "state.md").write_text(STATE, encoding="utf-8")
    write(root, render(rows(root)))
    once = (root / "knowledge" / "state.md").read_text(encoding="utf-8")
    write(root, render(rows(root)))
    assert (root / "knowledge" / "state.md").read_text(encoding="utf-8") == once


def test_missing_markers_are_a_clear_error(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "knowledge" / "state.md").write_text(
        "---\ntitle: State\n---\n\n# State\n", encoding="utf-8"
    )
    with pytest.raises(SystemExit) as raised:
        write(root, "| |")
    assert BEGIN in str(raised.value)


def test_a_missing_state_document_is_a_clear_error(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as raised:
        write(tmp_path, "| |")
    assert "knowledge/state.md" in str(raised.value)


UNDECLARED_ENTRY = """---
type: glossary
term: "greywater"
created: 2026-07-11
updated: 2026-07-11
---

# Greywater

Water from washing that no assertion of this fixture speaks about.

## Examples

<!-- examples:begin -->
<!-- examples:end -->
"""

SECOND_ASSERTION = """---
type: assertion
topics: ["[[Water]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/report-garden-water-2026#^s3]]"
phenomena: ["[[glossary/metering]]"]
created: 2026-07-11
updated: 2026-07-11
---

# A wet summer accompanied the metering year

## Support

- [[20_distillates/documents/report-garden-water-2026#^s3]] — the board names it.
"""

MAP_WITHOUT_REGIONS = """---
type: moc
topic: "Water"
created: 2026-07-11
updated: 2026-07-11
---

# MOC: Water

A lead sentence a person wrote.

## Open questions

- A question that belongs to a person.
"""

MAP_WITH_A_HEADING = """---
type: moc
topic: "Water"
created: 2026-07-11
updated: 2026-07-11
---

# MOC: Water

A lead sentence a person wrote.

## Assertions

- [[30_assertions/metering-reduces-water-use]] — a hand-written line.
"""


def _vault(tmp_path: Path) -> Path:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    return root


def _region(root: Path, rel: str, name: str) -> Region:
    (found,) = [r for r in regions(root)[root / rel] if r.name == name]
    return found


def _run_cli(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """The generator writes UTF-8, which the locale encoding of the caller is not."""
    return subprocess.run(
        [sys.executable, str(REPO / "tools" / "inventory.py"), str(root), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def test_the_example_region_lists_the_assertions_of_the_phenomenon() -> None:
    """One line per assertion, with its grounding anchors indented below it."""
    assert _region(MINIMAL, GLOSSARY_ENTRY, "examples").body == (
        f"- [[30_assertions/metering-reduces-water-use]] — {ASSERTION_TITLE}\n"
        "  - [[20_distillates/documents/report-garden-water-2026#^s2]]\n"
        "  - [[20_distillates/data/water-readings-2025#^s1]]\n"
        "  - [[20_distillates/publications/example-2024-metering#^s1]]"
    )


def test_a_phenomenon_no_assertion_declares_says_so(tmp_path: Path) -> None:
    root = _vault(tmp_path)
    (root / "glossary" / "greywater.md").write_text(UNDECLARED_ENTRY, encoding="utf-8")
    assert _region(root, "glossary/greywater.md", "examples").body == (
        "- No assertion declares this phenomenon yet."
    )


def test_the_topic_map_lists_the_distillates_its_assertions_ground_in() -> None:
    assert _region(MINIMAL, TOPIC_MAP, "distillates").body == (
        "- [[20_distillates/data/water-readings-2025]]\n"
        "- [[20_distillates/documents/report-garden-water-2026]]\n"
        "- [[20_distillates/publications/example-2024-metering]]"
    )


def test_a_distillate_of_the_topic_is_listed_without_an_assertion(
    tmp_path: Path,
) -> None:
    """A source is registered under its topic before any assertion rests on it."""
    root = _vault(tmp_path)
    assertion = root / "30_assertions" / "metering-reduces-water-use.md"
    assertion.write_text(
        assertion.read_text(encoding="utf-8").replace(
            '  - "[[20_distillates/data/water-readings-2025#^s1]]"\n', ""
        ),
        encoding="utf-8",
    )
    body = _region(root, TOPIC_MAP, "distillates").body
    assert "- [[20_distillates/data/water-readings-2025]]" in body
    assert len(body.splitlines()) == 3


def test_the_topic_map_lists_the_assertions_of_its_topic() -> None:
    assert _region(MINIMAL, TOPIC_MAP, "assertions").body == (
        f"- [[30_assertions/metering-reduces-water-use]] — {ASSERTION_TITLE}"
    )


def test_both_generated_lists_are_sorted_by_slug(tmp_path: Path) -> None:
    """A second assertion sorts above the first one and shares its distillate."""
    root = _vault(tmp_path)
    (root / "30_assertions" / "colder-summer-lowered-use.md").write_text(
        SECOND_ASSERTION, encoding="utf-8"
    )
    assert _region(root, TOPIC_MAP, "assertions").body.splitlines() == [
        "- [[30_assertions/colder-summer-lowered-use]] — "
        "A wet summer accompanied the metering year",
        f"- [[30_assertions/metering-reduces-water-use]] — {ASSERTION_TITLE}",
    ]
    assert _region(root, GLOSSARY_ENTRY, "examples").body.splitlines()[0].startswith(
        "- [[30_assertions/colder-summer-lowered-use]]"
    )
    # The distillate carries both assertions and is listed once.
    assert _region(root, TOPIC_MAP, "distillates").body.count(
        "report-garden-water-2026"
    ) == 1


def test_the_shipped_fixture_carries_every_region_up_to_date() -> None:
    assert outdated(MINIMAL) == []


def test_a_stale_region_is_reported_by_path_and_by_name(tmp_path: Path) -> None:
    root = _vault(tmp_path)
    entry = root / "glossary" / "metering.md"
    entry.write_text(
        entry.read_text(encoding="utf-8").replace(
            "<!-- examples:end -->", "- an entry no assertion declares\n<!-- examples:end -->"
        ),
        encoding="utf-8",
    )
    assert outdated(root) == [(GLOSSARY_ENTRY, "generated region examples is out of date")]


def test_a_map_without_markers_gains_its_regions_above_the_open_questions(
    tmp_path: Path,
) -> None:
    root = _vault(tmp_path)
    (root / TOPIC_MAP).write_text(MAP_WITHOUT_REGIONS, encoding="utf-8")
    assert regenerate(root) == [TOPIC_MAP]
    text = (root / TOPIC_MAP).read_text(encoding="utf-8")
    assert (
        text.index("## Sources and distillates")
        < text.index("## Assertions")
        < text.index("## Open questions")
    )
    assert "A lead sentence a person wrote." in text
    assert "- A question that belongs to a person." in text
    assert outdated(root) == []


def test_an_existing_heading_keeps_the_lines_a_person_wrote(tmp_path: Path) -> None:
    """The generator inserts under the heading and deletes nothing below it."""
    root = _vault(tmp_path)
    (root / TOPIC_MAP).write_text(MAP_WITH_A_HEADING, encoding="utf-8")
    regenerate(root)
    text = (root / TOPIC_MAP).read_text(encoding="utf-8")
    assert text.count("## Assertions") == 1
    assert "- [[30_assertions/metering-reduces-water-use]] — a hand-written line." in text
    assert text.index("<!-- assertions:end -->") < text.index("a hand-written line")
    assert outdated(root) == []


def test_regenerating_a_current_vault_writes_nothing(tmp_path: Path) -> None:
    root = _vault(tmp_path)
    (root / TOPIC_MAP).write_text(MAP_WITHOUT_REGIONS, encoding="utf-8")
    regenerate(root)
    once = (root / TOPIC_MAP).read_text(encoding="utf-8")
    assert regenerate(root) == []
    assert (root / TOPIC_MAP).read_text(encoding="utf-8") == once


def test_the_check_mode_passes_on_the_clean_fixture() -> None:
    result = _run_cli(MINIMAL, "--check")
    assert result.returncode == 0, result.stdout
    assert "0 generated region(s) out of date" in result.stdout


def test_the_check_mode_fails_and_names_the_file(tmp_path: Path) -> None:
    root = _vault(tmp_path)
    (root / TOPIC_MAP).write_text(MAP_WITHOUT_REGIONS, encoding="utf-8")
    result = _run_cli(root, "--check")
    assert result.returncode == 1
    assert TOPIC_MAP in result.stdout
    assert "2 generated region(s) out of date" in result.stdout


def test_without_write_the_table_still_goes_to_stdout(tmp_path: Path) -> None:
    root = _vault(tmp_path)
    (root / TOPIC_MAP).write_text(MAP_WITHOUT_REGIONS, encoding="utf-8")
    result = _run_cli(root)
    assert result.returncode == 0, result.stderr
    assert render(rows(root)) in result.stdout
    assert TOPIC_MAP in result.stdout
    assert (root / TOPIC_MAP).read_text(encoding="utf-8") == MAP_WITHOUT_REGIONS


def test_the_write_mode_regenerates_every_region(tmp_path: Path) -> None:
    root = _vault(tmp_path)
    (root / TOPIC_MAP).write_text(MAP_WITHOUT_REGIONS, encoding="utf-8")
    (root / "knowledge" / "state.md").write_text(STATE, encoding="utf-8")
    result = _run_cli(root, "--write")
    assert result.returncode == 0, result.stderr
    assert outdated(root) == []
    assert "stale row that predates the last ingest" not in (
        root / "knowledge" / "state.md"
    ).read_text(encoding="utf-8")
