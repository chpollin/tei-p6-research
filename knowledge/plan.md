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
updated: "2026-09-06"
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
the next two topics. The procedure text carries no figures. The tables of
the two runs are dated snapshots of the streams and of the atlas, and their
counts hold for the named manifests only.

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

This plan holds the selection table of a run at planning time. The chapter
register row of the chapter the run serves names the run, the count of
admitted sources and the table that selected them, and the checkpoint row of
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

Snapshot of 2026-09-06. The atlas is the projection of commit
`113e933e21f016e2655518321e9d10214b8d9fcb`, the GitHub stream is the run
`sources/manifests/2026-09-06-github-teic-tei-work-items.yaml`, the
SourceForge stream the run `sources/manifests/2026-09-06-tei-legacy-sourceforge-r4.yaml`,
the TEI-L stream the run `sources/manifests/2026-09-06-tei-l-psu.yaml`, and
the literature seeds the lock `sources/locks/literature.yaml` with the
pinned bibliography.

| Family | Declared query | Hits |
|---|---|---|
| atlas, membership | `classes_declared` names `att.naming` | 31 records, among them `att.personal`, `rs`, `geogName`, `country`, `settlement`, `region`, `district`, `bloc`, `state`, `trait`, `event`, `birth`, `death`, `author`, `editor` |
| atlas, membership | `att.canonical` | 31 records, among them `att.naming`, `relation`, `faith`, `object`, `date`, `title`, `bibl`, `author`, `term` |
| atlas, membership | `att.datable` | 74 records, among them `place`, `org`, `person`, `state`, `trait`, `event`, `idno`, `persName`, `placeName`, `name` |
| atlas, membership | `att.editLike` | 53 records, among them `persName`, `name`, `placeName`, `orgName`, `place`, `org`, `person`, `state`, `trait`, `event` |
| atlas, attribute | records declaring `key` | 10, `att.canonical` and nine ODD reference elements |
| atlas, attribute | `ref` | 3, `att.canonical`, `dataRef`, `g` |
| atlas, attribute | `nymRef` | 1, `att.naming` |
| atlas, attribute | `role` | 7, `att.naming`, `person`, `org`, `personGrp`, `persona`, `address`, `att.tableDecoration` |
| atlas, attribute | `cert`, `resp`, `evidence`, `source` | 2, 2, 2, 1; `cert` and `resp` in `att.global.responsibility`, `evidence` in `att.editLike`, `source` in `att.global.source`, all three classes reached through `att.global` |
| atlas, ident | `att.personal`, `att.global.responsibility`, `att.editLike`, `att.global.source`, `att.datable`, `att.datable.w3c`, `idno`, `place`, `org`, `trait`, `state`, `event`, `placeName`, `orgName` | 14, all present; `persName`, `placeName`, `orgName`, `name` and the name components declare `att.personal` and reach `att.naming` and `att.canonical` through it |
| chapters | `CE-CertaintyResponsibility.xml`, `HD-Header.xml`, `CO-CoreElements.xml` | 3 files |
| tests | `P5/Test/testnames.xml`, `names-demo-en.xml`, `testplace.xml`, `testnym.odd` | 4 files |
| GitHub, A1 | `att\.canonical\|att\.naming\|nymRef` | 19 |
| GitHub, A2 | `persName\|placeName\|orgName\|\brs\b\|geogName\|roleName\|surname\|forename\|addName\|genName\|nameLink\|<name>\|name element\|@type on name` | 24 |
| GitHub, A3 | `\bkey\b\|@ref\b` | 20 |
| GitHub, A4 | `prosopograph\|personograph\|listPerson\|listPlace\|listOrg\|<person>\|<place>\|<org>\|\bpersona\b\|personGrp\|\bidno\b\|linked data\|authority file\|\bURIs?\b` | 62 |
| GitHub, A5 | `\btrait\b\|\bstate\b\|\bevent\b\|\brelation\b\|listRelation\|\bnym\b\|listNym\|@cert\|@resp\|@evidence\|@source\|att\.datable\|att\.editLike\|att\.global\.responsibility\|responsibility` | 88 |
| GitHub, label | `Status: Reconsider for P6` | 17 |
| SourceForge, A1 to A5 | the same expressions on `summary` | 10, 12, 9, 34, 50; every hit maps to a GitHub record of the same title and date except support request 4 |
| TEI-L | `persName\|persongrp\|surname\|placeName\|orgName\|\bname\b\|\bidno\b\|traits of places\|authority\|prosopograph\|linked\|author` on `subject` | 9 threads, 38 messages, months 2512 to 2608 |
| literature | lock records; bibliography prefix `ND-`; title terms `name\|prosopograph\|onomast\|authority\|person\|place\|linked data\|entity\|identif` | 4 lock records, none on the topic; 1 entry with the prefix; 3 title hits |

