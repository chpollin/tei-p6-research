---
type: representation
source-type: document
source: '[[00_sources/tei-p5-citedata-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 citeData
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/citeData.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# citeData

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1536. Git blob: `b0843b3bf386dff95e6bdab2049086aed1ab0bcf`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-citeData" ident="citeData">
  <gloss versionDate="2020-02-03" xml:lang="en">citation data</gloss>
  <desc versionDate="2020-02-03" xml:lang="en">specifies how information may be extracted from citation structures.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citeStructurePart"/>
  </classes>
  <content>
    <empty/>        
  </content>
  <attList>
    <attDef ident="property" usage="req">
      <gloss versionDate="2020-02-03" xml:lang="en">property</gloss>
      <desc versionDate="2020-02-03" xml:lang="en">A URI indicating a property definition.</desc>
      <datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
    </attDef>    
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citeData-egXML-wd" source="#NONE">
      <citeStructure unit="book" match="//body/div" use="@n">
        <citeData property="http://purl.org/dc/terms/title" use="head"/>
      </citeStructure>
    </egXML>
  </exemplum>  
  <listRef>
    <ptr target="#CORS6"/>
    <ptr target="#SACRCS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-02-03" xml:lang="en">citation data</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-02-03" xml:lang="en">specifies how information may be extracted from citation structures.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citeStructurePart"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <empty/>        
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2020-02-03" xml:lang="en">property</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2020-02-03" xml:lang="en">A URI indicating a property definition.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citeData-egXML-wd" source="#NONE">
      <citeStructure unit="book" match="//body/div" use="@n">
        <citeData property="http://purl.org/dc/terms/title" use="head"/>
      </citeStructure>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS6"/>
    <ptr target="#SACRCS"/>
  </listRef>
```

^b9

