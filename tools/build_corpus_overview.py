"""Generate a compact static overview of the registered primary-data corpus."""

from __future__ import annotations

import argparse
import html
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

STATUS_LABELS = {
    "observable-complete": "Acquired",
    "bounded-complete": "Acquired",
    "partial": "Partially acquired",
    "planned": "Planned",
    "not_started": "Not started",
    "not-completable": "Not completable",
}

STATUS_HELP = {
    "observable-complete": "All objects exposed by the locked public interface were acquired or recorded as a gap.",
    "bounded-complete": "All results of the locked search or sampling protocol received a disposition.",
    "partial": "Part of the locked holding was acquired; open gaps are recorded.",
    "planned": "The source family is registered but has not yet been acquired.",
    "not_started": "The source family is registered but has not yet been acquired.",
    "not-completable": "The source family cannot be completed within its declared boundary.",
}

STATUS_ORDER = (
    "observable-complete",
    "bounded-complete",
    "partial",
    "planned",
    "not_started",
    "not-completable",
)

FAMILY_LABELS = {
    "normative-guidelines": "Normative P5 baseline",
    "development-records": "Development discussions",
    "development-infrastructure": "Development infrastructure",
    "development-and-implementation-records": "Source code and development",
    "governance-records": "Governance",
    "governance-working-documents": "Governance working documents",
    "official-p6-development": "Official P6 process",
    "releases": "Release history",
    "historical-records": "Historical TEI holdings",
    "historical-development-records": "Historical development",
    "reference-implementation": "Reference implementation and tools",
    "publication-infrastructure": "Publication infrastructure",
    "community-process-records": "Community and working groups",
    "observed-practice": "Documented practice",
    "literature": "Research literature",
}

SOURCE_TITLES = {
    "teic-tei-p5-4.12.0": "TEI P5 4.12.0 — Sources and published Guidelines",
    "github-teic-tei-work-items": "TEIC/TEI — Issues and pull requests",
    "teic-github-organization": "TEIC on GitHub — Repository census",
    "teic-public-git-repositories": "Public TEIC Git repositories",
    "tei-council-minutes": "TEI Technical Council — Meeting minutes",
    "tei-council-working-documents": "TEI Technical Council — Working documents",
    "tei-official-p6-process": "Official TEI P6 process",
    "tei-p5-release-history": "TEI P5 release history",
    "tei-board-records": "TEI Board — Meetings and policies",
    "tei-historical-archive": "Historical TEI archive",
    "tei-legacy-sourceforge": "Historical TEI trackers on SourceForge",
    "teic-stylesheets": "TEI XSL Stylesheets",
    "teic-tooling": "Official TEI tools",
    "tei-website-records": "Official TEI website",
    "tei-community-records": "TEI community, SIGs, and working groups",
    "tei-real-world-customizations": "Real-world ODD customizations and processing practice",
}

SOURCE_DESCRIPTIONS = {
    "teic-tei-p5-4.12.0": "Normative ODD sources, published Guidelines, and the release package for the P5 baseline.",
    "github-teic-tei-work-items": "Issues, pull requests, comments, reviews, and event histories from the TEIC/TEI repository.",
    "teic-github-organization": "A census of the TEI Consortium organization's publicly visible repositories.",
    "teic-public-git-repositories": "Pinned Git states of publicly registered TEIC repositories.",
    "tei-council-minutes": "Meeting minutes and linked working materials of the Technical Council.",
    "tei-council-working-documents": "Technical documents from the Council's public working repository.",
    "tei-official-p6-process": "Public materials and presentations from the official TEI P6 process.",
    "tei-p5-release-history": "Published P5 versions, release pages, and associated artifacts.",
    "tei-board-records": "Meeting and policy records of the TEI Board.",
    "tei-historical-archive": "Historical Guidelines, committee records, and other holdings from the TEI archive.",
    "tei-legacy-sourceforge": "Historical bug reports, feature requests, support tickets, and discussions.",
    "teic-stylesheets": "Source code and development history of the TEI XSL Stylesheets.",
    "teic-tooling": "Public tools for customization, validation, and conversion.",
    "tei-website-records": "Source code and published pages of the official TEI website.",
    "tei-community-records": "Records from TEI-L, SIGs, working groups, and annual meetings.",
    "tei-real-world-customizations": "Observed ODD customizations and processing practice from real projects.",
}

