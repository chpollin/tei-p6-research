---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.divbottom-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.divBottom
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.divBottom.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.divBottom

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1718. Git blob: `45ccdefce6990835570152f9f1f97ff48ddf8746`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="DIVBOT" type="model" ident="model.divBottom">
  <desc versionDate="2007-10-02" xml:lang="en">groups elements appearing at the end of a text
    division<!--(e.g., a <gi>trailer</gi>) with those that can occur either
  at the beginning or the end (e.g., a <gi>byline</gi>)-->.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 구역의 종료부에 나타타는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集僅可出現於文本區段結尾的元素，例如結尾題名。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストの終わりに現れる要素をまとめる。
    <!--(e.g., a <gi>trailer</gi>) with those that can occur either
  at the beginning or the end (e.g., a <gi>byline</gi>)--></desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments placés à la fin d'une division de
    texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que pueden aparecer sólo al final de una
    división textual, p.ej. un tráiler.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono alla fine di una
    partizione testuale, per esempio trailer, byline, ecc.</desc>
  <listRef>
    <ptr target="#DSDTB"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-02" xml:lang="en">groups elements appearing at the end of a text
    division<!--(e.g., a <gi>trailer</gi>) with those that can occur either
  at the beginning or the end (e.g., a <gi>byline</gi>)-->.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 구역의 종료부에 나타타는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集僅可出現於文本區段結尾的元素，例如結尾題名。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストの終わりに現れる要素をまとめる。
    <!--(e.g., a <gi>trailer</gi>) with those that can occur either
  at the beginning or the end (e.g., a <gi>byline</gi>)--></desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments placés à la fin d'une division de
    texte.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que pueden aparecer sólo al final de una
    división textual, p.ej. un tráiler.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono alla fine di una
    partizione testuale, per esempio trailer, byline, ecc.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSDTB"/>
  </listRef>
```

^b8

