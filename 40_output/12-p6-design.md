---
type: chapter
status: grounded
checked:
  validation: 2026-09-05
assertions:
  - "[[30_assertions/p5-anchor-identifies-a-textual-point]]"
  - "[[30_assertions/p5-span-associates-interpretation-with-text]]"
  - "[[30_assertions/w3c-quote-selection-can-match-multiple-sequences]]"
  - "[[30_assertions/tei-fr363-proposes-target-on-span]]"
  - "[[30_assertions/piez-treats-optional-hierarchy-as-object-of-study]]"
  - "[[30_assertions/renear-wickett-distinguish-string-mapping-from-persistent-identity]]"
  - "[[30_assertions/humboldt-diary-encodes-a-dated-nested-heading]]"
  - "[[30_assertions/humboldt-diary-separates-an-unknown-hand-note-and-editorial-explanation]]"
  - "[[30_assertions/humboldt-diary-encodes-a-page-pointer-and-separate-foliation]]"
posits: 13
created: 2026-09-05
updated: 2026-09-05
---

# Abstract Text Model 0.1: technical proposal for TEI P6

This proposal defines an experimental model of textual identity, selection,
structure, and interpretation for evaluation as a possible TEI P6 foundation.
Its objects and rules are independent project decisions. Formal conformance,
preservation of editorial distinctions, and practical usability require
separate evaluation.[^scope]

## 1. Scope and coverage method

The investigation covers every module in the pinned P5 4.12.0 baseline,
discussion records, literature, and documented practice. Modules organize
source retrieval. The conceptual analysis distinguishes document types such
as letters and charters, media forms such as manuscripts and recorded speech,
and phenomena such as correction and uncertainty. One case can combine these
dimensions without treating them as the same kind of model object.[^coverage]

For each module, the procedure inventories elements, attributes, classes,
macros, datatypes, constraints, and references at an exact baseline version.
It then examines effective customization rules, Guidelines prose, examples,
and observed use. Each proposed requirement records its source support or
project rationale, preservation criteria, and counterexamples. Issues and
literature can challenge these requirements. Reported difficulties must still
be checked against the relevant P5 version.[^coverage]

Coverage is reported separately for declaration inventory, source
interpretation, formal requirements, and executed cases. An inventory entry
does not establish model support. Each requirement names its disposition in
the core, a domain profile, a connected model, or open work, with links to
the checks supporting that decision. An executed case establishes coverage
only for its declared task and distinctions.[^coverage]

## 2. Text projections and occurrence identity

A heading in Humboldt's England diary H0017682 contains a note marked
`hand="#unknown"`, the reference text “6255”, and a nested editorial note with
`resp="#CT #DE"`.[^notesource]

Consider the task of reading the heading as “Reise. 1790. England.” while
inspecting the handwritten number and the editorial explanation separately.
The proposed representation retains all three with their relationships and
attribution. Excluding the notes from this reading sequence is an editorial
projection. Another task could select a different sequence. The mapping
contract must therefore declare its reading policy and retain the source.[^projection]

In another heading of the diary, “Bäder in Derbyshire” appears inside a date
element with `when="1790-06-15"`, with nested highlighting around the place name.[^headsource]

