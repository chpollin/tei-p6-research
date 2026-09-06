---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]", "[[Abstract Model]]"]
phenomena: ["[[glossary/entity-identification]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]]", "[[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]]", "[[30_assertions/teic-tei-issue-337-author-reports-a-wish-to-deprecate-key-held-back-by-its-wide-use]]", "[[30_assertions/p5-guidelines-state-that-interchange-is-improved-by-tag-uris-in-ref-instead-of-key]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s10]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, att.canonical provides no semantic basis and suggests no precedence when both key and ref are supplied

## Statement

In TEI P5 4.12.0, the remarks on att.canonical state that the Guidelines provide no semantic basis and no suggested precedence when both key and ref are provided on the same element.

## Support

- [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s10]] — The class remarks on the co-occurrence of the two attributes. They establish the absence of a rule at the class level; the chapter's preference for ref, recorded in [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]], concerns the choice between them and states no precedence for reading both.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
- [[30_assertions/MOC-Abstract Model]]
- [[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]]
