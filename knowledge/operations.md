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
updated: "2026-09-07"
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

Without `uv`:

```powershell
python -m pip install pyyaml pytest ruff
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

After a representation change, regenerate the source inventory in
[[knowledge/state]] from the files and revalidate:

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

## Distill

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

## Query

Enter through topic maps and follow assertions to distillate statements.
Consult source passages where exact wording matters. Cite assertions by
wikilink. Record unanswered questions in the topic map.

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

`tools/inventory.py` builds the source inventory in [[knowledge/state]], the
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
