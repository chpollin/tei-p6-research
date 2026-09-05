---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-anchor-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: validated
checked:
  validation: 2026-09-05
  machine-review: 2026-09-05
created: 2026-09-05
updated: 2026-09-05
---

# Distillate: TEI P5 4.12.0 anchor specification

This distillate reports the English definition and identifier requirement in the complete `anchor.xml` specification at the pinned TEI P5 4.12.0 release commit.

## Core statements

- In TEI P5 4.12.0, `anchor` attaches an identifier to a point in a text, whether or not that point corresponds to a textual element. [[10_markdown/documents/tei-p5-anchor-4.12.0#^r1]] ^s1
- The English remarks for `anchor` in TEI P5 4.12.0 require an `xml:id` identifying the point where the element occurs. [[10_markdown/documents/tei-p5-anchor-4.12.0#^r2]] ^s2

## Terms

- **anchor**: the element that attaches an identifier to a point within a text. [[10_markdown/documents/tei-p5-anchor-4.12.0#^r1]]

## Open questions

- What further source material would establish how identifiers behave across distinct versions of an edited text?
- Which source or experiment could establish an appropriate migration policy when the text around an anchor changes?

## Appraisal

This narrow release-bound specification supports a distinction between an identified point and a textual element. Extending that distinction into immutable text versions or automatic reanchoring would be an independent modeling proposal requiring additional evidence and testing.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
