---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-11
---

# Distillate: TEI P5 4.12.0 Non-hierarchical Structures

This distillate reports the pinned English Non-hierarchical Structures chapter, with its structural alternatives, examples and stated limits. The accompanying section audit records source-specific coverage; transcluded specifications retain separate source identities.

## Core statements

- The P5 4.12.0 Non-hierarchical Structures chapter identifies conflicts between physical and rhetorical structures, metrical and linguistic structures, direct speech and surrounding structures, and different analytical views of a document. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b2]] ^s1
- The chapter states that no current solution to non-nesting information combines formal simplicity, representation of every occurring or imaginable structure, and suitability for formal or mechanical validation. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b3]] ^s2
- The chapter presents multiple encodings, empty boundary elements, fragmentation with virtual reconstitution, and stand-off markup as methods for handling non-hierarchical information. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b4]] ^s3
- The chapter limits its worked metrical, grammatical and dialogic views to lines and line groups, sentences, and direct quotation respectively. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b5]] ^s4
- The multiple-encoding method captures each conflicting hierarchical view in a separate encoding of the same information. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b7]] ^s5
- The chapter calls multiple encoding TEI-conformant and simple to process per view, while identifying maintenance of repeated textual content and lack of explicit relations between views as disadvantages. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b11]] ^s6
- A note in the multiple-encoding discussion reports that identical textual content can serve as an indirect means of linking annotations. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b11]] ^s7
- Boundary marking identifies the start and end of material outside the privileged hierarchy while leaving no single XML element representing that material. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b13]] ^s8
- The chapter distinguishes the typographical line beginning marked by lb from a claim about metrical lineation, using Old English manuscripts as a counterexample to their correspondence. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b16]] ^s9
- The chapter illustrates delimiting sentences with anchor elements whose type and subtype identify their boundary roles. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b17]] ^s10
- The chapter calls the method of custom boundary elements TEI-conformant if the custom elements can be replaced by TEI elements and attributes without loss of information, and an extension if the custom elements introduce information or distinctions that cannot be captured using standard TEI elements. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b20]] ^s11
- The chapter describes adapting elements normally used to encode nesting textual features, such as said, seg or l, to serve as empty segment boundary delimiters when the features they encode cross hierarchical boundaries, with additional attributes, sID and eID in its example, that allow unambiguous correlation of start and end points, and says that this method has been introduced in the markup literature under various names, including Trojan milestones, HORSE markup, CLIX and COLT. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b21]] ^s12
- The chapter states that, depending on how the modifications are carried out, the method of adapted boundary delimiters may be TEI-conformant, if the modified elements and attributes can be mapped automatically and without loss of information to existing TEI markup structures such as milestone or anchor elements, may represent an extension, if the modified elements are placed in a distinct non-TEI namespace, or may produce a non-conformant and indeed strongly deprecated document, if the modified elements and attributes are not placed in such a namespace. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b21]] ^s13
- The noun-phrase example associates NPend anchors with identified NPstart anchors through corresp to distinguish overlapping analyses of the same type. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b23]] ^s14
- The chapter identifies ad hoc reconstruction of structures not uniformly represented by tree nodes as a processing difficulty of boundary delimiters. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b25]] ^s15
- The chapter states that grammar-based schema languages cannot define a content model for a range delimited by empty elements, while its note says rule-based languages can permit or prohibit sequences between such elements. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b26]] ^s16
- Fragmentation divides a single logical non-nesting element into smaller elements fitting the dominant hierarchy that can be reconstituted virtually. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b28]] ^s17
- The chapter illustrates inflation of element counts by marking seven seg spans for four linguistic sentences. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b31]] ^s18
- The chapter warns that fragments tagged as sentences can be semantically misleading because individual fragments need not be linguistic sentences. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b32]] ^s19
- The chapter uses next and prev to make relations between sentence fragments explicit and notes that this method of virtual joining is sometimes called chaining. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b34]] ^s20
- The chapter presents part values I, M and F as a mechanism for virtually joining fragments encoded with ab, l, lg, div or elements belonging to att.segLike. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b35]] ^s21
- The chapter identifies self-overlap and nested occurrences of the same element type as cases in which part-based reconstitution can leave fragment grouping or order difficult to determine. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b36]] ^s22
- The chapter demonstrates join elements listing target word identifiers to indicate the members of virtual sentences explicitly. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b37]] ^s23
- The chapter names as the major advantage of fragmentation and virtual joins that all the hierarchies in the text can be handled explicitly, both the privileged one directly represented and the alternate hierarchy that has been split up and rejoined, and as major disadvantages that, like most of the other methods it describes, the technique privileges one hierarchy over the others, requires special processing to reconstitute the elements of the other hierarchies and, except in the case of join, can be semantically misleading. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b39]] ^s24
- The chapter describes stand-off markup as a separate hierarchy whose XML nodes link to nodes in another XML document or spans of text. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b41]] ^s25
- The chapter says stand-off markup can annotate plain text using character offsets and can freely interlink several layers. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b42]] ^s26
- The chapter reports advantages of stand-off markup over embedded annotation: annotations can be produced for read-only sources and distributed separately from the source text. As further advantages mentioned in the literature, it lists combining discontinuous text segments in one annotation, independent annotations by independent parallel coders and different information layers in different annotation files. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b43]] ^s27
- The chapter identifies separate interpretation and interdependence of stand-off layers, together with potentially difficult generic access, as drawbacks. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b44]] ^s28
- The chapter states that stand-off markup involves a TEI extension insofar as it uses elements outside the TEI namespace. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b45]] ^s29
- In its section on non-XML-based approaches, the chapter lists shared-frontier trees, colored XML, MultiX, Just-In-Time-Trees, LMNL and MLCD, together with applying concurrent markup to XML, among the non-XML methods of encoding a text that either solve or do not suffer the problem of the inability to encode overlapping hierarchies. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b48]] ^s30
- The chapter states that these approaches are based either on non-standard XML processing or data models, or not based on XML at all, that since TEI is currently based on XML they are not described any further in the Guidelines, and that their use with TEI will certainly involve extensions and in most cases non-conformant documents. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b49]] ^s31

## Terms

- **Non-hierarchical Structures**: the subject of this source-specific account of P5 structural encoding. [[10_markdown/documents/tei-p5-guidelines-nh-non-hierarchical-4.12.0#^b2]]

## Open questions

- How do the cited alternatives behave in current implementations, and which of their capabilities preserve the independently selected editorial tasks?
- Which referenced specification constraints and external literature require separate extraction before this chapter's account can support an effective processing contract?

## Appraisal

The chapter is Guidelines prose at the pinned release with illustrative examples. It classifies the methods it presents as TEI-conformant, as extensions or as non-conformant, and weighs their advantages and disadvantages. These classifications and the reported processing advantages and difficulties remain attributed to the chapter. This extraction supplies no independent measurements of implementations or editorial practice.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
