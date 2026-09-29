---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-span-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-05
updated: 2026-09-11
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
- How far do the English description of `to` and the Schematron constraints in the XML, which report `from` or `to` combined with `target`, `to` without `from`, and more than one value in either attribute, bound the use of `from` described above, given that this distillate reports neither?

## Appraisal

The inspected descriptions are those the specification carries at the pinned release. They are not an endorsement of the pilot's half-open Unicode-code-point ranges, immutable text-version model, or reanchoring policy. Those remain independent proposals.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
