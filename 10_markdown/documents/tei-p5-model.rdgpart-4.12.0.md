---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.rdgpart-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.rdgPart
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.rdgPart.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.rdgPart

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2394. Git blob: `5ca16fe3192fe2851864cc730d68f83706d6173c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="FRAGMENT" type="model" ident="model.rdgPart">
  <desc versionDate="2005-10-10" xml:lang="en">groups elements which mark the beginning or ending of a fragmentary manuscript or other
    witness.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">파편화된 원고 또는 다른 비교 대상 텍스트의 시작부 또는 종료부를 표지하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">所匯集的元素標記出零散手稿的起始或結尾，或其他版本。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料や文献の断片の、始まりや終わりを示す要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui marquent le début ou la fin
    d'un manuscrit fragmentaire ou d'un autre témoin.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que señalan el inicio o el final de
    un manuscrito fragmentario o de otro testimonio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che segnalano l'inizio o la fine
    di un manoscritto frammentario o di altro testimone</desc>
  <remarks ident="model.rdgPart-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>These elements may appear anywhere within the elements <gi>lem</gi> and <gi>rdg</gi>, and
      also within any of their constituent elements. </p>
  </remarks>
  <remarks ident="model.rdgPart-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Ces éléments peuvent figurer n'importe où à l'intérieur des éléments <gi>lem</gi> et
      <gi>rdg</gi> ou dans tout élément qui les compose.</p>
  </remarks>
  <remarks ident="model.rdgPart-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、要素<gi>lem</gi>や<gi>rdg</gi>、自身の構成要素の内部で、 自由に出現できる。 </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">groups elements which mark the beginning or ending of a fragmentary manuscript or other
    witness.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">파편화된 원고 또는 다른 비교 대상 텍스트의 시작부 또는 종료부를 표지하는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所匯集的元素標記出零散手稿的起始或結尾，或其他版本。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料や文献の断片の、始まりや終わりを示す要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui marquent le début ou la fin
    d'un manuscrit fragmentaire ou d'un autre témoin.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que señalan el inicio o el final de
    un manuscrito fragmentario o de otro testimonio.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che segnalano l'inizio o la fine
    di un manoscritto frammentario o di altro testimone</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.rdgPart-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>These elements may appear anywhere within the elements <gi>lem</gi> and <gi>rdg</gi>, and
      also within any of their constituent elements. </p>
  </remarks>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.rdgPart-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Ces éléments peuvent figurer n'importe où à l'intérieur des éléments <gi>lem</gi> et
      <gi>rdg</gi> ou dans tout élément qui les compose.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.rdgPart-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、要素<gi>lem</gi>や<gi>rdg</gi>、自身の構成要素の内部で、 自由に出現できる。 </p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
```

^b11

