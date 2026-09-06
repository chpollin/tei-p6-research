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
implementation inventory. Section 13 fixes the claim pattern and the
identifier policy that every later domain extension of the model follows.

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

## 13. Claim pattern and identifier policy

Every later domain extension of the model, for entities, names, events,
places and media, follows one pattern for the assertions it makes and one
policy for the identifiers it exchanges. This section fixes both before any
such extension is built. Its rules are project posits in the
[statement roles](p6-evaluation.md#statement-roles) of the evaluation
document, contracts for the prototype and hypotheses for comparison, and none
of them records an official TEI decision. The v0.1 record contract of
sections 1 to 5 stays unchanged.

### Claim records

An assertion that a package makes about the world or about the edition is a
record of its own. That a mention denotes an entity, that an entity bears a
name, that a person was born at a date, that two entities are related, that a
version belongs to a text, each is a claim record with its own identity, a
responsible agent, a creation instant, an optional certainty, an optional
temporal scope of validity and a revisable status. No such assertion is a bare
attribute of the record it is about. A record that is not a claim carries only
what constitutes it, an identity, a display label, a definition or frozen
technical construction data.

| Field | Contract | In v0.1 |
|---|---|---|
| `id` | Package-local ID under the grammar of section 1, package-wide unique, nested claims included. | present |
| `agent` | Agent ID of the record responsible for the claim. | present |
| `created` | RFC 3339 date-time `YYYY-MM-DDTHH:MM:SS`, optional fraction, `Z` designator, checked for lexical form and calendar validity. It dates the record and orders nothing. | absent |
| `status` | Exactly one of `proposed`, `asserted`, `withdrawn`. | absent, read as `asserted` |
| `certainty` | Optional. Exactly one of `high`, `medium`, `low`, the agent's own qualification, without numeric comparison. | absent |
| `valid` | Optional. Object with optional `from` and `until`, at least one present, each a proleptic Gregorian date at year, month or day precision matching `[0-9]{4}(-[0-9]{2}(-[0-9]{2})?)?`. With `from` read as the start and `until` as the end of its calendar unit, `from` is not after `until`. It bounds the claimed state of affairs. | absent |
| `supersedes` | Duplicate-free array of IDs of earlier claims of the same kind, by the same agent, about the same subject; empty when nothing is revised. | `ep-supersedes` relations of the profile only |
| subject fields | Kind-specific references to the records the claim is about, declared as subject fields in the kind's record contract. | present |
| content fields | Kind-specific values the claim states about its subject, such as a criterion, a body, a name form or a date. | present |

`created` is transaction time, `valid` is valid time, and a date inside the
content of a claim, such as the date of a birth, is neither.

Formally, a claim kind `K` declares its subject fields `s_1, …, s_n` and its
content fields. A claim of kind `K` is a tuple
`(id, agent, created, status, certainty, valid, supersedes, s_1, …, s_n, content)`
with subject `(s_1, …, s_n)`. Two claims of one kind with equal subject and
content under distinct IDs are two records, as R01 requires. Every record
kind either constitutes an identity or a specification, as agent, concept,
text, version and selection do, or asserts something about identified records
or their referents. Every kind of the second sort is a claim kind and takes
the fields above; a kind of the first sort admits no field that states
something about the world, and a container of nested claim records, such as
`alignments` below, is no such field, because each nested record carries the
pattern. There is no third sort, so a later kind cannot bypass the pattern.

A claim is never rewritten under its ID. Revising any field, the status
included, appends a new claim of the same kind by the same agent about the
same subject whose `supersedes` names the earlier record. Supersession is
acyclic, a superseded claim stays in the package with its exact record, and a
claim is current when no claim supersedes it. Currency follows this structure
alone, because clocks and transcription make instants unreliable as an order.
Withdrawal is a superseding claim with status `withdrawn` and therefore
requires a nonempty `supersedes`. Removing a claim from a later package is a
rewrite, as the profile's `E_CLAIM_REWRITE` already rules for derivation
claims.

Disagreement between agents needs no branch of the package. Two claims about
one subject by different agents coexist as two records, neither supersedes
the other, because supersession is confined to one agent, and the validator
decides nothing between them. Two differently attributed continuity claims
coexist the same way under section 1, and the case
`contradictory_interpretations` keeps two agents' conflicting annotation
bodies over the same extent valid. A view for a task filters by agent, status
and currency over the package, which holds every claim.

Certainty is a field of the claim. It is the claiming agent's own
qualification, made in the same act and at the same instant as the claim; a
separate record would split one act into two records that must agree on agent
and instant and would double the record count in the common case. What a
field cannot carry is a second agent's assessment of the claim and a
certainty history separate from the claim history. Both remain expressible,
since a claim is an identified record and any relation or later assessment
kind can take it as its subject. The ordinal set stands in for a probability
because the [bindings](text-model-bindings.md) exclude floating-point values.

| Record kind | Subject fields | Present pattern fields | Added by the pattern |
|---|---|---|---|
| `continuities` | `text` | `id`, `agent`; `versions` and `criterion` are content | `created`, `status`, `certainty`, `valid`, `supersedes` |
| `readings` | `version` | `id`, `agent`; `label` and the node forest are content | the same five |
| `annotations` | `selection` | `id`, `agent`; `body` is content | the same five |
| `relations` | `source` | `id`, `agent`; `type` and `target` are content | the same five |
| `ep-derived-from` relations under the profile | `source` | `id`, `agent`, supersession through `ep-supersedes` under the same-agent, same-subject and acyclicity rules | `created`, `status`, `certainty`, `valid` |

The profile realizes supersession as a reserved relation because the v0.1
record shape admits no new field; the pattern fixes the field form for
extensions and leaves the profile's form in place. Whether the four v0.1
claim kinds receive the added fields is an additive change in the
[change classes](p6-architecture.md#change-classes) of the architecture,
decided with the first extension. Until then a v0.1 claim reads as
`asserted`, undated and unqualified.

Posit: one claim pattern with identity, agent, instant, status, optional
certainty, optional validity and supersession makes every domain assertion
revisable and every disagreement representable without a branch, and
certainty belongs to the claim itself. Open evidence question: which real
editorial workflows need a second agent's certainty about another agent's
claim, or a certainty history separate from the claim history, so that
certainty would have to become a claim about the claim?

### Local identity and global identifiers

Section 1 resolves every reference within one package and keeps IDs
package-local. For exchange, a package declares exactly one base IRI in the
package field `base`, next to `model_version`, and every record IRI is the
base followed by the record's local ID. The local ID stays the canonical
identifier; the base is a publication fact about the package. The field
enters the package contract with the first extension that is exchanged,
together with `former_bases` below, and the reference bindings carry both
under their existing preservation laws.

```text
base    IRI under RFC 3987 with a scheme, without query component,
        ending in "/" or "#", with "#" nowhere else
id      [A-Za-z][A-Za-z0-9._:-]*          the section 1 grammar, unchanged
IRI(r)  base ++ id(r)
```

The ID alphabet consists of unreserved characters and the colon, which RFC
3986 admits in a path segment and in a fragment without percent-encoding, so
no escaping exists in either direction. An ID contains neither `/`, `#`, `?`
nor `%` and starts with a letter, so a record IRI splits uniquely at its last
`/` or `#` into base and local ID and no local ID is a dot segment. Bases and
IRIs compare code point by code point, without case folding, percent-decoding
or Unicode normalization, in line with R11. A concrete RDF syntax may
abbreviate a record IRI to a prefixed name only where the local ID is a legal
local name there; an ID ending in `.` is none in Turtle and SPARQL, and the
binding then writes the IRI in full. Abbreviation is lexical and changes no
IRI.

Two copies of a package are the same package if and only if their canonical
serializations agree, which is R11 equivalence, witnessed by the SHA-256 of
`canonical_bytes`. `base` and every field this section adds enter the
canonical serialization; `supersedes` compares as a set, nested alignment
claims sort by ID like reading nodes, and every other new field compares as
an exact string. The package hash is a derived value; a package cannot
contain its own hash, so none is stored. Three identities stay apart. A
version's `sha256` identifies its content `c(v)`, and equal content under two
version IDs yields two records with two IRIs and one hash, as R01 requires. A
record IRI identifies the record. The package hash identifies the package.

Republishing a package under a new base creates a new package, because the
base is part of the canonical serialization, while every record keeps its
local ID. The former IRIs are aliases, recorded as claims in the package
field `former_bases`, an array of claim records whose subject is the package
and whose one content field `base` holds the former base, so that the alias
of any record `r` under a former base `b` is `b ++ id(r)` by the grammar
alone. Nothing in the record set is
rewritten, the earlier package remains what it was, and a record absent from
the republished package has no alias in it. A local ID is never renamed on
republication. A renamed record is a new record under R01, and a
correspondence between the old and the new record is an alignment claim with
relation `exact`, as defined below. References across packages remain
outside this version; alignment claims are the only link a package makes
beyond itself.

Posit: base plus canonical local ID gives every record a global identifier
without escaping or renaming, package identity is R11 equivalence witnessed
by the hash of the canonical serialization, and a republication is a new
package with recorded aliases rather than an edit of identifiers. Open
evidence question: which exchange practices, such as merging packages,
splitting a package or moving records between projects, require identifier
operations that this policy leaves unrepresentable?

### External alignment

Section 1 excludes an ontology alignment language, and that exclusion
stands. The minimal field that lets an RDF export interoperate is a list of
alignment claims. A concept record, an agent record and, once defined, an
entity record may carry an optional field `alignments`, an array of claim
records with the pattern fields and two content fields. `iri` is an absolute
IRI compared code point by code point. `relation` is exactly one of `exact`,
`close`, `broader`, `narrower`, read from the record to the external
resource. `exact` claims that both stand for the same thing for every purpose
of the package, `close` that they are interchangeable for some purposes
without stating which, `broader` that the external resource stands for
something more general than the record, `narrower` for something more
specific. The four kinds mirror the SKOS mapping properties and carry none of
their semantics here; a part-whole or membership relation between the things
themselves is a domain relation. Alignment claims nest in their carrier as
reading nodes nest in readings, with package-wide unique IDs, and their
subject is the carrier.

No inference is defined. The validator checks the field forms and the claim
rules and nothing about the external resource, neither its existence nor its
meaning. It derives no symmetric, transitive or inherited alignment and does
not propagate a concept's alignment to the nodes that carry the concept. Two
alignments of one record to one IRI with different relation kinds, or by
different agents, coexist as two claims. Consumers may use the alignments and
answer for the inference they add. Extending the carrier set to a text or a
version requires a recorded decision.

The table states the direction of the mapping, from package record kinds to
candidate target vocabularies, as a binding to be specified under section 12
with its own loss matrix. Nothing in it is implemented.

| Record kind | Candidate target | Without natural target |
|---|---|---|
| `agents` | PROV `prov:Agent`, CIDOC CRM `E39 Actor`; `label` as `rdfs:label`; the attribution of every claim as `prov:wasAttributedTo` | the identity of an outside person, which the record never asserts |
| `concepts` with `alignments` | SKOS `skos:Concept` with `skos:prefLabel` and `skos:definition`; the four relation kinds as `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch` | the role `node` or `relation`; agent, instant and status of an alignment, which a plain mapping triple drops |
| `versions` | none as a class; the record IRI serves as `oa:hasSource` | content, hash and technical parents |
| `selections` | Web Annotation `oa:SpecificResource` with `oa:TextPositionSelector` for `point` and `ranges`, `oa:TextQuoteSelector` with `oa:exact`, `oa:prefix`, `oa:suffix` for `quote` | the `match` policy; one aggregate of several segments against separate targets, for which `oa:List` and `oa:Independents` are candidates; unresolved candidates |
| `readings[].nodes[]` as mentions, `annotations`, denotation claims | Web Annotation `oa:Annotation`, motivated as classifying with the concept as body, with an `oa:TextualBody`, or as identifying with the entity IRI as body; `dcterms:creator` for `agent`, `dcterms:created` for `created` | the reading forest with its containment and sibling rules; certainty and status |
| `relations` and the pattern fields of every claim | CIDOC CRM `E13 Attribute Assignment` with `P140`, `P141`, `P177`, `P14`, `P4`; PROV `prov:wasAttributedTo`, `prov:generatedAtTime`, `prov:wasRevisionOf` for `supersedes` | a plain triple, which loses identity, agent and instant, so the binding must choose a claim node, RDF-star or named graphs; `status`, `certainty` and `valid`, for which CRMinf belief values are one candidate |
| `texts`, `continuities` | none | a grouping identity and an attributed membership under a criterion |
| entity, name, event (planned) | CIDOC CRM `E21 Person`, `E53 Place`, `E74 Group`; `E41 Appellation` through `P1`; `E5 Event` or PROV `prov:Activity` | the claim wrapper of each; the validity scope of a name; the `exact` alignment of an entity, for which `skos:exactMatch` states nothing about identity and `owl:sameAs` entails it |
| `former_bases` | PROV `prov:alternateOf` or OWL `owl:sameAs`, per record by the grammar | the choice between the two, whose entailments differ; the binding must state it |

Version content and hash, text and continuity claim, the reading forest,
unresolved candidates, the `match` policy and the fields `status`,
`certainty` and `valid` have no natural target yet.

Posit: a closed list of alignment claims with four relation kinds and no
inference is the smallest addition that lets an RDF export interoperate with
external vocabularies while the model stays free of an ontology language.
Open evidence question: which external vocabularies and which inference
expectations do consuming projects bring, and do four relation kinds cover
the alignments editors make?

### Record kinds of the entity extension

The pattern implies the record kinds of the entity extension that follows.
Their constraints are not defined here.

- Entity, an identity record for a thing the edition speaks about, with an ID
  and a display label and nothing about the world, motivated by the
  [P6 Design](../40_output/12-p6-design.md#2-text-projections-and-occurrence-identity)
  chapter's open question which additional objects real workflows require;
  section 11 already separates a record describing a person from that person.
- Name, a claim that an entity bears a name form, with the form, an optional
  language and an optional validity scope as content.
- Mention, a reading node whose concept marks it as a mention, or an
  annotation over a selection; the pattern adds no third kind, because both
  existing kinds already carry an occurrence in a text.
- Denotation claim, a claim that a mention denotes an entity, the record in
  which a retained responsibility marker such as the one discussed in the
  chapter's [third section](../40_output/12-p6-design.md#3-structure-as-an-attributed-reading)
  receives an attributed, revisable resolution.
- Alignment claim, as defined above, carried by concept, agent and entity
  records.

Withdrawal and cross-agent disagreement, two parts of the open question in
the chapter's
[fifth section](../40_output/12-p6-design.md#5-version-identity-and-revision-of-claims),
receive their representation from the pattern, withdrawal through a
superseding claim with status `withdrawn` and disagreement through coexisting
claims. A negative claim, that a mention does not denote an entity, is no
status of a positive claim; it would need a content field or a kind of its
own and stays open.

Posit: entity, name, mention, denotation claim and alignment claim are the
record kinds the pattern yields for the entity extension, and none of them
needs a construct outside the pattern. Open evidence question: which
independently selected editions with a named-entity practice show that these
kinds, once constrained, preserve the distinctions their editors make, and
which kinds are missing?

### Conformance note

The pattern reuses the checks of section 5, the ID grammar with `E_ID`,
package-wide uniqueness with `E_DUPLICATE_ID` for nested claims as for
reading nodes, closed references by category with `E_REFERENCE`, the concept
roles with `E_TYPE`, nonmutation under R10, canonical comparison under R11,
and acyclicity where a parent-like relation is declared, here for
`supersedes` as for version parents and reading parents. The append-only
claim check generalizes the profile's `E_CLAIM_REWRITE` from derivation
claims to every claim kind. New are the lexical checks of `created`, `valid`,
`base` and `iri`, the closed sets of `status`, `certainty` and `relation`,
the order of validity bounds, the same-agent and same-subject rule of
supersession, and `withdrawn` only with a nonempty `supersedes`.

Finite synthetic checks demonstrate these rules on supplied instances. They
cannot establish that the pattern is adequate for real editorial
disagreement, in which two editors dispute a denotation over years or a claim
is withdrawn on new evidence. The boundary that section 9 draws for the model
as a whole applies to this section without exception.

Posit: reusing the v0.1 checks and generalizing the profile's append-only
rule keeps the pattern executable within the existing validator. Open
evidence question: which recorded disagreements from real editions, replayed
as packages, falsify the claim that no branch of a package is ever needed?
