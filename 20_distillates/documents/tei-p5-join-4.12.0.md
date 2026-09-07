---
type: distillate
source-type: document
representation: "[[10_markdown/documents/tei-p5-join-4.12.0]]"
topics: ["[[Text and Document Structures]]", "[[Annotation and Overlap]]"]
status: grounded
checked: {}
created: 2026-09-07
updated: 2026-09-07
---

# Distillate: TEI P5 4.12.0 join

This distillate extracts the English descriptions, local declarations and selected examples of the pinned join specification.

## Core statements

- The P5 4.12.0 join element identifies a possibly fragmented text segment by pointing to the possibly discontiguous elements composing it. [[10_markdown/documents/tei-p5-join-4.12.0#^b3]] ^s1
- The joinTargets3 Schematron constraint asserts that at least two target values must be supplied on join. [[10_markdown/documents/tei-p5-join-4.12.0#^b12]] ^s2
- The result attribute specifies the name of an element that the aggregation may be understood to represent. [[10_markdown/documents/tei-p5-join-4.12.0#^b13]] ^s3
- The scope attribute distinguishes joining entire target elements, including their roots, from joining only their children. [[10_markdown/documents/tei-p5-join-4.12.0#^b21]] ^s4
- With scope root, the indicated rooted subtrees become children of the virtual element created by join. [[10_markdown/documents/tei-p5-join-4.12.0#^b30]] ^s5
- With scope branches, the children of the indicated subtrees become children of the virtual element and the subtree roots are discarded. [[10_markdown/documents/tei-p5-join-4.12.0#^b30]] ^s6
- The declaration of scope supplies root as its default value. [[10_markdown/documents/tei-p5-join-4.12.0#^b29]] ^s7
- The English line-group example uses join with result lg and scope root to assemble three l elements identified by target. [[10_markdown/documents/tei-p5-join-4.12.0#^b31]] ^s8
- The English list example uses scope branches to combine items from three lists into a single virtual list. [[10_markdown/documents/tei-p5-join-4.12.0#^b36]] ^s9
- The local content declaration of join permits zero or more alternatives from model.descLike and model.certLike. [[10_markdown/documents/tei-p5-join-4.12.0#^b11]] ^s10

## Terms

- **join**: the construct described by this source. Its source-specific meaning is stated in the core statements above. [[10_markdown/documents/tei-p5-join-4.12.0#^b3]]

## Open questions

- Which processing contract determines the order and identity of a virtual aggregate across implementations?
- Which effective inherited rules apply when the referenced classes and datatypes are compiled in a particular customization?

## Appraisal

The extraction distinguishes declared rules from observed processor behavior. Examples establish the encodings presented by the specification. Other-language translations and effective schema compilation remain outside this extraction. The section audit records the examined units and exclusions.

## Related

- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
