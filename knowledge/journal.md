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
updated: "2026-09-07"
related: [INDEX, specification, plan, state]
---

# Journal

Chronological decision record of the vault, append-only, newest entry last. The
knowledge documents carry the current state, and every entry here carries one
dated decision in a fixed form, what was decided, why, what it replaces and
where the result now lives.

## Entry format

```markdown
## YYYY-MM-DD — one-line subject

- **Decision.** What was decided, in one or two sentences.
- **Why.** The reason, in one to three sentences, with the alternative it was
  preferred to where one was weighed.
- **Supersedes.** What it replaced, or "nothing".
- **Carried by.** The documents, records or commits that hold the result, as
  wikilinks to knowledge documents or backticked paths.
```

An entry stays short. Work performed, results already recorded elsewhere and
progress counts belong in [[knowledge/state]] and in the Git history.

## 2026-09-04 — Vault instantiated

- **Decision.** The Grounded Vault template became the TEI P6 Research vault,
  with twelve controlled topic maps, three active source types and a German
  scholarly synthesis as the intended output. Findings, interpretations and
  proposals stay distinct, and human verification is reserved for the project
  owner or a designated domain expert, so review by another agent counts only
  as machine review.
- **Why.** A provenance-complete analysis of P5 needs a fixed evidence chain
  and a verification role that no machine process can occupy.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/specification]], [[knowledge/verification]].

## 2026-09-04 — Acquisition and official P6 scopes separated

- **Decision.** Collector build and corpus acquisition follow staged work
  packages with exclusive ownership. Official Council work on P6 becomes its
  own primary-process source family, the Council meeting index defines the
  observable minutes boundary while the documentation repository is a separate
  incomplete source, and the P5 4.12.0 baseline is pinned to commit
  `113e933e21f016e2655518321e9d10214b8d9fcb`. Raw mirrors, dumps, unlicensed
  discussion text and third-party publications stay local or metadata-only
  until rights are established.
- **Why.** An official record and an independent interpretation carry
  different authority, and a working-document repository cannot bound a record
  series its own index bounds.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/data]], [[knowledge/governance]],
  `sources/registry.yaml`.

## 2026-09-04 — Promptotyping project contract completed

- **Decision.** The documents in `knowledge/` are treated together as the
  executable Promptotyping contract of the project, and the entry points route
  into it instead of restating it. The project does not assume that P5 needs a
  rewrite, so repair, compatible evolution, redesign and non-change stay open
  alternatives until evidence and migration prototypes distinguish them.
- **Why.** A rewrite assumed at the start would settle the research question
  before the evidence exists, and a contract restated across parallel entry
  documents drifts.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/project]], [[knowledge/specification]],
  [[knowledge/INDEX]].

## 2026-09-04 — P6 design dossier established

- **Decision.** Provisional P6 design knowledge is kept apart from stable
  control knowledge in a navigable dossier under `docs/p6/`. The dossier is no
  evidence layer and cannot be cited as proof of P5 behaviour or of official
  TEI policy, and executable metamodels, bindings and fixtures receive their
  own artifact contracts before implementation.
- **Why.** Questions, hypotheses and evaluation contracts change on a
  different cycle than the control documents, and mixing them would let a
  hypothesis pass as a source-supported claim.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/text-model]], [[knowledge/p6-architecture]],
  [[knowledge/p6-evaluation]], [[knowledge/experiments]].

## 2026-09-04 — Public documentation language and plan boundary clarified

- **Decision.** Public entry points and architecture documents are written in
  English, while a later scholarly output may declare its own language. The
  oversized implementation plan gives way to a stable phase and gate map, with
  acquisition procedures, requirements and volatile progress each kept in the
  document that owns them.
- **Why.** The repository addresses the international TEI community, and a
  plan that repeats status or operational contracts drifts against documents
  that change on other schedules.
- **Supersedes.** The detailed implementation plan.
- **Carried by.** [[knowledge/plan]], [[knowledge/specification]],
  [[knowledge/state]].

## 2026-09-04 — Primary-source universe and acquisition artifacts defined

