---
type: assertion
topics: ["[[Interoperability and Processing]]", "[[ODD and Customization]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/practice-v1-dracor-build-c2f9e814#^s3]]"
  - "[[20_distillates/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^s2]]"
contested-with: []
related: []
created: 2026-09-11
updated: 2026-09-11
---

# The DraCor build script derives schemas with command-line converters, while the EpiDoc schema README names the OxGarage tool

## Statement

The DraCor build script runs `teitoodd` on `dracor.odd` to write `dist/dracor.odd.tmp`, then `teitorng` and `teitoschematron` on that intermediate file to write a RELAX NG schema and a Schematron file. The EpiDoc schema README states that the ODD requires the OxGarage tool to generate its RELAX NG schema. The assertion contrasts the two described paths. Neither path was executed by this project, and the README statement does not show how released EpiDoc schemas are currently produced.

## Support

- [[20_distillates/documents/practice-v1-dracor-build-c2f9e814#^s3]] — the converter sequence in the DraCor build script.
- [[20_distillates/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^s2]] — the tool the EpiDoc README names for schema generation.

## Related

- [[30_assertions/practice-v1-sampled-schematron-sits-in-odds-and-in-a-service]]
