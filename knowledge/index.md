---
title: Index
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
related: [specification, design, schema, operations, state, journal]
---

# Index

Navigation and terminology of the vault. Human readers start at [[HOME]]. Codex
starts at `AGENTS.md`; Claude Code starts at `CLAUDE.md`. Both action layers
route into this same declarative knowledge system.

Together, the seven files in `knowledge/` are the Promptotyping document of the
project: specification describes what is being attempted, design governs the
public research workbench, schema defines the artifacts, operations defines the
executable method, state records present reality, journal preserves decisions,
and this index connects them. Research claims do not live here; they enter the
Grounded Vault production layers.

## Reading paths

- **Understand the project**: [[knowledge/specification]] for problem,
  questions, scope, evaluation dimensions and success criteria, then
  [[knowledge/state]] for where work stands.
- **Produce or check content**: [[knowledge/schema]] for what a well-formed artifact is, [[knowledge/operations]] for the chain that produces it.
- **Understand a past decision**: [[knowledge/journal]], append-only, newest last.
- **Design or change the research workbench**: [[knowledge/design]] for the
  information architecture, content placement, interaction, accessibility,
  provenance, generation, and publication contract.
- **Plan acquisition**: `sources/registry.yaml`, `corpus/COMPLETENESS.md`, and
  `docs/multi-agent-acquisition-runbook.md` after the project contract.
- **Understand the repository system**: `ARCHITECTURE.md` for planes, data
  flows, authority, and trust boundaries.
- **Develop or evaluate a P6 design**: `docs/p6/README.md` for the provisional
  design dossier, then `workflows/evaluate-p6-proposal.md` for the grounded
  comparison procedure.

## The seven knowledge documents

| Document | Holds | Changes |
|---|---|---|
| [[knowledge/index]] | navigation, terminology | rarely |
| [[knowledge/specification]] | purpose, parameters, settled decisions | on decisions |
| [[knowledge/design]] | research-workbench information architecture and interface contract | on product decisions |
| [[knowledge/schema]] | layer model, document types, anchor mechanics, audit trail | rarely, by decision |
| [[knowledge/operations]] | the chains: acquire, ingest, distill, assertions, chapters, query, check | rarely, by decision |
| [[knowledge/state]] | source inventory, chapter register, everything volatile | constantly |
| [[knowledge/journal]] | decision history | append-only |

A document is split only when its sections develop divergent update rhythms or divergent readers.

The P6 architecture documents under `docs/p6/` are outside these seven control documents
and outside the evidence chain. They organize provisional requirements,
hypotheses, experiment contracts, and open research questions. They may not be
used as evidence for P5 behavior or official TEI policy.

## Terminology

- **Source**: The original file exactly as it arrived, kept untouched so that every later form of its content can be checked against it.
- **Markdown representation**: The uniform Markdown form of a source, produced once by converting the original and given block IDs so that later layers anchor into passages that never change afterwards.
- **Distillate**: The set of single statements extracted from one source, each anchored to the passage of the representation it was taken from.
- **Assertion**: A single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement.
- **Chapter**: An output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit.
- **Source type**: a class of sources defined by its Markdown representation, its distillation operation and its grounding anchor.
- **Grounding**: the anchor relation between an assertion and its source locations. A structural property an agent can produce; it says nothing about whether the statement is true.
- **Evidence**: a grounding relation that has passed human expert verification. Relational and deliberately rare; a fresh vault contains grounding, evidence arises only through review.
- **Provenance chain**: the unbroken anchor path from an output sentence through assertions and distillates to source locations. A break anywhere is a defect that validation detects.
- **Audit trail**: the principle that status fields record outcomes of checks that actually ran, each with its date on the checked document.
- **Posit**: a conclusion in the output without source support, explicitly marked with its rationale and open evidence question.
- **Validation / machine review / verification**: the three checking instances, deterministic, adversarial-probabilistic, human. Note that this assignment inverts the IEEE convention; here establishing truth is a human act.
- **Finding / interpretation / proposal**: respectively a source-supported
  observation, an explicitly reasoned reading of findings, and a design option.
  One may motivate the next but never silently becomes it.
- **Official P6 process**: TEI Council discussions, decisions, experiments and
  artifacts explicitly concerning P6. These are primary process records but
  are not identical with this independent vault's proposals and are not assumed
  to constitute a released standard.
- **Observable-complete**: every object publicly observable through the
  registered finite interface during the declared snapshot interval was
  retrieved or recorded as a gap. It does not mean everything that ever
  existed.
- **Bounded-complete**: every result of a declared finite search, index, or
  bibliography protocol received a recorded disposition.
