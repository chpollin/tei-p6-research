---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.gender-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.gender
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.gender.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.gender

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1121. Git blob: `7793793374e74c3f1cdf03a82a4b2251ce47c87c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.gender">
  <desc versionDate="2022-05-17" xml:lang="en">defines the range of attribute values used to
    represent the gender of a person, persona, or character.</desc>
  <content>
    <dataRef key="teidata.enumerated"/>
  </content>
  <remarks ident="teidata.gender-remarks" versionDate="2022-08-27" xml:lang="en">
    <p>Values for attributes using this datatype may be defined locally by a project, or they may refer to an external standard.</p>
    <p>Values for this datatype should not be used to encode morphological gender (cf. <gi>gen</gi>,
        <att>msd</att> as defined in <ident type="class">att.linguistic</ident>, and <ptr target="#DITPFO"/>).</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2022-05-17" xml:lang="en">defines the range of attribute values used to
    represent the gender of a person, persona, or character.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <dataRef key="teidata.enumerated"/>
  </content>
```

^b2

### Block 3

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.gender-remarks" versionDate="2022-08-27" xml:lang="en">
    <p>Values for attributes using this datatype may be defined locally by a project, or they may refer to an external standard.</p>
    <p>Values for this datatype should not be used to encode morphological gender (cf. <gi>gen</gi>,
        <att>msd</att> as defined in <ident type="class">att.linguistic</ident>, and <ptr target="#DITPFO"/>).</p>
  </remarks>
```

^b3

