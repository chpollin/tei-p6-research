---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sealdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sealDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sealDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sealDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3837. Git blob: `fdc32fa21a1eb1470ffa567055746db6f763eaf0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="SEALDESC" ident="sealDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">seal description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">봉인 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción del sello</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description des sceaux</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione dei sigilli</gloss>
  <desc versionDate="2018-07-17" xml:lang="en">describes the seals or similar items related to the object described, either as a series of paragraphs or as a series of <gi>seal</gi> elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"> 일련의 문단 혹은 또는 일련의 <gi>seal</gi> 요소(부가적인 <gi>decoNote</gi> 요소와 함께)로 원고에 부착된 봉인 또는 기타 외부 항목을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述章印或其他附於手稿的外部項目，可以是連續性的文字段落、或是一連串專用的<gi>印章</gi>元素，也許附上一些<gi>裝飾附註</gi>元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料に付属するシールや他の付着物について、一連の段落や、一連の
  要素<gi>seal</gi>により、可能であれば要素<gi>decoNote</gi>と共に示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit les sceaux ou autres objets attachés au
      manuscrit, soit en une série de paragraphes <gi>p</gi>, soit sous la forme d'une série
      d'éléments <gi>seal</gi>, complétés éventuellement par des éléments <gi>decoNote</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe los sellos u otros objetos externos aplicados a un manuscrito mediante una serie de párrafos o una serie de diversos elementos <gi>seal</gi> (sellos), eventualmente con ulteriores elementos <gi>decoNote</gi>.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive i sigilli o altri oggetti esterni applicati a un manoscritto sotto forma di una sequenza di paragrafi o una serie di diversi elementi <gi>seal</gi>, 
eventualmente con ulteriori elementi <gi>decoNote</gi></desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <alternate minOccurs="1" maxOccurs="unbounded">
            <elementRef key="decoNote"/>
            <elementRef key="seal"/>
            <elementRef key="condition"/>
          </alternate>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEALDESC-egXML-gg">
      <sealDesc>
        <seal type="pendant" contemporary="true">
          <p>Green wax vertical oval seal attached at base.</p>
        </seal>
      </sealDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEALDESC-egXML-ek">
      <sealDesc>
        <p>Parchment strip for seal in place; seal missing.</p>
      </sealDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msphse"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">seal description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">봉인 기술</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">descripción del sello</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description des sceaux</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione dei sigilli</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-07-17" xml:lang="en">describes the seals or similar items related to the object described, either as a series of paragraphs or as a series of <gi>seal</gi> elements.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"> 일련의 문단 혹은 또는 일련의 <gi>seal</gi> 요소(부가적인 <gi>decoNote</gi> 요소와 함께)로 원고에 부착된 봉인 또는 기타 외부 항목을 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述章印或其他附於手稿的外部項目，可以是連續性的文字段落、或是一連串專用的<gi>印章</gi>元素，也許附上一些<gi>裝飾附註</gi>元素。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料に付属するシールや他の付着物について、一連の段落や、一連の
  要素<gi>seal</gi>により、可能であれば要素<gi>decoNote</gi>と共に示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit les sceaux ou autres objets attachés au
      manuscrit, soit en une série de paragraphes <gi>p</gi>, soit sous la forme d'une série
      d'éléments <gi>seal</gi>, complétés éventuellement par des éléments <gi>decoNote</gi>.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe los sellos u otros objetos externos aplicados a un manuscrito mediante una serie de párrafos o una serie de diversos elementos <gi>seal</gi> (sellos), eventualmente con ulteriores elementos <gi>decoNote</gi>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive i sigilli o altri oggetti esterni applicati a un manoscritto sotto forma di una sequenza di paragrafi o una serie di diversi elementi <gi>seal</gi>, 
eventualmente con ulteriori elementi <gi>decoNote</gi></desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
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
        
        
          <alternate minOccurs="1" maxOccurs="unbounded">
            <elementRef key="decoNote"/>
            <elementRef key="seal"/>
            <elementRef key="condition"/>
          </alternate>
        
      </sequence>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEALDESC-egXML-gg">
      <sealDesc>
        <seal type="pendant" contemporary="true">
          <p>Green wax vertical oval seal attached at base.</p>
        </seal>
      </sealDesc>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEALDESC-egXML-ek">
      <sealDesc>
        <p>Parchment strip for seal in place; seal missing.</p>
      </sealDesc>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msphse"/>
  </listRef>
```

^b18

