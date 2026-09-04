---
title: Specification
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
related: [index, schema, operations]
---

# Specification

Purpose, parameters and settled decisions of this vault instance. The invariant architecture (layer model, anchor mechanics, check contracts, status progression) lives in [[knowledge/schema]] and [[knowledge/operations]]; this document holds what this project decided.

## Purpose

This vault studies the architecture, historical development, governance, and operational behaviour of TEI P5 and develops a grounded design for a possible next generation of TEI. It produces a provenance-complete scholarly synthesis and design specification for researchers, scholarly editors, standards maintainers, and tool builders: every load-bearing claim must resolve through an assertion and distillate to a source passage, verified quotation, or reproducible computation, while findings, interpretations, and proposals remain explicitly distinct.

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | P5 Architecture; Abstract Model; ODD and Customization; Elements and Classes; Text and Document Structures; Annotation and Overlap; Critical Apparatus; Metadata and Entities; History and Governance; Issues and Decisions; Interoperability and Processing; P6 Design |
| Active source types | document, publication, data |
| Output genre | scholarly synthesis and design specification |
| Chapter register | see [[knowledge/state]] |
| Working language of content | German; English TEI identifiers remain unchanged |
| Verification role | project owner or explicitly designated TEI domain expert; no human verifier is assigned yet |
| Validation mechanism | `tools/validate.py` |
| Machine review mechanism | adversarial review by a separate agent or model context under anti-anchoring; the result is recorded as machine review and never treated as human verification |

## Style sheet

Output uses precise German scholarly and technical prose. English TEI element names, attribute names, class identifiers, module identifiers, ODD identifiers, and other canonical identifiers remain unchanged. Every load-bearing statement carries the provenance link required by [[knowledge/schema]], and references name the relevant TEI release or exact upstream revision whenever the claim is version-sensitive. Findings (*Befund*), interpretations (*Interpretation*), and proposals (*Vorschlag*) are separated by structure or explicit sentence-level signalling; none may silently stand in for another. Quotations remain verbatim and visibly distinguished from paraphrase. No machine judgment is described as human verification.

## Settled decisions

- 2026-09-04: Vault instantiated as the TEI P6 Research Vault in the provisional `tei-p6` repository.
- 2026-09-04: The controlled topic set comprises twelve P5-analysis and P6-design topics, each represented by one topic map.
- 2026-09-04: All three source types are active; the output is a German scholarly synthesis and design specification.
- 2026-09-04: Human verification is reserved for the project owner or an explicitly designated TEI domain expert; no verifier is currently assigned.
- 2026-09-04: Separate-context adversarial review may establish machine review only and can never establish human verification.
