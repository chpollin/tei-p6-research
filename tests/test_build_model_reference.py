"""Checks for faithful contracts, safe canonical text and navigable reference HTML."""
import json
import re
import shutil
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import build_model_reference  # noqa: E402
from build_model_reference import build_page  # noqa: E402
from sitegen.model_reference import DEFINITION, PROFILE, SPEC, REFERENCES, build_view  # noqa: E402


class Inspect(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.ids = []
        self.links = []
        self.tags = []
        self.data = []
        self.feed(page)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs["href"])

    def handle_data(self, text):
        self.data.append(text)


@pytest.fixture
def fixture_root(tmp_path):
    for path in (DEFINITION, SPEC, PROFILE):
        dest = tmp_path / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, dest)
    return tmp_path


def test_all_ten_record_kinds_and_fields_are_present():
    page = Inspect(build_page(ROOT, "2026-09-05"))
    text = " ".join(page.data)
    spec = json.loads((ROOT / SPEC).read_text(encoding="utf-8"))
    expected = {"Agent": "agents", "Concept": "concepts", "Text": "texts", "Version": "versions", "Continuity": "continuities", "Selection": "selections", "Reading": "readings", "ReadingNode": "node", "Annotation": "annotations", "Relation": "relations"}
    for name, key in expected.items():
        assert f"class-{name}" in page.ids
        for field, contract in spec["input"][key]["required"].items():
            assert field in text
            assert contract in text
    assert len([tag for tag, attrs in page.tags if tag == "section" and attrs.get("data-kind")]) == 10


def test_cardinalities_distinguish_positive_claims_and_nested_nodes():
    refs = {(source, field): (target, count, extra) for source, field, target, count, extra in REFERENCES}
    assert refs["Continuity", "versions"][:2] == ("Version", "1..n")
    assert refs["Version", "parents"][:2] == ("Version", "0..n")
    assert refs["ReadingNode", "parent"][:2] == ("ReadingNode", "0..1")
    assert refs["Reading", "nodes"][:2] == ("ReadingNode", "1..n")
    assert "at least one" in refs["Continuity", "text"][2]
    assert "exactly one reading" in refs["Reading", "nodes"][2]


def test_generic_relation_endpoints_are_not_restricted_to_domain_entities():
    page = Inspect(build_page(ROOT, "2026-09-05"))
    text = " ".join(page.data)
    assert "not an extra record kind" in text
    assert "including Relation itself; self-links are permitted" in text
    assert "including Relation itself; relation cycles are permitted" in text
    assert "its label adds no endpoint rule" in text
    assert "subtype inference" in text
    assert "Every listed field is required" in text


def test_three_selectors_are_values_and_resolution_is_not_an_extra_record():
    page = Inspect(build_page(ROOT, "2026-09-05"))
    text = " ".join(page.data)
    for name in ("point", "ranges", "quote"):
        assert f"selector-{name}" in page.ids
    assert "Neither selectors nor results are identified package records" in text


def test_all_rules_and_operations_use_exact_contract_text():
    text = " ".join(Inspect(build_page(ROOT, "2026-09-05")).data)
    for path in (SPEC, PROFILE):
        contract = json.loads((ROOT / path).read_text(encoding="utf-8"))
        for group in ("rules", "operations"):
            for key, value in contract[group].items():
                assert key in text
                assert value in text


def test_full_canonical_definition_is_regenerated_not_a_summary(fixture_root):
    path = fixture_root / DEFINITION
    canonical = path.read_text(encoding="utf-8")
    path.write_text(canonical + "\n\n## Added definition section\n\nUnique final formal paragraph.\n", encoding="utf-8")
    page = Inspect(build_page(fixture_root, "2026-09-05"))
    text = " ".join(page.data)
    assert "Unique final formal paragraph." in text
    assert "Added definition section" in text
    assert "The prototype accepts only strings encodable as UTF-8" in text
    assert "These boundaries must be challenged" in text
    for heading in re.findall(r"^## (.+)$", canonical, re.M):
        assert heading in text


def test_canonical_links_are_repository_relative_or_pinned_to_requested_base():
    base = "https://github.com/example/project/blob/frozen/"
    page = Inspect(build_page(ROOT, "2026-09-05", base))
    assert base + DEFINITION in page.links
    assert base + SPEC in page.links
    assert base + "40_output/12-p6-design.md" in page.links
    local = Inspect(build_page(ROOT, "2026-09-05"))
    assert "../" + DEFINITION in local.links


