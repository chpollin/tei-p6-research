---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.spanning-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.spanning
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.spanning.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.spanning

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5589. Git blob: `5d5b441d935c79a1981c4d3f4ec8ff74f91cef31`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tei" type="atts" ident="att.spanning">
  <desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements which delimit a span of text by pointing mechanisms rather than by enclosing it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">포함보다는 포인터 메카니즘을 통하여 구분된 텍스트 구간을 나타내는 요소의 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素的屬性，這些元素使用參照機制來限定某一文字段，而非包含此文字段。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト幅の範囲を内容としてではなく参照機能を使って示す要素に付与される属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour les éléments qui délimitent un passage de texte par des mécanismes de pointage plutôt qu'en entourant le passage.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para elementos que delimitan un fragmento de texto utilizando los señalizadores en lugar de cerrando el texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi che delimitano una porzione di testo utilizzando dei puntatori invece di racchiudere il testo stesso.</desc>
  <attList>
    <attDef ident="spanTo" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">indicates the end of a span initiated by the element bearing this attribute.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 속성을 포함하는 요소에 의해 시작된 구간의 끝을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出文字段的結尾，該文字段以帶有此屬性的元素開頭。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素が示す範囲の終点を示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">indique la fin d'un passage introduit par l'élément portant cet attribut.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el final de un fragmento de texto iniciado con el elemento al cual es asignaado el atributo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la fine della porzione di testo che ha inizio con l'elemento a cui è assegnato l'attributo.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <constraintSpec ident="spanTo-points-to-following" scheme="schematron" xml:lang="en">
        <desc versionDate="2025-01-19" xml:lang="en">The @spanTo attribute must point to an element following the current element; however, this can only be tested if both this element and the one pointed to are in the same document.</desc>
        <constraint>
          <sch:rule context="tei:*[ starts-with( @spanTo, '#') ]">
            <sch:assert test="id( substring( @spanTo, 2 ) ) &gt;&gt; .">
              The element indicated by @spanTo (<sch:value-of select="@spanTo"/>) must follow the current &lt;<sch:name/>&gt; element.
            </sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </attDef>
  </attList>
  <remarks ident="att.spanning-remarks" versionDate="2012-10-29" xml:lang="en">
    <p>The span is defined as running in document order from the start
    of the content of the pointing element to the end of the
    content of the element pointed to by the <att>spanTo</att> attribute (if
    any). If no value is supplied for the attribute, the assumption is that the span is
    coextensive with the pointing element. If no content is present,
    the assumption is that the starting point of the span is
    immediately following the element itself.</p>
  </remarks>
  <remarks ident="att.spanning-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le passage est défini comme courant depuis le début du contenu de l'élément pointeur (s'il y en a un) jusqu'à la fin du contenu de l'élément
      pointé par l'attribut <att>spanTo</att> (s'il y en a un), dans l'ordre du document. Si aucune valeur n'est fournie pour l'attribut, il est entendu
      que le passage est de même étendue que l'élément pointeur.</p>
  </remarks>
  <remarks ident="att.spanning-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El span se define como ejecutándose en la orden del documento des del comienzo del contenido del elemento indicado (si lo hay) al extremo del contenido del elemento señalado por el atributo del spanTo (si lo hay).
    Si no se suministra ningún valor para el atributo, la asunción es que el span es coextensivo con el elemento indicado.</p>
  </remarks>
  <remarks ident="att.spanning-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該範囲は、当該文書中にある、(もしあれば)参照要素の内容の始点から、
    (もしあれば)属性spanToで示された要素の内容の終点までになる。
    当該属性に値がない場合、当該範囲は、当該参照要素と同じ範囲と想定す
    る。
    </p>
  </remarks>
  <listRef>
    <ptr target="#PHAD"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements which delimit a span of text by pointing mechanisms rather than by enclosing it.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">포함보다는 포인터 메카니즘을 통하여 구분된 텍스트 구간을 나타내는 요소의 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素的屬性，這些元素使用參照機制來限定某一文字段，而非包含此文字段。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト幅の範囲を内容としてではなく参照機能を使って示す要素に付与される属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour les éléments qui délimitent un passage de texte par des mécanismes de pointage plutôt qu'en entourant le passage.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para elementos que delimitan un fragmento de texto utilizando los señalizadores en lugar de cerrando el texto.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi che delimitano una porzione di testo utilizzando dei puntatori invece di racchiudere il testo stesso.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates the end of a span initiated by the element bearing this attribute.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 속성을 포함하는 요소에 의해 시작된 구간의 끝을 나타낸다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出文字段的結尾，該文字段以帶有此屬性的元素開頭。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素が示す範囲の終点を示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">indique la fin d'un passage introduit par l'élément portant cet attribut.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el final de un fragmento de texto iniciado con el elemento al cual es asignaado el atributo.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la fine della porzione di testo che ha inizio con l'elemento a cui è assegnato l'attributo.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="spanTo-points-to-following" scheme="schematron" xml:lang="en">
        <desc versionDate="2025-01-19" xml:lang="en">The @spanTo attribute must point to an element following the current element; however, this can only be tested if both this element and the one pointed to are in the same document.</desc>
        <constraint>
          <sch:rule context="tei:*[ starts-with( @spanTo, '#') ]">
            <sch:assert test="id( substring( @spanTo, 2 ) ) &gt;&gt; .">
              The element indicated by @spanTo (<sch:value-of select="@spanTo"/>) must follow the current &lt;<sch:name/>&gt; element.
            </sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b16

### Block 17

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.spanning-remarks" versionDate="2012-10-29" xml:lang="en">
    <p>The span is defined as running in document order from the start
    of the content of the pointing element to the end of the
    content of the element pointed to by the <att>spanTo</att> attribute (if
    any). If no value is supplied for the attribute, the assumption is that the span is
    coextensive with the pointing element. If no content is present,
    the assumption is that the starting point of the span is
    immediately following the element itself.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.spanning-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le passage est défini comme courant depuis le début du contenu de l'élément pointeur (s'il y en a un) jusqu'à la fin du contenu de l'élément
      pointé par l'attribut <att>spanTo</att> (s'il y en a un), dans l'ordre du document. Si aucune valeur n'est fournie pour l'attribut, il est entendu
      que le passage est de même étendue que l'élément pointeur.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.spanning-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El span se define como ejecutándose en la orden del documento des del comienzo del contenido del elemento indicado (si lo hay) al extremo del contenido del elemento señalado por el atributo del spanTo (si lo hay).
    Si no se suministra ningún valor para el atributo, la asunción es que el span es coextensivo con el elemento indicado.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="att.spanning-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該範囲は、当該文書中にある、(もしあれば)参照要素の内容の始点から、
    (もしあれば)属性spanToで示された要素の内容の終点までになる。
    当該属性に値がない場合、当該範囲は、当該参照要素と同じ範囲と想定す
    る。
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHAD"/>
  </listRef>
```

^b21

