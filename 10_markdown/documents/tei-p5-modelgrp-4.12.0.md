---
type: representation
source-type: document
source: '[[00_sources/tei-p5-modelgrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 modelGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/modelGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# modelGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4194. Git blob: `38e7ca179bba7b38df6be26305adcddb89f21f31`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" ident="modelGrp" xml:id="gi-modelGrp">
  <gloss versionDate="2022-06-09" xml:lang="en">model group</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">any grouping of <gi>model</gi> or <gi>modelSequence</gi> elements with
    a common output method.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identEquiv"/>
        <classRef key="model.descLike"/>
      </alternate>
      <elementRef key="outputRendition" minOccurs="0"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="modelSequence"/>
        <elementRef key="model"/>
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="useSourceRendition" usage="opt">
      <desc versionDate="2015-05-15" xml:lang="en">whether to obey any rendition attribute which is
        present.</desc>
      <datatype>
        <dataRef key="teidata.truthValue"/>
      </datatype>
    </attDef>
    <attDef ident="output" usage="opt">
      <desc versionDate="2015-05-15" xml:lang="en">the intended output method.</desc>
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="semi">
        <valItem ident="web">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a
            web format</desc>
        </valItem>
        <valItem ident="print">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a
            print format</desc>
        </valItem>
        <valItem ident="plaintext">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a
            plain text format</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-modelGrp-egXML-tj">
      <elementSpec mode="change" ident="abbr">
        <modelGrp output="web">
          <model predicate="parent::choice" behaviour="omit"/>
          <model predicate="ancestor::front" behaviour="inline">
            <outputRendition>font-style:italic; </outputRendition>
          </model>
          <model predicate="not(parent::choice)" behaviour="inline">
            <outputRendition scope="before">content: ' ('</outputRendition>
            <outputRendition scope="after">content: ')'</outputRendition>
          </model>
        </modelGrp>
        <modelGrp output="print">
          <model predicate="parent::choice" behaviour="omit"/>
          <model predicate="not(parent::choice)" behaviour="note">
            <param name="place" value="'foot'"/>
          </model>
        </modelGrp>
      </elementSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-modelGrp-egXML-am" source="#UND">
      <modelGrp output="print">
        <modelSequence>
          <model behaviour="inline">
            <param name="content" value="@n"/>
          </model>
          <model behaviour="note">
            <param name="place" value="'foot'"/>
          </model>
        </modelSequence>
      </modelGrp>
    </egXML>
  </exemplum>
  <remarks ident="modelGrp-remarks" versionDate="2015-08-21" xml:lang="en">
    <!-- <p>The <gi>modelGrp</gi> element may be used to group <gi>model</gi> elements for any purpose
      but if doing so by major output format (web, print, plaintext) then the <att>output</att>
      attribute should be used.</p>-->
    <p>The child <gi>model</gi> elements of a <gi>modelGrp</gi> are always processed
      independently.</p>
  </remarks>
  <listRef>
    <ptr target="#TDPMMC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2022-06-09" xml:lang="en">model group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">any grouping of <gi>model</gi> or <gi>modelSequence</gi> elements with
    a common output method.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identEquiv"/>
        <classRef key="model.descLike"/>
      </alternate>
      <elementRef key="outputRendition" minOccurs="0"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="modelSequence"/>
        <elementRef key="model"/>
      </alternate>
    </sequence>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2015-05-15" xml:lang="en">whether to obey any rendition attribute which is
        present.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.truthValue"/>
      </datatype>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2015-05-15" xml:lang="en">the intended output method.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="web">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a
            web format</desc>
        </valItem>
        <valItem ident="print">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a
            print format</desc>
        </valItem>
        <valItem ident="plaintext">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a
            plain text format</desc>
        </valItem>
      </valList>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-modelGrp-egXML-tj">
      <elementSpec mode="change" ident="abbr">
        <modelGrp output="web">
          <model predicate="parent::choice" behaviour="omit"/>
          <model predicate="ancestor::front" behaviour="inline">
            <outputRendition>font-style:italic; </outputRendition>
          </model>
          <model predicate="not(parent::choice)" behaviour="inline">
            <outputRendition scope="before">content: ' ('</outputRendition>
            <outputRendition scope="after">content: ')'</outputRendition>
          </model>
        </modelGrp>
        <modelGrp output="print">
          <model predicate="parent::choice" behaviour="omit"/>
          <model predicate="not(parent::choice)" behaviour="note">
            <param name="place" value="'foot'"/>
          </model>
        </modelGrp>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-modelGrp-egXML-am" source="#UND">
      <modelGrp output="print">
        <modelSequence>
          <model behaviour="inline">
            <param name="content" value="@n"/>
          </model>
          <model behaviour="note">
            <param name="place" value="'foot'"/>
          </model>
        </modelSequence>
      </modelGrp>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="modelGrp-remarks" versionDate="2015-08-21" xml:lang="en">
    <!-- <p>The <gi>modelGrp</gi> element may be used to group <gi>model</gi> elements for any purpose
      but if doing so by major output format (web, print, plaintext) then the <att>output</att>
      attribute should be used.</p>-->
    <p>The child <gi>model</gi> elements of a <gi>modelGrp</gi> are always processed
      independently.</p>
  </remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDPMMC"/>
  </listRef>
```

^b13

