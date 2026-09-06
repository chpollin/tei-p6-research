---
title: Text Model
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-06"
related: [text-model-bindings, p6-architecture, p6-evaluation, experiments, specification, state]
---

# Text Model

Abstract Text Model 0.1 is this project's independent experimental definition
of a text model for a possible TEI P6. Its definitions are project posits, not
an adopted standard or a complete ontology of everything expressible in text.

This version models finite character sequences, attributed editorial groupings,
selections, structural readings, annotations, and typed relations through a
reference implementation and independently authored examples. The wider
programme draws requirements from P5, discussion records, literature, and
editorial practice. This version sets an experimental scope for that work.

The definition in sections 1 to 9 is the contract that the case runner
fingerprints and that the public model reference renders in full. The wider
core-model sketch in sections 10 and 11 and the serialization and conformance
contract in section 12 frame that bounded candidate. Neither is an
implementation inventory.

## 1. What the objects mean

An instance is a finite package of records with distinct, package-local IDs.
The objects and relations are defined independently of their serialization.
The [reference bindings](text-model-bindings.md) encode the same package
in JSON, XML, or YAML. They are experimental exchange formats, not TEI P5
converters or official TEI P6 syntax.

| Object | Meaning and identity | Required information |
|---|---|---|
| Agent | An identified record of a responsible editor or processor. It does not prove the identity of an outside person. | ID, label |
| Concept | A locally defined semantic type for a node or relation. | ID, label, definition, applicable role |
| Text | An editorial grouping identity, whose positive membership is asserted through continuity claims. | ID, label |
| Version | A fixed finite Unicode sequence with declared frozen technical construction inputs. Equal sequences can have distinct version IDs. | ID, content, UTF-8 SHA-256, parent version IDs |
| Continuity claim | An agent's positive claim that specified versions belong to a text under an explicit criterion. | ID, text, nonempty version membership, agent, criterion |
| Selection | A version-bound specification of a location or locations, distinct from its resolution. | ID, version, selector |
| Reading | An attributed structural interpretation of one version. | ID, version, agent, label, nonempty collection of nodes |
| Reading node | A typed, identified occurrence in one reading, with a selected extent and optional parent. | ID, concept, selection, parent |
| Annotation | An attributed interpretive body linked to a selection, including a currently unresolved selection. | ID, agent, selection, body |
| Relation | An attributed, directed, typed link between any two identified package records. | ID, concept, source, target, agent |

All references resolve within one package. Reading nodes have package-wide
unique IDs independent of extent, type, and local label. Each concept has
exactly one role, `node` or `relation`. There is no subtype inference or ontology
alignment language. Humans or domain processors interpret the strings in
bodies, labels, definitions, and continuity criteria.

Every node is a textual reading node. Independent person, witness, carrier,
and other domain records, with their cardinality and range constraints, remain
outside v0.1. The wider sketch in section 11 is not an implementation
inventory.

Formally, let `V` be the finite set of version records and `c(v)` the sequence
of Unicode scalar values for a version `v`. A continuity claim is a tuple
`(text, agent, criterion, S)` with a nonempty subset `S` of `V`. Every declared
text must have at least one such claim. Versions may belong to several claims
and texts, or to none. This encodes attributed membership, not a globally
settled partition of all versions.

Membership omission makes no assertion of exclusion,
disagreement, or a different work. Two differently attributed groupings can
coexist without the validator deciding whether they are compatible. Negative
identity claims and closed-world grouping policies require a later contract.

The directed technical parent relation on versions is acyclic. Neither
parentage nor equal content establishes editorial continuity. `parents`
records declared technical inputs, not revisable
hypotheses about historical transmission. An empty list means no inputs
recorded, not an original or independent witness. The declaration does not
authenticate a production event or prove that all inputs were recorded.

## 2. Position, selection, and resolution

Positions count Unicode code points, not bytes, UTF-16 code units, grapheme
clusters, or tokens. Offsets range from zero to `len(c(v))`. No content
normalization occurs. Line endings, whitespace, case, and precomposed versus
decomposed characters remain distinct. A combining mark may be selected independently.
The prototype accepts only strings encodable as UTF-8, excluding lone surrogates.

Three selector forms are available.

