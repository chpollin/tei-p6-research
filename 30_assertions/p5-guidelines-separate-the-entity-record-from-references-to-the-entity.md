---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Abstract Model]]"]
phenomena: ["[[glossary/entity-record]]", "[[glossary/mention-of-an-entity]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]]", "[[30_assertions/p5-person-provides-information-about-an-identifiable-individual]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s40]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the Guidelines describe org, in a way analogous to place and person, as a unique wrapper for information about an entity distinct from the references to that entity, which a naming element typically encodes

## Statement

In TEI P5 4.12.0, the Guidelines state that org and listOrg store data about an organization, such as its preferred name, its locations or key persons within it, in a way analogous to place and person, meaning a unique wrapper for information about an entity distinct from references to that entity, which are typically encoded with a naming element such as name of type org or orgName. The content of a naming element represents the way an organization is named in a given context, while the content of org represents the information known to the encoder about that organization, gathered in a single place and independent of its textual realization.

## Support

- [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s40]] — The chapter's statement of the record and reference contrast for organizations, which it presents as analogous to place and person. It establishes the contrast in the chapter's own general wording and establishes nothing about the person and place records beyond that analogy.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Abstract Model]]
- [[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]]
