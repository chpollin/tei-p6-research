---
type: representation
source-type: document
source: '[[00_sources/tei-p5-annotationblock-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 annotationBlock
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/annotationBlock.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# annotationBlock

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2115. Git blob: `6fe9b587b44df2cffe5afc3ad2efa11251eb07fe`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="annotationBlock" xml:id="gi-annotationBlock" module="spoken">
  <!-- should this be in spoken module or analysis ? -->
  <desc versionDate="2016-02-27" xml:lang="en">groups together various annotations, e.g.
  for parallel interpretations of a spoken segment.</desc>
  <desc versionDate="2018-12-28" xml:lang="ja">様々な注釈をグループ化する。例えば、話されたセグメントの並行解釈のためなど。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
    <memberOf key="att.timed"/>
    <memberOf key="model.annotationLike"/>
    <memberOf key="model.divPart.spoken"/>
    </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="u"/>
      <elementRef key="spanGrp"/>
      <classRef key="model.global.spoken"/>
    </alternate>
  </content>
  <!-- shd there be a constraint to say if no child element is
       supplied the @corresp attrib must be used -->
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-annotationBlock-egXML-lt" source="#NONE">
      <annotationBlock who="#SPK1" start="#T2" end="#T3" xml:id="ag20">
        <u xml:id="u20">
          <seg xml:id="seg37" type="utterance" subtype="modeless">
            <w xml:id="w46">Yeah</w>
          </seg>
        </u>
      </annotationBlock>
      <annotationBlock who="#SPK1" start="#T5" end="#T6" xml:id="ag21">
        <u xml:id="u21">
          <seg xml:id="seg38" type="utterance" subtype="modeless">
            <w xml:id="w47">Mhm</w>
          </seg>
        </u>
      </annotationBlock>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TSTPAC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-02-27" xml:lang="en">groups together various annotations, e.g.
  for parallel interpretations of a spoken segment.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">様々な注釈をグループ化する。例えば、話されたセグメントの並行解釈のためなど。</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
    <memberOf key="att.timed"/>
    <memberOf key="model.annotationLike"/>
    <memberOf key="model.divPart.spoken"/>
    </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="u"/>
      <elementRef key="spanGrp"/>
      <classRef key="model.global.spoken"/>
    </alternate>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-annotationBlock-egXML-lt" source="#NONE">
      <annotationBlock who="#SPK1" start="#T2" end="#T3" xml:id="ag20">
        <u xml:id="u20">
          <seg xml:id="seg37" type="utterance" subtype="modeless">
            <w xml:id="w46">Yeah</w>
          </seg>
        </u>
      </annotationBlock>
      <annotationBlock who="#SPK1" start="#T5" end="#T6" xml:id="ag21">
        <u xml:id="u21">
          <seg xml:id="seg38" type="utterance" subtype="modeless">
            <w xml:id="w47">Mhm</w>
          </seg>
        </u>
      </annotationBlock>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSTPAC"/>
  </listRef>
```

^b6

