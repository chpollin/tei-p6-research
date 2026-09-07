---
type: representation
source-type: document
source: '[[00_sources/tei-p5-surfacegrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 surfaceGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/surfaceGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# surfaceGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2016. Git blob: `d66ab0989d348284d55bad723534a7faccc194e1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="surfaceGrp" xml:id="gi-surfaceGrp" module="transcr">
  <gloss versionDate="2022-06-09" xml:lang="en">surface group</gloss>
  <desc versionDate="2011-11-11" xml:lang="en">defines any kind of useful grouping of written surfaces, for
  example the recto and verso of a single leaf, which the encoder
  wishes to treat as a single unit.</desc>
  <classes>
    <memberOf key="att.global"/>
<!--    <memberOf key="att.coordinated"/> -->
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <!-- added by gen -->
  </classes>
  <content>
    
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.global"/>
        <elementRef key="surface"/>
        <elementRef key="surfaceGrp"/>
      </alternate>
    
  </content>
  <!-- need a rule to say at least two -->
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surfaceGrp-egXML-mz" source="#UND">
      <sourceDoc>
        <surfaceGrp>
          <surface ulx="0" uly="0" lrx="200" lry="300">
            <graphic url="Bovelles-49r.png"/>
          </surface>
          <surface ulx="0" uly="0" lrx="200" lry="300">
            <graphic url="Bovelles-49v.png"/>
          </surface>
        </surfaceGrp>
      </sourceDoc>
    </egXML>
  </exemplum>
  <remarks ident="surfaceGrp-remarks" versionDate="2011-11-11" xml:lang="en">
    <p>Where it is useful or meaningful to do so, any grouping of multiple
<gi>surface</gi> elements may be indicated using the
<gi>surfaceGrp</gi> elements. </p>
  </remarks>
  <listRef>
    <ptr target="#PHFAX"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2022-06-09" xml:lang="en">surface group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-11" xml:lang="en">defines any kind of useful grouping of written surfaces, for
  example the recto and verso of a single leaf, which the encoder
  wishes to treat as a single unit.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
<!--    <memberOf key="att.coordinated"/> -->
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <!-- added by gen -->
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.global"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surfaceGrp-egXML-mz" source="#UND">
      <sourceDoc>
        <surfaceGrp>
          <surface ulx="0" uly="0" lrx="200" lry="300">
            <graphic url="Bovelles-49r.png"/>
          </surface>
          <surface ulx="0" uly="0" lrx="200" lry="300">
            <graphic url="Bovelles-49v.png"/>
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
<remarks ident="surfaceGrp-remarks" versionDate="2011-11-11" xml:lang="en">
    <p>Where it is useful or meaningful to do so, any grouping of multiple
<gi>surface</gi> elements may be indicated using the
<gi>surfaceGrp</gi> elements. </p>
  </remarks>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHFAX"/>
  </listRef>
```

^b7

