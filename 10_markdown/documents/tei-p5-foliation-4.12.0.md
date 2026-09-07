---
type: representation
source-type: document
source: '[[00_sources/tei-p5-foliation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 foliation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/foliation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# foliation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2579. Git blob: `35e394c7f26c3040d61e92c86aa44878a2187531`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="FOLIATION" ident="foliation">
  <gloss versionDate="2007-06-12" xml:lang="en">foliation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">foliotation</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="foliation.desc">describes the numbering system or systems used to 
count the leaves or pages in a codex or similar object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">미제본 원고의 장 또는 페이지를 세는 시스템을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述計算手抄本紙張頁數的一種或多種編號系統。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">冊子における葉やページを数える付番システムを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit le ou les systèmes de numérotation des
      feuillets ou pages d'un codex.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe el sistema o sistemas de numeración usados para contar los fólios o las páginas de un códex.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive il sistema o i sistemi di numerazione usati per contare i fogli o le pagine di un codice.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FOLIATION-egXML-mm">
      <foliation>Contemporary foliation in red 
roman numerals in the centre
of the outer margin.</foliation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FOLIATION-egXML-fh">
      <foliation>Contemporary foliation in red roman numerals in the centre of the outer
        margin.</foliation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FOLIATION-egXML-zf">
      <foliation>頁邊空白的中心有以紅色羅馬數字標示的當代編張數號</foliation>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msphfo"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">foliation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">foliotation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="foliation.desc">describes the numbering system or systems used to 
count the leaves or pages in a codex or similar object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">미제본 원고의 장 또는 페이지를 세는 시스템을 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述計算手抄本紙張頁數的一種或多種編號系統。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">冊子における葉やページを数える付番システムを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit le ou les systèmes de numérotation des
      feuillets ou pages d'un codex.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe el sistema o sistemas de numeración usados para contar los fólios o las páginas de un códex.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il sistema o i sistemi di numerazione usati per contare i fogli o le pagine di un codice.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FOLIATION-egXML-mm">
      <foliation>Contemporary foliation in red 
roman numerals in the centre
of the outer margin.</foliation>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FOLIATION-egXML-fh">
      <foliation>Contemporary foliation in red roman numerals in the centre of the outer
        margin.</foliation>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FOLIATION-egXML-zf">
      <foliation>頁邊空白的中心有以紅色羅馬數字標示的當代編張數號</foliation>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msphfo"/>
  </listRef>
```

^b15

