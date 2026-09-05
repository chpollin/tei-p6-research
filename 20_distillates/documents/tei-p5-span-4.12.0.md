---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-span-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: validated
checked:
  validation: 2026-09-05
  machine-review: 2026-09-05
created: 2026-09-05
updated: 2026-09-05
---

# Distillate: TEI P5 4.12.0 span specification

This distillate reports the English definition and `from` description in the complete `span.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `span` directly associates an interpretative annotation with a span of text. [[10_markdown/documents/tei-p5-span-4.12.0#^r1]] ^s1
- In TEI P5 4.12.0, `span/@from` identifies the starting node of the annotated span; without `@to`, it identifies the node for the entire annotated span. [[10_markdown/documents/tei-p5-span-4.12.0#^r2]] ^s2

## Terms

- **span**: the element associating an interpretative annotation directly with a span of text. [[10_markdown/documents/tei-p5-span-4.12.0#^r1]]

## Open questions

- What further sources would establish a mapping from these node identifiers to a particular character-offset convention?
- What evidence would support preserving an annotation's interpretation when the annotated text changes?

## Appraisal

The inspected descriptions concern a release-specific annotation mechanism. They are not an endorsement of the pilot's half-open Unicode-code-point ranges, immutable text-version model, or reanchoring policy. Those remain independent proposals.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
