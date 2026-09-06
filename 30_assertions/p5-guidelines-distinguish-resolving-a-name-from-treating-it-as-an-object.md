---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Abstract Model]]"]
phenomena: ["[[glossary/name-as-an-object]]", "[[glossary/entity-identification]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-nym-contains-the-definition-of-a-canonical-name-or-name-component]]", "[[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s55]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the Guidelines distinguish the resolution of a name or referring string to its referent through key or ref from the treatment of names as objects in their own right, for whose canonical or normalized form they use the term nym

## Statement

In TEI P5 4.12.0, the Guidelines summarize the resolution of a name or referring string as a matter of the object it refers to, effected through key or ref on any member of att.naming, and then treat names as objects in their own right irrespective of the objects they are attached to, notably in onomastic studies. They use the term nym for the canonical or normalized form of a name regarded in this way and provide listNym and nym to encode it.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s55]] — The chapter's summary at the start of its section on nyms. It establishes the two-way distinction between resolving a name and studying it, reserves the term nym for the canonical or normalized form of a name so regarded, and establishes nothing about whether a canonical name in the sense of the module's purpose statement is the same notion.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Abstract Model]]
- [[30_assertions/p5-nym-contains-the-definition-of-a-canonical-name-or-name-component]]
