---
type: assertion
topics: ["[[Interoperability and Processing]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/practice-v1-gerdracor-ger000260-43fe1901#^s1]]"
  - "[[20_distillates/documents/practice-v1-isicily-isic000156-262784ad#^s1]]"
  - "[[20_distillates/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b#^s1]]"
contested-with: []
related: []
created: 2026-09-11
updated: 2026-09-11
---

# Two sampled input documents point to RELAX NG locations without a version number; the sampled CMIF file has no processing instruction before its root

## Statement

The sampled GerDraCor play references `https://dracor.org/schema.rng` in an `xml-model` processing instruction. The sampled I.Sicily inscription references `https://epidoc.stoa.org/schema/latest/tei-epidoc.rng` and a relative Schematron path. Neither RELAX NG location contains a version number. The sampled CMIF file begins at byte 0 with its TEI start tag, so no processing instruction precedes the root element. Which schema a processor applies to each file on a given date is not established.

## Support

- [[20_distillates/documents/practice-v1-gerdracor-ger000260-43fe1901#^s1]] — the unversioned DraCor schema URL in the play.
- [[20_distillates/documents/practice-v1-isicily-isic000156-262784ad#^s1]] — the `latest` EpiDoc schema path and the relative Schematron in the inscription.
- [[20_distillates/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b#^s1]] — no processing instruction before the CMIF root element.

## Related

- [[30_assertions/practice-v1-epidoc-latest-guidance-and-isicily-reference]]
