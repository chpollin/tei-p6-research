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

Everything volatile in one place, so the rule documents stay stable. Update rows here as work proceeds; never record processing state anywhere else.

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
| Literature corpus | planned | bounded seeds registered; no completed harvest or disposition report |
| Official P6 process | partial | public `TEIC/timeForP6` history acquired; relevant Council records inventoried; reported `TEIC/p6-sandbox` remains non-public or absent |
| Independent P6 design dossier | conceptual scaffold | design contracts exist under `docs/p6/`; no executable metamodel, binding, converter, fixture corpus or conformance result yet |
| Grounded knowledge | pilot begun | one official-P6-process source has an immutable representation and one-source distillate; no assertions or chapters exist |
| Research frontend | published | `docs/corpus.html` is a generated, read-only inventory governed by `knowledge/design.md` and published at `https://chpollin.github.io/tei-p6-research/` through GitHub Pages |

## Program phases

| Phase | Status | Exit condition |
|---|---|---|
| M0 Project contract and scaffold | complete | agent layers, Promptotyping documents, validation and acquisition contract present |
| M1 Collector implementation | complete | Git, GitHub, bounded-web, SourceForge, release-asset, and ZIP-inventory collectors pass offline tests |
| M2 Corpus bootstrap | in progress | source-family manifests reconcile and declare completion or explicit gaps |
| M3 P5 formal model | planned | ODD-derived model rebuilds deterministically from the pinned baseline |
| M4 Vertical grounding pilots | planned | three end-to-end chains pass validation and adversarial review |
| M5 Topic-scale P5 analysis | planned | central findings and counterevidence are grounded across the controlled topics |
| M6 P6 option evaluation | planned | alternatives and migration evidence are compared under the shared criteria |

## Source inventory

One row per source. Processing status: `new` → `ingested` → `distilled`. This section is generated from the real file state by `python tools/inventory.py . --write` and is never edited by hand; everything between the two markers is overwritten on each run.

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
| timeForP6 repository README at pinned commit eb924226 | document | collection | [[10_markdown/documents/tei-time-for-p6-readme-2026-07-16]] | [[20_distillates/documents/tei-time-for-p6-readme-2026-07-16]] | distilled |
<!-- inventory:end -->

## Chapter register

One row per chapter of the output. Writing status mirrors the chapter's frontmatter.

| Chapter | File | Status | Notes |
|---|---|---|---|
| P5 Architecture | `40_output/01-p5-architecture.md` | planned | Scope topic: P5 Architecture. |
| Abstract Model | `40_output/02-abstract-model.md` | planned | Scope topic: Abstract Model. |
| ODD and Customization | `40_output/03-odd-and-customization.md` | planned | Scope topic: ODD and Customization. |
| Elements and Classes | `40_output/04-elements-and-classes.md` | planned | Scope topic: Elements and Classes. |
| Text and Document Structures | `40_output/05-text-and-document-structures.md` | planned | Scope topic: Text and Document Structures. |
| Annotation and Overlap | `40_output/06-annotation-and-overlap.md` | planned | Scope topic: Annotation and Overlap. |
| Critical Apparatus | `40_output/07-critical-apparatus.md` | planned | Scope topic: Critical Apparatus. |
| Metadata and Entities | `40_output/08-metadata-and-entities.md` | planned | Scope topic: Metadata and Entities. |
| History and Governance | `40_output/09-history-and-governance.md` | planned | Scope topic: History and Governance. |
| Issues and Decisions | `40_output/10-issues-and-decisions.md` | planned | Scope topic: Issues and Decisions. |
| Interoperability and Processing | `40_output/11-interoperability-and-processing.md` | planned | Scope topic: Interoperability and Processing. |
| P6 Design | `40_output/12-p6-design.md` | planned | Scope topic: P6 Design. |

## Open work

<!-- Short, current list; done items are deleted, decisions go to the journal. -->

- Authenticate GitHub read access and complete the observable-complete issue,
  pull-request, comment, review, and timeline bootstrap.
- Reconcile the remaining Archive, SourceForge release-file and legacy
  version-control, external Council, and community-interface gaps.
- Resolve the P5 published-HTML and website-snapshot coverage exceptions before relying on their family-level `observable-complete` labels.
- Reconcile `planned`, `not_started`, and blocked acquisition language with the completion vocabulary.
- Complete three vertical production cycles before topic-scale source admission.
- Define a sampling and rights protocol for real-world ODD customizations and migration cases.
- Assign the human verification role before any artifact can enter `verified` status.
