---
type: representation
source-type: document
source: '[[00_sources/tei-p5-watermark-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 watermark
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/watermark.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# watermark

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2793. Git blob: `8badfed29ec7f9546ccd3e70805de6a3b2b3696f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="WATERMARK" ident="watermark">
  <gloss versionDate="2007-06-12" xml:lang="en">watermark</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">filigrane</gloss>
  <desc versionDate="2005-01-14" xml:lang="en" xml:id="watermark.desc">contains a word or phrase describing a watermark or similar device.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">워터마크 또는 유사 도구를 기술하는 단어 또는 구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個字詞，描述一個浮水印或是類似圖案。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">すかし模様などを表す語句を示す。</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">contient un mot ou une expression décrivant un filigrane ou une marque du même genre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o sintagma que describe una filigrana o una técnica similar.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una parola o espressione che descrive la filigrana o una tecnica simile.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="WATERMARK-egXML-dt">
      <support>
        <p><material>Rag paper</material> with <watermark>anchor</watermark> watermark</p>
      </support>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="WATERMARK-egXML-ko" source="#fr-ex-BnF-Reliures">
      <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
      <decoNote type="gardes">Gardes (3+2), filigrane <watermark>B</watermark>. </decoNote>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="WATERMARK-egXML-eb">
      <support>
        <p><material>布漿紙</material>上有 <watermark>錨點</watermark>水印</p>
      </support>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mswat"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">watermark</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">filigrane</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en" xml:id="watermark.desc">contains a word or phrase describing a watermark or similar device.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">워터마크 또는 유사 도구를 기술하는 단어 또는 구를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個字詞，描述一個浮水印或是類似圖案。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">すかし模様などを表す語句を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">contient un mot ou une expression décrivant un filigrane ou une marque du même genre.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o sintagma que describe una filigrana o una técnica similar.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una parola o espressione che descrive la filigrana o una tecnica simile.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="WATERMARK-egXML-dt">
      <support>
        <p><material>Rag paper</material> with <watermark>anchor</watermark> watermark</p>
      </support>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="WATERMARK-egXML-ko" source="#fr-ex-BnF-Reliures">
      <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
      <decoNote type="gardes">Gardes (3+2), filigrane <watermark>B</watermark>. </decoNote>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="WATERMARK-egXML-eb">
      <support>
        <p><material>布漿紙</material>上有 <watermark>錨點</watermark>水印</p>
      </support>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mswat"/>
  </listRef>
```

^b15

