---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sourcedesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sourceDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sourceDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sourceDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4671. Git blob: `3876cd04177b731c57f0c6077a015348038aa3da`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-sourceDesc" ident="sourceDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">source description</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">description de la source</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">원전 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción de la fuente</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione della fonte</gloss>
    <gloss versionDate="2016-11-17" xml:lang="de">Beschreibung der Quellen</gloss>
  <desc versionDate="2008-12-09" xml:lang="en">describes the source(s) from which an electronic text was derived or generated, typically a
    bibliographic description in the case of a digitized text, or a phrase such as <q>born digital</q>
    for a text which has no previous existence.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit la source à partir de laquelle un texte électronique a été
    dérivé ou produit, habituellement une description bibliographique pour un texte numérisé, ou une
    expression comme <q>document numérique natif</q> pour un texte qui n'a aucune existence précédente.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자 파일을 생성하거나 도출한 원전 텍스트에 대한 기술을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供所製電子文件的一個或數個來源文件的書目描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">電子テキストが作られた元テキストの情報を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">beschreibt die Quelle, von der sich der elektronische Text ableitet. 
        Üblicherweise eine bibliografische Beschreibung im Falle eines digitalisierten Textes oder eine Bezeichnung wie 
        <q>born digital</q> für einen nur in elektronischer Form vorliegenden Text.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona una descripción del texto (o textos) fuente
    del que un texto electrónico deriva o ha sido generado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it"> fornisce una descrizione relativa alla o alle fonti da
    cui è derivato o generato un documento elettronico.</desc>  
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.biblLike"/>
        <classRef key="model.sourceDescPart"/>
        <classRef key="model.listLike"/>
      </alternate>
    </alternate>
  </content>
  <constraintSpec ident="sourceDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:sourceDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-ea">
      <sourceDesc>
        <bibl><title level="a">The Interesting story of the Children in the Wood</title>. In
            <author>Victor E Neuberg</author>, <title>The Penny Histories</title>.
            <publisher>OUP</publisher><date>1968</date>. </bibl>
      </sourceDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-it">
      <sourceDesc>
        <p>Texte original : le texte a été créé sous sa forme électronique.</p>
      </sourceDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-vj">
      <sourceDesc>
        <p>無來源：以電腦可讀格式建立</p>
      </sourceDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-ie">
      <sourceDesc>
        <p>Born digital: no previous source exists.</p>
      </sourceDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">source description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">description de la source</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">원전 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">descripción de la fuente</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione della fonte</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Beschreibung der Quellen</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-12-09" xml:lang="en">describes the source(s) from which an electronic text was derived or generated, typically a
    bibliographic description in the case of a digitized text, or a phrase such as <q>born digital</q>
    for a text which has no previous existence.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit la source à partir de laquelle un texte électronique a été
    dérivé ou produit, habituellement une description bibliographique pour un texte numérisé, ou une
    expression comme <q>document numérique natif</q> pour un texte qui n'a aucune existence précédente.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자 파일을 생성하거나 도출한 원전 텍스트에 대한 기술을 제시한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供所製電子文件的一個或數個來源文件的書目描述。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">電子テキストが作られた元テキストの情報を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">beschreibt die Quelle, von der sich der elektronische Text ableitet. 
        Üblicherweise eine bibliografische Beschreibung im Falle eines digitalisierten Textes oder eine Bezeichnung wie 
        <q>born digital</q> für einen nur in elektronischer Form vorliegenden Text.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una descripción del texto (o textos) fuente
    del que un texto electrónico deriva o ha sido generado.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it"> fornisce una descrizione relativa alla o alle fonti da
    cui è derivato o generato un documento elettronico.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.biblLike"/>
        <classRef key="model.sourceDescPart"/>
        <classRef key="model.listLike"/>
      </alternate>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="sourceDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:sourceDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-ea">
      <sourceDesc>
        <bibl><title level="a">The Interesting story of the Children in the Wood</title>. In
            <author>Victor E Neuberg</author>, <title>The Penny Histories</title>.
            <publisher>OUP</publisher><date>1968</date>. </bibl>
      </sourceDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-it">
      <sourceDesc>
        <p>Texte original : le texte a été créé sous sa forme électronique.</p>
      </sourceDesc>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-vj">
      <sourceDesc>
        <p>無來源：以電腦可讀格式建立</p>
      </sourceDesc>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDesc-egXML-ie">
      <sourceDesc>
        <p>Born digital: no previous source exists.</p>
      </sourceDesc>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD3"/>
  </listRef>
```

^b23

