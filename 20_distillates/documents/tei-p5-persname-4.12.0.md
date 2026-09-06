---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-persname-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 persName specification

This distillate reports the English description carried by the complete `persName.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the English description of `persName` states that the element contains a proper noun or proper-noun phrase referring to a person. [[10_markdown/documents/tei-p5-persname-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the English description of `persName` states that this proper noun or proper-noun phrase possibly includes one or more of the person's forenames, surnames, honorifics and added names, with the enumeration left open by "etc.". [[10_markdown/documents/tei-p5-persname-4.12.0#^r1]] ^s2

## Terms

- **persName**: the element whose English description covers a proper noun or proper-noun phrase referring to a person. [[10_markdown/documents/tei-p5-persname-4.12.0#^r1]]

## Open questions

- The English reading projection of this source carries the description alone. Which further representation would make the declarations of the source anchorable, meaning its module assignment, its `classes` memberships and its `macro.phraseSeq` content model?
- The source declares class memberships without stating which attributes those classes contribute. Which admitted source establishes the attributes that reach `persName` through the declared classes `att.personal`, `att.typed` and the others, and whether `key`, `ref`, `nymRef` and `role` are among them?
- The XML carries examples in several languages and the English reading projection exposes none of them. Which representation could anchor the arrangement of name parts that the examples demonstrate?
- The source carries no English remarks paragraph. Which source establishes usage guidance for `persName` beyond its one description sentence?

## Appraisal

The English reading projection of this specification reduces to a single description sentence, so the source supports what the element is stated to contain and offers no anchorable evidence about its formal model. Class membership, content model and the attributes reaching `persName` require the specifications of those classes and macros as separately admitted sources, and joining them to this element belongs to the assertion layer.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