OBJECT_KIND_LABELS = {
    "git-tree-inventory": "Git tree inventory",
    "web-census": "Web page census",
    "release-asset-inventory": "Release archive",
    "zip-member-inventory": "ZIP member inventory",
    "github-organization-repository-census": "Repository census",
    "sourceforge-ticket-metadata": "Ticket and discussion records",
}

OBJECT_KIND_DESCRIPTIONS = {
    "git-tree-inventory": "File and directory structure of a pinned Git state.",
    "web-census": "Acquired web pages and responses within the locked crawl boundary.",
    "release-asset-inventory": "Downloaded release archive with checksum verification.",
    "zip-member-inventory": "Inventory of files contained in a release archive.",
    "github-organization-repository-census": "Publicly visible repositories at the observation time.",
    "sourceforge-ticket-metadata": "Ticket metadata and discussion posts from the historical trackers.",
}

ADAPTER_LABELS = {
    "tools.corpus.git_snapshot": "Git tree inventory",
    "tools.corpus.github_org_git_snapshot": "Public Git repositories",
    "tools.corpus.github_org_census": "Repository census",
    "tools.corpus.web_census": "Web page census",
    "tools.corpus.asset_snapshot": "File and release inventory",
    "tools.corpus.zip_inventory": "Archive member inventory",
    "tools.corpus.sourceforge_snapshot": "Ticket and discussion records",
}

ADAPTER_DESCRIPTIONS = {
    "tools.corpus.git_snapshot": "File and directory structure of a pinned Git state.",
    "tools.corpus.github_org_git_snapshot": "Pinned Git states of the registered public repositories.",
    "tools.corpus.github_org_census": "Publicly visible repositories at the observation time.",
    "tools.corpus.web_census": "Acquired web pages and responses within the locked crawl boundary.",
    "tools.corpus.asset_snapshot": "Inventory of acquired files and release artifacts.",
    "tools.corpus.zip_inventory": "Inventory of files contained in an archive.",
    "tools.corpus.sourceforge_snapshot": "Ticket metadata and discussion posts from the historical trackers.",
}

GAP_LABELS = {
    "published-html-release-asset-reconciliation-not-explicit": "Reconciliation between the published Guidelines and the release archive is pending",
    "authenticated-github-api-session-unavailable": "GitHub acquisition is waiting for authenticated read access",
    "linked-attachments-and-external-working-documents-not-yet-reconciled": "Linked attachments and external working documents have not yet been reconciled",
    "reported-p6-sandbox-not-publicly-observable": "The reported P6 sandbox is not publicly accessible",
    "p6-specific-council-records-not-yet-projected": "P6-specific Council records have not yet been projected separately",
    "per-release-child-locks-not-yet-generated": "Individual P5 releases have not yet been pinned separately",
    "one-legacy-backup-file-inventoried-not-fetched": "One historical backup file has not yet been fetched",
    "linked-objects-return-http-errors": "Some linked Board records could not be retrieved",
    "linked-non-html-artifacts-not-yet-reconciled": "Linked archive files have not yet been fully reconciled",
    "depth-boundary-links-require-deeper-census": "Part of the historical archive requires a deeper crawl",
    "archive-self-reports-historical-incompleteness": "The historical archive reports gaps in its own preservation",
    "sourceforge-rate-limit": "SourceForge acquisition was interrupted by access limits",
    "support-files-and-version-control-interfaces-not-yet-reconciled": "SourceForge files and version-control interfaces have not yet been reconciled",
    "first-partial-run-requires-refetch-for-per-ticket-raw-hash-links": "An earlier partial run requires a controlled refetch",
    "github-work-items-not-yet-acquired": "Issues and pull requests have not yet been acquired",
    "public-page-snapshot-boundary-not-yet-acquired": "Published web pages have not yet been acquired as a separate holding",
    "tei-l-archive-tls-certificate-not-verified": "Access to the TEI-L archive is not technically verified",
    "annual-meeting-and-workgroup-targets-under-reconciliation": "Annual meetings and working groups are still being reconciled",
    "sampling-protocol-not-yet-approved": "The sampling protocol for real-world projects has not yet been defined",
    "legacy-lite-customization-url-returns-404": "A historical Lite Customization is no longer reachable",
}

