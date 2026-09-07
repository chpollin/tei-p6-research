---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.rdglike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.rdgLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.rdgLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.rdgLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2599. Git blob: `a5d515b388086d9268972ddbeccf788833399920`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" type="model" ident="model.rdgLike">
  <desc versionDate="2007-10-03" xml:lang="en">groups elements which contain a single reading, other than the lemma, within a textual
    variation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형 내에서 레마 외에 단일 독법을 포함하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">所匯集的元素包含在原文變異中除了主題之外的對應本。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト中の異なりにおいて、対象語ではなく、ひとつの解釈を示す要素を まとめる。</desc>
  <desc versionDate="2009-05-27" xml:lang="fr">regroupe des éléments qui contiennent une seule leçon,
    autre que le lemme, à l'intérieur d'une version du texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que contienen una única lectura, a
    excepción del lema, dentro de una variante textual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che contengono un'unica lettura,
    ad esclusione del lemma, entro una variante testuale</desc>
  <classes/>
  <remarks ident="model.rdgLike-remarks" versionDate="2006-10-14" xml:lang="en">
    <p>This class allows for variants of the <gi>rdg</gi> element to be easily created via TEI
      customizations.</p>
  </remarks>
  <remarks ident="model.rdgLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe permet de créer facilement des variantes de l'élément <gi>rdg</gi>, par le biais
      de personnalisations de la TEI.</p>
  </remarks>
  <remarks ident="model.rdgLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase permite que las variantes del elemento <gi>rdg</gi> se creen fácilmente mediante
      las personalizaciones particulares de TEI.</p>
  </remarks>
  <remarks ident="model.rdgLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該クラスは、TEIのカスタマイズ機能により簡単に作られる、各種の要 素<gi>rdg</gi>をとる。 </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups elements which contain a single reading, other than the lemma, within a textual
    variation.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형 내에서 레마 외에 단일 독법을 포함하는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所匯集的元素包含在原文變異中除了主題之外的對應本。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト中の異なりにおいて、対象語ではなく、ひとつの解釈を示す要素を まとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">regroupe des éléments qui contiennent une seule leçon,
    autre que le lemme, à l'intérieur d'une version du texte.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que contienen una única lectura, a
    excepción del lema, dentro de una variante textual.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che contengono un'unica lettura,
    ad esclusione del lemma, entro una variante testuale</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes/>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.rdgLike-remarks" versionDate="2006-10-14" xml:lang="en">
    <p>This class allows for variants of the <gi>rdg</gi> element to be easily created via TEI
      customizations.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.rdgLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe permet de créer facilement des variantes de l'élément <gi>rdg</gi>, par le biais
      de personnalisations de la TEI.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.rdgLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase permite que las variantes del elemento <gi>rdg</gi> se creen fácilmente mediante
      las personalizaciones particulares de TEI.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.rdgLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該クラスは、TEIのカスタマイズ機能により簡単に作られる、各種の要 素<gi>rdg</gi>をとる。 </p>
  </remarks>
```

^b12

### Block 13

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b13

