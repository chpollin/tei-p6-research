---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.msexcerpt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.msExcerpt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.msExcerpt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.msExcerpt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4949. Git blob: `826e6eb54c1dc43c9d375df701415f1981c04f66`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" predeclare="true" module="msdescription" type="atts" ident="att.msExcerpt">
  <gloss versionDate="2007-03-05" xml:lang="en">manuscript excerpt</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">원고 발췌</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">手稿摘錄</gloss>
  <gloss versionDate="2009-05-28" xml:lang="fr">extrait d'un manuscrit</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">estratto di manoscritto</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">extracto de manuscrito</gloss>
  <gloss versionDate="2022-08-26" xml:lang="ja">手書き資料からの引用</gloss>
  <desc versionDate="2007-10-18" xml:lang="en">provides attributes used to describe excerpts from a manuscript placed in a description thereof.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 발췌본을 기술하는 속성을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供用來描述關於手稿摘錄的屬性</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料からの引用を記述するための属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour décrire les extraits d'un manuscrit.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">assegna degli attributi utilizzati per descrivere estratti di un manoscritto inseriti in una descrizione dello stesso.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos usados para describir extractos de un manuscrito ******</desc>
  <attList>
    <attDef ident="defective" usage="opt">
      <desc versionDate="2007-03-05" xml:lang="en">indicates whether the passage being quoted is defective,
      i.e. incomplete through loss or damage.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">인용 어구의 결합 여부를 표시한다. 즉, 손실 또는 손상을 통한 불완전성</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出所引用的段落是否不完全，例如因遺失或損毀而不完全。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該部分に問題があるかどうかを示す。例えば、欠損や損傷による不完
      全さなど。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">indique si le passage décrit est fautif, i.e. incomplet en raison d'une lacune ou d'une détérioration.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica se il brano citato sia o meno incompleto a causa di perdite o danni.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el pasaje que se describe es completo o no, p.ej. si ha sufrido pérdidas o daños.</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
    </attDef>
  </attList>
  <remarks ident="att.msExcerpt-remarks" versionDate="2007-03-05" xml:lang="en">
    <p>In the case of an incipit, indicates whether the incipit as
    given is defective, i.e. the first words of the text as preserved,
    as opposed to the first words of the work itself. In the case of
    an explicit, indicates whether the explicit as given is defective,
    i.e. the final words of the text as preserved, as opposed to what
    the closing words would have been had the text of the work been
    whole.</p>
  </remarks>
  <remarks ident="att.msExcerpt-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans le cas d'un incipit, indique si l'incipit est considéré comme fautif, c'est-à-dire qu'il
                présente les premiers mots du texte tels qu'ils ont été conservés, et non pas les
                premiers mots de l'oeuvre elle-même. 
                Dans le cas d'un explicit, indique si l'explicit est considéré comme fautif, c'est-à-dire qu'il présente les mots
                finaux du texte tels qu'ils ont été préservés, et non pas ce qu'auraient été ces mots si le texte de l'oeuvre avait été complet. </p>
  </remarks>
  <remarks ident="att.msExcerpt-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    冒頭語(incipit)の場合、当該属性はそこに問題があることを示す。
    例えば、当該テキストの最初の語句が、作品自体の最初の語句と一致しな
    い場合など。
    末尾語(explicit)の場合、当該属性はそこに問題があることを示す。
    例えば、当該テキストの最終語が、作品全体の最後の語と一致しない場合
    など。
    </p>
  </remarks>
  <listRef>
    <ptr target="#msco"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-03-05" xml:lang="en">manuscript excerpt</gloss>
```

^b1

### Block 2

XML location: `/classSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">원고 발췌</gloss>
```

^b2

### Block 3

XML location: `/classSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">手稿摘錄</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">extrait d'un manuscrit</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">estratto di manoscritto</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">extracto de manuscrito</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2022-08-26" xml:lang="ja">手書き資料からの引用</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">provides attributes used to describe excerpts from a manuscript placed in a description thereof.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 발췌본을 기술하는 속성을 제시한다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供用來描述關於手稿摘錄的屬性</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料からの引用を記述するための属性を示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour décrire les extraits d'un manuscrit.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna degli attributi utilizzati per descrivere estratti di un manoscritto inseriti in una descrizione dello stesso.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos usados para describir extractos de un manuscrito ******</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-03-05" xml:lang="en">indicates whether the passage being quoted is defective,
      i.e. incomplete through loss or damage.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인용 어구의 결합 여부를 표시한다. 즉, 손실 또는 손상을 통한 불완전성</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出所引用的段落是否不完全，例如因遺失或損毀而不完全。</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該部分に問題があるかどうかを示す。例えば、欠損や損傷による不完
      全さなど。</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">indique si le passage décrit est fautif, i.e. incomplet en raison d'une lacune ou d'une détérioration.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica se il brano citato sia o meno incompleto a causa di perdite o danni.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el pasaje que se describe es completo o no, p.ej. si ha sufrido pérdidas o daños.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b22

### Block 23

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.msExcerpt-remarks" versionDate="2007-03-05" xml:lang="en">
    <p>In the case of an incipit, indicates whether the incipit as
    given is defective, i.e. the first words of the text as preserved,
    as opposed to the first words of the work itself. In the case of
    an explicit, indicates whether the explicit as given is defective,
    i.e. the final words of the text as preserved, as opposed to what
    the closing words would have been had the text of the work been
    whole.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.msExcerpt-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans le cas d'un incipit, indique si l'incipit est considéré comme fautif, c'est-à-dire qu'il
                présente les premiers mots du texte tels qu'ils ont été conservés, et non pas les
                premiers mots de l'oeuvre elle-même. 
                Dans le cas d'un explicit, indique si l'explicit est considéré comme fautif, c'est-à-dire qu'il présente les mots
                finaux du texte tels qu'ils ont été préservés, et non pas ce qu'auraient été ces mots si le texte de l'oeuvre avait été complet. </p>
  </remarks>
```

^b24

### Block 25

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.msExcerpt-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    冒頭語(incipit)の場合、当該属性はそこに問題があることを示す。
    例えば、当該テキストの最初の語句が、作品自体の最初の語句と一致しな
    い場合など。
    末尾語(explicit)の場合、当該属性はそこに問題があることを示す。
    例えば、当該テキストの最終語が、作品全体の最後の語と一致しない場合
    など。
    </p>
  </remarks>
```

^b25

### Block 26

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msco"/>
  </listRef>
```

^b26

