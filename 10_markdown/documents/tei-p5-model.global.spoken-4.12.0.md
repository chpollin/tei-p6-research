---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.global.spoken-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.global.spoken
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.global.spoken.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.global.spoken

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2267. Git blob: `a6095786a10d12ab669394520a693aa227147a63`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" type="model" ident="model.global.spoken" predeclare="true">
  <desc versionDate="2007-10-07" xml:lang="en">groups  elements
which may appear globally within spoken texts.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 전체에 나타날 수 있는 요소들을 모아 놓는다.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話テキスト内のどこにでも使える要素をまとめる。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">regroupe des éléments qui peuvent apparaître
généralement dans des textes oraux.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">comprende gli elementi a livello di componente specifici dei testi parlati.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que aparecen a nivel de componente específicamente en los textos dialogados.</desc>
  <classes>
    
    <memberOf key="model.global"/>
  </classes>
  <remarks ident="model.global.spoken-remarks" versionDate="2007-10-07" xml:lang="en">
    <p>This class groups elements which can appear anywhere within
    transcribed speech. </p>
  </remarks>
  <remarks ident="model.global.spoken-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe regroupe des éléments pouvant se situer n'importe où dans une
                transcription de la parole. </p>
  </remarks>
  <remarks ident="model.global.spoken-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase agrupa elementos que pueden aparecer dondequiera dentro del discurso transcrito. </p>
  </remarks>
  <remarks ident="model.global.spoken-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該クラスは、転記された発話内でどこにでも出現可能な要素をまとめる。
    </p>
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
<desc versionDate="2007-10-07" xml:lang="en">groups  elements
which may appear globally within spoken texts.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 전체에 나타날 수 있는 요소들을 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話テキスト内のどこにでも使える要素をまとめる。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">regroupe des éléments qui peuvent apparaître
généralement dans des textes oraux.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">comprende gli elementi a livello di componente specifici dei testi parlati.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que aparecen a nivel de componente específicamente en los textos dialogados.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.global"/>
  </classes>
```

^b7

### Block 8

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.global.spoken-remarks" versionDate="2007-10-07" xml:lang="en">
    <p>This class groups elements which can appear anywhere within
    transcribed speech. </p>
  </remarks>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.global.spoken-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe regroupe des éléments pouvant se situer n'importe où dans une
                transcription de la parole. </p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.global.spoken-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase agrupa elementos que pueden aparecer dondequiera dentro del discurso transcrito. </p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.global.spoken-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該クラスは、転記された発話内でどこにでも出現可能な要素をまとめる。
    </p>
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

