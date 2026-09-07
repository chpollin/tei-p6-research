---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.resourced-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.resourced
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.resourced.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.resourced

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1664. Git blob: `063cfa695df7ab453cb64f53f44d10c2f9abf782`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.resourced">
  <desc versionDate="2013-01-11" xml:lang="en">provides attributes by which a resource (such as an externally
  held media file) may be located.</desc>
  <desc versionDate="2023-09-27" xml:lang="ja">（外部のメディアファイルのような）資料を示す属性を提供する。</desc>
  <attList>
    <attDef ident="url" usage="req">
      <gloss versionDate="2013-01-11" xml:lang="en">uniform resource locator</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">표준 원본 위치 지정소</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">localizador de recurso uniforme</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">adresse URL</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">URL (localizzatore universale di risorse)</gloss>
      <gloss versionDate="2023-09-27" xml:lang="ja">統一資源位置指定子</gloss>
      <desc versionDate="2013-01-11" xml:lang="en">specifies the URL from which the media concerned may be obtained.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">関連するメディアを入手するURLを示す。</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-01-11" xml:lang="en">provides attributes by which a resource (such as an externally
  held media file) may be located.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">（外部のメディアファイルのような）資料を示す属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2013-01-11" xml:lang="en">uniform resource locator</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">표준 원본 위치 지정소</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">localizador de recurso uniforme</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">adresse URL</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">URL (localizzatore universale di risorse)</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2023-09-27" xml:lang="ja">統一資源位置指定子</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-01-11" xml:lang="en">specifies the URL from which the media concerned may be obtained.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">関連するメディアを入手するURLを示す。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b11

