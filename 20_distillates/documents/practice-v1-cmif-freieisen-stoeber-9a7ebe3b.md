---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b]]"
topics: ["[[Interoperability and Processing]]", "[[Metadata and Entities]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: CMIF file freieisen-stoeber.xml at 9a7ebe3b

Three passages of one CMIF file held in the correspSearch storage repository show how the document begins, its licence and its single correspondence description.

## Core statements

- The CMIF file `freieisen-stoeber.xml` begins at byte 0 with the start tag `<TEI xmlns="http://www.tei-c.org/ns/1.0">`, so no XML declaration or processing instruction precedes its root element. [[10_markdown/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b#^r1]] ^s1
- The file's `licence` element has the target `https://creativecommons.org/licenses/by/4.0/` and, after whitespace normalization, the text "CC-BY 4.0". [[10_markdown/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b#^r2]] ^s2
- The file's `correspDesc` has a `sent` action with a `persName` and a `placeName` carrying GND and GeoNames URIs and `date when="1839-03-08"`, and a `received` action whose `date` carries `evidence="conjecture"` and `when="1839-03-12"`. [[10_markdown/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b#^r3]] ^s3

## Terms

No term definition is extracted from these passages.

## Open questions

- Is the file valid against the CMIF 1.1 schema and the check service's schema copy?
- How does correspSearch associate this file with a schema version when no processing instruction precedes its root?

## Appraisal

The statements describe one letter-metadata record. No representativeness of
CMIF practice or schema validation is claimed. The acquisition manifest records
the selection and rights evidence. Personal names, the publisher and an email
address in the header remain untouched source data.

## Related

- [[30_assertions/practice-v1-sampled-inputs-associate-schemas-differently]]
- [[30_assertions/practice-v1-cmif-evidence-restriction-appears-in-a-real-file]]
