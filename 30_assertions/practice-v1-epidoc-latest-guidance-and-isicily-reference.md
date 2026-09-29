---
type: assertion
topics: ["[[Interoperability and Processing]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^s5]]"
  - "[[20_distillates/documents/practice-v1-isicily-isic000156-262784ad#^s1]]"
contested-with: []
related: []
created: 2026-09-11
updated: 2026-09-11
---

# EpiDoc's schema recommendation distinguishes stable publication from active development with schema updates; the sampled I.Sicily file references a latest path on a different host

## Statement

The EpiDoc schema README recommends the most recent numbered release available as of publication for complete, more or less static projects. It recommends the `latest` release at `https://www.stoa.org/epidoc/schema/latest/tei-epidoc.rng` for projects in active development whose editors are comfortable following community changes and updating their XML if the schema changes. The sampled I.Sicily inscription references `https://epidoc.stoa.org/schema/latest/tei-epidoc.rng`. The two sources use a `latest` path on different host names. Whether both locations serve the same schema, and whether the project applied the README's criterion, is not established.

## Support

- [[20_distillates/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^s5]] — the README's version recommendation and its `latest` URL.
- [[20_distillates/documents/practice-v1-isicily-isic000156-262784ad#^s1]] — the `latest` location the inscription references.

## Related

- [[30_assertions/practice-v1-sampled-inputs-associate-schemas-differently]]
