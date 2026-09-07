---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.divpart-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.divPart
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.divPart.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.divPart

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2845. Git blob: `93f3e0da686193dc1e9bed37d7bd85f8f58e9c6a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="CHUNK" type="model" ident="model.divPart">
  <desc versionDate="2011-12-12" xml:lang="en">groups paragraph-level elements appearing directly within divisions.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구역 내에서 직접적으로 나타나는 문단-층위 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集可出現於段落與其他區塊之間，而非出現於兩者之內的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト部分中にある段落レベルの要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments de niveau paragraphe apparaissant
    directement dans des divisions.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que pueden aparecer entre párrafos u
    otras divisiones, pero no dentro de estos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi che compaiono tra paragrafi e altre
    porzioni di testo ma non al loro interno</desc>
  <classes>
    
    <memberOf key="model.common"/>
  </classes>
  <remarks ident="model.divPart-remarks" versionDate="2011-12-12" xml:lang="en">
    <p>Note that this element class does not include members of the <ident type="class">model.inter</ident> class, which can appear either within or between paragraph-level items.
    </p>
  </remarks>
  <remarks ident="model.divPart-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Noter que cette classe d'éléments ne comprend pas les membres de la classe <ident type="class">model.inter</ident>, qui peuvent apparaître soit à l'intérieur, soit entre des
      items de niveau paragraphe.</p>
  </remarks>
  <remarks ident="model.divPart-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Observa que esta clase de elemento no incluye a los miembros de la clase <ident type="class">model.inter</ident>, que puede aparecer dentro o entre los items del nivel-párrafo. </p>
  </remarks>
  <remarks ident="model.divPart-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素クラスは、クラス<ident type="class">model.inter</ident>の メンバーを含まないことに注意すること。 クラス<ident type="class">model.inter</ident>は、段落レベル項目内 または間にのみ出現可能である。 </p>
  </remarks>
  <listRef>
    <ptr target="#STEC"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-12-12" xml:lang="en">groups paragraph-level elements appearing directly within divisions.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구역 내에서 직접적으로 나타나는 문단-층위 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集可出現於段落與其他區塊之間，而非出現於兩者之內的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト部分中にある段落レベルの要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments de niveau paragraphe apparaissant
    directement dans des divisions.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que pueden aparecer entre párrafos u
    otras divisiones, pero no dentro de estos.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi che compaiono tra paragrafi e altre
    porzioni di testo ma non al loro interno</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.common"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.divPart-remarks" versionDate="2011-12-12" xml:lang="en">
    <p>Note that this element class does not include members of the <ident type="class">model.inter</ident> class, which can appear either within or between paragraph-level items.
    </p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.divPart-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Noter que cette classe d'éléments ne comprend pas les membres de la classe <ident type="class">model.inter</ident>, qui peuvent apparaître soit à l'intérieur, soit entre des
      items de niveau paragraphe.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.divPart-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Observa que esta clase de elemento no incluye a los miembros de la clase <ident type="class">model.inter</ident>, que puede aparecer dentro o entre los items del nivel-párrafo. </p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.divPart-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素クラスは、クラス<ident type="class">model.inter</ident>の メンバーを含まないことに注意すること。 クラス<ident type="class">model.inter</ident>は、段落レベル項目内 または間にのみ出現可能である。 </p>
  </remarks>
```

^b12

### Block 13

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
  </listRef>
```

^b13

