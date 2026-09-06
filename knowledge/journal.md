---
title: Journal
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-06"
related: [INDEX, specification, plan, state]
---

# Journal

Chronological decision history of the vault, append-only, newest entry last. Content documents carry only current state; the reasoning that led there lives here. An entry records a decision, a rejected alternative with the reason, or a calibration result of a check mechanism.

## Entry format

```markdown
## YYYY-MM-DD — one-line subject

<What was decided or found, why, and what it replaces. Link the affected
documents. Two to ten sentences.>
```

## 2026-09-04 — Vault instantiated

The Grounded Vault template was instantiated as the TEI P6 Research Vault in the provisional `tei-p6` repository. The vault will produce a provenance-complete analysis of TEI P5 and a grounded design for a possible next TEI generation as a German scholarly synthesis and design specification. Its controlled topic set consists of twelve topic maps spanning P5 architecture, history, issues, processing, and P6 design, and all three source types are active. Findings, interpretations, and proposals must remain distinct, while canonical English TEI identifiers remain unchanged. Human verification is reserved for the project owner or an explicitly designated TEI domain expert, but no verifier is assigned yet. Adversarial review by a separate agent or model context is recorded only as machine review and never substitutes for human verification. The complete parameters are recorded in [[knowledge/specification]].

## 2026-09-04 — Acquisition and official P6 scopes separated

The collector build and corpus acquisition will follow the staged, exclusive-ownership work packages in `docs/multi-agent-acquisition-runbook.md`. Official TEI Council work on P6 is now an explicit primary-process source family and must remain distinct from this independent vault's interpretations and proposals. The official Council meeting index, not `TEIC/Documentation`, defines the observable minutes boundary; that repository is registered separately as an incomplete working-document source. The P5 4.12.0 published revision has been resolved to full commit `113e933e21f016e2655518321e9d10214b8d9fcb`, while materialization and tree inventory remain pending. Large raw mirrors, API dumps, unlicensed discussion text, and third-party publications remain local or metadata-only until storage and redistribution rights are established.

## 2026-09-04 — Promptotyping project contract completed

The six documents in `knowledge/` are treated together as the executable Promptotyping document of this project rather than as generic template documentation. The project specification now states the problem, seven research questions, source-authority model, deliverables, comparative P6 evaluation dimensions, design constraints, success criteria, and decision gates. The project will not assume that P5 requires a full rewrite: repair, compatible evolution, redesign, and non-change remain alternatives until grounded evidence and migration prototypes distinguish them. `README.md`, `HOME.md`, `AGENTS.md`, and `CLAUDE.md` now route human and agent readers into the same contract and explicitly distinguish planned sources from acquired data.

## 2026-09-04 — P6 design dossier established

The repository now separates stable project control knowledge from provisional P6 design knowledge. `knowledge/` remains the six-document Promptotyping contract, while `docs/p6/` holds a navigable design dossier covering principles, the candidate core model, serialization and conformance, examples and migration, and comparative evaluation. These documents are not a new evidence layer and may not be cited as proof of P5 behavior or official TEI policy. They record questions, hypotheses, evaluation contracts, and intended experiments; factual claims must still enter through the canonical Grounded Vault chain, and accepted recommendations must be published in `40_output/` with their supporting assertions. Executable metamodels, bindings, and fixtures will receive dedicated artifact contracts before implementation rather than being mixed with the design notes.

## 2026-09-04 — Public documentation language and plan boundary clarified

The public project entry points and architecture documents use English so that the repository is accessible to the international TEI community; a later scholarly output may adopt a separately declared language. The oversized implementation plan was replaced by a stable phase and gate map. Detailed acquisition procedures remain in the acquisition runbook, project requirements remain in the specification, and all volatile progress remains in `knowledge/state.md` and run manifests. This prevents the README and plan from duplicating status or operational contracts that change on different schedules.

## 2026-09-04 — Primary-source universe and acquisition artifacts defined

“All primary sources” now means every publicly observable object within the
registered official interfaces at a declared observation time, plus objects
admitted through explicit sampling protocols; inaccessible, deleted, private,
and historically lost material remains a named gap. Normative publications,
governance decisions, development discussions, implementations, historical
records, and observed practice are separate authority classes rather than one
undifferentiated corpus. Content-addressed raw responses and Git mirrors remain
local, while repository-safe normalized inventories and append-only run
manifests provide identity, counts, hashes, coverage, and failure evidence.
Collectors for Git, GitHub organization and work-item APIs, bounded websites,
SourceForge trackers, and release assets are therefore accepted as upstream
corpus artifacts; none bypasses the canonical Grounded Vault evidence chain.

## 2026-09-05 — Primary-data overview established as a generated projection

