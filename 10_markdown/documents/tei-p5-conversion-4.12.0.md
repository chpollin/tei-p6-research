---
type: representation
source-type: document
source: '[[00_sources/tei-p5-conversion-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 conversion
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/conversion.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# conversion

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2633. Git blob: `a9a0050d2110bd6f552f1968ae2ac84bd28a1e68`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-conversion" ident="conversion">
  <desc versionDate="2019-07-03" xml:lang="en">defines how to calculate one unit of measure in terms of another.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.formula"/>
    <memberOf key="att.locatable"/>
  </classes>
  <content><empty/></content>
  <attList>
      <attDef ident="fromUnit" usage="req">
      <desc versionDate="2019-06-26" xml:lang="en">indicates a source unit of measure that is to be converted into another unit indicated in <att>toUnit</att>.</desc>
      <datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
    </attDef>
    <attDef ident="toUnit" usage="req">
      <desc versionDate="2019-06-26" xml:lang="en">the target unit of measurement for a conversion from a source unit referenced in <att>fromUnit</att>.</desc>
      <datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-conversion-egXML-ud" source="#NONE">
      <conversion fromUnit="#shilling" toUnit="#pence" formula="$fromUnit * 12" from="1707" to="1971"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-conversion-egXML-nt" source="#NONE">
      <conversion fromUnit="#pound" toUnit="#shilling" formula="$fromUnit * 20" from="1701" to="1971"/>
    </egXML>
  </exemplum>
  <remarks ident="conversion-remarks" versionDate="2019-06-25" xml:lang="en">
    <p>The conversion element is designed to store information about converting from one unit of measurement to another. The <att>formula</att> attribute holds an XPath expression that indicates how the measurement system in <att>fromUnit</att> is converted to the system in <att>toUnit</att>. Do not confuse the usage of the dating attributes (<att>from</att> and <att>to</att>) in the examples with the attributes (<att>fromUnit</att> and <att>toUnit</att>) designed to reference units of measure.</p>
  </remarks>
  <listRef>
    <ptr target="#HDUDECL" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-07-03" xml:lang="en">defines how to calculate one unit of measure in terms of another.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.formula"/>
    <memberOf key="att.locatable"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2019-06-26" xml:lang="en">indicates a source unit of measure that is to be converted into another unit indicated in <att>toUnit</att>.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2019-06-26" xml:lang="en">the target unit of measurement for a conversion from a source unit referenced in <att>fromUnit</att>.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-conversion-egXML-ud" source="#NONE">
      <conversion fromUnit="#shilling" toUnit="#pence" formula="$fromUnit * 12" from="1707" to="1971"/>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-conversion-egXML-nt" source="#NONE">
      <conversion fromUnit="#pound" toUnit="#shilling" formula="$fromUnit * 20" from="1701" to="1971"/>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="conversion-remarks" versionDate="2019-06-25" xml:lang="en">
    <p>The conversion element is designed to store information about converting from one unit of measurement to another. The <att>formula</att> attribute holds an XPath expression that indicates how the measurement system in <att>fromUnit</att> is converted to the system in <att>toUnit</att>. Do not confuse the usage of the dating attributes (<att>from</att> and <att>to</att>) in the examples with the attributes (<att>fromUnit</att> and <att>toUnit</att>) designed to reference units of measure.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDUDECL" type="div3"/>
  </listRef>
```

^b11

