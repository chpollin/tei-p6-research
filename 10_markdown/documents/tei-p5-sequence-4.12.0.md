---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sequence-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sequence
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sequence.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sequence

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2433. Git blob: `bf74ed170aeda9f60b429aebbbd39a240daa8208`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-sequence" ident="sequence">
  <desc versionDate="2013-11-21" xml:lang="en">indicates that the constructs referenced by its children form a sequence.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
  </classes>
  <content>
    <classRef key="model.contentPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="sequencechilden" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:sequence">
        <sch:assert test="count(*) gt 1">The &lt;sequence&gt; element must have at least two child elements.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="preserveOrder" validUntil="2027-05-06">
      <desc type="deprecationInfo" versionDate="2024-03-15" xml:lang="en">The <att>preserveOrder</att> on <gi>sequence</gi> has been deprecated. The <gi>interleave</gi> element should be used to denote unordered constructs.</desc>
      <desc xml:lang="en" versionDate="2023-03-21">if false, indicates that component elements of a sequence may occur in any order.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sequence-egXML-uc" xml:lang="en" source="#UND">
      <content>
        <sequence>
          <alternate>
            <elementRef key="name"/>
            <elementRef key="persName"/>
          </alternate>
          <elementRef key="placeName" minOccurs="0" maxOccurs="5"/>
        </sequence>
      </content>
    </egXML>
    <p>This example content model matches a sequence consisting of either
    a <gi>name</gi> or a <gi>persName</gi> followed by nothing, or by a
    sequence of up to five <gi>placeName</gi> elements. </p>
  </exemplum>
  <listRef>
    <ptr target="#DEFCON" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-11-21" xml:lang="en">indicates that the constructs referenced by its children form a sequence.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.contentPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="sequencechilden" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:sequence">
        <sch:assert test="count(*) gt 1">The &lt;sequence&gt; element must have at least two child elements.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc type="deprecationInfo" versionDate="2024-03-15" xml:lang="en">The <att>preserveOrder</att> on <gi>sequence</gi> has been deprecated. The <gi>interleave</gi> element should be used to denote unordered constructs.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc xml:lang="en" versionDate="2023-03-21">if false, indicates that component elements of a sequence may occur in any order.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sequence-egXML-uc" xml:lang="en" source="#UND">
      <content>
        <sequence>
          <alternate>
            <elementRef key="name"/>
            <elementRef key="persName"/>
          </alternate>
          <elementRef key="placeName" minOccurs="0" maxOccurs="5"/>
        </sequence>
      </content>
    </egXML>
    <p>This example content model matches a sequence consisting of either
    a <gi>name</gi> or a <gi>persName</gi> followed by nothing, or by a
    sequence of up to five <gi>placeName</gi> elements. </p>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DEFCON" type="div2"/>
  </listRef>
```

^b9

