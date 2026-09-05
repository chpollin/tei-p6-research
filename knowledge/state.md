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
updated: "2026-09-05"
related: [design, operations, journal]
---

# State

This file records current holdings, checks and open work. Update it when those
facts change. Stable contracts and historical decisions remain in their own
documents.

## Current checkpoint

| Area | State | Evidence |
|---|---|---|
| Local repository | ready | branch `main`; scaffold and acquisition-runbook commits exist |
| GitHub remote | ready | public `chpollin/tei-p6-research` repository configured as `origin` |
| Promptotyping contract | ready | specification, design, schema, operations, state, journal and index instantiated |
| P5 4.12.0 identity | resolved | full release commit recorded in `sources/locks/tei-p5-4.12.0.yaml` |
| P5 4.12.0 acquisition | partial | pinned Git tree and official release ZIP are complete; the published-HTML boundary still needs an explicit reconciliation against the ZIP before the family label can return to `observable-complete` |
| Public TEIC Git corpus | observable-complete | all 41 repositories exposed by the organization census are mirrored at full HEAD commits; 25,415 tree entries inventoried |
| TEI website records | partial | the website Git repository is inventoried, but the registered page-snapshot boundary has not yet been acquired |
| GitHub work-item corpus | blocked | collector and tests are ready; a read-only authenticated GitHub session is required for exhaustive issues, PRs, comments, reviews, and timelines |
| Governance corpus | partial | 206 Council pages and 225 Board targets observed; inaccessible historical links and external working documents remain explicit gaps |
| Historical TEI Archive | partial | 394 index/page responses acquired; 363 linked non-HTML artifacts are in reconciliation |
| Legacy SourceForge | partial | tracker API boundary observable-complete on 2026-09-05: all 1,349 enumerated bug, feature, and support tickets plus 8,880 discussion posts acquired; release-file and legacy version-control interfaces remain unreconciled |
| Literature corpus | partial | a bounded first reading records four candidates; W3C REC2017, Piez2014 and Renear/Wickett2010 have citation-only admissions; the Renear/Mylonas/Durand author-version full text returned HTTP 403; Zotero/JTEI and full seed census remain open |
| Official P6 process | partial | public `TEIC/timeForP6` history acquired; relevant Council records inventoried; reported `TEIC/p6-sandbox` remains non-public or absent |
| Independent P6 design dossier | bounded Abstract Text Model 0.1 implemented, human acceptance pending | Ten record kinds with formal constraints and five reference operations. JSON, XML and YAML bindings preserve the same model instance. Two real diary fragments have bounded mappings. Full TEI domain coverage, RDF and whole-document P5 conversion remain open. |
| Grounded knowledge | three bounded chapters; source-support reviews passed | five document sources and four citation-only sources have distillates; eleven assertions are `validated`; the three chapters remain `grounded`; six new Humboldt support pairs passed fresh-context review after narrowing one assertion heading; human verification remains open |
| Text identity pilot acceptance | awaiting owner review | nine support pairs passed independent fresh-context review on 2026-09-05 after source-context correction; same-model-family limitation remains; human decisions use the five items in `docs/p6/text-identity-pilot.md` |
| Text identity pilot technical gate | passed on 2026-09-05 | 238 tests passed after first-wave integration; 38 synthetic cases reproduced; full-vault and chapter validation had no errors or warnings; source admission, control-plane integrity and current review hashes passed; generated HTML reproduced byte-for-byte |
| Abstract Text Model 0.1 technical gate | passed on 2026-09-05 | all five reference operations implemented; 68 independently authored cases over 60 models, 38 canonical checks, and two standalone examples pass; deterministic report reproduces; 322 full-suite tests pass; full-vault and chapter 12 validation have no errors or warnings; current source-support audits, four quotation checks, and source control-plane checks pass |
| Abstract Text Model 0.1 review | machine reviews complete; human acceptance open | separate GPT-6 agents authored the implementation and cases; independent ontology and code reviews found no remaining material contract contradiction; positive-only membership, adjacent segments and diagnostic distinctions were clarified; finite synthetic checks do not establish domain adequacy, usability, or P5 migration; five owner-review items are in the model definition |
| Project text and argument review | integrated on 2026-09-05 | three GPT-6 review packages covered the model dossier, pilot argument, and research programme; final readback found no material contradictions in the reviewed model and method texts; these editorial reviews do not establish source support, ontological adequacy, or human acceptance |
| P5 specification atlas | bounded declaration navigation implemented | `corpus/projections/p5-specs-4.12.0.json` inventories 846 specification files, 546 local attributes and 131 local constraints; 57 named-datatype references remain outside declaration lookup; inheritance, Guidelines interpretation and effective ODD compilation remain open |
| First research wave | bounded integration and technical checks complete | four citation-only sources have checked quotations and validated distillates; four validated assertions feed `40_output/06-annotation-and-overlap.md`; eight source-support pairs passed fresh-context review after narrowing one heading; atlas reproduction, quotation checks, chapter and full-vault validation, control-plane checks and 238 tests passed; human verification remains open |
| Proposal for TEI P6 | continuous technical argument integrated | `40_output/12-p6-design.md` links nine grounded premises to thirteen explicit posits and seven comparative examples. Architecture ranking and adoption evidence remain open. |
| Editorial comparison | bounded execution complete | three fragments of one pinned Humboldt diary; two development mappings preserve the declared observations; the frozen candidate refuses the page/foliation holdout and the baseline projection also misses its required prose result; 18 independent synthetic provenance-profile cases pass; CC BY-SA 4.0 attribution and source hashes reconcile; full RNG/ODD conformance and media alignment remain untested |
| Research frontend | implemented and locally checked | The canonical proposal is `docs/index.html`, with `home.html` as a generated alias. Model, Materials, Knowledge and About use the same layout and the same local and published routes. No decorative horizontal rules. The model reference derives its ten classes and seventeen reference fields from the existing contract. Published revisions are identified by the Pages deployment log. |
| Integrated release gate | passed on 2026-09-05 | 902 tests pass. Full-vault validation reports no errors or warnings. Source admissions, current support-review hashes, four quotation checks, the P5 declaration atlas, 68 model cases and the editorial comparison reproduce. Five pages pass desktop and 390-pixel browser checks with keyboard navigation and no page errors. |
| Knowledge navigation | implemented | The browser inventories five source representations, nine distillates, eleven assertions and three chapters. Exact passage links and backreferences follow the immediate-layer chain. Citation-only admissions end at their checked quotation and citation. |
| Materials navigation | implemented | Sixteen primary source families and a separate literature view describe locked holdings and gaps. The page does not enumerate every raw object or imply complete acquisition. |

