---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.ptrlike.form-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.ptrLike.form
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.ptrLike.form.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.ptrLike.form

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1792. Git blob: `6914381c874d93b22a4eeec6c0ac87cc84260e4b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" predeclare="true" module="dictionaries" type="model" ident="model.ptrLike.form">
  <desc versionDate="2007-10-03" xml:lang="en">groups elements used for purposes of location of particular orthographic or pronunciation
    forms within a dictionary entry.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전 표제 항목 내의 특정한 철자 또는 발음 형태의 위치를 지정하는 요소들을 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集該字典中的元素，這些元素指向標題字的拼字或發音形式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書項目内で、特定の正書法や発音形式の場所を示す要素をまとめる。</desc>
  <desc versionDate="2009-10-06" xml:lang="fr">regroupe des éléments utilisés pour localiser
    des formes orthographiques ou phonétiques particulières dans une entrée de dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos de la base del diccionario que
    indican las forma ortográfica o la pronunciación del lema.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">in un dizionario raggruppa gli elementi che indirizzano a
    frome ortografiche o pronuncie di un lemma.</desc>
  <classes>
    
    <memberOf key="model.phrase"/>
  </classes>
  <listRef>
    <ptr target="#DI"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups elements used for purposes of location of particular orthographic or pronunciation
    forms within a dictionary entry.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전 표제 항목 내의 특정한 철자 또는 발음 형태의 위치를 지정하는 요소들을 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集該字典中的元素，這些元素指向標題字的拼字或發音形式。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書項目内で、特定の正書法や発音形式の場所を示す要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-10-06" xml:lang="fr">regroupe des éléments utilisés pour localiser
    des formes orthographiques ou phonétiques particulières dans une entrée de dictionnaire.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos de la base del diccionario que
    indican las forma ortográfica o la pronunciación del lema.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">in un dizionario raggruppa gli elementi che indirizzano a
    frome ortografiche o pronuncie di un lemma.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.phrase"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DI"/>
  </listRef>
```

^b9