- **Decision.** All primary sources means every publicly observable object
  within the registered official interfaces at a declared observation time,
  plus objects admitted through explicit sampling protocols, with
  inaccessible, deleted, private and lost material named as a gap. Normative
  publications, governance decisions, discussions, implementations, historical
  records and observed practice form separate authority classes. Raw responses
  and Git mirrors stay local, normalized inventories and run manifests are
  repository-safe, and the collectors are upstream artifacts outside the
  evidence chain.
- **Why.** Without a declared observation boundary no completeness claim can
  be checked, and one undifferentiated corpus would let a discussion carry the
  weight of a normative publication.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/data]], [[knowledge/operations]],
  [[knowledge/architecture]].

## 2026-09-05 — Primary-data overview established as a generated projection

- **Decision.** The first research frontend is a static overview generated at
  `docs/corpus.html` from the registry, the source locks and the manifests
  those locks reference. Its unit is the registered source family, it exposes
  status, completion target, rights and gaps without publishing raw source
  bodies, and it is a navigation projection that never appears in `grounding`
  and is never hand-edited.
- **Why.** A generated view over control records alone can neither invent
  evidence nor drift from what the project actually holds.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/design]], [[knowledge/architecture]].

## 2026-09-05 — Research frontend adopted as a public P6 support workbench

- **Decision.** The materials overview becomes the first surface of a research
  workbench for evidence-based P6 development, extended by evidence tracing,
  comparison, proposal evaluation and migration experiments only once their
  canonical inputs exist. GitHub Pages is the intended host, automation may be
  prepared before a remote exists, and publication stays blocked until
  repository owner and visibility are settled.
- **Why.** The workbench earns its audience through what the vault has
  actually acquired, and publication before settled ownership would fix an
  unchosen identity.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/design]], [[knowledge/project]].

## 2026-09-05 — Materials view aligned with the acquisition hierarchy

- **Decision.** The materials view shows one sortable row per registered
  source family with every manifest-declared data object as a subcollection
  beneath it. Titles and short descriptions come first, identifiers, control
  vocabulary, rights and manifest names move under technical details, search,
  filtering and sorting replace explanatory prose and aggregate counts, and an
  open gap becomes a short work item linked to its control record.
- **Why.** An aggregate number on a growing corpus reads as a claim about
  completeness.
- **Supersedes.** The prose-led materials overview with aggregate counts.
- **Carried by.** [[knowledge/design]].

## 2026-09-05 — Interface design split into a seventh control document

- **Decision.** [[knowledge/design]] becomes the seventh control document and
  owns the information architecture, content placement, interaction,
  accessibility, provenance, generation and publication contract of the public
  workbench. It grounds no claim and creates no status, and volatile
  implementation state stays in [[knowledge/state]].
- **Why.** The workbench has an audience, an update rhythm and a set of
  invariants that no longer fit inside the research specification or the
  evidence schema.
- **Supersedes.** The placement of interface design inside the specification
  and the schema.
- **Carried by.** [[knowledge/design]], [[knowledge/INDEX]].

## 2026-09-05 — Project working language unified as English

- **Decision.** English is the sole working language of the control documents,
  the public workbench and the intended scholarly synthesis and design
  specification, while canonical TEI identifiers stay unchanged.
- **Why.** One language across control documents and public surface removes
  the split between an English repository and a German output that readers of
  either would have to bridge.
- **Supersedes.** The allowance of a German final output and the German labels
  of the materials interface.
- **Carried by.** [[knowledge/specification]] § Style sheet,
  [[knowledge/project]].

## 2026-09-05 — Public repository established for the research vault

- **Decision.** The canonical public repository is `chpollin/tei-p6-research`,
  and GitHub Pages publishes the generated static workbench from it through
  the pinned workflow.
- **Why.** The name keeps the project visibly independent and stays broad
  enough for acquisition, grounded knowledge, P6 evaluation and the workbench
  without presenting itself as the official TEI P6 repository.
- **Supersedes.** The publication block on repository owner and visibility.
- **Carried by.** `README.md`, `.github/workflows/pages.yml`.

