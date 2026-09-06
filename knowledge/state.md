---
title: State
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
related: [INDEX, plan, handoff, operations, journal]
---

# State

This file records current holdings, checks and open work. Update it when those
facts change. Stable contracts and historical decisions remain in their own
documents, the milestones in [[knowledge/plan]] and open handoff points in
[[knowledge/handoff]].

## Current checkpoint

| Area | State | Evidence |
|---|---|---|
| Local repository | ready | branch `main`; scaffold, collector, workbench and repair commits exist |
| GitHub remote | ready | public `chpollin/tei-p6-research` repository configured as `origin` |
| Knowledge base | restructured on 2026-09-06 | every knowledge document lives in `knowledge/` under the Promptotyping convention with `INDEX.md` as hub; `PLAN.md`, `EXPOSE.md`, `ARCHITECTURE.md`, `contexts/`, `workflows/`, the concept, runbook, corpus-profile, primary-source and completeness documents and `docs/p6/research-agenda.md` were absorbed and deleted; the case-only rename of `knowledge/index.md` to `knowledge/INDEX.md` still has to be recorded in Git and the About page regenerated |
| P5 4.12.0 identity | resolved | full release commit recorded in `sources/locks/tei-p5-4.12.0.yaml` |
| P5 4.12.0 acquisition | partial | pinned Git tree and official release ZIP are complete; the TEIC/TEI mirror was re-acquired locally on 2026-09-06 (`sources/manifests/2026-09-06-teic-tei-p5-4.12.0-r2.yaml`, tag `P5_Release_4.12.0` resolves to the locked commit); the published-HTML boundary still needs an explicit reconciliation against the ZIP before the family label can return to `observable-complete` |
| Public TEIC Git corpus | observable-complete | all 41 repositories exposed by the organization census are mirrored at full HEAD commits; 25,415 tree entries inventoried |
| TEI-L mailing-list archive | partial | Penn State archive `bounded-complete` for December 2025 to September 2026 on 2026-09-06 (267 messages, metadata only, no sender fields); Wayback coverage of the retired Brown archive measured for all 432 months from 1990 to 2025 (368 captured, 64 missing, each missing month recorded as a gap); the fetch of captured months through the Wayback Machine and the export request to the TEI Consortium remain open |
| TEI website records | partial | the website Git repository is inventoried, but the registered page-snapshot boundary has not yet been acquired |
| GitHub work-item corpus | partial | both stages ran on 2026-09-06 under the authenticated session: the REST snapshot (2,476 issues, 455 pull requests, 19,565 issue comments, 1,258 reviews, 1,259 review comments, 74,981 timeline events) and the GraphQL relations stage (16,003 relations and 674 review threads over all 2,931 items, no gap, 253 rate-limit points); the boundary is complete in substance, while the family label stays `partial` because the recorded REST manifest still names the relations stage as its gap, which the next REST snapshot removes; bodies stay in the private raw store |
| Governance corpus | partial | 206 Council pages and 225 Board targets observed; inaccessible historical links and external working documents remain explicit gaps |
| Historical TEI Archive | partial | 394 index/page responses acquired; 363 linked non-HTML artifacts are in reconciliation |
| Legacy SourceForge | partial | tracker API boundary `observable-complete` on 2026-09-06 under adapter version 2: the 1,349 tickets and 8,880 discussion posts of the 2026-09-05 run reconcile against the tracker-reported counts (774 bugs, 567 feature requests, 8 support requests) in `sources/manifests/2026-09-06-tei-legacy-sourceforge-r4.yaml`; the raw responses of the earlier runs are not in this checkout; release-file and legacy version-control interfaces remain unreconciled |
| Literature corpus | partial | a bounded first reading records four candidates; W3C REC2017, Piez2014 and Renear/Wickett2010 have citation-only admissions; the Renear/Mylonas/Durand author-version full text returned HTTP 403; Zotero/JTEI and full seed census remain open |
| Official P6 process | partial | public `TEIC/timeForP6` history acquired; relevant Council records inventoried; reported `TEIC/p6-sandbox` remains non-public or absent |
| Independent P6 design knowledge | bounded Abstract Text Model 0.1 implemented, human acceptance pending | Ten record kinds with formal constraints and five reference operations. JSON, XML and YAML bindings preserve the same model instance. Two real diary fragments have bounded mappings. Full TEI domain coverage, RDF and whole-document P5 conversion remain open. |
| Grounded knowledge | four bounded chapters; entity run reviewed | fourteen document sources and four citation-only sources have distillates; the nine entity distillates of 2026-09-06 are `validated` after fresh-context review under a different model (101 source pairs, all passing after two reformulation rounds); forty-six assertions carry a passing machine review, of which forty-two are `validated` and four stay `contested` as recorded disagreements between the Guidelines chapter and the class specifications; the four chapters are `grounded`; human verification remains open |
| Text identity pilot acceptance | awaiting owner review | nine support pairs passed independent fresh-context review on 2026-09-05 after source-context correction; same-model-family limitation remains; human decisions use the five items in `knowledge/experiments.md` |
| Text identity pilot technical gate | passed on 2026-09-05 | 238 tests passed after first-wave integration; 38 synthetic cases reproduced; full-vault and chapter validation had no errors or warnings; source admission, control-plane integrity and current review hashes passed; generated HTML reproduced byte-for-byte |
| Entity extension 0.2 | drafted and implemented, human acceptance pending | section 14 of the text model defines entity, name, denotation, statement and alignment records on the claim pattern; the validator, two reference operations and a deterministic runner pass all fifty-eight independently authored cases and thirty-three canonical checks; four readings the text left open were settled and written back; a one-way RDF export in `tools/models/rdf_binding.py` preserves every record and reference edge under the identifier policy and is documented in `knowledge/text-model-rdf-binding.md`; five owner-review items stand in section 14.6 |
| Abstract Text Model 0.1 technical gate | passed on 2026-09-05 | all five reference operations implemented; 68 independently authored cases over 60 models, 38 canonical checks, and two standalone examples pass; deterministic report reproduces; 322 full-suite tests pass; full-vault and chapter 12 validation have no errors or warnings; current source-support audits, four quotation checks, and source control-plane checks pass |
| Abstract Text Model 0.1 review | machine reviews complete; human acceptance open | separate GPT-6 agents authored the implementation and cases; independent ontology and code reviews found no remaining material contract contradiction; positive-only membership, adjacent segments and diagnostic distinctions were clarified; finite synthetic checks do not establish domain adequacy, usability, or P5 migration; five owner-review items are in the model definition |
| Project text and argument review | integrated on 2026-09-05 | three GPT-6 review packages covered the model dossier, pilot argument, and research programme; final readback found no material contradictions in the reviewed model and method texts; these editorial reviews do not establish source support, ontological adequacy, or human acceptance |
| P5 specification atlas | bounded declaration navigation implemented | `corpus/projections/p5-specs-4.12.0.json` inventories 846 specification files, 546 local attributes and 131 local constraints; 57 named-datatype references remain outside declaration lookup; inheritance, Guidelines interpretation and effective ODD compilation remain open |
| First research wave | bounded integration and technical checks complete | four citation-only sources have checked quotations and validated distillates; four validated assertions feed `40_output/06-annotation-and-overlap.md`; eight source-support pairs passed fresh-context review after narrowing one heading; atlas reproduction, quotation checks, chapter and full-vault validation, control-plane checks and 238 tests passed; human verification remains open |
| Proposal for TEI P6 | continuous technical argument integrated | `40_output/12-p6-design.md` links nine grounded premises to thirteen explicit posits and seven comparative examples. Architecture ranking and adoption evidence remain open. |
| Editorial comparison | bounded execution complete | three fragments of one pinned Humboldt diary; two development mappings preserve the declared observations; the frozen candidate refuses the page/foliation holdout and the baseline projection also misses its required prose result; 18 independent synthetic provenance-profile cases pass; CC BY-SA 4.0 attribution and source hashes reconcile; full RNG/ODD conformance and media alignment remain untested |
| Research frontend | implemented and locally checked | The canonical proposal is `docs/index.html`. Model, Materials, Knowledge and About use the same layout and the same local and published routes. No decorative horizontal rules. The model reference derives its ten classes and seventeen reference fields from the existing contract. Published revisions are identified by the Pages deployment log. |
| Integrated release gate | passed on 2026-09-06 | 1,109 tests pass and ruff reports no finding. Full-vault validation reports no errors or warnings. Source admissions, current support-review hashes, 68 model cases and the editorial comparison reproduce; all five pages reproduce byte-for-byte from their recorded build date. The P5 declaration atlas and the four quotation checks need the local raw corpus, which this checkout does not hold. The 2026-09-05 browser checks were not repeated. |
| Knowledge navigation | implemented | The browser inventories five source representations, nine distillates, eleven assertions and three chapters. Exact passage links and backreferences follow the immediate-layer chain. Citation-only admissions end at their checked quotation and citation. |
| Materials navigation | implemented | Sixteen primary source families and a separate literature view describe locked holdings and gaps. The page does not enumerate every raw object or imply complete acquisition. |