The selection. A SourceForge original is named in the row of its GitHub
record with its status.

| Source | Family | Exact query or ident | Disposition | Reason |
|---|---|---|---|---|
| `P5/Source/Specs/att.personal.xml` | P5 specification | ident `att.personal`; declares `att.naming`; declared by `persName`, `placeName`, `orgName`, `name`, `objectName`, `surname`, `forename`, `addName`, `genName`, `roleName` | admit | Q1, the class through which the naming elements reach `att.naming` and `att.canonical`; `persName` and `placeName` declare neither class directly |
| `P5/Source/Specs/att.global.responsibility.xml` | P5 specification | ident; attribute lookup `cert`, `resp`; reached through `att.global` | admit, C | Q6, `cert` and `resp` are global at the pinned release, so every naming element carries them; this is the counterevidence query for the claim that identification names no agent or certainty |
| `P5/Source/Specs/att.global.source.xml` | P5 specification | ident; attribute lookup `source`; reached through `att.global` | admit, C | Q6, a source pointer is global at the pinned release |
| `P5/Source/Specs/att.editLike.xml` | P5 specification | ident; attributes `evidence`, `instant`; declared by the naming elements and the records | admit | Q5 and Q6, the class that carries `evidence` and `instant` to names and records |
| `P5/Source/Specs/att.datable.xml` | P5 specification | ident; attribute `period`; pulls `att.datable.w3c`, `att.datable.iso`, `att.datable.custom`; declared by `place`, `org`, `state`, `trait`, `event`, `idno` | admit, C | Q5, the time frame for statements about places and organizations; `place` and `org` are members at the pinned release, which answers the reading that the requirement holds for them |
| `P5/Source/Specs/idno.xml` | P5 specification | ident; declares `model.personPart`, `model.nameLike`, `att.datable`, `att.typed`, `att.sortable` | admit | Q4 and Q7, the specification's own statement of purpose and its availability inside `person` |
| `P5/Source/Specs/place.xml` | P5 specification | ident; declares `att.datable`, `att.editLike`, `att.sortable`, `att.typed`, `model.placeLike` | admit | Q3, the place record's description and remarks |
| `P5/Source/Specs/state.xml` | P5 specification | ident; declares `att.naming`, `att.datable`, `att.editLike`, `model.persStateLike`, `model.orgStateLike`, `model.placeStateLike` | admit | Q5 and Q7, a statement element that is itself a member of `att.naming`, so `key`, `ref` and `role` recur inside statements about persons, organizations and places |
| `P5/Test/testnames.xml` | encoded practice | file name; counts at the pinned commit `persName` 165, `placeName` 139, `person` 137, `key` 144, `role` 117, `ref` 11, `nym` 11 | admit | Q2, the release's own test document identifies mentions by `key`, places roles on mentions and uses nyms; rights follow the release with the per-file review recorded in the manifest |
| GitHub issue 337 (SourceForge feature request 336, `closed`) | work item | A3; created 2011-11-13, closed 2015-10-02, 21 comments, `Type: FeatureRequest`, `Status: Go`, `sf-automigrated` | admit, C | Q8, the thread that proposed a soft deprecation of `key` in favour of `ref`; `key` is still declared on `att.canonical` at the pinned release, so the released effect is at most the remarks text the chapter grounds in, which the thread has to establish |
| GitHub issue 2739 | work item | A1; created 2025-08-04, closed 2025-08-06, 4 comments | admit | Q1, reports an ODD error in the chain `att.personal`, `att.naming`, `att.canonical` before the pinned release; its outcome is checked against the admitted class blobs |
| GitHub issue 1414 | work item | A1; created 2015-12-15, closed 2019-07-15, 16 comments, `Type: FeatureRequest`, `Status: Go`, `TEI: Schema` | admit, C | Q7, the proposal to put the record elements themselves into `att.canonical`; at the pinned release `object` is a member and `person`, `place` and `org` are not, so the trail from proposal to released effect tests the claim that records link outward through `idno` only |
| `org.xml`, `trait.xml`, `event.xml`, `placeName.xml`, `orgName.xml`, `att.datable.w3c.xml` | P5 specification | ident | defer, budget | Q3 and Q5 in the next run; `place` and `state` stand for the record and the statement kinds in this run |
| `P5/Test/testplace.xml` (`placeName` 70, `place` 34, `ref` 12, `key` 9, `cert` 2, `resp` 2), `names-demo-en.xml` (`role` 117, `key` 1), `testnym.odd` (`nym` 15, `nymRef` 3) | encoded practice | file name and counts | defer, budget | `testplace.xml` in the next run for Q3 and Q6, records with `cert` and `resp`; `testnym.odd` for the nym question |
| `CE-CertaintyResponsibility.xml`, `HD-Header.xml`, `CO-CoreElements.xml` | chapter | file | defer, budget | CE for Q6 in the next run; HD and CO exceed the chapter budget beside CE and are entered through their specifications first |
| GitHub 290 (SourceForge feature request 289, `open-accepted`) | work item | A1; closed 2016-09-26, 12 comments, `Status: Blocked` | defer, budget, C | Q7, the proposal to give the trait and state elements `att.canonical`; at the pinned release `trait` and `state` are members of `att.naming`, so the effect exists and its trail is the next run's |
| GitHub 338 (SourceForge feature request 337, `closed-accepted`), 462 (feature request 462, `closed-fixed`), 158, 219, 698, 1424, 1442, 1480, 1481, 1685, 2071, pull request 2630 | work item | A4 | defer, budget, C for 338 | Q4, `idno` as the external reference of a record; the specification is admitted first and the threads follow |
| GitHub 444 (SourceForge feature request 443, `closed-fixed`), 536 (feature request 536), 465, 490, 509 (feature request 509, `closed-fixed`), 166, 191, 196, 240, 560, 681, 766, 1003, 1204, 1242, pull request 1352, 1368, 1631, 1668, 2158 | work item | A5, A2 | defer, budget, C for 444, 536 and 509 | Q6, the threads that made `resp`, `cert` and `source` global and allowed `cert` on `rs`; the admitted classes carry the released state, the trails follow |
| GitHub 367 (SourceForge feature request 366, `open`) | work item | label; closed 2025-09-14, 27 comments, `Status: Reconsider for P6` | defer, budget | Q3, the official process's own reconsideration of the content models of `org`, `place` and `person`; first thread of the next run |
| GitHub 843 (SourceForge bug 168), 1041, 1248, 1340, 518, 519, 1310, 616, 1723, 1756, 2382, pull request 2427, 2466, pull request 2483, 2499, 2523, 2524, 2699, 2827, pull request 2882 | work item | A5, A2, A4 | defer, budget, C for 843 | Q5, `trait`, `state` and `event` and their datability; the thread on state against trait is the counterevidence query for the extension of the requirement |
| GitHub 504 (SourceForge feature request 504, `closed-wont-fix`), 467, 495, 567, 640, 1183, 1262, 1314, 1552 | work item | A5 | defer, budget, C for 504 | the relation participants; the declined proposal to replace `active` and `passive` by `from` and `to` is the counterevidence query for the contested participant pair |
| GitHub 2451 with pull request 2881, 2389 with pull request 2952, 88, 210, 298, 299, 513, 608, 909, 1042, 1241, 1244, 1410, 1689, 1986, 1992, 2045, 2257, 2432, 2887 | work item | A5, A2 | defer, budget, C for 2451 | the class scope of `att.datable` and `att.editLike`; 2881 merged on 2026-05-04 gives `place` and `org` the class at the pinned release, 2952 merged on 2026-08-18 after the release, so `rs` is datable on the development branch only |
| GitHub 58 (SourceForge feature request 57), 125 (feature request 124), 1035 (bug 391, `closed-accepted`), 238 (feature request 245, `closed-accepted`), 623 (bug 27, `closed-accepted`), 781, 1531, 1684, 1695 | work item | A2, A1 | defer, budget, C for 1035 and 623 | Q1 and Q2, `role` and `type` on mentions, and the deliberate exclusion of `nameLink` from `key` and `ref` |
| GitHub 129, 130, 131, 146, 187, 206, 246, 625, 1521, 1525, 1659, 1775, 1821, 2392 with pull request 2655, 2687 | work item | A1, A3 | defer, budget | the growth of `att.canonical` and `att.naming` beyond names, to `author`, `title`, `editor`, `term`, `faith`, `actor`, `publisher`, `bibl`, `material` and `date`; which representations carry identification |
| GitHub 2, 69, 73, 183, 321, 322, 498, 627, 635, 638, 794, 1128, 1772, pull request 1974, 2011, 2016, 2180, 2296, 2475, 2595, 2651, 2745, 2890 with pull request 2891 | work item | A4 | defer, budget | the record elements, their lists and their roles; 2 is the origin of the module for the history topic, 2745 and 498 are leads on the identity of a person against a persona |
| GitHub 535 (SourceForge feature request 535, `closed-fixed`), 474, 1334 | work item | A3 | defer, lead | the Guidelines' own move of examples from `key` to `ref` |
| GitHub 696 (SourceForge bug 110, `closed-fixed`), 2150 | work item | A1, A5 | defer, lead | the description of `nymRef` and the definition of `listNym` as standardized, the latter open |
| GitHub 1400, 1508 | work item | label | defer, another topic's run | structure, see run 1 of Text and Document Structures below |
| GitHub 2843, 2893, 2894, 2957 | work item | label | defer, another topic's run | the class system and attribute naming for P6, for Elements and Classes and P6 Design |
| GitHub 1175, 1744, 1923, 2000, 2013, 2090, 2146, 2373, 2744, 2875 | work item | label | defer, another topic's run | ODD, apparatus, header and documentation topics |
| TEI-L threads persName or personGrp (8 messages, month 2607), surname (4, 2607), traits of places, persons, etc. in a linked fashion (1, 2512) | TEI-L | subject query | defer, prerequisite missing | bodies in the raw store only, no rights review, Penn State months only; the traits thread is a lead for Q6 |
| bibliography entry `github-mix-mix` | literature | title terms | defer, prerequisite missing | a project personography, a lead for encoded practice that needs the sampling protocol |
| GitHub 2738 | work item | A1 | reject, typography | a typo |
| GitHub 405, 485, 609, 1597, 1623, 1656, 1692, 1842, 2297 | work item | A2 | reject, outside the topic or example repair | whitespace, content models of other elements, schema tooling, example quality |
| GitHub 867, 903, 953, 1606, 1724, pull request 1742, pull request 1817, 2062, 2726, 2850, pull request 2852 | work item | A3 | reject, homonym | `key` of ODD references and datatypes |
| GitHub 68, 116, 217, 310, 339, 344, 348, 376, 385, 440, 1088, 1294, pull request 1443, 1989, 2198, 2345 | work item | A4 | reject, outside the topic | bibliographic and manuscript identifiers |
| GitHub 847, 959, 1232, 1446, 1592 | work item | A4 | reject, homonym | URI as namespace or stylesheet matter |
| GitHub 316, 424, 432, 745, 782, 883, 950, 961, 963, 1111, 1127, 1463, 1593, 1604, 1649, 1916, 2588, 2591, pull request 2692 | work item | A5 | reject, homonym | `state`, `source`, `relation`, `event` and `nym` in other senses, and the technical limit on nym parts |
| SourceForge support request 4 | ticket | A4 | reject, outside the topic | a support question of 2004 without a proposal |
| TEI-L threads idno for TEI (9 and 3 messages, 2602), author for AI-generated texts (7, 3 and 1, 2605), different shares of authorship (2, 2608) | TEI-L | subject query | reject, outside the topic | header identifiers and statements of responsibility |
| bibliography entries `ND-eg-99`, `fr-ex-Corneille_Place-Royale`, `DS-eg-05` | literature | prefix and title terms | reject, homonym | example sources of the Guidelines without a claim about the topic |
| lock records | literature | lock | no hit | the four records of wave one concern annotation and identity; the Journal of the TEI and Zotero seeds remain the recorded gap |

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

