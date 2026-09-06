---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-nym-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 nym specification

This distillate reports the English element description and the English description of the `parts` attribute in the complete `nym.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `nym` contains the definition for a canonical name or name component of any kind. [[10_markdown/documents/tei-p5-nym-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, `nym/@parts` points to constituent nyms. [[10_markdown/documents/tei-p5-nym-4.12.0#^r2]] ^s2

## Terms

- **nym**: the element that contains the definition for a canonical name or name component of any kind. [[10_markdown/documents/tei-p5-nym-4.12.0#^r1]]
- **parts**: the attribute described in this specification as pointing to constituent nyms. [[10_markdown/documents/tei-p5-nym-4.12.0#^r2]]

## Open questions

- Which source states in English what a `nym` may contain, given that this specification declares its content model only inside the XML, as an optional sequence of `idno` elements, members of `model.entryPart`, members of `model.pLike`, and further `nym` elements?
- Which source states in English the further formal declarations that this specification keeps inside the XML alone, meaning the class memberships `att.global`, `att.sortable` and `att.typed`, the English gloss `canonical name`, and the datatype and cardinality of `parts` as one or more values of `teidata.pointer`?
- Which source establishes how a name occurrence in a running text refers to a canonical name form, given that `nymRef` appears nowhere in this specification?
- Which source establishes where a `nym` belongs in a document, given that `listNym` appears nowhere in this specification and the only pointer to a Guidelines section is the XML `listRef` target `#NDNYM`?
- Which source explains what the examples demonstrate, given that this specification carries no remarks and its three examples carry no accompanying English prose?

## Appraisal

This specification carries two English descriptions and nothing else in prose. They establish the intended meaning of the element and of its `parts` attribute. Everything about how a name occurrence in a text reaches a canonical name form, and about the list structure that holds one, requires the Guidelines chapter that the XML `listRef` points to.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
