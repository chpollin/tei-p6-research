---
title: Plan
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-07"
related: [INDEX, project, specification, state, handoff, journal, testing, verification, experiments, p6-evaluation]
---

# Plan

Finishing means an independent Proposal for TEI P6 whose every premise rests
on validated assertions, whose model has been tested phenomenon by phenomenon
against independent and real cases, whose alternatives were compared under
the same dimensions with a migration prototype, and whose corpus boundaries
are either exhausted or recorded as gaps, so that a reader can follow every
claim to its source and every judgment to its reason. The criteria are in
[[knowledge/specification]], the current position in [[knowledge/state]].
This plan carries neither dates nor estimates.

## Two tracks

The evidence track builds the material and the grounded knowledge. It closes
the corpus foundation, adds the vault structures that make phenomena and
topics navigable, and runs the vertical cycles topic by topic. The model
track builds the candidate and its argument. It fixes the claim pattern and
identifier policy, extends the model phenomenon by phenomenon, and derives
the proposal from validated assertions. The tracks meet at the proposal,
whose premises come from the evidence track and whose posits from the model
track. Milestone 1 prepared both tracks, milestones 2 and 9 belong to both,
milestones 3, 4 and 6 to the evidence track and milestones 5, 7 and 8 to the
model track.

## Milestones

| Milestone | Exit condition | Success criterion served | Check |
|---|---|---|---|
| 1. Tools and gates repaired | done 2026-09-06 in commit `1cfdb2e`. Collectors derive completeness from recorded gaps, the validator survives malformed frontmatter and enforces every schema rule, the materials page links statically, CI runs the linter, and every page has a reproduction test | the validator and test suite pass and generated artifacts reproduce | `python -m ruff check .`, `python -m pytest tests -q` |
| 2. Knowledge base restructured | every knowledge document lives in `knowledge/` with one function, every rule has one home, the adapters route by link, every link resolves, and the About page is regenerated from the new inputs | the control system is internally consistent, so the same criterion as milestone 1 | `python tools/validate.py .`, `python tools/build_docs.py --date <date>`, `python -m pytest tests/test_build_docs.py tests/test_build_pages_reproduce.py` |
| 3. Vault structures | phenomena are glossary entries referenced from assertions, topic maps are generated from assertion frontmatter around a protected hand-written region, example lists are generated, element maps derive from anchors, and typed relations between assertions are validated | every assertion resolves to source-faithful statements and is reachable from its topic map | `python tools/validate.py .` with the new checks and `python -m pytest tests/test_validate.py` |
| 4. Foundation closed | the exhaustive TEIC/TEI work-item collection has run under the authenticated session including the GraphQL relations stage, the SourceForge trackers are re-run under adapter version 2 against tracker-reported counts, TEI-L is registered and acquired under its three-part boundary, the archive and website snapshots are reconciled, and a sampling protocol for real P5 documents and customizations is recorded | the GitHub snapshot is `observable-complete` and reconciled, governance, history and literature collections state boundaries, rights, dispositions and gaps, and at least one real-use corpus has a sampling and rights protocol | `python -m tools.corpus.validate_control_plane .` and the collector status lines with exit code 0 |
| 5. Claim pattern and IRI policy | the model states who asserts what about which object with what support as one claim pattern, and every model object, version, selector and reading carries an identifier under a recorded IRI policy, executable in `tools/models/` with cases that pass | the abstract text model is an executable contract with independently authored cases and a reproducible report | `python tools/check_abstract_text_v01.py --check`, `python -m pytest tests/models` |
| 6. Entity run and topic cycles | Metadata and Entities is the first selection-driven vertical cycle, with sources selected from projections, admitted, distilled, synthesized into validated assertions and written into a grounded chapter, and the remaining topics follow in the order set by the posits of chapter 12. The selection procedure of a topic run and the next two runs are fixed under Topic runs below | every central P5 problem claim has evidence, counterevidence or an explicit open-evidence status, and three vertical pilots traverse the full chain under independent review | `python tools/validate.py . --chapter 40_output/<slug>` per chapter and the review-only checks |
| 7. Model extended phenomenon by phenomenon | a coverage matrix relates phenomena to the pinned P5 modules and their effective ODD semantics, each phenomenon has independent synthetic cases and real cases from distinct editorial contexts, and an RDF binding preserves the model instance under a tested contract | P6 alternatives are compared against the same dimensions and representative use cases | `python tools/check_abstract_text_v01.py --check`, `python tools/check_editorial_cases.py --check` |
| 8. Proposal from assertions | every premise of the proposal is `validated`, a counter-reader review of the argument is recorded, the alternatives are compared under [[knowledge/p6-evaluation]], a migration prototype has run on representative P5 documents with loss, ambiguity, intervention and tooling impact reported, and the official P6 process is compared with a dated record | a migration prototype tests representative documents, alternatives are compared, and premises rest on validated assertions | `python tools/validate.py . --chapter 40_output/12-p6-design.md`, `python tools/check_wave1_sources.py . --review-only` |
| 9. Publication | the human verification sample per chapter is recorded with its quota, the site is rebuilt from the released revision, and the owner has cleared the release | no machine process assigns human verification and generated artifacts reproduce | the completion gate in [[knowledge/testing]] |

