---
type: representation
source-type: document
source: '[[00_sources/tei-p5-interleave-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 interleave
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/interleave.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# interleave

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2901. Git blob: `b9ef22c6ad5a4d135fb847233cce90bafbe5d25a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" ident="interleave">
  <desc versionDate="2024-03-16" xml:lang="en">indicates that the constructs referenced by its children occur in any order (i.e. are interleaved)</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
  </classes>
  <content>
    <classRef key="model.contentPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="interleavechilden" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:interleave">
        <sch:assert test="count(*) gt 1">The &lt;interleave&gt; element must have at least two child elements.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="en" source="#UND">
      <content>
        <interleave>
          <elementRef key="persName"/>
          <alternate minOccurs="0">
            <elementRef key="placeName"/>
            <elementRef key="location"/>
          </alternate>
          <elementRef key="note" minOccurs="0"/>
        </interleave>
      </content>
    </egXML>
    <p>This example describes a content model that consists of a
    mandatory <gi>persName</gi> element, zero or one of either
    <gi>placeName</gi> or <gi>location</gi>, and an optional
    <gi>note</gi> element, in any order.</p>
    <p>To express this content model in a DTD, the original schema
    language for XML, one might use
    <eg xml:space="preserve">(   persName
      | ( persName, note )
      | ( persName, ( placeName | location ) ) 
      | ( note, persName )
      | ( ( placeName | location ), persName )
      | ( persName, note, ( placeName | location ) )
      | ( persName, ( placeName | location ), note )
      | ( note, persName, ( placeName | location ) )
      | ( note, ( placeName | location ), persName )
      | ( ( placeName | location ), note, persName )
      | ( ( placeName | location ), persName, note )
    )</eg></p>
  </exemplum>
  <remarks ident="interleave-remarks" xml:lang="en" versionDate="2025-05-18">
    <p>If an ODD file makes use of this element, current processing
    software will not be able to generate a DTD from it. For this
    reason TEI P5 itself does not currently make use of
    <gi>interleave</gi> internally.</p>
  </remarks>
  <listRef>
    <ptr target="#DEFCON" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2024-03-16" xml:lang="en">indicates that the constructs referenced by its children occur in any order (i.e. are interleaved)</desc>
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
<constraintSpec ident="interleavechilden" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:interleave">
        <sch:assert test="count(*) gt 1">The &lt;interleave&gt; element must have at least two child elements.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="en" source="#UND">
      <content>
        <interleave>
          <elementRef key="persName"/>
          <alternate minOccurs="0">
            <elementRef key="placeName"/>
            <elementRef key="location"/>
          </alternate>
          <elementRef key="note" minOccurs="0"/>
        </interleave>
      </content>
    </egXML>
    <p>This example describes a content model that consists of a
    mandatory <gi>persName</gi> element, zero or one of either
    <gi>placeName</gi> or <gi>location</gi>, and an optional
    <gi>note</gi> element, in any order.</p>
    <p>To express this content model in a DTD, the original schema
    language for XML, one might use
    <eg xml:space="preserve">(   persName
      | ( persName, note )
      | ( persName, ( placeName | location ) ) 
      | ( note, persName )
      | ( ( placeName | location ), persName )
      | ( persName, note, ( placeName | location ) )
      | ( persName, ( placeName | location ), note )
      | ( note, persName, ( placeName | location ) )
      | ( note, ( placeName | location ), persName )
      | ( ( placeName | location ), note, persName )
      | ( ( placeName | location ), persName, note )
    )</eg></p>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="interleave-remarks" xml:lang="en" versionDate="2025-05-18">
    <p>If an ODD file makes use of this element, current processing
    software will not be able to generate a DTD from it. For this
    reason TEI P5 itself does not currently make use of
    <gi>interleave</gi> internally.</p>
  </remarks>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DEFCON" type="div2"/>
  </listRef>
```

^b7

