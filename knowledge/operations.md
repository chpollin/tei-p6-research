---
title: Operations
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-11"
related: [INDEX, schema, data, verification, testing, governance, state, journal]
---

# Operations

These procedures produce and check the artifacts defined in
[[knowledge/schema]]. The material they operate on is described in
[[knowledge/data]], the adversarial checks in [[knowledge/verification]] and
the completion gate in [[knowledge/testing]]. Record processing state in
[[knowledge/state]] and durable decisions in [[knowledge/journal]].

## Environment

A working checkout needs Git, Python 3.11 or newer, PyYAML, pytest for the
test suite, ruff for the linter, and the GitHub CLI when authenticated GitHub
acquisition or repository administration is required. Install with `uv`:

```powershell
uv sync
```

Without `uv`, use a Python virtual environment and install the declared tools.
This fallback does not reproduce the full transitive lock; `uv sync --locked`
is the reproducible setup:

```powershell
python -m pip install pyyaml pytest==8.4.2 ruff==0.15.21 rdflib==7.6.0
```

Verify the checkout:

```powershell
python tools/validate.py .
python -m pytest tests
```

Warnings such as `W-EMPTY` and `W-NO-OUTPUT` describe missing production
artifacts. Investigate and report them rather than hiding them. Their current
applicability belongs in [[knowledge/state]].

The repository root is the Obsidian vault, and the committed `.obsidian/`
configuration uses core features only. Personal workspace state, caches and
installed community plugins remain uncommitted. Human readers start at
`README.md` and route through [[knowledge/INDEX]]. The repository continues to
work as plain Markdown without Obsidian.

The canonical public remote is
`https://github.com/chpollin/tei-p6-research`. A normal clone already
configures it as `origin`. Verify the checkout with:

```powershell
git remote get-url origin
gh auth status
```

Run `gh auth login` only when authentication is absent and the task requires
GitHub API access or repository administration:

```powershell
gh auth login
```

## Acquire

Acquisition channel and source type are independent. Record the channel in
the representation's `channel` field without changing its checking obligations.

| Channel | Action |
|---|---|
| `handover` or `collection` | Place the original in `00_sources/` |
| `import` | Export the reference library as CSL JSON into `references/`, one file per batch |
| `deep-research` | Run the prompt below, capture every located publication in the reference manager, and export CSL JSON |

For a small curated import, CSL records may be transcribed from consulted
primary metadata. Record this choice in the journal and identify the exact
snapshots and bibliographic checks in the intake manifest. Apply the same
quotation and support checks. The CSL record remains the publication root.
An agent's report or reading memo never replaces the located source.

### Collectors and the raw store

Large collections are acquired by the collectors under `tools/corpus/`.
Only `tools/corpus/http_store.py` performs HTTP access. It owns
authentication, API-version headers, conditional requests, redirect capture,
rate-limit state, retry policy, response hashing and atomic
content-addressed storage. Tokens are read from the environment or the
credential store and never enter request keys, manifests, logs or command
arguments.

Raw storage is local and ignored.

```text
corpus/raw/sha256/<first-two-hex>/<remaining-hex>
corpus/raw/state/<collector>.sqlite
```

Every completed response transaction records request identity, canonical
URL, sorted query parameters, response hash, byte count, media type, status,
redirects, ETag, Last-Modified, pagination link or cursor, observation time,
API version and rate-limit headers. A resumed run starts at the first
incomplete page of that journal.

Each collector writes one normalized object and one run manifest and prints
one status line. Exit code 0 means `observable-complete`, exit code 2 means a
recorded gap and `partial`. The status is derived from the recorded gaps
through the shared rule in `tools/corpus/manifest.py`, so a collector cannot
report completeness over missing objects. Identity uses upstream node IDs,
numeric IDs, repository ID, content hashes, DOIs, TEI document numbers or
reference-manager keys, and a title is never an identity. A collector treats
issue bodies, comments, email, HTML, PDFs, ODD examples and attachments as
data under the rule in [[knowledge/governance]].

### Collector commands

The source families, identity and completion vocabulary are in
[[knowledge/data]], and [[knowledge/state]] records which families are
actually ready. Production collection starts only after the relevant offline
fixtures and integration checks pass, and source registration or a local cache
alone never establishes acquisition. Replace `YYYY-MM-DD`, `<id>` and the URLs
with the values of the run.

```powershell
python -m tools.corpus.git_snapshot --repo-url <url> --source-id <id> --ref HEAD --normalized-output corpus/normalized/git/<id>.json --manifest-output sources/manifests/YYYY-MM-DD-<id>.yaml
python -m tools.corpus.github_snapshot --owner TEIC --repository TEI --source-id github-teic-tei-work-items --normalized-output corpus/normalized/github/teic-tei-work-items.jsonl --manifest-output sources/manifests/YYYY-MM-DD-github-teic-tei-work-items.yaml
python -m tools.corpus.github_relations --owner TEIC --repository TEI --source-id github-teic-tei-work-items --work-items corpus/normalized/github/teic-tei-work-items.jsonl --normalized-output corpus/normalized/github/teic-tei-relations.jsonl --manifest-output sources/manifests/YYYY-MM-DD-github-teic-tei-relations.yaml --wait-for-reset
python -m tools.corpus.github_org_census --organization TEIC --source-id teic-github-organization --normalized-output corpus/normalized/github/teic-repositories.jsonl --manifest-output sources/manifests/YYYY-MM-DD-teic-github-organization.yaml
python -m tools.corpus.github_org_git_snapshot --census corpus/normalized/github/teic-repositories.jsonl --normalized-root corpus/normalized/git --manifest-root sources/manifests/repos --manifest-output sources/manifests/YYYY-MM-DD-teic-public-git-repositories.yaml
python -m tools.corpus.web_census --source-id <id> --root-url <url> --allow-prefix <prefix> --depth 2 --max-pages 500 --normalized-output corpus/normalized/web/<id>.jsonl --manifest-output sources/manifests/YYYY-MM-DD-<id>.yaml
python -m tools.corpus.sourceforge_snapshot --tracker bugs=https://sourceforge.net/rest/p/tei/bugs --tracker feature-requests=https://sourceforge.net/rest/p/tei/feature-requests --tracker support-requests=https://sourceforge.net/rest/p/tei/support-requests --workers 8 --delay-seconds 0.2 --normalized-output corpus/normalized/sourceforge/tei-legacy-trackers.jsonl --manifest-output sources/manifests/YYYY-MM-DD-tei-legacy-sourceforge.yaml
python -m tools.corpus.asset_snapshot --source-id <id> --url <asset url> --normalized-output corpus/normalized/assets/<name>.json --manifest-output sources/manifests/YYYY-MM-DD-<name>.yaml
python -m tools.corpus.zip_inventory --source-id <id> --archive corpus/raw/sha256/<aa>/<rest> --normalized-output corpus/normalized/assets/<name>-members.json --manifest-output sources/manifests/YYYY-MM-DD-<name>-members.yaml
```

