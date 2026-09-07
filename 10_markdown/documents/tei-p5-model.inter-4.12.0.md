---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.inter-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.inter
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.inter.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.inter

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2686. Git blob: `0d923fe6187a93e533dd57391ecd88990fcdced0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="INTER" type="model" ident="model.inter">
  <desc versionDate="2007-10-03" xml:lang="en">groups elements which can appear either within or between paragraph-like elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문단 같은 요소 내에서 또는 그 사이에서 나타날 수 있는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集中間層次的元素：可出現於段落內與段落之間，或方塊性層次內與層次間。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">句相当レベルの要素内または間に出現可能な要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui peuvent apparaître à l’intérieur ou entre des composants semblables au paragraphe.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos de la clase intermedia (internivel):
    tales elementos pueden aparecer bien al interno bien entre párrafos u entre otros elementos de
    tipo división de texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi della classe intermedia
    (interlivello): tali elementi possono apparire sia all'interno che tra paragrafi e altri
    elementi del tipo porzione di testo</desc>
  <classes>
    <memberOf key="model.common"/>
    
    <memberOf key="model.paraPart"/>
  </classes>
  <!--
  <remarks>
    <p>This element class contains a subset of those elements which
can appear in the unstructured <soCalled>soup</soCalled> with which
paragraph and other elements at the lowest level of crystal structures
are filled:  specifically all the elements which can also occur as
structural elements in their own right.  In prose, this means the
elements in this class can appear both within and between paragraphs.
This class is thus distinct from the purely phrase-level elements which
can appear only within soup, and not on their own; the latter class, in
keeping with this metaphor, is called <soCalled>broth</soCalled>; it
is represented by the class <term>phrase</term>.  Cf. also the
class <term>chunks</term>.</p>
  </remarks>
  -->
  <!-- preceding comment kept for reasons of historical piety -->
  <listRef>
    <ptr target="#STEC"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups elements which can appear either within or between paragraph-like elements.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문단 같은 요소 내에서 또는 그 사이에서 나타날 수 있는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集中間層次的元素：可出現於段落內與段落之間，或方塊性層次內與層次間。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">句相当レベルの要素内または間に出現可能な要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui peuvent apparaître à l’intérieur ou entre des composants semblables au paragraphe.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos de la clase intermedia (internivel):
    tales elementos pueden aparecer bien al interno bien entre párrafos u entre otros elementos de
    tipo división de texto.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi della classe intermedia
    (interlivello): tali elementi possono apparire sia all'interno che tra paragrafi e altri
    elementi del tipo porzione di testo</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="model.common"/>
    
    <memberOf key="model.paraPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
  </listRef>
```

^b9

