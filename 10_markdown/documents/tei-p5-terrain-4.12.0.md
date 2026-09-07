---
type: representation
source-type: document
source: '[[00_sources/tei-p5-terrain-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 terrain
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/terrain.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# terrain

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2613. Git blob: `fdb13da8981e6f6d8b6e1b4242228290d21f91a0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="terrain" xml:id="gi-terrain" module="namesdates">
  <gloss versionDate="2009-03-19" xml:lang="en">terrain</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">terrain</gloss>
  <desc versionDate="2007-10-18" xml:lang="en">contains information about the physical terrain of a place.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient des informations sur le terrain physique d'un lieu.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">장소의 물리적 지역에 대한 정보를 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene información sobre el terreno físico de un lugar.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">場所の地形情報を示す。</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene informazioni relative al terreno fisico di un luogo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>      
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
      </alternate>
      <elementRef key="terrain" minOccurs="0" maxOccurs="unbounded"/>      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-terrain-egXML-ju">
      <place xml:id="KERG">
        <placeName>Kerguelen Islands</placeName>
        <!-- ... -->
        <terrain>
          <desc>antarctic tundra</desc>
        </terrain>
        <!-- ... -->
      </place>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDGEOGste"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="en">terrain</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="fr">terrain</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">contains information about the physical terrain of a place.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient des informations sur le terrain physique d'un lieu.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">장소의 물리적 지역에 대한 정보를 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene información sobre el terreno físico de un lugar.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">場所の地形情報を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene informazioni relative al terreno fisico di un luogo.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>      
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
      </alternate>
      <elementRef key="terrain" minOccurs="0" maxOccurs="unbounded"/>      
    </sequence>
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-terrain-egXML-ju">
      <place xml:id="KERG">
        <placeName>Kerguelen Islands</placeName>
        <!-- ... -->
        <terrain>
          <desc>antarctic tundra</desc>
        </terrain>
        <!-- ... -->
      </place>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDGEOGste"/>
  </listRef>
```

^b12

