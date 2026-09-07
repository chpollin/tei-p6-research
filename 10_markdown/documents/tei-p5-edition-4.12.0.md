---
type: representation
source-type: document
source: '[[00_sources/tei-p5-edition-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 edition
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/edition.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# edition

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2735. Git blob: `2e2f63271fa8cb448e6807cf8f138c3cc42771bf`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-edition" ident="edition">
  <gloss versionDate="2007-01-21" xml:lang="en">edition</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">édition</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">편집, 판</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">版本</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Ausgabe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">edición</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">Edizione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the particularities of one edition of a text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit les particularités de l’édition d’un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 한 판의 특성을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述文件某一版本的特質。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストの版の詳細を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">beschreibt die Details einer Ausgabe eines Textes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe las particularidades de la edición de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive le peculiarità di una edizione del testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-edition-egXML-oh">
      <edition>First edition <date>Oct 1990</date>
         </edition>
      <edition n="S2">Students' edition</edition>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-edition-egXML-no">
      <edition>Première édition électronique, Nancy <date>2002</date>
         </edition>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-edition-egXML-nw">
      <edition>初版<date>1990年10月</date>
         </edition>
      <edition n="S2">學生版</edition>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD22"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="en">edition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">édition</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">편집, 판</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">版本</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Ausgabe</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">edición</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">Edizione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the particularities of one edition of a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit les particularités de l’édition d’un texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 한 판의 특성을 기술한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述文件某一版本的特質。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストの版の詳細を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">beschreibt die Details einer Ausgabe eines Textes.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe las particularidades de la edición de un texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive le peculiarità di una edizione del testo.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-edition-egXML-oh">
      <edition>First edition <date>Oct 1990</date>
         </edition>
      <edition n="S2">Students' edition</edition>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-edition-egXML-no">
      <edition>Première édition électronique, Nancy <date>2002</date>
         </edition>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-edition-egXML-nw">
      <edition>初版<date>1990年10月</date>
         </edition>
      <edition n="S2">學生版</edition>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD22"/>
  </listRef>
```

^b21

