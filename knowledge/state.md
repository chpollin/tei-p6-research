---
title: State
project:
  name: "TEI P6 Research Vault"
  repository: "tei-p6"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-04"
related: [operations, journal]
---

# State

Everything volatile in one place, so the rule documents stay stable. Update rows here as work proceeds; never record processing state anywhere else.

## Current checkpoint

| Area | State | Evidence |
|---|---|---|
| Local repository | ready | branch `main`; scaffold and acquisition-runbook commits exist |
| GitHub remote | blocked | no remote configured; owner and visibility not yet settled |
| Promptotyping contract | ready | specification, schema, operations, state, journal and index instantiated |
| P5 4.12.0 identity | resolved | full release commit recorded in `sources/locks/tei-p5-4.12.0.yaml` |
| P5 4.12.0 acquisition | observable-complete | pinned Git tree has 1,965 entries; official 333,504,131-byte release ZIP matches the upstream SHA-256 and contains 15,211 CRC-verified files |
| Public TEIC Git corpus | observable-complete | all 41 repositories exposed by the organization census are mirrored at full HEAD commits; 25,415 tree entries inventoried |
| GitHub work-item corpus | blocked | collector and tests are ready; a read-only authenticated GitHub session is required for exhaustive issues, PRs, comments, reviews, and timelines |
| Governance corpus | partial | 206 Council pages and 225 Board targets observed; inaccessible historical links and external working documents remain explicit gaps |
| Historical TEI Archive | partial | 394 index/page responses acquired; 363 linked non-HTML artifacts are in reconciliation |
| Legacy SourceForge | partial | 1,349 bug, feature, and support ticket IDs enumerated; 1,226 tickets and 7,925 discussion posts acquired; 123 ticket fetches await a rate-limit-safe continuation |
| Literature corpus | planned | bounded seeds registered; no completed harvest or disposition report |
| Official P6 process | partial | public `TEIC/timeForP6` history acquired; relevant Council records inventoried; reported `TEIC/p6-sandbox` remains non-public or absent |
| Independent P6 design dossier | conceptual scaffold | design contracts exist under `docs/p6/`; no executable metamodel, binding, converter, fixture corpus or conformance result yet |
| Grounded knowledge | empty | topic MOCs exist; no production representations, distillates, assertions or chapters |

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
<!-- inventory:end -->

## Chapter register

One row per chapter of the output. Writing status mirrors the chapter's frontmatter.

| Chapter | File | Status | Notes |
|---|---|---|---|
| P5-Architektur | `40_output/01-p5-architektur.md` | planned | Scope topic: P5 Architecture. |
| Abstraktes Modell | `40_output/02-abstraktes-modell.md` | planned | Scope topic: Abstract Model. |
| ODD und Customization | `40_output/03-odd-und-customization.md` | planned | Scope topic: ODD and Customization. |
| Elemente und Klassen | `40_output/04-elemente-und-klassen.md` | planned | Scope topic: Elements and Classes. |
| Text- und Dokumentstrukturen | `40_output/05-text-und-dokumentstrukturen.md` | planned | Scope topic: Text and Document Structures. |
| Annotation und Überlappung | `40_output/06-annotation-und-ueberlappung.md` | planned | Scope topic: Annotation and Overlap. |
| Kritischer Apparat | `40_output/07-kritischer-apparat.md` | planned | Scope topic: Critical Apparatus. |
| Metadaten und Entitäten | `40_output/08-metadaten-und-entitaeten.md` | planned | Scope topic: Metadata and Entities. |
| Geschichte und Governance | `40_output/09-geschichte-und-governance.md` | planned | Scope topic: History and Governance. |
| Issues und Entscheidungen | `40_output/10-issues-und-entscheidungen.md` | planned | Scope topic: Issues and Decisions. |
| Interoperabilität und Verarbeitung | `40_output/11-interoperabilitaet-und-verarbeitung.md` | planned | Scope topic: Interoperability and Processing. |
| P6-Design | `40_output/12-p6-design.md` | planned | Scope topic: P6 Design. |

## Open work

<!-- Short, current list; done items are deleted, decisions go to the journal. -->

- Confirm GitHub owner and repository visibility, then configure the remote.
- Authenticate GitHub read access before the observable-complete issue and PR bootstrap.
- Complete the authenticated GitHub work-item bootstrap after `gh auth login`.
- Reconcile the remaining Archive, SourceForge, external Council, and community-interface gaps.
- Complete three vertical production cycles before topic-scale source admission.
- Define a sampling and rights protocol for real-world ODD customizations and migration cases.
- Assign the human verification role before any artifact can enter `verified` status.