COUNT_LABELS = {
    "public_repositories": "repositories",
    "repositories_expected": "repositories expected",
    "repositories_mirrored": "repositories",
    "registered_repositories_materialized": "repositories",
    "registered_repository_tree_entries": "tree entries",
    "registered_repository_commits_all_refs_sum": "commits across all refs",
    "git_tree_entries": "tree entries",
    "tree_entries": "tree entries",
    "commits_all_observed_refs": "commits across all observed refs",
    "release_zip_files": "ZIP files",
    "files": "files",
    "official_pages_retrieved": "Council pages",
    "official_index_pages_retrieved": "index pages",
    "responses": "responses",
    "successful_responses": "successful responses",
    "release_index_responses": "release-index responses",
    "sig_index_pages_retrieved": "SIG pages",
    "sig_external_links_inventoried": "inventoried external SIG links",
    "tickets_retrieved": "tickets",
    "discussion_posts_retrieved": "discussion posts",
    "bugs_enumerated": "inventoried bug tickets",
    "issues": "issues",
    "pull_requests": "pull requests",
    "official_version_directories_observed": "observed version directories",
    "external_artifact_links_inventoried": "inventoried artifact links",
    "external_links_inventoried": "inventoried external links",
    "binary_links_not_fetched": "unfetched binary links",
    "non_html_artifacts_inventoried": "inventoried non-HTML artifacts",
    "time_for_p6_tree_entries": "P6 tree entries",
    "time_for_p6_commits_all_observed_refs": "P6 commits across all refs",
    "council_pages_in_shared_census": "Council pages",
    "gaps": "gaps",
}

COUNT_PRIORITY = tuple(COUNT_LABELS)


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def manifest_references(lock: dict[str, Any]) -> list[str]:
    references: list[str] = []
    single = lock.get("manifest")
    if isinstance(single, str):
        references.append(single)
    many = lock.get("manifests")
    if isinstance(many, list):
        references.extend(item for item in many if isinstance(item, str))
    records = lock.get("records")
    if isinstance(records, list):
        for record in records:
            if isinstance(record, dict) and isinstance(record.get("manifest"), str):
                references.append(record["manifest"])
    return list(dict.fromkeys(references))


def flatten_counts(value: Any, prefix: str = "") -> dict[str, int]:
    flattened: dict[str, int] = {}
    if not isinstance(value, dict):
        return flattened
    for key, child in value.items():
        name = f"{prefix}_{key}" if prefix else str(key)
        if isinstance(child, bool):
            continue
        if isinstance(child, int):
            flattened[name] = child
        elif isinstance(child, dict):
            flattened.update(flatten_counts(child, name))
    return flattened


def source_counts(lock: dict[str, Any], manifests: list[dict[str, Any]]) -> dict[str, int]:
    counts = flatten_counts(lock.get("counts", {}))
    if counts:
        return counts
    if len(manifests) == 1:
        return flatten_counts(manifests[0].get("counts", {}))
    return {}


def selected_metrics(counts: dict[str, int]) -> list[tuple[str, int]]:
    metrics: list[tuple[str, int]] = []
    used_labels: set[str] = set()
    used_keys: set[str] = set()
    for key in COUNT_PRIORITY:
        if key not in counts:
            continue
        label = COUNT_LABELS[key]
        if label.casefold() in used_labels:
            continue
        metrics.append((label, counts[key]))
        used_labels.add(label.casefold())
        used_keys.add(key)
        if len(metrics) == 3:
            return metrics
    for key, value in counts.items():
        if key in used_keys:
            continue
        leaf = key.rsplit("_", 1)[-1]
        if leaf in {"gaps", "bytes"}:
            continue
        label = key.replace("_", " ").capitalize()
        if label.casefold() in used_labels:
            continue
        metrics.append((label, value))
        used_labels.add(label.casefold())
        if len(metrics) == 3:
            break
    return metrics


def gap_records(lock: dict[str, Any], manifests: list[dict[str, Any]]) -> list[dict[str, Any]]:
    gaps = lock.get("gaps")
    if isinstance(gaps, list):
        return [gap for gap in gaps if isinstance(gap, dict)]
    if len(manifests) == 1 and isinstance(manifests[0].get("gaps"), list):
        return [gap for gap in manifests[0]["gaps"] if isinstance(gap, dict)]
    return []