| Selector | Definition | Result |
|---|---|---|
| `point` | One integer offset, including an endpoint or offset zero in an empty version. | One point target |
| `ranges` | A nonempty, ascending sequence of disjoint nonempty half-open intervals `[start,end)`, each carrying the exact selected quote. Adjacent intervals are permitted. | One region target containing all its ordered segments |
| `quote` | A nonempty exact string with optional immediately adjacent literal prefix and suffix, and explicit `match: one` or `match: all`. | One target per matching occurrence, subject to the match policy |

A discontinuous region is **one aggregate target**. Intentional quotation
plurality produces **separate targets**. These structures must not be flattened
into one another. Adjacent range segments retain their boundaries rather than
being silently merged.

For example, in `aaa`, `quote(exact="aa", match="all")` resolves to two
independent targets `[0,2)` and `[1,3)`. With `match="one"`, those same
occurrences are ambiguous candidates and no target is accepted. Encoding the
two overlapping intervals as components of one `ranges` selector is invalid,
because the components of that aggregate must be disjoint.

Resolution is `{version, status, targets, candidates}`. Matches are enumerated
by ascending start position, including overlapping occurrences. `candidates`
is always present and empty except for ambiguous single-choice selection.
Zero quotation matches gives `absent`, an empty target list and `W_ABSENT`.
Multiple `one` matches gives `ambiguous`, an empty target list and
`W_AMBIGUOUS`. Neither condition alone invalidates a well-formed package.
An annotation can preserve this unresolved specification for editorial review.

## 3. Structural readings and order

A reading is a finite forest of nodes over one version. Each node must select
exactly one nonempty contiguous region in that version. A region with adjacent
segments is contiguous. Its original segmentation remains in the resolution,
while its enclosing interval is used for hierarchy checks. A gap, point,
absent or ambiguous selection, or several independent targets is not a valid
reading-node extent in this version of the model.

Every parent belongs to the same reading, and the parent relation is acyclic.
For every edge `parent -> child`, the child's interval is contained in the
parent's interval. Siblings, including forest roots, do not overlap. Touching
intervals are allowed. Sibling order follows increasing start position and is
independent of serialized record order. Coverage need not be complete. Parent and
child may have equal extents.

Different readings can cross or disagree. For the fixed sequence `abcd`, one
reading can divide `[0,2)` and `[2,4)`, while another divides `[0,1)` and
`[1,4)`. Each is a valid partition within its own reading. Both preserve their
own nodes, type assignments, and responsible agent. The model does not select
a preferred reading or turn one reading into the sequence itself. Typed
relations can link nodes across readings without merging their identities.

Relation cycles and self-links are permitted. A relation's type definition
does not automatically constrain its endpoints beyond the closed reference
rule. For example, a concept labeled `precedes` does not acquire temporal or
acyclic semantics from its label. Such domain rules need an explicit extension.

## 4. Version integrity and editorial change

The hash checks the exact current UTF-8 content. It does not prove that a
record was historically immutable. `check_revision(before, after)` separately
checks reused version IDs for changed content, hash, or parent membership.
Both packages must first validate. Parent-array order is irrelevant. A caller
must declare that these packages share an ID scope. Coincidentally equal local
IDs in unrelated packages are not evidence of a rewrite.

Removing a version from a later package is not itself a rewrite. A new version
uses a new ID and may name earlier versions as technical inputs. Correcting
the recorded technical inputs also requires a new version-record ID, even
when the character content is unchanged. This deliberate rigidity protects
the technical record's identity. It does not cover every editorial meaning of
"version" or provide a persistent history service. Concept definitions,
annotations, and editorial groupings do not acquire historical immutability
through the version-specific check.

`propose_reanchor(package, selection, target_version, continuity)` requires a
valid package, a resolved source selection, and an explicit continuity claim
containing both versions. A quotation selector retains its exact string,
context, and match policy. A single-segment range becomes a quotation search
with `match="one"`. Point and multisegment reanchoring are unsupported, even
when multiple segments are adjacent.

The result is a proposal with its target resolution and `accepted: false`.
Absent or ambiguous destination matches remain visible. It never edits a
selection, annotation, or package, and never approves the interpretation for
the changed text. Operation diagnostics describe invalid requests or destination
resolution. Unrelated selection warnings are not copied. An unresolved source
causes `E_REANCHOR`. Invalid packages return their validation diagnostics.

### Optional editorial provenance profile

The [editorial provenance profile](../experiments/editorial_cases/profile.json)
uses existing v0.1 concepts and relations to represent revisable historical
derivation hypotheses. It changes neither the base record shape nor base
conformance. Only its exactly defined reserved concepts invoke these rules.
Giving another concept the label "derived from" does not.

