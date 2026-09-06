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
updated: "2026-09-06"
related: [project, specification, data, methodology, architecture, design, schema, operations, verification, testing, governance, plan, handoff, journal, state]
---

# Index

This index is the hub of the knowledge base. Every durably maintained
knowledge document of the project lives in `knowledge/`, each with one
function, and every rule of the project has exactly one home among them.
Human readers start at [[HOME]], Codex at `AGENTS.md` and Claude Code at
`CLAUDE.md`. The two adapters route into the same documents. Research claims
themselves enter the Grounded Vault layers defined in [[knowledge/schema]].

## Reading order

Read [[knowledge/project]] for the charter, then [[knowledge/specification]]
for deliverables, criteria and gates, then [[knowledge/state]] for the actual
holdings and open work. A task then follows the narrowest route in the table
below. [[knowledge/governance]] binds every session, [[knowledge/testing]]
closes every change, and [[knowledge/journal]] explains a settled choice when
its reason matters.

## Documents

| Document | Function | Routing question |
|---|---|---|
| [[knowledge/INDEX]] | hub, terminology, folder map | Where does a document or folder belong, and what does a term mean here? |
| [[knowledge/project]] | charter | What does the project ask, what does it deliver, and what lies outside its scope? |
| [[knowledge/specification]] | requirements | Which evaluation dimensions, constraints, deliverables, success criteria and gates bind the work? |
| [[knowledge/data]] | material | Which sources exist, how are they identified, what may be stored and cited, and what does complete mean? |
| [[knowledge/methodology]] | method rationale | Why is the knowledge organized as a Grounded Vault, and what does each check establish? |
| [[knowledge/architecture]] | system structure | Which planes, folders and generated products make up the repository, and who owns them? |
| [[knowledge/design]] | workbench contract | How does the public site present proposal, model, materials and knowledge? |
| [[knowledge/schema]] | artifact contracts | What does a representation, distillate, assertion, topic map, glossary entry or chapter look like? |
| [[knowledge/operations]] | procedures | How is a source acquired, ingested, distilled, synthesized, analyzed, written up and validated? |
| [[knowledge/verification]] | adversarial checking of own claims | How are the project's claims reviewed, by whom, and with what independence? |
| [[knowledge/testing]] | quality assurance | Which checks close a change, and what does each of them establish? |
| [[knowledge/governance]] | authority, trust, rights, roles | Who decides, what is trusted, what may be published, and how is work delegated? |
| [[knowledge/plan]] | forward planning | Which milestones remain, and what closes each of them? |
| [[knowledge/handoff]] | process inbox | Which open handoff points await the next session? |
| [[knowledge/journal]] | provenance of decisions | Why was a choice made, and what did it replace? |
| [[knowledge/state]] | current reality | What exists now, what passed which check, and what is open? |
| [[knowledge/text-model]] | formal definition of the abstract text model and its conformance rules | What exactly does the candidate model define, and when does an instance conform? |
| [[knowledge/text-model-bindings]] | the JSON, XML and YAML bindings that preserve one model instance | How is one model instance written in each supported syntax without changing it? |
| [[knowledge/p6-architecture]] | the candidate architecture beyond the text model, customization, versioning, migration, and the argument structure of the proposal | How do customization, versioning and migration surround the model, and how is the proposal argued? |
| [[knowledge/p6-evaluation]] | design principles, evaluation dimensions, comparison protocol and acceptance criteria for P6 options | How are P6 options compared without presuming the answer? |
| [[knowledge/experiments]] | experiment contracts, acceptance items and evidence entry points of the executed pilots | What did each executed pilot test, how is it reproduced, and what remains for human acceptance? |

A document is split only when its routing questions or update cycles differ.
Length alone never splits a document. Redundancy between documents is
expressed through links, and the most important content of a document comes
first.

The model, architecture, evaluation and experiment documents record
hypotheses, contracts and executed experiments. They stand outside the
evidence chain and cannot ground a claim about P5 or about official TEI
policy. Such a claim enters through the layers below and reaches output only
as an assertion or an explicit posit.

## Terminology

| Term | Meaning in this vault |
|---|---|
| Source | The original file, preserved exactly as received |
| Markdown representation | The stable converted source with block IDs for later citations |
| Distillate | Statements extracted from one source and individually anchored to it |
| Assertion | One source-supported statement grounded in one or more distillate statements |
| Chapter | Output whose factual premises cite assertions and whose own conclusions are marked as posits |
| Source type | A source class defined by its representation, distillation procedure, and grounding anchor |
| Citation-only source | A publication or thread whose full text stays outside the public repository and whose anchor is a checked quotation and identifier |
| Grounding | The structural anchor relation connecting a claim to source locations, without establishing truth |
| Evidence | A grounding relation that has passed human expert verification |
| Provenance chain | The unbroken path from output through assertions and distillates to source locations |
| Audit trail | Dated records of checks that actually ran on the artifact |
| Posit | An authorial conclusion with an explicit rationale and open evidence question |
| Validation | Deterministic checks of artifact structure, anchors, and declared rules |
| Machine review | Adversarial review of whether source passages support their statements |
| Verification | Review by the designated human expert |
| Navigation projection | A generated view such as a corpus projection, catalog, index, search result or site page that points toward evidence and never appears in `grounding` |
| Finding, interpretation, proposal | A source-supported observation, a reasoned account of findings, and a design option, respectively |
| Official P6 process | TEI Council records and artifacts concerning P6, distinct from this project's proposals and not presumed to be a released standard |
| Observable-complete | Every object observable through a registered finite interface during the snapshot interval was retrieved or recorded as a gap |
| Bounded-complete | Every result of a declared finite search, index, or bibliography protocol received a disposition |
| Work package | A bounded delegation with base commit, exclusive write globs, read-only inputs, expected outputs, required checks and gaps to report |
| Handoff point | An open item a session leaves for the next one in [[knowledge/handoff]] |

Findings can motivate interpretations and proposals without establishing them.
Completion labels describe the recorded boundary and never all material that
has ever existed. The full completion vocabulary is defined in
[[knowledge/data]], the artifact rules in [[knowledge/schema]].

## Folders

| Folder | Content | Rule |
|---|---|---|
| `00_sources/` | admitted originals, local only | gitignored except its README; every file is referenced by exactly one representation |
| `10_markdown/` | Markdown representations with block IDs, data files with schema descriptions | converted once and never edited |
| `20_distillates/` | one distillate per source, by source type | mints statement IDs |
| `30_assertions/` | atomic assertions and the topic maps `MOC-<Topic>.md` | every assertion reachable from a topic map |
| `40_output/` | one chapter per file | footnotes to assertions, posits marked |
| `glossary/` | one term per file | definition with grounding anchor where sourced |
| `references/` | CSL JSON bibliographic records | root of every citation-only source |
| `sources/` | registry, locks and append-only run manifests | the control plane of acquisition |
| `corpus/` | raw observations (local), normalized records, projections | never a grounding target |
| `experiments/` | hand-authored inputs and generated reports of the executed pilots | reports reproduce from declared inputs |
| `workbench/` | audit records of reviews under `workbench/reviews/<run-id>/` | records and never sources |
| `docs/` | the generated public site | never hand-edited |
| `tools/`, `tests/` | validators, collectors, builders, pilots and their tests | changed only with their tests |
| `.claude/skills/` | thin Claude Code adapters for ingest, distill and assertion building | route into [[knowledge/operations]] |
| `.github/workflows/` | continuous integration and publication | described in [[knowledge/testing]] |

[[knowledge/architecture]] explains how these folders form the planes of the
system and which files are generated.