def upstream_links(value: Any) -> list[tuple[str, str]]:
    links: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(child, str) and child.startswith(("https://", "http://")):
                label = key.replace("_", " ").capitalize()
                links.append((label, child))
            else:
                links.extend(upstream_links(child))
    elif isinstance(value, list):
        for child in value:
            if isinstance(child, str) and child.startswith(("https://", "http://")):
                links.append(("Source", child))
            else:
                links.extend(upstream_links(child))
    return links


def normalized_artifacts(manifests: list[dict[str, Any]]) -> list[str]:
    paths: list[str] = []
    for manifest in manifests:
        objects = manifest.get("objects")
        if not isinstance(objects, list):
            continue
        for item in objects:
            if not isinstance(item, dict):
                continue
            path = item.get("path")
            if isinstance(path, str) and path.startswith(
                ("corpus/normalized/", "corpus/projections/")
            ):
                paths.append(path)
    return list(dict.fromkeys(paths))


def first_scope_rule(value: Any) -> str:
    if isinstance(value, dict):
        rule = value.get("rule")
        if isinstance(rule, str):
            return rule
        for child in value.values():
            found = first_scope_rule(child)
            if found:
                return found
    elif isinstance(value, list):
        for child in value:
            found = first_scope_rule(child)
            if found:
                return found
    return ""


def display_number(value: int) -> str:
    return f"{value:,}"


def local_href(path: str) -> str:
    normalized = PurePosixPath(path.replace("\\", "/"))
    allowed = (
        ("sources", "locks"),
        ("sources", "manifests"),
        ("corpus", "normalized"),
        ("corpus", "projections"),
    )
    if normalized.is_absolute() or ".." in normalized.parts:
        raise ValueError(f"unsafe local overview link: {path}")
    if not any(normalized.parts[: len(prefix)] == prefix for prefix in allowed):
        raise ValueError(f"unexpected local overview link: {path}")
    return "../" + normalized.as_posix()


def link_attributes(path: str) -> str:
    return (
        'href="'
        + html.escape(local_href(path), quote=True)
        + '" data-repo-path="'
        + html.escape(PurePosixPath(path.replace("\\", "/")).as_posix(), quote=True)
        + '"'
    )


def material_records(
    manifests: list[dict[str, Any]], manifest_refs: list[str]
) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for manifest, manifest_ref in zip(manifests, manifest_refs, strict=True):
        manifest_records: list[dict[str, str]] = []
        objects = manifest.get("objects")
        if isinstance(objects, list):
            for item in objects:
                if not isinstance(item, dict):
                    continue
                kind = str(item.get("kind", ""))
                label = OBJECT_KIND_LABELS.get(
                    kind, kind.replace("-", " ").capitalize() or "Data holding"
                )
                manifest_records.append(
                    {
                        "label": label,
                        "description": OBJECT_KIND_DESCRIPTIONS.get(
                            kind, "Normalized holding from this acquisition run."
                        ),
                        "path": str(item.get("path") or ""),
                        "status": str(manifest.get("status") or ""),
                        "manifest_ref": manifest_ref,
                        "kind": kind,
                    }
                )
        if not manifest_records:
            adapter = manifest.get("adapter")
            adapter_name = adapter.get("name") if isinstance(adapter, dict) else None
            label = ADAPTER_LABELS.get(str(adapter_name))
            if label:
                manifest_records.append(
                    {
                        "label": label,
                        "description": ADAPTER_DESCRIPTIONS.get(
                            str(adapter_name), "Acquired holding from this acquisition run."
                        ),
                        "path": "",
                        "status": str(manifest.get("status") or ""),
                        "manifest_ref": manifest_ref,
                        "kind": str(adapter_name or ""),
                    }
                )
        records.extend(manifest_records)
    return records


def resolve_repo_file(root: Path, reference: str) -> Path:
    local_href(reference)
    normalized = PurePosixPath(reference.replace("\\", "/"))
    candidate = (root / Path(*normalized.parts)).resolve()
    if not candidate.is_relative_to(root.resolve()) or not candidate.is_file():
        raise FileNotFoundError(f"missing or unsafe overview input: {reference}")
    return candidate


