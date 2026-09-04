---
title: Specification
project:
  name: "TEI P6 Research Vault"
  repository: "tei-p6"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
profile:
  name: Grounded Vault
  url: https://github.com/DigitalHumanitiesCraft/grounded-vault
status: draft
language: en
created: "2026-09-04"
updated: "2026-09-04"
related: [index, schema, operations, state, journal]
---

# Specification

This is the Promptotyping project contract for the TEI P6 Research Vault. It
defines the problem, research questions, boundaries, intended artifacts,
evaluation dimensions, and success criteria of this instance. The invariant
Grounded Vault mechanics live in [[knowledge/schema]] and
[[knowledge/operations]]; volatile progress lives in [[knowledge/state]];
decisions and changes of rationale are appended to [[knowledge/journal]].

## Project proposition

The project will construct a provenance-complete account of how TEI P5 is
modeled, how that model developed, where its users and maintainers encounter
friction, and which architecture choices for TEI P6 are justified by the
evidence.

The project does not treat “P5 is historically grown” or “P6 requires a full
rewrite” as established facts. These are propositions to decompose and test.
Repair within P5, compatible evolution, major-version redesign, and deliberate
non-change remain comparable options until the evidence narrows them.

## Problem statement

TEI P5 is simultaneously a vocabulary, a customization system, a formal schema
source, a body of prose Guidelines, a governance process, an implementation
ecosystem, and a set of community practices. Judging its architecture from only
one of these surfaces produces incomplete conclusions:

- the published Guidelines show normative documentation but not every design
  rationale or implementation constraint;
- the ODD sources show formal structures but not how projects understand or use
  them;
- issues and pull requests show reported needs and change work but do not alone
  establish consensus or released effects;
- Council minutes show discussion and decisions but not necessarily merged or
  published implementation;
- papers and project reports show analyses and practices but are not normative;
- local ODDs and toolchains show real adaptation but form a biased sample unless
  their collection protocol is explicit.

A credible P6 design therefore needs an evidence system that keeps these source
roles separate while allowing their relationships to be studied.

## Intended outcome

The final outcome is not merely a new schema. It is a reviewable design dossier
consisting of:

1. a version-bound atlas of the P5 conceptual and formal model;
2. a history of significant model and governance decisions;
3. a classified corpus of demonstrated pain points, use cases, and successful
   patterns;
4. explicit P6 design principles and alternatives;
5. a proposed abstract model and its relation to serializations;
6. a compatibility and migration strategy;
7. executable prototypes or formalizations sufficient to test central claims;
8. an evaluation report linking each recommendation to P5 evidence,
   counterevidence, trade-offs, and open questions.

The output genre is a German scholarly synthesis and design specification for
researchers, scholarly editors, standards maintainers, educators, and tool
builders.

## Research questions

### RQ1 — What is the P5 model?

What conceptual entities, element and attribute classes, modules, macros,
datatypes, constraints, content models, customization mechanisms, and prose
rules constitute the selected P5 release? Where do the prose model, ODD model,
and generated schemas align or diverge?

### RQ2 — How did the model develop?

Which structures are inherited from earlier TEI generations, which were added
or revised during P5, and which constraints reflect historical technology,
compatibility, governance, or use-case decisions?

### RQ3 — Where is friction demonstrated?

Which difficulties are evidenced by repeated issues, workarounds, divergent
customizations, processing complexity, teaching problems, interoperability
failures, or migration experience? Which alleged problems are isolated
preferences or remain unsupported?

### RQ4 — What already works and must be preserved?

Which P5 capabilities, identifiers, customization patterns, interchange
contracts, community conventions, and processing expectations provide durable
value? What would be lost under each redesign option?

### RQ5 — What is the official P6 process deciding?

Which goals, agreements, disagreements, prototypes, and constraints are
documented by the official TEI P6 process? What remains exploratory? Official
records are reported as such and are never conflated with this independent
project's recommendations.

### RQ6 — Which architecture options perform best?

How do incremental P5 repair, compatibility-preserving evolution, and a major
P6 redesign compare across the evaluation dimensions below? Which decisions
require prototypes or empirical tests rather than textual argument?

### RQ7 — How can change be adopted?

What mappings, compatibility modes, migration tools, version declarations,
validation contracts, governance processes, and educational materials would be
required for existing projects and software to adopt a new architecture?

## Research object and temporal scope

The project keeps four states distinct:

| State | Role |
|---|---|
| P5 4.12.0 | immutable normative baseline pinned to an exact release commit |
| P5 development | moving, non-normative observations pinned to full commits and dates |
| historical TEI | earlier releases and records interpreted in their contemporary context |
| official P6 process | current process records and artifacts, not yet assumed normative |

The primary baseline is TEI P5 4.12.0 at commit
`113e933e21f016e2655518321e9d10214b8d9fcb`. The alias `current` and a moving
branch name are never used as immutable evidence identities.