The first research frontend is a compact static overview generated at
`docs/corpus.html` from `sources/registry.yaml`, the source locks, and only the
run manifests referenced by those locks. Its unit is the registered source
family, not an individual API object, Git blob, ZIP member, or web response;
secondary scholarly literature remains separately identified. The page exposes
family status, bounded completion target, selected non-additive counts, rights,
gaps, upstream interfaces, control records, and normalized data products
without reading or publishing raw source bodies. It is a navigation projection,
cannot appear in grounding, and creates no new evidence type, status, or anchor
form. `docs/corpus.html` is generated and must not be edited by hand.

## 2026-09-05 — Research frontend adopted as a public P6 support workbench

The generated materials overview is the first surface of a gradually expanding
research workbench for evidence-based TEI P6 development. It will begin with a
plain inventory of what the vault has actually acquired and may later add
evidence tracing, comparison, proposal evaluation, and migration experiments
only when their canonical inputs are ready. The interface remains independent
and unofficial, does not create evidence, and must preserve the distinction
between official TEI P6 records and this project's analyses or proposals.
GitHub Pages is the intended public host; deployment automation may be prepared
before a remote exists, but publication remains blocked until repository owner
and visibility are settled.

## 2026-09-05 — Materials view aligned with the acquisition hierarchy

The public working view now presents one sortable row per registered source
family and lists each manifest-declared data object as a concrete subcollection
beneath that source. Source titles and short material descriptions are primary;
internal IDs, control vocabulary, rights metadata, and manifest names are kept
under technical details. Full-text search, acquisition-status filtering,
material-type filtering, and column sorting replace explanatory prose and
aggregate number displays. Methodological qualifications remain in the project
documentation or concise status help, while open gaps appear as short work
items linked to their complete control records.

## 2026-09-05 — Interface design split into a seventh control document

The research workbench now has a distinct audience, update rhythm, and set of
invariants that no longer fit cleanly inside the research specification,
evidence schema, or an implementation journal. `knowledge/design.md` therefore
becomes the seventh Promptotyping control document. It records the stable
information architecture, content placement, interaction, accessibility,
provenance, generation, and publication contract for the public research
workbench.

This document is control meta-knowledge, not a source, representation,
distillate, assertion, or output layer. It cannot ground research claims, create
evidence statuses, or bypass the canonical
`00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output`
chain. Volatile implementation state remains in `knowledge/state.md`. The
working surface prioritizes materials and research tasks; About carries purpose,
method, completion semantics, and the independent-versus-official boundary; raw
control records remain secondary technical detail.

## 2026-09-05 — Project working language unified as English

English is now the sole working language for the control documents in
`knowledge/`, the public research workbench, and the intended scholarly
synthesis and design specification. This supersedes the earlier allowance for a
German final output and the initial German materials-interface labels. Canonical
TEI identifiers remain unchanged, while user-facing titles, descriptions,
statuses, help text, navigation, and planned output names are all English.

## 2026-09-05 — Public repository established for the research vault

The canonical public repository is `chpollin/tei-p6-research`. The name keeps
the project visibly independent and broad enough to contain acquisition,
grounded knowledge, P6 design evaluation, and the research workbench without
presenting itself as the official TEI P6 repository. GitHub Pages publishes the
generated static workbench from this repository through the pinned workflow.

## 2026-09-05 — Public name and documentation history policy settled

The public project name is **TEI P6 Research**. “Grounded Vault” describes the
evidence system used by the project, not the public project name. Repository
entry points retain separate responsibilities and route into the canonical
`knowledge/` contract instead of restating it as parallel specifications.

Git history records file-level change, `knowledge/state.md` records present
reality, and this journal records only durable decisions and their rationale.
A release-oriented changelog is intentionally deferred until the project
publishes named versions; maintaining one before then would duplicate Git and
encourage status facts to drift outside `knowledge/state.md`.

## 2026-09-05 — Static workbench source architecture modularized

The public workbench remains framework-free and produces deterministic static
HTML for GitHub Pages. Its maintained implementation is divided into data and
view-model construction, rendering, CSS, and JavaScript. Page-specific
renderers preserve the distinct Materials and About tasks; infrastructure is
shared only where their contracts coincide. CSS and JavaScript source modules
are embedded during generation, so complete generated HTML remains the only
published artifact.

This separation allows the workbench to grow without turning its builder into
one monolithic mixture of research data interpretation, markup, styling, and
interaction code. It changes implementation organization only: the workbench
remains a projection, creates no evidence layer, and publishes no raw source
bodies.

## 2026-09-05 — Bounded text identity and annotation pilot

The first executable model experiment concerns text, text versions, regions,
and annotations. Its purpose is to test the research-to-design workflow and
explicit identity assumptions, not to establish a universal ontology or select
the final P6 architecture. The user authorized this pilot and requested a
reviewable acceptance procedure with formal validation.