def prepare_sources(root: Path) -> list[dict[str, Any]]:
    registry = load_yaml(root / "sources" / "registry.yaml")
    sources = registry.get("sources")
    if not isinstance(sources, list):
        raise ValueError("sources/registry.yaml has no sources list")

    prepared: list[dict[str, Any]] = []
    seen_source_ids: set[str] = set()
    for source in sources:
        if not isinstance(source, dict):
            continue
        source_id = str(source.get("source_id", ""))
        if not source_id or source_id in seen_source_ids:
            raise ValueError(f"missing or duplicate source_id: {source_id!r}")
        seen_source_ids.add(source_id)
        lock_ref = source.get("lock")
        if not isinstance(lock_ref, str):
            raise ValueError(f"source {source.get('source_id')} has no lock")
        lock = load_yaml(resolve_repo_file(root, lock_ref))
        if lock.get("source_id") != source_id:
            raise ValueError(f"source_id mismatch between registry and {lock_ref}")
        registry_status = source.get("retrieval_status")
        lock_status = lock.get("retrieval_status")
        if registry_status != lock_status:
            raise ValueError(f"retrieval_status mismatch for {source_id}")
        manifest_refs = manifest_references(lock)
        missing_manifests = [
            reference
            for reference in manifest_refs
            if not (root / reference).resolve().is_file()
        ]
        if missing_manifests:
            raise FileNotFoundError(
                f"missing manifest(s) for {source_id}: {', '.join(missing_manifests)}"
            )
        manifests = [
            load_yaml(resolve_repo_file(root, reference)) for reference in manifest_refs
        ]
        counts = source_counts(lock, manifests)
        gaps = gap_records(lock, manifests)
        status = str(lock_status)
        rights = source.get("rights") if isinstance(source.get("rights"), dict) else {}
        source_types = source.get("vault_source_types")
        artifacts = normalized_artifacts(manifests)
        materials = material_records(manifests, manifest_refs)
        for artifact in artifacts:
            resolve_repo_file(root, artifact)
        prepared.append(
            {
                "source_id": source_id,
                "title": SOURCE_TITLES.get(source_id, str(source.get("title", ""))),
                "registered_title": str(source.get("title", "")),
                "description": SOURCE_DESCRIPTIONS.get(
                    source_id, "Registered primary-source holding of the research project."
                ),
                "family": str(source.get("family", "")),
                "family_label": FAMILY_LABELS.get(
                    str(source.get("family", "")),
                    str(source.get("family", "")),
                ),
                "authority": str(source.get("authority", "")),
                "status": status,
                "completion_target": str(source.get("completion_target", "")),
                "as_of": str(lock.get("as_of", "")),
                "rights": str(rights.get("rights_status", "not specified")),
                "redistribution": str(
                    rights.get("redistribution") or "not specified"
                ),
                "license": str(rights.get("license_expression") or "not specified"),
                "source_types": (
                    ", ".join(str(item) for item in source_types)
                    if isinstance(source_types, list)
                    else "not specified"
                ),
                "update_policy": str(source.get("update_policy", "not specified")),
                "scope_rule": first_scope_rule(lock.get("scope", {})),
                "metrics": selected_metrics(counts),
                "materials": materials,
                "gaps": gaps,
                "gap_count": counts.get("gaps", len(gaps)),
                "lock_ref": lock_ref,
                "manifest_refs": manifest_refs,
                "manifests": manifests,
                "artifacts": artifacts,
                "upstream": upstream_links(source.get("upstream", {})),
            }
        )
    return prepared


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
        gap_summary = "1 open item" if len(gap_labels) == 1 else f"{len(gap_labels)} open items"
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
    status_rank = STATUS_ORDER.index(status) if status in STATUS_ORDER else len(STATUS_ORDER)
    material_filter = "|".join(name.casefold() for name in material_names) or "__none__"

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


