"""Render the self-contained materials page from presentation-ready records."""

from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path
from typing import Any

from tools.sitegen.assets import read_asset
from tools.sitegen.chrome import render_footer, render_header
from tools.sitegen.markup import deployment_base, doc_id
from tools.sitegen.materials_view import (
    GAP_LABELS,
    STATUS_HELP,
    STATUS_LABELS,
    STATUS_ORDER,
    prepare_sources,
)
from tools.sitegen.source_data import control_href

CSS = "\n" + read_asset("workbench.css") + "\n" + read_asset("materials.css")
SCRIPT = "\n" + read_asset("materials.js")


def display_number(value: int) -> str:
    return f"{value:,}"


def control_link(path: str, base: str | None, label: str) -> str:
    """Link one control record, resolved at build time so it works without JS."""
    return f'<a href="{html.escape(control_href(path, base), quote=True)}">{html.escape(label)}</a>'


def render_source(source: dict[str, Any], index: int, base: str | None) -> str:
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
            control_link(record["path"], base, "Data") if record["path"] else ""
        )
        proof_link = control_link(record["manifest_ref"], base, "Manifest")
        record_status = STATUS_LABELS.get(record["status"], record["status"] or "—")
        material_rows.append(
            '<li class="holding-item"><div class="holding-title"><strong>'
            + html.escape(record["label"])
            + '</strong><span class="holding-status">'
            + html.escape(record_status)
            + '</span><span class="row-links">'
            + data_link
            + proof_link
            + "</span></div><small>"
            + html.escape(record["description"])
            + '</small><small class="run-meta">Run <code>'
            + html.escape(record["run_id"])
            + "</code>"
            + "</small></li>"
        )
    materials_detail = (
        '<ul class="holding-list">'
        + "".join(material_rows)
        + "</ul>"
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
        control_link(reference, base, f"Acquisition manifest {number}")
        for number, reference in enumerate(source["manifest_refs"], start=1)
    )
    lock_link = control_link(source["lock_ref"], base, "Source Lock")
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
        <div class="link-list technical-links">{lock_link}{manifest_links}</div>
      </details>
    </div>
  </td>
</tr>"""


def guidelines_reference(root: Path, base: str | None) -> str:
    path = root / "corpus/projections/guidelines-4.12.0.json"
    if not path.exists():
        if (root / "sources/manifests/2026-09-07-guidelines-4.12.0-admission.yaml").exists():
            raise ValueError("Guidelines admission exists without its coverage projection")
        return ""
    view = json.loads(path.read_text(encoding="utf-8"))
    counts = view["counts"]
    rows = []
    for row in view["contents"]:
        source = '<a href="knowledge.html#' + html.escape(doc_id(row["representation"]), quote=True) + '">Read source</a>'
        processing = "Imported; no distillate"
        if row["distillate"]:
            processing = '<a href="knowledge.html#' + html.escape(doc_id(row["distillate"]), quote=True) + '">Distillate available</a>'
        rows.append('<tr><td>' + html.escape(row["part"].title() + " " + row["number"])
                    + '</td><td>' + html.escape(row["title"]) + '</td><td>' + source
                    + '</td><td>' + processing + '</td></tr>')
    full = control_link("corpus/projections/guidelines-4.12.0.md", base, "All source files and dependencies")
    return ('<section id="guidelines" aria-labelledby="guidelines-title"><h2 id="guidelines-title">English Guidelines 4.12.0</h2>'
            f'<p>{counts["ingested"]} source representations cover the 24 main chapters, front and back matter, '
            f'{counts["specifications"]} specifications and supporting XML. {counts["distilled"]} sources have a distillate. '
            'Import establishes availability for citation. Exhaustive section review and human verification remain open.</p>'
            '<details><summary>Coverage of the published contents</summary><div class="table-wrap"><table class="guidelines-coverage">'
            '<caption>Source admission and distillation are separate processing steps.</caption>'
            '<thead><tr><th scope="col">Part</th><th scope="col">Entry</th><th scope="col">Source</th>'
            '<th scope="col">Processing</th></tr></thead><tbody>' + ''.join(rows)
            + '</tbody></table></div></details><p>' + full + '</p></section>')


def build_page(root: Path, date: str, repository_base: str | None = None) -> str:
    base = deployment_base(repository_base)
    guidelines = guidelines_reference(root, base)
    registered_sources = prepare_sources(root)
    sources = [
        source
        for source in registered_sources
        if source["authority"] != "secondary-scholarly"
    ]
    literature = [source for source in registered_sources if source["authority"] == "secondary-scholarly"]
    literature_rows = "".join(
        "<li>" + control_link(source["lock_ref"], base, source["title"]) + " · "
        + html.escape(STATUS_LABELS.get(source["status"], source["status"])) + "</li>"
        for source in literature
    )
    literature_note = (
        '<aside class="literature-note" id="literature"><h2>Registered literature</h2>'
        '<p>Scholarly literature is registered separately from the primary-source families. '
        'Its acquisition state does not imply a complete bibliography.</p><ul>'
        + literature_rows + '</ul><p>Read the resulting claims and source chains in '
        '<a href="knowledge.html">Knowledge</a>.</p></aside>'
        if literature else ''
    )
    literature_link = ' · <a href="#literature">Registered literature</a>' if literature else ''
    statuses = Counter(source["status"] for source in sources)
    rows = "".join(
        render_source(source, index, base)
        for index, source in enumerate(sources, start=1)
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

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Materials · TEI P6 Research</title>
<meta name="description" content="Source families, recorded holdings, acquisition states and gaps in TEI P6 Research.">
<style>{CSS}</style>
</head>
<body>
<a class="skip-link" href="#main">Skip to materials</a>
{render_header("materials")}
  <main class="wb-main" id="main">
  <header class="page-head">
    <h1 id="page-title">Materials</h1>
    <p class="results-meta" role="status" aria-live="polite"><span id="result-count">{len(sources)}</span> sources</p>
  </header>
  <p class="wb-description materials-scope">Source families and recorded holdings. Individual raw files are not enumerated here.<br><a href="knowledge.html">Knowledge</a>{literature_link}</p>
  {guidelines}
  <section aria-label="Source families">
    <div class="toolbar">
      <label class="control control-search"><span>Full-text search</span><input id="search" class="search" type="search" placeholder="Search sources and holdings"></label>
      <label class="control"><span>Acquisition</span><select id="status-filter" class="select">{"".join(status_options)}</select></label>
      <label class="control"><span>Material type</span><select id="material-filter" class="select">{"".join(material_options)}</select></label>
    </div>
    <div class="table-wrap" tabindex="0" role="region" aria-label="Source holdings table">
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
  {literature_note}
  </main>
{render_footer(date)}
<script>{SCRIPT}</script>
</body>
</html>
"""