The three-part TEI-L boundary defined in [[knowledge/data]] is collected by one
module in three modes. Message bodies and sender identities stay in the raw
store, and the normalized stream holds metadata only.

```powershell
python -m tools.corpus.listserv_snapshot psu --from-month 2512 --to-month YYMM --delay-seconds 1.0 --normalized-output corpus/normalized/mail/tei-l-psu.jsonl --manifest-output sources/manifests/YYYY-MM-DD-tei-l-psu.yaml
python -m tools.corpus.listserv_snapshot wayback-coverage --from-month 9001 --to-month 2512 --delay-seconds 0.5 --normalized-output corpus/normalized/mail/tei-l-wayback-coverage.jsonl --manifest-output sources/manifests/YYYY-MM-DD-tei-l-wayback-coverage.yaml
python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --delay-seconds 1.0 --normalized-output corpus/normalized/mail/tei-l-wayback.jsonl --manifest-output sources/manifests/YYYY-MM-DD-tei-l-wayback.yaml
```

After a run, validate the control plane:

```powershell
python -m tools.corpus.validate_control_plane .
```

Admission of a selected source into the knowledge chain follows § Ingest.

### Run manifests

Every run manifest under `sources/manifests/` includes at least these fields.

```yaml
schema_version: 1
run_id: <stable-id>
source_id: <registry-id>
started_at: <UTC timestamp>
finished_at: <UTC timestamp or null>
status: planned | partial | observable-complete | bounded-complete | failed
scope:
  boundary: <observed-interface-or-sample>
  status_applies_to: <request-or-object-boundary>
adapter:
  name: <name>
  version: <version-or-code-sha>
requests: []
objects: []
counts: {}
gaps: []
rights_exceptions: []
```

`source_id` resolves the lock through the registry, which remains
authoritative even when a manifest repeats `lock_file`. The manifest status
applies only to its declared request and `scope`. Counts belong only in
manifests produced from observed data, and registry and lock files keep
`counts: {}` until a run has enumerated the source. Manifests are
append-only, and a correction is a new manifest related with `corrects`.
Each object records its stable upstream ID, canonical URL, observed and
upstream timestamps, request or API version and pagination position, HTTP
status and safe response headers, raw SHA-256, byte length and media type,
normalized SHA-256 and transformation version, rights and trust
classifications, and its gap or error state when retrieval or parsing
failed. Access tokens, cookies, authorization headers, signed download URLs
and personal local paths are never recorded.

### GitHub work items

Authenticated access through `gh auth login` or `GITHUB_TOKEN` is required.
The bootstrap is serial, resumable and bounded, and exactly one collector
owns the authenticated quota and the request journal. The bootstrap order
is:

1. repository, labels, milestones and releases;
2. all work items and a separate pull-request census;
3. repository-wide issue, review and commit comments;
4. one fully paginated timeline per work item;
5. pull-request detail, reviews, commits and changed files;
6. GraphQL-only review-thread and relationship fields;
7. a second parent census and reconciliation.

The collector uses pages of 100, records `Link` headers or GraphQL cursors,
respects `Retry-After` and stops with a `rate-limit-stop` gap while quota
remains. A partially completed crawl is `partial`. An observable-complete
manifest requires exhausted pagination for every declared collection, issue
and pull-request totals reconciled independently, every pull request present
in both the work-item and the pull-request census, every work item with a
completed timeline or an explicit gap, every pull request with reviews,
commits, changed files and explicit API-limit gaps, unique stable IDs for
every object family, a start and end census reconciling the non-atomic
snapshot interval, verified raw and normalized hashes, and every error,
rights restriction and inaccessible record represented. The family
definition of `observable-complete` is in [[knowledge/data]].

Incremental runs start from the last successful finish time minus 24 hours,
fully rehydrate changed parents and retain prior body versions. They never
overwrite history. A periodic full identifier and timeline reconciliation
checks for missed changes. The issue endpoint contains issue-shaped pull
requests, which are separated by the `pull_request` field and reconciled
against the pull-request census.

### Governance, history and literature

Governance documents distinguish meeting events from agendas, draft minutes,
approved minutes, attachments and reports. Website, XML, PDF and repository
copies are manifestations rather than automatic duplicates. Reported and
parsed dates remain separate when the official index is inconsistent.

The literature boundary starts with:

1. the official TEI Zotero group, paginated with library and item versions;
2. all Journal of the TEI metadata exposed by the OpenEdition OAI-PMH set
   `journals:jtei`;
3. the bibliography in the pinned Guidelines release;
4. declared TEI conference proceedings;
5. at most one recorded citation-chaining pass for selected design topics.

Every discovered work receives a disposition, one of `included`,
`duplicate`, `excluded-with-reason`, `unavailable` or `pending-review`. Full
text is committed only after per-item rights review under the rule in
[[knowledge/data]].

### Recovery

- An interrupted API run resumes from the request journal and remains
  `partial`.
- Source-hash drift quarantines the new observation and never rewrites a
  lock.
- A failed count reconciliation leaves the previous accepted manifest active.
- A schema change pauses dependent work and is integrated before workers
  rebase.
- Generated drift is repaired by rebuilding from accepted inputs.
- Rights uncertainty sets the source to metadata and link only until it is
  independently reviewed.
- A post-merge failure is undone with `git revert`, which keeps the history
  intact.

#### Wayback checkpoint and resume

