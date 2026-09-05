---
title: Index
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
related: [specification, design, schema, operations, state, journal]
---

# Index

This index connects the project contracts and defines navigation terms.
Human readers start at [[HOME]], Codex at `AGENTS.md`, and Claude Code at
`CLAUDE.md`. The agent adapters route into the same knowledge contracts.
Research claims enter the Grounded Vault layers.

## Reading paths

Read [[knowledge/specification]] for scope and evaluation, then
[[knowledge/state]] for actual holdings and open work. Content production uses
[[knowledge/schema]] and [[knowledge/operations]]. Interface work follows
[[knowledge/design]]. The public workbench opens with the full technical
proposal and connects it to Model, Materials, Knowledge, and About.

| Task | Additional entry points |
|---|---|
| Plan acquisition | `sources/registry.yaml`, `corpus/COMPLETENESS.md`, and `docs/multi-agent-acquisition-runbook.md` |
| Understand repository structure | `ARCHITECTURE.md` |
| Develop or evaluate a P6 design | `docs/p6/README.md`, then `workflows/evaluate-p6-proposal.md` |
| Understand a past decision | [[knowledge/journal]], with newer entries last |

## The seven knowledge documents

| Document | Holds | Changes |
|---|---|---|
| [[knowledge/index]] | navigation, terminology | rarely |
| [[knowledge/specification]] | purpose, parameters, settled decisions | on decisions |
| [[knowledge/design]] | research-workbench information architecture and interface contract | on product decisions |
| [[knowledge/schema]] | layer model, document types, anchor mechanics, audit trail | rarely, by decision |
| [[knowledge/operations]] | acquisition, ingestion, synthesis, query, and checks | rarely, by decision |
| [[knowledge/state]] | source inventory, chapter register, everything volatile | constantly |
| [[knowledge/journal]] | decision history | append-only |

A document is split only when sections need different update rhythms or readers.

The dossier under `docs/p6/` organizes provisional requirements, hypotheses,
and experiment contracts. It is outside the evidence chain and cannot ground
claims about P5 or official TEI policy.

## Terminology

| Term | Meaning in this vault |
|---|---|
| Source | The original file, preserved exactly as received |
| Markdown representation | The stable converted source with block IDs for later citations |
| Distillate | Statements extracted from one source and individually anchored to it |
| Assertion | One source-supported statement grounded in one or more distillate statements |
| Chapter | Output whose factual premises cite assertions and whose own conclusions are marked as posits |
| Source type | A source class defined by its representation, distillation procedure, and grounding anchor |
| Grounding | The structural anchor relation connecting a claim to source locations, without establishing truth |
| Evidence | A grounding relation that has passed human expert verification |
| Provenance chain | The unbroken path from output through assertions and distillates to source locations |
| Audit trail | Dated records of checks that actually ran on the artifact |
| Posit | An authorial conclusion with an explicit rationale and open evidence question |
| Validation | Deterministic checks of artifact structure, anchors, and declared rules |
| Machine review | Adversarial review of whether source passages support their statements |
| Verification | Review by the designated human expert |
| Finding, interpretation, proposal | A source-supported observation, a reasoned account of findings, and a design option, respectively |
| Official P6 process | TEI Council records and artifacts concerning P6, distinct from this project's proposals and not presumed to be a released standard |
| Observable-complete | Every object observable through a registered finite interface during the snapshot interval was retrieved or recorded as a gap |
| Bounded-complete | Every result of a declared finite search, index, or bibliography protocol received a disposition |

Findings can motivate interpretations and proposals without establishing them.
Completion labels describe the recorded boundary, never all material that has
ever existed. The artifact rules remain in [[knowledge/schema]] and the
acquisition vocabulary in `corpus/COMPLETENESS.md`.