Design exploration may run ahead of the evidence track, but no candidate is
promoted as preferred before the relevant P5 baseline, problem evidence,
alternatives and migration results exist. Failure at a gate produces a
documented gap or open question.

## Workstreams inside the milestones

The independently reviewable workstreams of the programme keep their content
inside the milestones. Sources and provenance, meaning registry, locks,
collectors, manifests, rights, completeness and the raw and normalized
corpus, belong to milestone 4. P5 model extraction, meaning ODD parsing, the
object graph, constraints, generated schemas and release comparison,
supplies the module axis of milestone 7 and the element maps of milestone 3.
History and decisions, meaning issues, pull requests, commits, Council
records, releases and typed decision trails, are acquired in milestone 4 and
synthesized in the topic cycles of milestone 6. Knowledge engineering,
meaning representations, distillates, assertions, topic maps and retrieval
indexes, is milestones 3 and 6. P6 design, meaning principles, core-model
alternatives, blueprints, serializations, constraints, examples and
governance, is milestones 5, 7 and 8. Text concepts and practice, meaning
independently sourced definitions, explicit identity assumptions, bounded
case selection and editorial task expectations, feeds milestones 6 and 7.
Conformance and migration, meaning validators, converters, roundtrip
comparison, loss reports, compatibility matrices and implementation studies,
is the binding work of milestone 7 and the migration prototype of milestone
8, where equivalence, ambiguity, loss and implementation costs are measured
on representative P5 corpora and customizations. The design dossier, meaning
the evaluated alternatives and the grounded specification, is milestones 8
and 9.

## Research packages

Three bounded research packages remain open. Each names, before delegation,
the base commit, exclusive write paths, read-only inputs, required checks and
gaps to report under the work-package shape in [[knowledge/governance]].

- **A. Text identity requirements.** A bounded set of text-theoretical,
  annotation-model and editorial-practice sources is admitted and distilled
  separately, synthesized only through assertions, and turned into a
  requirement set that distinguishes source findings from project choices,
  with an adverse example for each requirement. Acceptance requires at least
  two conceptual alternatives facing the same independently reviewed
  observations. The executed text identity pilot compared two selectors
  inside one object model, which the acceptance criterion excludes, so the
  package stays open.
- **B. Real editorial cases.** Three bounded case packages from distinct
  editorial contexts cover hierarchy, overlap, and customization or
  contextual interpretation, with selection unit, inclusion and exclusion
  rules, source versions, rights, authority, ODD and tool context and known
  sampling bias recorded, required observations stated before encoding, and
  an adverse case reserved for testing after the candidates are defined.
  Acceptance requires reproduction from declared inputs, independent domain
  review of the expected distinctions and explicit coverage gaps. The
  executed editorial case study covers three fragments of one edition, so the
  package stays open.
- **C. One comparative workflow decision.** Annotation review after a text
  edit is the first decision-sized task. Repair within P5 tooling, compatible
  evolution, an alternative abstract model, and retaining or deferring the
  current behavior are compared with the editorial task and expected
  observations held fixed, with participant roles, procedure, baseline and
  acceptance criteria specified before correctness, effort, errors and
  interventions are measured, and with migration reported on separate axes
  for coverage, preservation, lexical changes, dependencies and
  reversibility. Acceptance requires technical and domain reviews of the same
  record, with costs and unknowns alongside benefits and the evidence named
  that would reverse the recommendation. No bounded execution of this package
  has occurred.

