"""Knowledge navigation must preserve actual, immediate provenance boundaries."""
import json
from html.parser import HTMLParser
from pathlib import Path

import pytest

from tools.build_knowledge import build_page
from tools.sitegen.knowledge_view import anchored_blocks, block_id, build_view
from tools.sitegen.markup import doc_id

ROOT = Path(__file__).parents[1]


def test_guidelines_filters_and_declared_links_in_real_page():
    page = Page(build_page(ROOT, '2026-09-07'))
    assert {'knowledge-topic', 'knowledge-module', 'knowledge-source-kind'} <= set(page.ids)
    ids = set(page.ids)
    assert all(href[1:] in ids for href in page.links if href.startswith('#'))
    sources = [attrs for tag, attrs in page.tags if tag == 'details' and attrs.get('data-source-kind')]
    assert len(sources) == 888
    app = next(attrs for attrs in sources if attrs['id'] == doc_id('10_markdown/documents/tei-p5-app-4.12.0.md'))
    assert app['data-module'] == 'textcrit'
    assert app['data-source-kind'] == 'elementSpec'
    assert 'Critical Apparatus' in json.loads(app['data-topics'])


def test_navigation_order_is_independent_of_platform_path_order(vault):
    write(vault, 'knowledge/INDEX.md', '# Index\n')
    write(vault, 'knowledge/architecture.md', '# Architecture\n')
    write(vault, 'glossary/Zeta.md', '# Zeta\n')
    write(vault, 'glossary/alpha.md', '# Alpha\n')
    navigation = build_view(vault, '2026-09-07')['navigation']
    assert [item['path'] for item in navigation] == [
        '30_assertions/MOC-Test.md',
        'knowledge/architecture.md', 'knowledge/INDEX.md',
        'knowledge/state.md', 'knowledge/text-model.md',
        'glossary/alpha.md', 'glossary/Zeta.md',
    ]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.tags = [], [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs['href'])


def write(root, path, content):
    file = root / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content, encoding='utf-8')


def replace(root, path, before, after):
    file = root / path
    text = file.read_text(encoding='utf-8')
    assert before in text
    file.write_text(text.replace(before, after), encoding='utf-8')


@pytest.fixture
def vault(tmp_path):
    write(tmp_path, '10_markdown/documents/source.md', '''---
type: representation
source-type: document
source: '[[00_sources/original.xml]]'
metadata:
  title: A source
  creator: Fixture publisher
  date: '2026-01-02'
  license: CC-BY-4.0
  confidential: false
  identifier: https://example.org/blob/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/source.xml
---
# A source

```xml
<unsafe>Never execute me</unsafe>
Fake marker in original source ^fake
```

Exact source <script>alert(1)</script> text. ^r1

Other source paragraph. ^r2
''')
    write(tmp_path, '20_distillates/documents/source.md', '''---
type: distillate
source-type: document
representation: '[[10_markdown/documents/source]]'
status: validated
checked:
  validation: 2026-09-05
  machine-review: 2026-09-05
---
# Distillate: A source

## Core statements

- A narrow reading. [[10_markdown/documents/source#^r1]] ^s1
- A second reading. [[10_markdown/documents/source#^r2]] ^s2

## Appraisal

This is an interpretation, not another statement.
''')
    write(tmp_path, '30_assertions/claim.md', '''---
type: assertion
status: grounded
grounding: ['[[20_distillates/documents/source#^s1]]']
---
# Claim <img src=x onerror=alert(1)>

## Statement

The precise claim is <script>alert(2)</script>.
''')
    write(tmp_path, '30_assertions/MOC-Test.md', '''---
type: moc
---
# Test topic
''')
    write(tmp_path, '40_output/12-p6-design.md', '''---
type: chapter
status: grounded
assertions: ['[[30_assertions/claim]]']
posits: 1
---
# Proposal

A grounded premise.[^fact] An explicit choice.[^choice]

[^fact]: Grounded in [[30_assertions/claim]].
[^choice]: Posit: choose this. Open evidence question: Is it useful?
''')
    write(tmp_path, 'knowledge/state.md', '# State\n\nA planned chapter is not an artifact.')
    write(tmp_path, 'knowledge/text-model.md', '# Text model\n\nProject reasoning.')
    return tmp_path


def test_actual_vault_all_assertions_and_documents_are_present():
    view = build_view(ROOT, '2026-09-05')
    found = {entry['path'] for entry in view['entries']}
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / '30_assertions').glob('*.md') if not p.name.startswith('MOC-')}
    assert actual <= found
    navigation = {entry['path'] for entry in view['navigation']}
    assert {p.relative_to(ROOT).as_posix() for p in (ROOT / 'knowledge').glob('*.md')} <= navigation
    assert '40_output/01-p5-architecture.md' not in found
    assert view['counts']['assertion'] == len(actual)


def test_full_chain_resolves_exact_blocks_and_backlinks(vault):
    view = build_view(vault, '2026-09-05')
    entries = {e['path']: e for e in view['entries']}
    assert entries['30_assertions/claim.md']['edges'][0]['href'] == '#' + block_id('20_distillates/documents/source.md', 's1')
    assert entries['20_distillates/documents/source.md']['edges'][0]['href'] == '#' + block_id('10_markdown/documents/source.md', 'r1')
    assert entries['10_markdown/documents/source.md']['backlinks'][0]['href'] == '#' + block_id('20_distillates/documents/source.md', 's1')
    assert entries['20_distillates/documents/source.md']['backlinks'][0]['target_anchor'] == 's1'
    page = Page(build_page(vault, '2026-09-05'))
    assert len(page.ids) == len(set(page.ids))
    assert all(href[1:] in page.ids for href in page.links if href.startswith('#'))


