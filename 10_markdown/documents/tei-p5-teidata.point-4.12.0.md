---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.point-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.point
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.point.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.point

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2047. Git blob: `7a1ac4738b0262ad4e28bf631cb77d8756b2e18b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="data-point" ident="teidata.point">
  <desc versionDate="2010-10-17" xml:lang="en">defines the data type used to express a point in cartesian space.</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">デカルト空間内の点を表現するデータ型を定義する。</desc>
  <content>
    <dataRef name="token" restriction="(-?[0-9]+(\.[0-9]+)?,-?[0-9]+(\.[0-9]+)?(,-?[0-9]+(\.[0-9]+)?)?)"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-point-egXML-qa" source="#UND">
      <facsimile>
        <surface ulx="0" uly="0" lrx="400" lry="280">
          <zone points="220,100 300,210 170,250 123,234">
            <graphic url="handwriting.png"/>
          </zone>
        </surface>
      </facsimile>
    </egXML>
  </exemplum>
  <remarks ident="teidata.point-remarks" versionDate="2019-02-24" xml:lang="en">
    <p>A point is defined by two or three numeric values separated by
    commas. The numeric values should be expressed as decimal numbers
    which do not end in a decimal point. E.g., both
    <val>0.0,84.2</val> and <val>0,84</val> are allowed, but
    <val>0.,84.</val> is not.
    <!-- 51°45'45.63"N,  1°16'11.81"W -->
    </p>
  </remarks>
  <remarks ident="teidata.point-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>点は、ふたつの数値で定義される。数値は10進小数で表されることが望ましい。数値は小数点で終わってはならない。たとえば、<code>0.0,84.2</code>も<code>0,84</code>も有効であるが、<code>0.,84.</code>はそうではない。</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2010-10-17" xml:lang="en">defines the data type used to express a point in cartesian space.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">デカルト空間内の点を表現するデータ型を定義する。</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <dataRef name="token" restriction="(-?[0-9]+(\.[0-9]+)?,-?[0-9]+(\.[0-9]+)?(,-?[0-9]+(\.[0-9]+)?)?)"/>
  </content>
```

^b3

### Block 4

XML location: `/dataSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-point-egXML-qa" source="#UND">
      <facsimile>
        <surface ulx="0" uly="0" lrx="400" lry="280">
          <zone points="220,100 300,210 170,250 123,234">
            <graphic url="handwriting.png"/>
          </zone>
        </surface>
      </facsimile>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.point-remarks" versionDate="2019-02-24" xml:lang="en">
    <p>A point is defined by two or three numeric values separated by
    commas. The numeric values should be expressed as decimal numbers
    which do not end in a decimal point. E.g., both
    <val>0.0,84.2</val> and <val>0,84</val> are allowed, but
    <val>0.,84.</val> is not.
    <!-- 51°45'45.63"N,  1°16'11.81"W -->
    </p>
  </remarks>
```

^b5

### Block 6

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.point-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>点は、ふたつの数値で定義される。数値は10進小数で表されることが望ましい。数値は小数点で終わってはならない。たとえば、<code>0.0,84.2</code>も<code>0,84</code>も有効であるが、<code>0.,84.</code>はそうではない。</p>
  </remarks>
```

^b6

