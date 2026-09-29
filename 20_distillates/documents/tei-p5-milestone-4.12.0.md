---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-milestone-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-11
---

# Distillate: TEI P5 4.12.0 milestone

This distillate extracts the English description, the local content declaration and the English remarks of the pinned milestone specification.

## Core statements

- The English P5 4.12.0 description states that milestone marks a boundary point separating any kind of section of a text, typically but not necessarily indicating a point at which some part of a standard reference system changes, where the change is not represented by a structural element. [[10_markdown/documents/tei-p5-milestone-4.12.0#^b4]] ^s1
- The local content declaration of milestone is empty. [[10_markdown/documents/tei-p5-milestone-4.12.0#^b13]] ^s2
- For milestone, n indicates the new number or other value of the unit that changes at the boundary. [[10_markdown/documents/tei-p5-milestone-4.12.0#^b17]] ^s3
- The English milestone remarks state that the special value unnumbered should be used in passages which fall outside the normal numbering scheme, such as chapter or other headings, poem numbers or titles. [[10_markdown/documents/tei-p5-milestone-4.12.0#^b17]] ^s4
- The milestone remarks state that the order of milestone elements at a given point is not normally significant. [[10_markdown/documents/tei-p5-milestone-4.12.0#^b17]] ^s5

## Terms

- **milestone**: the construct described by this source. Its source-specific meaning is stated in the core statements above. [[10_markdown/documents/tei-p5-milestone-4.12.0#^b4]]

## Open questions

- Which declared unit and spanning rules determine a milestone range in the effective customization?
- Which effective inherited rules apply when the classes declared in the XML, among them att.milestoneUnit and att.spanning, are compiled in a particular customization?

## Appraisal

The extraction reports declared rules and records no processor behavior. The examples of the specification, which carry no English prose, other-language translations and effective schema compilation remain outside this extraction. The section audit records the examined units and exclusions.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
