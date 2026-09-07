---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-07
---

# Distillate: TEI P5 4.12.0 Default Text Structure

This distillate reports the pinned English Default Text Structure chapter, with its structural alternatives, examples and stated limits. The accompanying section audit records source-specific coverage; transcluded specifications retain separate source identities.

## Core statements

- The P5 4.12.0 Default Text Structure chapter describes TEI as grouping metadata in teiHeader with encoded resources, including logical transcription, diplomatic transcription, facsimile images, stand-off information and feature system declarations. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b2]] ^s1
- Resources relating to the same source document and sharing metadata may follow a single teiHeader in one TEI element. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b3]] ^s2
- The chapter describes nested TEI elements as a means of combining collection-level metadata with individual documents and their own metadata. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b4]] ^s3
- The chapter describes teiCorpus as carrying its own header followed by complete TEI elements, thereby distinguishing collection-level and individual metadata. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b5]] ^s4
- The chapter makes availability of additional resource elements dependent on inclusion of the appropriate modules in the schema. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b7]] ^s5
- The chapter leaves the classification of borderline texts as unitary or composite to the encoder. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b8]] ^s6
- The chapter assigns body to a unitary text and group to a composite text whose body consists of subordinate texts or groups. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b9]] ^s7
- The chapter provides floatingText for an embedded text that interrupts or is quoted within another text without contributing to its hierarchical organization. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b12]] ^s8
- The chapter separates division type from hierarchical level and supplies numbered divisions or recursively nested unnumbered div elements, prohibiting their combination within a single front, body or back. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b16]] ^s9
- The chapter states that div receives type and subtype through membership in att.typed. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b18]] ^s10
- For numbered divisions, the chapter describes div1 through div7 and requires contained numbered divisions to be at the next lower level. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b23]] ^s11
- The chapter contrasts arbitrary nesting depth for unnumbered divisions with the depth limit of numbered divisions, and notes that one numbered level need not correspond to the same textual feature across works. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b28]] ^s12
- The chapter recommends reference strings or labels using n and xml:id for divisions regarded as significant for referencing. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b29]] ^s13
- The chapter illustrates customization by adding diaryEntry to model.divLike or by adding distinct diaryEntry, amEntry and pmEntry elements to numbered division classes. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b31]] ^s14
- The chapter describes incomplete source excerpts and ad hoc agglomerations of small texts as possible textual divisions, and acknowledges cases where subdivision order is difficult or impossible to determine. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b34]] ^s15
- The chapter illustrates an initial chapter sample with sample initial and part Y and recommends documenting incomplete sampling principles in samplingDecl. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b36]] ^s16
- The chapter describes part values I, F and M as indicating material omitted initially, finally or in the middle of a division, respectively. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b36]] ^s17
- For its composite newspaper example, the chapter says individual stories can be read in any order and added or removed without affecting existing components. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b38]] ^s18
- The chapter allows a textual division to begin with more than one head element. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b44]] ^s19
- The chapter states that the immediate parent of head implies its type or level and permits extending model.headLike with additional elements. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b45]] ^s20
- For heading-like material in the middle of text, the chapter leaves the decision about starting a new division to the encoder and suggests quote, q or cit for inserted or superimposed material. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b48]] ^s21
- The chapter reserves trailer for a heading-like feature at the end of a division. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b49]] ^s22
- The chapter uses byline and dateline for headings identifying authorship and provenance and explicitly extends their use beyond newspaper texts. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b52]] ^s23
- The chapter demonstrates opener and closer as grouping elements for sequences at the beginning or end of a division. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b53]] ^s24
- The chapter presents a prefatory argument encoded as a paragraph or a list as equally valid encodings of the same argument. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b56]] ^s25
- For an epigraph quotation with a bibliographic reference, the chapter recommends grouping quotation and source with cit. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b57]] ^s26
- The chapter defines a postscript as a passage added after a letter signature or, less frequently, after the main body of a book, article or essay. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b59]] ^s27
- The chapter makes the component-level elements available within divisions dependent on the modules in use. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b61]] ^s28
- The chapter states that low-level elements from different modules need not be kept together. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b62]] ^s29
- The chapter distinguishes group for independent texts regarded as one processing unit from floatingText for an independent text after which the containing text resumes. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b65]] ^s30
- The chapter states that a text belonging to a group may itself contain groups. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b69]] ^s31
- The chapter presents editorial introductory essays as either independent texts or front matter to embedded texts and deliberately shows both treatments for comparison. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b74]] ^s32
- The chapter suggests quotation or cit encoding as an alternative to treating short extracts in an anthology as texts in their own right. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b77]] ^s33
- The chapter describes a floating text A as contained in B with part of B preceding A and part following it, so that the whole of B cannot be tessellated in the described way. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b79]] ^s34
- The chapter states that floatingText belongs to model.divPart and can appear within a division-level element in the same way as a paragraph. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b80]] ^s35
- The chapter permits treating fragments of framing narrative as front or back matter where the nested tales have greater significance. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b83]] ^s36
- The chapter distinguishes the external-source implication of quote from floatingText, which carries no such implication and supplies a richer content model for a discrete inclusion. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b84]] ^s37
- The chapter permits floatingText within quote and quoted sections within floatingText. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b85]] ^s38
- The chapter assigns the processing of divGen to the application or stylesheet; the markup identifies the location and kind of the division to generate. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b89]] ^s39
- The chapter distinguishes front matter of the encoded text from the TEI header of the computer file. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b91]] ^s40
- The chapter permits excluding front matter and recommends recording that decision in samplingDecl. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b92]] ^s41
- The chapter illustrates table-of-contents links targeting either chapter divisions or identified page beginnings. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b94]] ^s42
- The chapter states that detailed bibliographical analysis of older title pages may require a more detailed module than the one proposed there. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b98]] ^s43
- The chapter permits figure within titlePage to record complex non-textual material and suggests graphic for simple ornaments or illustrations. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b99]] ^s44
- For title-page rendition, the chapter presents segmentation with seg and rend or a module specialized for typographic entities as possible approaches. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b105]] ^s45
- The chapter states that front and back have identical content models because conventions differ about the placement of material. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b108]] ^s46
- The chapter illustrates index references linked to identified pb elements when the original pagination is encoded. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b110]] ^s47
- The chapter identifies its module as textstructure and refers schema selection and module combination to the infrastructure discussion. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b115]] ^s48

## Terms

- **Default Text Structure**: the subject of this source-specific account of P5 structural encoding. [[10_markdown/documents/tei-p5-guidelines-ds-defaulttextstructure-4.12.0#^b2]]

## Open questions

- How do the chapter's account of part and its account of identical front and back content models reconcile with the pinned formal specifications?
- Which referenced specification constraints and external literature require separate extraction before this chapter's account can support an effective processing contract?

## Appraisal

The chapter is a release-specific normative source with illustrative examples. Reported processing advantages and difficulties remain attributed to the chapter. This extraction supplies no independent measurements of implementations or editorial practice. Examples and exceptions inform the account, while source dependencies and the finite section boundary remain visible in the audit.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
