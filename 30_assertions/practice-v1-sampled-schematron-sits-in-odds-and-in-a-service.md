---
type: assertion
topics: ["[[ODD and Customization]]", "[[Interoperability and Processing]]"]
status: grounded
checked:
  validation: 2026-10-17
grounding:
  - "[[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s4]]"
  - "[[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s5]]"
  - "[[20_distillates/documents/practice-v1-correspsearch-check-566b2d29#^s3]]"
contested-with: []
related: []
created: 2026-09-11
updated: 2026-10-17
---

# The sample records a DraCor ODD Schematron constraint, EpiDoc Schematron reports and a separately named correspSearch Schematron file

## Statement

The DraCor ODD adds a Schematron constraint in a rule on the TEI root with `role="warning"`. The constraint asserts that the root has `@type='dracor'` or the document has an `xml-model` processing instruction, and that such an instruction references `https://dracor.org/schema.rng`. The EpiDoc ODD embeds Schematron reports in its change to `gap`. The correspSearch CMIF check service applies a separately named Schematron file, `cmif.sch`, alongside a `validation:jing-report` call against `cmi-customization.rng`. The assertion reports declarations in these sources. It does not establish how the rules behave when executed or whether the CMIF ODD embeds any rules.

## Support

- [[20_distillates/documents/practice-v1-dracor-odd-c2f9e814#^s4]] — a Schematron constraint added by the DraCor ODD, including its two alternatives and the warning role.
- [[20_distillates/documents/practice-v1-epidoc-odd-e5b68eb8#^s5]] — embedded Schematron reports on `gap` in the EpiDoc ODD.
- [[20_distillates/documents/practice-v1-correspsearch-check-566b2d29#^s3]] — the service combining RELAX NG and a separate `cmif.sch`.

## Related

- [[30_assertions/practice-v1-sampled-schema-generation-paths-differ]]
