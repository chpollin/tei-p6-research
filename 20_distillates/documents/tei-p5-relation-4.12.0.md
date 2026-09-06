---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-relation-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 relation specification

This distillate reports the English descriptions and the English remarks paragraph carried by the complete `relation.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the English description of `relation` states that the element describes any kind of relationship or linkage amongst a specified group of items. [[10_markdown/documents/tei-p5-relation-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the English description of `relation` states that the relationship or linkage the element describes is one amongst a specified group of places, events, persons, objects or other items. [[10_markdown/documents/tei-p5-relation-4.12.0#^r1]] ^s2
- In TEI P5 4.12.0, the English description of the `name` attribute of `relation` states that it supplies a name for "the kind of relationship of which this is an instance". [[10_markdown/documents/tei-p5-relation-4.12.0#^r2]] ^s3
- In TEI P5 4.12.0, the English description of the `active` attribute of `relation` states that it identifies the active participants in a non-mutual relationship. [[10_markdown/documents/tei-p5-relation-4.12.0#^r3]] ^s4
- In TEI P5 4.12.0, the English description of the `active` attribute of `relation` states that it identifies all the participants in a mutual relationship. [[10_markdown/documents/tei-p5-relation-4.12.0#^r3]] ^s5
- In TEI P5 4.12.0, the English description of the `mutual` attribute of `relation` states that it supplies a list of participants amongst all of whom the relationship holds equally. [[10_markdown/documents/tei-p5-relation-4.12.0#^r4]] ^s6
- In TEI P5 4.12.0, the English description of the `passive` attribute of `relation` states that it identifies the passive participants in a non-mutual relationship. [[10_markdown/documents/tei-p5-relation-4.12.0#^r5]] ^s7
- In TEI P5 4.12.0, the English remarks for `relation` state that only one of the attributes `active` and `mutual` may be supplied. [[10_markdown/documents/tei-p5-relation-4.12.0#^r6]] ^s8
- In TEI P5 4.12.0, the English remarks for `relation` state that the attribute `passive` may be supplied only if the attribute `active` is supplied. [[10_markdown/documents/tei-p5-relation-4.12.0#^r6]] ^s9
- In TEI P5 4.12.0, the English remarks for `relation` state that not all of the constraints they state on `active`, `mutual` and `passive` can be enforced in all schema languages. [[10_markdown/documents/tei-p5-relation-4.12.0#^r6]] ^s10

## Terms

- **relation**: the element whose English description covers any kind of relationship or linkage amongst a specified group of places, events, persons, objects or other items. [[10_markdown/documents/tei-p5-relation-4.12.0#^r1]]
- **active**: the attribute identifying the active participants in a non-mutual relationship, or all the participants in a mutual one. [[10_markdown/documents/tei-p5-relation-4.12.0#^r3]]
- **mutual**: the attribute supplying a list of participants amongst all of whom the relationship holds equally. [[10_markdown/documents/tei-p5-relation-4.12.0#^r4]]
- **passive**: the attribute identifying the passive participants in a non-mutual relationship. [[10_markdown/documents/tei-p5-relation-4.12.0#^r5]]

## Open questions

- The English reading projection carries descriptions and one remarks paragraph alone. Which further representation would make the declarations of the source anchorable, meaning its `namesdates` module assignment, its declared class memberships `att.global`, `att.canonical`, `att.datable`, `att.editLike`, `att.sortable` and `att.typed`, and its content model of an optional `desc`?
- The source carries no English description of `type`, and the XML records that the local definition of the attribute was removed as vacuous and inconsistent with the text. Which source establishes the stated meaning of `type` on `relation` and how it reaches the element through `att.typed`?
- The XML declares a Schematron constraint requiring that one of `name`, `ref` or `key` be supplied, while the English remarks state only the constraints among `active`, `mutual` and `passive`. Which representation would make that requirement anchorable, and which source establishes the meaning of `ref` and `key` on `relation`?
- The source names no context in which `relation` may occur, so `listRelation` appears nowhere in it. Which source establishes where the element is permitted to stand?
- The English exempla and their explanatory prose lie outside the reading projection. Which representation could anchor the example that pairs a `name` value with `active` and `passive` pointers, the example that points at two resources by URL, or the example that assigns responsibility for identifying a relationship to an editor through `resp`?
- The descriptions separate mutual from non-mutual relationships without stating how the direction from active to passive participants is to be read by a processor. Which source establishes that reading?
- The remarks state that not all of the constraints can be enforced in all schema languages without saying which language enforces which. Which source establishes that mapping?

## Appraisal

The English reading projection of this specification supports what the element and its attributes `name`, `active`, `mutual` and `passive` are stated to mean, together with the two constraints the remarks spell out. Everything the source settles by declaration alone stays outside the anchorable evidence, meaning its class memberships, its content model, the `type` attribute and the Schematron requirement on `name`, `ref` and `key`, so each of those needs a further representation of this source or a separately admitted specification. The remark about schema languages concerns what a schema can enforce at this release and establishes nothing about encoding practice.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
