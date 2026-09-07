---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.authority-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.authority
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.authority.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.authority

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1224. Git blob: `ee0be915d5d264408e7a1add5930bfea8561f822`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.authority">
  <desc versionDate="2020-02-12" xml:lang="en">defines attribute values which derive from an 
    authority list, which may be an enumerated list defined in the document's schema, a list 
    or taxonomy elsewhere in the document, or an online taxonomy, gazetteer, or other authority.</desc>
  <content>
    <alternate>
      <dataRef key="teidata.enumerated"/>
      <dataRef key="teidata.pointer"/>
    </alternate>
  </content>
  <remarks ident="teidata.authority-remarks" versionDate="2020-02-12" xml:lang="en">
    <p>Attribute values with this datatype should either come from a value list in the attribute
      specification (<ident type="datatype">teidata.enumerated</ident>) or be a valid URI (<ident type="datatype">teidata.pointer</ident>).</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-02-12" xml:lang="en">defines attribute values which derive from an 
    authority list, which may be an enumerated list defined in the document's schema, a list 
    or taxonomy elsewhere in the document, or an online taxonomy, gazetteer, or other authority.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <dataRef key="teidata.enumerated"/>
      <dataRef key="teidata.pointer"/>
    </alternate>
  </content>
```

^b2

### Block 3

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.authority-remarks" versionDate="2020-02-12" xml:lang="en">
    <p>Attribute values with this datatype should either come from a value list in the attribute
      specification (<ident type="datatype">teidata.enumerated</ident>) or be a valid URI (<ident type="datatype">teidata.pointer</ident>).</p>
  </remarks>
```

^b3