## 2026-09-05 — Public name and documentation history policy settled

- **Decision.** The public project name is TEI P6 Research, while Grounded
  Vault names the evidence system the project uses. Git history records
  file-level change, [[knowledge/state]] records present reality, this journal
  records durable decisions, and a release-oriented changelog is deferred
  until the project publishes named versions.
- **Why.** A changelog before named versions would duplicate Git and invite
  status facts to drift outside the state document.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/INDEX]], [[knowledge/state]], this document.

## 2026-09-05 — Static workbench source architecture modularized

- **Decision.** The workbench stays framework-free and deterministic, and its
  implementation is divided into data and view-model construction, rendering,
  CSS and JavaScript, with page-specific renderers and shared infrastructure
  only where their contracts coincide. CSS and JavaScript modules are embedded
  during generation, so complete generated HTML stays the only published
  artifact.
- **Why.** One builder would otherwise mix research-data interpretation,
  markup, styling and interaction as the workbench grows.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/design]], `tools/sitegen/`.

## 2026-09-05 — Bounded text identity and annotation pilot

- **Decision.** A bounded pilot on text, versions, regions and annotations
  tests the research-to-design workflow and the identity assumptions, choosing
  no ontology and no architecture, and its reports never ground. Complete P5
  specification files enter from the locked 4.12.0 Git component with hashes
  and licensing, leaving the partial HTML family boundary unchanged. A
  representation keeps the full XML with verbatim descriptions as checked
  reading blocks. Reanchoring yields a proposal for human confirmation, and a
  review verdict binds to its prompt hash.
- **Why.** The first review exposed that bare English descriptions omit the
  release and attribute context these claims need, so the instrument was
  completed.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/experiments]], `experiments/text_identity/`,
  `workbench/reviews/2026-09-05-text-identity/`.

## 2026-09-05 — Critical review clarifies the route from evidence to a text model

- **Decision.** The research target is a scoped, coherent and usable abstract
  text model for a possible P6, with P5 as normative baseline and migration
  obligation and independent theory and practice as the challenge to its
  adequacy. A narrow claim needs complete coverage of its own source
  dependencies, an architecture-wide claim the full declared P5 inventory. The
  candidate prose separates model preservation, task-specific equivalence and
  byte preservation, and migration reporting gains axes for coverage,
  preservation, lexical change, dependencies and reversibility.
- **Why.** An external editorial review found the route from evidence to model
  unstated, and its judgments are no source-support verdicts.
- **Supersedes.** Nothing. It sharpens the scoped pilot policy.
- **Carried by.** [[knowledge/specification]] § Decision gates,
  [[knowledge/text-model]].

## 2026-09-05 — First research wave and proposal integration

- **Decision.** A first parallel wave ran P5 reconstruction, discussion
  analysis and literature reading and outlined an independent Proposal for TEI
  P6, bounded without narrowing the coverage ambition. The specification
  extractor writes a versioned navigation projection under
  `corpus/projections/` that records its source identity and never grounds a
  claim. Citation-only sources use the existing publication type with a
  locally transcribed CSL JSON record, unlicensed full text stays in ignored
  raw storage, and the quotation-fidelity check cannot be repeated in a clean
  checkout.
- **Why.** A wave stays bounded to remain checkable, and a narrowed assertion
  heading showed that the producer's agreement with a source cannot replace
  the independent check.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/experiments]], [[knowledge/data]],
  `corpus/projections/`.

## 2026-09-05 — Abstract Text Model 0.1 executable research contract

- **Decision.** Abstract Text Model 0.1 is a bounded modeling hypothesis whose
  normative definition and machine spec must agree, with case expectations
  authored independently of the resolver. The candidate separates content,
  continuity, targets, structural readings, annotations and typed relations,
  and excludes other media, full P5 migration, customization algebra and
  storage. A shared version ID needs a caller-declared scope, adjacent range
  components count as contiguous, and valid coordinates across overlapping
  aggregate components yield `E_SELECTOR` while invalid ones yield `E_BOUNDS`.
