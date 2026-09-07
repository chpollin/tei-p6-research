---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.scope-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.scope
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.scope.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.scope

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2329. Git blob: `82bdf4a7f2523017a0d65073321c1874b9633696`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" xml:id="class-attr-scope" ident="att.scope">
  <desc versionDate="2024-12-04" xml:lang="en">provides attributes to describe, in general terms, the scope of an element’s application.</desc>
  <attList>
    <attDef ident="scope" usage="opt">
      <desc versionDate="2024-12-04" xml:lang="en">indicates the scope of application of the element</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="sole">
          <desc versionDate="2024-12-04" xml:lang="en">only this particular feature is used throughout the document</desc>
        </valItem>
        <valItem ident="major">
          <desc versionDate="2024-12-04" xml:lang="en">this feature is used through most of the document</desc>
        </valItem>
        <valItem ident="minor">
          <desc versionDate="2024-12-04" xml:lang="en">this feature is used occasionally through the document</desc>
        </valItem>
      </valList>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scope-egXML-ls">
          <langUsage>
            <language ident="en" scope="major"/>
            <language ident="es" scope="minor"/>
            <language ident="x-ww" scope="minor">An invented language the children call <name>Wikwah</name>.</language>
          </langUsage>
        </egXML>
      </exemplum>
      <exemplum xml:lang="en">
        <!-- This example used to be "HANDNOTE-egXML-ey" -->
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scope-egXML-ey">
          <handNote scope="sole">
            <p>Written in insular phase II half-uncial with
            interlinear Old English gloss in an Anglo-Saxon
            pointed minuscule.</p>
          </handNote>
        </egXML>
      </exemplum>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2024-12-04" xml:lang="en">provides attributes to describe, in general terms, the scope of an element’s application.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2024-12-04" xml:lang="en">indicates the scope of application of the element</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="sole">
          <desc versionDate="2024-12-04" xml:lang="en">only this particular feature is used throughout the document</desc>
        </valItem>
        <valItem ident="major">
          <desc versionDate="2024-12-04" xml:lang="en">this feature is used through most of the document</desc>
        </valItem>
        <valItem ident="minor">
          <desc versionDate="2024-12-04" xml:lang="en">this feature is used occasionally through the document</desc>
        </valItem>
      </valList>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scope-egXML-ls">
          <langUsage>
            <language ident="en" scope="major"/>
            <language ident="es" scope="minor"/>
            <language ident="x-ww" scope="minor">An invented language the children call <name>Wikwah</name>.</language>
          </langUsage>
        </egXML>
      </exemplum>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
        <!-- This example used to be "HANDNOTE-egXML-ey" -->
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scope-egXML-ey">
          <handNote scope="sole">
            <p>Written in insular phase II half-uncial with
            interlinear Old English gloss in an Anglo-Saxon
            pointed minuscule.</p>
          </handNote>
        </egXML>
      </exemplum>
```

^b6

