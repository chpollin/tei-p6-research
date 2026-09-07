---
type: representation
source-type: document
source: '[[00_sources/tei-p5-bloc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 bloc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/bloc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# bloc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2675. Git blob: `9810ebfdbd5e8d43bc8e70b29c691a3dfa3b248a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-bloc" ident="bloc">
  <gloss versionDate="2008-12-09" xml:lang="en">bloc</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">bloc</gloss>
  <desc versionDate="2007-02-27" xml:lang="en">contains the name of a geo-political unit consisting of two or more nation states or countries.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">둘 이상의 민족국가 또는 국가로 구성된 지리-정치적 단위의 이름을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個地理政治區域名稱，由一個或多個國家所組成。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">複数の国や地域を跨ぐ地政学的な名前を示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient le nom d'une unité géo-politique composée d'au moins deux états ou pays.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de una unidad geopolítica que comprende uno o más estados nacionales o países.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'unità geopolitica comprendente uno o più stati nazione o paesi.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bloc-egXML-ty">
      <bloc type="union">the European Union</bloc>
      <bloc type="continent">Africa</bloc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bloc-egXML-vi">
      <bloc type="union">Pays Baltes</bloc>
      <bloc type="continent">Europe</bloc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bloc-egXML-kb">
      <bloc type="union">歐盟</bloc>
      <bloc type="continent">非洲</bloc>
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
<gloss versionDate="2008-12-09" xml:lang="en">bloc</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">bloc</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-02-27" xml:lang="en">contains the name of a geo-political unit consisting of two or more nation states or countries.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">둘 이상의 민족국가 또는 국가로 구성된 지리-정치적 단위의 이름을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個地理政治區域名稱，由一個或多個國家所組成。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">複数の国や地域を跨ぐ地政学的な名前を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient le nom d'une unité géo-politique composée d'au moins deux états ou pays.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de una unidad geopolítica que comprende uno o más estados nacionales o países.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'unità geopolitica comprendente uno o più stati nazione o paesi.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bloc-egXML-ty">
      <bloc type="union">the European Union</bloc>
      <bloc type="continent">Africa</bloc>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bloc-egXML-vi">
      <bloc type="union">Pays Baltes</bloc>
      <bloc type="continent">Europe</bloc>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bloc-egXML-kb">
      <bloc type="union">歐盟</bloc>
      <bloc type="continent">非洲</bloc>
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

