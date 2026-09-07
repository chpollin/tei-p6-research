---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.media-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.media
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.media.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.media

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2096. Git blob: `79fbf2b8e81a6fbfcea8d93a09632a0de037bc32`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.media">
  <desc versionDate="2013-01-11" xml:lang="en">provides attributes for specifying display and related properties of
  external media.</desc>
    <desc versionDate="2022-05-12" xml:lang="ja">外部メディアの表示と関連プロパティを指定するための諸属性を提供する。</desc>
  <classes>
    
    <memberOf key="att.internetMedia"/>
  </classes>
  <attList>
    <attDef ident="width" usage="opt">
      <desc versionDate="2013-01-10" xml:lang="en">Where the media are displayed, indicates the display width.</desc>
      <desc versionDate="2022-05-12" xml:lang="ja">メディアが表示されている場合、表示部分の幅を示す。</desc>
      <datatype><dataRef key="teidata.outputMeasurement"/></datatype>
    </attDef>
    <attDef ident="height" usage="opt">
      <desc versionDate="2013-01-10" xml:lang="en">Where the media are displayed, indicates the display height.</desc>
      <desc versionDate="2022-05-12" xml:lang="ja">メディアが表示されている場合、表示部分の高さを示す。</desc>
      <datatype><dataRef key="teidata.outputMeasurement"/></datatype>
    </attDef>
    <attDef ident="scale" usage="opt">
      <desc versionDate="2013-01-10" xml:lang="en">Where the media are displayed, indicates a scale factor to
      be applied when generating the desired display size.</desc>
      <desc versionDate="2022-05-12" xml:lang="ja">メディアが表示されている場合、望ましい表示サイズを生成する際に適用されるスケール倍率を示す。</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-01-11" xml:lang="en">provides attributes for specifying display and related properties of
  external media.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2022-05-12" xml:lang="ja">外部メディアの表示と関連プロパティを指定するための諸属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="att.internetMedia"/>
  </classes>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-01-10" xml:lang="en">Where the media are displayed, indicates the display width.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2022-05-12" xml:lang="ja">メディアが表示されている場合、表示部分の幅を示す。</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.outputMeasurement"/></datatype>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-01-10" xml:lang="en">Where the media are displayed, indicates the display height.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2022-05-12" xml:lang="ja">メディアが表示されている場合、表示部分の高さを示す。</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.outputMeasurement"/></datatype>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2013-01-10" xml:lang="en">Where the media are displayed, indicates a scale factor to
      be applied when generating the desired display size.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2022-05-12" xml:lang="ja">メディアが表示されている場合、望ましい表示サイズを生成する際に適用されるスケール倍率を示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b12

