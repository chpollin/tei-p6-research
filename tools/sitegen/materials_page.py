"""Render the self-contained materials page from presentation-ready records."""

from __future__ import annotations

import html
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any

from sitegen.assets import read_asset
from sitegen.materials_view import (
    GAP_LABELS,
    STATUS_HELP,
    STATUS_LABELS,
    STATUS_ORDER,
    prepare_sources,
)
from sitegen.source_data import local_href


CSS = "\n" + read_asset("materials.css")
SCRIPT = "\n" + read_asset("materials.js")


def display_number(value: int) -> str:
    return f"{value:,}"


def link_attributes(path: str) -> str:
    return (
        'href="'
        + html.escape(local_href(path), quote=True)
        + '" data-repo-path="'
        + html.escape(PurePosixPath(path.replace("\\", "/")).as_posix(), quote=True)
        + '"'
    )


def render_source(source: dict[str, Any], index: int) -> str:
    status = source["status"]
    status_label = STATUS_LABELS.get(status, status)
    status_help = STATUS_HELP.get(status, "Acquisition status of this holding.")
    material_names = list(
        dict.fromkeys(record["label"] for record in source["materials"])
    )
    gap_labels = [
        GAP_LABELS.get(
            str(gap.get("code", "")),
            str(gap.get("code", "Open item")).replace("-", " ").capitalize(),
        )
        for gap in source["gaps"]
    ]
    search = " ".join(
        [
            source["source_id"],
            source["title"],
            source["registered_title"],
            source["description"],
            source["family_label"],
            source["authority"],
            source["rights"],
            *material_names,
            *(record["description"] for record in source["materials"]),
            *gap_labels,
        ]
    ).casefold()
    metrics = " · ".join(
        f"{display_number(value)} {html.escape(name)}"
        for name, value in source["metrics"]
    ) or "—"

    material_summary = (
        '<ul class="material-summary">'
        + "".join(f"<li>{html.escape(name)}</li>" for name in material_names)
        + "</ul>"
        if material_names
        else '<span class="empty-value">Not yet acquired</span>'
    )
    material_rows = []
    for record in source["materials"]:
        data_link = (
            f'<a {link_attributes(record["path"])}>Data</a>'
            if record["path"]
            else ""
        )
        proof_link = f'<a {link_attributes(record["manifest_ref"])}>Manifest</a>'
        record_status = STATUS_LABELS.get(record["status"], record["status"] or "—")
        material_rows.append(
            "<tr><td><strong>"
            + html.escape(record["label"])
            + "</strong><small>"
            + html.escape(record["description"])
            + '</small><small class="run-meta">Run <code>'
            + html.escape(record["run_id"])
            + "</code>"
            + "</small></td><td>"
            + html.escape(record_status)
            + '</td><td><span class="row-links">'
            + data_link
            + proof_link
            + "</span></td></tr>"
        )
    materials_detail = (
        '<div class="subtable-wrap"><table class="subtable"><thead><tr><th>Holding</th><th>Acquisition</th><th>Open</th></tr></thead><tbody>'
        + "".join(material_rows)
        + "</tbody></table></div>"
        if material_rows
        else '<p class="empty-value">No completed acquisition run is available for this source.</p>'
    )

    if gap_labels:
        gap_block = '<ul class="gap-list">' + "".join(
            f"<li>{html.escape(label)}</li>" for label in gap_labels
        ) + "</ul>"
        gap_summary = (
            "1 open item" if len(gap_labels) == 1 else f"{len(gap_labels)} open items"
        )
    elif source["gap_count"]:
        gap_block = (
            f'<p>{display_number(source["gap_count"])} incompletely acquired objects are recorded in the acquisition manifest.</p>'
        )
        gap_summary = "Open objects"
    else:
        gap_block = '<p class="clear">No open items recorded.</p>'
        gap_summary = "No open items"

    upstream = "".join(
        '<a href="'
        + html.escape(url, quote=True)
        + '" rel="noreferrer">'
        + html.escape(name)
        + "</a>"
        for name, url in source["upstream"]
    )
    manifest_links = "".join(
        f'<a {link_attributes(reference)}>Acquisition manifest {number}</a>'
        for number, reference in enumerate(source["manifest_refs"], start=1)
    )
    lock_link_attributes = link_attributes(source["lock_ref"])
    detail_id = f"source-detail-{index}"
    status_rank = (
        STATUS_ORDER.index(status) if status in STATUS_ORDER else len(STATUS_ORDER)
    )
    material_filter = (
        "|".join(name.casefold() for name in material_names) or "__none__"
    )

    return f"""
<tr class="source-row" data-source-row data-detail-id="{detail_id}" data-status="{html.escape(status)}" data-status-rank="{status_rank}" data-materials="{html.escape(material_filter, quote=True)}" data-title="{html.escape(source["title"].casefold(), quote=True)}" data-date="{html.escape(source["as_of"], quote=True)}" data-search="{html.escape(search, quote=True)}">
  <td class="source-cell"><strong>{html.escape(source["title"])}</strong><small>{html.escape(source["description"])}</small></td>
  <td class="materials-cell">{material_summary}</td>
  <td class="metrics-cell">{metrics}</td>
  <td class="status-cell"><span class="status-text status-{html.escape(status)}" title="{html.escape(status_help, quote=True)}">{html.escape(status_label)}</span><small>{gap_summary}</small></td>
  <td class="date-cell"><time datetime="{html.escape(source["as_of"], quote=True)}">{html.escape(source["as_of"] or "—")}</time></td>
  <td class="action-cell"><button class="expand" type="button" aria-expanded="false" aria-controls="{detail_id}" aria-label="Show details for {html.escape(source["title"], quote=True)}"><span aria-hidden="true">+</span></button></td>
</tr>
<tr class="detail-row" id="{detail_id}" data-detail-row hidden>
  <td colspan="6">
    <div class="detail-panel">
      <section class="holdings-section">
        <h2>Holdings</h2>
        {materials_detail}
      </section>
      <section>
        <h2>Open items</h2>
        {gap_block}
      </section>
      <section>
        <h2>Sources</h2>
        <div class="link-list">{upstream or "<span>No URL registered</span>"}</div>
      </section>
      <details class="technical-details">
        <summary>Technical details</summary>
        <dl class="facts">
          <div><dt>Identifier</dt><dd><code>{html.escape(source["source_id"])}</code></dd></div>
          <div><dt>Material family</dt><dd>{html.escape(source["family_label"])}</dd></div>
          <div><dt>Rights</dt><dd>{html.escape(source["rights"])}</dd></div>
          <div><dt>Source types</dt><dd>{html.escape(source["source_types"])}</dd></div>
        </dl>
        <div class="link-list technical-links"><a {lock_link_attributes}>Source Lock</a>{manifest_links}</div>
      </details>
    </div>
  </td>
</tr>"""


