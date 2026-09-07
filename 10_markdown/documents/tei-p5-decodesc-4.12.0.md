---
type: representation
source-type: document
source: '[[00_sources/tei-p5-decodesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 decoDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/decoDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# decoDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4290. Git blob: `f58f0d84297b6bf2f267b18c4c440effff267fe8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="DECODESC" ident="decoDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">decoration description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">장식 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción de la decoración</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description de la décoration</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione della decorazione</gloss>
  <gloss versionDate="2024-08-12" xml:lang="ja">装飾の記述</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="decoDesc.desc">contains a description of the decoration of a manuscript or other object, either as in paragraphs, or as one or more <gi>decoNote</gi> elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일련의 문단 또는 주제별로 조직된 일련의 <gi>decoNote</gi> 요소로 원고의 장식 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿的裝飾描述，可以是連續性的文字段落、或是一連串依主題排列的<gi>裝飾附註</gi>元素。</desc>
  <desc versionDate="2024-08-12" xml:lang="ja">当該手書き資料の装飾を、一連の散文段落、または、トピックごとにまとめた、一連の<gi>decoNote</gi>要素で示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description de la décoration du
      manuscrit, soit en une série de paragraphes <term>p</term>, soit sous la forme d'une série
      d'éléments thématiques <gi>decoNote</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de la decoración de un manuscrito en forma de secuencia de párrafos o de secuencia de elementos <gi>decoNote</gi> organizados por el argumento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione della decorazione di un manoscritto in forma di sequenza di paragrafi oppure di sequenza di elementi <gi>decoNote</gi> organizzati per argomento.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="decoNote" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECODESC-egXML-ki">
      <decoDesc>
        <p>The start of each book of the Bible with a 10-line historiated
illuminated initial; prefaces decorated with 6-line blue initials with red
penwork flourishing; chapters marked by 3-line plain red initials; verses
with 1-line initials, alternately blue or red.</p>
      </decoDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECODESC-egXML-ye" source="#fr-ex-manus-Saint-Petersbourg">
      <decoDesc>
        <p>Les miracles de la Vierge, par Gautier de Coinci ; un volume in-fol. de 285 feuilles,
            orné d'initiales en or et en couleur,...</p>
      </decoDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECODESC-egXML-dj">
      <decoDesc>
        <p>每本聖經的第一個字母都是十行大小，飾以歷史圖案；引言部份的第一個字母是六行大小，並以紅筆花飾；章節的第一個字母是三行大小，紅的；韻文的第一個字母一行大小，有時是紅色有時是藍色的。</p>
      </decoDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">decoration description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">장식 기술</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">descripción de la decoración</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description de la décoration</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione della decorazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-08-12" xml:lang="ja">装飾の記述</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="decoDesc.desc">contains a description of the decoration of a manuscript or other object, either as in paragraphs, or as one or more <gi>decoNote</gi> elements.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일련의 문단 또는 주제별로 조직된 일련의 <gi>decoNote</gi> 요소로 원고의 장식 기술을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿的裝飾描述，可以是連續性的文字段落、或是一連串依主題排列的<gi>裝飾附註</gi>元素。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-12" xml:lang="ja">当該手書き資料の装飾を、一連の散文段落、または、トピックごとにまとめた、一連の<gi>decoNote</gi>要素で示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description de la décoration du
      manuscrit, soit en une série de paragraphes <term>p</term>, soit sous la forme d'une série
      d'éléments thématiques <gi>decoNote</gi>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de la decoración de un manuscrito en forma de secuencia de párrafos o de secuencia de elementos <gi>decoNote</gi> organizados por el argumento.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione della decorazione di un manoscritto in forma di sequenza di paragrafi oppure di sequenza di elementi <gi>decoNote</gi> organizzati per argomento.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="decoNote" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECODESC-egXML-ki">
      <decoDesc>
        <p>The start of each book of the Bible with a 10-line historiated
illuminated initial; prefaces decorated with 6-line blue initials with red
penwork flourishing; chapters marked by 3-line plain red initials; verses
with 1-line initials, alternately blue or red.</p>
      </decoDesc>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECODESC-egXML-ye" source="#fr-ex-manus-Saint-Petersbourg">
      <decoDesc>
        <p>Les miracles de la Vierge, par Gautier de Coinci ; un volume in-fol. de 285 feuilles,
            orné d'initiales en or et en couleur,...</p>
      </decoDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECODESC-egXML-dj">
      <decoDesc>
        <p>每本聖經的第一個字母都是十行大小，飾以歷史圖案；引言部份的第一個字母是六行大小，並以紅筆花飾；章節的第一個字母是三行大小，紅的；韻文的第一個字母一行大小，有時是紅色有時是藍色的。</p>
      </decoDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph3"/>
  </listRef>
```

^b20

