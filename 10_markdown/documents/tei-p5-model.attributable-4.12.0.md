---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.attributable-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.attributable
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.attributable.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.attributable

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2079. Git blob: `7090b4ab8dcded8502df8afcc5e744eee2638e1e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="HQINTER" type="model" ident="model.attributable">
  <desc versionDate="2020-08-05" xml:lang="en">groups elements that contain a word or phrase that can be attributed to a source.</desc>
  <desc versionDate="2020-08-14" xml:lang="de">gruppiert Elemente, die ein Wort oder eine Phrase enthalten, welche einer Quelle zugeschrieben werden können.</desc>
 <!--2020-07-04 ebeshero: These translations apply to the old model.qLike and need to be updated.
  <desc versionDate="2007-12-20" xml:lang="ko">덩어리 층위 요소 내에서 또는 그 사이에서 나타날 수 있는 주요 부분과 관련된 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集和顯目標示相關、且出現於方塊性層次元素內或之間的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">塊レベル要素内または間で出現可能な，強調部分と関連する要素をまとめる．</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments destinés à la mise en valeur, qui
    peuvent apparaître à l'intérieur ou entre des éléments de niveau fragment.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos relativos al evidenciado que aparece al
    interno de o entre elementos a nivel de fragmentos de texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi relativi all'evidenziatura che
    appaiono all'interno di o tra elementi a livello di porzioni di testo</desc>
 -->
  <classes>
    
    <memberOf key="model.inter"/>
  </classes>
  <listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#DSFLT"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-08-05" xml:lang="en">groups elements that contain a word or phrase that can be attributed to a source.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2020-08-14" xml:lang="de">gruppiert Elemente, die ein Wort oder eine Phrase enthalten, welche einer Quelle zugeschrieben werden können.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.inter"/>
  </classes>
```

^b3

### Block 4

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#DSFLT"/>
  </listRef>
```

^b4

