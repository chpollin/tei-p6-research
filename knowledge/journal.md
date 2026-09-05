---
title: Journal
project:
  name: "TEI P6 Research Vault"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-05"
related: [specification, state]
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
documentation or concise status help, while open gaps appear as short German
work items linked to their complete control records.

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
