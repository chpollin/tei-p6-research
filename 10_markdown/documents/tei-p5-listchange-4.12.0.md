---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listchange-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listChange
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listChange.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listChange

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3031. Git blob: `b9c3657d3bfe6cbe26562f11bdd5bb46e6f2f187`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="listChange" xml:id="gi-listChange" module="header">
  <desc versionDate="2013-04-14" xml:lang="en">groups a number of change descriptions associated 
with either the creation of a source text or the revision of an encoded text.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <content>  
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/> 
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="listChange"/>
        <elementRef key="change"/>
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="ordered">
      <desc versionDate="2013-04-14" xml:lang="en">indicates whether the ordering of its child <gi>change</gi>
elements is to be considered significant or not.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
      <defaultVal>true</defaultVal>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listChange-egXML-ne">
      <revisionDesc>
        <listChange>
          <change when="1991-11-11" who="#LB"> deleted chapter 10 </change>
          <change when="1991-11-02" who="#MSM"> completed first draft </change>
        </listChange>
      </revisionDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listChange-egXML-cx">
      <profileDesc>
        <creation>
          <listChange ordered="true">
            <change xml:id="CHG-1">First stage, written in ink by a writer</change>
            <change xml:id="CHG-2">Second stage, written in Goethe's hand using pencil</change>
            <change xml:id="CHG-3">Fixation of the revised passages and further revisions by
Goethe using ink</change>
            <change xml:id="CHG-4">Addition of another stanza in a          different hand,
probably at a later stage</change>
          </listChange>
        </creation>
      </profileDesc>
    </egXML>
  </exemplum>
  <remarks ident="listChange-remarks" versionDate="2013-04-14" xml:lang="en">
    <p>When this element appears within the <gi>creation</gi>
element it documents the set of revision campaigns or stages
identified during the evolution of the original text. When it appears within
the <gi>revisionDesc</gi> element, it documents only changes made
during the evolution of the encoded representation of that text.</p>
  </remarks>
  <listRef>
    <ptr target="#HD6"/>
    <ptr target="#PH-changes"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-14" xml:lang="en">groups a number of change descriptions associated 
with either the creation of a source text or the revision of an encoded text.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>  
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/> 
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="listChange"/>
        <elementRef key="change"/>
      </alternate>
    </sequence>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-04-14" xml:lang="en">indicates whether the ordering of its child <gi>change</gi>
elements is to be considered significant or not.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>true</defaultVal>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listChange-egXML-ne">
      <revisionDesc>
        <listChange>
          <change when="1991-11-11" who="#LB"> deleted chapter 10 </change>
          <change when="1991-11-02" who="#MSM"> completed first draft </change>
        </listChange>
      </revisionDesc>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listChange-egXML-cx">
      <profileDesc>
        <creation>
          <listChange ordered="true">
            <change xml:id="CHG-1">First stage, written in ink by a writer</change>
            <change xml:id="CHG-2">Second stage, written in Goethe's hand using pencil</change>
            <change xml:id="CHG-3">Fixation of the revised passages and further revisions by
Goethe using ink</change>
            <change xml:id="CHG-4">Addition of another stanza in a          different hand,
probably at a later stage</change>
          </listChange>
        </creation>
      </profileDesc>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listChange-remarks" versionDate="2013-04-14" xml:lang="en">
    <p>When this element appears within the <gi>creation</gi>
element it documents the set of revision campaigns or stages
identified during the evolution of the original text. When it appears within
the <gi>revisionDesc</gi> element, it documents only changes made
during the evolution of the encoded representation of that text.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD6"/>
    <ptr target="#PH-changes"/>
  </listRef>
```

^b10