An `ep-derived-from` relation links a subject version to a proposed historical
source version and identifies the agent making that hypothesis. An
`ep-supersedes` relation links a new derivation claim to an old one. Both claims
must concern the same subject version and have the same agent as the
supersession relation. Supersession is acyclic. Historical hypothesis cycles
and contradictory hypotheses may coexist without a truth verdict.

For a synthetic example, an editor initially proposes `B derives from A` and
later proposes `B derives from C`. Append the second claim and a supersession
link to the first. B's content, ID, technical parents, selections, and
annotations need not change. Both claims remain in the package, while the
current-claim view returns the second. An unsuperseded claim by another editor
also remains current. The profile does not silently rank agents or pick one
surviving branch. This example is not a historical finding about the diary
used in the separate
[editorial case study](experiments.md#editorial-case-study-of-one-diary-and-three-fragments).

The APIs in `tools.models.editorial_profile` are `validate_profile`,
`check_profile_revision`, and `current_derivations`. Profile revision first
validates both packages and applies the base version check, then requires every
prior derivation and supersession relation to remain present with its exact
record. Removal or rewriting gives `E_CLAIM_REWRITE`. Other profile diagnostics
identify invalid concepts, endpoints, supersession, or cycles. The caller must
declare a shared ID scope, just as for base revision comparison.

`current_derivations` returns deep copies of all derivation claims that are not
targets of supersession, sorted by ID, optionally filtered by agent or subject.
This order conveys no authority. All three operations leave inputs unchanged.
**Base `check_revision` alone does not enforce append-only claim history.**
Neither profile conformance nor a current historical hypothesis establishes
editorial continuity or authorizes reanchoring.

The profile has no bare withdrawal, negative derivation claims, cross-agent
supersession, external evidence-link semantics, authenticity guarantee, or
persistent history service. These remain extension questions for a broader
account of provenance, belief, or editorial identity.

## 5. Conformance and comparison

The exact fields are defined in
[`spec.json`](../experiments/abstract_text_v01/spec.json). The package has
`model_version: "0.1"` and the nine named collection arrays. Reading nodes are
nested within readings. Records reject unknown fields, missing fields, duplicate
IDs, and wrongly typed references. IDs match `[A-Za-z][A-Za-z0-9._:-]*`.
Integers exclude booleans. Empty collection arrays are allowed. An empty reading
and a text without a continuity claim are invalid.

`validate_model` returns `valid`, `all_selections_resolved`, sorted unique
`{code,path}` diagnostics, and resolutions indexed by selection ID. Any
structural error makes `valid` false and suppresses all resolutions. Warnings
alone retain `valid: true`, while absent or ambiguous selections make
`all_selections_resolved` false. An empty package is valid and vacuously resolved.
That result says nothing about its scholarly value.

| Diagnostics | Meaning |
|---|---|
| `E_SHAPE`, `E_ID`, `E_DUPLICATE_ID` | Malformed record, identifier, or repeated identity |
| `E_REFERENCE`, `E_TYPE` | Missing/wrong-category reference or wrong concept role |
| `E_HASH`, `E_VERSION_CYCLE`, `E_CONTINUITY` | Current content hash, ancestry, or editorial grouping constraint fails |
| `E_SELECTOR`, `E_BOUNDS`, `E_QUOTE` | Selector shape/type, coordinate, or exact range quotation fails |
| `E_READING_TARGET`, `E_READING_PARENT`, `E_READING_CYCLE` | Reading target or parent forest fails |
| `E_CONTAINMENT`, `E_SIBLING_OVERLAP` | Reading intervals violate containment or sibling separation |
| `E_VERSION_REWRITE` | A reused version ID changes frozen version information |
| `E_REANCHOR`, `E_REANCHOR_UNSUPPORTED` | Reanchor request fails or requires an unsupported selector operation |
| `W_ABSENT`, `W_AMBIGUOUS` | Well-formed quotation cannot resolve to the required target(s) |

`canonical_bytes` produces deterministic UTF-8 JSON for a valid package.
`equivalent` compares valid packages under rule R11. This is deliberately a
strict, declared comparison relation, not a universal definition of textual
or semantic equivalence. It ignores object-key order, registry order (including
node order), and order of version parents and continuity memberships. It
preserves IDs, strings, attribution, concepts, policies, selection kinds and
modes, segmentation, hierarchy edges, and bodies. It performs no ID renaming
or Unicode normalization. Thus two selectors that happen to resolve to the
same target may remain inequivalent because they encode different policies.

All public operations must leave their inputs unchanged. JSON byte equality,
R11 equivalence, equality of resolved targets, and suitability for an editorial
task are four different questions. The JSON, XML, and YAML
[bindings](text-model-bindings.md) implement a separate preservation
contract for model packages. Their round trips do not establish preservation
during P5 conversion. RDF remains outside the binding contract.

## 6. Requirement and test ledger

Every rule is a project contract. Source findings motivate tests without
logically entailing the chosen primitives. The source-supported argument and
its explicit posits are in [P6 Design](../40_output/12-p6-design.md).

| Rule | Observable distinction or constraint | Origin of requirement |
|---|---|---|
| R01 | Equal content, labels, or extents do not collapse IDs. | Project identity posit. String/continuity distinction motivates comparison. |
| R02 | References resolve by category. Only the declared parent graphs are acyclic. | Closed-package processing posit. |
| R03 | Current hash integrity differs from detecting rewritten content or frozen technical inputs under a reused version ID. | Reproducibility and revision posit. |
| R04 | Editorial membership is attributed and distinct from technical construction or historical derivation hypotheses. | Continuity-policy posit motivated by the string-transformation discussion. |
| R05 | Exact code points and endpoint positions survive processing. | Bounded coordinate-system choice. P5 point targeting motivates a test. |
| R06 | Discontinuous aggregation, plurality, and overlapping occurrences remain distinct. | Selection posit motivated by the W3C and historical span discussions. |
| R07 | Missing and ambiguous targets remain explicit editorial states. | Task-policy posit compared with deliberate all-match behavior. |
| R08 | Competing readings coexist while each reading satisfies its own forest constraints. | Attributed-structure posit motivated by the hierarchy discussion. |
| R09 | Concept roles are explicit without claiming to evaluate their meaning. | Ontological boundary and implementation posit. |
| R10 | Validation and proposal creation cannot silently change the research object. | Inspectable processing posit. |
| R11 | Exchange comparison preserves declared distinctions and policies. | Independent comparison-oracle posit. |
| R12 | Retargeting requires explicit continuity and remains an unaccepted proposal. | Editorial review and change-control posit. |
| R13 | Validity does not imply completeness, adequacy, or useful content. | Scope and interpretation boundary. |

The independent case file labels each case with the rules it challenges. The
runner rejects missing rule or operation coverage and compares actual outcomes
with frozen expectations, including full selection resolutions. This verifies
the declared examples. Rule labels are not a proof that every possible input
has been covered. Unit tests additionally exercise malformed inputs and the
test runner's rejection of stale or incomplete reports.

## 7. Competing architecture and migration questions

Compare this candidate, **versioned sequences with attributed forests**, with
an alternative, **one primary tree plus a separately attributed stand-off
structure**. The full-scope alternative in this table is conceptual, not a
claim about every P5 processor. The separate editorial case study implements
a smaller parsed-tree baseline for three fragment tasks. It does not implement
every operation or observation in this table.

| Same required observation | Sequence and forests candidate | Primary tree plus stand-off alternative |
|---|---|---|
| Two crossing readings over fixed content | Both readings refer to the same sequence. Neither is privileged. | One structure occupies the primary tree. A secondary structure must preserve its own nodes, attribution, and intervals. |
| One discontinuous annotation | One region contains several segments. | An annotation refers to several fragments under an explicit aggregation policy. |
| Deliberately annotate every quotation occurrence | `match=all` yields separate targets. | A selection layer enumerates occurrences with an explicit plural policy. |
| Preserve uncertainty about one intended occurrence | Candidate targets are retained without accepted targets. | Stand-off selection metadata must preserve ambiguity rather than choosing a node. |
| Review an annotation after a text edit | Version-specific locations and a continuity-qualified proposal. | Versioned tree snapshots and a reviewable target mapping are needed. |

Both alternatives can be designed to preserve these observations. This table
therefore does not establish an expressivity winner. The candidate adds explicit
records and reference resolution. The alternative needs rules for the status
and processing of secondary structures. Which is easier to author, teach, query,
or maintain requires equivalent tasks and measurements.

The source baseline is P5 4.12.0 at
`113e933e21f016e2655518321e9d10214b8d9fcb`. The following are mapping questions,
not general conversion guarantees. The bounded fragment mapping and its
additional annotation binding are evaluated separately in the
[editorial case study](experiments.md#editorial-case-study-of-one-diary-and-three-fragments).

| Baseline area | Candidate destination | Unresolved preservation obligation |
|---|---|---|
| Point targeting, such as `anchor` | Version-bound point | Derive stable positions from mixed content without losing identifiers or context. |
| Interpretive spans and annotations | Selection plus attributed annotation | Preserve scope, target policies, responsibility, and annotation body semantics. |
| Document containment | One or more attributed readings | Account for mixed content, empty elements, nontextual objects, and source ordering. |
| Stand-off links and identifiers | Typed relations and selections | Specify external reference identity, direction, grouping, and dependencies. |
| ODD customization | No v0.1 counterpart | Define effective constraints, extension semantics, composition, and diagnostics. |

Repair within P5 could improve documentation or targeted processing tools.
Compatible evolution could add an explicit
selection/review contract while preserving existing document contracts. An
architectural replacement would additionally have to justify bindings and
migration costs. Deferral is appropriate for a requirement whose need or
preservation policy has not been established. The recommendation for this
experiment is to retain these options while testing the candidate. Adoption
would require independent editorial and migration evidence.

## 8. Run and inspect

Run from the repository root with Python 3.11 or newer.

```powershell
py -3 tools/check_abstract_text_v01.py --check
py -3 tools/check_abstract_text_v01.py --validate experiments/abstract_text_v01/examples/competing-readings.json
py -3 tools/check_abstract_text_v01.py --validate experiments/abstract_text_v01/examples/identity-and-reanchoring.json
py -3 tools/check_editorial_cases.py --check
py -3 -m pytest tests/models tests/test_check_abstract_text_v01.py
```

Use the Python launcher above on Windows or replace `py -3` with `python`.
The library API is in `tools.models.abstract_text`. The runner performs no
network access. To regenerate the deterministic experiment report after an
intentional change, omit `--check`. A report records input hashes, independent
expectations, actual outcomes, and failures. It is not a Vault grounding source.
Current results and dates belong in [state](state.md).

## 9. Human acceptance and remaining scope

Review each item with a separate **accept / revise / defer** decision and an
example or reason. These are editorial decisions, not approval of source truth.

1. Do version, text grouping, technical construction, historical hypotheses,
   and attribution express the intended identity distinctions, including the
   new-ID requirement for correcting technical parents and the absence of
   negative membership claims?
2. Do point, discontinuous region, plural targets, and unresolved single-choice
   selection have the right meanings for the chosen tasks?
3. Do two structural readings preserve the required disagreement, and where
   would contiguous-node forests exclude a legitimate structure?
4. Are strict R11 comparison and unaccepted reanchor proposals useful for review,
   or do the intended tasks require a different comparison or acceptance policy?
5. Can an editor explain and alter a supplied example without losing intended
   distinctions, and which declarations or diagnostics need improvement?

Formal checks can demonstrate executable outcomes for supplied instances,
detect constraint violations, and reproduce the bounded test record. They do
not establish universal expressivity, ontological adequacy, interpretation
truth, usability, community agreement, or a proof of consistency for all cases.

This version has no physical-carrier, image-area, audio-time, token, or grapheme
coordinate system. It has no full domain model, customization algebra,
effective ODD processor, RDF binding, whole-document migration converter,
collaborative editing protocol, or external identity resolver.
The JSON, XML, and YAML reference bindings exchange core model packages.
Discontinuous and plural selections
are available for annotations, but reading nodes require contiguous extents.
The experimental fragment binding does not remove those limits. Its separate
decoder supplies source-attribute and note semantics that the base model does
not validate. These boundaries must be challenged by independently selected
real cases before extending the model or recommending an architecture for TEI P6.

## 10. Terms of the wider sketch

The core-model sketch in section 11 predates the executable candidate and uses
its own primitive vocabulary. The mapping below reads the two definition tables
against each other. It names the nearest v0.1 record kind for each sketch
primitive and records where the two differ. A correspondence does not claim
that the record implements the primitive in full.

| Sketch primitive | Nearest v0.1 record kind | Difference |
|---|---|---|
| concept | Concept | A v0.1 concept has exactly one role, `node` or `relation`, and a local definition string. The sketch's versioned applicable definition has no v0.1 counterpart. |
| node | Reading node | A v0.1 node is an occurrence in exactly one attributed reading, with one concept and one contiguous extent. The sketch admits an instance of several compatible concepts. |
| text segment | Version | A version is an identified fixed Unicode sequence with hashed content and declared technical parents. |
| hierarchy | Reading | A reading is one attributed containment forest over one version. Several readings may cross without a preferred one. |
| relation | Relation | A v0.1 relation is directed, typed and attributed. The sketch also admits undirected associations. |
| span | Selection | A selection is version-bound and distinct from its resolution. Beyond the sketch's contiguous region it admits a point, a discontinuous region and plural quotation targets. |
| declaration | package `model_version` | Only the model version is declared in a package. The XML binding adds its own `binding_version`. Blueprint, language and binding context have no v0.1 counterpart. |
| property | none | Every v0.1 field is fixed by the record contract. There are no typed values attached to nodes or relations beyond those fields. |
| content sequence | none | Order in v0.1 is the code point order of a version. Sibling order in a reading is derived from selected positions and is never recorded. |
| constraint | none | Rules R01 to R13 and their diagnostics are fixed in the implementation. Instances carry no constraint records. |

Agent, Text, Continuity claim and Annotation have no primitive of their own in
the sketch. The sketch treats attribution and the distinction between an
object, its description and a claim about it as a composition question for
experiments.

## 11. The wider sketch

The sketch is an independent modeling hypothesis, subject to evidence and
prototyping. It defines questions for comparing a serialization-independent
core with alternative models. It does not specify an implementation or
establish that its primitives are necessary or sufficient. Generic domain
entities, properties, customization, and the complete metamodel below remain
outside the v0.1 implementation.

### Modeling target

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

### Four modeling levels

The candidate separates four modeling levels for evaluation. The candidate
layers of the [P6 architecture](p6-architecture.md#candidate-layers) name the
same stack and add a project customization step between blueprint and
instance.

| Level | Role | Example responsibility |
|---|---|---|
| metamodel | defines what a P6 model may express | concept, property, relation, sequence, constraint |
| domain model | defines shared TEI concepts | paragraph, person, witness, reading, annotation |
| blueprint | selects and constrains a coherent usage contract | scholarly text, dictionary, manuscript description |
| instance | records a particular encoded object | nodes, text, values, links, spans, declarations |

A customization derives from a declared domain model or blueprint and records
every restriction, extension, alias, and conflict resolution. It does not
silently modify the meaning of a shared concept.

### Candidate primitives

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

### Abstract structure

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

### Order and mixed content

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

### Hierarchy, overlap, and stand-off annotation

Each hierarchy is named and has its own parent/child relation. A blueprint may
declare one hierarchy as the preferred serialization tree without implying that
other hierarchies are less meaningful. Nodes may participate in more than one
hierarchy when the relevant constraints allow it.

A region selector is evaluated against a declared sequence or text version.
A contiguous interval and a discontinuous selection require distinguishable
selection structures. Neither implies that the selected material remains the
same after editing. Experiments must state how versions, boundaries, and
repeated occurrences are identified and whether cross-version correspondence
is asserted, computed, or unresolved. The region record of the bounded
[text identity pilot](experiments.md#text-identity-and-annotation-pilot) is
one experimental representation, not a definition imposed on this general
model.

### Identity and references

Every addressable model object has an identity distinct from its display label,
serialization-local key, file path, or namespace prefix. Bindings may use XML
IDs, JSON keys, IRIs, blank nodes, or external indexes, but their mapping
contract must state how canonical identity is preserved.

References resolve within a declared dataset or package context. Distinguish
known missing or incompatible targets from targets that cannot yet be checked.
Cycles violate a rule only where the relevant relation or processing contract
prohibits them. Diagnostics name the condition and the rule being evaluated.

### Properties and datatypes

Property definitions declare domain, range, cardinality, ordering where
relevant, default behavior, and whether values are literals, identifiers,
references, or structured values. Language-tagged strings, dates, measures,
uncertain values, and controlled vocabularies require model-level semantics
rather than serialization-specific conventions.

Values inferred from a blueprint and values explicitly recorded by an encoder
must remain distinguishable whenever that affects validation,
roundtripping, or interpretation.

### Constraints

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
independently specified comparison relation, as section 12 states for the
serialization contract. These proposed obligations require evaluation against
P5 cases and counterexamples before adoption.

### What remains deliberately undecided

For this broader model, formal language, position units, identity rules,
defaults, hierarchy composition, ontology connections, and customization
algebra remain research questions. Version 0.1 fixes a subset for its bounded
contract. The [plan](plan.md) defines the comparisons needed to assess
extensions.

## 12. Serialization and conformance

P6 can be serialization-independent only if independence has testable meaning.
This section defines the candidate contract between the abstract model,
serialization bindings, validators, converters, and conformance reports. The
contract is an independent project proposal, subject to prototyping. The
[reference bindings](text-model-bindings.md) instantiate it for v0.1 packages
in JSON, XML and YAML.

### Terms

A **serialization binding** maps the core model to and from a concrete syntax.
A **syntax profile** restricts options within that syntax. A **projection**
exposes a declared subset for a particular task. A **canonical intermediate
representation** is the comparison form used to test semantic equivalence; it
is not automatically the public authoring format.

Supporting a syntax does not mean that every feature is lossless. The contract
must name the supported conformance level for each model feature and use case.

### Conformance classes

Report model preservation separately from lexical or byte preservation. The
following are proposed binding classes, not Grounded Vault research statuses.

| Class | Required behavior |
|---|---|
| model-lossless | model to binding to model preserves every distinction required by the named model and blueprint |
| declared-equivalence | preserves an explicitly defined task-specific equivalence relation, naming which model differences may be ignored |
| projection | a named subset is exported and omitted information is reported |
| unsupported | the binding rejects the construct with a defined diagnostic |

A conversion may be model-lossless for one blueprint and a projection for another.
Conformance is therefore reported against the model version, blueprint,
binding version, and declared class rather than against the file extension
alone.

Lexical normalization is compatible with model-lossless conversion only when
the changed distinction is outside that model contract. Byte identity is a
separate archival property. Ignoring differences in local labels is permissible
only if the declared task does not require those labels and required object
identities remain recoverable.

### Candidate bindings

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

XML, JSON and YAML are implemented for v0.1 packages by the
[reference bindings](text-model-bindings.md), whose preservation laws are
checked against every valid existing case. JSON-LD, RDF datasets, Turtle or
TriG, CBOR or MessagePack and CSV or TSV remain candidates without a decoder
or checked contract.

The initial target should be a small set of representative bindings rather than
a promise to support every syntax. XML tests hierarchy and mixed content;
JSON-LD tests application usability and graph mapping; RDF tests semantic graph
interchange; YAML can test a human-readable JSON-compatible form. Additional
bindings enter only with a stated use case and conformance contract.

### Required binding package

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

### Validation stack

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

The diagram groups responsibilities; implementations must follow the actual
dependencies between checks. Resolve and pin definitions needed by a rule
before evaluating it. Report a check as not evaluated when a required
dependency is unavailable, separately from a violated rule. Reference cycles
are violations only where the relevant relation or contract prohibits them.

Candidate technologies include RELAX NG and Schematron for XML, JSON Schema for
JSON-shaped data, SHACL or ShEx for RDF graphs, and an implementation-neutral
invariant layer for rules that those languages cannot express consistently.
JSON-LD may require both document-shape validation and graph validation after
expansion.

Passing a native schema is not sufficient for P6 conformance. It establishes
only the part of the contract assigned to that validation layer.

### Semantic comparison

Define the comparison relation before evaluating a converter, with examples
that must compare equal and examples that must remain different. Distinguish
identity preservation from permitted renaming of local identifiers. A
converter's own normalization is not sufficient evidence of preserved meaning.

Model roundtrips compare the declared model distinctions; byte preservation
requires a separate test. The comparison contract names its treatment of
order, identity, datatypes, language, explicit versus inferred values,
relations, spans, and named hierarchies. Any ignored difference needs a
task-specific rationale and an independently reviewed expected outcome.

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

### Loss reporting

Loss is a result, not an exception message. A machine-readable loss report
identifies the affected object, model feature, cause, severity, recoverability,
and possible remediation. It distinguishes lexical normalization, semantic
normalization, ambiguity requiring policy, intentional projection, and
unsupported information.

A conversion that completes while silently dropping information fails the
binding contract.

### Genericity limit

P6 should be generic at the semantic level, not reduced to the smallest common
denominator of all syntaxes. Ordered mixed text, multiple hierarchies, or typed
relations remain part of the model even when a binding must encode them
verbosely or declare them unsupported. This keeps serialization independence
from becoming semantic impoverishment.
