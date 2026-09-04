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
