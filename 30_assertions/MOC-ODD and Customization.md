---
type: moc
topic: "ODD and Customization"
created: 2026-09-04
updated: 2026-09-06
---

# MOC: ODD and Customization

This map covers ODD as a specification and customization language together with the
rules and limits of TEI-conformant customization.

## Sources and distillates

<!-- distillates:begin -->
- [[20_distillates/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b]]
- [[20_distillates/documents/practice-v1-cmif-odd-d171133e]]
- [[20_distillates/documents/practice-v1-correspsearch-check-566b2d29]]
- [[20_distillates/documents/practice-v1-dracor-build-c2f9e814]]
- [[20_distillates/documents/practice-v1-dracor-odd-c2f9e814]]
- [[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8]]
- [[20_distillates/documents/practice-v1-epidoc-schema-readme-e5b68eb8]]
- [[20_distillates/documents/practice-v1-gerdracor-ger000260-43fe1901]]
- [[20_distillates/documents/practice-v1-isicily-isic000156-262784ad]]
<!-- distillates:end -->

## Assertions

<!-- assertions:begin -->
- [[30_assertions/practice-v1-cmif-evidence-restriction-appears-in-a-real-file]] — The sampled CMIF ODD replaces att.editLike with a class allowing only conjecture on optional @evidence, and a sampled file uses that value on a received date
- [[30_assertions/practice-v1-sampled-odds-name-their-tei-source-differently]] — The sampled DraCor and EpiDoc schemaSpec declarations carry different source values; the CMIF schemaSpec has no source attribute
- [[30_assertions/practice-v1-sampled-odds-select-modules-by-contrasting-mechanisms]] — The sampled ODDs select P5 modules with different moduleRef strategies: mostly whole modules, except lists, or include lists
- [[30_assertions/practice-v1-sampled-schema-generation-paths-differ]] — The DraCor build script derives schemas with command-line converters, while the EpiDoc schema README names the OxGarage tool
- [[30_assertions/practice-v1-sampled-schematron-sits-in-odds-and-in-a-service]] — In the sample, Schematron rules appear embedded in the DraCor and EpiDoc ODDs and as a separately named file in the correspSearch check service
<!-- assertions:end -->

## Open questions

- Which semantic commitments of a customization are checked formally, and which
  remain documented only in prose?
