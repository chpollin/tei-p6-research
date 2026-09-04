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