`docs/p6/text-identity-pilot.md` owns the experiment contract and human review
procedure. `experiments/text_identity/` holds hand-authored synthetic fixtures,
an experiment specification, and a deterministically generated JSON report;
`tools/pilots/text_identity.py` implements the bounded semantics and runner;
`tests/pilots/` contains positive, negative, and adversarial checks. Experiment
format version 1 is local to this pilot, not a new Grounded Vault artifact type
or status. Experiment results and reports are not grounding targets. Any
persistent empirical assertion about them must first enter the canonical chain
as a versioned data source; the pilot chapter may instead present the proposed
experiment and its interpretation explicitly as posits.

Selected complete P5 specification files are admitted from the already acquired
4.12.0 Git component at its locked commit, with per-file hashes and upstream
licensing preserved. The partial family-level HTML boundary does not prevent
admission of those reconciled Git blobs and is not upgraded by this pilot.
Representations preserve the complete XML as a fenced source block and expose
verbatim English descriptions as mechanically checked reading blocks. Original
XML remains ignored and reproducibly materializable. Independent source-support
review uses the existing `tools/review.py` pairs and verdict vocabulary; audit
files under `experiments/text_identity/review/` are review records, never evidence.

All candidate definitions are project hypotheses. Both compared selectors bind
to an explicit immutable text version. Reanchoring creates a proposal for human
confirmation and cannot silently change an existing annotation. Human acceptance
of the experiment is separate from expert verification of grounding relations;
no machine process assigns `verified`.

The acceptance runner `tools/check_text_identity_pilot.py` checks the actual
chapter dependency closure against the declared pilot review scope and ties
each independent verdict to its exact prompt hash. Pilot source-review prompts
extend the existing pair cutter's source location with mechanically recovered
XML ancestor labels and the integrity-checked source title and locator. The
first review exposed that bare English descriptions alone omitted the release
and attribute context necessary for these claims; its nonpassing records are
retained. Context completion does not change immutable representations or
introduce the producer's reasoning into review.

## 2026-09-05 — Critical review clarifies the route from evidence to a text model

The user requested a constructive GPT-6 review of the project texts. Three
independent reading packages covered the model dossier, the pilot argument,
and the research programme. Their editorial judgments are not source-support
verdicts and do not replace passage-level review or human verification.

The research target is an explicitly scoped, conceptually coherent and usable
abstract text model for a possible P6. P5 supplies the normative baseline and
migration obligations; independent theoretical and practice sources must also
challenge the model's adequacy. Narrow claims need complete coverage of their
own source dependencies; generalized architectural claims require the full
declared P5 model inventory. This clarifies the existing scoped pilot policy.

The pilot compares selectors within one assumed object model, not complete
architectures. Its region record, selector and resolved interval are now
distinguished without changing the executable format. Additional synthetic
cases expose successful literal matching with a changed interpretive context;
the semantic judgment remains a declared human question.

Candidate design prose distinguishes model preservation, task-specific
equivalence and byte preservation. Proposed migration reporting uses separate
axes for coverage, preservation, lexical changes, dependencies and reversibility.
These revise future experiment contracts, not canonical evidence types or
statuses. No binding or migration implementation is implied. Source
representations and reviewed source claims remain unchanged; recommendations
remain posits even if an official body later adopts them.

## 2026-09-05 — First research wave and proposal integration

The user authorized a first parallel wave of P5 reconstruction, discussion
analysis, and literature reading, together with the outline of an independent
Proposal for TEI P6. The eventual coverage ambition includes every relevant
distinction and practice that the declared P5, issue, and literature boundaries
can substantiate. Individual waves remain bounded; they do not narrow the
long-term ambition or imply global completeness.

The first extractor produces a provisional navigation projection of the
top-level XML specifications in the locked P5 release. Its contract records
source commit, path, Git blob, SHA-256, and XML locators; direct declarations
and references are distinguished from inherited or compiled semantics. The
versioned JSON output under `corpus/projections/` is reproducible from those
inputs and is never a grounding target. This is a specialization of the existing
projection layer, not a new evidence type. Its rules and exclusions are recorded
in `docs/p6/research-wave-1.md` before persistent generation.

The proposal outline remains a design-dossier document. It maps questions and
acceptance obligations to the existing output chapters; it does not serve as
evidence or claim that the final proposal is already supported. Source reading,
requirement formation, model choice, and technical/practical evaluation remain
separate steps. Shared control files and integration are owned by the root agent.

For this small curated wave, citation-only sources use the existing publication
type and a local CSL JSON bibliography batch transcribed from the consulted
primary metadata. This instantiates import without an external reference-manager
export; it adds no source type or grounding layer. Exact response snapshots,
hashes, extraction rules, and short quotations are recorded at intake. W3C is
cited conservatively under its document-use notice; unlicensed discussion and
scholarly full text remain in ignored raw storage. Quotation fidelity is checked
locally before its date is recorded. Clean checkouts without those raw snapshots
retain the intake record but cannot claim to have repeated that check.

