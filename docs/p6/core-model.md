# Candidate P6 core model

An independent modeling hypothesis, subject to evidence and prototyping.

This broader sketch defines questions for comparing a serialization-independent
core with alternative models. It does not specify an implementation or
establish that its primitives are necessary or sufficient.

The [Abstract Text Model 0.1 definition](abstract-text-model-v0.1.md) specifies
the bounded executable candidate. It implements selected distinctions from
this sketch. Generic domain entities, properties, customization, and the
complete metamodel below remain outside that implementation.

## Modeling target

The core must represent textual documents that combine ordered content,
structural containment, metadata, annotation, references, overlapping regions,
and graph relations. It must also support domain-specific restrictions and
extensions without making a particular serialization normative.

The comparison requires explicit representations of order, containment,
overlap, and stand-off annotation. These requirements do not by themselves
select one data structure. A typed, attributed graph with ordered sequences and
named hierarchies is one candidate. A primary tree with separately modeled
references and annotations is another. Compare their preservation of the same
distinctions, authoring and processing costs, and migration behavior before
preferring either.

## Four modeling levels

The candidate separates four modeling levels for evaluation.

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

These primitives are proposed for comparison.

| Primitive | Meaning |
|---|---|
| concept | an identified semantic type whose applicable definition is versioned |
| node | an instance of one or more compatible concepts |
| property | a typed value attached to a node or relation |
| text segment | an immutable or versioned sequence of textual units |
| content sequence | an ordered list of occurrences of text items, nodes, or references |
| hierarchy | a named, directed containment view over nodes and sequences |
| relation | a typed directed or undirected association between identified objects |
| span | a contiguous region addressed by a selector within a declared sequence or version |
| constraint | a named rule with scope, severity, and test semantics |
| declaration | the blueprint, language, version, and binding context of an instance |

This candidate separates text, containment, and other relations. Experiments
must test which distinctions require separate primitives and which can be
expressed adequately through composition or a domain-specific profile.

Distinguish an encoding object, the object it describes, and an attributed claim
about that object when a use case requires it. A record describing a person is
not identical to that person. Two annotations of one region need not make the
same claim. Compare direct properties with independently addressable statements
using conflicting attributions, separate responsibility, and revision of one
claim. An extra statement object must
serve a demonstrated need for addressing, provenance, or interpretation.

## Abstract structure

A candidate instance has the following proposed components.

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

A content sequence records ordered occurrences of text segments, nodes, or
references. The formalization must state whether repeated references denote
distinct occurrences and how an anchor identifies the intended occurrence.
Sequence membership and hierarchical containment need an explicit consistency
rule. Neither may silently override the other. Converting contained annotation
to a separate region claim requires a mapping of target, scope, and
interpretation. Proper nesting alone does not establish equivalence.

The model must define policies for line endings, Unicode, and whitespace.
It must classify lexical distinctions such as entity references as semantic,
binding-specific, or preservation metadata.

## Hierarchy, overlap, and stand-off annotation

Each hierarchy is named and has its own parent/child relation. A blueprint may
declare one hierarchy as the preferred serialization tree without implying that
other hierarchies are less meaningful. Nodes may participate in more than one
hierarchy when the relevant constraints allow it.

A region selector is evaluated against a declared sequence or text version.
A contiguous interval and a discontinuous selection require distinguishable
selection structures. Neither implies that the selected material remains the
same after editing. Experiments must state how versions, boundaries, and
repeated occurrences are identified and whether cross-version correspondence
is asserted, computed, or unresolved. The bounded pilot's region record is one
experimental representation, not a definition imposed on this general model.

## Identity and references

Every addressable model object has an identity distinct from its display label,
serialization-local key, file path, or namespace prefix. Bindings may use XML
IDs, JSON keys, IRIs, blank nodes, or external indexes, but their mapping
contract must state how canonical identity is preserved.

References resolve within a declared dataset or package context. Distinguish
known missing or incompatible targets from targets that cannot yet be checked.
Cycles violate a rule only where the relevant relation or processing contract
prohibits them. Diagnostics name the condition and the rule being evaluated.

## Properties and datatypes

Property definitions declare domain, range, cardinality, ordering where
relevant, default behavior, and whether values are literals, identifiers,
references, or structured values. Language-tagged strings, dates, measures,
uncertain values, and controlled vocabularies require model-level semantics
rather than serialization-specific conventions.

Values inferred from a blueprint and values explicitly recorded by an encoder
must remain distinguishable whenever that affects validation,
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

A formalization must check unique identity, complete declarations, reference
resolution, deterministic order, and the graph and value rules defined above.
Version and customization dependencies must be explicit. A blueprint cannot
weaken a core rule designated as non-overridable.

Bindings must identify their normalizations and losses and preserve an
independently specified comparison relation. Tests must include both equivalent
instances and pairs that must remain distinct. These proposed obligations
require evaluation against P5 cases and counterexamples before adoption.

## What remains deliberately undecided

For this broader model, formal language, position units, identity rules,
defaults, hierarchy composition, ontology connections, and customization
algebra remain research questions. Version 0.1 fixes a subset for its bounded
contract. [research-agenda.md](research-agenda.md) defines the comparisons
needed to assess extensions.
