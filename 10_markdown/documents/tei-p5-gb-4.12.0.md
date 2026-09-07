---
type: representation
source-type: document
source: '[[00_sources/tei-p5-gb-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 gb
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/gb.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# gb

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1790. Git blob: `afd33b768866a2e0f1b6b2ccf8820d6ea4a07dc3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-gb" ident="gb">
  <gloss versionDate="2017-06-14" xml:lang="en">gathering beginning</gloss>
  <desc versionDate="2010-09-21" xml:lang="en">marks the beginning of a new gathering or quire in a transcribed codex.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gb-egXML-fe" source="#UND">
      <gb n="iii"/>
      <pb n="2r"/>
      <!-- material from page 2 recto of gathering iii here -->
      <pb n="2v"/>
      <!-- material from page 2 verso of gathering iii here -->
    </egXML>
  </exemplum>
  <remarks ident="gb-remarks" versionDate="2010-09-21" xml:lang="en">
    <p>By convention, <gi>gb</gi> elements should appear at the start
    of the first page in the gathering. The global <att>n</att>
    attribute indicates the number or other value used to identify
    this gathering in a collation.  </p>
    <p>The <att>type</att> attribute may be used to further
    characterize the gathering in any respect.</p>
  </remarks>
  <listRef>
    <ptr target="#CORS5" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2017-06-14" xml:lang="en">gathering beginning</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2010-09-21" xml:lang="en">marks the beginning of a new gathering or quire in a transcribed codex.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gb-egXML-fe" source="#UND">
      <gb n="iii"/>
      <pb n="2r"/>
      <!-- material from page 2 recto of gathering iii here -->
      <pb n="2v"/>
      <!-- material from page 2 verso of gathering iii here -->
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="gb-remarks" versionDate="2010-09-21" xml:lang="en">
    <p>By convention, <gi>gb</gi> elements should appear at the start
    of the first page in the gathering. The global <att>n</att>
    attribute indicates the number or other value used to identify
    this gathering in a collation.  </p>
    <p>The <att>type</att> attribute may be used to further
    characterize the gathering in any respect.</p>
  </remarks>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS5" type="div3"/>
  </listRef>
```

^b7