- **Why.** The programme needs an inspectable candidate for testing before it
  prefers an architecture, and independently authored expectations decide a
  disagreement with the implementation.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/text-model]], `experiments/abstract_text_v01/`,
  `tools/models/`.

## 2026-09-05 — Editorial provenance and real-case comparison

- **Decision.** Historical derivation becomes an attributed relation about the
  character version, and an optional editorial profile constrains the existing
  relation records. The real-case study takes at most four accessible edition
  repositories and three cases, each requiring real editorial XML, an exact
  snapshot and a recorded rights disposition, with expectations frozen before
  mapping and one adverse case held back. The home page carries the full
  proposal, and Materials stays separate.
- **Why.** Version identity stays separate from revisable hypotheses, tutorial
  examples cannot stand for editorial practice, and a holdout keeps the mapper
  from being fitted to the case that tests it.
- **Supersedes.** The inventory-only landing page.
- **Carried by.** [[knowledge/experiments]], [[knowledge/design]],
  `experiments/editorial_cases/`.

## 2026-09-05 — Technical proposal and comparative examples

- **Decision.** The home page becomes a technical publication with the
  canonical proposal first, example branches, P5 variants and candidate
  bindings. All P5 modules form the coverage inventory, with modules, document
  types, media and phenomena as distinct axes, and coverage stays a research
  obligation rather than an implemented-domain claim. The comparison view
  assembles cases, source pointers and runtime checks outside the evidence
  chain, keeps failed mappings visible, and never expands the core model or
  the frozen holdout for the display.
- **Why.** The owner rejected the promotional treatment, and a display that
  hides a failed mapping would misreport the reach of the candidate.
- **Supersedes.** The promotional home page treatment.
- **Carried by.** [[knowledge/design]], [[knowledge/p6-architecture]],
  [[knowledge/text-model-bindings]].

## 2026-09-05 — Shared workbench and concise prose

- **Decision.** One maintained source holds navigation, footer, typography and
  controls for all public pages, page styles describe only their own content,
  local and published routes are identical, and the old home path stays a
  generated alias. The Model reference derives from the model contract and the
  Knowledge browser from actual vault links, both navigation projections.
  Running prose avoids colons and semicolons, lists serve navigation,
  alternatives and procedures, tables compare fields, and historical journal
  entries stay unchanged.
- **Why.** The owner asked for one layout and rejected decorative rules, and a
  style rule with one home keeps the pages from drifting apart.
- **Supersedes.** The per-page layouts and the decorative rules.
- **Carried by.** [[knowledge/design]], [[knowledge/specification]] § Style
  sheet.

## 2026-09-06 — Review and repair of the tools

- **Decision.** The completeness rule moves into `tools/corpus/manifest.py` as
  adapter version 2, so a run derives its status from its recorded gaps. The
  validator gains a specimen for every schema rule, the materials source links
  become static, a reproduction test covers all pages, the linter enters the
  gate, and the migration tool and the alias page are retired. The tracker
  family drops to `partial` until it is re-run under the repaired rule against
  the tracker-reported counts.
- **Why.** An independent review found collectors reporting
  `observable-complete` over missing objects, a validator crashing on
  malformed frontmatter, and a tracker claim resting on a self-comparing count
  check.
- **Supersedes.** Adapter version 1 and the tracker family's
  `observable-complete` label.
- **Carried by.** [[knowledge/state]], [[knowledge/testing]],
  `tools/corpus/manifest.py`.

## 2026-09-06 — Knowledge base restructured to the Promptotyping convention

- **Decision.** Every durably maintained knowledge document lives in
  `knowledge/`, each with one function and each rule with one home, and
  [[knowledge/INDEX]] is the hub. The charter, source, governance, procedure,
  verification, architecture and planning content moved into the document that
  owns each question, and PLAN.md, EXPOSE.md, ARCHITECTURE.md, `contexts/`,
  `workflows/`, the runbook, the concept and the research agenda were deleted
  after absorption, together with the agent context packs and the runbook's
  module list.
