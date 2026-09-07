---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-div-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-07
---

# Distillate: TEI P5 4.12.0 div

This distillate extracts the English descriptions, local declarations and selected examples of the pinned div specification.

## Core statements

- The P5 4.12.0 div element contains a subdivision of the front, body or back of a text. [[10_markdown/documents/tei-p5-div-4.12.0#^b8]] ^s1
- The local class declarations of div include att.divLike and model.divLike. [[10_markdown/documents/tei-p5-div-4.12.0#^b16]] ^s2
- The div-in-l Schematron rule requires a div descendant of l to have a floatingText ancestor. [[10_markdown/documents/tei-p5-div-4.12.0#^b18]] ^s3
- The div-in-ab-or-p Schematron rule reports a div with a p or ab ancestor when it has no floatingText ancestor. [[10_markdown/documents/tei-p5-div-4.12.0#^b19]] ^s4
- The English div example nests divisions typed as part, chapter and section and supplies headings at these levels. [[10_markdown/documents/tei-p5-div-4.12.0#^b20]] ^s5
- The local div content declaration has references to model.divTop and model.global before an optional sequence, and references to model.divBottom and model.global at the end of that sequence. [[10_markdown/documents/tei-p5-div-4.12.0#^b17]] ^s6

## Terms

- **div**: the construct described by this source. Its source-specific meaning is stated in the core statements above. [[10_markdown/documents/tei-p5-div-4.12.0#^b8]]

## Open questions

- How do the local content declaration and referenced model classes expand in the effective schema?
- Which effective inherited rules apply when the referenced classes and datatypes are compiled in a particular customization?

## Appraisal

The extraction distinguishes declared rules from observed processor behavior. Examples establish the encodings presented by the specification. Other-language translations and effective schema compilation remain outside this extraction. The section audit records the examined units and exclusions.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
