"""Coverage, immutable reuse and inert XML boundaries of the full release intake."""

import html
import json
import shutil
from pathlib import Path

import pytest

from tools import ingest_git_blobs as shared
from tools import ingest_guidelines as baseline
from tools.sitegen.knowledge_page import literal
from tools.sitegen.knowledge_view import anchored_blocks
from tools.sitegen.materials_page import guidelines_reference

ROOT = Path(__file__).parents[1]


def test_baseline_uses_finite_paths_and_includes_support_xml():
    inventory = dict.fromkeys([
        baseline.MASTER, "P5/Source/Specs/name.xml", "P5/Source/Specs/readme.txt",
        "P5/Source/Guidelines/en/ND-NamesDates.xml",
        "P5/Source/Guidelines/en/Images/anthology.xml",
        "P5/Source/Guidelines/fr/ND-NamesDates.xml", "P5/Source/Defunct/old.xml",
    ], "blob")
    assert baseline.baseline_paths(inventory) == sorted([
        baseline.MASTER, "P5/Source/Specs/name.xml", "P5/Source/Guidelines/en/ND-NamesDates.xml",
        "P5/Source/Guidelines/en/Images/anthology.xml",
    ])


def test_example_includes_are_not_dependencies():
    """A quoted XInclude must never acquire or execute an example's target."""
    payload = b'''<div xmlns="http://www.tei-c.org/ns/1.0"
        xmlns:xi="http://www.w3.org/2001/XInclude">
        <xi:include href="../Specs/name.xml"/>
        <egXML xmlns="http://www.tei-c.org/ns/Examples">
            <xi:include href="https://example.invalid/private"/>
        </egXML></div>'''
    result = baseline.includes("P5/Source/Guidelines/chapter.xml", payload)
    assert [row["target"] for row in result] == ["P5/Source/Specs/name.xml"]


@pytest.mark.parametrize("payload", [
    b'<!DOCTYPE div [<!ENTITY x "expanded">]><div>&x;</div>',
    b'<!DOCTYPE div SYSTEM "https://example.invalid/private"><div/>',
])
def test_real_dtd_is_rejected_before_expansion(payload):
    with pytest.raises(ValueError, match="DTD/entity"):
        baseline.parse_xml(payload)
    with pytest.raises(ValueError, match="DTD/entity"):
        baseline.reference_blocks(payload)


def test_cdata_examples_tables_and_unicode_remain_exact():
    """Guidelines teach DTD syntax inside inert CDATA, unlike live declarations."""
    payload = '''<div xmlns="http://www.tei-c.org/ns/1.0"><head>Example</head>
<p>α <eg><![CDATA[<!DOCTYPE div [<!ENTITY x "preserved">]>]]></eg></p>
<table><row><cell>β</cell></row></table></div>'''.encode()
    baseline.parse_xml(payload)
    blocks = baseline.reference_blocks(payload)
    assert len(blocks) == 3
    assert '<!ENTITY x "preserved">' in blocks[1][1]
    assert '<table><row><cell>β</cell></row></table>' in blocks[2][1]
    rendered = "\n".join(body + f"\n^b{i}\n" for i, (_, body) in enumerate(blocks, 1))
    passages = anchored_blocks(rendered, "representation")
    assert "<!DOCTYPE" in passages["b2"]
    assert "β" in passages["b3"]


def test_fenced_source_content_cannot_mint_an_anchor():
    body = '```xml\n<p>Example. ^fake</p>\n^alsofake\n```\n\n^b1\n'
    result = anchored_blocks(body, "representation")
    assert set(result) == {"b1"}
    assert "^alsofake" in result["b1"]
    assert anchored_blocks('```\n^fake\n```\n\n## Next\nReal. ^r1', 'representation') == {"r1": "Real. ^r1"}


def test_html_source_whitespace_survives_without_trailing_file_spaces():
    source = '<p>Quoted text. \t\n  \tMore.  \n</p>'
    escaped = literal(source)
    assert html.unescape(escaped) == source
    assert '\t' not in escaped
    assert all(line == line.rstrip() for line in escaped.splitlines())


def test_dependency_path_escape_is_rejected():
    with pytest.raises(ValueError, match="escapes"):
        baseline.local_target("chapter.xml", "../../secret.xml")
    assert baseline.local_target("chapter.xml", "https://example.invalid/source.xml") is None


