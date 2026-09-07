---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.partials-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.partials
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.partials.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.partials

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4599. Git blob: `2c62638845a4cb752ab763b22d90ee2fa289cfc0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" ident="att.partials">
  <desc versionDate="2016-06-29" xml:lang="en">provides attributes for describing the extent of lexical references for a dictionary term.</desc>
  <desc versionDate="2023-08-24" xml:lang="ja">辞書用語の語彙参照の範囲を記述する属性を提供する。</desc>
  <attList>
    <attDef ident="extent" usage="opt">
      <desc versionDate="2016-06-29" xml:lang="en">indicates whether the pronunciation or orthography applies to all or part of a word.</desc>
      <desc versionDate="2016-06-29" xml:lang="fr">indique si la prononciation ou orthographie se rapporte au mot entier ou seulement à une partie.</desc>
      <!-- <desc versionDate="2007-12-20" xml:lang="ko">발음이 전체 단어 또는 부분에 대한 것인지를 표시한다.</desc>
    <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該發音為完整或部分發音。</desc>
    <desc versionDate="2023-08-24" xml:lang="ja">発音または正書法が単語の全部または一部に適用されるかどうかを示す。</desc>
    <desc versionDate="2007-05-04" xml:lang="es">indica si se trata de la pronunciación de la palabra completa o de una parte.</desc>
    <desc versionDate="2007-01-21" xml:lang="it">indica se la pronuncia riguarda l'intera parola o una sua parte.</desc> -->
    <datatype><dataRef key="teidata.enumerated"/></datatype>
    <valList type="semi">
      <valItem ident="full">
        <gloss versionDate="2005-01-14" xml:lang="en">full form</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">forme pleine</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">forma completa</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">forma completa</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">完全形</gloss>
      </valItem>
      <valItem ident="pref">
        <gloss versionDate="2005-01-14" xml:lang="en">prefix</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">préfixe</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">prefisso</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">prefijo</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">接頭辞</gloss>
      </valItem>
      <valItem ident="suff">
        <gloss versionDate="2005-01-14" xml:lang="en">suffix</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">suffixe</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">suffisso</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">sufijo</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">接尾辞</gloss>
      </valItem>
      <valItem ident="inf">
        <gloss versionDate="2016-06-29" xml:lang="en">infix</gloss>
        <gloss versionDate="2016-06-29" xml:lang="fr">infixe</gloss>
        <gloss versionDate="2016-06-29" xml:lang="it">infisso</gloss>
        <gloss versionDate="2016-06-29" xml:lang="es">infijteio</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">接中辞</gloss>
      </valItem>
      <valItem ident="part">
        <gloss versionDate="2005-01-14" xml:lang="en">partial</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">partiel</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">parziale</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">parcial</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">一部分</gloss>
      </valItem>
    </valList>
    <remarks ident="att.partials-attr.extent-remarks" versionDate="2016-06-29" xml:lang="en">
      <p>
        This attribute is optional, and no default value is specified, so it can be omitted if this information is not necessary.
        <!-- 2005-01-14 [Merge this and similar attributes into a class <term>partials</term>? -Ed.] -->
      </p>
    </remarks>
    <remarks ident="att.partials-attr.extent-remarks" versionDate="2023-08-24" xml:lang="ja">
      <p>
      この属性はオプションであり、デフォルト値は指定されていないため、この情報が不要な場合は省略することができる。
      </p>
    </remarks>
    </attDef>
  
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-06-29" xml:lang="en">provides attributes for describing the extent of lexical references for a dictionary term.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-08-24" xml:lang="ja">辞書用語の語彙参照の範囲を記述する属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2016-06-29" xml:lang="en">indicates whether the pronunciation or orthography applies to all or part of a word.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2016-06-29" xml:lang="fr">indique si la prononciation ou orthographie se rapporte au mot entier ou seulement à une partie.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
      <valItem ident="full">
        <gloss versionDate="2005-01-14" xml:lang="en">full form</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">forme pleine</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">forma completa</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">forma completa</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">完全形</gloss>
      </valItem>
      <valItem ident="pref">
        <gloss versionDate="2005-01-14" xml:lang="en">prefix</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">préfixe</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">prefisso</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">prefijo</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">接頭辞</gloss>
      </valItem>
      <valItem ident="suff">
        <gloss versionDate="2005-01-14" xml:lang="en">suffix</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">suffixe</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">suffisso</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">sufijo</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">接尾辞</gloss>
      </valItem>
      <valItem ident="inf">
        <gloss versionDate="2016-06-29" xml:lang="en">infix</gloss>
        <gloss versionDate="2016-06-29" xml:lang="fr">infixe</gloss>
        <gloss versionDate="2016-06-29" xml:lang="it">infisso</gloss>
        <gloss versionDate="2016-06-29" xml:lang="es">infijteio</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">接中辞</gloss>
      </valItem>
      <valItem ident="part">
        <gloss versionDate="2005-01-14" xml:lang="en">partial</gloss>
        <gloss versionDate="2007-06-12" xml:lang="fr">partiel</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">parziale</gloss>
        <gloss versionDate="2007-05-04" xml:lang="es">parcial</gloss>
        <gloss versionDate="2023-08-24" xml:lang="ja">一部分</gloss>
      </valItem>
    </valList>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.partials-attr.extent-remarks" versionDate="2016-06-29" xml:lang="en">
      <p>
        This attribute is optional, and no default value is specified, so it can be omitted if this information is not necessary.
        <!-- 2005-01-14 [Merge this and similar attributes into a class <term>partials</term>? -Ed.] -->
      </p>
    </remarks>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.partials-attr.extent-remarks" versionDate="2023-08-24" xml:lang="ja">
      <p>
      この属性はオプションであり、デフォルト値は指定されていないため、この情報が不要な場合は省略することができる。
      </p>
    </remarks>
```

^b8

