---
type: representation
source-type: document
source: '[[00_sources/tei-p5-geogname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 geogName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/geogName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# geogName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3055. Git blob: `5bfbcaadc70f68b0ac66bf3ea0ff37ef3983bed5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-geogName" ident="geogName">
  <gloss versionDate="2005-01-14" xml:lang="en">geographical name</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">지리명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">地理名稱</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">nom de lieu géographique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nombre geográfico</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nome proprio geografico</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">identifies a name associated with some geographical feature such as Windrush Valley or Mount Sinai.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">윈드러시 계곡 또는 시나이 산과 같이 지리적 특성과 관련된 이름</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">與地形名稱結合的地名，例如威拉索溪谷、西奈山等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ウィンドラッシュ峡谷、シナイ山などの地理的特性に関する名前。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">un nom associé à une caractéristique géographique comme Windrush Valley ou le Mont Sinaï.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">un nombre asociado a un un elemento geográfico, como valle Windrush o Monte Sinaí.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">nome associato a un elemento geografico, come valle Windrush o Monte Sinai.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geogName-egXML-rf">
      <geogName>
        <geogFeat>Mount</geogFeat>
        <name>Sinai</name>
      </geogName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geogName-egXML-jn">
      <geogName><geogFeat>Dune</geogFeat>du <name>Pilat</name></geogName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geogName-egXML-ta">
      <geogName>
        <geogFeat>山峰</geogFeat>
        <name>廬山</name>
      </geogName>
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
<gloss versionDate="2005-01-14" xml:lang="en">geographical name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">지리명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">地理名稱</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">nom de lieu géographique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nombre geográfico</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nome proprio geografico</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">identifies a name associated with some geographical feature such as Windrush Valley or Mount Sinai.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">윈드러시 계곡 또는 시나이 산과 같이 지리적 특성과 관련된 이름</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">與地形名稱結合的地名，例如威拉索溪谷、西奈山等。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ウィンドラッシュ峡谷、シナイ山などの地理的特性に関する名前。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">un nom associé à une caractéristique géographique comme Windrush Valley ou le Mont Sinaï.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">un nombre asociado a un un elemento geográfico, como valle Windrush o Monte Sinaí.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">nome associato a un elemento geografico, come valle Windrush o Monte Sinai.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geogName-egXML-rf">
      <geogName>
        <geogFeat>Mount</geogFeat>
        <name>Sinai</name>
      </geogName>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geogName-egXML-jn">
      <geogName><geogFeat>Dune</geogFeat>du <name>Pilat</name></geogName>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geogName-egXML-ta">
      <geogName>
        <geogFeat>山峰</geogFeat>
        <name>廬山</name>
      </geogName>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
```

^b19

