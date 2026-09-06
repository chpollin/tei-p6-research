---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-name-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 name specification

This distillate reports the English description and the English remarks in the complete `name.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `name` contains a proper noun or noun phrase. [[10_markdown/documents/tei-p5-name-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, the English remarks for `name` state that proper nouns referring to people, places, and organizations may be tagged instead with `persName`, `placeName`, or `orgName` when the TEI module for names and dates is included. [[10_markdown/documents/tei-p5-name-4.12.0#^r2]] ^s2

## Terms

- **name**: the element that contains a proper noun or noun phrase. [[10_markdown/documents/tei-p5-name-4.12.0#^r1]]

## Open questions

- Which source would establish what the class memberships declared in the XML of this specification (`att.global`, `att.cmc`, `att.datable`, `att.editLike`, `att.personal`, `att.typed`, `model.nameLike.agent`, `model.personPart`) contribute to `name`, given that no English reading block of this source covers them and the class specifications are not part of it?
- Which source would establish the role of the `type` attribute on `name`, given that this source shows `type` values only in its untranslated example and explains them in no English text?
- Which source would establish the content model of `name`, which this specification declares in XML through a reference to `macro.phraseSeq` alone?
- What evidence would establish when `name` rather than `persName`, `placeName`, or `orgName` is the appropriate choice, given that the English remarks state only that the more specific elements may be used instead when the module for names and dates is included?

## Appraisal

The English text of this specification is one description sentence and one remarks paragraph, so the source carries the definition of `name` and the pointer to the more specific name elements. Attribute semantics, class behavior, and the content model would need the class and macro specifications as separately admitted sources.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
