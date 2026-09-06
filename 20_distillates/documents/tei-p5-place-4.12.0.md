---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-place-4.12.0]]"
topics: ["[[Metadata and Entities]]"]
status: grounded
checked:
  validation: 2026-09-06
created: 2026-09-06
updated: 2026-09-06
---

# Distillate: TEI P5 4.12.0 place specification

This distillate reports the English definition in the complete `place.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `place` contains data about a geographic location. [[10_markdown/documents/tei-p5-place-4.12.0#^r1]] ^s1

## Terms

- **place**: the element that contains data about a geographic location. [[10_markdown/documents/tei-p5-place-4.12.0#^r1]]

## Open questions

- Which source admits the class memberships that the XML declares for `place`, namely `att.global`, `att.datable`, `att.editLike`, `att.sortable`, `att.typed` and `model.placeLike`, since no reading block reproduces that declaration?
- Which source establishes what a `place` element may contain, given that the content model appears only in XML declarations naming `model.headLike`, `model.pLike`, `model.labelLike`, `model.placeStateLike`, `model.eventLike`, `name`, `model.noteLike`, `model.biblLike`, `model.ptrLike`, `idno`, `linkGrp`, `link`, `model.placeLike` and `listPlace`?
- Which source states whether a `place` may nest inside another `place`, since the XML content model and the English example both show that nesting while no reading block states it?
- Which source states what a `type` value on `place` names, given that the English reading text of this specification carries the definition alone?
- Which source states how a record describing a place relates to references to that place in running text, since this specification carries no English remarks paragraph?
- Which source states what counts as a geographic location here, meaning whether an imaginary or otherwise non-terrestrial place is admitted, since no reading block addresses that question?
- What would establish which usage the English example in this specification demonstrates, meaning a country named in two languages together with two nested settlements, since no English prose in the source explains it?
- Which source supplies the Guidelines section that the untranslated pointer `#NDGEOG` in the XML addresses, since no reading block reproduces it?

## Appraisal

The English reading projection of this source carries one description, so the distillate rests on a single statement and reaches no further. The complete XML preserved in the representation declares class memberships and a structured content model that the reading text does not state, and those declarations stay outside the core statements until a reading block or another admitted source carries them. Typing, containment and the relation between a place record and references to it therefore need the class specifications and the geographic names chapter of the Guidelines as sources of their own.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
