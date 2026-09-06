---
type: assertion
topics: ["[[Metadata and Entities]]"]
phenomena: ["[[glossary/entity-identification]]"]
related: ["[[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]]", "[[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s4]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, key serves cases where no direct link is required, because a local convention resolves the reference or because the encoder judges that no resolution is necessary

## Statement

In TEI P5 4.12.0, the Guidelines provide the key attribute for cases where no direct link is required, either because resolution of the reference is carried out by some local convention, as when a project maintains its own local database whose entries are accessed through a system-specific identifier constructed from the key value, or because the encoder judges that no resolution is necessary, as with well-established codifications such as country or airport codes.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s4]] — The chapter's assignment of key to the two cases without a direct link. It establishes the division of labour between key and ref as the chapter states it, and it does not say what applies when both a local key and a URI are available.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]]
