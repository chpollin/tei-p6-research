# Research and implementation plan

This document defines the stable sequence of work for the TEI P6 Research
project. It does not repeat current progress, object counts, or blockers; those
belong in `knowledge/state.md` and acquisition manifests. Detailed project
requirements are in `knowledge/specification.md`, system boundaries in
`ARCHITECTURE.md`, and collector procedures in
`docs/multi-agent-acquisition-runbook.md`.

## Intended result

The programme develops an abstract text model whose conceptual distinctions
and practical consequences can be examined. It produces four connected outcomes:

1. a version-bound formal and conceptual atlas of TEI P5;
2. an auditable history of problems, decisions, implementations, and releases;
3. formally specified P6 alternatives with bindings, examples, and migration
   behavior;
4. a reasoned recommendation that exposes evidence, counterevidence,
   trade-offs, uncertainty, and adoption costs.

The intended integrating text is an independent **Proposal for TEI P6**.
`docs/p6/proposal-outline.md` maps its argument to the output chapters;
`docs/p6/research-wave-1.md` defines the first parallel execution packages.

P5 reconstruction and migration are essential baselines. Independent theoretical
and editorial sources must also challenge whether the proposed text concepts
are adequate for their declared scope.

## Work sequence

| Phase | Purpose | Exit condition |
|---|---|---|
| 0. Project contract | establish scope, evidence rules, rights, authority, and navigation | repository rules and checks are internally consistent |
| 1. Acquisition software | build reproducible TEI, GitHub, governance, archive, and literature collectors | offline fixtures, failure recovery, and manifest tests pass |
| 2. Corpus bootstrap | materialize every registered source family within its declared boundary | each family is reconciled or carries explicit gaps |
| 3. Formal P5 model | extract elements, classes, attributes, modules, macros, datatypes, constraints, and relations from pinned ODD | clean rebuild is deterministic and every object resolves to source |
| 4. Grounding pilots | complete representative end-to-end evidence chains | three pilots pass validation and adversarial review |
| 5. P5 synthesis | build topic-scale findings, counterclaims, decision trails, and use cases | central architecture claims have evidence or explicit open status |
| 6. P6 candidates | formalize alternative core models, blueprints, constraints, and bindings | candidates are executable on representative examples |
| 7. Conformance and migration | compare serializations and migrate representative P5 corpora and customizations | equivalence, ambiguity, loss, and implementation costs are measured |
| 8. Design dossier | evaluate alternatives and publish the grounded specification | recommendations satisfy the project success criteria and review gates |

Phases may overlap only where their inputs and authority boundaries are stable.
Design exploration may begin early, but no candidate is promoted as preferred
before the relevant P5 baseline, problem evidence, alternatives, and migration
results exist.

## Decision gates

The corpus gate requires declared source boundaries and rights. The model gate
requires an inventory-complete pinned P5 baseline before architectural critique
is generalized. The problem gate requires demonstrated friction and relevant
counterevidence. The option gate requires competing responses to be evaluated
under the same dimensions. The migration gate requires representative
documents, customizations, and processors. The verification gate reserves
`verified` status for designated human expert review.

Failure at a gate produces a documented gap or open question, not an invented
answer.

## Workstreams

The programme can be divided into independently reviewable workstreams:

- **Sources and provenance:** registry, locks, collectors, manifests, rights,
  completeness, and raw/normalized corpus records.
- **P5 model extraction:** ODD parsing, object graph, constraints, generated
  schemas, and release comparison.
- **History and decisions:** issues, pull requests, commits, Council records,
  releases, and typed decision trails.
- **Knowledge engineering:** representations, distillates, assertions, topic
  maps, retrieval indexes, and context packs.
- **P6 design:** principles, core-model alternatives, blueprints,
  serializations, constraints, examples, and governance.
- **Text concepts and practice:** independently sourced definitions, explicit
  identity assumptions, bounded case selection, and editorial task expectations.
- **Conformance and migration:** validators, converters, roundtrip comparison,
  loss reports, compatibility matrices, and implementation studies.

Shared schemas and artifact contracts are decided before parallel work begins.
Each work package owns disjoint paths, records its base revision and expected
outputs, and returns commands, results, gaps, and changed files for integration.

## Required outputs

The final repository must contain a reproducible primary-source corpus, a
formal P5 object graph, grounded topic knowledge, decision trails, a P6 option
matrix, executable example and migration suites, generated context packs, and a
source-linked scholarly design specification. Generated outputs must rebuild
from pinned inputs; hand-authored interpretations and proposals must remain
visibly distinct from derived data.

## Definition of completion

The project is complete only when the declared source boundaries have been
exhausted or their gaps recorded, every central P5 claim is traceable, the
formal P5 model rebuilds deterministically, P6 alternatives have been tested on
representative and adverse cases, migration losses are explicit, and the final
recommendations survive deterministic validation, adversarial review, and the
designated human verification process.

The authoritative current position within this sequence is maintained in
`knowledge/state.md`.
