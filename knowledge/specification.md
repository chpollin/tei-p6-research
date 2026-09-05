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
updated: "2026-09-05"
related: [index, design, schema, operations, state, journal]
---

# Specification

This contract defines the research questions, scope, deliverables, and
acceptance criteria. Grounded Vault rules live in [[knowledge/schema]] and
[[knowledge/operations]], current progress in [[knowledge/state]], and the
interface contract in [[knowledge/design]]. Durable decisions are appended
to [[knowledge/journal]].

## Project proposition

The project develops and evaluates an abstract text model for a possible TEI
P6. Its concepts, identities, relations, and rules must support practical
encoding and processing. The model states its scope and makes its choices
traceable to source findings, declared assumptions, and reproducible tests.

P5 supplies a normative baseline, successful patterns, demonstrated problems,
and migration obligations. Text-theoretical scholarship, alternative models,
and documented editorial practice must supply additional requirements and
counterexamples. Reproducing P5 coherently is not sufficient to establish that
a candidate adequately models text across the declared use contexts.

Repair within P5, compatible evolution, major-version redesign, and deliberate
non-change remain comparable options until the evidence narrows them.

## Problem statement

TEI P5 is simultaneously a vocabulary, a customization system, a formal schema
source, a body of prose Guidelines, a governance process, an implementation
ecosystem, and a set of community practices. These surfaces establish different
facts. ODD declarations alone do not explain editorial use, and a discussion
record does not establish a released capability. The source-authority table
below defines these limits. The research must connect the relevant records
without treating their authority as interchangeable.

## Intended outcome

The intended publication combines a P5 model atlas, decision history,
grounded requirements and successful patterns, an abstract model, evaluated
alternatives, and migration studies. Executable prototypes test the central
claims. Recommendations name their evidence, counterevidence, costs, and
open questions. The deliverables table specifies their locations and
acceptance conditions.

The output genre is an English scholarly synthesis and design specification for
researchers, scholarly editors, standards maintainers, educators, and tool
builders.

The public workbench opens with the full technical proposal. Examples branch
into comparisons of P5 variants and candidate bindings. Model presents the
formal definition and class relationships, Materials the acquisition inventory,
Knowledge the admitted artifacts and provenance chain, and About the project
contracts. These views use one layout and canonical repository inputs.
Publication does not create evidence or an official TEI decision.

## Research questions

The central question is which distinctions among textual objects, their
representations, and editorial claims are needed for the declared tasks.
Generality is relative to an explicit range of text forms and practices. The
project does not attempt to model every subject that a text can discuss.
Domain-specific descriptions may connect to other models through explicit
relations. Text identity, carriers, transcription, interpretation, and version
continuity remain questions that an element inventory alone cannot settle.

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

The project keeps four states distinct.

| State | Role |
|---|---|
| P5 4.12.0 | immutable normative baseline pinned to an exact release commit |
| P5 development | moving, non-normative observations pinned to full commits and dates |
| historical TEI | earlier releases and records interpreted in their contemporary context |
| official P6 process | current process records and artifacts, not yet assumed normative |

The primary baseline is TEI P5 4.12.0 at commit
`113e933e21f016e2655518321e9d10214b8d9fcb`. The alias `current` and a moving
branch name are never used as immutable evidence identities.

Every module in that baseline is in scope for investigation. Module inventory,
source interpretation, formal requirements, and executed cases remain separate
coverage measures. Document types, media forms, and textual phenomena are
cross-cutting dimensions rather than equivalents of P5 modules or model classes.

The project studies P5 and official P6 records globally where sources permit,
but corpus completeness is always bounded by the interfaces, dates, languages,
rights, and search protocols recorded under `sources/` and
`corpus/COMPLETENESS.md`.

## Source and authority model

Source authority is specific to the kind of claim being made.

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

Decision trails preserve the transitions between proposal and release.

```text
discussion/proposal
    -> explicit governance decision
        -> merged implementation
            -> released normative effect
```

Each transition requires its own support. Source authority, accessibility,
rights, and instruction trust are separate fields.

## Promptotyping model

The project is maintained as an executable research specification.

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
when the project learns something about its own method or scope. Research
findings themselves enter the canonical Grounded Vault layers.

## Acquisition and knowledge boundary

Large collections follow the acquisition chain.

```text
sources -> corpus/raw -> corpus/normalized -> corpus/projections
```

This corpus supports inventory, discovery, counting, graph construction, and
candidate selection. Persistent claims require admission to the knowledge chain.

```text
00_sources -> 10_markdown -> 20_distillates -> 30_assertions -> 40_output
```

The acquisition software, agent ownership, reconciliation gates, and recovery
procedures are specified in `docs/multi-agent-acquisition-runbook.md`.

## Evaluation dimensions for P6 options