The first fresh-context support review rejected the Renear/Wickett assertion
heading because it widened a distinction about modifying an entity into one
about identity. The heading was narrowed to the supported wording. The
nonpassing audit remains alongside the replacement review; agreement of the
producer with a source is not a substitute for this independent check.

## 2026-09-05 — Abstract Text Model 0.1 executable research contract

The user requested a complete first working model. Version 0.1 is a bounded,
independent modeling hypothesis with precise definitions, a reference JSON
encoding, pure validation and comparison operations, adversarial examples, and
a reproducible report. Its experimental artifacts live in
`experiments/abstract_text_v01/`, implementation in `tools/models/`, and focused
tests in `tests/models/`. The normative research definition is
`docs/p6/abstract-text-model-v0.1.md`; the machine field/rule contract is
`experiments/abstract_text_v01/spec.json`. They must agree. Case expectations
are authored independently of the resolver. Generated reports fingerprint all
inputs and never become grounding without source admission.

This specializes the existing experiment plane; no Vault source type, anchor,
or research status is added. Model object IDs and diagnostics belong only to
the experimental format. The old text-identity pilot, immutable sources, and
reviewed source assertions remain intact. The new design argument belongs in
the ordinary P6 Design output chapter with explicit posits.

The candidate separates versioned character content, attributed continuity,
target specifications and resolved targets, attributed structural readings,
annotations, and other typed relations. Intentional plural targets differ from
unresolved choice; a discontinuous aggregate differs from several independent
targets. A closed package uses finite Unicode strings; structural-reading nodes
use contiguous resolved intervals in 0.1. Other textual media, full P5 migration,
domain customization algebra, and persistent storage are excluded from this
release, without narrowing the programme's eventual coverage ambition.

Version 0.1 commits to an inspectable candidate for testing, not a preferred
final P6 architecture. The documentation compares a primary-tree-plus-stand-off
alternative on the same observations, without assuming that overlap defeats
all tree-based designs. Human acceptance of definitions and practical adequacy
remains separate from deterministic conformance.

Independent ontology review clarified that continuity membership is positive,
not exclusionary; shared version IDs require a caller-declared scope for
revision comparison. Adjacent range components retain their segmentation but
count as contiguous for reading containment. Reanchoring remains explicitly
single-segment for ranges. These are definitions of this experiment, not claims
that the selected distinctions exhaust textual identity or structure.

The implementation and fixture packages were authored by separate GPT-6 agents;
fixture expectations were written without consulting the implementation. Their
first integration exposed one diagnostic disagreement: valid coordinates in
overlapping aggregate components should yield `E_SELECTOR`, while individually
invalid coordinates yield `E_BOUNDS`. The implementation was aligned to this
distinction, preserving the independently authored expected outcome. A separate
read-only code review challenged malformed inputs and ancestry traversal.
These machine reviews test a project contract; they do not promote model
posits to source assertions or replace human acceptance.

## 2026-09-05 — Editorial provenance and real-case comparison

The owner requested implementation of the proposal review's three priorities:
clarify version identity, examine real editorial cases comparatively, and
rewrite the proposal around a continuous example. The v0.1 core remains a
bounded candidate. Its technical construction dependencies must be distinguished
from revisable scholarly hypotheses about historical derivation. Such hypotheses
are attributed relations, not changes to the character version they describe.
A small optional editorial profile will constrain the existing relation records
and demonstrate correction without changing version or selection identity.
This introduces no new Vault source type, status, anchor, or evidence layer.

The case study uses a purposive, finite discovery of at most four openly
accessible edition repositories and three selected cases, preferably within one
edition to make the intake boundary manageable. Inclusion requires real
editorial XML, an exact source snapshot, contextual identification, and a
recorded rights disposition; tutorial examples cannot substitute for practice.
The target tasks concern mixed content and hierarchy, discontinuous or competing
structures, and an adverse case involving information outside the candidate's
scope. This sample cannot establish community-wide need or usability.

Discovery handoffs are navigation aids. Exact sources and rights records enter
the acquisition controls and canonical admission chain before output makes
source-derived claims. Project-authored preservation expectations are frozen
before mapping. At least one adverse case is held back from mapper development
and evaluated after its rules are defined. Domain expert review remains a
separate, uncompleted task, never simulated by an agent verdict.

The experiment plane is specialized at `experiments/editorial_cases/`: a
hand-authored protocol and case expectations, selected source locators and
hashes, reference mappings, and generated observation/comparison reports.
`tools/models/editorial_profile.py` and `tools/tei/editorial_cases.py` own
executable processing; focused tests live beside their existing model and TEI
test families. `docs/p6/editorial-case-study.md` explains the method and choices;
`40_output/12-p6-design.md` remains the grounded synthesis with explicit posits.
No report or experiment file may be cited as grounding without its own source
admission. A comparison reports the exact preserved observations and declared
losses for both the range/forest candidate and a primary-tree-plus-stand-off
representation. It does not assume either architecture wins.