The project studies P5 and official P6 records globally where sources permit,
but corpus completeness is always bounded by the interfaces, dates, languages,
rights, and search protocols recorded under `sources/` and
`corpus/COMPLETENESS.md`.

## Source and authority model

Sources establish different kinds of claims:

| Source family | Primary authority | Cannot establish alone |
|---|---|---|
| released Guidelines, ODD, schemas | normative state of a named release | motivation, user success, future policy |
| Git tree and generated artifacts | implementation at a named commit | normative publication unless released |
| issues and pull requests | proposals, reports, discussion, implementation trail | consensus or released effect |
| Council/Board records | documented governance discussion or decision | actual merge or released semantics |
| official P6 records | state of the official P6 process at a date | this vault's recommendation or a final standard |
| local ODDs and project studies | observed customization and practice in the declared sample | universal community need |
| scholarly literature | analysis, critique, comparison, and reported practice | TEI normativity |
| deterministic corpus computation | aggregate result over the declared snapshot | meaning beyond its measured scope |

Decision trails preserve four independent transitions:

```text
discussion/proposal
    -> explicit governance decision
        -> merged implementation
            -> released normative effect
```

Each transition requires its own support. Source authority, accessibility,
rights, and instruction trust are separate fields.

## Promptotyping model

The project is maintained as an executable research specification:

| Component | Project realization |
|---|---|
| Intent | understand P5 well enough to compare and test P6 architecture options |
| Inputs | versioned normative, development, governance, historical, scholarly, and practice sources |
| Transformations | acquire, normalize, admit, distill, synthesize, review, prototype, evaluate |
| Knowledge objects | representations, distillates, assertions, topic maps, glossary entries, chapters |
| Control objects | registry, locks, run manifests, schemas, state, journal, tests |
| Outputs | P5 model atlas, decision trails, problem taxonomy, P6 options, migration and evaluation dossier |
| Feedback | deterministic validation, adversarial machine review, human verification, prototype results |

The documents in `knowledge/` are part of the control system. They are revised
when the project learns something about its own method or scope; research
findings themselves enter the canonical Grounded Vault layers.

## Acquisition and knowledge boundary

Large collections are acquired through:

```text
sources -> corpus/raw -> corpus/normalized -> corpus/projections
```

This corpus supports inventory, discovery, counting, graph construction, and
candidate selection. It is not evidence by itself. Persistent claims enter only
through:

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

The acquisition software, agent ownership, reconciliation gates, and recovery
procedures are specified in `docs/multi-agent-acquisition-runbook.md`.

## Evaluation dimensions for P6 options

No proposal is called “optimized” without naming the dimensions and trade-offs.
Every material option is evaluated against:

1. **Conceptual clarity** — concepts and distinctions are explicit and
   internally coherent.
2. **Expressivity** — documented use cases can be represented without
   misleading semantics or excessive workarounds.
3. **Compositionality** — modules, classes, constraints, and customizations
   combine predictably.
4. **Formal precision** — specifications can be implemented and tested without
   relying on undocumented processor behavior.
5. **Customization** — projects can constrain and extend the model while
   retaining a meaningful shared contract.
6. **Interoperability** — data and semantics can be exchanged across projects,
   tools, serializations, and linked-data environments.
7. **Validation and processing** — schemas, constraints, transformations, and
   diagnostics remain implementable and maintainable.
8. **Compatibility and migration** — existing P5 data and software have
   measurable mappings, costs, and failure modes.
9. **Learnability and accessibility** — the architecture can be taught,
   documented, localized, and used by communities with different resources.
10. **Governance and evolution** — versioning, deprecation, extension, and
    decision processes can sustain long-term change.

Evaluation records must state stakeholders, use cases, baseline, metric or
judgment procedure, evidence, counterevidence, uncertainty, and migration cost.
A gain on one dimension may be accepted only with its losses on others visible.

## Design constraints

- XML remains part of the evaluated ecosystem; replacement or supplementary
  serializations require evidence and explicit compatibility analysis.
- Existing TEI documents, ODDs, schemas, processors, teaching material, and
  institutional practices are migration subjects, not disposable noise.
- Formal simplification must not silently collapse conceptually necessary
  distinctions.
- Backward compatibility is a design variable to evaluate, not an absolute
  requirement and not a cost-free promise.
- Private or inaccessible material cannot be used as if publicly auditable.
- Public availability does not imply permission to redistribute full text.
- Agent output is not evidence merely because it is reproducible or fluent.
- The project may document unresolved alternatives; premature convergence is a
  defect.

## Non-goals

- Declaring the official TEI P6 architecture on behalf of the TEI Consortium.
- Treating every P5 feature or historical layer as a defect.
- Designing from issue frequency alone.
- Copying the whole web or every third-party paper into Git.
- Claiming recovery of deleted, private, overwritten, or inaccessible records.
- Equating issue closure, Council discussion, merge, and release.
- Replacing human domain verification with agent consensus.
- Producing a final P6 schema before evaluation criteria and evidence paths are
  operational.

## Deliverables

