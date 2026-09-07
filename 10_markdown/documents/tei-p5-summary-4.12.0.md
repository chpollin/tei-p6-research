---
type: representation
source-type: document
source: '[[00_sources/tei-p5-summary-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 summary
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/summary.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# summary

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2101. Git blob: `b21abc8dd193017e17a459a8c0682ed3711e3563`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="SUMMARY" ident="summary">
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="summary.desc">contains an overview of the available
  information concerning some aspect of an item or object (for example, its
intellectual content, history, layout, typography etc.) as a
complement or alternative to the  more detailed information  carried by
  more specific elements.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-vo">
      <summary>
This item consists of three books with a prologue and an epilogue.
</summary>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-gs">
      <summary> Cet item est formé de trois livres, d'un prologue et d'un épilogue.</summary>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-hm">
      <summary> 此物件包含三冊以及序與跋。</summary>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-dm">
      <typeDesc>
        <summary>Uses a mixture of Roman and Black Letter types.</summary>
        <typeNote>Antiqua typeface, showing influence of Jenson's Venetian
fonts.</typeNote>
        <typeNote>The black letter face is a variant of Schwabacher.</typeNote>
      </typeDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msco"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="summary.desc">contains an overview of the available
  information concerning some aspect of an item or object (for example, its
intellectual content, history, layout, typography etc.) as a
complement or alternative to the  more detailed information  carried by
  more specific elements.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-vo">
      <summary>
This item consists of three books with a prologue and an epilogue.
</summary>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-gs">
      <summary> Cet item est formé de trois livres, d'un prologue et d'un épilogue.</summary>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-hm">
      <summary> 此物件包含三冊以及序與跋。</summary>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUMMARY-egXML-dm">
      <typeDesc>
        <summary>Uses a mixture of Roman and Black Letter types.</summary>
        <typeNote>Antiqua typeface, showing influence of Jenson's Venetian
fonts.</typeNote>
        <typeNote>The black letter face is a variant of Schwabacher.</typeNote>
      </typeDesc>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msco"/>
  </listRef>
```

^b8