- **Why.** A rule with two homes drifts, and the dropped items described
  software that never existed in that form.
- **Supersedes.** The root, dossier and corpus-profile documents absorbed
  here.
- **Carried by.** [[knowledge/INDEX]] and the documents it lists.

## 2026-09-06 — Verification rules

- **Decision.** A premise of the proposal and every design requirement rests
  on `validated` assertions, so a `grounded` assertion may be cited in a draft
  but carries no requirement. Human verification runs as a stratified sample
  per chapter, with strata by source type and topic and the quota recorded
  before the draw. A review is independent when the reviewer comes from
  another model family in a fresh context without the author's rationale, and
  a same-family review is recorded as a limitation. A counterevidence search
  precedes any assertion supporting a design requirement.
- **Why.** Structural traceability alone supports no requirement, and a quota
  fixed after the draw can be fitted to its result.
- **Supersedes.** Sampling justified by the machine-review pass rate alone.
- **Carried by.** [[knowledge/verification]].

## 2026-09-06 — Licensing

- **Decision.** Project-authored code under `tools/`, `tests/`, `.github/` and
  the site assets is licensed MIT in `LICENSE-CODE`, `LICENSE` keeps CC BY 4.0
  for documentation and content, and `CITATION.cff` and `codemeta.json` carry
  both.
- **Why.** The operator default is MIT for code and CC BY 4.0 for text, and
  the inherited template had placed everything under CC BY 4.0 without any
  decision on code.
- **Supersedes.** The single CC BY 4.0 licence inherited for the whole
  repository.
- **Carried by.** [[knowledge/governance]], `LICENSE-CODE`, `LICENSE`.

## 2026-09-06 — Vault navigation structures

- **Decision.** Textual phenomena become glossary entries referenced from the
  assertions that concern them. Topic maps and example lists are generated
  from assertion and experiment frontmatter around a protected hand-written
  region holding the lead and the open questions, element maps derive from the
  anchors naming an element, and typed relations between assertions are
  validated.
- **Why.** A generated registration can no longer be forgotten while the open
  questions stay a human responsibility, and these structures add no evidence
  layer and no status.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/schema]], [[knowledge/plan]] milestone 3.

## 2026-09-06 — Agent model policy

- **Decision.** Opus performs specified implementation and ingestion whose
  acceptance criteria are written down before the work starts, and Fable
  performs the judgment tasks of source and case selection, synthesis,
  ontology work, adversarial reading and evaluation. A model name means the
  current version of its family, and every brief is a versioned file with a
  recorded SHA-256.
- **Why.** A result must be tied to the exact instruction it followed, and the
  two kinds of work fail in different ways.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/governance]], [[knowledge/verification]].

## 2026-09-06 — Thread sources and the mailing list

- **Decision.** GitHub issue, pull-request and mailing-list threads are
  admitted as citation-only publication sources, with the raw thread in the
  private raw store, a reference record of identifier, URL, dates and roles,
  and a public distillate whose quotations are checked against the snapshot. A
  generated thread index is a navigation projection. TEI-L receives a
  three-part boundary, the current archive since the move, Wayback captures of
  the retired one and a Consortium export for the months neither holds.
- **Why.** This is the path the wave-one literature already uses, and no
  single archive covers the life of the list.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/data]], [[knowledge/operations]].

## 2026-09-06 — Design dossier consolidated and first-wave run record

- **Decision.** The fourteen documents of `docs/p6/` were consolidated by
  moving and deduplicating into the five model, bindings, architecture,
  evaluation and experiment documents, with no definition, constraint, rule or
  table rewritten and two vocabularies kept side by side under an explicit
  mapping. The model definition keeps its numbered sections, so checkers and
  views now fingerprint the knowledge document. The pilot's review audit moved
  byte-for-byte under `workbench/reviews/`, the review-record convention. The
  first research wave is recorded from base commit
  `c682eb51eef0d437300274447d22bc1ee6455871`.
- **Why.** Fourteen overlapping design documents made a definition hard to
  locate, and a deduplicating move preserves the wording reviews have already
  judged.
