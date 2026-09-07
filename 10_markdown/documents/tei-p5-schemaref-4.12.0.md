---
type: representation
source-type: document
source: '[[00_sources/tei-p5-schemaref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 schemaRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/schemaRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# schemaRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1641. Git blob: `95a3c64a2d570144dbe26819a7b6905f6a44ab65`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="http://jenkins.tei-c.org/job/TEIP5/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="schemaRef" ident="schemaRef">
  <gloss versionDate="2016-11-24" xml:lang="en">schema reference</gloss>
  <desc versionDate="2016-11-24" xml:lang="en">describes or points to a related customization or schema file.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.resourced"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
 <content>
    <classRef key="model.descLike" minOccurs="0"/>
 </content>
  
  <attList>
    <attDef ident="key">
      <desc versionDate="2016-11-24" xml:lang="en">the identifier used for the customization or schema.</desc>
      <datatype><dataRef key="teidata.xmlName"/></datatype>
    </attDef>  
  </attList>
  
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="schemaRef-egXML-co" source="#UND">
      <schemaRef type="interchangeODD" url="http://www.tei-c.org/release/xml/tei/custom/odd/tei_lite.odd"/>
      <schemaRef type="interchangeRNG" url="http://www.tei-c.org/release/xml/tei/custom/odd/tei_lite.rng"/>
      <schemaRef type="projectODD" url="file:///schema/project.odd"/>
    </egXML>
  </exemplum>
  
  <listRef>
    <ptr target="#HDSCHSPEC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="en">schema reference</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-11-24" xml:lang="en">describes or points to a related customization or schema file.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.resourced"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.descLike" minOccurs="0"/>
 </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2016-11-24" xml:lang="en">the identifier used for the customization or schema.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="schemaRef-egXML-co" source="#UND">
      <schemaRef type="interchangeODD" url="http://www.tei-c.org/release/xml/tei/custom/odd/tei_lite.odd"/>
      <schemaRef type="interchangeRNG" url="http://www.tei-c.org/release/xml/tei/custom/odd/tei_lite.rng"/>
      <schemaRef type="projectODD" url="file:///schema/project.odd"/>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDSCHSPEC"/>
  </listRef>
```

^b8

