---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
phenomena: ["[[glossary/name-as-an-object]]", "[[glossary/entity-identification]]"]
related: ["[[30_assertions/p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object]]"]
status: contested
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-att.naming-4.12.0#^s3]]"
contested-with: ["[[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]]"]
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, att.naming describes nymRef as locating the canonical form of the names associated with the object named by the element bearing it

## Statement

In TEI P5 4.12.0, the description of the nymRef attribute in the class att.naming states that it provides a means of locating the canonical form, the nym, of the names associated with the object named by the element bearing it.

## Support

- [[20_distillates/documents/tei-p5-att.naming-4.12.0#^s3]] — The attribute description in the class specification. It reaches the canonical form through the object named, which is where it diverges from the chapter's statement recorded in [[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]]. The description states nothing about whether the canonical form belongs to the name or to the object.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
- [[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]]