`wayback-fetch` sichert jeden abgeschlossenen Monat im lokalen Rohdatenspeicher.
Der Checkpoint enthält die Identität der Coverage-Eingabe, die gewählten Monate,
das Nachrichtenlimit und versiegelte Monatsblöcke mit Metadaten und Rohdatenhashes.
Vor Wiederverwendung werden Eingabeidentität, Optionen und referenzierte Bytes
geprüft. Fertige Monate benötigen keine neue HTTP-Anfrage; abgebrochene oder
vorübergehend fehlgeschlagene Monate werden erneut versucht.

Checkpointversion 2 berücksichtigt leere Abstandszellen in historischen
LISTSERV-Kopftabellen. Ältere Checkpoints werden zurückgewiesen, damit deren
Nachrichtenklassifikation nach einer Parserkorrektur neu geprüft wird.

```powershell
python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --checkpoint corpus/raw/checkpoints/<run-id> --delay-seconds 0.5 --normalized-output corpus/normalized/mail/<run-id>.jsonl --manifest-output sources/manifests/<run-id>.yaml
python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --resume-from corpus/raw/checkpoints/<run-id> --delay-seconds 0.5 --normalized-output corpus/normalized/mail/<continued-run-id>.jsonl --manifest-output sources/manifests/<continued-run-id>.yaml
```

Die Wiederaufnahme verwendet dieselbe Monatenauswahl und dasselbe
`--max-messages` wie der Ursprungslauf. Für bereits abgeschlossene partielle
Läufe werden neue Ausgabe- und Manifestpfade gewählt, damit historische
Prüfsummen gültig bleiben. Checkpoints sind lokale Prozessartefakte. Sie
begründen weder eine Quellenaufnahme noch einen neuen Evidenzstatus.
Lose Rohdateien eines alten Laufs ohne Checkpoint sind nicht allein anhand
ihres Inhalts sicher einem Monat oder einer Anfrage zuzuordnen.

### Deep research prompt skeleton


> Research the topic **{topic from the controlled topic set}** for the project **{project}**.
> Search broadly, then prioritize: peer-reviewed and official sources first;
> exclude: {project exclusion list}. Evaluate candidates at full text.
> Counter-check adversarially: for each candidate finding, search for sources
> that contradict it. Deliver a list of publications with full bibliographic
> data and, per publication, the two or three passages that matter for the
> topic, quoted verbatim. Do not deliver synthesis; the vault synthesizes.

## Ingest

A source package enters the knowledge chain only after identity and
checksum verification, rights classification and source-type assignment, as
[[knowledge/data]] requires. Record the admission in a manifest that names
the exact snapshot, the hashes and the rights disposition of every admitted
object. Never create a shortcut from the acquisition corpus to a higher
evidence layer. Before topic-scale distillation begins, take one
rights-cleared source through the canonical chain end to end.

For an archivable document, first convert the original to Markdown while
preserving its headings, lists, tables, and paragraph boundaries. Then stamp
each anchor-relevant paragraph with a block ID. The resulting representation
is immutable.

Choose the converter by source structure and record it in `converter`.

| Source structure | Conversion |
|---|---|
| Short, simple text | Agent conversion |
| Standard office or PDF document | MarkItDown or pandoc |
| Complex layout or scanned document | Docling |
| Image requiring OCR | Unelaborated extension point |

| Source type | Required artifact |
|---|---|
| `document` | Markdown in `10_markdown/documents/`, with converter, original H1, and metadata |
| `data` | Data file in `10_markdown/data/` and a schema description with the same slug and metadata |
| `publication` | CSL JSON in `references/`, with no Markdown representation |

GitHub issue threads, pull-request threads and mailing-list threads are
admitted as citation-only publication sources. The raw thread stays in the
private raw store, the CSL record carries identifier, URL, dates and roles,
and the distillate carries the structured account of the thread with short
quotations checked against the raw snapshot at intake and recorded as
`checked.quote`. This is the path the research-wave-one literature already
uses. A generated metadata index of threads is a navigation projection and
never grounding.

After a representation change, regenerate
[[corpus/projections/source-inventory]] from the files and revalidate:

```powershell
python tools/inventory.py . --write
python tools/validate.py .
```

### Full Guidelines reference intake

The complete technical boundary in [[knowledge/data]] is admitted with:

```powershell
python -m tools.ingest_guidelines
python -m tools.ingest_guidelines --check
python -m tools.ingest_guidelines --refresh-coverage
```

The first command requires the pinned local Git mirror, reuses existing
admissions without changing them, and resumes an interrupted intake by
checking already written immutable files. It writes the admission manifest
only after every declared source is reconciled. It then regenerates the
JSON and Markdown coverage projections from the admitted files and actual
distillates. A repeat run may update those navigation projections; it never
overwrites changed source representations or an incompatible admission.

`--check` needs neither the mirror nor ignored originals. It reads the exact
XML embedded in the tracked representations, checks Git blob identities,
reproduces their converter output, proves the declared source and include
boundary, checks the admission record, and compares both coverage outputs.
Missing sources, modified bytes and stale processing counts fail the check.
If local originals exist, their bytes must also reconcile.

After adding or changing a distillate, regenerate the coverage with
`--refresh-coverage`, regenerate the inventory and affected pages, and run
the check. This mode verifies the tracked admission and updates only the
projections; it needs neither ignored originals nor a Git mirror.
The public Materials view exposes contents-level processing; Knowledge
exposes the individual sources and their precise anchored passages.

### Export and discovery

The admitted Guidelines can be exported without a local mirror or originals:

```powershell
uv run python -m tools.export_guidelines --output ../tei-p5-4.12.0-xml
uv run python -m tools.export_guidelines --output ../tei-p5-4.12.0-xml --check
```

The output retains upstream `P5/...` paths and exact XML bytes. The export
inventory records hashes, attribution and non-exported assets. Identical
existing files are reusable; conflicting files, path escapes and reparse points
fail before known conflicts can cause writes. Atomic publication requires
hardlink support. Generated HTML, schemas and images remain outside the export.

Rebuild the separate discovery projection after a coverage or topic-map change
with `python -m tools.build_guidelines_navigation`; `--check` compares its
recorded inputs and output. It joins declared atlas relations to source passages
and records rule-based topic suggestions. It never changes source metadata or
establishes scholarly classification.

