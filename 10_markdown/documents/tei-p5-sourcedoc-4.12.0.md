---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sourcedoc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sourceDoc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sourceDoc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sourceDoc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2570. Git blob: `3430841d3c0abbcaa25e359abe5383e32a0b1c46`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="sourceDoc" xml:id="gi-sourceDoc" module="transcr">
  <desc versionDate="2011-11-26" xml:lang="en"> contains a transcription or other representation of a single
 source document potentially forming part of a <foreign>dossier
 génétique</foreign> or collection of sources.</desc>
    <desc versionDate="2023-07-29" xml:lang="ja">
<foreign>dossier génétique</foreign>（生成文書）、あるいは資料のコレクションの一部を潜在的に形成し得る単一の資料文書の翻刻やその他の表現を含む。
    </desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="model.resource"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.global"/>
      <classRef key="model.graphicLike"/>
      <elementRef key="surface"/>
      <elementRef key="surfaceGrp"/>
    </alternate>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDoc-egXML-nz">
      <sourceDoc>
        <surfaceGrp n="leaf1">
          <surface facs="page1.png">
            <zone>All the writing on  page 1</zone>
          </surface>
          <surface>
            <graphic url="page2-highRes.png"/>
            <graphic url="page2-lowRes.png"/>
            <zone>
              <line>A line of writing on page 2</line>
              <line>Another line of writing on page 2</line>
            </zone>
          </surface>
        </surfaceGrp>
      </sourceDoc>
    </egXML>
  </exemplum>
  <remarks ident="sourceDoc-remarks" versionDate="2011-10-31" xml:lang="en">
    <p>This element may be used as an alternative to
<gi>facsimile</gi> for TEI documents containing only page images, or
for documents containing both images and
transcriptions. Transcriptions may be provided within the
<gi>surface</gi> elements making up a source document, in parallel
with them as part of a <gi>text</gi> element, or in both places if
the encoder wishes to distinguish these two modes of transcription.</p>
  </remarks>
  <listRef>
    <ptr target="#PHFAX"/>
    <ptr target="#PHZLAB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-26" xml:lang="en"> contains a transcription or other representation of a single
 source document potentially forming part of a <foreign>dossier
 génétique</foreign> or collection of sources.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-07-29" xml:lang="ja">
<foreign>dossier génétique</foreign>（生成文書）、あるいは資料のコレクションの一部を潜在的に形成し得る単一の資料文書の翻刻やその他の表現を含む。
    </desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="model.resource"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.global"/>
      <classRef key="model.graphicLike"/>
      <elementRef key="surface"/>
      <elementRef key="surfaceGrp"/>
    </alternate>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sourceDoc-egXML-nz">
      <sourceDoc>
        <surfaceGrp n="leaf1">
          <surface facs="page1.png">
            <zone>All the writing on  page 1</zone>
          </surface>
          <surface>
            <graphic url="page2-highRes.png"/>
            <graphic url="page2-lowRes.png"/>
            <zone>
              <line>A line of writing on page 2</line>
              <line>Another line of writing on page 2</line>
            </zone>
          </surface>
        </surfaceGrp>
      </sourceDoc>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="sourceDoc-remarks" versionDate="2011-10-31" xml:lang="en">
    <p>This element may be used as an alternative to
<gi>facsimile</gi> for TEI documents containing only page images, or
for documents containing both images and
transcriptions. Transcriptions may be provided within the
<gi>surface</gi> elements making up a source document, in parallel
with them as part of a <gi>text</gi> element, or in both places if
the encoder wishes to distinguish these two modes of transcription.</p>
  </remarks>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHFAX"/>
    <ptr target="#PHZLAB"/>
  </listRef>
```

^b7

