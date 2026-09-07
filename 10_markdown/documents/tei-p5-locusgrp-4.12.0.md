---
type: representation
source-type: document
source: '[[00_sources/tei-p5-locusgrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 locusGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/locusGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# locusGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2546. Git blob: `ba5b541308d738cc511e4884d1a02ce9c21bd1ad`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="gi-locusGrp" ident="locusGrp">
  <gloss versionDate="2020-12-20" xml:lang="en">locus group</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">groupe d'emplacements</gloss>
  <desc versionDate="2019-01-17" xml:lang="en">groups a number of locations which together form a
  distinct but discontinuous item within a manuscript, manuscript part, or other object.</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">regroupe un certain nombre d'emplacements qui forment ensemble un item identifiable bien que discontinu dans un manuscrit ou une partie de manuscrit selon une foliotation spécifique.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <elementRef key="locus" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <attList>
    <attDef ident="scheme">
      <gloss versionDate="2007-06-12" xml:lang="en">scheme</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">système</gloss>
      <desc versionDate="2009-01-24" xml:lang="en">identifies the foliation scheme in terms of which all the
      locations contained by the group are specified by pointing to some <gi>foliation</gi> element
        defining it, or to some other equivalent resource.</desc>
      <desc versionDate="2009-04-17" xml:lang="fr">désigne le système de foliotation selon lequel les emplacements contenus dans le groupe sont définis.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-locusGrp-egXML-gd" xml:lang="de">
      <msItem>
        <locusGrp>
          <locus from="13" to="26">Bl. 13--26</locus>
          <locus from="37" to="58">37--58</locus>
          <locus from="82" to="96">82--96</locus>
        </locusGrp>
        <note>Stücke von Daniel Ecklin’s Reise ins h. Land</note>
      </msItem>
    </egXML>
  </exemplum>
  <remarks ident="locusGrp-remarks" versionDate="2009-01-24" xml:lang="en">
    <p/>
  </remarks>
  <listRef>
    <ptr target="#msloc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">locus group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">groupe d'emplacements</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en">groups a number of locations which together form a
  distinct but discontinuous item within a manuscript, manuscript part, or other object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">regroupe un certain nombre d'emplacements qui forment ensemble un item identifiable bien que discontinu dans un manuscrit ou une partie de manuscrit selon une foliotation spécifique.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <elementRef key="locus" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">scheme</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">système</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2009-01-24" xml:lang="en">identifies the foliation scheme in terms of which all the
      locations contained by the group are specified by pointing to some <gi>foliation</gi> element
        defining it, or to some other equivalent resource.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">désigne le système de foliotation selon lequel les emplacements contenus dans le groupe sont définis.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-locusGrp-egXML-gd" xml:lang="de">
      <msItem>
        <locusGrp>
          <locus from="13" to="26">Bl. 13--26</locus>
          <locus from="37" to="58">37--58</locus>
          <locus from="82" to="96">82--96</locus>
        </locusGrp>
        <note>Stücke von Daniel Ecklin’s Reise ins h. Land</note>
      </msItem>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="locusGrp-remarks" versionDate="2009-01-24" xml:lang="en">
    <p/>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msloc"/>
  </listRef>
```

^b14

