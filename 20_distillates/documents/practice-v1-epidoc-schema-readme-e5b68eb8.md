---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8]]"
topics: ["[[Interoperability and Processing]]", "[[ODD and Customization]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: EpiDoc schema README at e5b68eb8

The EpiDoc schema README describes the ODD and RelaxNG schema, their rights, the named schema-generation tool, the subset policy and the choice between numbered and latest schema releases.

## Core statements

- The README describes the EpiDoc RelaxNG schema and the TEI ODD file from which it is generated. [[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^r1]] ^s1
- The README states that the ODD requires the OxGarage tool to generate the RelaxNG schema. [[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^r3]] ^s2
- The README states as policy that the EpiDoc schema should be a conformant subset of the latest TEI schema, with exceptions only where the development TEI ODD contains changes that will not reach a TEI release for one to six months. [[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^r4]] ^s3
- The README's procedure for a new schema version converts `tei-epidoc.xml` from ODD Document to RELAX NG schema in the OxGarage web interface and asks for thorough testing before a canonical schema is committed. [[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^r4]] ^s4
- For complete and more or less static projects, the README recommends the most recent numbered schema release available as of publication because that file remains stable. It recommends the `latest` release at `https://www.stoa.org/epidoc/schema/latest/tei-epidoc.rng` for projects in active development whose editors are comfortable following changes through community fora and updating their XML if the schema changes. [[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^r5]] ^s5
- The README attributes copyright in the TEI Schema to the TEI Consortium and, insofar as they are customized transformative versions, in the EpiDoc ODD and schema to one named contributor and the other contributors listed in `tei:revisionDesc`, and refers to `LICENSE.txt` for the license. [[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^r2]] ^s6

## Terms

- **latest release**: the schema location the README says is updated whenever a new EpiDoc schema is released [[10_markdown/documents/practice-v1-epidoc-schema-readme-e5b68eb8#^r5]]

## Open questions

- Does the documented OxGarage path still describe how released EpiDoc schemas are produced?
- Do `https://www.stoa.org/epidoc/schema/latest/` and `https://epidoc.stoa.org/schema/latest/` serve the same file?

## Appraisal

The README establishes documented procedures and recommendations. Actual
project practice and the named tool's output require separate evidence. Rights
evidence for the acquisition is recorded in its manifest.

## Related

- [[30_assertions/practice-v1-sampled-schema-generation-paths-differ]]
- [[30_assertions/practice-v1-epidoc-latest-guidance-and-isicily-reference]]
