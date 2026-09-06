---
title: Specification
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
profile:
  name: Grounded Vault
  url: https://github.com/DigitalHumanitiesCraft/grounded-vault
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-06"
related: [INDEX, project, data, governance, design, schema, operations, verification, testing, plan, state, journal]
---

# Specification

This document holds the requirements of the project. The charter, research
questions and scope are in [[knowledge/project]]. The source families and
their hierarchy are described in [[knowledge/data]] and the authority and
trust rules in [[knowledge/governance]]. Artifact rules are in
[[knowledge/schema]] and [[knowledge/operations]], the interface contract in
[[knowledge/design]], current progress in [[knowledge/state]] and the reasons
behind settled choices in [[knowledge/journal]].

## Evaluation dimensions for P6 options

Every material option is evaluated on the following dimensions, with losses
and gains reported together.

1. **Conceptual clarity.** Concepts and distinctions are explicit and
   internally coherent.
2. **Expressivity.** Documented use cases can be represented without
   misleading semantics or excessive workarounds.
3. **Compositionality.** Modules, classes, constraints and customizations
   combine predictably.
4. **Formal precision.** Specifications can be implemented and tested without
   relying on undocumented processor behavior.
5. **Customization.** Projects can constrain and extend the model while
   retaining a meaningful shared contract.
6. **Interoperability.** Data and semantics can be exchanged across projects,
   tools, serializations and linked-data environments.
7. **Validation and processing.** Schemas, constraints, transformations and
   diagnostics remain implementable and maintainable.
8. **Compatibility and migration.** Existing P5 data and software have
   measurable mappings, costs and failure modes.
9. **Learnability and accessibility.** The architecture can be taught,
   documented, localized and used by communities with different resources.
10. **Governance and evolution.** Versioning, deprecation, extension and
    decision processes can sustain long-term change.

Evaluation records must state stakeholders, use cases, baseline, metric or
judgment procedure, evidence, counterevidence, uncertainty and migration
cost. A gain on one dimension may be accepted only with its losses on others
visible. The comparison protocol and acceptance criteria that apply these
dimensions are in [[knowledge/p6-evaluation]].

## Design constraints

- XML remains part of the evaluated ecosystem. Alternative serializations
  require evidence and explicit compatibility analysis.
- Existing TEI documents, ODDs, schemas, processors, teaching material and
  institutional practices are migration subjects.
- Formal simplification must not silently collapse conceptually necessary
  distinctions.
- Backward compatibility is a design variable that is evaluated with its
  costs made explicit.
- Private or inaccessible material cannot be used as if publicly auditable.
- Public availability does not imply permission to redistribute full text.
  The rights rule is in [[knowledge/data]].
- Reproducibility or fluency of agent output establishes no evidence.
- Unresolved alternatives remain explicit until the evidence supports a
  decision.

## Deliverables

| Deliverable | Canonical location | Acceptance condition |
|---|---|---|
| source and rights register | `sources/` | version or snapshot, authority, rights, scope and gaps explicit |
| reproducible corpus | `corpus/` plus manifests | declared boundary exhausted or gaps recorded, with reconciled hashes |
| P5 formal object graph | generated corpus projections | byte-reproducible from pinned ODD sources |
| grounded topic knowledge | `10_markdown/` through `30_assertions/` | every assertion resolves to source-faithful statements |
| P5 architecture synthesis | `40_output/` | grounded factual premises and explicit posits |
| abstract text model and bindings | [[knowledge/text-model]], [[knowledge/text-model-bindings]], `experiments/` | executable contract, independently authored cases, reproducible report |
| P6 option matrix | `40_output/` | alternatives compared across the declared dimensions |
| migration dossier | `40_output/` | mappings, affected artifacts, costs, gaps and test results explicit |
| Proposal for TEI P6 | `40_output/12-p6-design.md` | premises rest on `validated` assertions, posits explicit, alternatives and reversal conditions named |
| research workbench | `docs/` | generated from declared inputs, with provenance, rights and independent status preserved |

## Success criteria

Research readiness requires the following results.

- The selected P5 baseline is fully materialized and every formal object
  points to an exact ODD source location.
- The declared GitHub snapshot is `observable-complete` and reconciled across
  issues, pull requests, comments, reviews, timelines, commits and releases.
- Governance, history and literature collections state finite boundaries,
  rights, dispositions and gaps.
- At least one real-use or customization corpus has a documented sampling
  and rights protocol.
- Every central P5 problem claim has supporting evidence, counterevidence or
  an explicit open-evidence status.
- Three vertical pilots traverse the full provenance chain and pass
  independent machine review.
- P6 alternatives are compared against the same evaluation dimensions and
  representative use cases.
- A migration prototype tests representative P5 documents and reports loss,
  ambiguity, manual intervention and tooling impact.
- The validator and test suite pass, generated artifacts reproduce, and no
  machine process assigns human verification.

