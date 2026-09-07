---
type: representation
source-type: document
source: '[[00_sources/tei-p5-interpgrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 interpGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/interpGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# interpGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4785. Git blob: `1d50d113a183f5c200236d56c8812878b8c60c46`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:xi="http://www.w3.org/2001/XInclude" module="analysis" xml:id="gi-interpGrp" ident="interpGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">interpretation group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">해석 집단</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">解釋群組</gloss>
  <gloss versionDate="2008-04-06" xml:lang="ja"/>
  <gloss versionDate="2007-06-12" xml:lang="fr">groupe d'interprétations</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de interpretación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di interpretazioni</gloss>
  <desc versionDate="2005-07-07" xml:lang="en">collects together a set of related interpretations which share responsibility or type.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">책임성 혹은 유형을 공유하고 있는, 관련된 해석들을 모아놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一系列具有共同任務或類型的相關解釋。</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">責任者や分類を共にする、関連し合う解釈をまとめる。</desc>
  <desc versionDate="2009-02-13" xml:lang="fr">regroupe un ensemble d'interprétations ayant en commun
    une mention de responsabilité ou un type.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">Agrupa un conjunto de interpretaciones relacionadas en
    base a la responsabilidad o al tipo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa un insieme di interpretazioni accomunate per
    responsabilità o tipo</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.interpLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="interp" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpGrp-egXML-bk">
      <interpGrp resp="#TMA" type="structuralunit">
        <desc>basic structural organization</desc>
        <interp xml:id="I1">introduction</interp>
        <interp xml:id="I2">conflict</interp>
        <interp xml:id="I3">climax</interp>
        <interp xml:id="I4">revenge</interp>
        <interp xml:id="I5">reconciliation</interp>
        <interp xml:id="I6">aftermath</interp>
      </interpGrp>
      <bibl xml:id="TMA">
        <!-- bibliographic citation for source of this
interpretive framework -->
      </bibl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpGrp-egXML-kg">
      <interpGrp resp="#fr_TMA" type="structuralunit">
        <desc>Organisation structurelle de base</desc>
        <interp xml:id="fr_I1">introduction</interp>
        <interp xml:id="fr_I2">conflit</interp>
        <interp xml:id="fr_I3">apogée</interp>
        <interp xml:id="fr_I4">vengeance</interp>
        <interp xml:id="fr_I5">reconciliation</interp>
        <interp xml:id="fr_I6">conséquence</interp>
      </interpGrp>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpGrp-egXML-rf">
      <interpGrp resp="#zh-tw_TMA" type="段落架構">
        <interp xml:id="zh-tw_註11">序</interp>
        <interp xml:id="zh-tw_註I2">衝突</interp>
        <interp xml:id="zh-tw_註I3">高潮</interp>
        <interp xml:id="zh-tw_註I4">復仇</interp>
        <interp xml:id="zh-tw_註I5">調和</interp>
        <interp xml:id="zh-tw_註I6">結局</interp>
      </interpGrp>
      <bibl xml:id="zh-tw_TMA">
        <!--  註明資料來源-->
      </bibl>
    </egXML>
  </exemplum>
  <remarks ident="interpGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Any number of <gi>interp</gi> elements.</p>
  </remarks>
  <remarks ident="interpGrp-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Un nombre quelconque d'éléments <gi>interp</gi>.</p>
  </remarks>
  <remarks ident="interpGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 任意数の要素<gi>interp</gi>。 </p>
  </remarks>
  <listRef>
    <ptr target="#AISP"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">interpretation group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">해석 집단</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">解釋群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="ja"/>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">groupe d'interprétations</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de interpretación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di interpretazioni</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-07-07" xml:lang="en">collects together a set of related interpretations which share responsibility or type.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">책임성 혹은 유형을 공유하고 있는, 관련된 해석들을 모아놓는다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一系列具有共同任務或類型的相關解釋。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">責任者や分類を共にする、関連し合う解釈をまとめる。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-02-13" xml:lang="fr">regroupe un ensemble d'interprétations ayant en commun
    une mention de responsabilité ou un type.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">Agrupa un conjunto de interpretaciones relacionadas en
    base a la responsabilidad o al tipo.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa un insieme di interpretazioni accomunate per
    responsabilità o tipo</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.interpLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="interp" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpGrp-egXML-bk">
      <interpGrp resp="#TMA" type="structuralunit">
        <desc>basic structural organization</desc>
        <interp xml:id="I1">introduction</interp>
        <interp xml:id="I2">conflict</interp>
        <interp xml:id="I3">climax</interp>
        <interp xml:id="I4">revenge</interp>
        <interp xml:id="I5">reconciliation</interp>
        <interp xml:id="I6">aftermath</interp>
      </interpGrp>
      <bibl xml:id="TMA">
        <!-- bibliographic citation for source of this
interpretive framework -->
      </bibl>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpGrp-egXML-kg">
      <interpGrp resp="#fr_TMA" type="structuralunit">
        <desc>Organisation structurelle de base</desc>
        <interp xml:id="fr_I1">introduction</interp>
        <interp xml:id="fr_I2">conflit</interp>
        <interp xml:id="fr_I3">apogée</interp>
        <interp xml:id="fr_I4">vengeance</interp>
        <interp xml:id="fr_I5">reconciliation</interp>
        <interp xml:id="fr_I6">conséquence</interp>
      </interpGrp>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpGrp-egXML-rf">
      <interpGrp resp="#zh-tw_TMA" type="段落架構">
        <interp xml:id="zh-tw_註11">序</interp>
        <interp xml:id="zh-tw_註I2">衝突</interp>
        <interp xml:id="zh-tw_註I3">高潮</interp>
        <interp xml:id="zh-tw_註I4">復仇</interp>
        <interp xml:id="zh-tw_註I5">調和</interp>
        <interp xml:id="zh-tw_註I6">結局</interp>
      </interpGrp>
      <bibl xml:id="zh-tw_TMA">
        <!--  註明資料來源-->
      </bibl>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="interpGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Any number of <gi>interp</gi> elements.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="interpGrp-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Un nombre quelconque d'éléments <gi>interp</gi>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="interpGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 任意数の要素<gi>interp</gi>。 </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AISP"/>
  </listRef>
```

^b23