def test_output_is_deterministic_and_escaped(vault):
    page = build_page(vault, '2026-09-05')
    assert page == build_page(vault, '2026-09-05')
    assert '<script>alert' not in page
    assert '<img src=x' not in page
    assert '&lt;script&gt;alert(1)&lt;/script&gt;' in page
    assert 'Never execute me' not in page
    assert 'Fake marker in original source' not in page
    assert '00_sources/original.xml' in page
    assert not any('00_sources/' in href for href in Page(page).links)
    assert 'human verification' in page
    assert not any(e['status'] == 'verified' for e in build_view(vault, '2026-09-05')['entries'])


@pytest.mark.parametrize(('path', 'before', 'after', 'message'), [
    ('30_assertions/claim.md', 'source#^s1', 'source#^missing', 'Missing grounding anchor'),
    ('30_assertions/claim.md', 'source#^s1', 'absent#^s1', 'grounding target'),
    ('30_assertions/claim.md', 'source#^s1', 'source', 'exact block'),
    ('20_distillates/documents/source.md', 'source#^r1', 'source#^missing', 'Missing grounding anchor'),
    ('20_distillates/documents/source.md', 'source#^r1', 'source#^fake', 'Missing grounding anchor'),
    ('20_distillates/documents/source.md', 'source#^r1', 'source', 'exact block'),
    ('10_markdown/documents/source.md', 'confidential: false', 'confidential: true', 'Confidential'),
    ('30_assertions/claim.md', 'status: grounded', 'status: verified', 'verification date'),
    ('40_output/12-p6-design.md', '[^fact]: Grounded in [[30_assertions/claim]].', '[^fact]: Grounded in [[30_assertions/missing]].', 'mirror'),
])
def test_invalid_provenance_fails_closed(vault, path, before, after, message):
    replace(vault, path, before, after)
    with pytest.raises(ValueError, match=message):
        build_page(vault, '2026-09-05')


@pytest.mark.parametrize('url', ['javascript:alert(1)', '//example.org/path', 'https://good.example\\@evil.example/', 'https://user:secret@example.org/', ' https://example.org/'])
def test_unsafe_source_urls_fail(vault, url):
    replace(vault, '10_markdown/documents/source.md', 'identifier: https://example.org/blob/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/source.xml', 'identifier: ' + json.dumps(url))
    with pytest.raises(ValueError, match='URL'):
        build_page(vault, '2026-09-05')


def test_publication_ends_at_checked_quote_not_invented_representation(vault):
    write(vault, 'references/sources.json', json.dumps([{'id': 'paper', 'title': 'A cited paper', 'URL': 'https://example.org/paper', 'issued': {'date-parts': [[2020]]}, 'note': 'Citation only; full text not redistributable.'}]))
    write(vault, '20_distillates/publications/paper.md', '''---
type: distillate
source-type: publication
reference: paper
status: validated
checked:
  quote: 2026-09-05
  validation: 2026-09-05
  machine-review: 2026-09-05
---
# Distillate: A cited paper
## Core statements
- A stated finding. ^s1
  > "A short exact quotation." (paper, p. 1)
''')
    page = build_page(vault, '2026-09-05')
    assert 'A short exact quotation.' in page
    assert 'Citation and checked quotation.' in page
    assert 'https://example.org/paper' in Page(page).links
    assert '10_markdown/publications/paper' not in page
    replace(vault, '20_distillates/publications/paper.md', '  quote: 2026-09-05\n', '')
    with pytest.raises(ValueError, match='intake check'):
        build_page(vault, '2026-09-05')


def test_repository_base_links_and_public_anchor_contract(vault):
    page = Page(build_page(vault, '2026-09-05', 'https://github.com/org/repo/blob/main'))
    assert 'https://github.com/org/repo/blob/main/30_assertions/claim.md' in page.links
    assert 'https://github.com/org/repo/blob/main/knowledge/state.md' in page.links
    assert doc_id('30_assertions/A claim.md') == 'doc-30-assertions-a-claim'
    assert block_id('20_distillates/documents/source.md', '^s1') == 'doc-20-distillates-documents-source--s1'
    with pytest.raises(ValueError, match='HTTPS'):
        build_page(vault, '2026-09-05', 'http://example.org/')


def test_no_js_accessibility_contract(vault):
    page = Page(build_page(vault, '2026-09-05'))
    artifacts = [(tag, attrs) for tag, attrs in page.tags if attrs.get('class') == 'artifact']
    assert len(artifacts) == 4
    assert all(tag == 'details' and 'hidden' not in attrs for tag, attrs in artifacts)
    assert len([tag for tag, _ in page.tags if tag == 'summary']) == 4
    assert ('a', {'class': 'skip-link', 'href': '#main'}) in page.tags


def test_block_parser_refuses_duplicate_anchors_and_ignores_code():
    with pytest.raises(ValueError, match='Duplicate'):
        anchored_blocks('One. ^r1\n\nTwo. ^r1', 'representation')
    assert anchored_blocks('```\nCode. ^r1\n```\n\nReal. ^r2', 'representation') == {'r2': 'Real. ^r2'}


def test_status_and_metadata_remain_actual(vault):
    replace(vault, '30_assertions/claim.md', 'status: grounded', 'status: verified\nchecked:\n  verification: 2026-09-05')
    view = build_view(vault, '2026-09-05')
    entry = next(e for e in view['entries'] if e['kind'] == 'assertion')
    assert entry['status'] == 'verified'
    page = build_page(vault, '2026-09-05')
    assert 'Not recorded in the matched admission' in page
    assert 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' in page
    assert 'CC-BY-4.0' in page