def build_page(root: Path, date: str, repository_base: str | None = None) -> str:
    registered_sources = prepare_sources(root)
    sources = [
        source
        for source in registered_sources
        if source["authority"] != "secondary-scholarly"
    ]
    statuses = Counter(source["status"] for source in sources)
    rows = "".join(
        render_source(source, index) for index, source in enumerate(sources, start=1)
    )

    status_options = ['<option value="all">All acquisition states</option>']
    for status in STATUS_ORDER:
        if statuses[status]:
            status_options.append(
                '<option value="'
                + html.escape(status)
                + '">'
                + html.escape(STATUS_LABELS.get(status, status))
                + "</option>"
            )
    material_names = sorted(
        {
            record["label"]
            for source in sources
            for record in source["materials"]
        },
        key=str.casefold,
    )
    material_options = ['<option value="all">All material types</option>']
    material_options.extend(
        '<option value="'
        + html.escape(name.casefold(), quote=True)
        + '">'
        + html.escape(name)
        + "</option>"
        for name in material_names
    )
    if any(not source["materials"] for source in sources):
        material_options.append('<option value="__none__">Not yet acquired</option>')

    repository_base = repository_base.rstrip("/") + "/" if repository_base else ""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="repository-base" content="{html.escape(repository_base, quote=True)}">
<title>Materials · TEI P6 Research</title>
<meta name="description" content="Working inventory of acquired primary materials and known gaps in TEI P6 Research.">
<style>{CSS}</style>
</head>
<body>
<div class="shell">
  <header class="site-header">
    <a class="brand" href="corpus.html"><span class="brand-name">TEI P6</span><span class="brand-context">Research</span></a>
    <nav class="primary-nav" aria-label="Primary navigation">
      <a class="nav-link" href="corpus.html" aria-current="page">Materials</a>
      <a class="nav-link" href="index.html" data-project-link>About</a>
    </nav>
  </header>
  <main>
  <header class="page-head">
    <h1 id="page-title">Materials</h1>
    <p class="results-meta" role="status" aria-live="polite"><span id="result-count">{len(sources)}</span> sources</p>
  </header>
  <section aria-label="Source families">
    <div class="toolbar">
      <label class="control control-search"><span>Full-text search</span><input id="search" class="search" type="search" placeholder="Search sources and holdings"></label>
      <label class="control"><span>Acquisition</span><select id="status-filter" class="select">{"".join(status_options)}</select></label>
      <label class="control"><span>Material type</span><select id="material-filter" class="select">{"".join(material_options)}</select></label>
    </div>
    <div class="table-wrap">
      <table class="source-table">
        <caption class="sr-only">Registered primary sources and their acquired holdings</caption>
        <colgroup><col><col><col><col><col><col></colgroup>
        <thead>
          <tr>
            <th data-sort-header="title" aria-sort="ascending"><button class="sort-button" type="button" data-sort="title">Source <span class="sort-mark" aria-hidden="true">↑</span></button></th>
            <th data-sort-header="materials" aria-sort="none"><button class="sort-button" type="button" data-sort="materials">Holdings <span class="sort-mark" aria-hidden="true"></span></button></th>
            <th>Extent</th>
            <th data-sort-header="status" aria-sort="none"><button class="sort-button" type="button" data-sort="status">Acquisition <span class="sort-mark" aria-hidden="true"></span></button></th>
            <th data-sort-header="date" aria-sort="none"><button class="sort-button" type="button" data-sort="date">As of <span class="sort-mark" aria-hidden="true"></span></button></th>
            <th><span class="sr-only">Details</span></th>
          </tr>
        </thead>
        <tbody id="source-body">{rows}</tbody>
      </table>
    </div>
    <p id="empty" class="empty">No source matches the current selection.</p>
  </section>
  </main>
  <footer class="site-footer">
    <p>Independent research project · not officially affiliated with the TEI Consortium</p>
    <nav class="footer-nav" aria-label="Further information">
      <a href="index.html" data-project-link>About</a>
    </nav>
  </footer>
</div>
<script>{SCRIPT}</script>
</body>
</html>
"""
