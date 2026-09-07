---
type: representation
source-type: document
source: '[[00_sources/tei-p5-geo-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 geo
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/geo.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# geo

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4165. Git blob: `d96a239779afefd5729bb25213b49b063cab9af7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-geo" ident="geo">
  <gloss versionDate="2007-06-15" xml:lang="en">geographical coordinates</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">지리적 좌표</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">coordenadas geográficas</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">coordonnées géographiques</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">coordinate geografiche</gloss>
  <desc versionDate="2007-06-15" xml:lang="en">contains any expression of a set of geographic coordinates, representing a point, line, or area on the surface of the earth in some
        notation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">특정 표기법으로 지표상 지점, 선, 영역을 표시하는 지리적 좌표의 집합 표현을 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene cualquier expresión de un conjunto de coordenadas geográficas, representando un punto, línea o
        área en la superficie de la tierra en alguna anotación.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">地球上の一点、線、領域を表すための、地理上の座標を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient toute expression, dans un système de notation, d'un ensemble de coordonnées géographiques
        représentant un point, une ligne ou une zone sur la surface de la Terre.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una qualsiasi espressione di una serie di coordinate geografiche che rappresenti un punto, una
        linea o un'area sulla superficie della terra in una data notazione</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="model.measureLike"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <exemplum xml:lang="und">
    <!--  RIB 262. A tombstone plus six lines of
	 Anglo-Saxon text. Still in situ at Church of St. Mary-le-Wigford in
	 Lincoln. Prose description is: "built into the west tower (on the south side
	 of the archway, at 8 ft. above the ground)" -->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geo-egXML-zd">
      <geoDecl xml:id="WGS" datum="WGS84">World Geodetic System</geoDecl>
      <geoDecl xml:id="OS" datum="OSGB36">Ordnance Survey</geoDecl>
      <!-- ... -->
      <location>
        <desc>A tombstone plus six lines of
	 Anglo-Saxon text, built into the west tower (on the south side
	 of the archway, at 8 ft. above the ground) of the
	 Church of St. Mary-le-Wigford in Lincoln.</desc>
        <geo decls="#WGS">53.226658 -0.541254</geo>
        <geo decls="#OS">SK 97481 70947</geo>
      </location>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geo-egXML-lu">
      <geo>41.687142 -74.870109</geo>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geo-egXML-vl">
      <geo decls="#BYDEGREES">W 8°37'--W 6°00'/N 34°00'--N 31°57'</geo>
    </egXML>
  </exemplum>
  <remarks ident="geo-remarks" versionDate="2013-02-02" xml:lang="en">
    <p>Uses of <gi>geo</gi> can be associated with a coordinate
    system, defined by a <gi>geoDecl</gi> element supplied in the TEI
    header, using the <att>decls</att> attribute. If no such link is
    made, the assumption is that the content of each <gi>geo</gi>
    element will be a pair of numbers separated by whitespace, to be
    interpreted as latitude followed by longitude according to the
    World Geodetic System.</p>
  </remarks>
  <listRef>
    <ptr target="#NDGEOGva" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-15" xml:lang="en">geographical coordinates</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">지리적 좌표</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">coordenadas geográficas</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">coordonnées géographiques</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">coordinate geografiche</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-06-15" xml:lang="en">contains any expression of a set of geographic coordinates, representing a point, line, or area on the surface of the earth in some
        notation.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">특정 표기법으로 지표상 지점, 선, 영역을 표시하는 지리적 좌표의 집합 표현을 포함한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene cualquier expresión de un conjunto de coordenadas geográficas, representando un punto, línea o
        área en la superficie de la tierra en alguna anotación.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">地球上の一点、線、領域を表すための、地理上の座標を示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient toute expression, dans un système de notation, d'un ensemble de coordonnées géographiques
        représentant un point, une ligne ou une zone sur la surface de la Terre.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una qualsiasi espressione di una serie di coordinate geografiche che rappresenti un punto, una
        linea o un'area sulla superficie della terra in una data notazione</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="model.measureLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <!--  RIB 262. A tombstone plus six lines of
	 Anglo-Saxon text. Still in situ at Church of St. Mary-le-Wigford in
	 Lincoln. Prose description is: "built into the west tower (on the south side
	 of the archway, at 8 ft. above the ground)" -->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geo-egXML-zd">
      <geoDecl xml:id="WGS" datum="WGS84">World Geodetic System</geoDecl>
      <geoDecl xml:id="OS" datum="OSGB36">Ordnance Survey</geoDecl>
      <!-- ... -->
      <location>
        <desc>A tombstone plus six lines of
	 Anglo-Saxon text, built into the west tower (on the south side
	 of the archway, at 8 ft. above the ground) of the
	 Church of St. Mary-le-Wigford in Lincoln.</desc>
        <geo decls="#WGS">53.226658 -0.541254</geo>
        <geo decls="#OS">SK 97481 70947</geo>
      </location>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geo-egXML-lu">
      <geo>41.687142 -74.870109</geo>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geo-egXML-vl">
      <geo decls="#BYDEGREES">W 8°37'--W 6°00'/N 34°00'--N 31°57'</geo>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="geo-remarks" versionDate="2013-02-02" xml:lang="en">
    <p>Uses of <gi>geo</gi> can be associated with a coordinate
    system, defined by a <gi>geoDecl</gi> element supplied in the TEI
    header, using the <att>decls</att> attribute. If no such link is
    made, the assumption is that the content of each <gi>geo</gi>
    element will be a pair of numbers separated by whitespace, to be
    interpreted as latitude followed by longitude according to the
    World Geodetic System.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDGEOGva" type="div3"/>
  </listRef>
```

^b18

