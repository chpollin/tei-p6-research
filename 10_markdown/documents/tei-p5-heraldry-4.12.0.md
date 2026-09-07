---
type: representation
source-type: document
source: '[[00_sources/tei-p5-heraldry-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 heraldry
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/heraldry.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# heraldry

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2939. Git blob: `640e9d5f7efcd25242d63b6c1f55e3f124388533`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="HERALDRY" ident="heraldry">
  <gloss versionDate="2007-06-12" xml:lang="en">heraldry</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">héraldique</gloss>
  <desc versionDate="2005-12-13" xml:lang="en" xml:id="heraldry.desc">contains a heraldic formula
or phrase, typically found as part of a blazon, coat of arms, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">보통 문장이 새겨진 방패의 일부로 사용되는 문장 형식 또는 구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個紋章學的常規或詞彙，通常是裝飾、或盾形紋章等的一部分。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">紋章学的記述を含む。例えば、紋章記述や紋章など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une devise ou une formule d'héraldique,
      comme celles qu'on trouve sur un blason, des armoiries, etc.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula o frade heráldica, normalmente parte de un escudo de armas, blasón, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una formula araldica di solito parte di uno stemma, blasone, ecc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HERALDRY-egXML-wk">
      <p>Ownership stamp (xvii cent.) on i recto with the arms
<heraldry>A bull passant within a bordure bezanty, 
in chief a crescent for difference</heraldry> [Cole], 
crest, and the legend <q>Cole Deum</q>.</p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HERALDRY-egXML-hi" source="#fr-ex-Viton-dictionnaire">
      <p>Barbey, en Normandie : <heraldry>d'azur, à deux bars adossés d'argent ; au chef cousu de
            gueules, chargé de trois tourteaux d'or.</heraldry>.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HERALDRY-egXML-ik" source="#biblzh-tw_n44">
      <p>劍鞘正面的交叉雙彎刀及棗椰樹金雕貼花圖案為沙烏地阿拉伯王國的紋章。藍色絨布外盒，鑲有金色交叉雙彎刀及棗椰樹圖案。</p>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mshera"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">heraldry</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">héraldique</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-12-13" xml:lang="en" xml:id="heraldry.desc">contains a heraldic formula
or phrase, typically found as part of a blazon, coat of arms, etc.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">보통 문장이 새겨진 방패의 일부로 사용되는 문장 형식 또는 구를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個紋章學的常規或詞彙，通常是裝飾、或盾形紋章等的一部分。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">紋章学的記述を含む。例えば、紋章記述や紋章など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une devise ou une formule d'héraldique,
      comme celles qu'on trouve sur un blason, des armoiries, etc.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula o frade heráldica, normalmente parte de un escudo de armas, blasón, etc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una formula araldica di solito parte di uno stemma, blasone, ecc.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HERALDRY-egXML-wk">
      <p>Ownership stamp (xvii cent.) on i recto with the arms
<heraldry>A bull passant within a bordure bezanty, 
in chief a crescent for difference</heraldry> [Cole], 
crest, and the legend <q>Cole Deum</q>.</p>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HERALDRY-egXML-hi" source="#fr-ex-Viton-dictionnaire">
      <p>Barbey, en Normandie : <heraldry>d'azur, à deux bars adossés d'argent ; au chef cousu de
            gueules, chargé de trois tourteaux d'or.</heraldry>.</p>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HERALDRY-egXML-ik" source="#biblzh-tw_n44">
      <p>劍鞘正面的交叉雙彎刀及棗椰樹金雕貼花圖案為沙烏地阿拉伯王國的紋章。藍色絨布外盒，鑲有金色交叉雙彎刀及棗椰樹圖案。</p>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mshera"/>
  </listRef>
```

^b15