## Operator decisions

The following decisions belong to the owner and are recorded in
[[knowledge/journal]] when taken.

- Accept, revise or defer each model document and each acceptance item in
  [[knowledge/experiments]].
- Select the foreign editions that supply the real cases of package B and
  milestone 7.
- Authorize the exhaustive authenticated GitHub collection run of milestone 4.
- Rank the architecture options after milestone 8.
- Clear the release of milestone 9.

## Definition of completion

The project is complete only when the declared source boundaries have been
exhausted or their gaps recorded, every central P5 claim is traceable, the
formal P5 model rebuilds deterministically, P6 alternatives have been tested
on representative and adverse cases, migration losses are explicit, and the
final recommendations survive deterministic validation, adversarial review
and the designated human verification process.

## Topic runs

A topic run is one selection-driven vertical cycle of milestone 6 on one
topic of the controlled topic set. It starts from the evidence questions of
the topic and ends with a grounded chapter and a recorded human sample. The
entity run of 2026-09-06 was the first such cycle; its selection was made
case by case and the gaps it left stand under Open work in
[[knowledge/state]]. This section fixes the selection procedure so that an
agent can execute it and a reader can audit it, and applies the procedure to
the next two topics. The procedure text carries no figures. The dated
snapshot and selection tables of the two runs are records under
`workbench/selections/`, where their counts hold for the named manifests
only.

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
  sampling protocol of milestone 4 and package B; a run may reuse a document
  the vault has already admitted by extending its distillate, which cuts new
  pairs for review and leaves the reviewed pairs untouched.
- GitHub work items. The stream `corpus/normalized/github/teic-tei-work-items.jsonl`
  is read for records with `kind` `issue` or `pull-request`, matched on
  `title` and filtered by `labels`. A hit is listed with number, kind, state,
  creation and closing dates, comment count and labels, and the table names
  the manifest of the stream it read. Bodies stay in the private raw store,
  and a thread is admitted only when its raw snapshot is present in the
  checkout that ingests it.
- SourceForge tickets. The stream `corpus/normalized/sourceforge/tei-legacy-trackers-r4.jsonl`
  is read for records with `object_type` `ticket`, matched on `summary` and
  listed with tracker, number and status. The migration copied the ticket
  titles into GitHub issues that carry the label `sf-automigrated`, so every
  SourceForge hit is reconciled with the GitHub record of the same normalized
  title and creation date. The two stay distinct records related by
  migration, the fuller manifestation is the one admitted, and the other is
  named in the same row. The SourceForge status vocabulary, `closed-fixed`,
  `closed-accepted`, `closed-rejected`, `closed-wont-fix` and
  `open-accepted`, is the first outcome signal, because the GitHub copy of a
  migrated ticket carries `closed` and nothing more.
- TEI-L threads. The stream `corpus/normalized/mail/tei-l-psu.jsonl` is
  matched on `subject` and grouped into threads by the subject without its
  reply prefixes; a hit is a thread with its months and its message count.
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
- items closed as `Wontfix`, `closed-rejected` or `closed-wont-fix`, which
  show that the case was considered and declined, with the reason to be read
  in the thread;
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

### Run 2 of Metadata and Entities

The entity run left three gaps in [[knowledge/state]]. Class membership
stands only in XML, no admitted source is encoded practice, and no source
states what applies when a local key and a URI are both available. The
second run of the topic closes them. Its questions come from the posits of
`40_output/08-metadata-and-entities.md` and from Open work.

| Question | Kind | Origin |
|---|---|---|
| Q1. Which class specifications carry `key`, `ref`, `nymRef` and `role` to the naming elements, through which chain, and do their remarks travel with the attributes? | coverage | posits boundary and inheritance; Open work |
| Q2. Which encoded practice at the pinned release places the kind of referent or a role on a mention, and identifies mentions by `key`, by `ref` or by both? | coverage | posits mention and alignment; Open work |
| Q3. Where do the sources state the separation of record and reference for person and place records, and how do records point outward? | coverage | posit separation |
| Q4. What purpose does the specification of `idno` state, and does encoded practice carry external references through it? | coverage | posit idnoread |
| Q5. Which sources state the time frame, documentation and relatability requirement for traits, states, places and organizations? | coverage | posit extension |
| Q6. Do the sources give the act of identifying an agent, a date, a certainty or a source pointer? | problem claim, identification names no agent, date or certainty | posit denotation |
| Q7. Do the records themselves carry identification, or only their names? | problem claim, the record links outward through `idno` and the mention through `key` and `ref` | posits separation and alignment |
| Q8. What applies when a local key and a URI are both available? | problem claim, no precedence when `key` and `ref` co-occur | Open work; assertion `p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur` |