Snapshot of 2026-09-06 over the same manifests, atlas and lock as run 2.

| Family | Declared query | Hits |
|---|---|---|
| atlas, membership | `att.fragmentable` | 6, `ab`, `l`, `p`, `post`, `att.divLike`, `att.segLike` |
| atlas, membership | `att.breaking` | 5, `cb`, `gb`, `lb`, `milestone`, `pb` |
| atlas, membership | `att.divLike` | 10, `div`, `div1` to `div7`, `lg`, `spGrp` |
| atlas, membership | `att.spanning` | 14, among them `pb`, `lb`, `cb`, `gb`, `milestone`, `addSpan`, `delSpan`, `metamark` |
| atlas, membership | `att.placement` | 17, among them `div`, `note`, `head`, `fw`, `figure`, `att.transcriptional` |
| atlas, membership | `att.written` | 29, among them `div`, `p`, `ab`, `head`, `note`, `line`, `zone`, `text` |
| atlas, attribute | `part`, `break`, `facs`, `next`, `prev`, `spanTo`, `place` | 1 each, in `att.fragmentable`, `att.breaking`, `att.global.facs`, `att.global.linking` for both `next` and `prev`, `att.spanning`, `att.placement` |
| atlas, attribute | `target` | 13, among them `att.pointing`, `annotation`, `alt`, `metamark`, `change` |
| atlas, ident | `div`, `p`, `ab`, `seg`, `head`, `note`, `pb`, `lb`, `milestone`, `fw`, `join`, `att.fragmentable`, `att.breaking`, `att.global.linking`, `att.global.facs`, `text`, `body`, `floatingText`, `sourceDoc`, `surface`, `zone`, `line`, `facsimile` | 23, all present; `ab` has the content `macro.abContent`, `facsimile` admits a nested `facsimile` |
| chapters | `NH-Non-hierarchical.xml`, `DS-DefaultTextStructure.xml`, `SA-LinkingSegmentationAlignment.xml`, `PH-PrimarySources.xml`, `CO-CoreElements.xml` | 5 files |
| tests | `P5/Test/testoverlap.xml`, `testfrag.xml`, `testtranscr.xml`, `testtranscr2.xml`, `testtranscr4.xml`, `torture.xml` | 6 files; `testoverlap.xml` holds `p` 9 and `pb` 4 |
| GitHub, B1 | `overlap\|hierarch\|concurrent\|OHCO` | 5 |
| GitHub, B2 | `milestone\|\bpb\b\|\blb\b\|\bcb\b\|\bgb\b\|page ?break\|line ?break\|column ?break\|\bfw\b\|foliation\|att\.breaking\|@break` | 29 |
| GitHub, B3 | `fragmentable\|@part\b\|\bjoin\b\|joinGrp\|discontinu\|@next\|@prev\|aggregat` | 8 |
| GitHub, B4 | `stand-?off\|listAnnotation\|\bannotation\b\|\bspan\b\|spanGrp\|\banchor\b\|att\.spanning\|spanTo\|xpointer\|@target` | 48 |
| GitHub, B5 | `floatingText\|sourceDoc\|\bzone\b\|\bsurface\b\|<line>\|facsimile\|@facs\|embedded transcription\|documentary\|genetic` | 46 |
| GitHub, B6 | `<div>\|<ab>\|<seg>\|<p>\|<head>\|<body>\|<text>\|<group>\|<front>\|<back>\|<note>\|att\.divLike\|content model of div\|\bstructures?\b` | 50 |
| GitHub, label | `Status: Reconsider for P6` | 17, dispositions in run 2 except 1400 and 1508 |
| SourceForge, B1 to B6 | the same expressions on `summary` | 3, 19, 3, 19, 20, 27; every hit maps to a GitHub record of the same title and date |
| TEI-L | `overlap\|hierarch\|structure\|page\|milestone\|stand-?off\|interlinear\|support\|\bdiv\b\|\bp\b\|\bseg\b\|\bnote\b\|facsimile\|zone\|surface\|dictionary-entries\|damage` on `subject` | 8 threads, 55 messages, months 2512 to 2608 |
| literature | lock records; bibliography prefixes `NH-`, `DS-`, `SA-`, `PH-`, `AI-`; title terms `overlap\|hierarch\|structure\|stand-?off\|markup\|OHCO\|document\|milestone\|LMNL\|annotation` | 3 admitted and 1 unavailable lock record; 10, 6, 5, 20 and 7 prefixed entries; 15 title hits |

