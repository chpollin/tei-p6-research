---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-rs-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: grounded
checked: {}
created: 2026-09-06
updated: 2026-09-11
---

# Distillate: TEI P5 4.12.0 rs specification

This distillate reports the English definition in the complete `rs.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `rs` contains a general purpose name or referring string. [[10_markdown/documents/tei-p5-rs-4.12.0#^r1]] ^s1

## Terms

- **rs**: the element that contains a general purpose name or referring string. [[10_markdown/documents/tei-p5-rs-4.12.0#^r1]]

## Open questions

- Which source states what a `type` value on `rs` names, given that the English reading text of this specification carries the definition alone?
- Which reading block or other source makes the class memberships of `rs` anchorable, given that its XML declares `att.global`, `att.cmc`, `att.naming`, `att.typed` and `model.nameLike` while the English reading text states no class membership?
- Would the separate specifications of the declared attribute classes `att.global`, `att.cmc`, `att.naming` and `att.typed`, and of any class they draw on, carry the attributes such memberships supply at this release, and would `key`, `ref`, `nymRef` and `role` be among them?
- Which source states how a referring string differs from a name in TEI P5 4.12.0, since this specification carries no English remarks paragraph?
- What would establish which usage the English example in this specification demonstrates, since no English prose in the source explains it?

## Appraisal

The English reading projection of this source carries one description, so the distillate rests on a single statement and reaches no further. The complete XML preserved in the representation declares more than that reading text says, and those declarations stay outside the core statements until a reading block or another admitted source carries them. Class membership is declared only in that XML, and typing and attribute semantics of `rs` need the class specifications as sources of their own.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
