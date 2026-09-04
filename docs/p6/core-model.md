# Candidate P6 core model

Status: modeling hypothesis
Authority: independent project proposal, subject to evidence and prototyping

This document defines the smallest useful candidate for a
serialization-independent P6 model. It is deliberately a conceptual contract,
not yet a schema or implementation. Its purpose is to make competing
formalizations comparable.

## Modeling target

The core must represent textual documents that combine ordered content,
structural containment, metadata, annotation, references, overlapping regions,
and graph relations. It must also support domain-specific restrictions and
extensions without making a particular serialization normative.

A plain tree is insufficient when structures overlap or annotations are
stand-off. A plain unordered graph is insufficient when textual sequence and
mixed content matter. The working hypothesis is therefore a typed, attributed,
ordered graph with explicit text regions and named hierarchies.

## Four modeling levels

The design separates four levels that P5 implementations often encounter
through different surfaces:

| Level | Role | Example responsibility |
|---|---|---|
| metamodel | defines what a P6 model may express | concept, property, relation, sequence, constraint |
| domain model | defines shared TEI concepts | paragraph, person, witness, reading, annotation |
| blueprint | selects and constrains a coherent usage contract | scholarly text, dictionary, manuscript description |
| instance | records a particular encoded object | nodes, text, values, links, spans, declarations |

A customization derives from a declared domain model or blueprint and records
every restriction, extension, alias, and conflict resolution. It does not
silently modify the meaning of a shared concept.

## Candidate primitives

The following primitives form the current hypothesis:

| Primitive | Meaning |
|---|---|
| concept | a stable semantic type with an identifier and definition |
| node | an instance of one or more compatible concepts |
| property | a typed value attached to a node or relation |
| text segment | an immutable or versioned sequence of textual units |
| content sequence | an ordered list of text items, nodes, or references |
| hierarchy | a named, directed containment view over nodes and sequences |
| relation | a typed directed or undirected association between identified objects |
| span | an identified region anchored by boundaries in a content sequence |
| constraint | a named rule with scope, severity, and test semantics |
| declaration | the blueprint, language, version, and binding context of an instance |

Text, containment, and relation are separate primitives. This avoids treating a
character sequence as an accidental property of XML, treating every relation
as containment, or forcing overlapping structures into a single tree.

## Abstract structure

A candidate instance can be sketched as:

```text
I = (D, N, X, Q, H, R, S, V)

D  declaration and version context
N  identified typed nodes
X  text segments
Q  ordered content sequences
H  named containment hierarchies
R  typed relations
S  anchored spans
V  property values and datatypes
```

This notation does not decide an implementation language. Its value is that a
binding can state how every component is represented and whether reconstruction
is exact.

## Order and mixed content

Order is semantic only where the model declares an ordered sequence. Object
member order in JSON, triple order in RDF, attribute order in XML, and map order
in YAML must not acquire meaning accidentally.

A content sequence contains explicit items. An item may be a text segment, a
contained node, or a reference to another identified object. Inline annotation
can therefore be represented as contained structure when properly nested or as
a span/relation when nesting would create false semantics.

The model must define normalization boundaries: line-ending normalization,
Unicode normalization, whitespace policy, and whether lexical distinctions such
as entity references are semantic, binding-specific, or preservation metadata.

## Hierarchy, overlap, and stand-off annotation

Each hierarchy is named and has its own parent/child relation. A blueprint may
declare one hierarchy as the preferred serialization tree without implying that
other hierarchies are less meaningful. Nodes may participate in more than one
hierarchy when the relevant constraints allow it.

Spans point to stable boundaries in an ordered sequence. They support overlap,
discontinuous annotation, and stand-off layers without splitting the underlying
text merely to satisfy one serialization. The design must still decide how
boundaries survive editing and how text versions affect anchored annotations.

## Identity and references

Every addressable model object has an identity distinct from its display label,
serialization-local key, file path, or namespace prefix. Bindings may use XML
IDs, JSON keys, IRIs, blank nodes, or external indexes, but their mapping
contract must state how canonical identity is preserved.

References resolve within a declared dataset or package context. Broken,
ambiguous, cyclic, or version-incompatible references receive defined
diagnostics rather than processor-dependent behavior.

## Properties and datatypes

Property definitions declare domain, range, cardinality, ordering where
relevant, default behavior, and whether values are literals, identifiers,
references, or structured values. Language-tagged strings, dates, measures,
uncertain values, and controlled vocabularies require model-level semantics
rather than serialization-specific conventions.

Defaults are especially sensitive: a value inferred from a blueprint is not
the same as a value explicitly recorded by an encoder. The canonical
representation must preserve that distinction whenever it affects validation,
roundtripping, or interpretation.

## Constraints

Every constraint has a stable identifier, human-readable rationale, formal or
executable condition where possible, scope, severity, and diagnostic template.
Constraints may apply to the metamodel, domain model, blueprint, instance, or
binding. Context-sensitive constraints name the relevant hierarchy, ancestor,
neighbor, declaration, or relation instead of relying on an implicit processor
context.

Constraints should distinguish at least violations, warnings, and informative
normalizations. A binding-specific limitation is reported by the binding and
does not silently weaken the core model.

## Candidate invariants

Any formalization of this core should test at least these invariants:

1. identities are unique in their declared scope;
2. every type, property, hierarchy, relation, and constraint is declared;
3. references and span boundaries resolve or carry an explicit external status;
4. ordered sequence positions are deterministic;
5. each named containment hierarchy satisfies its declared acyclicity and
   ownership rules;
6. property values satisfy their datatype and cardinality contracts;
7. a blueprint cannot weaken a non-overridable core invariant;
8. a binding identifies every normalization or loss it introduces;
9. equivalent serializations normalize to the same semantic comparison form;
10. version and customization dependencies are explicit.

These are candidate invariants, not settled P6 requirements. Each must be tested
against grounded P5 examples and counterexamples before adoption.

## What remains deliberately undecided

The canonical formal language, granularity of text positions, identity model,
default semantics, hierarchy composition, ontology relationship, and precise
customization algebra remain open. `research-agenda.md` records the experiments
needed to choose among alternatives without turning this initial sketch into an
unexamined commitment.
