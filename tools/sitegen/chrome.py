"""Shared navigation and footer for every public workbench page."""
from __future__ import annotations

import html

PAGES = (("home", "Proposal", "index.html"), ("model", "Model", "model.html"), ("materials", "Materials", "corpus.html"),
         ("knowledge", "Knowledge", "knowledge.html"), ("about", "About", "project.html"))


def render_header(active: str) -> str:
    if active not in {key for key, _, _ in PAGES}:
        raise ValueError("Unknown workbench page")
    links = "".join(f'<a href="{path}"' + (' aria-current="page"' if key == active else '')
                    + f'>{label}</a>' for key, label, path in PAGES)
    return '<header class="wb-header"><a class="wb-brand" href="index.html">TEI P6 <span>Research</span></a><nav class="wb-nav" aria-label="Main navigation">' + links + '</nav></header>'


def render_footer(date: str) -> str:
    return '<footer class="wb-footer"><span>Independent research. No official TEI Consortium affiliation.</span><span>Build ' + html.escape(date) + '</span></footer>'
