---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-correspsearch-check-566b2d29]]"
topics: ["[[Interoperability and Processing]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: correspSearch CMIF check service at 566b2d29

Three passages of the `index.xql` check service in the correspSearch API repository show which modules it imports, how it obtains a document, and which checks it applies.

## Core statements

- The check service `index.xql` imports a module bound to the prefix `schxslt` by the namespace `https://doi.org/10.5281/zenodo.1495494` and a geonames check module from the local file `check-geonames.xql`. [[10_markdown/documents/practice-v1-correspsearch-check-566b2d29#^r1]] ^s1
- The document-loading branch first tests the `xml-file` parameter and, when present, obtains the uploaded data, base64-decodes it and parses it as XML. Otherwise, when the `$url` variable has a value, it loads the document with `doc($url)`. [[10_markdown/documents/practice-v1-correspsearch-check-566b2d29#^r2]] ^s2
- The service assembles a `check` element from `validation:jing-report` against `doc('cmi-customization.rng')`, `schxslt:validate` against `doc('cmif.sch')` and a geonames check, and transforms the result with `view.xsl`. [[10_markdown/documents/practice-v1-correspsearch-check-566b2d29#^r3]] ^s3

## Terms

No term definition is extracted from these passages.

## Open questions

- Which schema and Schematron copies does the deployed service resolve for `cmi-customization.rng` and `cmif.sch`, and which CMIF version do they encode?
- Does the service's result decide whether a CMIF file is harvested?

## Appraisal

The source is service code and was not executed. Its calls and file references
establish no validation outcome or equivalence between schema versions.

Acquisition record: [practice admission](../../sources/manifests/2026-09-11-practice-v1-admission.yaml).

## Related

- [[30_assertions/practice-v1-sampled-schematron-sits-in-odds-and-in-a-service]]
