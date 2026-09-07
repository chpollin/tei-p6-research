---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.performed-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.performed
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.performed.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.performed

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2519. Git blob: `0251a410365863ba2557c428fa0240bb65790da4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" 
  type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" type="atts" ident="att.performed">
  <desc versionDate="2026-03-03" xml:lang="en">provides attributes to specify performance-based information.</desc>
  <attList>
    <attDef ident="perf" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">performance</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">연기</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">función</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">jeu</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">rappresentazione</gloss>
      <desc versionDate="2026-03-03" xml:lang="en">identifies the performance or performances in which this element occurred.</desc>
      <!--JT (2026-03-03): These descs are from the performance attribute formerly
        defined on move. They are likely close to correct, but will need to be fixed slightly-->
      <desc versionDate="2007-12-20" xml:lang="ko">명시된 대로 이동할 때의 연기를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明這項舞台動作出現在哪些演出中。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">identifica la puesta en escena en la cual este movimiento se produjo según lo especificado.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該動きの演技を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">identifie la ou les représentations au cours desquelles s'est effectué le déplacement décrit.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la rappresentazione o le rappresentazioni in cui il movimento è stato eseguito così come specificato.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks versionDate="2026-07-05"
        ident="att.performed-attr.perf-remarks" xml:lang="en">
        <p>The <att>perf</att> attribute contains one or more pointers to a canonical description of the performance, typically described by a <gi>performance</gi> or <gi>event</gi> element.</p>
      </remarks>
    </attDef>
  </attList>
</classSpec>

```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2026-03-03" xml:lang="en">provides attributes to specify performance-based information.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">performance</gloss>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">연기</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">función</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">jeu</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">rappresentazione</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2026-03-03" xml:lang="en">identifies the performance or performances in which this element occurred.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">명시된 대로 이동할 때의 연기를 명시한다.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明這項舞台動作出現在哪些演出中。</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">identifica la puesta en escena en la cual este movimiento se produjo según lo especificado.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該動きの演技を示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">identifie la ou les représentations au cours desquelles s'est effectué le déplacement décrit.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la rappresentazione o le rappresentazioni in cui il movimento è stato eseguito così come specificato.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks versionDate="2026-07-05"
        ident="att.performed-attr.perf-remarks" xml:lang="en">
        <p>The <att>perf</att> attribute contains one or more pointers to a canonical description of the performance, typically described by a <gi>performance</gi> or <gi>event</gi> element.</p>
      </remarks>
```

^b15

