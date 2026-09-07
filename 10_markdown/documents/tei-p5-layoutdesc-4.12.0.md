---
type: representation
source-type: document
source: '[[00_sources/tei-p5-layoutdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 layoutDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/layoutDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# layoutDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4594. Git blob: `be6ea6cdb9ac4bc0ddf31bdbbdca2ccc1ba77695`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="LAYOUTDESC" ident="layoutDesc">
  <gloss versionDate="2007-11-18" xml:lang="en">layout description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">레이아웃 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción de la disposición</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description de la mise en page</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione dell'impaginazione</gloss>
  <desc versionDate="2019-01-17" xml:lang="en">collects the set of layout descriptions applicable to a manuscript or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고에 적용가능한 레이아웃 기술 집합을 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">收集一組適當的手稿外觀編排描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料のレイアウト情報をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">rassemble les descriptions des mises en page d' un
      manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa el conjunto de las descripciones de la distribución aplicable a un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa l'insieme delle descrizioni dell'impaginazione relative a un manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="layout" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-cv">
      <layoutDesc>
        <p>Most pages have between 25 and 32 long lines ruled in lead.</p>
      </layoutDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-nc">
      <layoutDesc>
        <p>Most pages have between 25 and 32 long lines ruled in lead.</p>
      </layoutDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-ym">
      <layoutDesc>
        <layout columns="2" ruledLines="42">
          <p><locus from="f12r" to="f15v"/> 2 columns of 42 lines pricked and ruled in ink, with
              central rule between the columns.</p>
        </layout>
        <layout columns="3">
          <p><locus from="f16"/>Prickings for three columns are visible.</p>
        </layout>
      </layoutDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-yo">
      <layoutDesc>
        <p>每頁14行，每行40到43字不等；有 註文小字雙行，字數不等。</p>
      </layoutDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-oe">
      <layoutDesc>
        <layout columns="2" ruledLines="42">
          <p><locus from="f12r" to="f15v"/>兩欄共42行以墨水圈選、標誌，欄間有直線分隔。</p>
        </layout>
        <layout columns="3">
          <p><locus from="f16"/>小孔的三欄可見.</p>
        </layout>        
      </layoutDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-nx">
      <layoutDesc>
        <layout columns="2" ruledLines="42">
          <p><locus from="f12r" to="f15v"/>
   2 columns of 42 lines pricked and ruled in ink, with 
   central rule between the columns.</p>
        </layout>
        <layout columns="3">
          <p><locus from="f16"/>Prickings for three columns are visible.</p>
        </layout>
      </layoutDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-11-18" xml:lang="en">layout description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">레이아웃 기술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">descripción de la disposición</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description de la mise en page</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione dell'impaginazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en">collects the set of layout descriptions applicable to a manuscript or other object.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고에 적용가능한 레이아웃 기술 집합을 모아 놓는다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">收集一組適當的手稿外觀編排描述。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料のレイアウト情報をまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">rassemble les descriptions des mises en page d' un
      manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa el conjunto de las descripciones de la distribución aplicable a un manuscrito.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa l'insieme delle descrizioni dell'impaginazione relative a un manoscritto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="layout" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-cv">
      <layoutDesc>
        <p>Most pages have between 25 and 32 long lines ruled in lead.</p>
      </layoutDesc>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-nc">
      <layoutDesc>
        <p>Most pages have between 25 and 32 long lines ruled in lead.</p>
      </layoutDesc>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-ym">
      <layoutDesc>
        <layout columns="2" ruledLines="42">
          <p><locus from="f12r" to="f15v"/> 2 columns of 42 lines pricked and ruled in ink, with
              central rule between the columns.</p>
        </layout>
        <layout columns="3">
          <p><locus from="f16"/>Prickings for three columns are visible.</p>
        </layout>
      </layoutDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-yo">
      <layoutDesc>
        <p>每頁14行，每行40到43字不等；有 註文小字雙行，字數不等。</p>
      </layoutDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-oe">
      <layoutDesc>
        <layout columns="2" ruledLines="42">
          <p><locus from="f12r" to="f15v"/>兩欄共42行以墨水圈選、標誌，欄間有直線分隔。</p>
        </layout>
        <layout columns="3">
          <p><locus from="f16"/>小孔的三欄可見.</p>
        </layout>        
      </layoutDesc>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUTDESC-egXML-nx">
      <layoutDesc>
        <layout columns="2" ruledLines="42">
          <p><locus from="f12r" to="f15v"/>
   2 columns of 42 lines pricked and ruled in ink, with 
   central rule between the columns.</p>
        </layout>
        <layout columns="3">
          <p><locus from="f16"/>Prickings for three columns are visible.</p>
        </layout>
      </layoutDesc>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph2"/>
  </listRef>
```

^b22

