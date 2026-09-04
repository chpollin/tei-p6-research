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

- Complete one full first production cycle before scaling source ingestion.
- Assign the human verification role before any artifact can enter `verified` status.
- Materialize and inventory the pinned TEI P5 4.12.0 release tree.
- Authenticate GitHub read access before the observable-complete issue and PR bootstrap.