## Distill

The bounded structure run uses `python -m tools.check_text_structures --emit
--scope source` and the corresponding `--scope assertion` to freeze its review
pairs. The source runner recovers XML ancestor identities from the exact
embedded source and adds bibliographic identities for citation-only sources;
it leaves the global cutter and immutable representations unchanged. Running
`python -m tools.check_text_structures` audits both recorded verdict batches
against the current pairs. Missing verdicts fail the audit. Emission assigns
no review status, and the runner never books a status automatically.

The five quotations in this run can be checked against local raw snapshots
with `python tools/check_wave1_sources.py --manifest
sources/manifests/2026-09-07-text-structures-citations.yaml --references
references/text-structures-run1.json`. A clean clone can inspect the admitted
quotations and their hashes; repeating that fidelity check requires the named
local snapshots.

### Systematic Guidelines distillation

Technical availability is followed by source-specific scholarly extraction.
Keep one distillate per source and process large sources by their actual
section boundaries before reconciling the result into that distillate.
The review record under `workbench/reviews/<run-id>/` must identify each
examined section by source path and XML location, what was extracted, and
any exclusion or remaining section with its reason. A short summary or a
passing support review of selected statements does not establish that the
whole chapter was examined.

For each substantive section, examine its concepts, normative rules,
encoding alternatives, examples, exceptions, dependencies and capabilities
that an evolution must preserve. Front matter and bibliography may warrant
descriptive extraction or a reasoned exclusion from a particular research
question. Assertions are selected for the research question after source
distillation; no fixed number of statements per paragraph is required.
Compare prose, formal declarations and practice at the assertion layer,
and preserve disagreements and their release identities.

### Extraction and fidelity

Produce one distillate per source through three steps.

1. Extract core statements with the canonical prompt, one statement per
   anchor, without evaluation or cross-source merging.
2. Apply the section skeleton, statement IDs, and anchor syntax in
   [[knowledge/schema]] through deterministic formatting.
3. Compare every statement with its source anchor. For publications, check
   the quotation while the full text is available and record `checked.quote`.

Reformulate or discard statements that fail fidelity checking and repeat the
check until every retained statement passes. Write any optional Appraisal
afterwards so that judgments cannot influence the extraction. Appraisal
remains outside the source-fidelity check.

### Canonical extraction prompt skeleton

> Extract the core statements of the source **{source short title}**, and of this
> source alone. Work only from the text given below.
> One statement per anchor. Each statement stands on its own, is understandable
> without its neighbours, and stays within the literal sense of the source.
> Do not evaluate, do not interpret, do not infer, and do not merge this source
> with any other; the vault synthesizes at a later layer.
> No statement without a nameable source location. Where you cannot name one,
> drop the statement.
> Deliver per statement the statement itself and its source location, in the form
> the source type requires: for a document the block it was taken from, for a
> publication the verbatim quotation with page, for data the computation that
> yields the stated result.
>
> SOURCE: {Markdown representation, quotation set, or data schema description}

Set the new distillate to `grounded`, then run the same pair again:

```powershell
python tools/inventory.py . --write
python tools/validate.py .
```

## Build assertions

Work by topic, with one file per assertion.

1. Enter through the topic map and read every distillate registered there.
2. Group statements about the same matter across sources and source types.
3. Formulate one atomic assertion per group, supported jointly by that group.
   An atomic statement cannot be split without losing its point.
4. List the supporting statement IDs in `grounding`, one per supporting
   source, and explain each anchor's contribution in Support.
5. For irreconcilable statements, write two assertions, mark both `contested`,
   and link them reciprocally through `contested-with`.
6. Reserve unsupported conclusions and distillate appraisals for output posits.
   They cannot ground assertions.
7. Register each assertion in its topic map with a short orientation and
   record unresolved questions under Open questions.

Machine-review every assertion against each supporting statement under the
protocol in [[knowledge/verification]]. Only *fully supports* passes. Narrow
a failed assertion or replace its unsupported anchor with one that carries
the claim, then review the changed pair again. Before an assertion supports
a design requirement, run and record the counterevidence search defined
there.

### Assertion review prompt skeleton

> You are an adversarial reviewer. Below are a distillate statement and an
> assertion that claims to be supported by it. Your task is to refute the
> assertion. Judge only whether this statement supports this assertion; whether
> the assertion is true is out of scope. Answer with exactly one verdict: fully supports
> | partially supports | overreaches | contradicts | not in the text. Then give
> one sentence of justification, and where the verdict is not *fully supports*,
> name the part of the assertion that the statement does not carry.
>
> STATEMENT: {distillate statement, without its own grounding anchor}
> ASSERTION: {assertion as one sentence}

## Write chapters

Use the working language and style sheet in [[knowledge/specification]].
Every load-bearing sentence receives a `Grounded in [[assertion]]` footnote
or, for an own conclusion, a
`Posit: <rationale>. Open evidence question: <question>` footnote. Mirror the
referenced assertions and posit count in frontmatter and update the chapter
register in [[knowledge/state]].

A synthesis of a topic uses the same chapter contract. Enter through its map.
Ground agreement in the relevant assertions and disagreement in both sides of
a contested pair. Citing only one side triggers `W-CONTESTED`. A research gap
drawn from the map's open questions enters as a posit with its evidence
question. A synthesis chapter remains an ordinary chapter even when it later
informs another chapter.

## Analyze

Five recurring analysis tasks specialize the operations above without adding
an artifact type. Each enters through the matching topic map, follows
load-bearing statements down to their distillate statements and, where
exactness matters, to source passages, and reports the absence of support as
an open question instead of completing a gap from model memory. Persistent
knowledge from any of them enters through acquire, ingest, distill and
assertion building. A chat answer may report what the present vault does and
does not support and points to canonical anchors. Every task separates source
observation, cross-source assertion and author posit, preserves release,
repository, date and source-state qualifiers, and runs the checks in
[[knowledge/testing]] when the vault was edited.

### Analyze an element