The owner explicitly requested the full proposal on the frontend home page and
a stronger explanatory interface. This supersedes the original inventory-only
landing-page choice. The new generated home combines the canonical proposal,
inspectable example views, assertion/posit distinctions, and evidence navigation;
the existing inventory remains a separate Materials page. No client framework,
backend, evidence layer, or duplicated proposal text is introduced. Small
licensed excerpts keep their own attribution and license. The integrator owns
navigation, Pages routing, shared contracts, source integration, and publication
configuration; the frontend worker owns only its new generator, view, assets,
and focused tests. Local completion does not imply a committed or deployed site.

## 2026-09-05 — Technical proposal and comparative examples

The owner rejected the promotional home treatment and requested a technical
publication: canonical proposal first, right-hand example branches, P5 variants,
candidate bindings, formal descriptions and relationship diagrams. All P5
modules provide the coverage inventory; modules, document types, media and
phenomena remain distinct navigation axes. Coverage is a research obligation,
not an implemented-domain claim. A generated comparison view outside the Vault
chain assembles existing cases, source pointers and runtime checks. Its bindings
have explicit contracts and preservation tests; unavailable bindings and failed
mappings remain visible. The core model and frozen editorial holdout are not
silently expanded to improve the display. Publishing to the existing GitHub
Pages site was requested by the owner and remains the delivery target.

## 2026-09-05 — Shared workbench and concise prose

The owner requested one layout across all public pages and rejected decorative
horizontal rules. Navigation, footer, typography and controls now have one
maintained source. Page styles describe only their content. Local and published
routes are identical. The old home path remains a generated compatibility alias.

The Model reference derives fields and constraints from the existing model
contract. The Knowledge browser follows immediate-layer links and backreferences
through actual Vault artifacts. Both are navigation projections outside the
evidence chain. The Materials page distinguishes source-family holdings from
individual raw objects, and the proposal links its grounded premises to the
Knowledge browser.

Editorial revision removes repeated introductions and consolidates overlapping
document roles. Running prose avoids colons and semicolons. Lists serve
navigation, alternatives and procedures. Tables express comparable fields,
constraints and results. Code, identifiers, quotations, source records and
required anchor notation preserve their exact syntax. Historical journal entries
remain unchanged so that earlier decisions can still be reconstructed.

## 2026-09-06 — Review and repair of the tools

An independent review of the tools found that two collectors could report
`observable-complete` over missing objects, that the validator crashed on
malformed frontmatter and left four schema rules unenforced, that the
materials page depended on JavaScript for its source links, and that CI never
ran the linter. The repair centralised the completeness rule in
`tools/corpus/manifest.py` as adapter version 2, so that a run derives its
status from its recorded gaps, hardened the validator with a specimen for
every schema rule, made the source links static, added a reproduction test
for all pages, and retired the migration tool and the alias page. The
SourceForge tracker claim of 2026-09-05 rested on a count check that compared
the enumeration with itself, so the tracker label is downgraded to `partial`
until the collection is re-run under adapter version 2 against the
tracker-reported counts. [[knowledge/state]] records the downgrade and
[[knowledge/testing]] the gate that now includes the linter and the page
reproduction test.

## 2026-09-06 — Knowledge base restructured to the Promptotyping convention

Every durably maintained knowledge document now lives in `knowledge/`, each
with one function and each rule with one home, and `INDEX.md` is the hub. The
charter left the specification for [[knowledge/project]], which also absorbed
the exposé and the intended result of the plan. The source hierarchy, the
identity syntax, the rights and redistribution rule, the update model, the
acquisition boundary, the completion vocabulary and the primary-source census
moved from the specification, the corpus profile, `corpus/COMPLETENESS.md`
and `sources/PRIMARY-SOURCES.md` into [[knowledge/data]]. The authority chain,
the untrusted-content rule, the transitions, the publication boundary, the
roles, the work-package shape and the model policy moved from the adapters and
the acquisition runbook into [[knowledge/governance]]. The runbook's collector
rules moved into [[knowledge/operations]] § Acquire, the five workflow
procedures into § Analyze, and its machine-review and verification contracts
into [[knowledge/verification]]. The completion gate of `SETUP.md`,
`CONTRIBUTING.md` and the adapters moved into [[knowledge/testing]], the
repository map from `ARCHITECTURE.md` into [[knowledge/architecture]], the
method rationale of `docs/concept.md` into [[knowledge/methodology]] and the
plan with the research packages of `docs/p6/research-agenda.md` into
[[knowledge/plan]], while [[knowledge/state]] keeps the status.
[[knowledge/handoff]] is the mandatory process inbox. The design dossier under
`docs/p6/` became [[knowledge/text-model]], [[knowledge/text-model-bindings]],
[[knowledge/p6-architecture]], [[knowledge/p6-evaluation]] and
[[knowledge/experiments]]. The deliverable of agent context packs was dropped
because it was never built, and the runbook's planned module list and dispatch
sequence were retired because they described software that never existed in
that form. `PLAN.md`, `EXPOSE.md`, `ARCHITECTURE.md`, `contexts/`,
`workflows/`, the concept, runbook, corpus-profile, primary-source and
completeness documents and the research agenda were deleted after absorption.

