# Abstract Text Model 0.1

This independent experimental definition explores a possible TEI P6. Its
definitions are project posits, not an adopted standard or a complete ontology
of everything expressible in text.

This version models finite character sequences, attributed editorial groupings,
selections, structural readings, annotations, and typed relations through a
reference implementation and independently authored examples. The wider
programme draws requirements from P5, discussion records, literature, and
editorial practice. This version sets an experimental scope for that work.

## 1. What the objects mean

An instance is a finite package of records with distinct, package-local IDs.
The objects and relations are defined independently of their serialization.
The [reference bindings](serialization-bindings-v0.1.md) encode the same package
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
outside v0.1. The broader sketch in `core-model.md` is not an implementation
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

The [editorial provenance profile](../../experiments/editorial_cases/profile.json)
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
surviving branch. This example is not a historical finding about the Humboldt
diary used in the separate [editorial case study](editorial-case-study.md).

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
[`spec.json`](../../experiments/abstract_text_v01/spec.json). The package has
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
[bindings](serialization-bindings-v0.1.md) implement a separate preservation
contract for model packages. Their round trips do not establish preservation
during P5 conversion. RDF remains outside the binding contract.

## 6. Requirement and test ledger

Every rule is a project contract. Source findings motivate tests without
logically entailing the chosen primitives. The source-supported argument and
its explicit posits are in [P6 Design](../../40_output/12-p6-design.md).

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
[editorial case study](editorial-case-study.md).

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
Current results and dates belong in `knowledge/state.md`.

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
