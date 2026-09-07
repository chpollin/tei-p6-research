---
type: representation
source-type: document
source: '[[00_sources/tei-p5-seriesstmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 seriesStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/seriesStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# seriesStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4579. Git blob: `ce5a71eb25fd72e16ec87bf8c11f334ad43b61c7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-seriesStmt" ident="seriesStmt">
  <gloss versionDate="2005-01-14" xml:lang="en">series statement</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">mention de collection</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">연속간행물 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">集叢陳述</gloss>
    <gloss versionDate="2016-11-17" xml:lang="de">Angaben zu einer Publikationsreihe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de serie</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulla serie</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups information about the series, if any, to which a publication belongs.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">regroupe toute information relative à la collection (si
    elle existe) à laquelle appartient une publication.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">연속 간행물에 대한 정보를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">若出版品隸屬於某叢書，則在此匯集該叢書的相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">出版されたシリーズの情報をまとめる。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">umfasst Angaben zu einer Publikationsreihe, zu der eine Veröffentlichung gehört.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa información sobre la serie, si la hay, a la que
    pertenece una publicación.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni circa la serie alla quale
    eventualmente la pubblicazione appartiene.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <sequence>
        <elementRef key="title" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="editor"/>
          <elementRef key="respStmt"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="idno"/>
          <elementRef key="biblScope"/>
        </alternate>
      </sequence>
    </alternate>
  </content>
  <constraintSpec ident="seriesStmt-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:seriesStmt"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seriesStmt-egXML-ju">
      <seriesStmt>
        <title>Machine-Readable Texts for the Study of Indian Literature</title>
        <respStmt>
          <resp>ed. by</resp>
          <name>Jan Gonda</name>
        </respStmt>
        <biblScope unit="volume">1.2</biblScope>
        <idno type="ISSN">0 345 6789</idno>
      </seriesStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seriesStmt-egXML-rx" source="#fr-ex-Babel">
      <seriesStmt>
        <title>Babel</title>
        <respStmt>
          <resp>directeur de collection</resp>
          <name>Jacques Dubois</name>
        </respStmt>
        <respStmt>
          <resp>directeur de collection</resp>
          <name>Hubert Nyssen</name>
        </respStmt>
        <idno type="ISSN">1140-3853</idno>
      </seriesStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seriesStmt-egXML-ry">
      <seriesStmt>
        <title>《印度文學研究》的電腦可讀文件</title>
        <respStmt>
          <resp>編者</resp>
          <name>珍．崗妲</name>
        </respStmt>
        <idno type="ISSN">0 345 6789</idno>
        <biblScope unit="volume">1.2</biblScope>
      </seriesStmt>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD26"/>
    <ptr target="#HD2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">series statement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">mention de collection</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">연속간행물 진술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">集叢陳述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angaben zu einer Publikationsreihe</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de serie</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulla serie</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups information about the series, if any, to which a publication belongs.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">regroupe toute information relative à la collection (si
    elle existe) à laquelle appartient une publication.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">연속 간행물에 대한 정보를 모아 놓는다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">若出版品隸屬於某叢書，則在此匯集該叢書的相關資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">出版されたシリーズの情報をまとめる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">umfasst Angaben zu einer Publikationsreihe, zu der eine Veröffentlichung gehört.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa información sobre la serie, si la hay, a la que
    pertenece una publicación.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni circa la serie alla quale
    eventualmente la pubblicazione appartiene.</desc>
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
      <sequence>
        <elementRef key="title" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="editor"/>
          <elementRef key="respStmt"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="idno"/>
          <elementRef key="biblScope"/>
        </alternate>
      </sequence>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="seriesStmt-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:seriesStmt"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seriesStmt-egXML-ju">
      <seriesStmt>
        <title>Machine-Readable Texts for the Study of Indian Literature</title>
        <respStmt>
          <resp>ed. by</resp>
          <name>Jan Gonda</name>
        </respStmt>
        <biblScope unit="volume">1.2</biblScope>
        <idno type="ISSN">0 345 6789</idno>
      </seriesStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seriesStmt-egXML-rx" source="#fr-ex-Babel">
      <seriesStmt>
        <title>Babel</title>
        <respStmt>
          <resp>directeur de collection</resp>
          <name>Jacques Dubois</name>
        </respStmt>
        <respStmt>
          <resp>directeur de collection</resp>
          <name>Hubert Nyssen</name>
        </respStmt>
        <idno type="ISSN">1140-3853</idno>
      </seriesStmt>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seriesStmt-egXML-ry">
      <seriesStmt>
        <title>《印度文學研究》的電腦可讀文件</title>
        <respStmt>
          <resp>編者</resp>
          <name>珍．崗妲</name>
        </respStmt>
        <idno type="ISSN">0 345 6789</idno>
        <biblScope unit="volume">1.2</biblScope>
      </seriesStmt>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD26"/>
    <ptr target="#HD2"/>
  </listRef>
```

^b22