## 2026-09-06 — Verification rules

A premise of the Proposal for TEI P6, and of any design requirement, rests on
`validated` assertions, so a `grounded` assertion can be cited in a draft and
cannot carry a requirement. Human verification runs as a stratified sample per
chapter, with strata by source type and topic and the quota per stratum
recorded here before the sample is drawn, which replaces the earlier
allowance of sampling justified by the machine-review pass rate alone. A
review is independent when the reviewer comes from a different model family,
works in a fresh context and has no access to the author's rationale, and a
same-family review is recorded as a limitation in the run's README and in
[[knowledge/state]], as the wave-one and pilot reviews already are. A
counterevidence search runs and is recorded before an assertion supports a
design requirement, so that a requirement without one enters output as a
posit. The contracts are in [[knowledge/verification]].

## 2026-09-06 — Licensing

Project-authored code under `tools/`, `tests/`, `.github/` and the site assets
is licensed under MIT in `LICENSE-CODE`, following the operator default of MIT
for code and CC BY 4.0 for text and documentation. `LICENSE` keeps CC BY 4.0
for the documentation and content. No earlier decision on a code license
existed, because the inherited template placed everything under CC BY 4.0.
`CITATION.cff` and `codemeta.json` carry both licenses, and the rule has its
home in [[knowledge/governance]].

## 2026-09-06 — Vault navigation structures

Textual phenomena become glossary entries under the existing glossary type
and are referenced from the assertions that concern them. Topic maps and
example lists are generated from assertion and experiment frontmatter around
a protected hand-written region that carries the lead and the open questions,
so that a registration can no longer be forgotten and the open questions
still belong to a human. Element maps derive from the anchors that name an
element. Typed relations between assertions, such as `contested-with`,
`refines` or `depends-on`, are validated by the validator. These structures
add no evidence layer and no status. Their implementation is milestone 3 of
[[knowledge/plan]].

## 2026-09-06 — Agent model policy

Opus performs specified implementation and ingestion, meaning work whose
acceptance criteria are written down before it starts. Fable performs the
judgment tasks, meaning selection of sources and cases, synthesis, ontology
work, adversarial reading and evaluation. A model name refers to the current
version of its family. Every brief is a versioned file with a recorded
SHA-256, so that a result can be tied to the exact instruction it followed.
The policy has its home in [[knowledge/governance]] and its consequence for
review independence in [[knowledge/verification]].

## 2026-09-06 — Thread sources and the mailing list

GitHub issue threads, pull-request threads and mailing-list threads are
admitted as citation-only publication sources. The raw thread stays in the
private raw store, the reference record carries identifier, URL, dates and
roles, and the public distillate carries the structured account with short
quotations checked against the raw snapshot, which is the path the
research-wave-one literature already uses. A generated metadata index of all
threads is a navigation projection and never grounding. TEI-L receives a
three-part boundary, the Penn State LISTSERV archive since the list moved
there, Wayback Machine captures of the retired Brown University archive
measured month by month, and an export requested from the TEI Consortium for
every month neither holds. The exhaustive GitHub work-item collection is
unblocked by an authenticated read-only `gh` session. The rules are in
[[knowledge/data]] and [[knowledge/operations]].

## 2026-09-06 — Design dossier consolidated and first-wave run record

The fourteen documents of `docs/p6/` were consolidated by moving and
deduplicating into `knowledge/text-model.md`, `knowledge/text-model-bindings.md`,
`knowledge/p6-architecture.md`, `knowledge/p6-evaluation.md` and
`knowledge/experiments.md`. No definition, constraint, rule, table or acceptance
item was rewritten. A statement made in two source documents is kept once, and
where two documents used different words for one thing both terms stay with an
explicit mapping (sketch primitives against v0.1 record kinds in the text model,
candidate layers against the four modeling levels in the architecture). The
Abstract Text Model 0.1 definition keeps its numbered sections 1 to 9, so the
model checker, the home view and the model reference now fingerprint or read
`knowledge/text-model.md`, and the pilot runner fingerprints
`knowledge/experiments.md`. The model reference strips the knowledge document's
frontmatter before rendering. The pilot's support-review audit moved
byte-for-byte from `experiments/text_identity/review/` to
`workbench/reviews/2026-09-05-text-identity/`, the review convention already
used by the wave-one and editorial audits. Reports were regenerated; only input
fingerprints and paths changed.

