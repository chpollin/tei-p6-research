# P6 design dossier

This directory organizes the project's provisional design knowledge for a
possible TEI P6. It is a research workbench, not an official TEI specification
and not a layer of the Grounded Vault evidence chain.

The dossier asks how a next-generation TEI model could be made conceptually
clearer, formally testable, serialization-independent, customizable, and
migratable without presuming that a complete redesign is the correct answer.

## Documents

| Document | Question |
|---|---|
| [`design-principles.md`](design-principles.md) | What properties should guide every candidate? |
| [`core-model.md`](core-model.md) | What must a serialization-independent model represent? |
| [`abstract-text-model-v0.1.md`](abstract-text-model-v0.1.md) | What exactly does the bounded executable candidate mean, how is it checked, and how can it be accepted? |
| [`blueprints-and-customization.md`](blueprints-and-customization.md) | How can shared models be selected, constrained, and extended? |
| [`serialization-and-conformance.md`](serialization-and-conformance.md) | How do bindings, validation, equivalence, and loss work? |
| [`examples-and-migration.md`](examples-and-migration.md) | How are P5/P6 comparisons and migrations made executable? |
| [`editorial-case-study.md`](editorial-case-study.md) | What do the bounded diary mappings preserve, where do they fail, and what does the separate historical-claim profile test? |
| [`evaluation.md`](evaluation.md) | How are alternatives compared without assuming the answer? |
| [`versioning-and-governance.md`](versioning-and-governance.md) | How do identifiers, releases, compatibility, and decisions evolve? |
| [`research-agenda.md`](research-agenda.md) | Which questions require evidence, prototypes, or governance decisions? |
| [`text-identity-pilot.md`](text-identity-pilot.md) | How can a bounded text/version/region/annotation experiment be tested and accepted? |
| [`proposal-outline.md`](proposal-outline.md) | How will the findings, model alternatives, and evaluations form an independent Proposal for TEI P6? |
| [`research-wave-1.md`](research-wave-1.md) | What bounded P5, discussion, and literature packages feed the first proposal integration? |

The project-wide purpose and constraints remain authoritative in
`knowledge/specification.md`. Grounded descriptions of P5 belong in the
numbered evidence chain. Accepted research conclusions belong in `40_output/`.
This dossier contains design hypotheses, definitions under consideration, and
contracts for experiments. The broader core-model sketch is not an inventory of
v0.1 features. The [P6 Design chapter](../../40_output/12-p6-design.md) connects
the bounded candidate to grounded premises and explicit project posits.

## Candidate architecture

```text
P5 + text theory + editorial practice
          |
          v
requirements and counterexamples
          |
          v
serialization-independent core model
          |
          +--> blueprint/customization
          |          |
          |          v
          +--> normative serialization bindings
                         |
                         v
              validators and converters
                         |
                         v
        examples + migration + roundtrip tests
                         |
                         v
              comparative evaluation
```

This flow sketches one candidate: a semantic core with customization rules,
normative bindings, invariants, conformance levels, diagnostic behavior, and an
executable test suite. The need for each component, its boundary, and competing
arrangements remain questions for comparative evaluation. Neither this diagram
nor a successful selector pilot settles the architecture.

## Epistemic discipline

Statements in this directory use four roles:

- **Requirement:** a capability a candidate is evaluated against. Distinguish
  requirements derived from grounded findings from explicit project choices;
  a project decision records a commitment, not external evidence of need.
- **Hypothesis:** a proposed design choice that must be tested against
  alternatives.
- **Contract:** an operational rule for a prototype or evaluation.
- **Question:** an unresolved issue assigned to evidence gathering, formal
  analysis, prototyping, or governance.

None of these roles establishes a fact about P5 or the official P6 process.
When a design document relies on such a fact, the final research output must
cite the relevant assertion in `30_assertions/`.

## Boundaries

The design dossier may describe candidate structures and expected experiments,
but executable schemas, converters, fixtures, and reports require explicit
artifact contracts before dedicated directories are created. Those contracts
must state canonical inputs, generated outputs, authority, versioning,
validation, and whether an artifact is hand-authored or derived.

Progress and blockers are not tracked here. They belong in
`knowledge/state.md`; durable decisions and rejected alternatives belong in
`knowledge/journal.md`.
