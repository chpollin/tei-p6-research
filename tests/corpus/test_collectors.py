from tools.corpus.git_snapshot import parse_tree, repository_slug
from tools.corpus.github_snapshot import metadata, next_link
from tools.corpus.github_org_census import repository_metadata
from tools.corpus.http_store import canonical_url
from tools.corpus.sourceforge_snapshot import paged_url, public_ticket_metadata
from tools.corpus.web_census import extract_links, is_allowed


def test_canonical_url_removes_fragment_and_sorts_query() -> None:
    assert canonical_url("HTTPS://EXAMPLE.org/a?z=2&a=1#part") == (
        "https://example.org/a?a=1&z=2"
    )


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


def test_allowed_prefix_and_binary_policy() -> None:
    prefixes = ["https://example.org/archive/"]
    assert is_allowed("https://example.org/archive/a.html", prefixes, False)
    assert is_allowed("https://example.org/archive/4.12.0/", prefixes, False)
    assert not is_allowed("https://example.org/archive/a.pdf", prefixes, False)
    assert is_allowed("https://example.org/archive/a.pdf", prefixes, True)
    assert not is_allowed("https://example.org/other/a.html", prefixes, True)


def test_parse_git_tree() -> None:
    raw = (
        "100644 blob aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\tz.xml\0"
        "100644 blob bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\ta.xml\0"
    )
    assert [entry["path"] for entry in parse_tree(raw)] == ["a.xml", "z.xml"]


def test_repository_slug() -> None:
    assert repository_slug("https://github.com/TEIC/TEI.git") == "TEIC-TEI"


def test_next_link() -> None:
    header = (
        '<https://api.github.com/items?page=2>; rel="next", '
        '<https://api.github.com/items?page=8>; rel="last"'
    )
    assert next_link(header) == "https://api.github.com/items?page=2"


def test_github_metadata_excludes_body() -> None:
    record = metadata(
        "issue",
        {
            "id": 1,
            "node_id": "I_1",
            "number": 7,
            "title": "Example",
            "body": "untrusted full text",
            "user": {"node_id": "U_1", "login": "person"},
            "labels": [{"name": "bug"}],
        },
    )
    assert record["title"] == "Example"
    assert record["author_node_id"] == "U_1"
    assert record["labels"] == ["bug"]
    assert "body" not in record
    assert "login" not in record


def test_sourceforge_pagination_is_canonical() -> None:
    assert paged_url("https://sourceforge.net/rest/p/tei/bugs/", 2) == (
        "https://sourceforge.net/rest/p/tei/bugs?limit=100&page=2"
    )


def test_sourceforge_normalized_record_excludes_description() -> None:
    result = public_ticket_metadata(
        {
            "ticket_num": 7,
            "description": "raw prose",
            "summary": "Short title",
            "discussion_thread": {"_id": "thread-1"},
        },
        "bugs",
    )
    assert result["body_present_in_raw"] is True
    assert "description" not in result


def test_github_org_repository_metadata() -> None:
    result = repository_metadata(
        {"id": 1, "full_name": "TEIC/TEI", "license": {"spdx_id": "BSD-2-Clause"}}
    )
    assert result["full_name"] == "TEIC/TEI"
    assert result["license_spdx_id"] == "BSD-2-Clause"
