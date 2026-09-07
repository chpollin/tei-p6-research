---
type: moc
topic: "Text and Document Structures"
created: 2026-09-04
updated: 2026-09-06
---

# MOC: Text and Document Structures

This map covers the modeling of logical text structures, material document
structures, order, hierarchy and segmentation in TEI P5.

## Sources and distillates

<!-- distillates:begin -->
- [[20_distillates/documents/humboldt-h0017682-7d174637]]
- [[20_distillates/documents/tei-p5-anchor-4.12.0]]
- [[20_distillates/documents/tei-p5-att.fragmentable-4.12.0]]
- [[20_distillates/documents/tei-p5-att.global.linking-4.12.0]]
- [[20_distillates/documents/tei-p5-div-4.12.0]]
- [[20_distillates/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0]]
- [[20_distillates/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0]]
- [[20_distillates/documents/tei-p5-join-4.12.0]]
- [[20_distillates/documents/tei-p5-milestone-4.12.0]]
- [[20_distillates/documents/tei-p5-note-4.12.0]]
- [[20_distillates/documents/tei-p5-pb-4.12.0]]
- [[20_distillates/documents/tei-p5-span-4.12.0]]
- [[20_distillates/documents/tei-p5-test-testoverlap-4.12.0]]
- [[20_distillates/publications/teic-tei-issue-1400]]
- [[20_distillates/publications/teic-tei-issue-1505]]
<!-- distillates:end -->

## Assertions

<!-- assertions:begin -->
- [[30_assertions/humboldt-diary-encodes-a-dated-nested-heading]] — Humboldt diary H0017682 encodes a dated heading with nested highlighting
- [[30_assertions/humboldt-diary-encodes-a-page-pointer-and-separate-foliation]] — Humboldt diary H0017682 encodes a page pointer and separate foliation
- [[30_assertions/structure-issue1505-recommendation-self-report]] — On 2017-05-03, a participant in TEIC/TEI issue 1505 reported adding a recommendation in the classSpec and Guidelines text.
- [[30_assertions/structure-p5-boundary-range-validation]] — P5 4.12.0 distinguishes the inability of grammar-based schemas to define a content model for an empty-element-delimited range from the ability of rule-based schemas to constrain sequences between such elements.
- [[30_assertions/structure-p5-composite-stories-have-flexible-order]] — For its composite newspaper example, P5 4.12.0 states that individual stories can be read in any order and added or removed without affecting existing components.
- [[30_assertions/structure-p5-div-in-line-needs-floatingtext]] — The P5 4.12.0 div-in-l Schematron rule requires a div descendant of l to have a floatingText ancestor.
- [[30_assertions/structure-p5-div-in-paragraph-needs-floatingtext]] — The P5 4.12.0 div-in-ab-or-p Schematron rule reports a div with a p or ab ancestor when it has no floatingText ancestor.
- [[30_assertions/structure-p5-divgen-processing-is-application-defined]] — P5 4.12.0 assigns divGen processing to the application or stylesheet while the markup identifies where and what kind of division is to be generated.
- [[30_assertions/structure-p5-division-type-is-independent-of-depth]] — P5 4.12.0 categorizes divisions independently of hierarchical level and permits numbered or recursively nested unnumbered divisions, while prohibiting their combination within one front, body or back.
- [[30_assertions/structure-p5-floatingtext-does-not-imply-external-origin]] — P5 4.12.0 distinguishes the external-source implication of quote from floatingText, whose meaning carries no such implication.
- [[30_assertions/structure-p5-floatingtext-interrupts-resumable-text]] — P5 4.12.0 describes floatingText as representing an independent text after which the containing text resumes.
- [[30_assertions/structure-p5-has-several-nonhierarchical-methods]] — P5 4.12.0 presents multiple encodings, boundary marking, fragmentation with virtual reconstitution and stand-off markup as methods for non-hierarchical information.
- [[30_assertions/structure-p5-join-combines-virtual-elements]] — P5 4.12.0 uses join to combine explicitly identified elements into a virtual aggregate.
- [[30_assertions/structure-p5-multiple-encoding-maintenance-cost]] — P5 4.12.0 identifies repeated textual content and absent explicit relations between views as disadvantages of the multiple-encoding method.
- [[30_assertions/structure-p5-next-same-type-recommendation]] — P5 4.12.0 recommends that next point to an element of the same type as the element bearing the attribute.
- [[30_assertions/structure-p5-note-number-omission-is-conditional]] — P5 4.12.0 permits omitting sequential note numbers when processing software can reconstruct them automatically.
- [[30_assertions/structure-p5-note-responsibility-code-needs-definition]] — The P5 4.12.0 translator-note example requires its resp code to be defined elsewhere, for example in a responsibility statement in the associated TEI header.
- [[30_assertions/structure-p5-part-locates-omissions-in-ds]] — The P5 4.12.0 Default Text Structure chapter describes part values I, F and M as indicating material omitted initially, finally or in the middle of a division.
- [[30_assertions/structure-p5-part-positions-fragments]] — The P5 4.12.0 att.fragmentable value list defines I, M and F as the initial, medial and final parts of a fragmented element.
- [[30_assertions/structure-p5-part-reconstitution-ambiguity]] — P5 4.12.0 identifies self-overlap and nested occurrences of the same element type as difficulties for determining fragment grouping or order with part.
- [[30_assertions/structure-p5-pb-associates-page-image]] — P5 4.12.0 permits associating a page beginning with a facsimile image of the introduced page through facs.
- [[30_assertions/structure-p5-pb-number-and-sequence]] — P5 4.12.0 distinguishes the page number or other value carried by pb/@n from physical sequence implicit in the presence of pb.
- [[30_assertions/structure-p5-prev-same-type-recommendation]] — P5 4.12.0 recommends that prev point to an element of the same type as the element bearing the attribute.
- [[30_assertions/structure-p5-stand-off-discontinuous-annotation]] — P5 4.12.0 reports that stand-off annotation can combine discontinuous text segments in one annotation.
- [[30_assertions/structure-p5-test-page-marker-inside-paragraph]] — The pinned P5 4.12.0 overlap test document encodes a page beginning inside continuing paragraph text.
- [[30_assertions/structure-p6-numbered-divisions-reconsideration-label]] — At the recorded 2026-09-06 snapshot, TEIC/TEI issue 1400 carried a label marking reconsideration for P6.
<!-- assertions:end -->

## Open questions

- Which structural concepts does P5 separate conceptually, and which remain coupled
  through the XML tree?
