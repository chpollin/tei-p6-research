---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.global.analytic-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.global.analytic
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.global.analytic.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.global.analytic

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4683. Git blob: `e8a0def256aaffd75c29d7e18e0aa4915a027edf`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" predeclare="true" module="analysis" xml:id="CLANA" type="atts" ident="att.global.analytic">
  <desc versionDate="2006-01-05" xml:lang="en">provides additional global attributes for associating specific analyses or
interpretations with appropriate portions of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 일정한 부분의 특별한 분석 혹은 해석과 관련된 부가적인 전반적 속성들을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供附加的全域屬性，將特定的分析或詮釋和合宜的文字結合。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">任意のテキスト部分への分析・解釈に関連するグローバル属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs globaux complémentaires pour
      associer des analyses ou des interprétations spécifiques avec des portions de texte
      appropriées.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos globales adicionales para asociar análisis específicos o interpretaciones con las partes apropiadas de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna ulteriori attributi globali per associare specifiche analisi o interpretazioni alle adeguate porzioni di un testo.</desc>
  <attList>
    <attDef ident="ana" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">analysis</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">분석</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">análisis</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">analyse</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">analisi</gloss>
      <gloss versionDate="2019-06-08" xml:lang="ja">分析</gloss>
      <desc versionDate="2006-01-05" xml:lang="en">indicates one or more elements containing interpretations of the
element on which the <att>ana</att> attribute appears.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"><att>ana</att> 속성이 나오는 요소들의 해석을 포함하는 하나 혹은 그 이상의 요소들을 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出一個或多個元素，其中包含帶有屬性<att>ana</att>的元素解釋。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">属性<att>ana</att>を伴う要素の解釈を含む要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique un ou plusieurs éléments contenant des
          interprétations de l'élément qui porte l'attribut <att>ana</att>.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica uno o más elementos que contienen interpretaciones del elemento en el cual aparece el atributo <att>ana</att></desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica uno o più elementi che contengono interpretazioni dell'elemento specificato dall'attributo <att>ana</att></desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>


      <remarks ident="att.global.analytic-attr.ana-remarks" versionDate="2006-01-05" xml:lang="en">
        <p>When multiple values are given, they may reflect either
multiple divergent interpretations of an ambiguous text, or multiple
mutually consistent interpretations of the same passage in different
contexts.</p>
      </remarks>
      <remarks ident="att.global.analytic-attr.ana-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Quand on donne de multiples valeurs, celles-ci peuvent refléter, soit des
                        interprétations multiples et divergentes d'un texte ambigu soit des
                        interprétations multiples et compatibles du même passage dans différents
                        contextes.</p>
      </remarks>
      <remarks ident="att.global.analytic-attr.ana-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        複数の属性値が付与される場合、各値は当該テキストの異なる解釈や、
        または同じ部分が異なる文脈でも同じ解釈であることを示す。
        </p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#AIATTS"/>
    <ptr target="#AISP"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-05" xml:lang="en">provides additional global attributes for associating specific analyses or
interpretations with appropriate portions of a text.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 일정한 부분의 특별한 분석 혹은 해석과 관련된 부가적인 전반적 속성들을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供附加的全域屬性，將特定的分析或詮釋和合宜的文字結合。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">任意のテキスト部分への分析・解釈に関連するグローバル属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs globaux complémentaires pour
      associer des analyses ou des interprétations spécifiques avec des portions de texte
      appropriées.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos globales adicionales para asociar análisis específicos o interpretaciones con las partes apropiadas de un texto.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna ulteriori attributi globali per associare specifiche analisi o interpretazioni alle adeguate porzioni di un testo.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">analysis</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">분석</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">análisis</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">analyse</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">analisi</gloss>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2019-06-08" xml:lang="ja">分析</gloss>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2006-01-05" xml:lang="en">indicates one or more elements containing interpretations of the
element on which the <att>ana</att> attribute appears.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><att>ana</att> 속성이 나오는 요소들의 해석을 포함하는 하나 혹은 그 이상의 요소들을 가리킨다.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出一個或多個元素，其中包含帶有屬性<att>ana</att>的元素解釋。</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性<att>ana</att>を伴う要素の解釈を含む要素を示す。</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique un ou plusieurs éléments contenant des
          interprétations de l'élément qui porte l'attribut <att>ana</att>.</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica uno o más elementos que contienen interpretaciones del elemento en el cual aparece el atributo <att>ana</att></desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica uno o più elementi che contengono interpretazioni dell'elemento specificato dall'attributo <att>ana</att></desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.global.analytic-attr.ana-remarks" versionDate="2006-01-05" xml:lang="en">
        <p>When multiple values are given, they may reflect either
multiple divergent interpretations of an ambiguous text, or multiple
mutually consistent interpretations of the same passage in different
contexts.</p>
      </remarks>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.global.analytic-attr.ana-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Quand on donne de multiples valeurs, celles-ci peuvent refléter, soit des
                        interprétations multiples et divergentes d'un texte ambigu soit des
                        interprétations multiples et compatibles du même passage dans différents
                        contextes.</p>
      </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.global.analytic-attr.ana-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        複数の属性値が付与される場合、各値は当該テキストの異なる解釈や、
        または同じ部分が異なる文脈でも同じ解釈であることを示す。
        </p>
      </remarks>
```

^b24

### Block 25

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AIATTS"/>
    <ptr target="#AISP"/>
  </listRef>
```

^b25

