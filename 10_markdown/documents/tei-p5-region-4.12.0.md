---
type: representation
source-type: document
source: '[[00_sources/tei-p5-region-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 region
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/region.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# region

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3034. Git blob: `38441d3c087a82d54af60754280712bbdb5d1737`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-region" ident="region">
  <gloss versionDate="2008-12-09" xml:lang="en">region</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">région</gloss>
  <desc versionDate="2006-01-22" xml:lang="en">contains the name of an administrative unit such as a state, province, or county, larger than a settlement, but smaller than a country.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">도보다는 작고 정착지보다는 큰 주, 성, 도와 같은 행정단위명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含行政單位的名稱，例如州、省、或郡，範圍大於主政區，但小於國家。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">行政上の単位の名前を示す。例えば、地方、郡、居住地など。居住地よりも 広く、国家より狭い地域。</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient le nom d'une unité administrative comme un état, une province ou un comté, plus grande qu'un lieu de peuplement, mais plus petite qu'un pays.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">&gt;contiene el nombre de una unidad administrativa, como un estado, una región o una província, que sea mayor que un pequeño asentamiento, pero menor a un país.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'unità amministrativa, come uno stato o una provincia, che sia più ampia di un piccolo insediamento ma più piccola di un paese.</desc>
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
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-region-egXML-yg">
      <placeName>
        <region type="state" n="IL">Illinois</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-region-egXML-ft">
      <placeName>
        <region type="state" n="IL">Illinois</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-region-egXML-nk">
      <placeName>
        <region type="state" n="IL">依利諾</region>
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
<gloss versionDate="2008-12-09" xml:lang="en">region</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">région</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-22" xml:lang="en">contains the name of an administrative unit such as a state, province, or county, larger than a settlement, but smaller than a country.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">도보다는 작고 정착지보다는 큰 주, 성, 도와 같은 행정단위명을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含行政單位的名稱，例如州、省、或郡，範圍大於主政區，但小於國家。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">行政上の単位の名前を示す。例えば、地方、郡、居住地など。居住地よりも 広く、国家より狭い地域。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient le nom d'une unité administrative comme un état, une province ou un comté, plus grande qu'un lieu de peuplement, mais plus petite qu'un pays.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">&gt;contiene el nombre de una unidad administrativa, como un estado, una región o una província, que sea mayor que un pequeño asentamiento, pero menor a un país.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'unità amministrativa, come uno stato o una provincia, che sia più ampia di un piccolo insediamento ma più piccola di un paese.</desc>
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
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-region-egXML-yg">
      <placeName>
        <region type="state" n="IL">Illinois</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-region-egXML-ft">
      <placeName>
        <region type="state" n="IL">Illinois</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-region-egXML-nk">
      <placeName>
        <region type="state" n="IL">依利諾</region>
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

