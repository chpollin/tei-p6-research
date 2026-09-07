---
type: representation
source-type: document
source: '[[00_sources/tei-p5-rdggrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 rdgGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/rdgGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# rdgGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5086. Git blob: `643f909c2646627115eff1d665d88275cae0ddc5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-rdgGrp" ident="rdgGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">reading group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">독법군</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">對應本群組</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">groupe de leçons</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de lecturas</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di letture</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">within a textual variation, groups two or more readings perceived to have a genetic relationship or other affinity.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형 내에서 계통 관계 또는 유사 관계로 이해되는 둘 이상의 독법을 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">原文變異中，匯集兩個或多個認為具有根源關係或於其他方面性質類似的對應本。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">異なるテキストで、系統関係や類縁性があるとされる、二つ以上の読みをま とめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe deux leçons ou plus qui sont perçues comme ayant une relation génétique ou une autre affinité.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa al interno de una variante textual dos o más lecturas consideradas emparentadas o afines.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">all'interno di una variante testuale raggruppa due o più letture considerate imparentate o affini.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.textCritical"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="lem" minOccurs="0"/>
    <alternate maxOccurs="unbounded" minOccurs="0">
      <classRef key="model.rdgLike"/>
      <classRef key="model.noteLike"/>
      <elementRef key="witDetail"/>
      <elementRef key="wit"/>      
      <elementRef key="rdgGrp"/>      
    </alternate>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="only1lem" xml:lang="en">
    <constraint xmlns:sch="http://purl.oclc.org/dsdl/schematron">
      <sch:rule context="tei:rdgGrp">
        <sch:assert test="count(tei:lem) lt 2">Only one &lt;lem&gt; element may appear within a &lt;rdgGrp&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdgGrp-egXML-tu">
      <app>
        <lem wit="#El #Ra2">though</lem>
        <rdgGrp type="orthographic">
          <rdg wit="#Hg">thogh</rdg>
          <rdg wit="#La">thouhe</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdgGrp-egXML-qz">
      <app>
        <lem wit="#fr_wit1">comte</lem>
        <rdgGrp type="orthographic">
          <rdg wit="#fr_wit2">cante</rdg>
          <rdg wit="#fr_wit3">contes</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdgGrp-egXML-ku">
      <app>
        <lem wit="#El #Ra2">壓</lem>
        <rdgGrp type="orthographic">
          <rdg wit="#Hg">壓</rdg>
          <rdg wit="#La">压</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
  <remarks ident="rdgGrp-remarks" versionDate="2019-07-03" xml:lang="en">
    <p rend="dataDesc">May contain readings and nested reading groups.</p>
    <p>Usually, only one <gi>lem</gi> element should appear within
       a single apparatus entry, whether it appears outside a <gi>rdgGrp</gi>
       element or within it.</p>
  </remarks>
  <remarks ident="rdgGrp-remarks" versionDate="2019-07-03" xml:lang="fr">
    <p rend="dataDesc">Contient des leçons et des groupes de leçons emboîtées.</p>
    <p>En général, un seul élément <gi>lem</gi> doit apparaître dans une seule entrée d'apparat,
       qu'il se trouve à l'intérieur ou à l'extérieur d'un élément <gi>rdgGrp</gi>.</p>
  </remarks>
  <remarks ident="rdgGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    読みまたは入れ子化された読みのグループをとるかもしれない。
    </p>
    <p>
    要素<gi>lem</gi>は、要素<gi>rdgGrp</gi>の内外にあるかどうかに関係
    なく、校勘資料のいち項目中では、ひとつしか現れないことに注意するこ
    と。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">reading group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">독법군</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">對應本群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">groupe de leçons</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de lecturas</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di letture</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">within a textual variation, groups two or more readings perceived to have a genetic relationship or other affinity.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형 내에서 계통 관계 또는 유사 관계로 이해되는 둘 이상의 독법을 모아 놓는다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">原文變異中，匯集兩個或多個認為具有根源關係或於其他方面性質類似的對應本。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">異なるテキストで、系統関係や類縁性があるとされる、二つ以上の読みをま とめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe deux leçons ou plus qui sont perçues comme ayant une relation génétique ou une autre affinité.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa al interno de una variante textual dos o más lecturas consideradas emparentadas o afines.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">all'interno di una variante testuale raggruppa due o più letture considerate imparentate o affini.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.textCritical"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="lem" minOccurs="0"/>
    <alternate maxOccurs="unbounded" minOccurs="0">
      <classRef key="model.rdgLike"/>
      <classRef key="model.noteLike"/>
      <elementRef key="witDetail"/>
      <elementRef key="wit"/>      
      <elementRef key="rdgGrp"/>      
    </alternate>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="only1lem" xml:lang="en">
    <constraint xmlns:sch="http://purl.oclc.org/dsdl/schematron">
      <sch:rule context="tei:rdgGrp">
        <sch:assert test="count(tei:lem) lt 2">Only one &lt;lem&gt; element may appear within a &lt;rdgGrp&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdgGrp-egXML-tu">
      <app>
        <lem wit="#El #Ra2">though</lem>
        <rdgGrp type="orthographic">
          <rdg wit="#Hg">thogh</rdg>
          <rdg wit="#La">thouhe</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdgGrp-egXML-qz">
      <app>
        <lem wit="#fr_wit1">comte</lem>
        <rdgGrp type="orthographic">
          <rdg wit="#fr_wit2">cante</rdg>
          <rdg wit="#fr_wit3">contes</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rdgGrp-egXML-ku">
      <app>
        <lem wit="#El #Ra2">壓</lem>
        <rdgGrp type="orthographic">
          <rdg wit="#Hg">壓</rdg>
          <rdg wit="#La">压</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="rdgGrp-remarks" versionDate="2019-07-03" xml:lang="en">
    <p rend="dataDesc">May contain readings and nested reading groups.</p>
    <p>Usually, only one <gi>lem</gi> element should appear within
       a single apparatus entry, whether it appears outside a <gi>rdgGrp</gi>
       element or within it.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="rdgGrp-remarks" versionDate="2019-07-03" xml:lang="fr">
    <p rend="dataDesc">Contient des leçons et des groupes de leçons emboîtées.</p>
    <p>En général, un seul élément <gi>lem</gi> doit apparaître dans une seule entrée d'apparat,
       qu'il se trouve à l'intérieur ou à l'extérieur d'un élément <gi>rdgGrp</gi>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="rdgGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    読みまたは入れ子化された読みのグループをとるかもしれない。
    </p>
    <p>
    要素<gi>lem</gi>は、要素<gi>rdgGrp</gi>の内外にあるかどうかに関係
    なく、校勘資料のいち項目中では、ひとつしか現れないことに注意するこ
    と。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b23