The streams queried on 2026-09-06, the declared query of every family with
its hit count and the disposition of every hit stand in the
[selection record](../workbench/selections/2026-09-06-metadata-and-entities-run2.md).

Run 2 admits twelve sources, no chapter among them and three threads. They
are `att.personal.xml`, `att.global.responsibility.xml`, `att.global.source.xml`,
`att.editLike.xml`, `att.datable.xml`, `idno.xml`, `place.xml`, `state.xml`,
`P5/Test/testnames.xml`, GitHub issues 337, 2739 and 1414. The raw snapshots
of the three threads are present in the checkout of 2026-09-06; the raw
responses of the SourceForge originals are not, which is why the GitHub
records are the admitted manifestations.

The run was executed on 2026-09-06 through admission, distillation, three
rounds of source review, assertion building with a fresh-context review and
the rewrite of chapter 08; [[knowledge/state]] holds its counts and
[[knowledge/journal]] its outcomes, and the questions it left open stand in
the entity topic map. The human verification sample over both entity runs
remains an operator decision.

### Run 1 of Text and Document Structures

The second topic is Text and Document Structures. In the order of the posits
of chapter 12, the first open evidence questions that no admitted source
addresses are those of the projection posit, the objects posit and the
readings posit, and all three ask how P5 encodes structure, the reading of
a main text apart from its notes, distinct roles over the same characters and
a containment model for crossing or noncontiguous structures. The selection
posit, whose question the topic Annotation and Overlap serves, comes later in
that order and already rests on three admitted specifications, three
admitted publications and the grounded chapter
`40_output/06-annotation-and-overlap.md`. The structure topic has no admitted
P5 specification at all, its map holds two diary assertions, and the single
recorded failure of the candidate, the refused page and foliation holdout in
[[knowledge/experiments]], is a structure phenomenon. Overlap is the bridge
between the two topics, and the run admits P5's own chapter on it; the
stand-off mechanisms are deferred to the annotation run.

| Question | Kind | Origin |
|---|---|---|
| Q1. Which cases require noncontiguous nodes, shared occurrences or another containment model, and how does P5 itself account for structures that cross the tree? | problem claim, a forest of contiguous extents is the first account of structure while P5 has only the tree and its workarounds | posit readings; map question on coupled concepts |
| Q2. Which constructs place a note or an embedded text relative to the main text, so that a reading projection can be checked against them? | coverage | posit projection |
| Q3. Which structural elements keep distinct roles over the same characters, and which content models decide what may contain what? | coverage | posit objects; map question |
| Q4. How does P5 record a page beginning, a folio number and a facsimile pointer, and what does it say about their alignment? | problem claim, the page and foliation distinction is spread over constructs the candidate refused | posit evaluation; Open work |
| Q5. Which mechanisms serve stand-off and range annotation, and which of them belong to the annotation topic? | coverage, a boundary question | posit selection; map question of Annotation and Overlap |
| Q6. Which of the official process's own reconsiderations for P6 concern structure? | coverage | label query |

The streams queried on 2026-09-06, the declared query of every family with
its hit count and the disposition of every hit stand in the
[selection record](../workbench/selections/2026-09-06-text-and-document-structures-run1.md).

Run 1 admits twelve sources, two chapters and two threads among them. They
are `NH-Non-hierarchical.xml`, `DS-DefaultTextStructure.xml`,
`att.fragmentable.xml`, `join.xml`, `att.global.linking.xml`,
`milestone.xml`, `pb.xml`, `div.xml`, `note.xml`, `P5/Test/testoverlap.xml`,
GitHub issues 1505 and 1400. The raw snapshots of both threads are present
in the checkout of 2026-09-06.
