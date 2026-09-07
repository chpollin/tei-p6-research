---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.divpart.spoken-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.divPart.spoken
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.divPart.spoken.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.divPart.spoken

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2481. Git blob: `30e6926dacf0b210a61b1ced62d9899367e58e6b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" xml:id="COMPSPOK" type="model" ident="model.divPart.spoken" predeclare="true">
  <desc versionDate="2007-10-02" xml:lang="en">groups elements structurally analogous to paragraphs within spoken texts.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 내의 문단과 구조적으로 유사한 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">所匯集的元素僅出現在口說文件的組成層次。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話テキスト中にある、構造上段落と類似する要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments structurellement analogues aux
    paragraphes dans des textes contenant de la parole transcrite.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que aparecen a nivel de componente
    específicamente en los textos dialogados.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">comprende gli elementi a livello di componente specifici
    dei testi parlati</desc>
  <classes>
      
      <memberOf key="model.divPart"/>
  </classes>
  <remarks ident="model.divPart.spoken-remarks" versionDate="2007-10-02" xml:lang="en">
      <p>Spoken texts may be structured in many ways; elements in this class are typically larger
      units such as turns or utterances. </p>
  </remarks>
  <remarks ident="model.divPart.spoken-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Les textes contenant de la parole transcrite peuvent être structurés de plusieurs façons; les
      éléments de cette classe sont habituellement des unités plus grandes, comme des tournures ou
      des énoncés. </p>
  </remarks>
  <remarks ident="model.divPart.spoken-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 発話テキストは、様々に構造化される。当該クラスの要素は、一般に発話 の順番といった大きめの単位とされる。 </p>
  </remarks>
  <listRef>
      <ptr target="#TSOV"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-02" xml:lang="en">groups elements structurally analogous to paragraphs within spoken texts.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 내의 문단과 구조적으로 유사한 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所匯集的元素僅出現在口說文件的組成層次。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話テキスト中にある、構造上段落と類似する要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments structurellement analogues aux
    paragraphes dans des textes contenant de la parole transcrite.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que aparecen a nivel de componente
    específicamente en los textos dialogados.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">comprende gli elementi a livello di componente specifici
    dei testi parlati</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
      
      <memberOf key="model.divPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.divPart.spoken-remarks" versionDate="2007-10-02" xml:lang="en">
      <p>Spoken texts may be structured in many ways; elements in this class are typically larger
      units such as turns or utterances. </p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.divPart.spoken-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Les textes contenant de la parole transcrite peuvent être structurés de plusieurs façons; les
      éléments de cette classe sont habituellement des unités plus grandes, comme des tournures ou
      des énoncés. </p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.divPart.spoken-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 発話テキストは、様々に構造化される。当該クラスの要素は、一般に発話 の順番といった大きめの単位とされる。 </p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
      <ptr target="#TSOV"/>
  </listRef>
```

^b12