- **Supersedes.** The `docs/p6/` dossier.
- **Carried by.** [[knowledge/text-model]], [[knowledge/experiments]],
  `workbench/reviews/`.

## 2026-09-06 — Claim pattern and identifier policy

- **Decision.** Every assertion about the world or the edition becomes a claim
  record with agent, creation instant, a status from `proposed`, `asserted`
  and `withdrawn`, optional certainty and validity, and a `supersedes` list.
  Revision is append-only supersession, withdrawal a superseding claim,
  disagreement the coexistence of claims. A record IRI is the package base
  plus the local ID, a republication under a new base is a new package, and an
  alignment carries an external IRI and one of `exact`, `close`, `broader` and
  `narrower` without inference.
- **Why.** Certainty is the claiming agent's own qualification in the same
  act, so it is a field of the claim, while certainty about a claim stays the
  open question.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/text-model]] § 13.

## 2026-09-06 — Foundation acquisitions completed

- **Decision.** The exhaustive GitHub work-item collection ran under adapter
  version 2 with the GraphQL relations stage as its only gap, and sender
  identities never enter the normalized stream. The collector gained a
  wait-for-reset option, so an hourly quota no longer ends a run with a gap.
  The Wayback coverage of the retired TEI-L archive was measured for every
  month from 1990 to 2025, with each missing month recorded as a gap.
- **Why.** The first live run exposed two collector defects that offline tests
  could not see, a path limit and a trailing slash on the repository resource.
- **Supersedes.** The tracker family's `partial` label, now reconciled against
  the tracker counts.
- **Carried by.** [[knowledge/state]], `sources/registry.yaml`.

## 2026-09-06 — Entity sources admitted and the review instrument corrected

- **Decision.** The nine entity sources were admitted through one shared
  admission engine. The representations were regenerated under converter
  version 2, whose locators name identified elements by their `ident`, and the
  pair cutter now shows the source title, the heading path and the locator
  line with the block. Pilot representations keep converter version 1 with
  their passed review, and a verdict binds to its prompt hash and names the
  reviewing model.
- **Why.** The first review returned partial verdicts because the passage
  shown named neither the attribute nor the release, so the instrument was
  corrected rather than the rule relaxed.
- **Supersedes.** Converter version 1 for newly admitted sources.
- **Carried by.** [[knowledge/operations]], [[knowledge/verification]],
  `tools/review.py`.

## 2026-09-06 — Entity assertions and the chapter on metadata and entities

- **Decision.** The assertions of the topic Metadata and Entities were built
  with five new glossary phenomena and two contested pairs where the chapter
  and a class specification disagree. An assertion is narrowed to what its own
  statement carries, and every widening the chapter's argument still needs
  becomes an explicit posit with its open evidence question.
- **Why.** The adversarial review rejected half of the pairs on one pattern, a
  generalization beyond the cited statement, for example an entity where the
  statement speaks of a person.
- **Supersedes.** Nothing.
- **Carried by.** `30_assertions/`, `40_output/08-metadata-and-entities.md`,
  [[knowledge/state]].

## 2026-09-06 — Entity extension drafted for version 0.2

- **Decision.** Version 0.2 drafts the entity extension on the claim pattern.
  The concept on a mention classifies the expression while the kind of the
  referent sits on the entity, `nymRef` becomes a relation between two name
  claims, a `ref` with several URIs mints one entity with one alignment per
  URI, and `key` becomes the local entity ID.
- **Why.** The claim pattern already carries revision and disagreement, so the
  extension needs no second mechanism, its changes stay additive and
  binding-only, and nothing is inferred from alignments or denotations.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/text-model]] § 14.

## 2026-09-06 — Entity extension implemented against independent cases

- **Decision.** The entity extension became executable with a deterministic
  runner and a machine-readable contract, checked against cases a separate
  agent authored from the section alone. Where implementation and cases
  disagreed the section decided and its text was sharpened, so the warning
  stage runs only over an error-free package, a withdrawn claim that nothing
  supersedes stays current, and `created` and `status` are required on the new
  claim kinds. The check enters the completion gate and the CI workflow.