## Program phases

| Phase | Status | Exit condition |
|---|---|---|
| M0 Project contract and scaffold | complete | agent layers, Promptotyping documents, validation and acquisition contract present |
| M1 Collector implementation | complete | Git, GitHub, bounded-web, SourceForge, release-asset, and ZIP-inventory collectors pass offline tests |
| M2 Corpus bootstrap | in progress | source-family manifests reconcile and declare completion or explicit gaps |
| M3 P5 formal model | in progress | direct-declaration atlas implemented; effective ODD-derived model and prose relations must still rebuild from the pinned baseline |
| M4 Vertical grounding pilots | in progress | the bounded text-identity chapter traverses the chain; full normative-model coverage and the governance/release and official-P6 pilots remain open |
| M5 Topic-scale P5 analysis | planned | central findings and counterevidence are grounded across the controlled topics |
| M6 P6 option evaluation | in progress | bounded candidate and conceptual primary-tree-plus-stand-off comparison exist; comparable real workflows, implemented alternatives, and migration evidence remain open |

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
| TEI P5 4.12.0 span specification | document | collection | [[10_markdown/documents/tei-p5-span-4.12.0]] | [[20_distillates/documents/tei-p5-span-4.12.0]] | distilled |
| timeForP6 repository README at pinned commit eb924226 | document | collection | [[10_markdown/documents/tei-time-for-p6-readme-2026-07-16]] | [[20_distillates/documents/tei-time-for-p6-readme-2026-07-16]] | distilled |
| <span>should be generalised to support discontinuous spans | publication | import | — | [[20_distillates/publications/tei-sourceforge-fr363]] | distilled |
| Hierarchies within range space: From LMNL to OHCO | publication | import | — | [[20_distillates/publications/piez2014range]] | distilled |
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
| Metadata and Entities | `40_output/08-metadata-and-entities.md` | planned | Scope topic: Metadata and Entities. |
| History and Governance | `40_output/09-history-and-governance.md` | planned | Scope topic: History and Governance. |
| Issues and Decisions | `40_output/10-issues-and-decisions.md` | planned | Scope topic: Issues and Decisions. |
| Interoperability and Processing | `40_output/11-interoperability-and-processing.md` | planned | Scope topic: Interoperability and Processing. |
| P6 Design | `40_output/12-p6-design.md` | grounded | Bounded Abstract Text Model 0.1 proposal with nine grounded premises and thirteen explicit posits. Validated structurally on 2026-09-05. Architecture and adoption verdicts remain open. |

## Open work

<!-- Short, current list; done items are deleted, decisions go to the journal. -->

- Authenticate GitHub read access and complete the observable-complete issue,
  pull-request, comment, review, and timeline bootstrap.
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
  `docs/p6/editorial-case-study.md` with independently selected editions and
  domain reviewers. Test annotation review after actual editing and measure
  preservation, authoring, query, and teaching costs on comparable tasks.
- Review Abstract Text Model 0.1 using the five accept/revise/defer items in
  `docs/p6/abstract-text-model-v0.1.md`. Challenge the independently authored
  synthetic requirements with real editorial cases, including negative identity
  claims, noncontiguous structural nodes, and nontextual entities or media.
- Extend and measure the two bounded comparison implementations before ranking
  architectures. Resolve the observed page/foliation limitation through a new
  declared study, preserving the frozen holdout result; add full-document P5
  mappings, preservation/loss reports, and adoption costs.
- Extend the direct-declaration atlas with inherited/effective ODD semantics and
  source-linked prose interpretation before treating it as the formal P5 model.
- Assign the human verification role before any artifact can enter `verified` status.
