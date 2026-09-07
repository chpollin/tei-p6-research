---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.timed-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.timed
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.timed.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.timed

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6244. Git blob: `90da6d289e8caf867ca0c70dba0283cb7a3cce24`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="TIMED" type="atts" ident="att.timed">
  <desc versionDate="2007-10-02" xml:lang="en">provides attributes common to those elements which
  have a duration in time, expressed either absolutely or by reference
  to an alignment map.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">절대적 또는 배열 지도에 대한 참조에 의해 표현된 시간의 지속을 나타내는 요소들 사이에 공통적 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一組屬性，通用於帶有時間長度的元素，這些元素以絕對方式表明，或是參照到組序表。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">時間幅を持つ要素に共通する属性を示す。絶対的または関連図への参照で示
  される。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">fournit des attributs communs aux éléments qui
      expriment une durée dans le temps, soit de manière absolue, soit en se référant à une carte d'alignement.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona un conjunto de atributos comunes a los elementos que tienen una duración en el tiempo expresada en términs absolutos o por referencia a un esquema de alineamiento</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna un insieme di attributi comuni agli elementi che hanno una durata nel tempo espressa in termini assoluti o rispetto a uno schema di allineamento.</desc>
  <classes>
    
    <memberOf key="att.duration"/>
  </classes>
  <attList>
    <attDef ident="start" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">indicates the location within a temporal alignment at
      which this element begins.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 요소가 시작된 시간 배열 내의 위치를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出時間組序中此元素的起始位置。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">時間関連図上で、当該要素が始まることを示す時間点を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique dans un alignement temporel (un ordre chronologique) l'endroit où commence cet élément.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el punto en el ámbito de un alineamiento temporal en el cual comienza el elemento</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il punto nell'ambito di un allineamento temporale in cui comincia l'elemento.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.timed-attr.start-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>If no value is supplied, the element is assumed to follow
	the immediately preceding element at the same hierarchic
	level.</p>
      </remarks>
      <remarks ident="att.timed-attr.start-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Si aucune valeur n'est donnée, il est entendu que l'élément suit l'élément immédiatement précédent au même niveau hiérarchique.</p>
      </remarks>
      <remarks ident="att.timed-attr.start-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Si no se suministra ningún valor, el elemento es asumido para seguir el elemento inmediatament anterior en el mismo nivel jerárquico.</p>
      </remarks>
      <remarks ident="att.timed-attr.start-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	値がない場合は、当該要素は同じ構造レベル上の直前の要素の後に続
	くものとされる。
	</p>
      </remarks>
    </attDef>
    <attDef ident="end" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">indicates the location within a temporal alignment at
      which this element ends.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 요소가 종료된 시간 배열 내의 위치를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出時間組序 (順序點) 中此元素的結尾位置。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">時間関連図上で、当該要素が終わることを示す時間点を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique l'endroit où se termine cet élément dans un alignement temporel.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el punto en el ámbito de un alineamiento temporal en el cual comienza el elemento</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il punto nell'ambito di un allineamento temporale in cui termina l'elemento.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.timed-attr.end-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>If no value is supplied, the element is assumed to precede
        the immediately following element at the same hierarchic
        level.</p>
      </remarks>
      <remarks ident="att.timed-attr.end-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si aucune valeur n'est donnée, il est entendu que l'élément précède l'élément immédiatement suivant au même niveau hiérarchique.</p>
      </remarks>
      <remarks ident="att.timed-attr.end-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Si no se suministra ningún valor, el elemento es asumido para preceder el elemento inmediatamente posterior en el mismo nivel jerárquico.</p>
      </remarks>
      <remarks ident="att.timed-attr.end-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	値がない場合は、当該要素は同じ構造レベル上の直前の要素の後に続
	くものとされる。
	</p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#TSBATI"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-02" xml:lang="en">provides attributes common to those elements which
  have a duration in time, expressed either absolutely or by reference
  to an alignment map.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">절대적 또는 배열 지도에 대한 참조에 의해 표현된 시간의 지속을 나타내는 요소들 사이에 공통적 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一組屬性，通用於帶有時間長度的元素，這些元素以絕對方式表明，或是參照到組序表。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間幅を持つ要素に共通する属性を示す。絶対的または関連図への参照で示
  される。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">fournit des attributs communs aux éléments qui
      expriment une durée dans le temps, soit de manière absolue, soit en se référant à une carte d'alignement.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un conjunto de atributos comunes a los elementos que tienen una duración en el tiempo expresada en términs absolutos o por referencia a un esquema de alineamiento</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un insieme di attributi comuni agli elementi che hanno una durata nel tempo espressa in termini assoluti o rispetto a uno schema di allineamento.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="att.duration"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates the location within a temporal alignment at
      which this element begins.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 요소가 시작된 시간 배열 내의 위치를 제시한다.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出時間組序中此元素的起始位置。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間関連図上で、当該要素が始まることを示す時間点を示す。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique dans un alignement temporel (un ordre chronologique) l'endroit où commence cet élément.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el punto en el ámbito de un alineamiento temporal en el cual comienza el elemento</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il punto nell'ambito di un allineamento temporale in cui comincia l'elemento.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.timed-attr.start-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>If no value is supplied, the element is assumed to follow
	the immediately preceding element at the same hierarchic
	level.</p>
      </remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.timed-attr.start-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Si aucune valeur n'est donnée, il est entendu que l'élément suit l'élément immédiatement précédent au même niveau hiérarchique.</p>
      </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.timed-attr.start-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Si no se suministra ningún valor, el elemento es asumido para seguir el elemento inmediatament anterior en el mismo nivel jerárquico.</p>
      </remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="att.timed-attr.start-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	値がない場合は、当該要素は同じ構造レベル上の直前の要素の後に続
	くものとされる。
	</p>
      </remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates the location within a temporal alignment at
      which this element ends.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 요소가 종료된 시간 배열 내의 위치를 제시한다.</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出時間組序 (順序點) 中此元素的結尾位置。</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間関連図上で、当該要素が終わることを示す時間点を示す。</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique l'endroit où se termine cet élément dans un alignement temporel.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el punto en el ámbito de un alineamiento temporal en el cual comienza el elemento</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il punto nell'ambito di un allineamento temporale in cui termina l'elemento.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.timed-attr.end-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>If no value is supplied, the element is assumed to precede
        the immediately following element at the same hierarchic
        level.</p>
      </remarks>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="att.timed-attr.end-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si aucune valeur n'est donnée, il est entendu que l'élément précède l'élément immédiatement suivant au même niveau hiérarchique.</p>
      </remarks>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="att.timed-attr.end-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Si no se suministra ningún valor, el elemento es asumido para preceder el elemento inmediatamente posterior en el mismo nivel jerárquico.</p>
      </remarks>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="att.timed-attr.end-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	値がない場合は、当該要素は同じ構造レベル上の直前の要素の後に続
	くものとされる。
	</p>
      </remarks>
```

^b32

### Block 33

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSBATI"/>
  </listRef>
```

^b33

