---
title: Journal
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
