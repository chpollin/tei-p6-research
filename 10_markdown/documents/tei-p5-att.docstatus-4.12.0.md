---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.docstatus-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.docStatus
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.docStatus.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.docStatus

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2435. Git blob: `2163dd1b21af2bf59e4fc52e1a744d7b2332f3f8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-docStatus" ident="att.docStatus">
  <desc versionDate="2010-05-06" xml:lang="en">provides attributes for use on metadata elements
  describing the status of a document.</desc>
  <desc versionDate="2019-05-10" xml:lang="ja">文書のステータスを記述するメタデータ要素用の属性を提供する。</desc>
  <attList>
    <attDef ident="status">
      <desc versionDate="2010-05-06" xml:lang="en">describes the status of a document either currently or, when
associated with a dated element, at the time indicated.</desc>
      <desc versionDate="2019-05-10" xml:lang="ja">現在の、もしくは日時に関連づけられた要素にあっては、指定された時点における文書のステータスを記述する。</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>draft</defaultVal>
      <valList type="open">
        <valItem ident="approved"/>
        <valItem ident="candidate"/>
        <valItem ident="cleared"/>
        <valItem ident="deprecated"/>
        <valItem ident="draft"/>
        <valItem ident="embargoed"/>
        <valItem ident="expired"/>
        <valItem ident="frozen"/>
        <valItem ident="galley"/>
        <valItem ident="proposed"/>
        <valItem ident="published"/>
        <valItem ident="recommendation"/>
        <valItem ident="submitted"/>
        <valItem ident="unfinished"/>
        <valItem ident="withdrawn"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-docStatus-egXML-dj" source="#UND">
      <revisionDesc status="published">
        <change when="2010-10-21" status="published"/>
        <change when="2010-10-02" status="cleared"/>
        <change when="2010-08-02" status="embargoed"/>
        <change when="2010-05-01" status="frozen" who="#MSM"/>
        <change when="2010-03-01" status="draft" who="#LB"/>
      </revisionDesc>
    </egXML>
  </exemplum>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2010-05-06" xml:lang="en">provides attributes for use on metadata elements
  describing the status of a document.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-05-10" xml:lang="ja">文書のステータスを記述するメタデータ要素用の属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2010-05-06" xml:lang="en">describes the status of a document either currently or, when
associated with a dated element, at the time indicated.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2019-05-10" xml:lang="ja">現在の、もしくは日時に関連づけられた要素にあっては、指定された時点における文書のステータスを記述する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>draft</defaultVal>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="approved"/>
        <valItem ident="candidate"/>
        <valItem ident="cleared"/>
        <valItem ident="deprecated"/>
        <valItem ident="draft"/>
        <valItem ident="embargoed"/>
        <valItem ident="expired"/>
        <valItem ident="frozen"/>
        <valItem ident="galley"/>
        <valItem ident="proposed"/>
        <valItem ident="published"/>
        <valItem ident="recommendation"/>
        <valItem ident="submitted"/>
        <valItem ident="unfinished"/>
        <valItem ident="withdrawn"/>
      </valList>
```

^b7

### Block 8

XML location: `/classSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-docStatus-egXML-dj" source="#UND">
      <revisionDesc status="published">
        <change when="2010-10-21" status="published"/>
        <change when="2010-10-02" status="cleared"/>
        <change when="2010-08-02" status="embargoed"/>
        <change when="2010-05-01" status="frozen" who="#MSM"/>
        <change when="2010-03-01" status="draft" who="#LB"/>
      </revisionDesc>
    </egXML>
  </exemplum>
```

^b8