def test_unique_ids_and_internal_link_destinations_exist():
    page = Inspect(build_page(ROOT, "2026-09-05"))
    assert len(page.ids) == len(set(page.ids))
    assert {href[1:] for href in page.links if href.startswith("#")} <= set(page.ids)
    assert len([tag for tag, _ in page.tags if tag == "h1"]) == 1
    assert any(tag == "a" and attrs.get("aria-current") == "page" and attrs.get("href") == "model.html" for tag, attrs in page.tags)


def test_optional_profile_does_not_silently_change_base_conformance():
    text = " ".join(Inspect(build_page(ROOT, "2026-09-05")).data)
    assert "requires its own validation" in text
    assert "introduces no new record kinds" in text
    assert "ep-derived-from" in text
    assert "ep-supersedes" in text
    assert "No cross-agent supersession" in text


def test_escapes_canonical_markup_and_contract_values(fixture_root):
    path = fixture_root / DEFINITION
    path.write_text(path.read_text(encoding="utf-8") + '\n\n<script>alert("x")</script>\n', encoding="utf-8")
    path = fixture_root / SPEC
    spec = json.loads(path.read_text(encoding="utf-8"))
    spec["input"]["agents"]["required"]["label"] = '<img src=x onerror="alert(1)">'
    path.write_text(json.dumps(spec), encoding="utf-8")
    page = build_page(fixture_root, "2026-09-05")
    assert '&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;' in page
    assert "<img src=x" not in page
    assert '&lt;img src=x onerror=&quot;alert(1)&quot;&gt;' in page


@pytest.mark.parametrize("base", ["javascript:alert(1)", "http://example.org/", "//example.org/", "https://example.org/#fragment", "https://example.org/?query=1"])
def test_invalid_repository_bases_rejected(base):
    with pytest.raises(ValueError):
        build_page(ROOT, "2026-09-05", base)


def test_unsafe_link_in_canonical_text_fails_build(fixture_root):
    path = fixture_root / DEFINITION
    path.write_text(path.read_text(encoding="utf-8") + '\n\n[Bad](javascript:alert)\n', encoding="utf-8")
    with pytest.raises(ValueError, match="Unsafe"):
        build_page(fixture_root, "2026-09-05")


def test_definition_must_retain_all_canonical_class_rows(fixture_root):
    path = fixture_root / DEFINITION
    path.write_text(path.read_text(encoding="utf-8").replace("| Agent |", "| Removed |"), encoding="utf-8")
    with pytest.raises(ValueError, match="object row: Agent"):
        build_view(fixture_root, "2026-09-05")


def test_unsupported_contract_change_fails_instead_of_displaying_stale_diagram(fixture_root):
    path = fixture_root / SPEC
    spec = json.loads(path.read_text(encoding="utf-8"))
    del spec["input"]["readings"]["required"]["nodes"]
    path.write_text(json.dumps(spec), encoding="utf-8")
    with pytest.raises(ValueError, match="Diagram field no longer exists"):
        build_view(fixture_root, "2026-09-05")


def test_no_decorative_horizontal_rules_and_static_content_visible():
    page = Inspect(build_page(ROOT, "2026-09-05"))
    assert not any(tag == "hr" for tag, _ in page.tags)
    for tag, attrs in page.tags:
        if tag == "section" and attrs.get("data-kind"):
            assert "hidden" not in attrs
    css = (ROOT / "tools/sitegen/assets/model.css").read_text(encoding="utf-8")
    assert not re.search(r"border-(top|bottom)\s*:", css)
    assert "model-edge path" in css


def test_deterministic_build_and_cli_output(fixture_root, monkeypatch):
    expected = build_page(fixture_root, "2026-09-05")
    assert expected == build_page(fixture_root, "2026-09-05")
    monkeypatch.setattr(sys, "argv", ["build_model_reference.py", "--root", str(fixture_root), "--date", "2026-09-05"])
    build_model_reference.main()
    assert (fixture_root / "docs/model.html").read_bytes() == expected.encode("utf-8")


def test_invalid_date_rejected():
    with pytest.raises(ValueError):
        build_page(ROOT, "2026-99-01")
