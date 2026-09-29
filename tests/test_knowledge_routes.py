"""Keep the two harnesses on the same research and navigation contracts."""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]


def section(text, heading):
    return text.split('## ' + heading + '\n', 1)[1].split('\n## ', 1)[0].strip()


@pytest.mark.parametrize('heading', [
    'Project identity', 'Authority and trust', 'Start and route',
    'Hard research contracts', 'Generation', 'Completion',
])
def test_harnesses_route_through_the_same_contracts(heading):
    codex = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
    claude = (ROOT / 'CLAUDE.md').read_text(encoding='utf-8')
    assert section(codex, heading) == section(claude, heading)


def test_every_maintained_knowledge_document_is_in_the_hub():
    index = (ROOT / 'knowledge/INDEX.md').read_text(encoding='utf-8')
    linked = set(re.findall(r'\[\[(knowledge/[^]|#]+)', index))
    actual = {path.relative_to(ROOT).as_posix().removesuffix('.md')
              for path in (ROOT / 'knowledge').glob('*.md')}
    assert actual <= linked
    assert all((ROOT / (path + '.md')).is_file() for path in linked)