The selection.

| Source | Family | Exact query or ident | Disposition | Reason |
|---|---|---|---|---|
| `P5/Source/Guidelines/en/NH-Non-hierarchical.xml` | chapter | file at the pinned commit | admit, C | Q1, P5's own account of the problem and of its strategies, boundary marking, fragmentation with reconstitution and stand-off; the chapter names the cases the readings posit asks for and is the counterevidence query for the claim that P5 has only the tree |
| `P5/Source/Guidelines/en/DS-DefaultTextStructure.xml` | chapter | file at the pinned commit | admit | Q2 and Q3, divisions numbered and unnumbered, prose and anonymous blocks, heads, floating texts, front and back |
| `P5/Source/Specs/att.fragmentable.xml` | P5 specification | ident; attribute lookup `part`; declared by `ab`, `l`, `p`, `post`, `att.divLike`, `att.segLike` | admit, C | Q1, the declared way to mark a fragment of a virtual element; `p` is a member at the pinned release, the released effect of issue 399 |
| `P5/Source/Specs/join.xml` | P5 specification | ident; attributes `result`, `scope`; declares `att.pointing`, `model.global.meta` | admit | Q1, the reconstitution of a virtual element from fragments |
| `P5/Source/Specs/att.global.linking.xml` | P5 specification | ident; attributes `corresp`, `synch`, `sameAs`, `copyOf`, `next`, `prev`, `exclude`, `select`; reached by every element through `att.global` | admit | Q1, `next` and `prev` as the aggregation attributes and `exclude` and `select` as alternation |
| `P5/Source/Specs/milestone.xml` | P5 specification | ident; declares `att.breaking`, `att.spanning`, `att.milestoneUnit`, `att.edition`, `model.milestoneLike` | admit | Q1 and Q4, boundary marking by an empty element, with `spanTo` as the bridge to a range |
| `P5/Source/Specs/pb.xml` | P5 specification | ident; declares `att.breaking`, `att.spanning`, `att.edition`, `model.milestoneLike` | admit, C | Q4, the page beginning of the holdout case; `facs` reaches it through `att.global` |
| `P5/Source/Specs/div.xml` | P5 specification | ident; declares `att.divLike`, `att.placement`, `att.written`, `att.declaring`, `model.divLike`; two constraints | admit | Q3, the structural division and its containment constraints; `att.divLike` brings `part` |
| `P5/Source/Specs/note.xml` | P5 specification | ident; declares `att.placement`, `att.anchoring`, `att.pointing`, `att.written`, `model.noteLike` | admit | Q2, where a note stands relative to the text, through `place`, anchoring and `targetEnd`, for the reading projection |
| `P5/Test/testoverlap.xml` | encoded practice | file name; counts `p` 9, `pb` 4 | admit | Q1 and Q4, the release's own test of paragraphs crossed by page beginnings |
| GitHub issue 1505 | work item | B3; created 2016-09-22, closed 2017-05-03, 14 comments, `Type: Bug`, `Status: Go`, `TEI: Guidelines & Documentation`, `TEI: Schema` | admit, C | Q1, the clarification of `next` and `prev` against `join` with `scope`, `result` and `exclude`; its released effect is read in the admitted specifications and in the NH chapter |
| GitHub issue 1400 | work item | label; created 2015-11-10, open, 20 comments, `Type: FeatureRequest`, `Status: Reconsider for P6` | admit | Q3 and Q6, the official process's own reconsideration of numbered divisions |
| `att.spanning.xml`, `att.breaking.xml`, `att.divLike.xml`, `att.placement.xml`, `seg.xml`, `p.xml`, `ab.xml`, `head.xml`, `floatingText.xml`, `text.xml`, `body.xml`, `fw.xml`, `att.global.facs.xml` | P5 specification | ident | defer, budget | Q2, Q3 and Q4 in the next run; `milestone` and `pb` carry the breaking and spanning classes into this run through membership |
| `sourceDoc.xml`, `surface.xml`, `zone.xml`, `line.xml`, `facsimile.xml` with `PH-PrimarySources.xml` | P5 specification and chapter | ident, file | defer, budget | the documentary view and the carrier, a run of their own because PH exceeds the chapter budget beside NH and DS |
| `SA-LinkingSegmentationAlignment.xml`, `CO-CoreElements.xml` | chapter | file | defer, budget | SA holds the aggregation and segmentation prose the specifications point to, CO the milestone prose; both are entered through their specifications in this run |
| `P5/Test/testfrag.xml`, `testtranscr.xml`, `testtranscr2.xml`, `testtranscr4.xml`, `torture.xml` | encoded practice | file name | defer, lead | the file names suggest fragmentation and transcription tests; their counts are taken in the next run |
| GitHub 1856 | work item | B6; created 2019-02-18, closed 2022-10-20, 59 comments | defer, budget, C | Q3, whether `ab` may nest; at the pinned release the content of `ab` is `macro.abContent`, where the outcome is read |
| GitHub 399 (SourceForge feature request 397, `closed-accepted`), 1227, 1750, 2756 | work item | B3 | defer, budget, C for 399 | `part` on `p` and other components, released; `q` as fragmentable still open in 2025 |
| GitHub 2367 with pull request 2633 (merged 2025-01-14), 641 (SourceForge bug 40), 678 (bug 78), 760 (bug 87), 1156 (bug 519), 1529, 269 (feature request 268, `closed-fixed`), 200 (feature request 199), 325 (feature request 324, closed 2025-09-14), 108 (feature request 107), 128, 164, 190, 266, 707, 879, 1660, 1677 | work item | B2 | defer, budget, C for 2367, 760 and 641 | Q4, the typographic line beginning against the topographic line, the consistency of `pb`, `lb`, `cb` and `gb`, foliation and `facs` on `pb`; 1660 declined the renaming of `lb` |
| GitHub 34 (SourceForge feature request 33), 253, 166, 681, 335, 391, 394, 479, 1466, 2551, 435, 452, 701, 1051, 1169, 1939, 2089, 2460, 2711, 1957 with pull request 1983 | work item | B6 | defer, budget, C for 2551 | Q2 and Q3, the placement of notes and heads and the content models of divisions, front and back; `div` is a member of `att.placement` at the pinned release, the released effect of 2551 |
| GitHub 64 (SourceForge feature request 63), 261 (feature request 260, `closed-accepted`), 264 (feature request 261, `closed-later`), 1578, 2607 | work item | B5, B6 | defer, lead | the floating embedded text, from its origin to a report that names an abstract model violation |
| GitHub 258 (SourceForge feature request 257, `closed-accepted`), 259, 98, 113, 204, 213, 278, 456, 515, 541, 1453, 1493, 1508, 1515, 1838, 2148, 2300 with pull request 2360, 2363, pull request 2449, 2476, 2565 with pull request 2654, 2737 | work item | B5 | defer, budget | the documentary run of the topic; the genetic origin of `sourceDoc`, `surface`, `zone` and `line`, the restriction of embedded transcription, the coordinate system and the nesting of `facsimile`; 1508 carries the P6 label |
| GitHub 1691 | work item | B1 | defer, lead | `said` and `q` in the context of overlapping hierarchies, open |
| GitHub 374 (SourceForge feature request 378, `open`), 61 comments, with pull request 2018 (merged 2020-08-17), 51, 168 (feature request 167), 197, 208, 279, 355 (feature request 354), 389, 1049, 1186, 1624, 1626, 1658, pull request 1665, 1666, 1676, 1745, 1779, 1976, 1977, 2048, 2246 with pull request 2662, 2436 with pull request 2555, pull request 2448, 2474, 2530, pull request 2767, 2941 | work item | B4 | defer, another topic's run | Q5, the stand-off and range mechanisms belong to the run of Annotation and Overlap, which starts from 374 and 2018; 1049 and 2767 were declined |
| GitHub 364 (SourceForge feature request 363) | work item | B3, B4 | already admitted | the migrated copy of the feature request admitted in wave one as `tei-sourceforge-fr363` |
| GitHub 503, 1552 | work item | B6 | defer, another topic's run | the content models of `person` and the placement of `listRelation`, for run 2 of Metadata and Entities |
| GitHub 1312 | work item | B6 | defer, another topic's run | conformance wording that singles out `text`, for P5 Architecture |
| TEI-L threads interlinear variation (8 messages, month 2512), tei structure question (7, 2512), different page sizes but one support element (9, 2608) | TEI-L | subject query | defer, prerequisite missing | bodies in the raw store only, no rights review, Penn State months only; leads for Q1, Q3 and Q4 |
| bibliography entries `NH-BIBL-1`, `NH-BIBL-3`, `NH-BIBL-4`, `NH-BIBL-5`, `NH-BIBL-6`, `NH-BIBL-7`, `NH-BIBL-8` | literature | prefix `NH-` | defer, prerequisite missing | the literature the NH chapter cites on overlap, concurrent markup and layered markup; enters through the literature protocol with per-item rights, the review article first |
| GitHub 470, 629 (SourceForge bug 33), 1139, 1876 | work item | B1 | reject, homonym or typography | overlap of attribute classes, and a typo in the multiple-hierarchy examples |
| GitHub 10, 301, 450, 2164, 874, 1222, 1432, 1995, 2241 with pull request 2288 | work item | B2 | reject, outside the topic or tooling and typography | witnesses, dictionaries and geographic features, a stylesheet defect, translations, a typo and release milestones |
| GitHub 1382, 1919 | work item | B3 | reject, typography or outside the topic | markup of a mention and the content of `joinGrp` |
| GitHub 104, 178, 222, 919, 1106, 1118, 1205, 1211, 1367, 1383, 1469, 1620, pull request 1732, 1852, 2145, 2883 | work item | B4 | reject, outside the topic or tooling and typography | `target` on manuscript, bibliographic and apparatus elements, stylesheet defects and example repairs |
| GitHub 177, 729, 741, 758, 1047, 1206, 1363, 1364, 1758, 1767, pull request 2039, 2043, 2414, 2637, 2747 | work item | B5 | reject, outside the topic or tooling and typography | audio facsimile, stylesheet defects, wording, translations, build tooling and example requests |
| GitHub 548, 571, 572, 770, 956, 1108, 1151, 1164, 1207, 1514, 1542, 1641, pull request 1701, 1967, 2147, 2149, pull request 2151, 2719, pull request 2731, 2889 | work item | B6 | reject, outside the topic or tooling and typography | the header, verse and manuscript description, linguistic markup, ODD, stylesheets and example repairs |
| TEI-L threads att.typed and the p element (19 and 2 messages, 2512), nested dictionary-entries (4, 2512), question about the use of damage (2, 2512), describing menu structures in TEI (4, 2601) | TEI-L | subject query | reject, outside the topic | attribute classes, dictionaries, transcription phenomena and a modelling question without structure content |
| bibliography entries with `-eg-` and `-ib` in their identifier under the five prefixes, `SA-BIBL-2`, `PH-BIBL-1`, `AI-BIBL-1` to `AI-BIBL-7` | literature | prefixes and title terms | reject, homonym or outside the topic | example sources and editions the Guidelines cite for illustration, and corpus linguistics |
| lock records `piez2014range`, `w3c-web-annotation-20170223`, `renear-wickett2010documents` | literature | lock | already admitted | wave one; `renear-mylonas-durand-ohco-author1993` stays unavailable |

Run 1 admits twelve sources, two chapters and two threads among them. They
are `NH-Non-hierarchical.xml`, `DS-DefaultTextStructure.xml`,
`att.fragmentable.xml`, `join.xml`, `att.global.linking.xml`,
`milestone.xml`, `pb.xml`, `div.xml`, `note.xml`, `P5/Test/testoverlap.xml`,
GitHub issues 1505 and 1400. The raw snapshots of both threads are present
in the checkout of 2026-09-06.
