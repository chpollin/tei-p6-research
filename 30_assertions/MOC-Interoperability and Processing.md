---
type: moc
topic: "Interoperability and Processing"
created: 2026-09-04
updated: 2026-09-06
---

# MOC: Interoperability and Processing

This map covers TEI conformance, schema generation, validation, transformation,
interchange, tool chains and alternative representations.

## Sources and distillates

<!-- distillates:begin -->
- [[20_distillates/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b]]
- [[20_distillates/documents/practice-v1-correspsearch-check-566b2d29]]
- [[20_distillates/documents/practice-v1-dracor-build-c2f9e814]]
- [[20_distillates/documents/practice-v1-dracor-odd-c2f9e814]]
- [[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8]]
- [[20_distillates/documents/practice-v1-epidoc-schema-readme-e5b68eb8]]
- [[20_distillates/documents/practice-v1-gerdracor-ger000260-43fe1901]]
- [[20_distillates/documents/practice-v1-isicily-isic000156-262784ad]]
- [[20_distillates/documents/tei-p5-annotation-4.12.0]]
<!-- distillates:end -->

## Assertions

<!-- assertions:begin -->
- [[30_assertions/practice-v1-epidoc-latest-guidance-and-isicily-reference]] — EpiDoc's schema recommendation distinguishes stable publication from active development with schema updates; the sampled I.Sicily file references a latest path on a different host
- [[30_assertions/practice-v1-sampled-inputs-associate-schemas-differently]] — Two sampled input documents point to RELAX NG locations without a version number; the sampled CMIF file has no processing instruction before its root
- [[30_assertions/practice-v1-sampled-schema-generation-paths-differ]] — The DraCor build script derives schemas with command-line converters, while the EpiDoc schema README names the OxGarage tool
- [[30_assertions/practice-v1-sampled-schematron-sits-in-odds-and-in-a-service]] — In the sample, Schematron rules appear embedded in the DraCor and EpiDoc ODDs and as a separately named file in the correspSearch check service
<!-- assertions:end -->

## Open questions

- Which interoperability problems arise from the standard itself, which from
  customizations and which from particular processing systems?
