---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-note-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-07
---

# Distillate: TEI P5 4.12.0 note

This distillate extracts the English descriptions, local declarations and selected examples of the pinned note specification.

## Core statements

- The P5 4.12.0 note element contains a note or annotation. [[10_markdown/documents/tei-p5-note-4.12.0#^b3]] ^s1
- The local class declarations of note include att.anchoring, att.placement, att.pointing and model.noteLike. [[10_markdown/documents/tei-p5-note-4.12.0#^b10]] ^s2
- The local content declaration of note references macro.specialPara. [[10_markdown/documents/tei-p5-note-4.12.0#^b11]] ^s3
- The English translator-note example embeds a note within a sentence and gives it place bottom, type gloss and a resp pointer to a responsibility statement. [[10_markdown/documents/tei-p5-note-4.12.0#^b12]] ^s4
- The English translator-note example requires the code used by its resp pointer to be defined elsewhere, for example in a responsibility statement in the associated TEI header. [[10_markdown/documents/tei-p5-note-4.12.0#^b12]] ^s5
- The note example explains that n can supply the symbol or number marking the attachment point in the source text. [[10_markdown/documents/tei-p5-note-4.12.0#^b17]] ^s6
- The note example permits omission of sequential note numbers when processing software can reconstruct them automatically. [[10_markdown/documents/tei-p5-note-4.12.0#^b17]] ^s7

## Terms

- **note**: the construct described by this source. Its source-specific meaning is stated in the core statements above. [[10_markdown/documents/tei-p5-note-4.12.0#^b3]]

## Open questions

- Which reading and placement rules govern nested notes and stand-off notes in a particular editorial task?
- Which effective inherited rules apply when the referenced classes and datatypes are compiled in a particular customization?

## Appraisal

The extraction distinguishes declared rules from observed processor behavior. Examples establish the encodings presented by the specification. Other-language translations and effective schema compilation remain outside this extraction. The section audit records the examined units and exclusions.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
