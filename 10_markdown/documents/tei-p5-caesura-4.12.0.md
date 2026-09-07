---
type: representation
source-type: document
source: '[[00_sources/tei-p5-caesura-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 caesura
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/caesura.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# caesura

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2506. Git blob: `6e82f9a954595609c6538c4059140fc691626ff3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="verse" xml:id="gi-caesura" ident="caesura">
  <desc versionDate="2005-01-14" xml:lang="en">marks the point at which a metrical line may be divided.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">운율 행이 분리될 수 있는 지점을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記韻律詩行可能被截斷的位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">韻律行が分割されている場所を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">signale une coupe rythmique à l'intérieur d'un vers.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">señala una interrupción rítmica en el interior de un verso.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segnala un'interruzione ritmica all'interno di un verso.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.lPart"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caesura-egXML-yf" source="#VESTR-eg-1" xml:lang="ang">
      <l>Hwæt we Gar-Dena <caesura/> in gear-dagum</l>
      <l>þeod-cyninga <caesura/> þrym gefrunon,</l>
      <l>hy ða æþelingas <caesura/> ellen fremedon.</l>
    </egXML>
    <!-- Beowulf, ed Wrenn , 1953 -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caesura-egXML-jd" source="#fr-ex-Lamartine">
      <l>Souvent sur la montagne,<caesura/> à l'ombre du vieux chêne,</l>
      <l> Au coucher du soleil,<caesura/> tristement je m'assieds ;</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caesura-egXML-iq" source="#biblzh-tw_n62-64">
      <l>枯藤<caesura/>老樹<caesura/>昏鴉</l>
      <l>小橋<caesura/>流水<caesura/>人家</l>
      <l>古道<caesura/>西風<caesura/>瘦馬</l>
      <l>夕陽西下<caesura/>斷腸人在天涯</l>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#VESE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks the point at which a metrical line may be divided.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">운율 행이 분리될 수 있는 지점을 표시한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記韻律詩行可能被截斷的位置。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">韻律行が分割されている場所を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">signale une coupe rythmique à l'intérieur d'un vers.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala una interrupción rítmica en el interior de un verso.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segnala un'interruzione ritmica all'interno di un verso.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.lPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caesura-egXML-yf" source="#VESTR-eg-1" xml:lang="ang">
      <l>Hwæt we Gar-Dena <caesura/> in gear-dagum</l>
      <l>þeod-cyninga <caesura/> þrym gefrunon,</l>
      <l>hy ða æþelingas <caesura/> ellen fremedon.</l>
    </egXML>
    <!-- Beowulf, ed Wrenn , 1953 -->
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caesura-egXML-jd" source="#fr-ex-Lamartine">
      <l>Souvent sur la montagne,<caesura/> à l'ombre du vieux chêne,</l>
      <l> Au coucher du soleil,<caesura/> tristement je m'assieds ;</l>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caesura-egXML-iq" source="#biblzh-tw_n62-64">
      <l>枯藤<caesura/>老樹<caesura/>昏鴉</l>
      <l>小橋<caesura/>流水<caesura/>人家</l>
      <l>古道<caesura/>西風<caesura/>瘦馬</l>
      <l>夕陽西下<caesura/>斷腸人在天涯</l>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#VESE"/>
  </listRef>
```

^b13

