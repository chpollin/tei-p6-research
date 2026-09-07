---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-att.global.linking-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-07
---

# Distillate: TEI P5 4.12.0 att.global.linking

This distillate extracts the English descriptions, local declarations and selected examples of the pinned att.global.linking specification.

## Core statements

- The P5 4.12.0 class att.global.linking provides attributes for hypertextual linking. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b1]] ^s1
- The corresp attribute points to elements corresponding to the current element in some way. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b16]] ^s2
- The corresp example links a place record for London with literary person records while explicitly denying that the allegorical character and physical city could be substituted for each other. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b26]] ^s3
- The synch attribute points to elements synchronous with the current element. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b34]] ^s4
- The sameAs attribute points to an element that is the same as the current element. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b43]] ^s5
- The copyOf attribute points to an element of which the current element is a copy. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b52]] ^s6
- The copyOf remarks direct processing to ignore any content of the current element and take its true content from the pointed-to element. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b61]] ^s7
- The next attribute points to the next element of a virtual aggregate of which the current element is part. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b67]] ^s8
- The prev attribute points to the previous element of a virtual aggregate of which the current element is part. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b85]] ^s9
- The next remarks recommend that the target element have the same type as the element bearing the attribute. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b76]] ^s10
- The prev remarks recommend that the target element have the same type as the element bearing the attribute. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b94]] ^s11
- The exclude attribute points to elements in exclusive alternation with the current element. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b96]] ^s12
- The select attribute selects alternants; selecting one marks ambiguity or uncertainty as resolved, while selecting several marks it as reduced by the number not selected. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b105]] ^s13
- The select remarks recommend placing the attribute on an element superordinate to all alternants from which the selection is made. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b113]] ^s14

## Terms

- **att.global.linking**: the construct described by this source. Its source-specific meaning is stated in the core statements above. [[10_markdown/documents/tei-p5-att.global.linking-4.12.0#^b1]]

## Open questions

- Which constraints establish reciprocal linking, cycle handling and aggregate ordering beyond the individual next and prev descriptions?
- Which effective inherited rules apply when the referenced classes and datatypes are compiled in a particular customization?

## Appraisal

The extraction distinguishes declared rules from observed processor behavior. Examples establish the encodings presented by the specification. Other-language translations and effective schema compilation remain outside this extraction. The section audit records the examined units and exclusions.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
