---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.global.change-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.global.change
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.global.change.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.global.change

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1653. Git blob: `dfc247065fbd49b425bd0ff05130a7d4921d4ab9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" ident="att.global.change" predeclare="true" module="transcr" type="atts">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes allowing its member
elements to specify one or more states or revision campaigns with which they are
associated.</desc>
  <desc versionDate="2019-06-08" xml:lang="ja">そのメンバ要素が関連する1つ以上の状態または改定を指定できるように、<att>change</att>属性を提供する。</desc>
  <attList>
    <attDef ident="change">
      <desc versionDate="2011-10-31" xml:lang="en">points to one or more <gi>change</gi> elements documenting
      a state or revision campaign to which the element bearing this
      attribute and its children have been assigned by the encoder.</desc>
      <desc versionDate="2019-07-21" xml:lang="ja">この属性とその子を持つ要素が符号化する人によって割り当てられた状態または改定を記述する1つまたは複数の<gi>change</gi>要素を示す。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <!-- isotron rule need to check that we are pointing at <change>s -->
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes allowing its member
elements to specify one or more states or revision campaigns with which they are
associated.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-06-08" xml:lang="ja">そのメンバ要素が関連する1つ以上の状態または改定を指定できるように、<att>change</att>属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-10-31" xml:lang="en">points to one or more <gi>change</gi> elements documenting
      a state or revision campaign to which the element bearing this
      attribute and its children have been assigned by the encoder.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2019-07-21" xml:lang="ja">この属性とその子を持つ要素が符号化する人によって割り当てられた状態または改定を記述する1つまたは複数の<gi>change</gi>要素を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b5

