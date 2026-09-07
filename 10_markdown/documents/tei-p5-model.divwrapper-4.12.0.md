---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.divwrapper-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.divWrapper
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.divWrapper.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.divWrapper

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1642. Git blob: `e9b8ebd781560a3b7cae51301bd26398c87ca55f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="DIVTOP" type="model" ident="model.divWrapper">
  <desc versionDate="2007-10-02" xml:lang="en">groups elements which can appear at either top or bottom of a
  textual division.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 구역 상단 또는 하단에 나타날 수 있는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集可出現於任何區段集元素起始或結尾的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の上部また下部に現れる要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui peuvent être placés au
      début ou à la fin de n'importe quelle division de texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que pueden aparecer al principio o al final de cualquier elemento de clase de división.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono all'inizio di una partizione testuale.</desc>
  <classes>
      <memberOf key="model.divBottom"/>
      
      <memberOf key="model.divTop"/>
  </classes>
  <listRef>
      <ptr target="#DSDTB"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-02" xml:lang="en">groups elements which can appear at either top or bottom of a
  textual division.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 구역 상단 또는 하단에 나타날 수 있는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集可出現於任何區段集元素起始或結尾的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の上部また下部に現れる要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui peuvent être placés au
      début ou à la fin de n'importe quelle division de texte.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que pueden aparecer al principio o al final de cualquier elemento de clase de división.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono all'inizio di una partizione testuale.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
      <memberOf key="model.divBottom"/>
      
      <memberOf key="model.divTop"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
      <ptr target="#DSDTB"/>
  </listRef>
```

^b9

