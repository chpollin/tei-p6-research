---
type: representation
source-type: document
source: '[[00_sources/tei-p5-origdate-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 origDate
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/origDate.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# origDate

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3305. Git blob: `347c5d8c67afaa94bb9dfd7f5075ef1f8392541f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="ORIGDATE" ident="origDate">
  <gloss versionDate="2007-07-04" xml:lang="en">origin date</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">생성 날짜</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">fecha origen</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">date de la création</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">data di origine</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="origdate.desc">contains any form of date, used to identify the date of origin for a manuscript, manuscript part, or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 일부의 생산 날짜를 식별하는 날짜 형식을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何格式的日期，用以確認手稿或手稿部分的來源日期。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料が生まれた日付を特定するたための日付を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une date, dans une forme libre, utilisée pour dater la création d'un manuscrit ou d'une partie d'un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de fecha utilizada para indicar la fecha de origen de un manuscrito o de una de sus partes.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una data espressa in una forma qualsiasi utilizzata per indicare la data di origine di un manoscritto o di una sua parte.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.calendarSystem"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGDATE-egXML-zq">
      <origDate notBefore="-0300" notAfter="-0200">3rd century BCE</origDate>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGDATE-egXML-kx">
      <origDate notBefore="-0300" notAfter="-0200">3rd century BCE</origDate>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGDATE-egXML-tx">
      <origDate notBefore="-0300" notAfter="-0200">西元前三世紀</origDate>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msdates"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">origin date</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">생성 날짜</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">fecha origen</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">date de la création</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">data di origine</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="origdate.desc">contains any form of date, used to identify the date of origin for a manuscript, manuscript part, or other object.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 일부의 생산 날짜를 식별하는 날짜 형식을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何格式的日期，用以確認手稿或手稿部分的來源日期。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料が生まれた日付を特定するたための日付を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une date, dans une forme libre, utilisée pour dater la création d'un manuscrit ou d'une partie d'un manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de fecha utilizada para indicar la fecha de origen de un manuscrito o de una de sus partes.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una data espressa in una forma qualsiasi utilizzata per indicare la data di origine di un manoscritto o di una sua parte.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.calendarSystem"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGDATE-egXML-zq">
      <origDate notBefore="-0300" notAfter="-0200">3rd century BCE</origDate>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGDATE-egXML-kx">
      <origDate notBefore="-0300" notAfter="-0200">3rd century BCE</origDate>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGDATE-egXML-tx">
      <origDate notBefore="-0300" notAfter="-0200">西元前三世紀</origDate>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msdates"/>
  </listRef>
```

^b19

