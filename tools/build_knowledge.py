"""Build the static inventory of actual knowledge and its provenance chain."""
from __future__ import annotations

import argparse
from datetime import date as calendar_date
from pathlib import Path

from sitegen.knowledge_page import render_page
from sitegen.knowledge_view import build_view


def build_page(root: Path, date: str, repository_base: str | None = None) -> str:
    calendar_date.fromisoformat(date)
    return render_page(build_view(Path(root), date, repository_base))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--date', required=True)
    parser.add_argument('--repository-base')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    page = build_page(args.root, args.date, args.repository_base)
    output = args.output or args.root / 'docs/knowledge.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding='utf-8', newline='\n')
    print(f'Built {output}')


if __name__ == '__main__':
    main()