The project reaches design-candidate readiness only after the P5 atlas,
demonstrated-problem corpus, option matrix and migration evidence all satisfy
their acceptance conditions. A polished proposal without those prerequisites
remains a hypothesis. The milestones that close these criteria are in
[[knowledge/plan]].

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | P5 Architecture, Abstract Model, ODD and Customization, Elements and Classes, Text and Document Structures, Annotation and Overlap, Critical Apparatus, Metadata and Entities, History and Governance, Issues and Decisions, Interoperability and Processing, P6 Design |
| Active source types | document, publication, data |
| Primary baseline | TEI P5 4.12.0, commit `113e933e21f016e2655518321e9d10214b8d9fcb` |
| Output genre | scholarly synthesis and design specification |
| Working language of content | English, with canonical TEI identifiers unchanged |
| Verification role | project owner or explicitly designated TEI domain expert |
| Validation mechanism | `tools/validate.py` |
| Machine review | fresh-context adversarial review under the protocol in [[knowledge/verification]] |
| Corpus completion | family-specific `observable-complete`, `bounded-complete`, or explicit gap state as defined in [[knowledge/data]] |

## Style sheet

Output uses precise English scholarly and technical prose. Each paragraph
develops one point. Remove repeated scope statements and sentences that add
no information. Use no colons or semicolons in running prose. Preserve
punctuation required by code, quotations, URLs, metadata and formal citation
syntax. Use lists for navigation, independent checks or ordered actions, and
tables to compare the same attributes across alternatives.

Canonical TEI element, attribute, class, module, macro, datatype and ODD
identifiers remain unchanged. Every load-bearing statement carries the
provenance link required by [[knowledge/schema]] and names the release,
commit or snapshot when version-sensitive.

Findings, interpretations and proposals are separated structurally or by
explicit sentence-level signalling. Quotations are verbatim and visibly
distinct from paraphrase. Official TEI positions are attributed and dated. No
machine judgment is described as human verification. Documentation names
third parties by role and institution.

## Decision gates

| Gate | Requirement |
|---|---|
| Corpus | Source boundaries and rights rules must be operational before bulk synthesis |
| Model | A bounded architectural claim needs complete source coverage for its constructs and dependencies. Architecture-wide claims also require the declared P5 inventory and its prose relations to be complete. Exploratory hypotheses may proceed with explicit scope and gaps. Inventory completion alone does not establish ontological adequacy |
| Problem | A claimed problem needs supporting evidence and relevant counterevidence before becoming a design requirement |
| Option | Alternatives face the same evaluation dimensions before a P6 option is preferred |
| Migration | Representative P5 migration is prototyped before design-candidate readiness |
| Verification | Only the designated human expert may assign `verified` |

The bounded text identity and annotation pilot applied these gates to one
experimental question before broader architecture selection. Its contract and
human acceptance procedure are in [[knowledge/experiments]]. It tests
explicit definitions and finite synthetic cases and establishes neither a
general ontology of text, nor complete P5 coverage, nor real-world
migratability. Failure at a gate produces a documented gap or open question.

## Settled decisions

The decision rationale remains in [[knowledge/journal]].

| Date | Settled choice |
|---|---|
| 2026-09-05 | Independent TEI P6 Research in `chpollin/tei-p6-research`, using the Grounded Vault evidence system |
| 2026-09-04 | Twelve topic maps and all three source types |
| 2026-09-05 | English project content and interface, with canonical TEI identifiers unchanged |
| 2026-09-04 | Human verification by the owner or an explicitly designated TEI domain expert |
| 2026-09-04 | Separate-context adversarial review establishes machine review only |
| 2026-09-04 | Official P6 process records remain distinct from independent proposals |
| 2026-09-04 | Corpus discovery and analysis cannot bypass the canonical knowledge chain |
| 2026-09-04 | P6 alternatives are compared without presuming a complete rewrite |
| 2026-09-04 | Provisional design work stays outside the evidence chain. Executable artifacts require explicit contracts |
| 2026-09-06 | The completeness of a collector run is derived from recorded gaps in one shared rule (adapter version 2), and a family label that rested on a self-referential count check is downgraded until re-run |
| 2026-09-06 | The knowledge base follows the Promptotyping convention with one home per rule in `knowledge/`; design knowledge lives in [[knowledge/text-model]], [[knowledge/text-model-bindings]], [[knowledge/p6-architecture]], [[knowledge/p6-evaluation]] and [[knowledge/experiments]] |
| 2026-09-06 | A proposal premise rests on `validated` assertions, human verification runs as a stratified sample per chapter with a recorded quota, independence of review means a different model family in a fresh context, and a counterevidence search precedes every design requirement |
| 2026-09-06 | Code is licensed under MIT, text and documentation under CC BY 4.0 |
| 2026-09-06 | Phenomena become glossary entries, topic maps and example lists are generated from frontmatter around a protected hand-written region, and typed relations are validated |
| 2026-09-06 | Opus performs specified implementation and ingestion, Fable performs judgment tasks, and briefs are versioned files with a recorded hash |
| 2026-09-06 | Issue threads, pull-request threads and mailing-list threads are admitted as citation-only publication sources, and TEI-L carries a three-part boundary |