| Deliverable | Canonical location | Acceptance condition |
|---|---|---|
| source and rights register | `sources/` | version/snapshot, authority, rights, scope, and gaps explicit |
| reproducible corpus | `corpus/` plus manifests | declared boundary exhausted or gaps recorded; hashes reconcile |
| P5 formal object graph | generated corpus projections | byte-reproducible from pinned ODD sources |
| grounded topic knowledge | `10_markdown/` through `30_assertions/` | every assertion resolves to source-faithful statements |
| P5 architecture synthesis | `40_output/` | all load-bearing claims grounded; posits explicit |
| P6 option matrix | `40_output/` | alternatives compared across declared dimensions |
| migration dossier | `40_output/` | mappings, affected artifacts, costs, gaps, and test results explicit |
| agent context packs | `contexts/generated/` | deterministic, dependency-hashed, no new propositions |

## Success criteria

The project reaches research readiness when:

- the selected P5 baseline is fully materialized and every formal object points
  to an exact ODD source location;
- the declared GitHub snapshot is `observable-complete` and reconciled across
  issues, PRs, comments, reviews, timelines, commits, and releases;
- governance, history, and literature collections state finite boundaries,
  rights, dispositions, and gaps;
- at least one real-use/customization corpus has a documented sampling and
  rights protocol;
- every central P5 problem claim has supporting evidence, counterevidence or an
  explicit open-evidence status;
- three vertical pilots traverse the full provenance chain and pass independent
  machine review;
- P6 alternatives are compared against the same evaluation dimensions and
  representative use cases;
- a migration prototype tests representative P5 documents and reports loss,
  ambiguity, manual intervention, and tooling impact;
- the validator and test suite pass, generated artifacts reproduce, and no
  machine process assigns human verification.

The project reaches design-candidate readiness only after the P5 atlas,
demonstrated-problem corpus, option matrix, and migration evidence all satisfy
their acceptance conditions. A polished proposal without those prerequisites
is not a design candidate.

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | P5 Architecture; Abstract Model; ODD and Customization; Elements and Classes; Text and Document Structures; Annotation and Overlap; Critical Apparatus; Metadata and Entities; History and Governance; Issues and Decisions; Interoperability and Processing; P6 Design |
| Active source types | document, publication, data |
| Primary baseline | TEI P5 4.12.0, commit `113e933e21f016e2655518321e9d10214b8d9fcb` |
| Output genre | scholarly synthesis and design specification |
| Working language of content | German; canonical English TEI identifiers remain unchanged |
| Verification role | project owner or explicitly designated TEI domain expert; no human verifier assigned |
| Validation mechanism | `tools/validate.py` |
| Machine review | adversarial review in a separate agent/model context under anti-anchoring |
| Corpus completion | family-specific `observable-complete`, `bounded-complete`, or explicit gap state |

## Style sheet

Output uses precise German scholarly and technical prose. English TEI element,
attribute, class, module, macro, datatype, and ODD identifiers remain unchanged.
Every load-bearing statement carries the provenance link required by
[[knowledge/schema]] and names the release, commit, or snapshot when
version-sensitive.

Findings (*Befund*), interpretations (*Interpretation*), and proposals
(*Vorschlag*) are separated structurally or by explicit sentence-level
signalling. Quotations are verbatim and visibly distinct from paraphrase.
Official TEI positions are attributed and dated. No machine judgment is
described as human verification.

## Decision gates

1. **Corpus gate:** no bulk synthesis before source boundaries and rights rules
   are operational.
2. **Model gate:** no architectural critique before the baseline ODD model and
   its prose relations are inventory-complete.
3. **Problem gate:** no problem is promoted to a design requirement without
   evidence and relevant counterevidence.
4. **Option gate:** no preferred P6 option before alternatives are evaluated
   against the same dimensions.
5. **Migration gate:** no design candidate before representative P5 migration
   is prototyped.
6. **Verification gate:** no `verified` status without the designated human
   expert.

## Settled decisions

- 2026-09-04: The Grounded Vault was instantiated as the independent TEI P6
  Research Vault in the local `tei-p6` repository.
- 2026-09-04: The controlled topic set contains twelve P5-analysis and P6-design
  maps; all three source types are active.
- 2026-09-04: The output is a German scholarly synthesis and design
  specification; canonical TEI identifiers remain English.
- 2026-09-04: Human verification is reserved for the project owner or an
  explicitly designated TEI domain expert.
- 2026-09-04: Separate-context adversarial review establishes machine review
  only, never human verification.
- 2026-09-04: Official TEI P6 process records and independent P6 proposals are
  different source and claim categories.
- 2026-09-04: The data corpus is a discovery and analysis layer; it cannot
  bypass the canonical Grounded Vault chain.
- 2026-09-04: P6 options are evaluated comparatively; a complete rewrite is not
  assumed in advance.
- 2026-09-04: Provisional P6 design knowledge is organized under `docs/p6/`.
  It is not an evidence layer; factual claims still require the canonical
  Grounded Vault chain, and executable artifacts require explicit contracts.