Fix the exact element name, with namespace where ambiguity is possible, and
the P5 release or commit, defaulting to the pinned baseline. Establish the
formal identity from the pinned ODD or generated schema, meaning owning
module, classes, inherited attributes, content model, datatype or
constraints and documented availability. Establish the prose semantics
separately from the formal declaration, because a name alone carries no
intended meaning. Inspect examples only for the behavior they demonstrate.
Trace deprecation, replacement or historical rationale through the issue and
decision procedure when such a claim matters. Test boundary cases against the
pinned schema when validation behavior is part of the question and record
the exact schema and command. Report identity, semantic purpose, formal
model, interactions, representative patterns, version scope and open
questions. A generated declaration proves the declaration in that pinned
build and nothing about its rationale. Guidelines prose explains intention
and does not replace the executable content model when validation behavior
is claimed. GitHub discussions establish attributed proposals, and a claim
that TEI changed requires merged and released evidence.

### Analyze a module

Fix the module identifier and release or commit before collecting facts.
Establish from the pinned declarations the module purpose, the elements and
classes it defines, dependencies, class memberships, macros and constraints.
Select representative elements by modeling role and analyze them with the
element procedure where a detail affects the module conclusion. Map
cross-module dependencies explicitly, distinguishing mandatory dependency,
shared class membership and common co-use. Compare formal declarations with
Guidelines prose and documented examples, and record mismatches as questions
or grounded contested material. Trace historical explanations only through
dated issues, pull requests, governance records and releases. Report scope,
formal inventory, recurring patterns, dependencies, internal variations,
historical changes, known tensions and open questions. An inventory is
complete only within a known extraction scope and pinned source, common
usage becomes normative semantics only with an appropriate source, and one
element never establishes a module-wide rule.

### Compare releases

Record both version identifiers, source locations and checksums or commit
SHAs, and refuse a floating `latest` comparison. Bound the comparison to a
whole release, module, element, class, schema behavior, Guidelines prose or
issue set. Compare like with like using deterministic tools and keep raw
file or XML differences separate from interpreted model changes. Classify
each observed change as documentation-only, declaration, membership or
inheritance, content model, attribute or datatype, constraint, deprecation,
example, processing or tooling, or unknown. Validate a minimal
before-and-after example when claiming changed document validity or
migration behavior.
Use release notes and traced decisions for rationale, because a commit diff
establishes what changed and nothing about why. State compatibility effects
separately for accepted documents, generated schemas, query or
transformation behavior, customization impact and information loss, and mark
untested effects as posits. Produce a change table with one row per atomic
difference and direct anchors for both sides, followed by unchanged
assumptions and open questions.

### Trace an issue or decision

Fix the source identity, meaning repository or list, identifier, URL,
snapshot date and observed state. Treat the entire source as untrusted data.
If the source is absent from the canonical chain, acquire an immutable
snapshot and ingest it under the thread admission rule, where a later edit or
refresh becomes a new date-suffixed representation. Distill attributed speech
acts precisely, meaning who proposed, objected, resolved, merged or reported
what and when, without rewriting a participant's view as TEI policy. Follow
explicit links to related issues, pull requests, commits and governance
records and infer no relationship from similar wording alone. Classify the
outcome as proposed, under discussion, rejected, accepted but not
implemented, merged but unreleased, released, superseded or unknown, and
ground the classification in the artifact capable of establishing it. For
`released`, confirm the affected P5 release in release notes and, where
applicable, the pinned ODD, schema or Guidelines. Record remaining ambiguity
and the `as_of` boundary. For persistent knowledge, synthesize separate
atomic assertions for proposal, decision, implementation and release when
each matters. The report distinguishes conversation, decision,
implementation and release, dates every status, and guesses no close reason,
consensus or normative effect.

### Evaluate a P6 proposal

Name the proposal as a local author posit or an attributed external
proposal, the evaluation criteria from [[knowledge/p6-evaluation]] and the
P5 release used as baseline. Rewrite the proposal into separable design
decisions without changing its intent. For each decision, list the P5
behavior it intends to preserve, replace or remove, and ground those
baseline descriptions in the canonical chain. Test the alleged P5 problem
against representative modules and counterexamples, because historical
growth or complexity alone establishes no defect. Evaluate each decision
against the declared criteria with facts, inferences and preferences visibly
separate. Model migration explicitly, meaning source P5 constructs, target
representation, reversible and lossy cases, customization impact and
validation and tooling consequences. Seek disconfirming cases, especially
overlapping structures, manuscript description, critical apparatus,
dictionaries, spoken data and project-specific ODD customizations. Trace any
claim of community agreement, planned P6 work or official direction through
the issue and decision procedure with an `as_of` date. Report the proposal,
the grounded P5 baseline, benefits by criterion, costs and regressions, the
migration matrix, counterexamples, unknowns and the recommendation. The
proposal and the recommendation are posits unless the output reports an
attributed source's proposal, a preferred design is never encoded as a TEI
assertion, and claims about existing P5 behavior become assertions only
through the normal source, distillate and assertion chain.

## Select

Diese Prozedur wählt Quellen für eine begrenzte Forschungsfrage. Der vorhandene Referenzbestand bleibt erhalten; eine Auswahl bestimmt seine Verwendung in einem Forschungslauf. Die historischen Fragen der ersten Themenläufe stehen im [Auswahlkontext](../workbench/selections/2026-09-06-topic-run-context.md).

`tools.select_sources` führt die deklarierte Auswahl offline aus. Die Ausgabe enthält die Suchausdrücke, Trefferidentitäten, Snapshot- und Manifestprüfsummen sowie Abdeckungslücken. Eine Aufnahme oder Forschungsbewertung erfolgt anschließend nach dieser Prozedur.

```powershell
python -m tools.select_sources --github-label "Status: Reconsider for P6" --github-label "Status: Wontfix"
python -m tools.select_sources --atlas-member att.fragmentable --atlas-attribute part
python -m tools.select_sources --queries workbench/selections/<declared-query-file>.yaml --output workbench/selections/<new-run>.json
```

Eine Abfragedatei enthält eine Liste unter `queries`, mit je `id`, `stream` und beispielsweise `pattern` oder `label`. Die zulässigen Formen stehen in `python -m tools.select_sources --help` und im Modulvertrag. Der [Abgleich der Gegenbelegsuche vom 2026-09-11](../workbench/selections/2026-09-11-counterevidence-reconciliation.md) hält die fehlende Wontfix-Abfrage der ersten beiden Läufe und ihre 32 Kandidaten fest. Die anschließende [Einzelprüfung der Beschreibungen und Kommentare](../workbench/selections/2026-09-11-wontfix-context.md) ergänzt diese historischen Auswahlprotokolle mit begründeten Auswahlen und Korrekturen; eine empfohlene Aufnahme ist weiterhin kein eingelesener Beleg.

