---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.milestonelike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.milestoneLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.milestoneLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.milestoneLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1590. Git blob: `e5e9606bf0eba1f5e3f1fad52137d0dd052d9112`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="REFSYS" type="model" ident="model.milestoneLike">
  <desc versionDate="2007-10-18" xml:lang="en">groups milestone-style
elements used to represent reference systems.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">참조 체계를 표상하는 이정표 유형의 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集用於呈現參照系統的類似分界點元素</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">参照システムを示すための、標石要素相当の要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments de type borne utilisés pour
      représenter des systèmes de référence.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos del tipo frontera (milestone) utilizados para representar sistemas de referencia.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi del tipo milestone utilizzati per rappresentare sistemi di riferimento.</desc>
  <classes>
    
    <memberOf key="model.global"/>
  </classes>
  <listRef>
    <ptr target="#STEC"/>
    <ptr target="#CORS5"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">groups milestone-style
elements used to represent reference systems.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참조 체계를 표상하는 이정표 유형의 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集用於呈現參照系統的類似分界點元素</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">参照システムを示すための、標石要素相当の要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments de type borne utilisés pour
      représenter des systèmes de référence.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos del tipo frontera (milestone) utilizados para representar sistemas de referencia.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi del tipo milestone utilizzati per rappresentare sistemi di riferimento.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.global"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
    <ptr target="#CORS5"/>
  </listRef>
```

^b9