CSS = """
:root {
  color-scheme: light;
  --paper: #ffffff;
  --soft: #f7f8f9;
  --ink: #191919;
  --muted: #686b70;
  --line: #dfe1e4;
  --link: #174ea6;
  --complete: #26734d;
  --partial: #8a5a00;
  --pending: #9b3a32;
}
* { box-sizing: border-box; }
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0;
}
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 16px/1.5 "Segoe UI", Inter, system-ui, sans-serif;
}
a { color: var(--link); }
button, input, select { font: inherit; }
button, select { cursor: pointer; }
.shell { width: min(1580px, calc(100% - 2.5rem)); margin: 0 auto; padding: 1.15rem 0 3rem; }
.site-header {
  display: flex; align-items: stretch; justify-content: space-between; gap: 1.5rem;
  min-height: 3.4rem; border-bottom: 1px solid var(--line);
}
.brand { display: flex; align-items: center; gap: .55rem; color: var(--ink); text-decoration: none; }
.brand-name { font-weight: 700; letter-spacing: -.015em; }
.brand-context { color: var(--muted); font-size: .82rem; }
.primary-nav { display: flex; align-items: stretch; gap: 1.35rem; }
.nav-link { display: flex; align-items: center; border-bottom: 2px solid transparent; color: var(--muted); text-decoration: none; font-size: .87rem; }
.nav-link:hover { color: var(--ink); }
.nav-link[aria-current="page"] { border-bottom-color: var(--ink); color: var(--ink); }
.page-head { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; padding: 1.2rem 0 .85rem; }
h1 { margin: 0; font-size: 1.55rem; line-height: 1.2; letter-spacing: -.015em; font-weight: 650; }
.results-meta { margin: 0; color: var(--muted); font-size: .84rem; white-space: nowrap; }
.toolbar {
  position: sticky; top: 0; z-index: 5;
  display: grid; grid-template-columns: minmax(18rem, 1fr) minmax(11rem, auto) minmax(13rem, auto);
  gap: .65rem; padding: .7rem 0; background: var(--paper); border-top: 1px solid var(--line);
}
.control { display: grid; gap: .22rem; min-width: 0; }
.control span { color: var(--muted); font-size: .76rem; }
.search, .select {
  width: 100%; min-height: 2.45rem; padding: .46rem .65rem;
  border: 1px solid #b9bcc1; border-radius: 2px; background: var(--paper); color: var(--ink);
}
.search:focus, .select:focus, .expand:focus, .sort-button:focus { outline: 2px solid var(--link); outline-offset: 1px; }
.table-wrap { overflow-x: auto; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
.source-table { width: 100%; min-width: 1120px; border-collapse: collapse; table-layout: fixed; }
.source-table col:nth-child(1) { width: 31%; }
.source-table col:nth-child(2) { width: 24%; }
.source-table col:nth-child(3) { width: 18%; }
.source-table col:nth-child(4) { width: 15%; }
.source-table col:nth-child(5) { width: 9%; }
.source-table col:nth-child(6) { width: 3%; }
th { padding: .55rem .7rem; border-bottom: 1px solid var(--line); color: var(--muted); text-align: left; font-size: .76rem; font-weight: 600; }
.sort-button { display: inline-flex; align-items: center; gap: .35rem; padding: 0; border: 0; background: transparent; color: inherit; font: inherit; }
.sort-button:hover { color: var(--ink); }
.sort-mark { width: .8rem; color: var(--muted); }
td { padding: .85rem .7rem; border-top: 1px solid var(--line); vertical-align: top; }
.source-row:first-child td { border-top: 0; }
.source-row:hover td { background: #fbfbfb; }
.source-row[hidden], .detail-row[hidden] { display: none; }
.source-cell strong { display: block; line-height: 1.3; font-size: .95rem; font-weight: 620; }
.source-cell small { display: block; margin-top: .3rem; max-width: 54ch; color: var(--muted); font-size: .78rem; line-height: 1.4; }
.material-summary { margin: 0; padding-left: 1rem; font-size: .84rem; }
.material-summary li + li { margin-top: .16rem; }
.metrics-cell, .date-cell { color: var(--muted); font-size: .82rem; }
.status-cell > small { display: block; margin-top: .28rem; color: var(--muted); font-size: .76rem; }
.status-text { font-size: .84rem; font-weight: 600; text-decoration: underline dotted; text-underline-offset: .2rem; }
.status-observable-complete, .status-bounded-complete { color: var(--complete); }
.status-partial { color: var(--partial); }
.status-planned, .status-not_started, .status-not-completable { color: var(--pending); }
.action-cell { padding-left: .2rem; padding-right: .2rem; text-align: center; }
.expand { width: 2rem; height: 2rem; padding: 0; border: 0; background: transparent; color: var(--muted); font-size: 1.1rem; line-height: 1; }
.expand:hover { color: var(--ink); background: var(--soft); }
.expand[aria-expanded="true"] span { display: inline-block; transform: rotate(45deg); }
.detail-row > td { padding: 0; background: var(--soft); }
.detail-panel { display: grid; grid-template-columns: minmax(30rem, 2fr) minmax(15rem, 1fr) minmax(12rem, .8fr); gap: 1.6rem; padding: 1.25rem 1.5rem 1.5rem; }
.detail-panel h2 { margin: 0 0 .55rem; color: var(--muted); font-size: .76rem; font-weight: 650; letter-spacing: .045em; text-transform: uppercase; }
.detail-panel p, .gap-list { margin: 0; font-size: .84rem; }
.holdings-section { min-width: 0; }
.subtable-wrap { overflow-x: auto; }
.subtable { width: 100%; min-width: 34rem; border-collapse: collapse; table-layout: auto; background: var(--paper); }
.subtable th { padding: .4rem .55rem; background: #f0f1f2; }
.subtable td { padding: .55rem; font-size: .8rem; }
.subtable td:first-child { width: 58%; }
.subtable strong { display: block; font-weight: 600; }
.subtable small { display: block; margin-top: .16rem; color: var(--muted); line-height: 1.35; }
.row-links { display: flex; flex-wrap: wrap; gap: .45rem; }
.facts { margin: 0; }
.facts div + div { margin-top: .5rem; }
dt { color: var(--muted); font-size: .7rem; letter-spacing: .04em; text-transform: uppercase; }
dd { margin: .05rem 0 0; font-size: .82rem; overflow-wrap: anywhere; }
.gap-list { padding-left: 1.1rem; }
.gap-list li + li { margin-top: .3rem; }
.clear { color: var(--complete); }
.link-list { display: flex; flex-wrap: wrap; gap: .35rem .8rem; font-size: .84rem; }
.link-list a, .link-list span, .detail-panel p, dd { overflow-wrap: anywhere; }
.technical-details { grid-column: 1 / -1; border-top: 1px solid var(--line); padding-top: .8rem; }
.technical-details summary { color: var(--muted); cursor: pointer; font-size: .8rem; }
.technical-details[open] summary { margin-bottom: .8rem; }
.technical-details .facts { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; }
.technical-links { margin-top: .8rem; }
.empty-value { color: var(--muted); font-size: .82rem; }
.empty { display: none; margin: 0; padding: 2rem .7rem; border-bottom: 1px solid var(--line); color: var(--muted); }
.site-footer { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin-top: 1rem; padding-top: .85rem; border-top: 1px solid var(--line); color: var(--muted); font-size: .76rem; }
.site-footer p { margin: 0; }
.footer-nav { display: flex; flex-wrap: wrap; gap: .9rem; }
.site-footer a { color: inherit; text-decoration: none; }
.site-footer a:hover { color: var(--ink); text-decoration: underline; }
@media (max-width: 860px) {
  .shell { width: min(100% - 1.25rem, 1580px); padding-top: .75rem; }
  .toolbar { grid-template-columns: 1fr 1fr; }
  .control-search { grid-column: 1 / -1; }
  .detail-panel { grid-template-columns: 1fr; }
  .technical-details { grid-column: 1; }
  .technical-details .facts { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .brand-context { display: none; }
  .site-footer { align-items: flex-start; flex-direction: column; }
}
"""


