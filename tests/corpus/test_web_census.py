"""Bounded web crawl: one link policy, gaps for everything not retrieved."""

import json

import pytest

from tools.corpus.web_census import crawl, extract_links, is_allowed

ROOT = "https://example.org/index.html"
PREFIX = "https://example.org/"


def run(tmp_path, **overrides) -> dict:
    arguments = {
        "source_id": "tei-website-records",
        "root_url": ROOT,
        "allow_prefixes": [PREFIX],
        "depth": 1,
        "max_pages": 100,
        "include_binary": False,
        "raw_root": tmp_path / "raw",
        "normalized_output": tmp_path / "census.jsonl",
        "manifest_output": tmp_path / "run.yaml",
    }
    return crawl(**(arguments | overrides))


def records(tmp_path) -> list[dict]:
    return [
        json.loads(line)
        for line in (tmp_path / "census.jsonl").read_text(encoding="utf-8").splitlines()
    ]


def test_extract_links_resolves_and_deduplicates() -> None:
    body = b'<a href="one.html#x">One</a><a href="one.html">Again</a>'
    assert extract_links("https://example.org/root/", body, "text/html") == [
        "https://example.org/root/one.html"
    ]


def test_extract_links_tolerates_legacy_sgml_declarations() -> None:
    body = b'''<![ malformed><a href="paper.html">Paper</a>'''
    assert extract_links("https://example.org/archive/", body, "text/html") == [
        "https://example.org/archive/paper.html"
    ]


def test_extract_links_ignores_non_markup() -> None:
    assert extract_links("https://example.org/", b'<a href="x.html">', "application/pdf") == []


def test_allowed_prefix_and_binary_policy() -> None:
    prefixes = [PREFIX]
    assert is_allowed("https://example.org/a.html", prefixes, False)
    assert is_allowed("https://example.org/4.12.0/", prefixes, False)
    assert not is_allowed("https://example.org/a.pdf", prefixes, False)
    assert is_allowed("https://example.org/a.pdf", prefixes, True)
    assert not is_allowed("https://other.org/a.html", prefixes, True)


def test_a_fully_retrieved_crawl_is_observable_complete(tmp_path, fake_http) -> None:
    fake_http.serve(ROOT, b'<a href="page.html">Page</a>')
    fake_http.serve("https://example.org/page.html", b"<p>Leaf</p>")

    manifest = run(tmp_path)

    assert manifest["gaps"] == []
    assert manifest["status"] == "observable-complete"
    assert manifest["counts"]["responses"] == 2
    assert [row["depth"] for row in records(tmp_path)] == [0, 1]


def test_external_binary_and_error_links_are_accounted_for(tmp_path, fake_http) -> None:
    fake_http.serve(
        ROOT,
        b'<a href="page.html">Page</a>'
        b'<a href="report.pdf">Report</a>'
        b'<a href="missing.html">Missing</a>'
        b'<a href="https://elsewhere.org/x.html">Elsewhere</a>',
    )
    fake_http.serve("https://example.org/page.html", b"<p>Leaf</p>")
    fake_http.serve("https://example.org/missing.html", b"gone", status=404)

    manifest = run(tmp_path)

    assert manifest["status"] == "partial"
    assert sorted(gap["code"] for gap in manifest["gaps"]) == [
        "binary-link-inventoried-not-fetched",
        "http-error",
    ]
    assert manifest["counts"] == {
        "responses": 3,
        "successful_responses": 2,
        "external_links_inventoried": 1,
        "depth_boundary_links_inventoried": 0,
        "binary_links_inventoried_not_fetched": 1,
        "gaps": 2,
    }
    assert manifest["external_links"] == ["https://elsewhere.org/x.html"]


def test_binary_links_are_fetched_when_requested(tmp_path, fake_http) -> None:
    fake_http.serve(ROOT, b'<a href="report.pdf">Report</a>')
    fake_http.serve("https://example.org/report.pdf", b"%PDF-1.4", media_type="application/pdf")

    manifest = run(tmp_path, include_binary=True)

    assert manifest["gaps"] == []
    assert manifest["counts"]["responses"] == 2


def test_links_beyond_the_depth_are_inventoried_not_fetched(tmp_path, fake_http) -> None:
    fake_http.serve(ROOT, b'<a href="page.html">Page</a>')

    manifest = run(tmp_path, depth=0)

    assert manifest["counts"]["responses"] == 1
    assert manifest["depth_boundary_links"] == ["https://example.org/page.html"]
    assert manifest["gaps"] == []
    assert manifest["status"] == "observable-complete"


def test_the_page_limit_is_a_gap(tmp_path, fake_http) -> None:
    fake_http.serve(ROOT, b'<a href="page.html">Page</a>')
    fake_http.serve("https://example.org/page.html", b"<p>Leaf</p>")

    manifest = run(tmp_path, max_pages=1)

    assert [gap["code"] for gap in manifest["gaps"]] == ["page-limit-reached"]
    assert manifest["gaps"][0]["remaining_queue"] == 1
    assert manifest["status"] == "partial"


def test_an_unreachable_page_is_a_gap(tmp_path, fake_http) -> None:
    fake_http.serve(ROOT, b'<a href="page.html">Page</a>')

    manifest = run(tmp_path)

    assert [gap["code"] for gap in manifest["gaps"]] == ["fetch-failed"]
    assert manifest["gaps"][0]["url"] == "https://example.org/page.html"
    assert manifest["status"] == "partial"


@pytest.mark.parametrize(("depth", "max_pages"), [(-1, 10), (1, 0)])
def test_cli_rejects_an_impossible_boundary(monkeypatch, tmp_path, depth, max_pages) -> None:
    from tools.corpus import web_census

    monkeypatch.setattr(
        "sys.argv",
        [
            "web_census",
            "--source-id",
            "tei-website-records",
            "--root-url",
            ROOT,
            "--allow-prefix",
            PREFIX,
            "--depth",
            str(depth),
            "--max-pages",
            str(max_pages),
            "--normalized-output",
            str(tmp_path / "census.jsonl"),
            "--manifest-output",
            str(tmp_path / "run.yaml"),
        ],
    )
    with pytest.raises(SystemExit, match="depth must be"):
        web_census.main()
