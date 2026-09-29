# Normalized corpus records

Normalized records are machine-readable derivatives of raw acquisition
objects. They make heterogeneous sources queryable without pretending that a
record is the original. Like everything under `corpus/`, they are acquired
content, carry no instruction authority and are never a grounding target.

## Provenance

Provenance belongs to the file rather than to every row. Each normalized file
is a named object of an append-only run manifest under `sources/manifests/`,
which records the file path and its SHA-256 together with the source ID, the
adapter and its version, the requests or response journal, counts, gaps,
status and scope. A file a manifest names is never rewritten; a later run
writes a new file under a new name, as the SourceForge streams `-r2` to `-r4`
show, and `python -m tools.corpus.validate_control_plane .` checks every
recorded hash. The source lock names its manifests, and the registry holds
content authority, instruction trust and rights status. Raw response bytes
stay in the ignored local store `corpus/raw/`, addressed by SHA-256, and a row
points to them only where the table below names a raw pointer.

## Streams

Each stream records the upstream identity of an object together with its
kind; titles and URLs are labels. The table names identity and raw pointers
only. Other fields are specific to a stream and its collector, and no field is
promised for a stream whose collector does not write it.

| Files | Collector | Record and kind | Upstream identity | Raw pointer |
|---|---|---|---|---|
| `web/*.jsonl` | `tools.corpus.web_census` | one row per fetched page with `depth`, outgoing `links` and a `response` record | `response.canonical_url`, with `response.final_url` after redirects | `response.sha256`, `response.raw_path` |
| `assets/tei-council-assets.json`, `assets/tei-p5-4.12.0-release.json` | `tools.corpus.asset_snapshot` | one object whose `assets` list holds response records | `canonical_url` of each asset | `sha256`, `raw_path` per asset |
| `assets/tei-p5-4.12.0-release-members.json` | `tools.corpus.zip_inventory` | one object whose `entries` list the members of one archive | member `path` inside the archive named by `archive_sha256` | the archive hash; members carry CRC-32 and sizes only |
| `git/*.json`, `git/org/*.json` | `tools.corpus.git_snapshot` | one tree inventory per repository and requested ref | `repository`, `resolved_commit` and `root_tree`, then each entry's `path`, `object_type` and Git `object_id` | none; Git object IDs address the content |
| `github/teic-repositories.jsonl` | `tools.corpus.github_org_census` | `object_type: github-repository` | GitHub `id` and `node_id` | none; the manifest journals every response |
| `github/teic-tei-work-items.jsonl` | `tools.corpus.github_snapshot` | `kind`, for example `issue`, `pull-request`, `issue-comment`, `review`, `timeline-event` or `changed-file` | `node_id` or `id` where GitHub supplies one, `number` for issues, pull requests and milestones, `parent_number` for child rows; `changed-file` rows carry only `parent_number` and count files without identifying them | none; the manifest journals every response |
| `github/teic-tei-relations.jsonl` | `tools.corpus.github_relations` | `kind: relation` or `kind: review-thread` | source and target node IDs and numbers, or `thread_node_id` with `pull_number` | none; the manifest journals every response |
| `sourceforge/*.jsonl` | `tools.corpus.sourceforge_snapshot` | `object_type: ticket` | `tracker` and `ticket_num`, and `object_id` | `raw_responses` from `-r3` on; the earlier streams carry none |
| `mail/tei-l-psu.jsonl` | `tools.corpus.listserv_snapshot psu` | `object_type: mailing-list-message`, `via: psu` | `list`, `month` and `message_id` | `raw_sha256`, `raw_path` |
| `mail/tei-l-wayback-coverage.jsonl` | `tools.corpus.listserv_snapshot wayback-coverage` | `object_type: wayback-month-coverage` | `list` and `month` | none; the manifest records the CDX endpoint and months |
| Wayback message stream, no run recorded yet | `tools.corpus.listserv_snapshot wayback-fetch` | `object_type: mailing-list-message`, `via: wayback` or `via: wayback-index` | `list`, `month` and `message_id` | `raw_sha256`, `raw_path`, both null on a `wayback-index` row, which rests on the month index alone |
| `observed-practice/*.json` | `tools.ingest_editorial_cases` | one object with `scope`, `license`, `attribution` and `records` | `record_id` with repository `commit` and `path` | `sha256`, `raw_path` per record |

## Rights and content

The rights rule in `knowledge/data.md` decides what a stream may carry. The
web, GitHub, SourceForge and TEI-L streams carry identifiers, metadata, links
and pointers, while discussion, ticket and message bodies stay in the raw
store; SourceForge rows state this in `body_present_in_raw`. The TEI-L streams
carry no sender field. SourceForge usernames and GitHub author and actor node
IDs are kept as the interface exposed them. Only the observed-practice records
hold source text, under the license and attribution recorded in the file and
in its lock. JSONL serializes streams and JSON bounded objects, and derived
summaries and embeddings do not belong in this layer.
