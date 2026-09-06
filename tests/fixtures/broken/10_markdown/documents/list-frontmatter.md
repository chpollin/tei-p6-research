---
- a
- b
---

# Frontmatter that is not a map

Fixture: the frontmatter parses as a YAML list rather than a map of fields, so
no field of the schema can be read from it (defect: unreadable frontmatter).
