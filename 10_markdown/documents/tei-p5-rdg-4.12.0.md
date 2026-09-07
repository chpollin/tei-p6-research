---
type: representation
source-type: document
source: '[[00_sources/tei-p5-rdg-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 rdg
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/rdg.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# rdg

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3706. Git blob: `d7bd65dd7572f6ffee89a888a47407f8f9da0524`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-rdg" ident="rdg">
  <gloss versionDate="2005-01-14" xml:lang="en">reading</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">독법</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">對應本</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">leçon</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">lectura</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">lettura</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a single reading within a textual variation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형 내에서 단일 독법을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含原文變異中的一個對應本。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">異なるテキスト中で、ひとつの読みを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une leçon à l'intérieur d'une variante
                        du texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una única lectura dentro de una variante textual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un'unica lettura entro una variante testuale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.textCritical"/>
    <memberOf key="att.witnessed"/>
    <memberOf key="model.rdgLike"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.divLike"/>
      <classRef key="model.divPart"/>
      <elementRef key="titlePage"/>
      <!-- WINITA: begin 454 hack section -->
      <!--
          model.titlepagePart sans <binaryObject> and <graphic>, i.e.
          change to <classRef key="model.titlepagePart" except="binaryObject graphic"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="argument"/>
      <elementRef key="byline"/>
      <elementRef key="docAuthor"/>
      <elementRef key="docDate"/>
      <elementRef key="docEdition"/>
      <elementRef key="docImprint"/>
      <elementRef key="docTitle"/>
      <elementRef key="epigraph"/>
      <elementRef key="imprimatur"/>
      <elementRef key="titlePart"/>
      <!--
          model.frontPart.drama sans <castList>, i.e.
          change to <classRef key="model.frontPart.drama" except="castList"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="epilogue"/>
      <elementRef key="performance"/>
      <elementRef key="prologue"/>
      <elementRef key="set"/>
      <!-- WINITA: end 454 hack section -->
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.inter"/>
      <classRef key="model.global"/>
      <classRef key="model.rdgPart"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdg-egXML-vd">
      <rdg wit="#Ra2">Eryment</rdg>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdg-egXML-rx">
      <rdg wit="#fr_wit1">cuens</rdg>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">reading</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">독법</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">對應本</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">leçon</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">lectura</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">lettura</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a single reading within a textual variation.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형 내에서 단일 독법을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含原文變異中的一個對應本。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">異なるテキスト中で、ひとつの読みを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une leçon à l'intérieur d'une variante
                        du texte.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una única lectura dentro de una variante textual.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un'unica lettura entro una variante testuale.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.textCritical"/>
    <memberOf key="att.witnessed"/>
    <memberOf key="model.rdgLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.divLike"/>
      <classRef key="model.divPart"/>
      <elementRef key="titlePage"/>
      <!-- WINITA: begin 454 hack section -->
      <!--
          model.titlepagePart sans <binaryObject> and <graphic>, i.e.
          change to <classRef key="model.titlepagePart" except="binaryObject graphic"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="argument"/>
      <elementRef key="byline"/>
      <elementRef key="docAuthor"/>
      <elementRef key="docDate"/>
      <elementRef key="docEdition"/>
      <elementRef key="docImprint"/>
      <elementRef key="docTitle"/>
      <elementRef key="epigraph"/>
      <elementRef key="imprimatur"/>
      <elementRef key="titlePart"/>
      <!--
          model.frontPart.drama sans <castList>, i.e.
          change to <classRef key="model.frontPart.drama" except="castList"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="epilogue"/>
      <elementRef key="performance"/>
      <elementRef key="prologue"/>
      <elementRef key="set"/>
      <!-- WINITA: end 454 hack section -->
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.inter"/>
      <classRef key="model.global"/>
      <classRef key="model.rdgPart"/>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdg-egXML-vd">
      <rdg wit="#Ra2">Eryment</rdg>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdg-egXML-rx">
      <rdg wit="#fr_wit1">cuens</rdg>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b18

