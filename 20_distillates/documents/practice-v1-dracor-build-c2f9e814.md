---
type: distillate
source-type: document
representation: "[[10_markdown/documents/practice-v1-dracor-build-c2f9e814]]"
topics: ["[[Interoperability and Processing]]", "[[ODD and Customization]]"]
status: grounded
checked: {}
created: 2026-09-11
updated: 2026-09-11
---

# Distillate: DraCor schema build script at c2f9e814

Three passages of the DraCor schema repository's `build` script show where its converters come from, a Java setting it exports, and the order in which it derives schemas from the ODD.

## Core statements

- The DraCor build script sets `BIN=./Stylesheets/bin` and runs `git submodule init` and `git submodule update` when that directory does not exist. [[10_markdown/documents/practice-v1-dracor-build-c2f9e814#^r1]] ^s1
- The build script exports `JAVA_TOOL_OPTIONS` with `jdk.xml.maxGeneralEntitySizeLimit` and `jdk.xml.totalEntitySizeLimit` set to 0, commenting that limits lowered in JDK 24/25 would make the ODD transformation fail with JAXP00010003 and JAXP00010004 errors. [[10_markdown/documents/practice-v1-dracor-build-c2f9e814#^r2]] ^s2
- The build script runs `teitoodd` on `dracor.odd` to write `dist/dracor.odd.tmp`, then `teitorng` and `teitoschematron` on that file to write `dist/dracor.rng` and `dist/dracor.sch`, and inserts the version into the RNG with `sed`. [[10_markdown/documents/practice-v1-dracor-build-c2f9e814#^r3]] ^s3

## Terms

No term definition is extracted from these passages.

## Open questions

- Which converter revision and Java version produce the intended schema outputs?
- Does the intermediate ODD differ when the Java entity limits are not raised?

## Appraisal

The statements describe the commands and comments in the script. This project
did not execute it, its converters or Java. Output files and error behaviour
require a recorded run.

Acquisition record: [practice admission](../../sources/manifests/2026-09-11-practice-v1-admission.yaml).

## Related

- [[30_assertions/practice-v1-sampled-schema-generation-paths-differ]]
