---
title: Data
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-06"
related: [INDEX, project, specification, governance, operations, schema, state]
---

# Data

This document describes the material of the project. It defines the source
families and their hierarchy, the identity of records and citations, the
rights and redistribution rule, the update model, the boundary between the
acquisition corpus and the knowledge chain, the meaning of every completion
label and the admission rule for discussion threads. What has actually been
acquired is recorded in `sources/registry.yaml`, the locks under
`sources/locks/`, the run manifests under `sources/manifests/` and
[[knowledge/state]]. A registered or planned source is never an acquired
source.

## Meaning of all primary sources

There is no globally finite set of every TEI-related primary source. Private
mail, deleted records, closed project documentation, inaccessible chat
history and unknown local customizations cannot be exhaustively recovered.
The project therefore uses a bounded claim.

> All publicly observable primary-source objects exposed by the registered
> official interfaces and repositories during the declared census interval,
> plus every result admitted through a documented real-world sampling
> protocol, with inaccessible and historically lost material recorded as gaps.

Primary means that a source directly records a specification, artifact,
event, decision, implementation, report or encoding practice being studied.
Being primary makes a source neither normative nor reliable for every claim.

## Source hierarchy and authority

The hierarchy distinguishes authority from availability.

1. Primary normative. The tagged P5 release source and the published
   Guidelines.
2. Primary publication and process. Official releases, commits, issues, pull
   requests and Council records.
3. Secondary scholarly. Peer-reviewed literature, including the Journal of
   the Text Encoding Initiative.
4. Community and contextual. Discussion and implementation experience.

Source authority is specific to the kind of claim being made.

| Source family | Primary authority | Cannot establish alone |
|---|---|---|
| released Guidelines, ODD, schemas | normative state of a named release | motivation, user success, future policy |
| Git tree and generated artifacts | implementation at a named commit | normative publication unless released |
| issues and pull requests | proposals, reports, discussion, implementation trail | consensus or released effect |
| Council and Board records | documented governance discussion or decision | actual merge or released semantics |
| official P6 records | state of the official P6 process at a date | this vault's recommendation or a final standard |
| local ODDs and project studies | observed customization and practice in the declared sample | universal community need |
| scholarly literature | analysis, critique, comparison and reported practice | TEI normativity |
| deterministic corpus computation | aggregate result over the declared snapshot | meaning beyond its measured scope |

An issue proposal is evidence that a proposal or discussion occurred. A
Council minute is evidence of the recorded meeting state. A released ODD or
specification at the locked revision is the normative baseline. The
transitions from proposal to released effect and the trust rules for
acquired content are governed by [[knowledge/governance]].

## Source families

The registry `sources/registry.yaml` carries the operative record of every
family with its authority, trust, rights, update policy and completion
target. The tables below explain what each family contains and where its
boundary lies.

### Normative and publication sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| P5 4.12.0 release | ODD source, prose Guidelines, specifications, exemplars, schemas, release notes, license, published HTML and PDF, release artifacts | exact release tag and full commit | normative for the named release |
| P5 release history | every P5 version exposed by the official release page, Vault, GitHub releases and Zenodo | official indexes at census time | publication history |
| Earlier Guidelines | P1 to P4, DTDs, ODD where available, migration material and rendered editions | official TEI Archive index | historical normative and publication record for its period |
| Official customizations | TEI All, Lite, Tite, simplePrint, jTEI, Bare, Corpus, MS, Drama, Speech, ODD, SVG, MathML, XInclude and the other exemplars in the pinned release | pinned release tree and official customization index | normative or official exemplar within its declared scope |

