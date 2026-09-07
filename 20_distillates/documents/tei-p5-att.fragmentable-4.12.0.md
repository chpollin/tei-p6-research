---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.fragmentable-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-07
---

# Distillate: TEI P5 4.12.0 att.fragmentable

This distillate extracts the English descriptions, local declarations and selected examples of the pinned att.fragmentable specification.

## Core statements

- The P5 4.12.0 class att.fragmentable provides attributes for representing fragmentation of a structural element, typically resulting from an overlapping hierarchy. [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0#^b1]] ^s1
- The part attribute describes fragmentation, with examples including a speech divided between stanzas, a paragraph split across a page division, and a verse line divided between speakers. [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0#^b3]] ^s2
- The closed value list for part defines Y as fragmentation in an unspecified respect and N as either absence of fragmentation or absence of a claim about completeness. [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0#^b7]] ^s3
- The part value list defines I, M and F as the initial, medial and final parts of a fragmented element, respectively. [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0#^b7]] ^s4
- The declaration of part gives N as its default value. [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0#^b6]] ^s5
- The remarks require I, M and F to be used only where it is clear how the element may be reconstituted. [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0#^b8]] ^s6

## Terms

- **att.fragmentable**: the construct described by this source. Its source-specific meaning is stated in the core statements above. [[10_markdown/documents/tei-p5-att.fragmentable-4.12.0#^b1]]

## Open questions

- How is reconstitution determined for self-overlapping fragments or repeated occurrences of the same element type?
- Which effective inherited rules apply when the referenced classes and datatypes are compiled in a particular customization?

## Appraisal

The extraction distinguishes declared rules from observed processor behavior. Examples establish the encodings presented by the specification. Other-language translations and effective schema compilation remain outside this extraction. The section audit records the examined units and exclusions.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
