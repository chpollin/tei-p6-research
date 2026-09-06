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
| 6. Entity run and topic cycles | Metadata and Entities is the first selection-driven vertical cycle, with sources selected from projections, admitted, distilled, synthesized into validated assertions and written into a grounded chapter, and the remaining topics follow in the order set by the posits of chapter 12 | every central P5 problem claim has evidence, counterevidence or an explicit open-evidence status, and three vertical pilots traverse the full chain under independent review | `python tools/validate.py . --chapter 40_output/<slug>` per chapter and the review-only checks |
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