SCRIPT = """
const search = document.querySelector("#search");
const statusFilter = document.querySelector("#status-filter");
const materialFilter = document.querySelector("#material-filter");
const rows = [...document.querySelectorAll("[data-source-row]")];
const tableBody = document.querySelector("#source-body");
const resultCount = document.querySelector("#result-count");
const empty = document.querySelector("#empty");
const repositoryBase = document.querySelector('meta[name="repository-base"]')?.content;
let sortKey = "title";
let sortDirection = "asc";

if (repositoryBase) {
  document.querySelectorAll("[data-repo-path]").forEach((link) => {
    link.href = new URL(link.dataset.repoPath, repositoryBase).href;
  });
  document.querySelectorAll("[data-project-link]").forEach((link) => {
    link.href = "project.html";
  });
}

function closeDetails(row) {
  const detail = document.querySelector(`#${row.dataset.detailId}`);
  const button = row.querySelector(".expand");
  if (detail) detail.hidden = true;
  if (button) button.setAttribute("aria-expanded", "false");
}

function compareRows(left, right) {
  let comparison = 0;
  if (sortKey === "status") {
    comparison = Number(left.dataset.statusRank) - Number(right.dataset.statusRank);
  } else if (sortKey === "date") {
    comparison = left.dataset.date.localeCompare(right.dataset.date);
  } else if (sortKey === "materials") {
    comparison = left.dataset.materials.localeCompare(right.dataset.materials, "en");
  } else {
    comparison = left.dataset.title.localeCompare(right.dataset.title, "en");
  }
  return sortDirection === "asc" ? comparison : -comparison;
}

function updateSortHeaders() {
  document.querySelectorAll("[data-sort-header]").forEach((header) => {
    const active = header.dataset.sortHeader === sortKey;
    header.setAttribute("aria-sort", active ? (sortDirection === "asc" ? "ascending" : "descending") : "none");
    const mark = header.querySelector(".sort-mark");
    if (mark) mark.textContent = active ? (sortDirection === "asc" ? "↑" : "↓") : "";
  });
}

function applyView() {
  const query = search.value.trim().toLowerCase();
  const selectedStatus = statusFilter.value;
  const selectedMaterial = materialFilter.value;
  let visible = 0;
  rows.forEach((row) => {
    const statusMatches = selectedStatus === "all" || row.dataset.status === selectedStatus;
    const materialMatches = selectedMaterial === "all" || row.dataset.materials.split("|").includes(selectedMaterial);
    const searchMatches = !query || row.dataset.search.includes(query);
    const show = statusMatches && materialMatches && searchMatches;
    row.hidden = !show;
    const detail = document.querySelector(`#${row.dataset.detailId}`);
    if (!show) closeDetails(row);
    if (detail && row.hidden) detail.hidden = true;
    if (show) visible += 1;
  });
  [...rows].sort(compareRows).forEach((row) => {
    const detail = document.querySelector(`#${row.dataset.detailId}`);
    tableBody.append(row);
    if (detail) tableBody.append(detail);
  });
  resultCount.textContent = visible;
  empty.style.display = visible ? "none" : "block";
  updateSortHeaders();
}

document.querySelectorAll(".sort-button").forEach((button) => {
  button.addEventListener("click", () => {
    const nextKey = button.dataset.sort;
    if (sortKey === nextKey) {
      sortDirection = sortDirection === "asc" ? "desc" : "asc";
    } else {
      sortKey = nextKey;
      sortDirection = nextKey === "date" ? "desc" : "asc";
    }
    applyView();
  });
});

document.querySelectorAll(".expand").forEach((button) => {
  button.addEventListener("click", () => {
    const row = button.closest("[data-source-row]");
    const detail = document.querySelector(`#${row.dataset.detailId}`);
    const willOpen = button.getAttribute("aria-expanded") !== "true";
    button.setAttribute("aria-expanded", String(willOpen));
    detail.hidden = !willOpen;
  });
});

search.addEventListener("input", applyView);
statusFilter.addEventListener("change", applyView);
materialFilter.addEventListener("change", applyView);
applyView();
"""


def build_page(root: Path, date: str, repository_base: str | None = None) -> str:
    registered_sources = prepare_sources(root)
    sources = [
        source for source in registered_sources if source["authority"] != "secondary-scholarly"
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
        material_options.append(
            '<option value="__none__">Not yet acquired</option>'
        )

    repository_base = repository_base.rstrip("/") + "/" if repository_base else ""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="repository-base" content="{html.escape(repository_base, quote=True)}">
<title>Materials · TEI P6 Research Vault</title>
<meta name="description" content="Working inventory of acquired primary materials and known gaps in the TEI P6 Research Vault.">
<style>{CSS}</style>
</head>
<body>
<div class="shell">
  <header class="site-header">
    <a class="brand" href="corpus.html"><span class="brand-name">TEI P6</span><span class="brand-context">Research Vault</span></a>
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
    output.write_text(page, encoding="utf-8")
    print(f"OK: {output} ({len(page)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