### Selection procedure

#### 1. Evidence questions

A run takes its questions from four places in this order. First come the
posits of `40_output/12-p6-design.md` whose open evidence question names a
construct or a phenomenon of the topic. Second come the posits of the topic's
own chapter, where one exists. Third come the open questions of the topic map
`30_assertions/MOC-<Topic>.md`. Fourth come the gaps named under Open work in
[[knowledge/state]]. Each question receives an identifier and one of two
kinds. A coverage question asks which source states, declares or encodes
something. A problem claim holds that P5 folds two things into one construct,
lacks a construct or leaves a rule unstated, and every problem claim receives
a counterevidence query under step 4. The list of questions is closed before
the first query runs, and a question that arises later belongs to the next
run of the topic.

#### 2. Declared queries

From the questions the run derives, before any query runs, one finite list
of terms per family and records it with the run. Specification idents, class
names and attribute names come from the questions and from the glossary
entries of the topic. Guidelines chapters are named by file. Title and
subject terms are regular expressions matched without regard to case. An
ident that is also an ordinary word, such as name, key, ref, state, event,
part, line, head, note or place, is queried in a marked form, as `@key`,
`<name>` or `att.naming`, because the bare word returns homonyms that would
have to be rejected one by one; where a bare form is declared anyway, the
declaration says so and the homonyms are booked as rejections. Two GitHub
labels are queried in every run, `Status: Reconsider for P6` because it is
the official process's own marker of P6 relevance, and `Status: Wontfix`
because it is a counter-signal for the dispositions.

#### 3. Family queries

Each family is queried with its declared terms against a named snapshot, and
the query, the snapshot and the hit count go into the run's table.

- P5 specifications. The atlas `corpus/projections/p5-specs-4.12.0.json` is
  read through its `records` list with three lookups, an ident lookup on
  `ident`, a membership lookup that returns every record whose
  `classes_declared` names the class, and an attribute lookup that returns
  every record whose `local_attributes` declares the attribute. A hit is the
  file `P5/Source/Specs/<ident>.xml` at the pinned commit
  `113e933e21f016e2655518321e9d10214b8d9fcb`. The atlas is a navigation aid,
  the admitted object is the Git blob, and membership means declared
  membership only, because the atlas does not expand inheritance; a class
  reached through another class is followed by hand and the chain is written
  into the table.
- Guidelines chapters. `git ls-tree` of `P5/Source/Guidelines/en/` at the
  pinned commit lists the chapter files. A chapter is a hit when it documents
  the module of a hit specification or the phenomenon of a question. Chapters
  are admitted whole with their XInclude references unresolved, as in the
  entity run, so that every specification a chapter pulls in is a separate
  admission.
- Encoded practice at the pinned release. The test documents under `P5/Test/`
  at the pinned commit are queried by file name and characterized by a
  deterministic count of the elements and attributes the questions name; the
  count goes into the table. The `exemplum` blocks of a specification travel
  with that specification. Real editorial documents enter only through the
  sampling protocol of research package B in [[knowledge/plan]]; a run may reuse a document
  the vault has already admitted by extending its distillate, which cuts new
  pairs for review and leaves the reviewed pairs untouched.
- GitHub work items. The stream `corpus/normalized/github/teic-tei-work-items.jsonl`
  is read once per record with `kind` `work-item-detail`, matched on
  `title` and filtered by `labels`. Companion `issue` and `pull-request-summary`
  records identify the work-item kind without creating additional hits.
  A hit is listed with number, kind, state,
  creation and closing dates, comment count and labels, and the table names
  the manifest of the stream it read. Bodies stay in the private raw store,
  and a thread is admitted only when its raw snapshot is present in the
  checkout that ingests it.
- SourceForge tickets. The stream `corpus/normalized/sourceforge/tei-legacy-trackers-r4.jsonl`
  is read for records with `object_type` `ticket`, matched on `summary` and
  listed with tracker, number and status. The migration copied the ticket
  titles into GitHub issues that carry the label `sf-automigrated`. Matching
  titles and dates identify candidates for reconciliation. A migration relation
  requires an explicit upstream pointer or separately documented source review;
  until then it remains unknown. The records retain their upstream identities.
  When migration is established, admit the fuller manifestation and name the
  related record in the same row. The SourceForge status vocabulary, `closed-fixed`,
  `closed-accepted`, `closed-rejected`, `closed-wont-fix` and
  `open-accepted`, is the first outcome signal, because the GitHub copy of a
  migrated ticket carries `closed` and nothing more.
- TEI-L threads. The stream `corpus/normalized/mail/tei-l-psu.jsonl` is
  matched on `subject` and grouped by subject without reply prefixes; each
  group records its months and message count. A subject group is a reading lead.
  Thread identity requires the message and reply references.
  The stream covers the Penn State months only and carries no sender fields,
  so a thread hit stays a lead until the Brown months are fetched and the
  rights review of the thread has run.
- Literature seeds. The lock `sources/locks/literature.yaml` supplies the
  seed sets and the disposition of every record already discovered. The
  pinned bibliography `P5/Source/Guidelines/en/BIB-Bibliography.xml` is
  queried by the chapter prefix of each entry's `xml:id`, which tags the
  entry with the chapter that cites it, and by title terms. The Journal of
  the TEI and the Zotero seeds are not acquired and stay a recorded gap in
  every run until their census has run. A discovered record receives a
  disposition in the lock's vocabulary and enters the vault only through the
  literature protocol of [[knowledge/operations]].

#### 4. Counterevidence queries

For every problem claim the run declares, before the claim can support a
requirement, one query that would find P5 handling the case; such a query
and its hits are marked `C` in the table. Three kinds of source answer it:

- closed work items with the claim's terms whose outcome was a merged and
  released change, checked against the declaration in the atlas at the
  pinned commit;