Every material option is evaluated on the following dimensions, with losses
and gains reported together.

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

- XML remains part of the evaluated ecosystem. Alternative serializations
  require evidence and explicit compatibility analysis.
- Existing TEI documents, ODDs, schemas, processors, teaching material, and
  institutional practices are migration subjects, not disposable noise.
- Formal simplification must not silently collapse conceptually necessary
  distinctions.
- Backward compatibility is a design variable to evaluate, not an absolute
  requirement and not a cost-free promise.
- Private or inaccessible material cannot be used as if publicly auditable.
- Public availability does not imply permission to redistribute full text.
- Agent output is not evidence merely because it is reproducible or fluent.
- Unresolved alternatives remain explicit until the evidence supports a decision.

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
| reproducible corpus | `corpus/` plus manifests | declared boundary exhausted or gaps recorded, with reconciled hashes |
| P5 formal object graph | generated corpus projections | byte-reproducible from pinned ODD sources |
| grounded topic knowledge | `10_markdown/` through `30_assertions/` | every assertion resolves to source-faithful statements |
| P5 architecture synthesis | `40_output/` | grounded factual premises and explicit posits |
| P6 option matrix | `40_output/` | alternatives compared across declared dimensions |
| migration dossier | `40_output/` | mappings, affected artifacts, costs, gaps, and test results explicit |
| agent context packs | `contexts/generated/` | deterministic, dependency-hashed, no new propositions |
| research workbench | `docs/` | generated from declared inputs, with provenance, rights, and independent status preserved |

## Success criteria

Research readiness requires the following results.

- the selected P5 baseline is fully materialized and every formal object points
  to an exact ODD source location.
- the declared GitHub snapshot is `observable-complete` and reconciled across
  issues, PRs, comments, reviews, timelines, commits, and releases.
- governance, history, and literature collections state finite boundaries,
  rights, dispositions, and gaps.
- at least one real-use/customization corpus has a documented sampling and
  rights protocol.
- every central P5 problem claim has supporting evidence, counterevidence or an
  explicit open-evidence status.
- three vertical pilots traverse the full provenance chain and pass independent
  machine review.
- P6 alternatives are compared against the same evaluation dimensions and
  representative use cases.
- a migration prototype tests representative P5 documents and reports loss,
  ambiguity, manual intervention, and tooling impact.
- the validator and test suite pass, generated artifacts reproduce, and no
  machine process assigns human verification.

The project reaches design-candidate readiness only after the P5 atlas,
demonstrated-problem corpus, option matrix, and migration evidence all satisfy
their acceptance conditions. A polished proposal without those prerequisites
is not a design candidate.

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
| Machine review | adversarial review in a separate agent/model context under anti-anchoring |
| Corpus completion | family-specific `observable-complete`, `bounded-complete`, or explicit gap state |

## Style sheet

Output uses precise English scholarly and technical prose. Each paragraph
develops one point. Remove repeated scope statements and sentences that add no
information. Use no colons or semicolons in running prose. Preserve punctuation
required by code, quotations, URLs, metadata, and formal citation syntax.
Use lists for navigation, independent checks, or ordered actions, and tables
to compare the same attributes across alternatives.

Canonical TEI element, attribute, class, module, macro, datatype, and ODD
identifiers remain unchanged.
Every load-bearing statement carries the provenance link required by
[[knowledge/schema]] and names the release, commit, or snapshot when
version-sensitive.

Findings, interpretations, and proposals are separated structurally or by
explicit sentence-level signalling. Quotations are verbatim and visibly distinct from paraphrase.
Official TEI positions are attributed and dated. No machine judgment is
described as human verification.

## Decision gates

The bounded text identity and annotation pilot applies these gates to one
experimental question before broader architecture selection. Its contract and
human acceptance procedure are in `docs/p6/text-identity-pilot.md`. It tests
explicit definitions and finite synthetic cases. It does not establish a
general ontology of text, complete P5 coverage, or real-world migratability.

| Gate | Requirement |
|---|---|
| Corpus | Source boundaries and rights rules must be operational before bulk synthesis |
| Model | A bounded architectural claim needs complete source coverage for its constructs and dependencies. Architecture-wide claims also require the declared P5 inventory and its prose relations to be complete. Exploratory hypotheses may proceed with explicit scope and gaps. Inventory completion alone does not establish ontological adequacy |
| Problem | A claimed problem needs supporting evidence and relevant counterevidence before becoming a design requirement |
| Option | Alternatives face the same evaluation dimensions before a P6 option is preferred |
| Migration | Representative P5 migration is prototyped before design-candidate readiness |
| Verification | Only the designated human expert may assign `verified` |

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
| 2026-09-04 | Provisional design work belongs in `docs/p6/`, outside the evidence chain. Executable artifacts require explicit contracts |
