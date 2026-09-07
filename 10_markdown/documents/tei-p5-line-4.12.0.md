---
type: representation
source-type: document
source: '[[00_sources/tei-p5-line-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 line
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/line.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# line

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2459. Git blob: `d4b20d802f45dc02598dc965704655e203761077`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="line" xml:id="gi-line" module="transcr">
  <desc versionDate="2011-11-02" xml:lang="en">contains the transcription of a topographic line in the source document.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.coordinated"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.linePart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.global"/>
        <classRef key="model.gLike"/>
        <classRef key="model.linePart"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <p>This example shows topographical lines as a means of preserving the visual appearance of a poem:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-line-egXML-ij">
      <surface>
        <zone>
          <line>Poem</line>
          <line>As in Visions of — at</line>
          <line>night —</line>
          <line>All sorts of fancies running through</line>
          <line>the head</line>
        </zone>
      </surface>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-line-egXML-ar">
      <surface>
        <zone>
          <line>Hope you enjoyed</line>
          <line>Wales, as they
said</line>
          <line>to Mrs FitzHerbert</line>
          <line>Mama</line>
        </zone>
        <zone>
          <line>Printed in England</line>
        </zone>
      </surface>
    </egXML>
  </exemplum>
  <remarks ident="line-remarks" versionDate="2011-11-02" xml:lang="en">
    <p>This element should be used only to mark up writing which
is topographically organized as a series of lines, horizontal or
vertical. It should not be used to mark lines of verse (for which use
<gi>l</gi>) nor to mark line beginnings within text which has been encoded
using structural elements such as <gi>p</gi> (for which use
<gi>lb</gi>).</p>
  </remarks>
  <listRef>
    <ptr target="#PHZLAB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-02" xml:lang="en">contains the transcription of a topographic line in the source document.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.coordinated"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.linePart"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.global"/>
        <classRef key="model.gLike"/>
        <classRef key="model.linePart"/>
      </alternate>
    
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>This example shows topographical lines as a means of preserving the visual appearance of a poem:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-line-egXML-ij">
      <surface>
        <zone>
          <line>Poem</line>
          <line>As in Visions of — at</line>
          <line>night —</line>
          <line>All sorts of fancies running through</line>
          <line>the head</line>
        </zone>
      </surface>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-line-egXML-ar">
      <surface>
        <zone>
          <line>Hope you enjoyed</line>
          <line>Wales, as they
said</line>
          <line>to Mrs FitzHerbert</line>
          <line>Mama</line>
        </zone>
        <zone>
          <line>Printed in England</line>
        </zone>
      </surface>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="line-remarks" versionDate="2011-11-02" xml:lang="en">
    <p>This element should be used only to mark up writing which
is topographically organized as a series of lines, horizontal or
vertical. It should not be used to mark lines of verse (for which use
<gi>l</gi>) nor to mark line beginnings within text which has been encoded
using structural elements such as <gi>p</gi> (for which use
<gi>lb</gi>).</p>
  </remarks>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHZLAB"/>
  </listRef>
```

^b7

