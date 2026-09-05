---
type: chapter
status: grounded
checked:
  validation: 2026-09-05
assertions:
  - "[[30_assertions/p5-span-associates-interpretation-with-text]]"
  - "[[30_assertions/w3c-quote-selection-can-match-multiple-sequences]]"
  - "[[30_assertions/tei-fr363-proposes-target-on-span]]"
  - "[[30_assertions/piez-treats-optional-hierarchy-as-object-of-study]]"
  - "[[30_assertions/renear-wickett-distinguish-string-mapping-from-persistent-identity]]"
posits: 4
created: 2026-09-05
updated: 2026-09-05
---

# Selection, hierarchy, and identity: requirements to test

## From target selection to interpretation

TEI P5 4.12.0 defines `span` as associating an interpretative annotation directly
with a span of text.[^p5] The W3C 2017 Web Annotation Data Model recommends
treating multiple Text Quote Selector matches as matching all the discovered
sequences.[^matches]

A candidate text model should distinguish an intended plural target from
uncertainty about which single target was intended. The pilot's unique-only
quotation rule should therefore be evaluated as a task policy, with two
different examples: deliberately annotating every occurrence and identifying
one particular occurrence. Neither example determines whether an interpretation
remains appropriate after an edit. This requirement should be tested before
making uniqueness an invariant of the shared model.[^plural]

## Historical proposals and present requirements

The author of TEI SourceForge feature request 363 proposes adding an @target
attribute to the span element.[^request]

Historical proposals should initiate a comparison with the pinned current
baseline, existing alternatives, and primary decision, implementation, and
release records. The request alone should not be used to establish either a
current deficiency or the success of its proposed repair. The next requirement
comparison should include continuous and discontinuous targeting and the costs
of expressing both within P5.[^history]

## Structure as an attributed reading

Piez argues that permitting any hierarchy or none makes hierarchy itself open
to study.[^hierarchy]

A model comparison should include two differently attributed structural
readings of the same fixed character sequence. It should ask whether both
readings can be represented, independently revised, and queried without
silently treating one as the text itself. This is a proposed test of hierarchy
and attribution, not an inference that all texts require a range-based or graph
architecture.[^structure]

## String transformation and editorial continuity

Renear and Wickett describe editing strings as mapping between strings rather
than modifying a persistent underlying entity.[^strings]

The model should treat string equality, version identity, and an editor's
judgment of textual continuity as separate questions. A next experiment should
compare two explicit continuity policies over the same versions, including
equal strings assigned different identities and different strings assigned to
one editorial grouping. The comparison should state what would make a policy
inappropriate for the task. Passing hash or reference checks cannot settle that
editorial judgment.[^identity]

[^p5]: Grounded in [[30_assertions/p5-span-associates-interpretation-with-text]].
[^matches]: Grounded in [[30_assertions/w3c-quote-selection-can-match-multiple-sequences]].
[^request]: Grounded in [[30_assertions/tei-fr363-proposes-target-on-span]].
[^hierarchy]: Grounded in [[30_assertions/piez-treats-optional-hierarchy-as-object-of-study]].
[^strings]: Grounded in [[30_assertions/renear-wickett-distinguish-string-mapping-from-persistent-identity]].
[^plural]: Posit: task-dependent plural selection and unresolved single-target intent should be tested separately. Open evidence question: which real annotation workflows require each behavior, and how do editors distinguish them?
[^history]: Posit: historical complaints require present-baseline and outcome checks before motivating architectural replacement. Open evidence question: which governance, implementation, release, and user evidence establishes the costs and benefits of this extension?
[^structure]: Posit: competing attributed hierarchies test conceptual commitments that a single preferred hierarchy can hide. Open evidence question: which independently reviewed editorial cases require preserving such readings, and at what processing cost?
[^identity]: Posit: continuity policies should be evaluated independently of string integrity. Open evidence question: which textual traditions and editing tasks accept or reject each identity policy?