## Milestones

The milestones and their exit conditions are defined in [[knowledge/plan]].

| Milestone | Status | Position |
|---|---|---|
| 1. Tools and gates repaired | complete | commit `1cfdb2e` on 2026-09-06 |
| 2. Knowledge base restructured | complete | commit `021b633` on 2026-09-06; every knowledge document lives in `knowledge/` with one function |
| 3. Vault structures | complete | commit `82bce81` on 2026-09-06; topic maps and glossary example lists are generated regions, phenomena are glossary entries, `phenomena` and `related` are validated |
| 4. Foundation closed | in progress | the exhaustive GitHub REST run, the SourceForge reconciliation, the local P5 mirror, the Penn State TEI-L months and the Wayback coverage measurement are done (commits `2a481dc`, `0ac8964`); the Wayback fetch of the Brown archive runs, and the GraphQL relations stage, the archive and website reconciliation, the export request to the Consortium and the sampling protocol remain open |
| 5. Claim pattern and IRI policy | complete | commit `0419968` on 2026-09-06; section 13 of the text model fixes the claim record, the IRI grammar and the alignment field |
| 6. Entity run and topic cycles | in progress | the first selection-driven vertical cycle ran on the topic Metadata and Entities (commit `0ac8964`): nine sources, nine validated distillates, thirty-five reviewed assertions, chapter 08 grounded; the next topics follow the order of the posits of chapter 12 |
| 7. Model extended phenomenon by phenomenon | in progress | the entity extension of section 14 is drafted, implemented in `tools/models/entities.py` and checked against fifty-eight independently authored cases on 2026-09-06; the coverage matrix names what stays uncovered; real cases from distinct editions, the RDF binding and the five acceptance items remain open |
| 8. Proposal from assertions | in progress | chapter 12 links nine validated premises to thirteen posits; counter-reader review, option ranking, migration prototype and dated official-P6 comparison remain open |
| 9. Publication | planned | no human verification sample recorded |

