---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.interval-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.interval
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.interval.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.interval

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1414. Git blob: `6608b5097ac47d2b1b667eeb4c6fc0a988c159e4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.interval">
  <desc versionDate="2013-04-13" xml:lang="en">defines attribute values used to express an interval value.</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">間隔の値の表現に用いる属性値を定義する。</desc>
  <content>
      <alternate>
         <dataRef name="float"/>
         <valList>
            <valItem ident="regular"/>
            <valItem ident="irregular"/>
            <valItem ident="unknown"/>
         </valList>
      </alternate>
   </content>
  <remarks ident="teidata.interval-remarks" versionDate="2013-04-13" xml:lang="en">
      <p>Any value greater than zero or any one of the values
    <val>regular</val>, <val>irregular</val>, <val>unknown</val>.</p>
  </remarks>
  <remarks ident="teidata.interval-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>
      ゼロより大きな数値、あるいは<val>regular</val>、<val>irregular</val>、<val>unknown</val>のいずれかの値。
    </p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-13" xml:lang="en">defines attribute values used to express an interval value.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">間隔の値の表現に用いる属性値を定義する。</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <alternate>
         <dataRef name="float"/>
         <valList>
            <valItem ident="regular"/>
            <valItem ident="irregular"/>
            <valItem ident="unknown"/>
         </valList>
      </alternate>
   </content>
```

^b3

### Block 4

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.interval-remarks" versionDate="2013-04-13" xml:lang="en">
      <p>Any value greater than zero or any one of the values
    <val>regular</val>, <val>irregular</val>, <val>unknown</val>.</p>
  </remarks>
```

^b4

### Block 5

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.interval-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>
      ゼロより大きな数値、あるいは<val>regular</val>、<val>irregular</val>、<val>unknown</val>のいずれかの値。
    </p>
  </remarks>
```

^b5

