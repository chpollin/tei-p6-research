"""Review context must preserve source identity and reject unresolved locators."""

import pytest

from tools.check_text_structures import ancestor_context


def test_attribute_identity_changes_review_context_without_changing_description():
    source = b'<classSpec ident="linking"><attList><attDef ident="next"><desc>Points to an element.</desc></attDef></attList></classSpec>'
    locator = "/classSpec[1]/attList[1]/attDef[1]/desc[1]"
    context = ancestor_context(source, locator)
    assert '"ident": "next"' in context
    assert context != ancestor_context(source.replace(b'"next"', b'"prev"'), locator)


@pytest.mark.parametrize("locator", ["/other[1]", "/div[0]", "/div[1]/p[2]", "/div[1]/../p[1]"])
def test_missing_or_unsupported_context_fails(locator):
    with pytest.raises(ValueError):
        ancestor_context(b"<div><p>Text</p></div>", locator)


def test_heading_context_retains_inline_text_and_is_inert():
    source = b'<div xml:id="intro"><head>A <name>source</name> heading</head><p>Text</p></div>'
    context = ancestor_context(source, "/div[1]/p[1]")
    assert '"id": "intro"' in context
    assert 'heading="A source heading"' in context


def test_context_rejects_live_doctype():
    with pytest.raises(ValueError):
        ancestor_context(b'<!DOCTYPE div SYSTEM "https://example.org/inert.dtd"><div/>', "/div[1]")
