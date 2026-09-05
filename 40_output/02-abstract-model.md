---
type: chapter
status: grounded
checked:
  validation: 2026-09-05
assertions:
  - "[[30_assertions/p5-anchor-identifies-a-textual-point]]"
  - "[[30_assertions/p5-span-associates-interpretation-with-text]]"
  - "[[30_assertions/p5-span-from-identifies-start-or-whole-node]]"
  - "[[30_assertions/p5-annotation-refers-to-web-annotation-model]]"
posits: 4
created: 2026-09-05
updated: 2026-09-05
---

# Text identity and annotation: a bounded P5-to-model pilot

## What the selected P5 sources establish

TEI P5 4.12.0 defines `anchor` as identifying a point within a text, whether or
not that point corresponds to a textual element.[^anchor] It defines `span`
as associating an interpretative annotation directly with a span of text.[^span]
For `span/@from`, the description identifies the starting node, or the node
of the entire annotated span when `@to` is absent.[^from] The specification
also describes `annotation` as following the Web Annotation Data Model.[^annotation]

## Independent modeling proposal

The source distinctions between a target, its addressing, and an associated
interpretation motivate a question about what happens when text changes; they
do not entail the following answer. The pilot proposes an editor-assigned
grouping of text versions, an immutable string version, an identified region
record containing a version reference and selector, and an annotation referring
to that record. A region record, its selector, and the resolved interval should
remain distinct. Equality of strings should not establish version identity,
and a target alone should not determine its interpretation. This bounded model
excludes empty regions and therefore does not yet model textual points.[^identity]

The proposed comparison holds that object model fixed and varies the selector:
version-bound positions with an exact-quote check, or version-bound quotations
with optional literal context. It should clarify the difference between
resolving a target and carrying an interpretation. It cannot decide between
competing text ontologies, establish a replacement for P5, or demonstrate
equivalence with its node-based addressing.[^alternatives]

Reanchoring after an edit should produce an explicit proposal for review,
preserving the old target. A unique matching quotation is insufficient to
establish that an interpretation remains appropriate, even if its position is
unchanged. Ambiguity and failure to match the retained selector should remain
visible; a failed context-qualified selector need not mean that its quotation
has disappeared.[^reanchor]

The experiment should be accepted as a research step only if its definitions,
source-support chain, failure cases, and reproducible checks are intelligible
to a human reviewer. Success on synthetic strings should motivate testing on
real editorial workflows rather than a claim of universal textual expressivity
or demonstrated P5 migratability.[^acceptance]

[^anchor]: Grounded in [[30_assertions/p5-anchor-identifies-a-textual-point]].
[^span]: Grounded in [[30_assertions/p5-span-associates-interpretation-with-text]].
[^from]: Grounded in [[30_assertions/p5-span-from-identifies-start-or-whole-node]].
[^annotation]: Grounded in [[30_assertions/p5-annotation-refers-to-web-annotation-model]].
[^identity]: Posit: separating identity, string state, selection, and interpretation makes the pilot's commitments explicit. Open evidence question: which real editorial cases require a different account of textual continuity?
[^alternatives]: Posit: a controlled selector comparison can expose trade-offs within an assumed object model. Open evidence question: how do different object models, node-based P5 addressing, and real customizations compare under these tasks?
[^reanchor]: Posit: a conservative proposal boundary preserves auditability without treating character matching as semantic judgment. Open evidence question: which editing workflows permit safe automatic acceptance, and under what domain-specific policy?
[^acceptance]: Posit: finite formal checks and human review answer different questions and should be accepted separately. Open evidence question: which real-world cases, selected under an explicit sampling scope, would invalidate this pilot's definitions?
