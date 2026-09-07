---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.titlepagepart-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.titlepagePart
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.titlepagePart.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.titlepagePart

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2165. Git blob: `f21c07c829c450d4e6072f8b7ad09a88f909f3af`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="TPPARTS" type="model" ident="model.titlepagePart">
  <desc versionDate="2007-12-15" xml:lang="en">groups elements which can occur as direct constituents of a title page, such as
    <gi>docTitle</gi>, <gi>docAuthor</gi>, <gi>docImprint</gi>, or <gi>epigraph</gi>.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><gi>docTitle</gi>, <gi>docAuthor</gi>,
    <gi>docImprint</gi>, 또는 <gi>epigraph</gi>와 같이 제목 페이지의 직접 구성성분으로 나타날 수 있는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素可成為標題頁的直接組成要素 (元素<gi>docTitle</gi>,
    <gi>docAuth</gi>, <gi>docImprint</gi>, <gi>epigraph</gi>等。)</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">タイトルページの構成要素となる要素をまとめる。例えば、要素 <gi>docTitle</gi>、
      <gi>docAuth</gi>、<gi>docImprint</gi>、<gi>epigraph</gi>など。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments qui peuvent apparaître comme
    constituants directs d'une page de titre (<gi>docTitle</gi>,
    <gi>docAuth</gi>, <gi>docImprint</gi> ou <gi>epigraph</gi>).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que aparecen como componentes
    directos del frontispicio electrónico (<gi>docTitle</gi>, <gi>docAuthor</gi>,
    <gi>docImprint</gi>, <gi>epigraph</gi>, etc.)</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono come componenti
    dirette del frontespizio elettronico (<gi>docTitle</gi>, <gi>docAuthor</gi>,
    <gi>docImprint</gi>, <gi>epigraph</gi>, ecc.)</desc>
  <listRef>
    <ptr target="#DSTITL"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-12-15" xml:lang="en">groups elements which can occur as direct constituents of a title page, such as
    <gi>docTitle</gi>, <gi>docAuthor</gi>, <gi>docImprint</gi>, or <gi>epigraph</gi>.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><gi>docTitle</gi>, <gi>docAuthor</gi>,
    <gi>docImprint</gi>, 또는 <gi>epigraph</gi>와 같이 제목 페이지의 직접 구성성분으로 나타날 수 있는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素可成為標題頁的直接組成要素 (元素<gi>docTitle</gi>,
    <gi>docAuth</gi>, <gi>docImprint</gi>, <gi>epigraph</gi>等。)</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">タイトルページの構成要素となる要素をまとめる。例えば、要素 <gi>docTitle</gi>、
      <gi>docAuth</gi>、<gi>docImprint</gi>、<gi>epigraph</gi>など。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments qui peuvent apparaître comme
    constituants directs d'une page de titre (<gi>docTitle</gi>,
    <gi>docAuth</gi>, <gi>docImprint</gi> ou <gi>epigraph</gi>).</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que aparecen como componentes
    directos del frontispicio electrónico (<gi>docTitle</gi>, <gi>docAuthor</gi>,
    <gi>docImprint</gi>, <gi>epigraph</gi>, etc.)</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che appaiono come componenti
    dirette del frontespizio elettronico (<gi>docTitle</gi>, <gi>docAuthor</gi>,
    <gi>docImprint</gi>, <gi>epigraph</gi>, ecc.)</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b8

