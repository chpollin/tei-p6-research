---
type: representation
source-type: document
source: '[[00_sources/tei-p5-district-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 district
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/district.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# district

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3992. Git blob: `3f20b412654e98ec38673f3c71a09a7a9771114b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-district" ident="district">
  <gloss versionDate="2008-12-09" xml:lang="en">district</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">district</gloss>
  <desc versionDate="2006-01-22" xml:lang="en">contains the name of any kind of subdivision of a settlement, such as a parish, ward, or other administrative or geographic unit.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">교구, 구 또는 다른 행정 지리적 단위와 같이 거주지의 하위 구분명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何次行政區名稱，例如教區、選區、或其他行政或地理單元。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">場所を示す要素として、集落より小さい名前を示す。例えば、小教区や区な ど、行政上・地勢上の単位。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient le nom d'une subdivision quelconque d'une ville, comme une paroisse, une circonscription électorale ou toute autre unité administrative ou géographique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de cualquier subdivisión al interno de un asentamiento, como una circunscripción, un barrio u otras unidades administrativas o geográficas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di una qualsiasi suddivisione all'interno di un insediamento, come una circoscrizione, un quartiere o altre unità amministrative o geografiche.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-jy">
      <placeName>
        <district type="ward">Jericho</district>
        <settlement>Oxford</settlement>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-yl">
      <placeName>
        <district type="ward">La Castellane</district>
        <settlement>Marseille</settlement>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-mv">
      <placeName>
        <district type="area">Rive gauche</district>
        <settlement>Paris</settlement>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-il">
      <placeName>
        <district type="ward">中環</district>
        <settlement>香港</settlement>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-zj">
      <placeName>
        <district type="area">南邊</district>
        <settlement>廣州</settlement>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-ed">
      <placeName>
        <district type="area">South Side</district>
        <settlement>Chicago</settlement>
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
<gloss versionDate="2008-12-09" xml:lang="en">district</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">district</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-22" xml:lang="en">contains the name of any kind of subdivision of a settlement, such as a parish, ward, or other administrative or geographic unit.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">교구, 구 또는 다른 행정 지리적 단위와 같이 거주지의 하위 구분명을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何次行政區名稱，例如教區、選區、或其他行政或地理單元。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">場所を示す要素として、集落より小さい名前を示す。例えば、小教区や区な ど、行政上・地勢上の単位。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient le nom d'une subdivision quelconque d'une ville, comme une paroisse, une circonscription électorale ou toute autre unité administrative ou géographique.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de cualquier subdivisión al interno de un asentamiento, como una circunscripción, un barrio u otras unidades administrativas o geográficas.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di una qualsiasi suddivisione all'interno di un insediamento, come una circoscrizione, un quartiere o altre unità amministrative o geografiche.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-jy">
      <placeName>
        <district type="ward">Jericho</district>
        <settlement>Oxford</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-yl">
      <placeName>
        <district type="ward">La Castellane</district>
        <settlement>Marseille</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-mv">
      <placeName>
        <district type="area">Rive gauche</district>
        <settlement>Paris</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-il">
      <placeName>
        <district type="ward">中環</district>
        <settlement>香港</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-zj">
      <placeName>
        <district type="area">南邊</district>
        <settlement>廣州</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-district-egXML-ed">
      <placeName>
        <district type="area">South Side</district>
        <settlement>Chicago</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
```

^b18

