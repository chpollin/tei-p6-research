---
type: representation
source-type: document
source: '[[00_sources/tei-p5-facsimile-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 facsimile
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/facsimile.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# facsimile

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3974. Git blob: `dd315b946bde9fbc24e20d50caa0a74a26237b0a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="facsimile" xml:id="gi-facsimile" module="transcr">
  <desc versionDate="2007-08-26" xml:lang="en">contains a representation of some written source in the form of a set of images rather than as transcribed or encoded text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전사 또는 부호화된 텍스트 형태보다는 이미지 집합의 형태로 기록 원본의 표상을 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una representación de una cierta fuente escrita bajo la forma de conjunto de las imágenes algo que como texto transcrito o codificado.</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">転記または符号化されたテキストではなく、画像データ中にある、書記資料の 表現を示す。</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">contient une représentation d'une source écrite quelconque sous la forme d'un ensemble d'images plutôt que sous la forme d'un texte transcrit ou encodé.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una rappresentazione di una qualche fonte scritta sotto forma di una serie di immagini piuttosto che di testo trascritto o codificato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="model.resource"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="front" minOccurs="0"/>
      <alternate>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.graphicLike"/>
          <elementRef key="surface"/>
          <elementRef key="surfaceGrp"/>
        </alternate>
        <elementRef key="facsimile" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
      <elementRef key="back" minOccurs="0"/>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="no_facsimile_text_nodes" xml:lang="en">
    <constraint>
      <sch:rule context="tei:facsimile//tei:line | tei:facsimile//tei:zone">
        <sch:report test="child::text()[ normalize-space(.) ne '']">
          A &lt;facsimile> element represents a text with images, thus
          transcribed text should not be present within it.
        </sch:report>
      </sch:rule>
    </constraint>
    <!-- 
         What about:
         * ellipses/supplied/text()
         * writing
         * label, formula, app, witDetail, metamark?
         * notatedMusic?
         * figure/[all-sorts-of-crazy-stuff-e.g.-entry]
         * addSpan, damageSpan, delSpan
         Or the fact that <front> and <back> (but not <body>) are
         permitted inside <facsimile>, and thus *anything* can be
         inside ther?
         See https://github.com/TEIC/TEI/issues/2363
    -->
  </constraintSpec>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-facsimile-egXML-bn" source="#UND">
      <facsimile>
        <graphic url="page1.png"/>
        <surface>
          <graphic url="page2-highRes.png"/>
          <graphic url="page2-lowRes.png"/>
        </surface>
        <graphic url="page3.png"/>
        <graphic url="page4.png"/>
      </facsimile>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-facsimile-egXML-cf" source="#UND">
      <facsimile>
        <surface ulx="0" uly="0" lrx="200" lry="300">
          <graphic url="Bovelles-49r.png"/>
        </surface>
      </facsimile>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHFAX"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-08-26" xml:lang="en">contains a representation of some written source in the form of a set of images rather than as transcribed or encoded text.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전사 또는 부호화된 텍스트 형태보다는 이미지 집합의 형태로 기록 원본의 표상을 포함한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una representación de una cierta fuente escrita bajo la forma de conjunto de las imágenes algo que como texto transcrito o codificado.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">転記または符号化されたテキストではなく、画像データ中にある、書記資料の 表現を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">contient une représentation d'une source écrite quelconque sous la forme d'un ensemble d'images plutôt que sous la forme d'un texte transcrit ou encodé.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una rappresentazione di una qualche fonte scritta sotto forma di una serie di immagini piuttosto che di testo trascritto o codificato.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="model.resource"/>
  </classes>
```

^b7

### Block 8

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="front" minOccurs="0"/>
      <alternate>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.graphicLike"/>
          <elementRef key="surface"/>
          <elementRef key="surfaceGrp"/>
        </alternate>
        <elementRef key="facsimile" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
      <elementRef key="back" minOccurs="0"/>
    </sequence>
  </content>
```

^b8

### Block 9

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="no_facsimile_text_nodes" xml:lang="en">
    <constraint>
      <sch:rule context="tei:facsimile//tei:line | tei:facsimile//tei:zone">
        <sch:report test="child::text()[ normalize-space(.) ne '']">
          A &lt;facsimile> element represents a text with images, thus
          transcribed text should not be present within it.
        </sch:report>
      </sch:rule>
    </constraint>
    <!-- 
         What about:
         * ellipses/supplied/text()
         * writing
         * label, formula, app, witDetail, metamark?
         * notatedMusic?
         * figure/[all-sorts-of-crazy-stuff-e.g.-entry]
         * addSpan, damageSpan, delSpan
         Or the fact that <front> and <back> (but not <body>) are
         permitted inside <facsimile>, and thus *anything* can be
         inside ther?
         See https://github.com/TEIC/TEI/issues/2363
    -->
  </constraintSpec>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-facsimile-egXML-bn" source="#UND">
      <facsimile>
        <graphic url="page1.png"/>
        <surface>
          <graphic url="page2-highRes.png"/>
          <graphic url="page2-lowRes.png"/>
        </surface>
        <graphic url="page3.png"/>
        <graphic url="page4.png"/>
      </facsimile>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-facsimile-egXML-cf" source="#UND">
      <facsimile>
        <surface ulx="0" uly="0" lrx="200" lry="300">
          <graphic url="Bovelles-49r.png"/>
        </surface>
      </facsimile>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHFAX"/>
  </listRef>
```

^b12