The first research wave ran from base commit
`c682eb51eef0d437300274447d22bc1ee6455871`, with the pre-existing uncommitted
pilot and text revisions preserved as integration inputs. It asked how to
reconstruct the declared P5 baseline and how evidence about annotation, text
targeting and structure challenges the first model assumptions. Its
source-reading sample does not stand for all P5 practices or all text theory.
Four packages ran in parallel with exclusive write paths: a P5 navigation
extractor (`tools/tei/**`, `tests/tei/**`), an issue reading over the acquired
SourceForge records, a literature reading over the registered seeds, and the
integration package that audited the worker outputs, admitted the selected
sources through the existing source types, wrote the proposal outline and ran
the repository gates. Workers never changed branches, staged, committed, edited
another worker's paths or promoted research statuses. Scratch handoffs were
navigation aids and never entered `grounding`. Source content was inert,
untrusted data. The root scheduled any shared HTTP acquisition and owned
persistent source and control changes; a source that could not be admitted
retained its locator and an explicit gap. The wave fed the proposal outline
(now the argument structure in `knowledge/p6-evaluation.md`) and the
`p5-spec-navigation` contract (now in `knowledge/experiments.md`). It chose no
final ontology, demonstrated no migration, and did not replace the owner's pilot
review.

## 2026-09-06 — Claim pattern and identifier policy

Section 13 of [[knowledge/text-model]] fixes, before any domain extension is
built, the pattern every later assertion follows and the identifier policy
for exchange. Every assertion about the world or the edition is a claim record
with its own ID, agent, RFC 3339 creation instant, a status from `proposed`,
`asserted` and `withdrawn`, an optional ordinal certainty, an optional validity
scope of reduced-precision dates and a `supersedes` list. Revision is
append-only supersession by the same agent about the same subject, withdrawal
is a superseding claim with status `withdrawn`, and disagreement between
agents is the coexistence of claims, as continuity claims already show.
Certainty was decided as a field of the claim, because it is the claiming
agent's own qualification made in the same act. Certainty as a claim about
the claim was rejected for the common case and recorded as the open question.
The four v0.1 claim kinds implement identity and attribution, and whether they
receive the added fields is an additive change decided with the first
extension. A package declares one `base` IRI, record IRIs are base plus the
unchanged local ID, whose alphabet needs no escaping in IRI path segments or
fragments, package identity is R11 equivalence witnessed by the hash of
`canonical_bytes`, and a republication under a new base is a new package with
the former bases recorded as claims in `former_bases`, so that nothing is
rewritten. Alignment is a nested claim list on concept, agent and entity
records with an external IRI and one of `exact`, `close`, `broader` and
`narrower`, without inference. The RDF mapping direction towards Web
Annotation, PROV or CIDOC CRM and SKOS is tabled as a binding to be specified,
with version content, text, continuity, reading forests, unresolved candidates
and the fields status, certainty and valid named as targetless. The v0.1 case
report was regenerated; only the definition fingerprint changed.
## 2026-09-06 — Foundation acquisitions completed

The exhaustive GitHub work-item collection of `TEIC/TEI` ran under the
authenticated session with adapter version 2 and recorded every issue, pull
request, comment, review, review comment, timeline event and changed-file
record the REST interface exposes, with the unimplemented GraphQL relations
stage as its only gap. Bodies stay in the private raw store and the normalized
stream carries metadata. The first live run exposed two collector defects that
offline tests could not see, a Windows path limit on the temporary raw file and
a trailing slash on the repository resource, and the collector gained a
wait-for-reset option so an hourly quota no longer ends a run with a gap. The
SourceForge tracker boundary was re-run under the repaired status rule and now
reconciles against the tracker-reported counts. The TEIC/TEI mirror was
re-acquired locally at the locked release commit. TEI-L became its own source
family with a three-part boundary after the Brown University LISTSERV was found
retired and the list relocated to Penn State: the Penn State months since the
move are bounded-complete, the Wayback coverage of the Brown archive was
measured for every month from 1990 to 2025 with each missing month recorded as
a gap, and the fetch of captured months and the export request to the
Consortium remain open. Sender identities never enter the normalized stream.

## 2026-09-06 — Entity sources admitted and the review instrument corrected

