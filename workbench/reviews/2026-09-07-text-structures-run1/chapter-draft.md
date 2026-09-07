---
status: draft
checked: {}
assertions:
  - "[[30_assertions/structure-p5-has-several-nonhierarchical-methods]]"
  - "[[30_assertions/structure-p5-join-combines-virtual-elements]]"
  - "[[30_assertions/structure-p5-boundary-range-validation]]"
  - "[[30_assertions/structure-p5-part-reconstitution-ambiguity]]"
  - "[[30_assertions/structure-p5-part-positions-fragments]]"
  - "[[30_assertions/structure-p5-part-locates-omissions-in-ds]]"
  - "[[30_assertions/structure-p5-floatingtext-interrupts-resumable-text]]"
  - "[[30_assertions/structure-p5-floatingtext-does-not-imply-external-origin]]"
  - "[[30_assertions/structure-p5-div-in-line-needs-floatingtext]]"
  - "[[30_assertions/structure-p5-div-in-paragraph-needs-floatingtext]]"
  - "[[30_assertions/structure-p5-pb-associates-page-image]]"
  - "[[30_assertions/structure-p5-pb-number-and-sequence]]"
  - "[[30_assertions/structure-p5-test-page-marker-inside-paragraph]]"
  - "[[30_assertions/structure-p5-next-same-type-recommendation]]"
  - "[[30_assertions/structure-p5-prev-same-type-recommendation]]"
  - "[[30_assertions/structure-p5-multiple-encoding-maintenance-cost]]"
  - "[[30_assertions/structure-p5-composite-stories-have-flexible-order]]"
  - "[[30_assertions/structure-p5-division-type-is-independent-of-depth]]"
  - "[[30_assertions/structure-p5-note-responsibility-code-needs-definition]]"
  - "[[30_assertions/structure-p5-note-number-omission-is-conditional]]"
  - "[[30_assertions/structure-p6-numbered-divisions-reconsideration-label]]"
  - "[[30_assertions/structure-issue1505-recommendation-self-report]]"
  - "[[30_assertions/structure-p5-stand-off-discontinuous-annotation]]"
  - "[[30_assertions/structure-p5-divgen-processing-is-application-defined]]"
posits: 7
created: 2026-09-07
updated: 2026-09-07
---

# Text and document structures in a bounded P5 reading

This working draft waits for source-support review and validated assertions. Under the synthesis-role rule in knowledge/governance.md it cannot enter 40_output until those prerequisites are satisfied. The earlier chapter-scoped structural check established only schema consistency and did not authorize synthesis from unreviewed assertions. This file is a working record and cannot ground research claims.

This draft uses the assertions prepared for the first Text and Document Structures run. Their source-support reviews and human verification remain open. The account distinguishes source statements from proposed questions for comparison.[^scope]

## Structural alternatives already described by P5

P5 4.12.0 presents multiple encodings, empty boundary markers, fragmentation with virtual reconstitution and stand-off markup as methods for non-hierarchical information.[^methods] It uses join to combine explicitly identified elements into a virtual aggregate.[^join] The Guidelines also report that stand-off annotation can combine discontinuous segments in a single annotation.[^discontinuous]

These accounts include processing qualifications. The chapter on non-hierarchical structures identifies repeated textual content and absent explicit relations between views as disadvantages of multiple encoding.[^multiple] It distinguishes the inability of grammar-based schemas to define a content model for an empty-element-delimited range from the ability of rule-based schemas to constrain sequences between such elements.[^validation]

An eventual architecture comparison should test the documented alternatives on the same editorial task. Useful observations would include which logical objects are explicitly addressable, what reconstruction a query requires, and which constraints can be checked. These are proposed comparison questions; the present source account supplies no implementation measurements or preferred architecture.[^comparison]

## Divisions, interrupted texts and reading order

P5 categorizes divisions independently of hierarchical level and permits numbered divisions or recursively nested unnumbered divisions. It prohibits combining the two styles within one front, body or back element.[^divisions] In its composite newspaper example, P5 says the individual stories may be read in any order and added or removed without affecting existing components.[^order]

P5 describes floatingText as an independent text after which its containing text resumes.[^floating] It distinguishes the external-source implication of quote from floatingText, whose meaning carries no such implication.[^origin] The local div-in-l Schematron rule requires a div descendant of l to have a floatingText ancestor.[^line] The div-in-ab-or-p rule reports a div with a p or ab ancestor when no floatingText ancestor is present.[^paragraph]

For generated divisions, P5 assigns divGen processing to the application or stylesheet; the markup identifies where and what kind of division should be generated.[^generated] A proposed mapping study should therefore declare its treatment of interrupted text, independently ordered components and application-generated content before comparing representations. The needed editorial observations and effective customization remain open.[^mapping]

## Fragmentation and the meaning of part

P5 identifies self-overlap and nested occurrences of the same element type as difficulties for determining fragment grouping or order with part.[^ambiguity] Its att.fragmentable value list defines I, M and F as the initial, medial and final parts of a fragmented element.[^fragment] The Default Text Structure chapter instead describes I, F and M as indicating material omitted initially, finally or in the middle of a division.[^omission]

This difference needs a separate interpretation check. A review should determine whether the two passages can be reconciled in their respective contexts or require a documented correction. Until that question is resolved, a mapping experiment should preserve the source wording and its uncertainty rather than silently selecting one interpretation.[^part]

