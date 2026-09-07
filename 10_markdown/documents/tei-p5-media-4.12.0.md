---
type: representation
source-type: document
source: '[[00_sources/tei-p5-media-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 media
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/media.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# media

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3056. Git blob: `ce16ad113efd58c1b91c3a78d6f837adb455d167`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-media" ident="media">
  <desc versionDate="2013-01-10" xml:lang="en">indicates the location of any form of external media such as
  an audio or video clip etc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.media"/>
    <memberOf key="att.resourced"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.graphicLike"/>
    <memberOf key="model.recordingPart"/>
  </classes>
  <content>
    
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
  <attList>
    <attDef ident="mimeType" usage="req" mode="change"/>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-qq">
      <figure>
        <media mimeType="image/png" url="fig1.png"/>
        <head>Figure One: The View from the Bridge</head>
        <figDesc>A Whistleresque view showing four or five sailing boats in the foreground, and a
          series of buoys strung out between them.</figDesc>
      </figure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-in">
      <media mimeType="audio/wav" url="dingDong.wav" dur="PT10S">
        <desc>Ten seconds of bellringing sound</desc>
      </media>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-bp">
      <media mimeType="video/mp4" url="clip45.mp4" dur="PT45M" width="500px">
        <desc>A 45 minute video clip to be displayed in a window 500
	  px wide</desc>
      </media>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-rh" source="#biblzh-tw_n5">
      <figure>
        <media type="graphic" mimeType="image/png" url="fig1.png"/>
        <head>維納斯</head>
        <figDesc> 波提且利 1484-1486年 畫布、蛋彩 佛羅倫斯，烏菲滋美術館</figDesc>
      </figure>
    </egXML>
  </exemplum>
  <remarks ident="media-remarks" versionDate="2013-01-10" xml:lang="en">
    <p>The attributes available for this element are not appropriate in
all cases. For example, it makes no sense to specify the temporal duration of a
graphic. Such errors are not
currently detected.</p>
    <p>The <att>mimeType</att> attribute must be used to specify the MIME media type of
the resource specified by the <att>url</att> attribute.</p>
  </remarks>
  <listRef>
    <ptr target="#COGR" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-01-10" xml:lang="en">indicates the location of any form of external media such as
  an audio or video clip etc.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.media"/>
    <memberOf key="att.resourced"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.graphicLike"/>
    <memberOf key="model.recordingPart"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-qq">
      <figure>
        <media mimeType="image/png" url="fig1.png"/>
        <head>Figure One: The View from the Bridge</head>
        <figDesc>A Whistleresque view showing four or five sailing boats in the foreground, and a
          series of buoys strung out between them.</figDesc>
      </figure>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-in">
      <media mimeType="audio/wav" url="dingDong.wav" dur="PT10S">
        <desc>Ten seconds of bellringing sound</desc>
      </media>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-bp">
      <media mimeType="video/mp4" url="clip45.mp4" dur="PT45M" width="500px">
        <desc>A 45 minute video clip to be displayed in a window 500
	  px wide</desc>
      </media>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-media-egXML-rh" source="#biblzh-tw_n5">
      <figure>
        <media type="graphic" mimeType="image/png" url="fig1.png"/>
        <head>維納斯</head>
        <figDesc> 波提且利 1484-1486年 畫布、蛋彩 佛羅倫斯，烏菲滋美術館</figDesc>
      </figure>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="media-remarks" versionDate="2013-01-10" xml:lang="en">
    <p>The attributes available for this element are not appropriate in
all cases. For example, it makes no sense to specify the temporal duration of a
graphic. Such errors are not
currently detected.</p>
    <p>The <att>mimeType</att> attribute must be used to specify the MIME media type of
the resource specified by the <att>url</att> attribute.</p>
  </remarks>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COGR" type="div2"/>
  </listRef>
```

^b9

