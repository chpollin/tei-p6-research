---
type: representation
source-type: document
source: '[[00_sources/tei-p5-correspdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 correspDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/correspDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# correspDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3132. Git blob: `b3b1596adefdb20bb4d1e4857030313a0e4848fa`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-correspDesc" ident="correspDesc">
  <gloss versionDate="2014-01-13" xml:lang="en">correspondence description</gloss>
  <gloss versionDate="2021-02-02" xml:lang="it">descrizione di corrispondenza epistolare</gloss>
  <gloss versionDate="2024-07-01" xml:lang="ja">書簡の記述</gloss>
  <desc versionDate="2015-01-29" xml:lang="en">contains a description
    of the actions related to one act of correspondence.</desc>
  <desc versionDate="2024-07-01" xml:lang="ja">書簡の一連のやりとりに関連する所作の記述を含む。</desc>
  <desc versionDate="2021-02-02" xml:lang="it">contiene una descrizione delle azioni intorno a un atto di corrispondenza epistolare.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    <!-- modeled after publicationStmt -->
    <alternate>
      <classRef key="model.correspDescPart" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>      
    </alternate>
  </content>
  <constraintSpec ident="correspDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:correspDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspDesc-egXML-ve">
      <correspDesc>
        <correspAction type="sent">
          <persName>Carl Maria von Weber</persName>
          <settlement>Dresden</settlement>
          <date when="1817-06-23">23 June 1817</date>
        </correspAction>
        <correspAction type="received">
          <persName>Caroline Brandt</persName>
          <settlement>Prag</settlement>
        </correspAction>
        <correspContext>
          <ref type="prev" target="http://www.weber-gesamtausgabe.de/A041209">Previous letter of 
            <persName>Carl Maria von Weber</persName> 
            to <persName>Caroline Brandt</persName>: 
            <date from="1817-06-19" to="1817-06-20">June 19/20, 1817</date>
          </ref>
          <ref type="next" target="http://www.weber-gesamtausgabe.de/A041217">Next letter of 
            <persName>Carl Maria von Weber</persName> to 
            <persName>Caroline Brandt</persName>: 
            <date when="1817-06-27">June 27, 1817</date>
          </ref>
        </correspContext>
      </correspDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD44CD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2014-01-13" xml:lang="en">correspondence description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2021-02-02" xml:lang="it">descrizione di corrispondenza epistolare</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2024-07-01" xml:lang="ja">書簡の記述</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2015-01-29" xml:lang="en">contains a description
    of the actions related to one act of correspondence.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-07-01" xml:lang="ja">書簡の一連のやりとりに関連する所作の記述を含む。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2021-02-02" xml:lang="it">contiene una descrizione delle azioni intorno a un atto di corrispondenza epistolare.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b7

### Block 8

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!-- modeled after publicationStmt -->
    <alternate>
      <classRef key="model.correspDescPart" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>      
    </alternate>
  </content>
```

^b8

### Block 9

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="correspDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:correspDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspDesc-egXML-ve">
      <correspDesc>
        <correspAction type="sent">
          <persName>Carl Maria von Weber</persName>
          <settlement>Dresden</settlement>
          <date when="1817-06-23">23 June 1817</date>
        </correspAction>
        <correspAction type="received">
          <persName>Caroline Brandt</persName>
          <settlement>Prag</settlement>
        </correspAction>
        <correspContext>
          <ref type="prev" target="http://www.weber-gesamtausgabe.de/A041209">Previous letter of 
            <persName>Carl Maria von Weber</persName> 
            to <persName>Caroline Brandt</persName>: 
            <date from="1817-06-19" to="1817-06-20">June 19/20, 1817</date>
          </ref>
          <ref type="next" target="http://www.weber-gesamtausgabe.de/A041217">Next letter of 
            <persName>Carl Maria von Weber</persName> to 
            <persName>Caroline Brandt</persName>: 
            <date when="1817-06-27">June 27, 1817</date>
          </ref>
        </correspContext>
      </correspDesc>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD44CD"/>
  </listRef>
```

^b11

