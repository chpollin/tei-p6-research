---
type: representation
source-type: document
source: '[[00_sources/tei-p5-alternate-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 alternate
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/alternate.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# alternate

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2469. Git blob: `bd569357fc01a44ffabeeb1d1538db158da07d16`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="alternate" xml:id="gi-alternate" module="tagdocs">
  <desc versionDate="2013-11-21" xml:lang="en">indicates that the constructs referenced by its children form an alternation.</desc>
  <desc versionDate="2018-12-28" xml:lang="ja">子要素らが参照している複数の構造が交換可能であることを示す。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
  </classes>
  <content>
    <alternate>
      <sequence>
        <elementRef key="valList" minOccurs="1" maxOccurs="1"/>
        <classRef key="model.contentPart" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <sequence>
        <classRef key="model.contentPart" minOccurs="1" maxOccurs="unbounded"/>
        <elementRef key="valList" minOccurs="0" maxOccurs="1"/>
      </sequence>        
      <!--
          That is, either the content starts with a <valList>, in
          which case it (the <valList>) may be followed by zero or
          more contentPart elements, OR it starts with a contentPart
          element, in which case they (the conentPart elements) may be
          followed by zero or one <valList>.
      -->
    </alternate>
  </content>
  <constraintSpec ident="alternatechilden" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:alternate">
        <sch:assert test="count(*) gt 1">The alternate element must have at least two child elements.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-alternate-egXML-eg" xml:lang="en" source="#UND"><content>
      <alternate>
        <elementRef key="name"/>
        <elementRef key="persName"/>
      </alternate>
    </content>
    </egXML>
    <p>This example content model permits either a <gi>name</gi> or a
    <gi>persName</gi>. </p>
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
<desc versionDate="2013-11-21" xml:lang="en">indicates that the constructs referenced by its children form an alternation.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">子要素らが参照している複数の構造が交換可能であることを示す。</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <sequence>
        <elementRef key="valList" minOccurs="1" maxOccurs="1"/>
        <classRef key="model.contentPart" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <sequence>
        <classRef key="model.contentPart" minOccurs="1" maxOccurs="unbounded"/>
        <elementRef key="valList" minOccurs="0" maxOccurs="1"/>
      </sequence>        
      <!--
          That is, either the content starts with a <valList>, in
          which case it (the <valList>) may be followed by zero or
          more contentPart elements, OR it starts with a contentPart
          element, in which case they (the conentPart elements) may be
          followed by zero or one <valList>.
      -->
    </alternate>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="alternatechilden" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:alternate">
        <sch:assert test="count(*) gt 1">The alternate element must have at least two child elements.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-alternate-egXML-eg" xml:lang="en" source="#UND"><content>
      <alternate>
        <elementRef key="name"/>
        <elementRef key="persName"/>
      </alternate>
    </content>
    </egXML>
    <p>This example content model permits either a <gi>name</gi> or a
    <gi>persName</gi>. </p>
  </exemplum>
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

