---
type: representation
source-type: document
source: '[[00_sources/tei-p5-notatedmusic-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 notatedMusic
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/notatedMusic.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# notatedMusic

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2767. Git blob: `f5436e8b9e1aae06291263fb550af33930988a7b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="figures" xml:id="gi-notatedMusic" ident="notatedMusic">
  <desc versionDate="2011-04-12" xml:lang="en">encodes the presence of music notation in a text.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global"/>
  </classes>
  <content>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.labelLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="graphic"/>
        <elementRef key="binaryObject"/>
        <elementRef key="seg"/>
      </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notatedMusic-egXML-mr">
      <notatedMusic>
        <ptr target="bar1.xml"/>
        <graphic url="bar1.jpg"/>
        <desc>First bar of Chopin's Scherzo No.3 Op.39</desc>
      </notatedMusic>
    </egXML>
  </exemplum>
  <remarks ident="notatedMusic-remarks" versionDate="2011-07-04" xml:lang="en">
    <p>It is possible to describe
        the content of the notation using elements from the <ident type="class">model.labelLike</ident> class and it is possible
        to point to an external representation using elements from <ident type="class">model.ptrLike</ident>. It is possible to
        specify the location of digital objects representing the notated music in other media such
        as images or audio-visual files. The encoder's interpretation of the correspondence between
        the notated music and these digital objects is not encoded explicitly. We recommend the use
        of graphic and binaryObject mainly as a fallback mechanism when the notated music format is
        not displayable by the application using the encoding. The alignment of encoded notated
        music, images carrying the notation, and audio files is a complex matter for which we refer
        the encoder to other formats and specifications such as MPEG-SMR.</p>
    <p>It is also recommended, when useful, to embed XML-based music notation formats, such as the 
      <ref target="http://music-encoding.org">Music Encoding Initiative</ref> format as content of 
      <gi>notatedMusic</gi>. This must be done by means of customization.</p>
  </remarks>
  <listRef>
    <ptr target="#FTNM"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-04-12" xml:lang="en">encodes the presence of music notation in a text.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.labelLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="graphic"/>
        <elementRef key="binaryObject"/>
        <elementRef key="seg"/>
      </alternate>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notatedMusic-egXML-mr">
      <notatedMusic>
        <ptr target="bar1.xml"/>
        <graphic url="bar1.jpg"/>
        <desc>First bar of Chopin's Scherzo No.3 Op.39</desc>
      </notatedMusic>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="notatedMusic-remarks" versionDate="2011-07-04" xml:lang="en">
    <p>It is possible to describe
        the content of the notation using elements from the <ident type="class">model.labelLike</ident> class and it is possible
        to point to an external representation using elements from <ident type="class">model.ptrLike</ident>. It is possible to
        specify the location of digital objects representing the notated music in other media such
        as images or audio-visual files. The encoder's interpretation of the correspondence between
        the notated music and these digital objects is not encoded explicitly. We recommend the use
        of graphic and binaryObject mainly as a fallback mechanism when the notated music format is
        not displayable by the application using the encoding. The alignment of encoded notated
        music, images carrying the notation, and audio files is a complex matter for which we refer
        the encoder to other formats and specifications such as MPEG-SMR.</p>
    <p>It is also recommended, when useful, to embed XML-based music notation formats, such as the 
      <ref target="http://music-encoding.org">Music Encoding Initiative</ref> format as content of 
      <gi>notatedMusic</gi>. This must be done by means of customization.</p>
  </remarks>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FTNM"/>
  </listRef>
```

^b6

