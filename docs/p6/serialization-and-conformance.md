# Serialization and conformance

Status: candidate contract
Authority: independent project proposal, subject to prototyping

P6 can be serialization-independent only if independence has testable meaning.
This document defines the candidate contract between the abstract model,
serialization bindings, validators, converters, and conformance reports.

## Terms

A **serialization binding** maps the core model to and from a concrete syntax.
A **syntax profile** restricts options within that syntax. A **projection**
exposes a declared subset for a particular task. A **canonical intermediate
representation** is the comparison form used to test semantic equivalence; it
is not automatically the public authoring format.

Supporting a syntax does not mean that every feature is lossless. The contract
must name the supported conformance level for each model feature and use case.

## Conformance classes

| Class | Required behavior |
|---|---|
| lossless | model to binding to model preserves every normative distinction |
| semantic | declared meaning is preserved, but lexical or presentation details may normalize |
| projection | a named subset is exported and omitted information is reported |
| unsupported | the binding rejects the construct with a defined diagnostic |

A document may be lossless for one blueprint and only a projection for another.
Conformance is therefore reported against the model version, blueprint,
binding version, and declared class rather than against the file extension
alone.

## Candidate bindings

| Binding | Intended role | Principal design concern |
|---|---|---|
| XML | hierarchical authoring and exchange | mixed content, namespaces, and mapping graph structures |
| JSON | application and API representation | explicit order, mixed content, identity, and duplicate-key avoidance |
| YAML | human-readable form of the JSON data model | preventing YAML-specific tags, aliases, or map behavior from changing semantics |
| JSON-LD | JSON authoring with linked-data semantics | reconciling document shape with RDF expansion |
| RDF datasets | graph interchange and semantic integration | explicit order, closed-world constraints, and text-region representation |
| Turtle or TriG | readable concrete RDF syntax | same model obligations as the RDF dataset binding |
| CBOR or MessagePack | compact transport of a defined JSON profile | semantic identity with the JSON profile and deterministic decoding |
| CSV or TSV | bounded tabular projection | explicit declaration of omitted hierarchy, text, and relations |

The initial target should be a small set of representative bindings rather than
a promise to support every syntax. XML tests hierarchy and mixed content;
JSON-LD tests application usability and graph mapping; RDF tests semantic graph
interchange; YAML can test a human-readable JSON-compatible form. Additional
bindings enter only with a stated use case and conformance contract.

## Required binding package

Every normative binding should provide one versioned package containing:

1. mapping rules for every core primitive used by the supported blueprint;
2. syntax-level schema or shape definitions;
3. normalization and default rules;
4. identifier, reference, datatype, language, order, and namespace behavior;
5. a feature-by-feature conformance and loss matrix;
6. positive, negative, boundary, and hostile-input fixtures;
7. model-to-syntax and syntax-to-model converter behavior;
8. stable diagnostic identifiers;
9. canonical comparison and roundtrip expectations;
10. version compatibility and deprecation rules.

If reconstruction depends on information outside the serialized document, the
binding declares the required package context rather than claiming standalone
losslessness.

## Validation stack

Validation is layered so that success at one level cannot hide failure at
another:

```text
syntax parsing
    -> binding-shape validation
        -> canonical-model construction
            -> core invariants
                -> blueprint constraints
                    -> reference and package integrity
                        -> cross-binding conformance
```

Candidate technologies include RELAX NG and Schematron for XML, JSON Schema for
JSON-shaped data, SHACL or ShEx for RDF graphs, and an implementation-neutral
invariant layer for rules that those languages cannot express consistently.
JSON-LD may require both document-shape validation and graph validation after
expansion.

Passing a native schema is not sufficient for P6 conformance. It establishes
only the part of the contract assigned to that validation layer.

## Semantic comparison

Roundtrip tests compare normalized model states, not source bytes. The
comparison process must preserve semantic order, identity, datatypes, language,
explicit versus inferred values where relevant, relations, spans, and named
hierarchies.

Each roundtrip produces a report containing the input binding and version,
blueprint, normalization steps, losses, unsupported constructs, diagnostics,
and the result of semantic comparison. Byte-for-byte preservation may be an
optional archival profile but is not implied by semantic equivalence.

Expected test paths include:

```text
P5 XML -> migration -> P6 model -> P6 XML
P6 XML -> model -> JSON-LD -> model
P6 JSON-LD -> RDF dataset -> model
P6 model -> YAML -> model
P6 model -> projection -> explicit loss report
```

## Loss reporting

Loss is a result, not an exception message. A machine-readable loss report
identifies the affected object, model feature, cause, severity, recoverability,
and possible remediation. It distinguishes lexical normalization, semantic
normalization, ambiguity requiring policy, intentional projection, and
unsupported information.

A conversion that completes while silently dropping information fails the
binding contract.

## Genericity limit

P6 should be generic at the semantic level, not reduced to the smallest common
denominator of all syntaxes. Ordered mixed text, multiple hierarchies, or typed
relations remain part of the model even when a binding must encode them
verbosely or declare them unsupported. This keeps serialization independence
from becoming semantic impoverishment.
