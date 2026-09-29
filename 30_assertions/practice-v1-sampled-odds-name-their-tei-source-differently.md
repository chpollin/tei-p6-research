---
type: assertion
topics: ["[[ODD and Customization]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s1]]"
  - "[[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s3]]"
  - "[[20_distillates/documents/practice-v1-cmif-odd-d171133e#^s1]]"
contested-with: []
related: []
created: 2026-09-11
updated: 2026-09-11
---

# The sampled DraCor and EpiDoc schemaSpec declarations carry different source values; the CMIF schemaSpec has no source attribute

## Statement

The sampled DraCor ODD declares `schemaSpec/@source="tei:4.12.0"`, the EpiDoc ODD declares the TEI Vault URL of the P5 4.10.2 `p5subset.xml`, and the CMIF ODD carries no `source` attribute on its `schemaSpec`. The observation covers these three declarations only and says nothing about which TEI source a processor actually uses.

## Support

- [[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s1]] — DraCor names `tei:4.12.0` as the source.
- [[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s3]] — EpiDoc names the 4.10.2 Vault subset URL.
- [[20_distillates/documents/practice-v1-cmif-odd-d171133e#^s1]] — CMIF declares no `source` attribute.

## Related

- [[30_assertions/practice-v1-sampled-odds-select-modules-by-contrasting-mechanisms]]