def test_interrupted_creation_does_not_leave_a_partial_immutable_file(tmp_path, monkeypatch):
    target = tmp_path / "source.md"
    write = Path.write_bytes

    def interrupted(path, payload):
        write(path, payload[:3])
        raise OSError("simulated interrupted write")

    with monkeypatch.context() as patch:
        patch.setattr(Path, "write_bytes", interrupted)
        with pytest.raises(OSError, match="interrupted"):
            shared.immutable_output(target, b"complete source", False)
    assert not target.exists()
    shared.immutable_output(target, b"complete source", False)
    assert target.read_bytes() == b"complete source"
    assert not target.with_suffix(".md.tmp").exists()


@pytest.fixture(scope="module")
def clean_checkout(tmp_path_factory):
    """Copy tracked intake inputs, deliberately excluding originals and the mirror."""
    root = tmp_path_factory.mktemp("guidelines-clean-checkout")
    for path in (shared.LOCK, shared.UPSTREAM, shared.INVENTORY, baseline.MANIFEST,
                 baseline.COVERAGE, baseline.OVERVIEW, baseline.MEMBERS, baseline.MEMBERS_MANIFEST):
        output = root / path
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, output)
    for folder in ("10_markdown/documents", "20_distillates/documents"):
        shutil.copytree(ROOT / folder, root / folder)
    return root


def test_full_admission_reproduces_without_ignored_data(clean_checkout):
    assert not (clean_checkout / "00_sources").exists()
    assert not (clean_checkout / shared.GIT_DIR).exists()
    view = baseline.build(clean_checkout, check=True)
    baseline.projection_output(clean_checkout / baseline.COVERAGE,
                               json.dumps(view, ensure_ascii=False, indent=2) + "\n", True)
    baseline.projection_output(clean_checkout / baseline.OVERVIEW, baseline.markdown(view), True)
    assert view["counts"]["sources"] == 888
    assert view["counts"]["specifications"] == 846
    assert len(view["contents"]) == 40
    assert view["publication_inventory"]["contents_pages_matched"] == 40
    assert {row["source"] for row in view["publication_inventory"]["unmatched_specifications"]} == {
        "P5/Source/Specs/re.xml", "P5/Source/Specs/teidata.key.xml",
    }
    chapters = {row["source"] for row in view["contents"] if row["part"] == "body"}
    assert all(section["heading_block"] for row in view["sources"] if row["source"] in chapters for section in row["sections"])
    assert all(row["section_review"] == "not-recorded" for row in view["sources"])
    assert not (clean_checkout / "00_sources").exists()


def test_missing_representation_fails_check(clean_checkout):
    path = clean_checkout / "10_markdown/documents/tei-p5-guidelines-use-4.12.0.md"
    payload = path.read_bytes()
    path.unlink()
    try:
        with pytest.raises(FileNotFoundError):
            baseline.build(clean_checkout, check=True)
    finally:
        path.write_bytes(payload)


def test_refresh_coverage_works_without_originals(clean_checkout, monkeypatch):
    path = clean_checkout / baseline.COVERAGE
    path.write_text("stale projection", encoding="utf-8")
    monkeypatch.setattr("sys.argv", ["ingest_guidelines", str(clean_checkout), "--refresh-coverage"])
    assert baseline.main() == 0
    assert json.loads(path.read_text(encoding="utf-8"))["counts"]["sources"] == 888
    assert not (clean_checkout / "00_sources").exists()


def test_modified_source_is_detected(clean_checkout):
    path = clean_checkout / "10_markdown/documents/tei-p5-guidelines-use-4.12.0.md"
    payload = path.read_bytes()
    path.write_bytes(payload.replace(b"<head>", b"<HEAD>", 1))
    try:
        with pytest.raises(ValueError, match="Git blob"):
            baseline.build(clean_checkout, check=True)
    finally:
        path.write_bytes(payload)


def test_projection_cannot_silently_promote_research_status(tmp_path):
    path = tmp_path / baseline.COVERAGE
    path.parent.mkdir(parents=True)
    path.write_text('{"status":"verified"}', encoding="utf-8")
    with pytest.raises(ValueError, match="stale"):
        baseline.projection_output(path, '{"status":"ingested"}', True)


def test_public_coverage_links_actual_sources_and_escapes_titles(tmp_path):
    view = json.loads((ROOT / baseline.COVERAGE).read_text(encoding="utf-8"))
    view["contents"][0]["title"] = "<script>alert(1)</script>"
    path = tmp_path / baseline.COVERAGE
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(view), encoding="utf-8")
    html = guidelines_reference(tmp_path, "https://github.com/example/repo/blob/pinned/")
    assert "<script>" not in html
    assert "&lt;script&gt;" in html
    assert "knowledge.html#doc-10-markdown-documents-tei-p5-guidelines-use-4-12-0" in html
    assert "Imported; no distillate" in html
    assert "Distillate available" in html
