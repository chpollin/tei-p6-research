---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.phrase-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.phrase
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.phrase.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.phrase

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2523. Git blob: `c2f857824c317e6205379cda353fd0868899e7be`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="PHRASE" type="model" ident="model.phrase">
  <desc versionDate="2007-10-03" xml:lang="en">groups elements which can occur at the level of individual words or phrases.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개별 단어 또는 구 층위에서 나타날 수 있는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素可出現於個人字詞層次上。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">独立した語句レベルに出現する要素をまとめる。</desc>
  <desc versionDate="2009-10-06" xml:lang="fr">regroupe des éléments qui apparaissent au niveau des
    mots isolés ou des groupes de mots.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que pueden aparecer en el nivel de
    palabras o sintagmas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono a livello di singole
    parole o sintagmi</desc>
  <classes>
    
    <memberOf key="model.paraPart"/>
  </classes>
  <remarks ident="model.phrase-remarks" versionDate="2014-11-19" xml:lang="en">
    <p>This class of elements can occur within paragraphs, list items, lines of verse, etc.</p>
  </remarks>
  <remarks ident="model.phrase-remarks" versionDate="2014-11-19" xml:lang="fr">
    <p>Cette classe d'éléments peut se trouver dans des paragraphes, des entrées de
      listes, des vers, etc.</p>
  </remarks>
  <remarks ident="model.phrase-remarks" versionDate="2014-11-19" xml:lang="es">
    <p>Esta clase de elementos puede aparecer dentro de párrafos, en los elementos de una lista, en las líneas de verso, etc.</p>
  </remarks>
  <remarks ident="model.phrase-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素クラスは、クラス<term>inter</term>にある大きめの要素、すな わち<term>塊</term>の中で出現可能である。散文においては、当該要素
      は、段落、リスト項目、韻文行などの中で出現可能である。 </p>
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
<desc versionDate="2007-10-03" xml:lang="en">groups elements which can occur at the level of individual words or phrases.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개별 단어 또는 구 층위에서 나타날 수 있는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素可出現於個人字詞層次上。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">独立した語句レベルに出現する要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-10-06" xml:lang="fr">regroupe des éléments qui apparaissent au niveau des
    mots isolés ou des groupes de mots.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que pueden aparecer en el nivel de
    palabras o sintagmas.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono a livello di singole
    parole o sintagmi</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.paraPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.phrase-remarks" versionDate="2014-11-19" xml:lang="en">
    <p>This class of elements can occur within paragraphs, list items, lines of verse, etc.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.phrase-remarks" versionDate="2014-11-19" xml:lang="fr">
    <p>Cette classe d'éléments peut se trouver dans des paragraphes, des entrées de
      listes, des vers, etc.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.phrase-remarks" versionDate="2014-11-19" xml:lang="es">
    <p>Esta clase de elementos puede aparecer dentro de párrafos, en los elementos de una lista, en las líneas de verso, etc.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.phrase-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素クラスは、クラス<term>inter</term>にある大きめの要素、すな わち<term>塊</term>の中で出現可能である。散文においては、当該要素
      は、段落、リスト項目、韻文行などの中で出現可能である。 </p>
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

