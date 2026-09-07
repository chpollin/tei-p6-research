---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.emphlike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.emphLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.emphLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.emphLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1664. Git blob: `b2946108edc97566a68ba0ce34726c300a5cf60f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="model" ident="model.emphLike">
  <desc versionDate="2007-10-03" xml:lang="en">groups phrase-level elements which are typographically
  distinct and to which a specific function can be attributed.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">인쇄상 구분되며 특정 기능을 수행하는 구-층위 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集語義上的詞組層次元素</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">印刷上他とは異なり、特定の機能が付与されている、句レベルの要素をまと
  める。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui sont distingués visuellement, et auxquels on peut attribuer une signification  sémantique.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi a livello di sintagma tipograficamente distinti e ai quali è attribuibile una funzione specifica.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos sintagmáticos semánticos.</desc>
  <classes>
      
      <memberOf key="model.highlighted"/>
      <memberOf key="model.limitedPhrase"/>
  </classes>
  <listRef>
      <ptr target="#COHQ"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups phrase-level elements which are typographically
  distinct and to which a specific function can be attributed.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인쇄상 구분되며 특정 기능을 수행하는 구-층위 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集語義上的詞組層次元素</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">印刷上他とは異なり、特定の機能が付与されている、句レベルの要素をまと
  める。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui sont distingués visuellement, et auxquels on peut attribuer une signification  sémantique.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi a livello di sintagma tipograficamente distinti e ai quali è attribuibile una funzione specifica.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos sintagmáticos semánticos.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
      
      <memberOf key="model.highlighted"/>
      <memberOf key="model.limitedPhrase"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
      <ptr target="#COHQ"/>
  </listRef>
```

^b9

