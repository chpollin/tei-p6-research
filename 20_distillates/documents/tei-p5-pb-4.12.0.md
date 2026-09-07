---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-pb-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-07
---

# Distillate: TEI P5 4.12.0 pb

This distillate extracts the English descriptions, local declarations and selected examples of the pinned pb specification.

## Core statements

- The P5 4.12.0 pb element marks the beginning of a new page in a paginated document. [[10_markdown/documents/tei-p5-pb-4.12.0#^b8]] ^s1
- The local content declaration of pb is empty. [[10_markdown/documents/tei-p5-pb-4.12.0#^b17]] ^s2
- The pb example encodes differing page beginnings for two editions by giving their page numbers and ed values. [[10_markdown/documents/tei-p5-pb-4.12.0#^b18]] ^s3
- A page beginning may be associated with a facsimile image of the page it introduces using facs. [[10_markdown/documents/tei-p5-pb-4.12.0#^b20]] ^s4
- The pb remarks recommend placing pb at the start of the page it identifies. [[10_markdown/documents/tei-p5-pb-4.12.0#^b22]] ^s5
- For pb, n supplies a number or other value associated with the page, normally its printed page number or signature, while physical sequence is implicit in the presence of pb. [[10_markdown/documents/tei-p5-pb-4.12.0#^b22]] ^s6
- The pb remarks prefer break, ed or edRef over the general type attribute when describing word breaking or the source of a page beginning. [[10_markdown/documents/tei-p5-pb-4.12.0#^b22]] ^s7

## Terms

- **pb**: the construct described by this source. Its source-specific meaning is stated in the core statements above. [[10_markdown/documents/tei-p5-pb-4.12.0#^b8]]

## Open questions

- How is the image pointer resolved and how are page regions aligned in a complete edition?
- Which effective inherited rules apply when the referenced classes and datatypes are compiled in a particular customization?

## Appraisal

The extraction distinguishes declared rules from observed processor behavior. Examples establish the encodings presented by the specification. Other-language translations and effective schema compilation remain outside this extraction. The section audit records the examined units and exclusions.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