- items labelled `Wontfix`, `closed-rejected` or `closed-wont-fix`, whose
  descriptions and complete discussion must be read to establish the outcome.
  A label alone does not establish rejection: the thread may report a duplicate,
  a move to another repository, a withdrawn proposal, a completed change or a
  decision to retain existing behaviour. Attribute a reported decision to its
  speaker and seek the decision record before treating it as Council policy;
- the remarks of the admitted specifications and the Guidelines sections the
  chapter cites.

A hit that contradicts the claim
yields a second assertion and a contested pair, and a query without a
finding is entered with its date under the open questions of the topic map,
as [[knowledge/verification]] requires. Closure is booked as closure only;
the step to a released effect is traced through the pinned declaration or
the release notes.

#### 5. Dispositions

Every hit receives exactly one disposition, `admit`, `defer` or `reject`,
with a reason from a fixed list. The rejection reasons are these:

- homonym, where the term names something else;
- outside the topic;
- duplicate manifestation;
- tooling or typography, which covers stylesheet defects, typos and
  translations;
- example repair without semantic content.

The deferral reasons are these:

- budget, for a relevant source that waits for the next run of the topic;
- another topic's run;
- prerequisite missing, which covers a raw body absent from the checkout, a
  pending rights review, a missing sampling protocol and an unacquired seed;
- lead, where the title suggests relevance and the body has not been
  checked.

Hits that share one disposition and one reason may
stand in one row by number. The selection is `bounded-complete` in the
vocabulary of [[knowledge/data]] when every declared query ran against the
named snapshot and every hit carries a disposition; the label says nothing
about the completeness of a family, which its manifests hold.

#### 6. Admission budget

The following budget governs scholarly topic runs, including their
distillation and source-support reviews. The full deterministic Guidelines
reference intake has the separate finite boundary in [[knowledge/data]] and
does not consume this budget or assign reviewed status. Sources already
admitted by that intake are reused in a topic run with their existing
representations and anchors. Every Guidelines chapter and specification
remains in scope for systematic source-specific distillation; the generated
[coverage](../corpus/projections/guidelines-4.12.0.md) identifies the actual
processing position. Source availability does not close a topic cycle.

A run admits at most twelve sources, among them at most two Guidelines
chapters and at most four threads. The entity run of 2026-09-06 admitted nine
sources, and its review cut 101 source pairs, 59 of them from the one
Guidelines chapter, each pair judged in a fresh context
(`workbench/reviews/2026-09-06-entities`). Reformulation rounds, assertion
pairs and the human sample scale with that count, and twelve sources with two
chapters keep a run near the size that stayed checkable. Sources beyond the
budget are deferred with the reason budget to a further run of the same
topic. A topic may have any number of runs, and a run is identified as
`<date>-<topic slug>-<n>` when its admission manifest is written.

#### 7. Order of steps

1. Ingest. An admission manifest `sources/manifests/<date>-<topic slug>-admission.yaml`
   names commit, blob, path, hash and rights of every admitted object.
   Document sources receive an immutable representation under the current
   converter version, threads a citation-only record in `references/` with
   their locators, while the raw snapshot stays local.
2. Distill. One source per agent in a fresh context with the canonical
   extraction prompt, followed by the fidelity check and, for threads, the
   quotation check against the raw snapshot.
3. Review the distillates in fresh contexts with a reviewer from a different
   model family than the producer or, where one family is available, with a
   different model of that family and the limitation recorded in the run's
   README.
4. Synthesize assertions through the topic map, one atomic assertion per
   group and a contested pair for each disagreement, and record the result
   of the counterevidence query before any assertion supports a requirement.
5. Review the assertion pairs as in step 3.
6. Narrow. Reformulate every failed pair to what its statement carries and
   review the changed pair again; earlier rounds stay in the run directory.
7. Write or extend the topic's chapter with grounded and posit footnotes,
   mirror the assertions and the posit count, and update the chapter
   register.
8. Draw the human sample after its strata and quota have been recorded in
   [[knowledge/journal]].

#### 8. The record a run leaves

`workbench/selections/` holds the dated snapshot and selection tables of a
run in one record, written once when the selection is made. The chapter
register row of the chapter the run serves names the run, the count of
admitted sources and the selection record that selected them, and the checkpoint row of
[[knowledge/state]] carries the executed state with its dates and the gaps
left under Open work. The admission manifest is the audit record of
ingestion. `workbench/reviews/<run-id>/` holds `pairs.jsonl`,
`verdicts.jsonl` and a README naming scope and model pairing. The topic map
carries the dated counterevidence entries, and durable decisions go to the
journal.

## Query

Die lokale Suche liefert vorhandene Artefakte und passende Passagen. Sie erzeugt keine Antworten und vergibt keinen Prüfstatus. Vor der Suche wird bestimmt, ob die Frage eine P5-Quelle, eine bereits geprüfte Aussage, einen offiziellen Diskussionsstand oder einen Projektvertrag betrifft.

```powershell
python -m tools.retrieval "att.canonical" --layer representation --limit 5 --json
python -m tools.retrieval "key ref precedence" --layer assertion --status validated --limit 5 --json
python -m tools.retrieval "revision" --layer knowledge --limit 5 --json
```

Exakte TEI-Kennungen und markierte Attributnamen begrenzen die Suche besser als allgemeine Wörter. Eine breite Suche kann anschließend mit Schicht, Status, Quellenautorität, Version und Thema eingeschränkt werden. Die Kriterien `authority` und `version` beschreiben die belegte Quellenherkunft des Ergebnisses; unbekannte Metadaten bleiben unbekannt.

Die lokale Suche gewichtet lexikalische Treffer und weist pro Ergebnis `matched_terms` und `missing_terms` aus. Teilergebnisse bleiben als solche sichtbar; sie beantworten keine fehlenden Suchbegriffe. Die Quellenautorität einer Familie kann verschiedene Textarten umfassen: Beispielsweise gehört ein P5-Testdokument zur Familie `primary-normative`, hat aber laut `admission_authority` die Rolle eines Beispiels. Für eine normative Aussage ist die konkrete Guidelines-Passage zu lesen. Die Websuche verlangt dagegen alle eingegebenen Wörter und öffnet die passende Passage oder das vollständige Artefakt.

