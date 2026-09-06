"""Build presentation-ready material-source records from control data."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tools.sitegen.source_data import load_source_records, resolve_repo_file

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


def gap_records(
    lock: dict[str, Any], manifests: list[dict[str, Any]]
) -> list[dict[str, Any]]:
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


def material_records(
    manifests: list[dict[str, Any]], manifest_refs: list[str]
) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for manifest, manifest_ref in zip(manifests, manifest_refs, strict=True):
        manifest_records: list[dict[str, str]] = []
        run_id = str(manifest.get("run_id") or Path(manifest_ref).stem)
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
                        "run_id": run_id,
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
                            str(adapter_name),
                            "Acquired holding from this acquisition run.",
                        ),
                        "path": "",
                        "status": str(manifest.get("status") or ""),
                        "manifest_ref": manifest_ref,
                        "kind": str(adapter_name or ""),
                        "run_id": run_id,
                    }
                )
        records.extend(manifest_records)
    return records


def prepare_sources(root: Path) -> list[dict[str, Any]]:
    """Build stable presentation records from reconciled source controls."""
    prepared: list[dict[str, Any]] = []
    for loaded in load_source_records(root):
        source = loaded["source"]
        source_id = loaded["source_id"]
        lock = loaded["lock"]
        manifests = loaded["manifests"]
        manifest_refs = loaded["manifest_refs"]
        counts = source_counts(lock, manifests)
        gaps = gap_records(lock, manifests)
        rights = source.get("rights") if isinstance(source.get("rights"), dict) else {}
        source_types = source.get("vault_source_types")
        materials = material_records(manifests, manifest_refs)
        # Every normalized holding a manifest declares must exist below the root.
        for artifact in normalized_artifacts(manifests):
            resolve_repo_file(root, artifact)
        prepared.append(
            {
                "source_id": source_id,
                "title": SOURCE_TITLES.get(source_id, str(source.get("title", ""))),
                "registered_title": str(source.get("title", "")),
                "description": SOURCE_DESCRIPTIONS.get(
                    source_id,
                    "Registered primary-source holding of the research project.",
                ),
                "family": str(source.get("family", "")),
                "family_label": FAMILY_LABELS.get(
                    str(source.get("family", "")), str(source.get("family", ""))
                ),
                "authority": str(source.get("authority", "")),
                "status": loaded["status"],
                "as_of": str(lock.get("as_of", "")),
                "rights": str(rights.get("rights_status", "not specified")),
                "source_types": (
                    ", ".join(str(item) for item in source_types)
                    if isinstance(source_types, list)
                    else "not specified"
                ),
                "metrics": selected_metrics(counts),
                "materials": materials,
                "gaps": gaps,
                "gap_count": counts.get("gaps", len(gaps)),
                "lock_ref": loaded["lock_ref"],
                "manifest_refs": manifest_refs,
                "upstream": upstream_links(source.get("upstream", {})),
            }
        )
    return prepared
