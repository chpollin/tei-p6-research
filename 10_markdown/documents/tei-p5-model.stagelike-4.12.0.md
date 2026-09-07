---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.stagelike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.stageLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.stageLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.stageLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2967. Git blob: `162a2a4f41b8ac142a778b71577da05914090a27`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="STAGEDIR" type="model" ident="model.stageLike">
  <desc versionDate="2007-08-29" xml:lang="en">groups elements containing stage directions or similar things defined by the module for
    performance texts.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">공연 텍스트의 모듈에 의해 정의된 무대 지시 또는 유사 내용을 포함하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素包含特殊的舞台指示，定義於劇本的附加標籤組中。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">舞台芸術モジュールで定義されている、ト書きなどを示す要素をまとめる。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments contenant des indications scéniques
    ou des indications de même nature, définies par le module relatif aux textes de théâtre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">aggrupa elementos que contienen indicaciones específicas
    de escena definidas en el conjunto adicional de marcadores de textos teatrales.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi che contengono specifiche indicazioni
    di scena definite nell'insieme aggiuntivo di marcatori per testi teatrali</desc>
  <classes>
    
    <!--    <memberOf key="model.common"/>-->
    <memberOf key="model.inter"/>
  </classes>
  <remarks ident="model.stageLike-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>Stage directions are members of class <term>inter</term>: that is, they can appear between or
      within component-level elements.</p>
  </remarks>
  <remarks ident="model.stageLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les indications scéniques appartiennent à la classe <term>inter</term> : cela signifie
      qu'elles peuvent apparaître  à l'intérieur d'éléments de niveau composant  ou bien entre ces éléments.</p>
  </remarks>
  <remarks ident="model.stageLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Las direcciones de etapa son miembros de la clase <term>inter</term>: es decir, pueden
      aparecer entre o dentro de los elementos del componente-nivel.</p>
  </remarks>
  <remarks ident="model.stageLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> ト書きは、クラス<term>inter</term>のメンバーである。すなわち、構成 要素レベル要素内または間で出現可能である。 </p>
  </remarks>
  <listRef>
    <ptr target="#DROTH"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-08-29" xml:lang="en">groups elements containing stage directions or similar things defined by the module for
    performance texts.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">공연 텍스트의 모듈에 의해 정의된 무대 지시 또는 유사 내용을 포함하는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素包含特殊的舞台指示，定義於劇本的附加標籤組中。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">舞台芸術モジュールで定義されている、ト書きなどを示す要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments contenant des indications scéniques
    ou des indications de même nature, définies par le module relatif aux textes de théâtre.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">aggrupa elementos que contienen indicaciones específicas
    de escena definidas en el conjunto adicional de marcadores de textos teatrales.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi che contengono specifiche indicazioni
    di scena definite nell'insieme aggiuntivo di marcatori per testi teatrali</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <!--    <memberOf key="model.common"/>-->
    <memberOf key="model.inter"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.stageLike-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>Stage directions are members of class <term>inter</term>: that is, they can appear between or
      within component-level elements.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.stageLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les indications scéniques appartiennent à la classe <term>inter</term> : cela signifie
      qu'elles peuvent apparaître  à l'intérieur d'éléments de niveau composant  ou bien entre ces éléments.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.stageLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Las direcciones de etapa son miembros de la clase <term>inter</term>: es decir, pueden
      aparecer entre o dentro de los elementos del componente-nivel.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.stageLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> ト書きは、クラス<term>inter</term>のメンバーである。すなわち、構成 要素レベル要素内または間で出現可能である。 </p>
  </remarks>
```

^b12

### Block 13

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DROTH"/>
  </listRef>
```

^b13