The heading, date, and outer highlighting remain distinct occurrences
even when they cover the same characters. Preserving only their extents would
lose their roles and nesting. A version supplies the character sequence.
Identified nodes describe a structural reading, selections connect nodes to
positions, and annotations retain further interpretation. The
[equal-extents example](#example=equal-extents) and
[editorial-notes example](#example=editorial-notes) expose these mapping choices
for review.[^objects]

## 3. Structure as an attributed reading

Piez argues that permitting any hierarchy or none makes hierarchy itself open
to study.[^hierarchysource]

The candidate treats structure as an attributed reading of a version.
Different readings may cross or disagree while preserving their own nodes,
agents, and parent relationships. Each version 0.1 reading is a forest of
contiguous extents. Children are contained in
parents, and siblings do not overlap. Equal parent and child extents are
allowed. Discontinuous regions remain selectable for annotations, but they are
not structural nodes under this first contract. The
[overlap example](#example=overlap) compares two crossing ranges in separate
readings of one constructed sentence. Cases needing another account of
structure challenge this boundary instead of being flattened to fit it.[^readings]

Within this contract, every reading refers to exactly one version and one
responsible agent. Every node belongs to one reading, refers to one node
concept and one selection, and has at most one parent within that reading.
The parent relation is acyclic. A node's identity remains distinct from its
concept and selected extent. Two nodes are not merged because their extents
coincide. These constraints define a structural representation, not the truth
of the interpretation assigned to it.[^readings]

For the diary task, separating a main reading from note bodies does not make
the notes semantically self-explanatory. Preserving their source attributes,
nested relationships, and responsibility markers requires an explicit mapping
contract beyond the core's generic annotation body. That contract must
declare how to decode these records and validate their connections. Retaining
`#CT #DE` as a value does not resolve or authenticate
the people it refers to.[^binding]

## 4. Selection and unresolved targets

TEI P5 4.12.0 defines `anchor` as attaching an identifier to a point within a
text.[^point] It defines `span` as associating an interpretative annotation
directly with a span of text.[^span] The W3C 2017 Web Annotation Data Model
recommends treating multiple Text Quote Selector matches as matching all the
discovered sequences.[^pluralsource]

The candidate distinguishes a point, one region with several ordered
components, and several independently selected regions. It also
distinguishes selecting every occurrence of a quotation from uncertainty about
which single occurrence was intended. An editor searching for one occurrence
of a repeated heading receives unresolved candidates until the intended
location is decided. An annotation remains inspectable in that state.
The [discontinuous-region example](#example=discontinuous) and
[ambiguous-target example](#example=ambiguous-target) separate these cases.
These policies are explicit task choices, not conclusions logically forced
by the source definitions.[^selection]

For a version v with character sequence c(v), positions count Unicode code
points from zero to the sequence length. A range `[a,b)` includes its start
and excludes its end, with `0 <= a < b <= len(c(v))`. Its recorded quotation
must equal the selected substring. Range components in one aggregate are
ordered and disjoint. A point may address either endpoint, while an absent
or ambiguous quotation may remain unresolved in a well-formed annotation.
Such an unresolved selection cannot supply a structural node's extent under
the version 0.1 reading rules.[^selection]

## 5. Version identity and revision of claims

Renear and Wickett describe editing strings as mapping between strings rather
than modifying a persistent underlying entity.[^stringsource]

The model separates exact character content, identified version records,
technical construction inputs, historical hypotheses, and editorial continuity.
In version 0.1, `versions.parents` means declared frozen technical inputs
used to construct a version record. An empty list means that none were
recorded. It does not establish an original or independent historical
witness. Correcting those frozen technical declarations requires a new
version-record ID. Equal strings are allowed in distinct version records.[^identity]

Consider a synthetic research revision, separate from any historical claim
about the diary. An editor first hypothesizes that version B derives from A,
then concludes that it derives from C. The optional editorial provenance
profile represents both attributed hypotheses and appends an explicit
supersession relation from the new claim to the old one. B's version record,
content, selections, and annotations remain unchanged. Another editor's
unsuperseded hypothesis remains visible. A separate append-only revision
check preserves claim history. The core's version check alone does not
enforce that history.[^history]

Editorial continuity remains a separate, attributed positive grouping
under a stated criterion. Omitted membership does not imply exclusion.
Reanchoring an annotation to a new version requires such a continuity
claim and returns an unaccepted proposal. Neither a unique literal match, a
hash, nor a historical derivation hypothesis approves that annotation's
meaning after an edit. The
[identity and reanchoring example](#example=identity-reanchoring) makes this
distinction available for inspection.[^identity]

## 6. Formal model, bindings, and equivalence

The [model definition](../docs/p6/abstract-text-model-v0.1.md) serves as
the explicit contract for identified objects, local references, selectors,
attributed readings, and diagnostics. Its strict comparison rule must
preserve identity, attribution, exact content, target policy, and segmentation
while ignoring registry order. The abstract definition identifies objects and
their admissible relations. A serialization binding assigns those objects a
concrete syntax and defines encoding and decoding. Changing the displayed
syntax must not silently change the selected model instance.[^formal]

For a binding with encoder E and decoder D, the preservation obligation is
`equivalent(M, D(E(M)))` for each supported valid model M. This contract must
name its supported domain, rejected inputs, normalization rules, and comparison
relation before the roundtrip is executed. Equality of generated files is a
different test. JSON, XML, YAML, or a future RDF binding cannot be credited
with equivalent semantics merely because each file parses. The
[binding contract](../docs/p6/serialization-bindings-v0.1.md) supplies the
versioned syntax rules and supported domain.[^formal]

P5-to-model migration requires the observations of the P5 input and the decoded
candidate to agree for the
declared editorial task. A model roundtrip alone says nothing about whether
that first migration preserved the source distinctions. Attribute values
retained as uninterpreted strings, external references left unresolved, and
policy-dependent reading projections remain explicit dependencies.[^formal]

## 7. Examples as comparative specifications

Each phenomenon is specified by a task, the distinctions it must preserve,
one or more justified P5 encodings, a candidate model instance, and the
candidate's supported serializations. P5 variants are alternatives to compare,
not successive steps toward a presumed P6 solution. The associated formal
description supplies object identities, relation domains and ranges,
cardinalities, ordering rules, invariants, and diagnostic expectations. A type
diagram explains those constraints. An instance diagram identifies the
objects in the actual example. For range phenomena, a separate position view
shows extents that an entity-relationship diagram cannot express clearly.[^comparison]

The [overlap comparison](#example=overlap), for example, must examine an
anchor-and-span mapping against the candidate's attributed readings without
crediting the candidate with a capability merely because its notation differs.
The P5 definitions above establish points and interpretative spans. Specific
variant semantics, customization validity, and the required task observations
still need explicit checks. Each comparison therefore reports preservation,
loss, assumptions, and untested properties for each alternative, rather than
selecting a winner from markup length or a diagram.[^comparison]

## 8. Validation and failure boundaries

A paragraph in the diary continues across a page break with `facs="#f0018"`
and `n="[9v]"`, followed by a foliation element
containing “16.”.[^pagesource]

A candidate unable to preserve the required page and foliation distinction
must refuse that migration explicitly. A technically successful refusal
does not count as a successfully migrated case. The
[page and foliation example](#example=page-foliation) and
[editorial case study](../docs/p6/editorial-case-study.md) make this
distinction inspectable alongside development examples, source locators,
projection choices, and comparison limits. Neither an image pointer alone
nor a text-only model establishes demonstrated image alignment.[^evaluation]

Formal validation should test record shape, reference integrity, bounds,
declared graph constraints, version rewrites, and the profile's claim-history
rules. Independently authored cases and reproducible reports should expose
disagreement between intended and implemented behavior. Human acceptance
should separately ask whether editors can explain the distinctions, preserve
their intended readings, and revise an example without losing meaning. Finite
passing tests should not establish universal expressivity, interpretation
truth, or community agreement.[^evaluation]

## 9. Architecture comparison and open decisions

The author of TEI SourceForge feature request 363 proposes adding an @target
attribute to the span element.[^request]

Historical proposals guide investigation of the current baseline. They do
not establish a present P5 defect. The project should compare P5
repair, compatible evolution, architectural replacement, and deferral against
the same editorial tasks. A primary tree with separately attributed stand-off
observations deserves the same preservation tests as the sequence-and-readings
candidate. If both preserve the required distinctions, the decision should
turn on additional evidence about authoring, querying, maintenance, migration,
and teaching costs rather than a preferred diagram.[^recommendation]

The next recommendation should depend on independently selected editions and
text forms, effective customization constraints, explicit loss reports, and
observed editorial work. The profile needs challenges involving withdrawal,
negative claims, and disagreements across agents. The model needs challenges
involving carriers, images, spoken time, and noncontiguous structures. Evidence
that an existing workflow preserves the required distinctions at lower total
cost, or that the candidate erases a necessary distinction, should reverse a
preference for replacement. Advance this model as a research instrument while
withholding an official adoption recommendation.[^recommendation]

[^point]: Grounded in [[30_assertions/p5-anchor-identifies-a-textual-point]].
[^span]: Grounded in [[30_assertions/p5-span-associates-interpretation-with-text]].
[^pluralsource]: Grounded in [[30_assertions/w3c-quote-selection-can-match-multiple-sequences]].
[^hierarchysource]: Grounded in [[30_assertions/piez-treats-optional-hierarchy-as-object-of-study]].
[^stringsource]: Grounded in [[30_assertions/renear-wickett-distinguish-string-mapping-from-persistent-identity]].
[^request]: Grounded in [[30_assertions/tei-fr363-proposes-target-on-span]].
[^notesource]: Grounded in [[30_assertions/humboldt-diary-separates-an-unknown-hand-note-and-editorial-explanation]].
[^headsource]: Grounded in [[30_assertions/humboldt-diary-encodes-a-dated-nested-heading]].
[^pagesource]: Grounded in [[30_assertions/humboldt-diary-encodes-a-page-pointer-and-separate-foliation]].
[^scope]: Posit: a bounded executable definition makes assumptions reviewable while keeping broad coverage a research obligation. Open evidence question: which independently selected textual traditions and working practices must the next version cover?
[^coverage]: Posit: derive requirements across pinned P5 modules through source interpretation, domain tasks, and counterexamples. Report inventory, formalization, and execution separately. Open evidence question: which effective constraints and textual practices are missing, and which require a core primitive, a profile, or a connected model?
[^projection]: Posit: an explicit reading projection makes selection of the main text inspectable while retaining other textual material. Open evidence question: do editors accept this main-text and note distinction for the intended task, and which alternative projections do they need?
[^objects]: Posit: separate occurrence identity, extent, type, and interpretation preserve distinctions that equal positions alone cannot express. Open evidence question: which actual workflows require each distinction and which additional objects are necessary?
[^readings]: Posit: attributed forests provide a testable first account of competing structures without establishing sufficient generality. Open evidence question: which cases require noncontiguous nodes, shared occurrences, or another containment model?
[^binding]: Posit: declaring the annotation binding makes processing dependencies visible rather than crediting generic bodies with unimplemented semantics. Open evidence question: which source distinctions need core primitives and which remain usable through domain bindings?
[^selection]: Posit: aggregate regions, intentional plurality, and unresolved single-target intent require distinct representations for the proposed tasks. Open evidence question: which real annotation practices require these distinctions, and how should their interfaces present them?
[^identity]: Posit: frozen technical records, attributed continuity, and unaccepted retargeting separate reproducible data from editorial judgment. Open evidence question: do real correction and editing tasks accept these boundaries, including a new ID for corrected technical parent metadata?
[^history]: Posit: an optional attributed claim graph permits historical reinterpretation without rewriting version identity. Open evidence question: how should withdrawal, negative claims, cross-agent disagreement, and external support be represented without concealing earlier claims?
[^formal]: Posit: separate abstract objects, concrete bindings, model equivalence, and P5 task preservation so that a serialization roundtrip cannot define migration correctness. Open evidence question: which distinctions must real interchange preserve, and which normalizations or identity mappings should its contract permit?
[^comparison]: Posit: a shared phenomenon specification with P5 alternatives, candidate bindings, formal constraints, and separate type and instance diagrams makes technical comparison inspectable without presuming replacement. Open evidence question: which independently checked variants cover the actual editorial task, and which parts of the comparison help editors or implementers detect lost meaning?
[^evaluation]: Posit: independent expectations, explicit failure, and reproducible observations strengthen technical review without establishing conceptual truth. Open evidence question: which expert-reviewed cases and observed workflows would falsify or support practical adequacy?
[^recommendation]: Posit: advance the bounded experiment while withholding an architecture or adoption verdict until alternatives, preservation, and costs are evaluated. Open evidence question: what current-baseline, migration, tooling, pedagogy, and governance evidence would justify retaining, extending, or replacing a candidate?
