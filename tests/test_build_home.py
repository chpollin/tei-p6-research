"""Contract checks for the canonical proposal home and its bounded examples."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from build_home import build_page  # noqa: E402
import build_home  # noqa: E402
from sitegen.assets import read_asset  # noqa: E402
from sitegen.chrome import render_header, render_footer  # noqa: E402
from sitegen.home_view import build_view, wiki_path  # noqa: E402


class Inspect(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.ids = []
        self.links = []
        self.tags = []
        self.text = []
        self.feed(page)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.tags.append((tag, values))
        if "id" in values:
            self.ids.append(values["id"])
        if tag == "a":
            self.links.append(values["href"])

    def handle_data(self, value):
        self.text.append(value)


def write(root, path, text):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


@pytest.fixture
def minimal(tmp_path, monkeypatch):
    write(tmp_path, "40_output/12-p6-design.md", """---
type: chapter
assertions: ['[[30_assertions/premise]]']
---
# A complete fixture proposal

Opening sentinel with a grounded claim.[^fact]

## Distinguish the objects

A middle sentinel and **emphasis** remain visible.[^choice]

## A final objection

Closing sentinel follows the same premise again.[^fact]

[^fact]: Grounded in [[30_assertions/premise]].
[^choice]: Posit: retain a reversible distinction. Open evidence question: which case would refute this?
""")
    write(tmp_path, "30_assertions/premise.md", """---
type: assertion
grounding: ['[[20_distillates/documents/source-1.0#^s1]]']
---
# A premise
## Statement

Actual assertion text <script>alert('unsafe')</script>.

## Support
A source.
""")
    write(tmp_path, "20_distillates/documents/source-1.0.md", """---
representation: '[[10_markdown/documents/source-1.0]]'
---
A source-specific statement. ^s1
""")
    write(tmp_path, "10_markdown/documents/source-1.0.md", """---
metadata:
  identifier: https://example.org/pinned-source
---
The original source.
""")
    write(tmp_path, "docs/p6/abstract-text-model-v0.1.md", "\n".join(f"| {name} | A definition of {name}. | ID |" for name in ("Version", "Reading", "Annotation", "Relation")))
    source = "edition-fixture"
    write(tmp_path, f"10_markdown/documents/{source}.md", """---
metadata:
  identifier: https://example.org/blob/01234567/edition.xml
  license: CC-BY-SA-4.0
