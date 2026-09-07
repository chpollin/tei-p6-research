---
type: representation
source-type: document
source: '[[00_sources/tei-p5-secl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 secl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/secl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# secl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1733. Git blob: `505c794c5fd51a999fbda7d9c28697e7e634e4bd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-secl" ident="secl">
  <gloss versionDate="2015-08-06" xml:lang="en">secluded text</gloss>
  <desc versionDate="2015-05-30" xml:lang="en">marks text present in the source which the editor believes to be genuine but out of its original place (which is unknown).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="reason" usage="opt">
      <desc versionDate="2015-05-30" xml:lang="en">one or more words indicating why this text has been secluded, e.g.
      <mentioned>interpolated</mentioned> etc.</desc>
      <datatype maxOccurs="unbounded">
        <dataRef key="teidata.enumerated"/>
      </datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-secl-egXML-eh"><rdg source="#Pescani">
      <secl>
        <l n="15" xml:id="l15">Alphesiboea suos ulta est pro coniuge fratres,</l>
        <l n="16" xml:id="l16">sanguinis et cari vincula rupit amor.</l>
      </secl>
    </rdg><note>secl. Pescani</note></egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHOM"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2015-08-06" xml:lang="en">secluded text</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2015-05-30" xml:lang="en">marks text present in the source which the editor believes to be genuine but out of its original place (which is unknown).</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2015-05-30" xml:lang="en">one or more words indicating why this text has been secluded, e.g.
      <mentioned>interpolated</mentioned> etc.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded">
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-secl-egXML-eh"><rdg source="#Pescani">
      <secl>
        <l n="15" xml:id="l15">Alphesiboea suos ulta est pro coniuge fratres,</l>
        <l n="16" xml:id="l16">sanguinis et cari vincula rupit amor.</l>
      </secl>
    </rdg><note>secl. Pescani</note></egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHOM"/>
  </listRef>
```

^b8

