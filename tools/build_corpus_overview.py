"""Generate a compact static overview of the registered primary-data corpus."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # direct script run

from tools.sitegen.materials_page import build_page
from tools.sitegen.materials_view import prepare_sources

__all__ = ["build_page", "prepare_sources"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="generation date, ISO 8601")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="vault root",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="target file (default: <root>/docs/corpus.html)",
    )
    parser.add_argument(
        "--repository-base",
        default=None,
        help="optional Git repository blob URL used for links in hosted output",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output or root / "docs" / "corpus.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    page = build_page(root, args.date, repository_base=args.repository_base)
    output.write_text(page, encoding="utf-8", newline="\n")
    print(f"OK: {output} ({len(page)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