## Source inventory

The inventory is generated by `python tools/inventory.py . --write` and is never
edited by hand. Processing follows `new` → `ingested` → `distilled`. Each run
replaces the region between the markers with the actual file state.

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
| edition humboldt digital: England travel diary H0017682 | document | collection | [[10_markdown/documents/humboldt-h0017682-7d174637]] | [[20_distillates/documents/humboldt-h0017682-7d174637]] | distilled |
| TEI P5 4.12.0 anchor specification | document | collection | [[10_markdown/documents/tei-p5-anchor-4.12.0]] | [[20_distillates/documents/tei-p5-anchor-4.12.0]] | distilled |
| TEI P5 4.12.0 annotation specification | document | collection | [[10_markdown/documents/tei-p5-annotation-4.12.0]] | [[20_distillates/documents/tei-p5-annotation-4.12.0]] | distilled |
| TEI P5 4.12.0 att.canonical specification | document | collection | [[10_markdown/documents/tei-p5-att.canonical-4.12.0]] | [[20_distillates/documents/tei-p5-att.canonical-4.12.0]] | distilled |
| TEI P5 4.12.0 att.datable specification | document | collection | [[10_markdown/documents/tei-p5-att.datable-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.editLike specification | document | collection | [[10_markdown/documents/tei-p5-att.editlike-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.responsibility specification | document | collection | [[10_markdown/documents/tei-p5-att.global.responsibility-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.global.source specification | document | collection | [[10_markdown/documents/tei-p5-att.global.source-4.12.0]] | — | ingested |
| TEI P5 4.12.0 att.naming specification | document | collection | [[10_markdown/documents/tei-p5-att.naming-4.12.0]] | [[20_distillates/documents/tei-p5-att.naming-4.12.0]] | distilled |
| TEI P5 4.12.0 att.personal specification | document | collection | [[10_markdown/documents/tei-p5-att.personal-4.12.0]] | — | ingested |
| TEI P5 4.12.0 Guidelines chapter Names, Dates, People, and Places | document | collection | [[10_markdown/documents/tei-p5-guidelines-nd-4.12.0]] | [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0]] | distilled |
| TEI P5 4.12.0 idno specification | document | collection | [[10_markdown/documents/tei-p5-idno-4.12.0]] | — | ingested |
| TEI P5 4.12.0 name specification | document | collection | [[10_markdown/documents/tei-p5-name-4.12.0]] | [[20_distillates/documents/tei-p5-name-4.12.0]] | distilled |
| TEI P5 4.12.0 nym specification | document | collection | [[10_markdown/documents/tei-p5-nym-4.12.0]] | [[20_distillates/documents/tei-p5-nym-4.12.0]] | distilled |
| TEI P5 4.12.0 persName specification | document | collection | [[10_markdown/documents/tei-p5-persname-4.12.0]] | [[20_distillates/documents/tei-p5-persname-4.12.0]] | distilled |
| TEI P5 4.12.0 person specification | document | collection | [[10_markdown/documents/tei-p5-person-4.12.0]] | [[20_distillates/documents/tei-p5-person-4.12.0]] | distilled |
| TEI P5 4.12.0 place specification | document | collection | [[10_markdown/documents/tei-p5-place-4.12.0]] | — | ingested |
| TEI P5 4.12.0 relation specification | document | collection | [[10_markdown/documents/tei-p5-relation-4.12.0]] | [[20_distillates/documents/tei-p5-relation-4.12.0]] | distilled |
| TEI P5 4.12.0 rs specification | document | collection | [[10_markdown/documents/tei-p5-rs-4.12.0]] | [[20_distillates/documents/tei-p5-rs-4.12.0]] | distilled |
| TEI P5 4.12.0 span specification | document | collection | [[10_markdown/documents/tei-p5-span-4.12.0]] | [[20_distillates/documents/tei-p5-span-4.12.0]] | distilled |
| TEI P5 4.12.0 state specification | document | collection | [[10_markdown/documents/tei-p5-state-4.12.0]] | — | ingested |
| TEI P5 4.12.0 test document testnames.xml | document | collection | [[10_markdown/documents/tei-p5-test-testnames-4.12.0]] | — | ingested |
| timeForP6 repository README at pinned commit eb924226 | document | collection | [[10_markdown/documents/tei-time-for-p6-readme-2026-07-16]] | [[20_distillates/documents/tei-time-for-p6-readme-2026-07-16]] | distilled |
| <span>should be generalised to support discontinuous spans | publication | import | — | [[20_distillates/publications/tei-sourceforge-fr363]] | distilled |
| att.personal, att.naming, and att.canonical: Error in ODD? | publication | import | — | — | new |
| Hierarchies within range space: From LMNL to OHCO | publication | import | — | [[20_distillates/publications/piez2014range]] | distilled |
| ogrophy elements should be in att.canonical | publication | import | — | — | new |
| soft deprecation of @key | publication | import | — | — | new |
| There are No Documents | publication | import | — | [[20_distillates/publications/renear-wickett2010documents]] | distilled |
| Web Annotation Data Model | publication | import | — | [[20_distillates/publications/w3c-web-annotation-20170223]] | distilled |
<!-- inventory:end -->

## Chapter register

One row per chapter of the output. Writing status mirrors the chapter's frontmatter.

| Chapter | File | Status | Notes |
|---|---|---|---|
| P5 Architecture | `40_output/01-p5-architecture.md` | planned | Scope topic: P5 Architecture. |
| Abstract Model | `40_output/02-abstract-model.md` | grounded | Bounded text identity and annotation pilot; four grounded P5 statements and four explicit model posits; human acceptance pending. |
| ODD and Customization | `40_output/03-odd-and-customization.md` | planned | Scope topic: ODD and Customization. |
| Elements and Classes | `40_output/04-elements-and-classes.md` | planned | Scope topic: Elements and Classes. |
| Text and Document Structures | `40_output/05-text-and-document-structures.md` | planned | Scope topic: Text and Document Structures. |
| Annotation and Overlap | `40_output/06-annotation-and-overlap.md` | grounded | First synthesis: five grounded premises and four explicit proposed tests; source-support review and owner review remain distinct. |
| Critical Apparatus | `40_output/07-critical-apparatus.md` | planned | Scope topic: Critical Apparatus. |
| Metadata and Entities | `40_output/08-metadata-and-entities.md` | grounded | First topic-scale synthesis from thirty-five assertions over nine entity sources; thirteen explicit posits connect the findings to the record kinds of the claim pattern; human verification and encoded practice remain open. |
| History and Governance | `40_output/09-history-and-governance.md` | planned | Scope topic: History and Governance. |
| Issues and Decisions | `40_output/10-issues-and-decisions.md` | planned | Scope topic: Issues and Decisions. |
| Interoperability and Processing | `40_output/11-interoperability-and-processing.md` | planned | Scope topic: Interoperability and Processing. |
| P6 Design | `40_output/12-p6-design.md` | grounded | Bounded Abstract Text Model 0.1 proposal with nine grounded premises and thirteen explicit posits. Validated structurally on 2026-09-05. Architecture and adoption verdicts remain open. |

## Open work

<!-- Short, current list; done items are deleted, decisions go to the journal. -->

- Run the exhaustive TEIC/TEI issue, pull-request, comment, review, and
  timeline collection under the authenticated session, then implement the
  GraphQL relations stage so the family can leave `partial`.
- Re-run the SourceForge tracker collection under adapter version 2 so the
  tracker boundary is reconciled against tracker-reported counts.
- Fetch the 368 Wayback-captured months of the Brown TEI-L archive through the
  Wayback Machine and request an export from the TEI Consortium for the 64
  months without capture.
- Take the next REST snapshot of `TEIC/TEI` under the two-stage collector so
  the recorded manifests carry no stage gap and the family can leave `partial`.
- Draw the stratified human verification sample over the entity run (nine
  distillates, thirty-five assertions, chapter 08) and record the quota.
- Close the evidence gaps of the entity run: admit the class specifications
  that carry `key`, `ref`, `nymRef` and `role` to the naming elements, select
  encoded practice and the GitHub threads on `att.canonical`, and settle what
  applies when a local key and a URI are both available.
- Reconcile the remaining Archive, SourceForge release-file and legacy
  version-control, external Council, and community-interface gaps.
- Resolve the P5 published-HTML and website-snapshot coverage exceptions before relying on their family-level `observable-complete` labels.
- Reconcile `planned`, `not_started`, and blocked acquisition language with the completion vocabulary.
- Complete three vertical production cycles before topic-scale source admission.
- Review the bounded text identity pilot using its five acceptance questions;
  record a separate accept/revise/defer decision for each item. Synthetic
  success is not proof of ontological adequacy, real-world usability, or P5
  migratability.
- Extend the three-fragment, single-diary comparison in
  `knowledge/experiments.md` with independently selected editions and
  domain reviewers. Test annotation review after actual editing and measure
  preservation, authoring, query, and teaching costs on comparable tasks.
- Review Abstract Text Model 0.1 using the five accept/revise/defer items in
  `knowledge/text-model.md`. Challenge the independently authored
  synthetic requirements with real editorial cases, including negative identity
  claims, noncontiguous structural nodes, and nontextual entities or media.
- Extend and measure the two bounded comparison implementations before ranking
  architectures. Resolve the observed page/foliation limitation through a new
  declared study, preserving the frozen holdout result; add full-document P5
  mappings, preservation/loss reports, and adoption costs.
- Extend the direct-declaration atlas with inherited/effective ODD semantics and
  source-linked prose interpretation before treating it as the formal P5 model.
- Assign the human verification role before any artifact can enter `verified` status.
- Record the case-only rename of `knowledge/index.md` to `knowledge/INDEX.md` in
  Git and regenerate all five pages after both restructuring packages land.