---
Pinned edition fixture.
""")
    cases = {"source": source, "attribution": "Fixture editors, 2026", "projection_policy": "Whitespace collapsed for the task.", "cases": [{"case_id": "case-2-interrupted-heading", "holdout": False, "start_line": 1, "end_line": 2, "editorial_task": "Separate a note from a heading.", "primary_text": "First. Last.", "primary_segments": ["First.", "Last."], "unknown_hand_note_text": "6255", "editorial_note_text": "A fixture editorial explanation.", "original_xml": '<head>First.<note>6255</note>Last.<script>inert</script></head>'}]}
    write(tmp_path, "experiments/editorial_cases/cases.json", json.dumps(cases))
    synthetic = {"versions": [{"id": "v1", "content": "abcdef"}], "agents": [{"id": "ada", "label": "Editor Ada"}], "selections": [{"id": "selected", "version": "v1", "selector": {"segments": [{"start": 0, "end": 4, "quote": "abcd"}]}}], "readings": [{"agent": "ada", "nodes": [{"selection": "selected"}]}]}
    write(tmp_path, "experiments/abstract_text_v01/examples/competing-readings.json", json.dumps(synthetic))
    from sitegen import comparison_view
    comparison = {"cases": [{"id": "fixture", "title": "Fixture example", "phenomenon": "crossing readings", "source_kind": "Synthetic fixture", "description": "An independently inspectable case.", "primary_text": "First. Last.", "p5": [{"id": "inline", "title": "Inline annotation", "xml": cases["cases"][0]["original_xml"], "status": "Authored illustration", "notes": ["Fixture editors, 2026; CC BY-SA 4.0"], "sources": [{"label": "Pinned XML", "url": "https://example.org/blob/01234567/edition.xml#L1-L2"}]}], "candidate": {"status": "Fixture model", "serializations": {"json": '{"id":"v1"}', "xml": '<version id="v1"/>', "yaml": 'id: v1'}, "validation": {"valid": True, "diagnostics": []}, "notes": ["Fixture binding"]}, "formal": ["Version v1 remains fixed."], "limits": ["No complete TEI conformance claim."], "graph": {"nodes": [{"id": "v1", "label": "Version v1", "kind": "Version"}], "edges": []}, "links": []}], "coverage": [{"module": "core", "title": "Core", "status": "Planned", "phenomena": ["note"], "document_types": ["letter"]}], "bindings": [{"id": "xml", "label": "XML", "status": "Implemented"}, {"id": "rdf", "label": "RDF", "status": "Planned"}]}
    monkeypatch.setattr(comparison_view, "build_comparisons", lambda root: comparison)
    return tmp_path


def test_canonical_proposal_is_complete_visible_and_not_collapsed(minimal):
    page = build_page(minimal, "2026-09-05")
    article = re.search(r'<article class="proposal-text".*?</article>', page, re.S).group()
    assert "<details" not in article and "hidden" not in article
    assert all(text in article for text in ("Opening sentinel", "A middle sentinel", "Closing sentinel", "A final objection"))
    assert "[[" not in page and "[^" not in page


def test_footnotes_show_actual_assertion_and_keep_posits_distinct(minimal):
    page = build_page(minimal, "2026-09-05")
    assert "Actual assertion text &lt;script&gt;" in page
    assert "Source-grounded premise" in page
    assert "retain a reversible distinction." in page
    assert "which case would refute this?" in page
    assert "Source representation" in page and "Distillate ^s1" in page
    assert 'href="#ref-fact-1"' in page and 'href="#ref-fact-2"' in page


def test_untrusted_source_markup_is_inert(minimal):
    page = build_page(minimal, "2026-09-05")
    parsed = Inspect(page)
    assert sum(tag == "script" for tag, _ in parsed.tags) == 1
    assert "&lt;script&gt;inert&lt;/script&gt;" in page
    assert "<script>alert" not in page


def test_all_local_fragment_links_resolve_and_ids_are_unique(minimal):
    parsed = Inspect(build_page(minimal, "2026-09-05"))
    assert len(parsed.ids) == len(set(parsed.ids))
    assert all(href[1:] in parsed.ids for href in parsed.links if href.startswith("#"))


def test_repository_base_encodes_paths_without_inventing_github_block_ids(minimal):
    page = build_page(minimal, "2026-09-05", "https://github.com/example/repo/blob/01234567/")
    assert 'href="https://github.com/example/repo/blob/01234567/20_distillates/documents/source-1.0.md"' in page
    assert "#%5Es1" not in page
    assert wiki_path("[[20_distillates/documents/source-1.0#^s1]]") == "20_distillates/documents/source-1.0.md#^s1"


def test_case_controls_have_accessible_state_and_all_static_representations(minimal):
    page = build_page(minimal, "2026-09-05")
    parsed = Inspect(page)
    tabs = [attrs for tag, attrs in parsed.tags if tag == "button" and attrs.get("role") == "tab"]
    assert len(tabs) == 3
    assert all(attrs["aria-controls"] in parsed.ids and "aria-selected" in attrs for attrs in tabs)
    assert tabs[0]["data-case-tab"] == "comparison" and tabs[0]["aria-selected"] == "true"
    assert 'aria-live="polite"' in page
    assert "Fixture editors, 2026" in page and "CC BY-SA 4.0" in page
    assert "https://example.org/blob/01234567/edition.xml#L1-L2" in page
    assert all(f'data-binding="{binding}"' in page for binding in ("xml", "json", "yaml"))
    assert 'data-binding="rdf"' not in page
    assert "Core type relationships" in page and "Objects in this example" in page
    assert 'data-object="v1"' in page


def test_build_is_self_contained_and_reproducible(minimal):
    page = build_page(minimal, "2026-09-05")
    assert page == build_page(minimal, "2026-09-05")
    assert read_asset("home.css") in page and read_asset("home.js") in page
    assert '<script src=' not in page and '<link rel="stylesheet"' not in page
    assert "fetch(" not in read_asset("home.js")


def test_page_uses_shared_workbench_chrome_and_design_system(minimal):
    page = build_page(minimal, "2026-09-05")
    assert render_header("home") in page
    assert render_footer("2026-09-05") in page
    assert page.index(read_asset("workbench.css")) < page.index(read_asset("home.css"))


@pytest.mark.parametrize("path", ["40_output/12-p6-design.md", "30_assertions/premise.md", "20_distillates/documents/source-1.0.md", "docs/p6/abstract-text-model-v0.1.md", "experiments/editorial_cases/cases.json"])
def test_missing_required_inputs_fail_closed(minimal, path):
    (minimal / path).unlink()
    with pytest.raises(FileNotFoundError):
        build_page(minimal, "2026-09-05")


def test_missing_footnote_and_missing_grounding_block_fail_closed(minimal):
    source = minimal / "40_output/12-p6-design.md"
    source.write_text(source.read_text() + "\nUnresolved reference.[^missing]\n", encoding="utf-8")
    with pytest.raises(ValueError, match="reconcile"):
        build_page(minimal, "2026-09-05")


def test_missing_grounding_block_fails_closed(minimal):
    write(minimal, "20_distillates/documents/source-1.0.md", "---\nrepresentation: '[[10_markdown/documents/source-1.0]]'\n---\nNo requested anchor.")
    with pytest.raises(ValueError, match="Missing distillate block"):
        build_page(minimal, "2026-09-05")


def test_unsafe_link_in_canonical_input_fails_closed(minimal):
    source = minimal / "40_output/12-p6-design.md"
    source.write_text(source.read_text().replace("Opening sentinel", "[Unsafe](javascript:alert) Opening sentinel"), encoding="utf-8")
    with pytest.raises(ValueError, match="Unsafe link scheme"):
        build_page(minimal, "2026-09-05")


def test_actual_repository_preserves_all_proposal_headings_and_footnotes():
    view = build_view(REPO, "2026-09-05")
    page = build_page(REPO, "2026-09-05")
    parsed = Inspect(page)
    text = " ".join(parsed.text)
    for heading in re.findall(r"^#{1,6} (.+)$", view["body"], re.M):
        assert heading in text
    assert len(parsed.ids) == len(set(parsed.ids))
    assert all("note-" + note["id"] in parsed.ids for note in view["notes"])
    assert all(href[1:] in parsed.ids for href in parsed.links if href.startswith("#"))
    assert "Reise. 1790. England." in page
    assert "Handschriftliche Notiz" in page
    assert 'aria-current="page">Proposal' in page
    assert 'href="knowledge.html">Knowledge' in page
    assert 'href="corpus.html">Materials' in page
    assert 'href="project.html">About' in page


def test_technical_shell_starts_with_proposal_and_has_no_promotional_hero(minimal):
    page = build_page(minimal, "2026-09-05")
    assert 'class="hero"' not in page
    assert "One text." not in page
    assert page.index('<article class="proposal-text"') < page.index('id="examples"')
    assert page.count("<h1 ") == 1
    assert 'href="knowledge.html#doc-30-assertions-premise"' in page


def test_explicit_example_links_retain_deep_link_and_unknown_case_fails(minimal):
    source = minimal / "40_output/12-p6-design.md"
    source.write_text(source.read_text() + "\n[Compare](#example=fixture)\n", encoding="utf-8")
    assert 'href="#example=fixture">Compare' in build_page(minimal, "2026-09-05")
    source.write_text(source.read_text() + "\n[Missing](#example=missing)\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Unknown example"):
        build_page(minimal, "2026-09-05")


def test_mapping_refusal_has_no_invented_serialization(minimal, monkeypatch):
    from sitegen import comparison_view
    data = comparison_view.build_comparisons(minimal)
    data["cases"][0]["candidate"] = {"status": "Mapping refused", "serializations": {}, "validation": {"valid": False, "diagnostics": ["Unsupported pb"]}, "notes": []}
    monkeypatch.setattr(comparison_view, "build_comparisons", lambda root: data)
    page = build_page(minimal, "2026-09-05")
    assert "Mapping refused" in page and "Unsupported pb" in page
    assert 'data-binding="xml"' not in page
    assert 'class="mapping-unavailable"' in page
    assert "No candidate mapping" in page
    assert "Fail — candidate model validation" not in page


def test_external_comparison_links_are_checked_and_source_markup_escaped(minimal, monkeypatch):
    from sitegen import comparison_view
    data = comparison_view.build_comparisons(minimal)
    data["cases"][0]["links"] = [{"label": "unsafe", "url": "javascript:alert(1)"}]
    monkeypatch.setattr(comparison_view, "build_comparisons", lambda root: data)
    with pytest.raises(ValueError, match="Unsafe link scheme"):
        build_page(minimal, "2026-09-05")


@pytest.mark.parametrize("explicit", [False, True])
def test_cli_publishes_canonical_index_and_compatibility_alias(tmp_path, monkeypatch, explicit):
    args = ["build_home.py", "--root", str(tmp_path), "--date", "2026-09-05"]
    custom = tmp_path / "preview.html"
    if explicit:
        args.extend(["--output", str(custom)])
    monkeypatch.setattr(sys, "argv", args)
    monkeypatch.setattr(build_home, "build_page", lambda *args: "<p>Deterministic fixture</p>\n")
    build_home.main()
    if explicit:
        assert custom.is_file()
        assert not (tmp_path / "docs/index.html").exists()
    else:
        assert (tmp_path / "docs/index.html").read_bytes() == (tmp_path / "docs/home.html").read_bytes()


def test_document_and_inspector_use_spacing_instead_of_decorative_rules(minimal):
    css = read_asset("home.css")
    borders = re.findall(r"(?:^|[;{])\s*(border(?:-(?:top|right|bottom|left))?(?:-(?:width|style|color))?)\s*:\s*([^;}]+)", css)
    assert all(value.strip() in ("0", "none") for _, value in borders)
    assert not any(tag == "hr" for tag, _ in Inspect(build_page(minimal, "2026-09-05")).tags)


def test_comparison_is_primary_and_context_is_available_in_disclosure(minimal):
    page = build_page(minimal, "2026-09-05")
    case = re.search(r'<section class="comparison-case".*?(?=<aside class="home-source-license")', page, re.S).group()
    assert 'data-case-tab="description"' not in case
    assert case.index('data-case-panel="comparison"') < case.index('class="case-context"')
    assert "Context, sources and limits" in case
    assert "An independently inspectable case." in case