- **Why.** Cases written without sight of the implementation test the
  specification instead of the code.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/text-model]] § 14, `tools/models/entities.py`.

## 2026-09-06 — RDF binding of the extended model

- **Decision.** The RDF direction tables became a one-way export. Mentions
  with their denotations become identifying Web Annotations, entities take
  CIDOC CRM classes by kind, names become appellations, statements become
  attribute assignments, and alignments become SKOS matches where `exact`
  never becomes `owl:sameAs`. Records without an external class stay in a
  project namespace, and reasoning, SHACL shapes and a decoder stay out of
  scope.
- **Why.** Every record IRI and reference edge must be readable from the
  triples alone, and no mapping may entail an identity the model does not
  claim.
- **Supersedes.** Nothing.
- **Carried by.** [[knowledge/text-model-bindings]] § RDF export,
  `tools/models/rdf_binding.py`.

## 2026-09-06 — GraphQL relations stage of the GitHub collector

- **Decision.** The relations stage reads every issue and pull-request number
  of the REST snapshot and asks the GraphQL API in batches for
  cross-references, closing events, mentions and review threads, keeping
  bodies and logins out of the normalized stream. Project closers stay
  uncollected and the module records the missing token scope as its limit. The
  family label stays `partial` until the next REST snapshot under the
  two-stage collector.
- **Why.** A run manifest is append-only, so the recorded manifest of the same
  day still carries the stage as a gap and may not be rewritten.
- **Supersedes.** Nothing. It closes the foundation run's only gap.
- **Carried by.** [[knowledge/state]], [[knowledge/data]].

## 2026-09-06 — Thread quotations lengthened to one sentence

- **Decision.** A quotation from a thread may run to one complete sentence of
  a comment, still an exact substring of the raw snapshot and starting after
  any personal name. A statement carries only what its quotation shows, with
  anaphora left as the source gives them, every comment attributed to the
  issue author or a commenter, and the issue named in the statement. Where a
  comment breaks across lines or runs into quoted third-party text, only
  narrowing remains.
- **Why.** A fragment of fifteen words rarely carries the frame of a
  statement, so the statements supplied it from the surrounding comment, which
  the reviewer cannot see.
- **Supersedes.** The fifteen-word quotation cap for thread distillates.
- **Carried by.** [[knowledge/data]], [[knowledge/schema]].

## 2026-09-06 — Second entity run closed

- **Decision.** The second run of Metadata and Entities executed the selection
  procedure of [[knowledge/plan]] end to end and rewrote chapter 08 on the
  enlarged base. Two posits became premises, the separation of record and
  reference for persons, places and organizations and the purpose of `idno`
  for external identifiers, and four posits were narrowed. A contested pair
  holds the announced deprecation of `key` against the attribute retained at
  the release. The next topic run is the first run of Text and Document
  Structures.
- **Why.** A conclusion becomes a premise only where the enlarged source base
  carries it, and the counterevidence searches found nothing against the
  chapter's claims.
- **Supersedes.** The posit status of the two promotions.
- **Carried by.** `40_output/08-metadata-and-entities.md`,
  [[knowledge/state]], [[knowledge/plan]].

## 2026-09-06 — Root documents folded into README and the knowledge base

- **Decision.** SETUP.md, HOME.md and NOTICE.md are deleted. The attribution
  of the inherited vault architecture moves to `README.md` § Licence and
  attribution, the navigation and the topic-map list to [[knowledge/INDEX]],
  and each command to the knowledge document that owns the procedure it
  executes. `README.md` gains a quick start.
- **Why.** The convention gives every rule and every command one home, and the
  root keeps only what GitHub and the licences expect, meaning README,
  CONTRIBUTING, the two adapters and the licence and citation files.
- **Supersedes.** SETUP.md, HOME.md and NOTICE.md.
- **Carried by.** `README.md`, [[knowledge/INDEX]], [[knowledge/operations]],
  [[knowledge/experiments]], [[knowledge/design]], [[knowledge/testing]],
  [[knowledge/data]].

