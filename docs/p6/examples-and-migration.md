# Examples and migration

Status: experimental design contract
Authority: independent project proposal

Examples are not illustrations added after the model is written. They are
executable specifications used to discover requirements, expose regressions,
compare alternatives, and test migrations between P5 and candidate P6 models.

## Example unit

Each design case should answer the same sequence of questions:

```text
What does the source material encode?
How does the selected P5 baseline represent it?
What concrete problem or successful pattern is being examined?
What must a P6 representation preserve?
How does the candidate core model express it?
How do supported bindings serialize it?
Which constraints accept or reject it?
What happens during migration and roundtrip?
```

The problem statement must be grounded. A complicated P5 example does not by
itself prove that P5 is defective; complexity may reflect the domain, an
intentional distinction, or an avoidable modeling choice.

## Future case package

After the executable-artifact contract is approved, a case should use a stable
package resembling:

```text
cases/<case-id>/
|-- README.md                 purpose, scope, and expected behavior
|-- evidence.md               grounded P5 claims and source pointers
|-- p5/
|   |-- minimal.xml
|   `-- realistic.xml
|-- model/
|   `-- expected.cir.*        canonical semantic expectation
|-- p6/
|   |-- example.xml
|   |-- example.jsonld
|   |-- example.ttl
|   `-- example.yaml
|-- invalid/                  one fixture per expected diagnostic
|-- migration/                mapping, ambiguity, and loss expectations
`-- expected/                 machine-readable validation results
```

The exact extensions remain undecided until the core formalism is selected.
The package layout separates authored inputs from generated representations and
must declare which files are canonical.

## Required variants

A complete case contains a minimal example that isolates one rule, a realistic
example that preserves domain complexity, a boundary or adversarial example,
an invalid example with an expected diagnostic, and a migration example from
the pinned P5 baseline. When multiple serializations are in scope, the case also
defines their expected semantic equivalence or declared loss.

Negative cases are essential. They distinguish a model that merely accepts the
happy path from one whose constraints and diagnostics are actually specified.

## Initial case families

| Family | Capability under test |
|---|---|
| mixed content | ordered alternation of text and inline structures |
| overlap | spans and concurrent hierarchies without false nesting |
| context-sensitive content | rules whose meaning or validity depends on structural context |
| stand-off annotation | stable references, ranges, and external annotation layers |
| linking and identity | local and global identifiers, pointers, and relation typing |
| bibliography | structured, unstructured, and partially known descriptions |
| critical apparatus | readings, witnesses, lemmas, variation, and location |
| manuscript description | deep structures, uncertain values, and reusable entities |
| linguistic annotation | tokenization, segmentation, alternatives, and alignment |
| facsimile alignment | text regions, surfaces, coordinates, and media references |

The first pilots should include at least one primarily hierarchical case, one
overlap or stand-off case, and one case that exercises context-sensitive
customization. This prevents the initial model from being optimized around a
single structural pattern.

## Before-and-after comparison

A comparison records more than shorter markup. It identifies the semantic
objects in both representations, constraints expressed or lost, amount of
implicit context, required processing knowledge, diagnostic quality,
customization effects, and teaching or authoring consequences.

Useful measurements include element or node count, nesting depth, number of
cross-references, constraint count, transformation steps, unresolved
ambiguities, loss events, validator diagnostics, and implementation effort.
Quantitative measures are interpreted alongside domain review; fewer nodes do
not automatically mean a better model.

## Migration classes

Every P5 construct in a case receives one of these migration outcomes:

| Outcome | Meaning |
|---|---|
| exact | the relevant structure and semantics map directly and reversibly |
| normalized | semantics remain, while declared lexical distinctions change |
| equivalent | the representation changes but the declared meaning is preserved |
| policy-dependent | more than one target is possible and a named policy is required |
| enriched | migration requires external or inferred information, recorded as such |
| partial | only a declared subset can be represented |
| unsupported | no valid target exists under the selected model or binding |

Migration reports identify the source object, target object, applied rule,
confidence or determinism, warnings, information loss, manual intervention, and
reverse-mapping behavior.

## Migration pipeline

```text
P5 document + P5 customization + baseline version
    -> P5 validation and feature inventory
        -> normalized P5 interpretation
            -> explicit migration rules
                -> candidate P6 model
                    -> P6 blueprint validation
                        -> selected serialization
                            -> semantic and loss report
```

The source customization is part of the migration input. Validating only
against TEI All can miss project-specific restrictions and extensions that
determine the intended meaning.

## Acceptance rule

A design decision is example-ready when its valid behavior, invalid behavior,
migration effect, and serialization effect are all testable. It becomes a
candidate recommendation only after representative examples and disconfirming
cases have been evaluated against grounded P5 knowledge.
