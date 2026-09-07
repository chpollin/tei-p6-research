---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listplace-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listPlace
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listPlace.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listPlace

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3916. Git blob: `67b8a4bebde3b2181621e8bc63d72211467c4f1b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-listPlace" ident="listPlace">
  <gloss versionDate="2007-07-04" xml:lang="en">list of places</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">장소 목록</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">lista de lugares</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">liste de lieux</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">elenco dei luoghi</gloss>
  <desc versionDate="2007-06-14" xml:lang="en">contains a list of places, optionally followed by a list of relationships (other than
        containment) defined amongst them.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">장소 목록을 포함하며, 그 뒤에 수의적으로 그들 사이에 정의된 (포함 외의) 관련성 목록을
        제시한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una lista de lugares, seguida opcionalmente
        por una lista de interelaciones (a excepción de la inclusión) definidas entre ellos.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">場所のリストを示す。選択的に、場所間の(包含関係ではなく)関連性を 示すリストが続く。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient une liste de lieux, qui peut être suivie d'une
        liste de relations définies entre les lieux (autres que la relation d'inclusion).</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una lista di luoghi, eventualmente seguita da
        una lista di relazioni tra questi (ad eccezione di quella contenete-contenuto)</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
    <memberOf key="model.orgPart"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.placeLike" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listPlace" minOccurs="1" maxOccurs="1"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <constraintSpec ident="listPlace-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listPlace"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listPlace-egXML-lt">
      <listPlace type="offshoreIslands">
        <place>
          <placeName>La roche qui pleure</placeName>
        </place>
        <place>
          <placeName>Ile aux cerfs</placeName>
        </place>
      </listPlace>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD3"/>
    <ptr target="#NDGEOG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">list of places</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">장소 목록</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">lista de lugares</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">liste de lieux</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">elenco dei luoghi</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-06-14" xml:lang="en">contains a list of places, optionally followed by a list of relationships (other than
        containment) defined amongst them.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">장소 목록을 포함하며, 그 뒤에 수의적으로 그들 사이에 정의된 (포함 외의) 관련성 목록을
        제시한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una lista de lugares, seguida opcionalmente
        por una lista de interelaciones (a excepción de la inclusión) definidas entre ellos.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">場所のリストを示す。選択的に、場所間の(包含関係ではなく)関連性を 示すリストが続く。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient une liste de lieux, qui peut être suivie d'une
        liste de relations définies entre les lieux (autres que la relation d'inclusion).</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una lista di luoghi, eventualmente seguita da
        una lista di relazioni tra questi (ad eccezione di quella contenete-contenuto)</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
    <memberOf key="model.orgPart"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.placeLike" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listPlace" minOccurs="1" maxOccurs="1"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="listPlace-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listPlace"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listPlace-egXML-lt">
      <listPlace type="offshoreIslands">
        <place>
          <placeName>La roche qui pleure</placeName>
        </place>
        <place>
          <placeName>Ile aux cerfs</placeName>
        </place>
      </listPlace>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD3"/>
    <ptr target="#NDGEOG"/>
  </listRef>
```

^b16