1. Trefferpfad und gegebenenfalls Blockanker öffnen. Ein Ausschnitt genügt zur Orientierung; der unmittelbar verlinkte Kontext entscheidet über seine Verwendung.
2. Bei Assertions die Grounding-Kette zu Destillat und Quellpassage verfolgen. Bei einer `contested`-Aussage die bezeichnete Gegenposition ebenfalls lesen.
3. Prüfdatum und Quellenversion festhalten. Ein `validated`-Filter enthält genau diesen Status; er schließt `grounded`, `contested` und `verified` aus.
4. Die Autorität auf die Frage beziehen. Ein Releasebeleg, ein Diskussionsbeitrag und ein Projektvorschlag beantworten unterschiedliche Fragen. Ein Projektvertrag wird niemals als offizieller TEI-Befund zitiert.
5. Bei fehlendem Beleg die Suche in den benannten Quellen-Snapshots nach Select erweitern. Ein leerer Treffer erlaubt keine Aussage, dass P5 eine Fähigkeit nicht besitzt. Offene Sachfragen gehören in die entsprechende Themenkarte.

Die Suche verwendet lexikalische Treffer und explizite Metadaten. Sie garantiert weder semantische Vollständigkeit noch wissenschaftliche Eignung. Der Webbrowser bietet zusätzlich eine geordnete Trefferliste, einen Prüfstatusfilter und unveränderte Quellenanker. Die Projektionen und Suchergebnisse bleiben außerhalb von `grounding`.

## Check

Validation is defined here. Machine review, its independence, human
verification, the premise rule and the counterevidence search are defined in
[[knowledge/verification]], and the completion gate that runs all checks in
[[knowledge/testing]].

### Contract: validation

Validation checks formal conformance against [[knowledge/schema]]. It is
deterministic and runs on every change. A failing file cannot proceed to
another check. Validation alone does not promote status. Record
`checked.validation: <date>` on each file that passes.

Run `python tools/validate.py .` to check frontmatter, anchors, statement IDs,
quotation identity where source text is available, computation declarations,
topic-map reachability, reciprocal contested links, chapter mirrors and
footnote keywords, and status discipline. Data computations are rerun and
their results compared by default. `--no-computations` omits that step for a
faster, narrower check.

Use `python tools/validate.py . --chapter 40_output/<slug>` to check a chapter
and the assertions, distillates, and representations it grounds in. The scope
walk follows only immediate-layer anchors. Other branches and vault-wide
warnings are excluded, and the closing output names the excluded checks.
Any warning or error within chapter scope fails the run.

`tools/inventory.py` builds [[corpus/projections/source-inventory]], the
two lists of every topic map and the example list of every glossary entry from
the files themselves. Validation compares each of these regions against that
result and raises `E-GENERATED` for a region whose content differs and for one
a document does not carry yet. Write them with
`python tools/inventory.py . --write`; `--check` reports the same drift and
changes nothing. Everything outside the markers is hand-written and survives
every run. The regions navigate and never ground, so they stay out of a
`--chapter` run.

| Diagnostic | Condition |
|---|---|
| `E-ANCHOR` | An anchor or frontmatter target in `source`, `data`, `representation`, `superseded-by`, `contested-with`, `phenomena`, or `related` does not resolve |
| `E-LAYER` | An anchor skips its direct predecessor layer |
| `E-GROUNDING` | An artifact with a grounding obligation has empty grounding |
| `E-DUPLICATE` | A block or statement ID occurs more than once within a file |
| `E-STATUS` | A required check is missing or an entry in `checked` lacks a date |
| `E-LADDER` | An artifact's status exceeds that of an anchor it rests on |
| `W-PLACEHOLDER` | An unreplaced double-brace placeholder remains in the vault |
| `W-EMPTY` | No document exists in the production chain from `10_markdown` to `40_output` |
| `W-STALE` | `updated` is later than the most recent recorded check date. Artifacts without check dates do not trigger it |
| `W-DUPLICATE-GROUNDING` | Two assertions have equal grounding sets or one set contains the other |
| `W-ALIAS` | A chapter footnote alias differs from its assertion's H1 and may omit a qualifying clause |
| `E-FRONTMATTER` | Frontmatter is unreadable or not a map, carries an unknown type, misses a required field, holds an illegal value, gives a list-valued field another type, or leaves a declared metadata field out |
| `E-SOURCE` | A second representation or a second distillate names a source another one already holds |
| `E-STATEMENT` | A core statement has no statement ID, has no source anchor or more than one, or mints an ID outside the Core statements section |
| `E-QUOTE` | A publication distillate records no intake quotation check (`checked.quote`) |
| `E-COMPUTATION` | A data computation names other than one script, passes an argument, lies outside `tools/analysis/`, is missing, fails, or yields another result than the stated one |
| `E-TOPIC` | A `topics` value names no topic map of the controlled topic set |
| `E-PHENOMENON` | A `phenomena` value names a document that is no glossary entry |
| `E-GENERATED` | A generated region is missing or differs from what `tools/inventory.py` builds from the files |
| `E-ORPHAN` | An assertion is reachable from no topic map |
| `E-CONTESTED` | A contested assertion names no counterpart, or a contested relation is one-sided |
| `E-FOOTNOTE` | A chapter footnote is used without definition, defined without use, defined twice, or opens with neither `Grounded in` nor `Posit:` |
| `E-MIRROR` | A chapter's `assertions` mirror or `posits` count disagrees with its footnotes |
| `E-SCOPE` | `--chapter` names no chapter document |
| `W-NAME` | A file name is no ASCII-lowercase hyphen slug; `MOC-<Topic>.md` is the schema's exception |
| `W-UNANCHORED` | A chapter paragraph carries no footnote marker |
| `W-NO-OUTPUT` | The vault holds no chapter, so the footnote contract has no subject |

Every warning must be investigated. Warnings identify either a check with no
subject or a condition the schema does not classify as an error. They are
printed and counted. Vault-wide warnings preserve a successful exit code for
work in progress. Chapter warnings fail the run because it judges readiness
for acceptance.

### Status discipline

`grounded` → (validation and machine review passed) → `validated` →
(expert passed) → `verified`. Assertion building or review may set
`contested` when sources conflict. Only verification resolves it.
An artifact's status is the minimum of its anchors' states.