## Page beginnings and notes

P5 permits associating a page beginning with an image of the introduced page through facs.[^image] The pb remarks distinguish the page number or other value carried by n from the physical sequence implicit in the presence of pb.[^number] The pinned overlap test document places a page beginning inside continuing paragraph text.[^test]

A bounded migration comparison should assess preservation of a page marker separately from the resolution and alignment of its image target. The proposed test would also state whether the reading includes printed pagination or other page furniture. Those decisions require an editorial case and expected observations beyond the pointer association documented here.[^media]

The P5 translator-note example requires the code referenced through resp to be defined elsewhere, for example in a responsibility statement in the associated TEI header.[^responsibility] P5 permits omitting sequential note numbers when software can reconstruct them automatically.[^notenumber] A proposed reading projection should make note responsibility, attachment and reconstructible numbering independently inspectable. Which note content should enter a main reading remains a task question for editorial review.[^notes]

## Discussion records and released statements

At the recorded 2026-09-06 snapshot, TEIC/TEI issue 1400 carried a label marking reconsideration for P6.[^p6] In issue 1505, a participant reported on 2017-05-03 having added a recommendation in the classSpec and Guidelines text.[^report] The pinned P5 4.12.0 specification recommends that next point to an element of the same type as the element bearing the attribute.[^next] It gives the corresponding recommendation for prev.[^prev]

A decision history connecting these observations should identify the relevant changes and releases before claiming a causal transition. The dated P6 label provides a starting point for examining the official process. Architecture recommendations would additionally require checked source support and comparative evidence about preservation and editorial use.[^history]

[^methods]: Grounded in [[30_assertions/structure-p5-has-several-nonhierarchical-methods]].
[^join]: Grounded in [[30_assertions/structure-p5-join-combines-virtual-elements]].
[^discontinuous]: Grounded in [[30_assertions/structure-p5-stand-off-discontinuous-annotation]].
[^multiple]: Grounded in [[30_assertions/structure-p5-multiple-encoding-maintenance-cost]].
[^validation]: Grounded in [[30_assertions/structure-p5-boundary-range-validation]].
[^divisions]: Grounded in [[30_assertions/structure-p5-division-type-is-independent-of-depth]].
[^order]: Grounded in [[30_assertions/structure-p5-composite-stories-have-flexible-order]].
[^floating]: Grounded in [[30_assertions/structure-p5-floatingtext-interrupts-resumable-text]].
[^origin]: Grounded in [[30_assertions/structure-p5-floatingtext-does-not-imply-external-origin]].
[^line]: Grounded in [[30_assertions/structure-p5-div-in-line-needs-floatingtext]].
[^paragraph]: Grounded in [[30_assertions/structure-p5-div-in-paragraph-needs-floatingtext]].
[^generated]: Grounded in [[30_assertions/structure-p5-divgen-processing-is-application-defined]].
[^ambiguity]: Grounded in [[30_assertions/structure-p5-part-reconstitution-ambiguity]].
[^fragment]: Grounded in [[30_assertions/structure-p5-part-positions-fragments]].
[^omission]: Grounded in [[30_assertions/structure-p5-part-locates-omissions-in-ds]].
[^image]: Grounded in [[30_assertions/structure-p5-pb-associates-page-image]].
[^number]: Grounded in [[30_assertions/structure-p5-pb-number-and-sequence]].
[^test]: Grounded in [[30_assertions/structure-p5-test-page-marker-inside-paragraph]].
[^responsibility]: Grounded in [[30_assertions/structure-p5-note-responsibility-code-needs-definition]].
[^notenumber]: Grounded in [[30_assertions/structure-p5-note-number-omission-is-conditional]].
[^p6]: Grounded in [[30_assertions/structure-p6-numbered-divisions-reconsideration-label]].
[^report]: Grounded in [[30_assertions/structure-issue1505-recommendation-self-report]].
[^next]: Grounded in [[30_assertions/structure-p5-next-same-type-recommendation]].
[^prev]: Grounded in [[30_assertions/structure-p5-prev-same-type-recommendation]].
[^scope]: Posit: the selected assertions are presented as a provisional source account whose research implications remain questions. Open evidence question: which statements survive the pending source-support and human reviews?
[^comparison]: Posit: a shared task can expose the preservation and processing commitments of existing and proposed representations. Open evidence question: which independently reviewed task and implementations permit a fair comparison?
[^mapping]: Posit: interruption, ordering and generated content need explicit mapping policies. Open evidence question: which effective customization and editorial expectations determine the distinctions to preserve?
[^part]: Posit: the differing explanations of part need interpretation before they can support a mapping rule. Open evidence question: can the source contexts reconcile the descriptions, and what evidence would settle their application?
[^media]: Posit: preserving a page marker, resolving its image and defining a reading projection are separate observations in a migration test. Open evidence question: which real edition and image-alignment task supplies the expected results?
[^notes]: Posit: a note projection should expose responsibility and attachment while stating any numbering policy. Open evidence question: which editorial reading requires inclusion or exclusion of particular note content?
[^history]: Posit: a process label or participant report initiates a decision-history inquiry. Open evidence question: which governance records, changes and releases establish a transition, and which comparative results justify a recommendation?
