---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.naming-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 att.naming specification

This distillate reports the English class description, the two English attribute descriptions and the English `nymRef` remarks in the complete `att.naming.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, the description of the attribute class `att.naming` states that the class "provides attributes common to elements which refer to named persons, places, organizations etc." [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the description of the `role` attribute in `att.naming` states that it may be used to specify further information about the entity referenced by this name in the form of a set of whitespace-separated values, for example the occupation of a person, or the status of a place. [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r2]] ^s2
- In TEI P5 4.12.0, the description of the `nymRef` attribute in `att.naming` states that it provides a means of locating the canonical form (`nym`) of the names associated with the object named by the element bearing it. [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r3]] ^s3
- In TEI P5 4.12.0, the English remarks on `nymRef` state that its value must point directly to one or more XML elements by means of one or more URIs separated by whitespace, and that if more than one is supplied the implication is that the name is associated with several distinct canonical names. [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r4]] ^s4

## Terms

- **att.naming**: the attribute class described as providing attributes common to elements which refer to named persons, places, organizations etc. [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r1]]
- **role**: the attribute described as specifying further information about the entity referenced by the name, in whitespace-separated values. [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r2]]
- **nymRef**: the attribute described as providing a means of locating the canonical form of the names associated with the object named by the element bearing it. [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r3]]
- **nym**: the canonical form of the names associated with the object named by the element bearing the attribute. [[10_markdown/documents/tei-p5-att.naming-4.12.0#^r3]]

## Open questions

- Which source material would establish the effect of the `memberOf key="att.canonical"` declaration, which this specification carries in its XML and in no English reading block?
- Which source would establish which elements and classes belong to `att.naming`, given that this specification names no member of its own?
- Which source would establish the optionality and the value space of `role` and `nymRef`, declared in this XML as `usage="opt"` with the datatypes `teidata.enumerated` and `teidata.pointer` and covered by no English reading block?
- Which source would establish what `role` and `nymRef` do not do, given that the English text states only what each attribute may be used for and what a `nymRef` value must point to?
- Which Guidelines chapters do the `listRef` pointers `#CONARS` and `#NDNYM` resolve to, and what do those chapters state about the attributes of this class?

## Appraisal

The source establishes how one release-pinned attribute class describes itself and its two attributes in English. It carries no worked encoding example, so the behavior of `role` and `nymRef` in documents remains to be established from the Guidelines chapters and from encoded material.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