The principal origins are the [TEIC/TEI repository](https://github.com/TEIC/TEI),
the [current P5 Guidelines](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/),
the [P5 release index](https://www.tei-c.org/guidelines/p5/) and the
[TEI Archive](https://www.tei-c.org/Vault/).

### Development and decision sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| TEIC/TEI Git history | commits, tags, branches, diffs, file history and release ancestry | complete observable Git object graph at pinned observations | implementation history |
| TEIC repository census | every public repository exposed by the official GitHub organization | paginated organization API at census time | discovery and publication-infrastructure record |
| TEIC public Git repositories | complete Git object graphs and pinned HEAD trees for every repository in that census | every repository the census observed at its census time | mixed development, implementation, event and infrastructure evidence, classified per repository |
| TEIC/TEI GitHub work items | issues, pull requests, comments, reviews, review comments, timelines, commits, changed files, labels, milestones, releases and relations | authenticated API pagination to exhaustion with start and end reconciliation | proposal, report, discussion and implementation trail |
| Legacy SourceForge | bug, feature-request and support trackers, file releases, CVS and SVN material where exposed, migration relations to GitHub | public SourceForge project interfaces | historical development record |
| Council minutes | agendas, minutes, attachments, reports, decisions and referenced working documents | every meeting linked from the official Council index through the census date | primary technical-governance record |
| Council working documents | repository documents and separately linked papers | complete public `TEIC/Documentation` Git tree plus official links | primary process record, incomplete as a minutes mirror |
| Board records | meeting minutes, agendas, AGM slides, procedural documents and published policy decisions | every object linked from the official Board page through the census date | primary strategic-governance record |
| Official P6 process | P6-specific Council records, accessible artifacts and official presentation repositories | official Council index plus registered public repositories | primary process and development record without the status of a release |

The official Council meeting index defines the observable minutes boundary.
`TEIC/Documentation` is registered separately as an incomplete
working-document source.

### Reference implementation and tooling sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| TEI Stylesheets | source, tests, releases, issues, pull requests and transformation profiles | public `TEIC/Stylesheets` repository and its work items | reference ecosystem implementation, outside the normative model |
| Roma | RomaJS and relevant predecessor repositories, source, configuration, tests, releases, issues and pull requests | registered TEIC repositories | observed customization-tool behavior |
| TEIGarage and converters | TEIGarage, EGE services, converters, validators and exposed API contracts | relevant public TEIC repositories | observed processing and conversion behavior |
| Website and infrastructure | TEI website source, publication configuration, redirects and policies needed to interpret official manifestations | public TEIC website and infrastructure repositories | publication and operational record |

Tool behavior can establish what an implementation does at a version. It
overrides neither the released Guidelines nor the behavior of other TEI
processors.

### Historical design sources

The historical TEI Archive contains the primary records needed to understand
why earlier modeling decisions exist. These are the Poughkeepsie Principles,
Advisory Board material, the documents of the Analysis and Interpretation,
Metalanguage and Syntax, Text Documentation, Text Representation, Steering,
Technical Review and editorial committees, working papers and proposals,
concluded workgroup records, earlier Guidelines, migration guidance and
unnumbered reports.

The Archive itself warns that its historical holdings were assembled from
multiple servers and personal collections and are incomplete. This family can
be observable-complete for the official Archive index while remaining
historically incomplete.

### Community and practice sources

| Family | Primary objects | Boundary | Authority |
|---|---|---|---|
| TEI-L | publicly archived messages and threads | three parts, the Penn State LISTSERV archive since the list moved there, Wayback Machine captures of the retired Brown University archive measured month by month, and an export requested from the TEI Consortium for every month neither holds | primary record of community questions and practice, without establishing consensus |
| SIGs and workgroups | charters, minutes, reports, proposals, schemas, repositories, wiki pages and list archives | official active and dormant SIG and concluded-workgroup indexes | primary community and process record |
| Annual meetings | programmes, AGM material, abstracts, slides, reports and published proceedings | official meeting indexes and archives | primary event and attributed proposal record |
| Registered projects | project documentation, schemas, examples and processing code | explicit sample selected under a published protocol | observed practice within the sample |
| Real-world ODDs | customization source, generated schemas, documentation, tests, release history and compatibility declarations | reproducible repository and registry census plus purposive domain sample | observed customization practice within the sample |
| TEI-L archive (`tei-l-archive`) | month indexes and message pages of the Penn State archive, Wayback captures of the retired Brown month indexes and their messages, and a requested consortium export | three declared parts, each with its own month interval and its own completion state | primary record of community questions and practice, without establishing consensus |

TEI-L and SIG material is user-generated content. Rights, privacy and
redistribution are reviewed per collection under the rule below.

The TEI-L archive is registered as its own source because no single interface
holds the history of the list. The Penn State LISTSERV serves the months since
the list moved there. The Internet Archive is measured month by month for
captures of the retired Brown University month indexes, and a captured month is
fetched from its capture. Months that neither part covers are requested from the
TEI Consortium as an export, an operator action with no retrieval interface.
Each part declares its own month interval, so a coverage claim holds for the
months a run named and for no wider period. Threads from this archive enter the
knowledge chain as citation-only publication sources under the rule below, with
message bodies and sender identity kept in the local raw store.

### Secondary and interpretive sources

Journal articles, books, dissertations, tutorials, retrospective essays and
research reports are essential to the project and are normally secondary
sources. They are collected through the bounded literature protocol in
[[knowledge/operations]]. An article may contain primary empirical material,
and its role is declared for the specific claim rather than inferred from
the publication venue.

### Acquisition tiers

The census uses three priorities without changing source authority.

1. Core. The pinned P5 release and Git history, TEIC/TEI work items, Council
   and Board records, official P6 records and the P5 release history.
2. Interpretive infrastructure. The TEI Archive, SourceForge, Stylesheets,
   Roma and TEIGarage, website sources and official customizations.
3. Observed practice. TEI-L, SIG and workgroup outputs, annual meetings and
   a rights-aware sample of projects and ODD customizations.

Core sources are required for any architecture-level conclusion. Later tiers
are required before claims about historical motivation, processing cost,
community need or real-world migration can be generalized.

## Identity of records and citations

Records use upstream-stable identifiers where available.

```text
tei:p5:4.12.0:element:persName
git:TEIC/TEI@<full-sha>
github:TEIC/TEI:issue:<number>
github:TEIC/TEI:pr:<number>
github-node:<node-id>
tei-council:<meeting-date>:<source-id>
doi:<doi>
```

Titles and URLs may change and are therefore labels or locators. Exact source
locators use release plus TEI `xml:id` or XPath, full Git SHA plus path,
GitHub node or event ID, meeting date plus heading, or DOI plus section or
page. Stable upstream IDs define identity, and raw bytes are addressed by
SHA-256.

## Version semantics

The normative baseline is TEI P5 4.12.0. Its published abbreviated revision
is resolved to the full commit
`113e933e21f016e2655518321e9d10214b8d9fcb` and the annotated tag object in
`sources/locks/tei-p5-4.12.0.yaml`, and every evidence identity names that
full commit. `current` is a role and never an evidence identity.

Development snapshots are separately locked to the observed full commit and
remain outside the normative baseline. Historical releases are independent
immutable objects. Comparisons always name both endpoints, and a diff against
a moving branch name is inadmissible as evidence. The four states that the
project keeps distinct are defined in [[knowledge/project]].

## Rights and redistribution

Public visibility of a source grants no permission to redistribute its full
text. This rule has its home here, and every other document links to it.

TEI source and Guidelines are registered under the upstream dual license,
with per-file review of third-party examples and assets retained. GitHub
discussion text, Council pages, attachments, mail and literature carry a
conservative per-item status. Journal of the TEI licensing is read from each
article rather than inferred from the journal as a whole.

The registry separates three fields for every source. `rights_status`
records whether storage and redistribution have been established,
`content_authority` records the epistemic role of the source, and
`instruction_trust` is always `none` for acquired content.

The consequences for storage are these.

- Raw content defaults to local-only storage.
- The committed repository may contain source metadata, hashes, locators,
  checked short quotations and project-authored summaries.
- Full text is committed only after the applicable license or permission has
  been verified and recorded for the item.
- GitHub comments, mailing-list posts, unlicensed working documents and
  uncertain historical material default to local raw storage plus public
  metadata, locator and checked short quotation.
- Rights uncertainty sets a source to metadata and link only until it has
  been independently reviewed.

Normal Git stores code, schemas, registries, locks, append-only run
manifests, checksums, small rights-cleared fixtures, reviewed Markdown
representations, distillates, assertions, output and reproducible projections
within declared size limits. Git mirrors, raw API dumps, third-party PDFs,
mailing-list archives, large release bundles, unreviewed discussion full
text, tokens and caches stay ignored and local. A larger accepted artifact
requires a checksummed external store, release asset or LFS policy plus a
reproducible materialization command. Nobody uses `git add -f` on ignored raw
data. When a reviewed original is approved for versioning, the integrator
adds a narrow per-file exception to `.gitignore` so that the policy change is
visible in review.

The licenses of the project's own text and code and the publication boundary
are governed by [[knowledge/governance]].

## Update model

- Immutable releases are fetched once, hashed and periodically audited.
- The upstream Git repository is fetched with branches and tags, and every
  observation records the full SHA and ref map.
- GitHub work items use an initial full census, incremental changed-item runs
  with overlap and periodic full reconciliation.
- Council acquisition reconciles the official index with its source
  repository.
- Literature runs are bounded searches with explicit queries and a
  disposition for every result.

A changed body is a new observed version. Local history is never rewritten to
match the newest remote representation.

## Acquisition and knowledge boundary

Large collections follow the acquisition chain.

```text
sources -> corpus/raw -> corpus/normalized -> corpus/projections
```

`corpus/raw/` materializes byte-preserving responses, archives or Git objects
and stays local and ignored. `corpus/normalized/` holds loss-minimizing
machine records that preserve source identifiers, order, timestamps,
relationships and a pointer to the raw hash. `corpus/projections/` holds
deterministic reading and retrieval views. Every transformation is tied to an
append-only run manifest under `sources/manifests/` and a source hash. The
manifest is the audit record.

This corpus supports inventory, discovery, counting, graph construction and
candidate selection. Persistent claims require admission to the knowledge
chain.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

A source package enters the chain only after identity and checksum
verification, rights classification, source-type assignment (`document`,
`publication` or `data`), placement of the admitted original under
`00_sources/` and creation of the immutable `10_markdown` representation
where the source type has one. No record in `corpus/`, no registry entry, no
lock and no projection is a grounding target, and no shortcut leads from
`corpus/` to a distillate, assertion or chapter. Admission creates neither a
research finding nor human verification. The procedure is in
[[knowledge/operations]].

## Completion vocabulary

The corpus never uses complete to mean everything that ever existed. It means
that a declared, testable boundary was exhausted at a stated observation
time. The strongest permitted corpus-wide statement is this.

> Complete for the objects publicly observable through the registered sources
> and interfaces at the snapshot time, subject to the recorded exclusions and
> failures.

Deleted, private, embargoed, access-controlled or historically overwritten
content cannot be presumed recoverable. An unavailable object remains a gap in
the manifest.

### Completion states

Every ingestion run and source family uses one of these states.

- `planned`: scope declared, no retrieval attempted;
- `partial`: retrieval began but at least one declared boundary or check is
  unfinished;
- `observable-complete`: every currently observable object inside the boundary
  was enumerated, retrieved or explicitly marked unavailable, and reconciled;
- `bounded-complete`: a finite search or bibliography protocol was exhausted;
- `not-completable`: the source does not expose a finite or auditable boundary.

No planned count is a coverage result. Counts are written only by an
ingestion run and must cite its manifest. A collector derives the status of
its run from the recorded gaps through one shared rule, so that a run with an
unresolved gap can never report `observable-complete`. Completing a narrower
interface or sample does not change the completion status of the whole
family.

### Family-specific definitions

**TEI P5 4.12.0 normative baseline.** `observable-complete` requires all of
the following.

1. The published revision has been resolved to one full Git object ID and
   verified against the declared release and tag.
2. Every tracked file at that commit has an inventory entry and content hash.
3. The Guidelines source, component specifications, release notes, generated
   schemas and published documentation artifacts declared by the lock are
   represented or explicitly marked unavailable.
4. Release, Vault and repository manifestations are related without treating
   byte-different formats as duplicates.
5. Every admitted object carries source, version, trust and rights metadata.

**GitHub issues and pull requests.** For repository `TEIC/TEI` at time `T`,
`observable-complete` means all of the following.

1. The issue endpoint was paginated to exhaustion with state `all`.
2. Issue-shaped pull requests were identified and counted once.
3. Every observable issue has its detail record, comments and timeline
   events.
4. Every observable pull request has its detail record, issue comments,
   reviews, review comments, commits and declared relation metadata.
5. Labels, milestones, releases, redirects and transfers, pagination and API
   errors were recorded.
6. A second enumeration reconciled identifiers and API-reported child counts.
7. Missing, minimized, deleted or inaccessible objects are recorded as gaps. The work-item family is acquired in two stages, a REST snapshot of items and their children and a GraphQL stage for review threads and relationship fields, and `observable-complete` for the family requires both run manifests.

The API exposes current representations rather than every historical edit.
Periodic snapshots create a local observation history from the first
successful run onward.

**Council minutes.** For a declared date interval, `observable-complete`
requires that every meeting link reachable from the official Council meeting
index was enumerated, that the official page and every linked agenda,
attachment, draft or report were modeled as separate manifestations of the
same meeting event, that attachments and referenced working papers were
inventoried, that unreachable or rights-restricted items were retained as
explicit gaps, and that the discovered meeting-date set was reconciled
against the index at the end of the run.

**P5 releases.** At time `T`, `observable-complete` requires every P5 release
listed by the official release index to have a version record, publication
date when supplied, release, tag and revision identifiers when supplied,
release notes, artifact inventory, hashes for retrieved artifacts and
explicit missing-artifact status. The alias `current` is never used as an
immutable identifier.

**Public TEIC Git repositories.** `observable-complete` requires an
organization API census paginated to exhaustion, a full mirror of every
repository in that census, a resolved HEAD commit and tree inventory for each
repository, and an explicit failure for any repository that cannot be
mirrored. Repository authority is classified separately, and completeness
makes no repository normative.

**Historical and governance web records.** For the Council, Board and TEI
Archive, `observable-complete` applies only to the registered official
indexes. Every in-bound page and attachment must be retrieved or named as a
gap, and external targets must be inventoried. The Archive's own warning that
historical holdings are incomplete remains a permanent limitation even after
its present public index has been exhausted.

**Legacy SourceForge records.** `observable-complete` requires every tracker
exposed by the project metadata to be enumerated through its API and
reconciled against the tracker-reported counts, every ticket and discussion
page to be fetched, file and version-control interfaces to be inventoried,
and migration relations to be preserved when supplied. Rate-limit stops and
unavailable legacy tools remain explicit gaps.

**Community records and observed customizations.** These families can only
be `bounded-complete`. Each run must name the official indexes, external
archives, time interval, rights constraints and sampling protocol. A complete
official link census makes neither an open-ended mailing list nor the
universe of real-world ODDs complete.

**Literature.** All TEI literature has no finite boundary and is
`not-completable`. A literature snapshot may be `bounded-complete` only when
it names its seed bibliographies, journals, indexes and exact queries, its
language, date, document-type and relevance boundaries, the observation date
and pagination or result limits, and a disposition for every discovered
record, which is one of `included`, `duplicate`, `excluded-with-reason`,
`unavailable` or `pending-review`. The first bounded seeds are the
bibliography of the locked Guidelines release and the Journal of the Text
Encoding Initiative. Neither seed is treated as the whole field.

### Reconciliation invariants

- Stable upstream IDs define identity. Titles and URLs are labels.
- Raw bytes are addressed by SHA-256.
- A changed source body creates a new observed version and never overwrites
  history.
- Exact hashes may deduplicate byte-identical manifestations. Fuzzy
  similarity may propose a relation and never merges records automatically.
- SourceForge-to-GitHub migrations, web-to-repository minutes and XML, HTML
  and PDF renditions remain distinct records connected by typed relations.
- Every projection can be traced to normalized record hashes, raw hashes, the
  transformation version and the lock used for the run.

## Threads as citation-only sources

GitHub issue threads, pull-request threads and mailing-list threads are
admitted as citation-only publication sources. The raw thread stays in the
private raw store. The reference record in `references/` carries identifier,
URL, dates and roles. The public distillate carries the structured account of
the thread with short quotations checked against the raw snapshot, the same
path the research-wave-one literature already uses. Personal names of third
parties appear in that research data only, and documentation about the work
names roles and institutions.

A generated metadata index of all threads with title, state, labels, dates
and link is a navigation projection. It supports selection and never appears
in `grounding`.