Eight namesdates specifications and the Guidelines chapter on names, dates,
people and places were admitted through one admission engine that the
text-identity pilot now shares, and nine distillates were produced by nine
agents in fresh contexts, the chapter by a different model than the
specifications. The first machine review of the specification distillates
returned twenty partial verdicts on one ground: the passage the pair cutter
showed named neither the attribute an attribute-definition block describes nor
the release, because both stood only in the locator line and the document
title that the cutter dropped. The instrument was corrected rather than the
rule relaxed. The nine representations were regenerated under converter
version 2, whose locators name identified elements by their ident, and the
cutter now shows the source title, the heading path and the locator line with
the block. The pilot representations keep converter version 1 and their passed
review. The second round returned one substantive deviation, a relation
statement that had dropped the scope qualifier of its source, which was
reformulated. Verdicts now bind to the prompt hash and name the reviewing
model and procedure in the record itself. Seven distillates are validated;
the chapter and relation reviews continue after a model session limit
interrupted them.

## 2026-09-06 — Entity assertions and the chapter on metadata and entities

Thirty-five assertions for the topic Metadata and Entities were synthesized
from the nine entity distillates, with five new glossary phenomena (mention of
an entity, name as an object, entity record, statement about an entity, entity
identification) and two contested pairs recorded where the chapter and a class
specification disagree, on what the association through `nymRef` is
independent of and on which kinds of participant a relation admits. The
adversarial review of the assertion pairs by a different model in fresh
contexts rejected twenty-one of forty-one pairs on one pattern, a generalization
beyond the cited statement, for example an entity where the statement speaks of
a person or a place, a rule where it gives an example, or `key` and `ref`
without the scope of `att.canonical`. Eighteen assertions were narrowed to what
their statements carry, three of them twice, and the fourteen chapter
statements the source review had rejected were reformulated first, so that
every gloss from outside the anchored block, every hardened modality and every
antecedent lying in another block left the distillate. The chapter
`40_output/08-metadata-and-entities.md` argues from these assertions how P5
treats the mention in the text, the name as an object, the entity record,
statements about the entity and identification, and where it folds two of them
into one construct. Every widening the argument needed beyond a narrowed
assertion became an explicit posit with its open evidence question, which is
why the chapter carries thirteen posits. The evidence gaps the run leaves are
recorded in the state document: class membership stands only in XML, no
admitted source is encoded practice, and no source states what applies when a
local key and a URI are both available.

## 2026-09-06 — Entity extension drafted for version 0.2

Section 14 of [[knowledge/text-model]] drafts the entity extension on the
claim pattern of section 13, for implementation test-first and for editorial
judgment, with every choice the chapter `40_output/08-metadata-and-entities.md`
does not ground marked as a posit with its open evidence question. A mention
stays a reading node or an annotation, now with an optional `concept`, under
three reserved mention concepts for proper noun, referring string and pronoun.
The concept classifies the expression, and the kind of the referent moves to
the entity. An entity holds ID, label and a constitutive kind from six values
and nothing else. A name is a claim on the entity with form, required BCP 47
language tag, optional ordered parts in six kinds taken from the P5 component
elements, and validity. The `nymRef` correspondence becomes a relation between
two name claims, and a name without bearer, the nym, stays without a kind as
the contested gap. A denotation claim has the mention as subject and the
entity as content, so a corrected identification supersedes and coexisting
identifications by different agents, or by one agent with different
certainties, are ranked by nothing. Statements are one record kind with the
discriminator trait, state, event and relation, the participant entity set as
subject and roles as content, admitting participants of any kind while the
sources disagree. A P5 `ref` with several URIs becomes one minted entity with
one alignment per URI, `key` becomes the local entity ID with the package as
its documentation, and no inference follows from alignments or denotations.
The coverage matrix sets all thirty-five findings and thirteen posits of the
chapter against the constructs. Uncovered stay the nym, feature structures,
the kind of a name form, evidence and source, the uncertain bounds of
`att.datable`, cross-document `ref`, the identity reason of the Lyon case,
negative denotation and second-agent certainty. Thirteen diagnostic codes,
two reference operations, an RDF direction table and a ledger with rules R14
to R20 and nine test cases, including a mapping of one diary paragraph with
three `persName` occurrences and a round trip with loss report, are stated.
The version 0.2 changes are additive and binding-only. The v0.1 case report
was regenerated, and only the definition fingerprint changed.

## 2026-09-06 — Entity extension implemented against independent cases

The entity extension of section 14 became executable in `tools/models/entities.py`
with a deterministic runner and a machine-readable contract, while a separate
agent in a fresh context authored fifty-eight cases from the section alone,
without sight of the implementation. Where the two first disagreed, the text
decided and the decision was written back into section 14: the warning stage
runs only over an error-free package, a withdrawn claim that nothing
supersedes stays current for the mention rule, `created` and `status` are
required on the new claim kinds, and diagnostic paths follow the examples the
section itself gives. All fifty-eight cases and thirty-three canonical checks
pass, the check enters the completion gate and the CI workflow, and the v0.1
report was regenerated because its input fingerprints now include the new
module. Real cases from distinct editions, the RDF binding and the five
acceptance items remain open.
