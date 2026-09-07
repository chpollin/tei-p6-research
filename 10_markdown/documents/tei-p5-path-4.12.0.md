---
type: representation
source-type: document
source: '[[00_sources/tei-p5-path-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 path
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/path.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# path

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4054. Git blob: `381b0b5acc4cac60c921605d520e653e2cc95a32`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="path" xml:id="gi-path" module="transcr">
  <gloss versionDate="2018-07-13" xml:lang="en">path</gloss>
  <desc versionDate="2018-03-28" xml:lang="en">defines any line passing through two or more points within a <gi>surface</gi>
element.</desc>
  <gloss versionDate="2018-07-13" xml:lang="de">Pfad</gloss>
  <desc versionDate="2018-07-13" xml:lang="de">definiert eine beliebige Linie, die durch zwei oder mehr Punkte innerhalb eines <gi>surface</gi> Elements verläuft.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.coordinated"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.linePart"/>
  </classes>
  <content>
    <empty/>
  </content>
  
  <constraintSpec ident="pathmustnotbeclosed" scheme="schematron" xml:lang="en">
    <desc versionDate="2023-04-11" xml:lang="en">
      Since a <gi>path</gi> represents a line with distinct start and
      end points, the last coordinate should not be the same as the
      first coordinate.
    </desc>
    <constraint>
      <sch:rule context="tei:path[@points]">
        <sch:let name="firstPair" value="tokenize( normalize-space( @points ), ' ')[1]"/>
        <sch:let name="lastPair" value="tokenize( normalize-space( @points ), ' ')[last()]"/>
        <sch:let name="firstX" value="xs:float( substring-before( $firstPair, ',') )"/>
        <sch:let name="firstY" value="xs:float( substring-after( $firstPair, ',') )"/>
        <sch:let name="lastX" value="xs:float( substring-before( $lastPair, ',') )"/>
        <sch:let name="lastY" value="xs:float( substring-after( $lastPair, ',') )"/>
        <sch:report test="$firstX eq $lastX and $firstY eq $lastY">The first and
          last elements of this path are the same. To specify a closed polygon, use
          the &lt;zone> element rather than the &lt;path> element. </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  
  <attList>
    <attDef ident="points" mode="change">
      <desc versionDate="2018-03-28" xml:lang="en">identifies a line 
        within the container or bounding box
        specified by the parent element by means of
        a series of two or more pairs of numbers, each of which 
        gives the x,y coordinates
        of a point on the line.</desc>
      <desc versionDate="2018-07-13" xml:lang="de">beschreibt eine Linie innerhalb eines Begrenzungsrahmens, der durch das Elternelement definiert ist, über eine Reihe von zwei oder mehr Zahlenpaaren, die jeweils die X- und Y-Koordinaten eines Punktes dieser Linie angeben.</desc>
      <datatype minOccurs="2" maxOccurs="unbounded"><dataRef key="teidata.point"/></datatype>
    </attDef>
  </attList>
  
  
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-path-egXML-ym" source="#UND">
      <surface ulx="0" uly="0" lrx="443" lry="272">
        <graphic url="facs-fig3.jpg"/>
        <path points="74,73 171,244"/>
        <path points="71,203 173,116"/>
      </surface>
    </egXML>
  </exemplum>
  
  <remarks ident="path-remarks" versionDate="2018-10-07" xml:lang="en">
    <p>Although the simplest form of a path is a straight line between
    two points, a line with more than two points may bend at any point. The order
    of coordinates in <att>points</att> is significant, because the line follows
    the coordinate sequence.</p>
      <p>To specify a closed polygon, use
        the <gi>zone</gi> element rather than the <gi>path</gi> element. </p>
    </remarks>

  <listRef>
    <ptr target="#PHFAX"/>
    <ptr target="#PHZLAB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2018-07-13" xml:lang="en">path</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-03-28" xml:lang="en">defines any line passing through two or more points within a <gi>surface</gi>
element.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2018-07-13" xml:lang="de">Pfad</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2018-07-13" xml:lang="de">definiert eine beliebige Linie, die durch zwei oder mehr Punkte innerhalb eines <gi>surface</gi> Elements verläuft.</desc>
```

^b4

### Block 5

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

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <empty/>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="pathmustnotbeclosed" scheme="schematron" xml:lang="en">
    <desc versionDate="2023-04-11" xml:lang="en">
      Since a <gi>path</gi> represents a line with distinct start and
      end points, the last coordinate should not be the same as the
      first coordinate.
    </desc>
    <constraint>
      <sch:rule context="tei:path[@points]">
        <sch:let name="firstPair" value="tokenize( normalize-space( @points ), ' ')[1]"/>
        <sch:let name="lastPair" value="tokenize( normalize-space( @points ), ' ')[last()]"/>
        <sch:let name="firstX" value="xs:float( substring-before( $firstPair, ',') )"/>
        <sch:let name="firstY" value="xs:float( substring-after( $firstPair, ',') )"/>
        <sch:let name="lastX" value="xs:float( substring-before( $lastPair, ',') )"/>
        <sch:let name="lastY" value="xs:float( substring-after( $lastPair, ',') )"/>
        <sch:report test="$firstX eq $lastX and $firstY eq $lastY">The first and
          last elements of this path are the same. To specify a closed polygon, use
          the &lt;zone> element rather than the &lt;path> element. </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2018-03-28" xml:lang="en">identifies a line 
        within the container or bounding box
        specified by the parent element by means of
        a series of two or more pairs of numbers, each of which 
        gives the x,y coordinates
        of a point on the line.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2018-07-13" xml:lang="de">beschreibt eine Linie innerhalb eines Begrenzungsrahmens, der durch das Elternelement definiert ist, über eine Reihe von zwei oder mehr Zahlenpaaren, die jeweils die X- und Y-Koordinaten eines Punktes dieser Linie angeben.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="2" maxOccurs="unbounded"><dataRef key="teidata.point"/></datatype>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-path-egXML-ym" source="#UND">
      <surface ulx="0" uly="0" lrx="443" lry="272">
        <graphic url="facs-fig3.jpg"/>
        <path points="74,73 171,244"/>
        <path points="71,203 173,116"/>
      </surface>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="path-remarks" versionDate="2018-10-07" xml:lang="en">
    <p>Although the simplest form of a path is a straight line between
    two points, a line with more than two points may bend at any point. The order
    of coordinates in <att>points</att> is significant, because the line follows
    the coordinate sequence.</p>
      <p>To specify a closed polygon, use
        the <gi>zone</gi> element rather than the <gi>path</gi> element. </p>
    </remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHFAX"/>
    <ptr target="#PHZLAB"/>
  </listRef>
```

^b13

