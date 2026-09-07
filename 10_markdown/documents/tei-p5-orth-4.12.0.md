---
type: representation
source-type: document
source: '[[00_sources/tei-p5-orth-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 orth
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/orth.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# orth

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3946. Git blob: `e235063356728bea802b131d4a2ae5ec9bec1795`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-orth" ident="orth">
  <gloss versionDate="2005-01-14" xml:lang="en">orthographic form</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">철자 형식</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">拼字形式</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">forme orthographique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">forma ortográfica</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">forma ortografica</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">gives the orthographic form of a dictionary headword.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전 표제어의 철자 형식을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供字典標題字的拼字形式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書の見出し語の正書形を示す。</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">donne l’orthographe d'un mot-vedette de dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona la forma ortográfica del lema de la entrada
    del diccionario</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce la forma ortografica di un lemma.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.partials"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.formPart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the type of spelling.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">철자 유형을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供拼字的類型。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該綴りの種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le type d’orthographe.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el tipo de ortografía.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce il tipo di trascrizione ortografica.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-fa">
      <form type="infl">
        <orth>brags</orth>
        <orth>bragging</orth>
        <orth>bragged</orth>
      </form>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-mb">
      <form>
        <orth type="standard" xml:lang="ko-Hang">치다</orth>
        <orth type="transliterated" xml:lang="ko-Latn">chida</orth>
      </form>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-ti">
      <form type="derivative">
        <orth>Déshéritement</orth>
      </form>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-tl">
      <form>
        <orth xml:lang="zh-Hant-TW">龍</orth>
        <orth xml:lang="zh-Hans-CN">龙</orth>
        <orth xml:lang="ja-Hani">竜</orth>
      </form>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">orthographic form</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">철자 형식</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">拼字形式</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">forme orthographique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">forma ortográfica</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">forma ortografica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the orthographic form of a dictionary headword.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전 표제어의 철자 형식을 제시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供字典標題字的拼字形式。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書の見出し語の正書形を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">donne l’orthographe d'un mot-vedette de dictionnaire.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona la forma ortográfica del lema de la entrada
    del diccionario</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce la forma ortografica di un lemma.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.partials"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.formPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the type of spelling.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">철자 유형을 제시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供拼字的類型。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該綴りの種類を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne le type d’orthographe.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el tipo de ortografía.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il tipo di trascrizione ortografica.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-fa">
      <form type="infl">
        <orth>brags</orth>
        <orth>bragging</orth>
        <orth>bragged</orth>
      </form>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-mb">
      <form>
        <orth type="standard" xml:lang="ko-Hang">치다</orth>
        <orth type="transliterated" xml:lang="ko-Latn">chida</orth>
      </form>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-ti">
      <form type="derivative">
        <orth>Déshéritement</orth>
      </form>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orth-egXML-tl">
      <form>
        <orth xml:lang="zh-Hant-TW">龍</orth>
        <orth xml:lang="zh-Hans-CN">龙</orth>
        <orth xml:lang="ja-Hani">竜</orth>
      </form>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
```

^b28

