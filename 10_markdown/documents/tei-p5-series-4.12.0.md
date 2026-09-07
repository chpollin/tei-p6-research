---
type: representation
source-type: document
source: '[[00_sources/tei-p5-series-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 series
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/series.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# series

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3184. Git blob: `53b9d808839f762305b340ec6be505645422e43c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-series" ident="series">
  <gloss versionDate="2005-01-14" xml:lang="en">series information</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">연간물 정보</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">叢書資訊</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">informations sur la série</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">series de información</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">informazioni sulla collana</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains information about the series in which a book or other bibliographic item has
    appeared.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">책 또는 다른 참고문헌 항목이 나타나는 연간물 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含某書目項目所屬的叢書資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">書籍または他の書誌項目のシリーズに関する情報を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une information sur la série dans laquelle une
    monographie ou un autre élément bibliographique ont paru.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene información sobre las series en que un libro u
    otro elemento bibliográfico ha aparecido.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene indicazioni sulla collana in cui un libro o
    un'altra unità bibliografica sono stati pubblicati.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <elementRef key="title"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="editor"/>
        <elementRef key="respStmt"/>
        <elementRef key="biblScope"/>
        <elementRef key="idno"/>
        <elementRef key="textLang"/>
        <classRef key="model.global"/>
        <elementRef key="availability"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-series-egXML-tk">
      <series xml:lang="de">
        <title level="s">Halbgraue Reihe zur Historischen Fachinformatik</title>
        <respStmt>
          <resp>Herausgegeben von</resp>
          <name type="person">Manfred Thaller</name>
          <name type="org">Max-Planck-Institut für Geschichte</name>
        </respStmt>
        <title level="s">Serie A: Historische Quellenkunden</title>
        <biblScope>Band 11</biblScope>
      </series>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COBICOL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">series information</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">연간물 정보</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">叢書資訊</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">informations sur la série</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">series de información</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">informazioni sulla collana</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains information about the series in which a book or other bibliographic item has
    appeared.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">책 또는 다른 참고문헌 항목이 나타나는 연간물 정보를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含某書目項目所屬的叢書資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">書籍または他の書誌項目のシリーズに関する情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une information sur la série dans laquelle une
    monographie ou un autre élément bibliographique ont paru.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene información sobre las series en que un libro u
    otro elemento bibliográfico ha aparecido.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene indicazioni sulla collana in cui un libro o
    un'altra unità bibliografica sono stati pubblicati.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
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
        <elementRef key="title"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="editor"/>
        <elementRef key="respStmt"/>
        <elementRef key="biblScope"/>
        <elementRef key="idno"/>
        <elementRef key="textLang"/>
        <classRef key="model.global"/>
        <elementRef key="availability"/>
      </alternate>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-series-egXML-tk">
      <series xml:lang="de">
        <title level="s">Halbgraue Reihe zur Historischen Fachinformatik</title>
        <respStmt>
          <resp>Herausgegeben von</resp>
          <name type="person">Manfred Thaller</name>
          <name type="org">Max-Planck-Institut für Geschichte</name>
        </respStmt>
        <title level="s">Serie A: Historische Quellenkunden</title>
        <biblScope>Band 11</biblScope>
      </series>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOL"/>
  </listRef>
```

^b17

