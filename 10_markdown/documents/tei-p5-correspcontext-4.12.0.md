---
type: representation
source-type: document
source: '[[00_sources/tei-p5-correspcontext-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 correspContext
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/correspContext.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# correspContext

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2529. Git blob: `6f4d197a14978a975cd986dbdc2b3057f2a5945f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-correspContext" ident="correspContext">
  <gloss versionDate="2014-01-13" xml:lang="en">correspondence context</gloss>
  <gloss versionDate="2014-01-13" xml:lang="de">Korrespondenzstelle</gloss>
  <gloss versionDate="2022-06-02" xml:lang="ja">書簡の文脈</gloss>
  <!-- related by sender/addressee or topics … -->
  <desc versionDate="2014-01-13" xml:lang="en">provides references to preceding or following correspondence related to this piece of correspondence.</desc>
  <desc versionDate="2024-07-01" xml:lang="ja">当該書簡の前後の書簡への参照。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.correspDescPart"/>
  </classes>
  <content>
    <classRef key="model.correspContextPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspContext-egXML-uq" source="#UND">
      <correspContext>
        <ptr type="next" subtype="toAuthor" target="http://tei.ibi.hu-berlin.de/berliner-intellektuelle/manuscript?Brief101VarnhagenanBoeckh"/>
        <ptr type="prev" subtype="fromAuthor" target="http://tei.ibi.hu-berlin.de/berliner-intellektuelle/manuscript?Brief103BoeckhanVarnhagen"/>
      </correspContext>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspContext-egXML-qm">
      <correspContext>
        <ref type="prev" target="http://weber-gesamtausgabe.de/A040962">
          Previous letter of 
          <persName>Carl Maria von Weber</persName> to 
          <persName>Caroline Brandt</persName>: 
          <date when="1816-12-30">December 30, 1816</date>
        </ref> 
        <ref type="next" target="http://weber-gesamtausgabe.de/A041003">
          Next letter of 
          <persName>Carl Maria von Weber</persName> to 
          <persName>Caroline Brandt</persName>: 
          <date when="1817-01-05">January 5, 1817</date>
        </ref>
      </correspContext>
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
<gloss versionDate="2014-01-13" xml:lang="en">correspondence context</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2014-01-13" xml:lang="de">Korrespondenzstelle</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2022-06-02" xml:lang="ja">書簡の文脈</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2014-01-13" xml:lang="en">provides references to preceding or following correspondence related to this piece of correspondence.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-07-01" xml:lang="ja">当該書簡の前後の書簡への参照。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.correspDescPart"/>
  </classes>
```

^b6

### Block 7

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.correspContextPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspContext-egXML-uq" source="#UND">
      <correspContext>
        <ptr type="next" subtype="toAuthor" target="http://tei.ibi.hu-berlin.de/berliner-intellektuelle/manuscript?Brief101VarnhagenanBoeckh"/>
        <ptr type="prev" subtype="fromAuthor" target="http://tei.ibi.hu-berlin.de/berliner-intellektuelle/manuscript?Brief103BoeckhanVarnhagen"/>
      </correspContext>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspContext-egXML-qm">
      <correspContext>
        <ref type="prev" target="http://weber-gesamtausgabe.de/A040962">
          Previous letter of 
          <persName>Carl Maria von Weber</persName> to 
          <persName>Caroline Brandt</persName>: 
          <date when="1816-12-30">December 30, 1816</date>
        </ref> 
        <ref type="next" target="http://weber-gesamtausgabe.de/A041003">
          Next letter of 
          <persName>Carl Maria von Weber</persName> to 
          <persName>Caroline Brandt</persName>: 
          <date when="1817-01-05">January 5, 1817</date>
        </ref>
      </correspContext>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD44CD"/>
  </listRef>
```

^b10

