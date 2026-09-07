---
type: representation
source-type: document
source: '[[00_sources/tei-p5-settlement-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 settlement
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/settlement.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# settlement

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3076. Git blob: `88a4b2bf1e1bb1aea40cd4ace66e918eb641e2f6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-settlement" ident="settlement">
  <gloss versionDate="2008-12-09" xml:lang="en">settlement</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">lieu de peuplement</gloss>
  <desc versionDate="2006-01-22" xml:lang="en">contains the name of a settlement such as a city, town, or village identified as a single geo-political or administrative unit.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 지리-정치 또는 행정 단위로 식별되는 시, 읍, 마을과 같이 거주지명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含主行政區的名稱，例如城市、鄉鎮、村莊等單一地理政治或行政單位。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">地政学上または行政上の単位としてある市、街、村などの居住地の名前を示 す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient le nom d'un lieu de peuplement comme une cité, une ville ou un village, identifié comme une unité géo-politique ou administrative unique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de un asentamiento, del tipo ciudad, pueblo, villa etc. identificado como una unidad geopolítica o administrativa.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un insediamento quale una città o un comune considerati come unità geopolitica o amministrativa.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settlement-egXML-nl">
      <placeName>
        <settlement type="town">Glasgow</settlement>
        <region>Scotland</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settlement-egXML-tj">
      <placeName>
        <settlement type="town">Brest</settlement>
        <region>Bretagne</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settlement-egXML-pc">
      <placeName>
        <settlement type="town">淡水</settlement>
        <region>台北縣</region>
      </placeName>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">settlement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">lieu de peuplement</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-22" xml:lang="en">contains the name of a settlement such as a city, town, or village identified as a single geo-political or administrative unit.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 지리-정치 또는 행정 단위로 식별되는 시, 읍, 마을과 같이 거주지명을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含主行政區的名稱，例如城市、鄉鎮、村莊等單一地理政治或行政單位。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">地政学上または行政上の単位としてある市、街、村などの居住地の名前を示 す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient le nom d'un lieu de peuplement comme une cité, une ville ou un village, identifié comme une unité géo-politique ou administrative unique.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de un asentamiento, del tipo ciudad, pueblo, villa etc. identificado como una unidad geopolítica o administrativa.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un insediamento quale una città o un comune considerati come unità geopolitica o amministrativa.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settlement-egXML-nl">
      <placeName>
        <settlement type="town">Glasgow</settlement>
        <region>Scotland</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settlement-egXML-tj">
      <placeName>
        <settlement type="town">Brest</settlement>
        <region>Bretagne</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settlement-egXML-pc">
      <placeName>
        <settlement type="town">淡水</settlement>
        <region>台北縣</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
```

^b15

