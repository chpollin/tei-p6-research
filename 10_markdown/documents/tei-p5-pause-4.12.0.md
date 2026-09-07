---
type: representation
source-type: document
source: '[[00_sources/tei-p5-pause-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 pause
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/pause.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# pause

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2071. Git blob: `02052e6f9bc09739d94fb3bb10f1146c9d3f2606`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" xml:id="PAUSE" ident="pause">
  <gloss versionDate="2007-06-12" xml:lang="en">pause</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">pause</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">marks a pause either between or within utterances.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">발화들 사이 또는 발화들 내에서의 휴지</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">說話之間或說話時的停頓。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話にある間を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">une pause entre énonciations ou bien à
			l'intérieur d'énonciations.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">una pausa al interno de un enunciado o entre un enunciado y otro.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">pausa all'interno di un enuciatiato o tra un enuciato e l'altro.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PAUSE-egXML-pr" source="#UND">
      <pause dur="PT42S" type="pregnant"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PAUSE-egXML-vx" source="#UND">
      <pause dur="PT42S" type="pregnant"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TSBAPA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">pause</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">pause</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">marks a pause either between or within utterances.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">발화들 사이 또는 발화들 내에서의 휴지</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說話之間或說話時的停頓。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話にある間を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">une pause entre énonciations ou bien à
			l'intérieur d'énonciations.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">una pausa al interno de un enunciado o entre un enunciado y otro.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">pausa all'interno di un enuciatiato o tra un enuciato e l'altro.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PAUSE-egXML-pr" source="#UND">
      <pause dur="PT42S" type="pregnant"/>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PAUSE-egXML-vx" source="#UND">
      <pause dur="PT42S" type="pregnant"/>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSBAPA"/>
  </listRef>
```

^b14

