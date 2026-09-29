---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-person-4.12.0]]"
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
status: grounded
checked: {}
created: 2026-09-06
updated: 2026-09-11
---

# Distillate: TEI P5 4.12.0 person specification

This distillate reports the English definition, the four attribute descriptions with their remarks and the content remark in the complete `person.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `person` provides information about an identifiable individual, for example a participant in a language interaction or a person referred to in a historical source. [[10_markdown/documents/tei-p5-person-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the English remarks for `person` state that it may contain either a prose description organized as paragraphs or a sequence of more specific demographic elements drawn from the `model.personPart` class. [[10_markdown/documents/tei-p5-person-4.12.0#^r10]] ^s2
- In TEI P5 4.12.0, the `role` attribute of `person` specifies a primary role or classification for the person. [[10_markdown/documents/tei-p5-person-4.12.0#^r2]] ^s3
- In TEI P5 4.12.0, the English remarks on `person/@role` state that a project may define its values locally using arbitrary keywords, that each such keyword should be associated with a definition, and that such local definitions will typically be provided by a `valList` element in the project schema specification. [[10_markdown/documents/tei-p5-person-4.12.0#^r3]] ^s4
- In TEI P5 4.12.0, the `sex` attribute of `person` specifies the sex of the person. [[10_markdown/documents/tei-p5-person-4.12.0#^r4]] ^s5
- In TEI P5 4.12.0, the English remarks on `person/@sex` state that its values may be defined locally by a project or may refer to an external standard. [[10_markdown/documents/tei-p5-person-4.12.0#^r5]] ^s6
- In TEI P5 4.12.0, the `gender` attribute of `person` specifies the gender of the person. [[10_markdown/documents/tei-p5-person-4.12.0#^r6]] ^s7
- In TEI P5 4.12.0, the English remarks on `person/@gender` state that its values may be defined locally by a project or may refer to an external standard. [[10_markdown/documents/tei-p5-person-4.12.0#^r7]] ^s8
- In TEI P5 4.12.0, the `age` attribute of `person` specifies an age group for the person. [[10_markdown/documents/tei-p5-person-4.12.0#^r8]] ^s9
- In TEI P5 4.12.0, the English remarks on `person/@age` state that a project may define its values locally using arbitrary keywords, that each such keyword should be associated with a definition, and that such local definitions will typically be provided by a `valList` element in the project schema specification. [[10_markdown/documents/tei-p5-person-4.12.0#^r9]] ^s10

## Terms

- **person**: the element that provides information about an identifiable individual. [[10_markdown/documents/tei-p5-person-4.12.0#^r1]]
- **model.personPart**: the class from which the more specific demographic elements a `person` may contain are drawn. [[10_markdown/documents/tei-p5-person-4.12.0#^r10]]

## Open questions

- Which source establishes where a `person` element belongs, given that no reading block of this specification names `listPerson`, `particDesc` or any other container and the XML carries only two untranslated pointers into Guidelines sections?
- Which source admits the class memberships that the XML declares for `person`, namely `att.global`, `att.datable`, `att.editLike`, `att.sortable` and `model.personLike`, since no reading block reproduces that declaration?
- Which specific elements does `model.personPart` hold, since the reading blocks name the class without listing its members and elements such as birth and death occur only inside the XML examples?
- Which source states how a `person` record is referenced from a name occurrence in running text, given that no reading block names `xml:id` or any other identifier attribute?
- Which source draws the distinction between the record that describes a person and the occurrences of that person's name in a text, a distinction no reading block of this specification makes?
- Which source states whether the identifiable individual of the definition may be fictional as well as real, since no reading block addresses that question while the English prose of the vCard example speaks of a fictional character?
- What would admit the explanatory prose of the two English exempla as anchorable source locations, meaning the adaptation of the vCard standard for an unknown gender and the use of a `ref` element with a private URI scheme that the example prose says is presumably declared in the `teiHeader` with a `prefixDef`, given that the reading blocks reproduce only descriptions and remarks?

## Appraisal

The English reading blocks of this specification carry the definition of the element, four attribute descriptions with their remarks and one content remark, so they ground the stated semantics of `person` and its four attributes at the pinned release. The XML also holds the English gloss "person", the declared content model and English examples, two of them with explanatory prose, which no reading block reproduces. Class membership, including `model.personLike`, remains in XML declarations, the identifier practice is visible only in the example markup, and the specification names no container for a `person` record, which bounds what this distillate can support.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