## 2026-09-06 — Method rationale and RDF binding merged, selection records moved to the workbench

- **Decision.** The method rationale is folded into [[knowledge/schema]]
  § Rationale and [[knowledge/architecture]] § Lineage, and the RDF binding
  document becomes [[knowledge/text-model-bindings]] § RDF export. The
  selection tables of the topic runs leave [[knowledge/plan]] and become
  records under `workbench/selections/`, a records folder beside
  `workbench/reviews/` and an architecture decision.
- **Why.** A document is split only when its routing question or update cycle
  differs. The rationale shares the question of the artifact contracts and the
  RDF export that of the other bindings, while a dated selection table is a
  record the forward plan points to.
- **Supersedes.** `knowledge/methodology.md`,
  `knowledge/text-model-rdf-binding.md` and the selection tables in
  [[knowledge/plan]].
- **Carried by.** [[knowledge/schema]] § Rationale, [[knowledge/architecture]]
  § Lineage, [[knowledge/text-model-bindings]] § RDF export,
  `workbench/selections/`.

## 2026-09-06 — Journal condensed to a fixed entry form

- **Decision.** Every entry now carries Decision, Why, Supersedes and Carried
  by. The earlier prose of the entries stays in the Git history at commit
  `67c7518`, and from this entry on the journal is append-only again.
- **Why.** The entries had grown into narrations of work that
  [[knowledge/state]] and the Git history already hold, and a decision record
  is read for the decision and its reason.
- **Supersedes.** The free-form entry format.
- **Carried by.** This document.

## 2026-09-07 — Vollständige Guidelines-Aufnahme als Referenzbasis

- **Decision.** Die englischen Guidelines des festgelegten Releases 4.12.0
  werden vollständig auf Quellenebene aufgenommen. Die Grenze umfasst das
  englische Masterdokument, seine Front-, Haupt- und Anhangsteile, sämtliche
  Spezifikationen und lokale XML-Einbindungen. Bereits aufgenommene Quellen
  und ihre Anker bleiben unverändert. Ein generierter Abdeckungsbericht unter
  `corpus/projections/` verbindet Inhaltsverzeichnis, Quellen, Abhängigkeiten
  und tatsächliche Destillationsstände. Er bleibt eine Navigationsprojektion
  außerhalb der Grounding-Kette. Bilder und externe Verweise erhalten einen
  expliziten Nachweis ihres Bestands oder ihrer Grenze. Die Aufnahme erzeugt
  keine Destillate, Assertions oder fachlichen Prüfstände.
- **Why.** Die bisherige thematische Auswahl lässt große Teile der
  P5-Referenzbasis unberücksichtigt. Vollständige Quellenaufnahme und
  überschaubare fachliche Prüfung benötigen unterschiedliche Grenzen.
- **Supersedes.** Die Begrenzung auf zwölf Quellen und zwei Kapitel gilt
  weiterhin für fachliche Themenläufe; die deterministische Aufnahme der
  vollständigen Referenzbasis erhält den hier definierten eigenen Umfang.
- **Carried by.** `tools/ingest_guidelines.py`, [[knowledge/data]],
  [[knowledge/operations]], [[knowledge/plan]], [[knowledge/testing]],
  [[knowledge/design]], [[knowledge/state]].

## 2026-09-07 — Plattformunabhängige Sortierung der Wissensnavigation

- **Decision.** Die Navigation sortiert Dateinamen explizit ohne Beachtung
  der Großschreibung und verwendet den originalen Namen als zweiten Schlüssel.
- **Why.** Windows und Linux vergleichen Path-Objekte unterschiedlich. Nach
  der Umbenennung von `index.md` zu `INDEX.md` reproduzierte die Knowledge-Seite
  deshalb in GitHub Actions die unter Windows erzeugte Reihenfolge nicht.
- **Supersedes.** Die implizite Sortierung nach dem Path-Vergleich des Systems.
- **Carried by.** `tools/sitegen/knowledge_view.py` und
  `tests/test_build_knowledge.py`.
