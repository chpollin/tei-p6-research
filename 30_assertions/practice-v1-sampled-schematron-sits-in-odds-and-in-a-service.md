---
type: assertion
topics: ["[[ODD and Customization]]", "[[Interoperability and Processing]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s4]]"
  - "[[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s5]]"
  - "[[20_distillates/documents/practice-v1-correspsearch-check-566b2d29#^s3]]"
contested-with: []
related: []
created: 2026-09-11
updated: 2026-09-11
---

# In the sample, Schematron rules appear embedded in the DraCor and EpiDoc ODDs and as a separately named file in the correspSearch check service

## Statement

The DraCor ODD embeds a Schematron rule, marked as a warning, about how a document references the DraCor schema. The EpiDoc ODD embeds Schematron reports in its change to `gap`. The correspSearch CMIF check service applies a separately named Schematron file, `cmif.sch`, alongside a `validation:jing-report` call against `cmi-customization.rng`. The assertion reports where such rules appear in these sources. It does not establish how the rules behave when executed or whether the CMIF ODD embeds any rules.

## Support

- [[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s4]] — an embedded Schematron constraint with a warning role in the DraCor ODD.
- [[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s5]] — embedded Schematron reports on `gap` in the EpiDoc ODD.
- [[20_distillates/documents/practice-v1-correspsearch-check-566b2d29#^s3]] — the service combining RELAX NG and a separate `cmif.sch`.

## Related

- [[30_assertions/practice-v1-sampled-schema-generation-paths-differ]]
