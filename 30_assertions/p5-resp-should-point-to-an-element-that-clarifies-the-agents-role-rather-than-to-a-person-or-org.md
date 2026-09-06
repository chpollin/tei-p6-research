---
type: assertion
topics: ["[[Metadata and Entities]]", "[[Elements and Classes]]"]
phenomena: ["[[glossary/responsibility-for-a-statement]]"]
related: ["[[40_output/12-p6-design]]", "[[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]]", "[[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]]", "[[30_assertions/p5-person-provides-information-about-an-identifiable-individual]]"]
status: validated
checked:
  machine-review: 2026-09-06
  validation: 2026-09-06
grounding:
  - "[[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0#^s7]]"
created: 2026-09-06
updated: 2026-09-06
---

# In TEI P5 4.12.0, the English remarks on resp in att.global.responsibility recommend pointing resp to a respStmt, an author, an editor or a similar element which clarifies the exact role played by the agent, and advise against pointing it to a person or an org

## Statement

In TEI P5 4.12.0, the English remarks on the resp attribute in att.global.responsibility recommend that resp be used to point to a respStmt, an author, an editor or a similar element which clarifies the exact role played by the agent, and advise against pointing it to an agent, meaning a person or an org.

## Support

- [[20_distillates/documents/tei-p5-att.global.responsibility-4.12.0#^s7]] — The remarks on resp at the pinned release. They establish that the target of a responsibility pointer is meant to be a statement of the agent's role rather than the record of the agent, which keeps the entity record and the responsibility statement apart, and they state nothing about the elements on which resp is available.

## Related

- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-Elements and Classes]]
- [[30_assertions/p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup]]
- [[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]]
