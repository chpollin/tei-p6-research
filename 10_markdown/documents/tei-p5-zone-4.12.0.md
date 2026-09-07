---
type: representation
source-type: document
source: '[[00_sources/tei-p5-zone-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 zone
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/zone.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# zone

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6033. Git blob: `25195999fe6a3e5e0b97b3f0741940119ac7e5ff`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="zone" xml:id="gi-zone" module="transcr">
  <desc versionDate="2011-11-20" xml:lang="en">defines any two-dimensional or three-dimensional area within a <gi>surface</gi>
element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><gi>surface</gi> 요소 내에 포함된 직사각형 영역을 정의한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">define el área rectangular de la <gi>superficie</gi>.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素<gi>surface</gi>にある表面上の矩形範囲を定義する。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">définit une surface planaire de tout type par rapport à un élément <gi>surface</gi>.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">definisce un'area bidimensionale contenuta all'interno di un elemento <gi>surface</gi></desc>
  <desc versionDate="2018-04-15" xml:lang="de">beschreibt eine beliebige zweidimensionale Fläche innerhalb eines
    <gi>surface</gi>-Elements.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.coordinated"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.graphicLike"/>
      <classRef key="model.global"/>
      <elementRef key="surface"/>
      <classRef key="model.linePart"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="rotate">
      <desc versionDate="2011-10-31" xml:lang="en">indicates the amount by which this zone has been
         rotated clockwise, with respect to the normal orientation of
         the parent <gi>surface</gi> element as implied by the
         dimensions given in the <gi>msDesc</gi> element or by the
         coordinates of the <gi>surface</gi> itself. The orientation
         is expressed in arc degrees.</desc>
      <desc versionDate="2018-04-15" xml:lang="de">gibt das Ausmaß der Drehung (im Uhrzeigersinn) dieser <gi>zone</gi> an.
        Als Bezugspunkt gilt dabei die natürliche Ausrichtung des <gi>surface</gi>-Elternelements, die entweder
        im <gi>msDesc</gi>-Element beschrieben ist oder durch die Koordinaten des <gi>surface</gi>-Elements selbst.
        Die Drehung wird in Bogengrad angegeben.</desc>
      <datatype minOccurs="1" maxOccurs="1"><dataRef key="teidata.numeric"/></datatype>
      <defaultVal>0</defaultVal>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-zone-egXML-nw" source="#UND">
      <surface ulx="14.54" uly="16.14" lrx="0" lry="0">
        <graphic url="stone.jpg"/>
        <zone points="4.6,6.3 5.25,5.85 6.2,6.6 8.19222,7.4125 9.89222,6.5875 10.9422,6.1375 11.4422,6.7125 8.21722,8.3125 6.2,7.65"/>
      </surface>
    </egXML>
    <p>This example defines a non-rectangular zone: see the illustration
in section <ptr target="#PH-surfzone"/>.    </p>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-zone-egXML-bw" source="#UND">
      <facsimile>
        <surface ulx="50" uly="20" lrx="400" lry="280">
          <zone ulx="0" uly="0" lrx="500" lry="321">
            <graphic url="graphic.png"/>
          </zone>
        </surface>
      </facsimile>
    </egXML>
    <p>This example defines a zone which has been defined as larger than its parent
surface in order to match the dimensions of the graphic it contains.</p>
  </exemplum>
  <remarks ident="zone-remarks" versionDate="2018-04-08" xml:lang="en">
    <p>The position of every zone for a given surface is always
defined by reference to the coordinate system defined for that
surface. </p>
    <p>A graphic element contained by a zone represents the whole
of the zone.</p>
    <p>A zone may be of any shape. The attribute <att>points</att> may be
used to define a polygonal zone, using the coordinate system defined
by its parent surface.</p>
    <p>A zone is always a closed polygon. Repeating the initial coordinate
    at the end of the sequence is optional. To encode an 
    unclosed path, use the <gi>path</gi> element.</p>
  </remarks>
  <remarks ident="zone-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La position de chaque zone pour une surface donnée est toujours définie par rapport au système de coordonnées défini pour cette surface. Tout élément graphique contenu par une zone se représente par toute la zone.</p>
  </remarks>
  <remarks ident="zone-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
要素<gi>zone</gi>が表す場所は全て、左表システムを参照して定義される。
当該要素<gi>zone</gi>に含まれる要素<gi>graphic</gi>は、当該要素
<gi>zone</gi>が表す面全体を示す。
</p>
  </remarks>
  <remarks ident="zone-remarks" versionDate="2018-04-15" xml:lang="de">
    <p>Die Position jeder <gi>zone</gi> einer <gi>surface</gi> ist
      immer durch Bezugnahme auf das Koordinatensystem dieser
      <gi>surface</gi> definiert. </p>
    <p>Ein <gi>graphic</gi>-Element innerhalb eines <gi>zone</gi>-Elements
      repräsentiert stets die gesamte <gi>zone</gi>. </p>
    <p>Eine <gi>zone</gi> kann jede beliebige Form haben.
      Das <att>points</att>-Attribute kann genutzt werden, um ein Polygon 
      zu beschreiben. Hierbei gilt das Koordinatensystem des 
      <gi>surface</gi>-Elternelements als Referenz. </p>
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
<desc versionDate="2011-11-20" xml:lang="en">defines any two-dimensional or three-dimensional area within a <gi>surface</gi>
element.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><gi>surface</gi> 요소 내에 포함된 직사각형 영역을 정의한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">define el área rectangular de la <gi>superficie</gi>.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素<gi>surface</gi>にある表面上の矩形範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">définit une surface planaire de tout type par rapport à un élément <gi>surface</gi>.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">definisce un'area bidimensionale contenuta all'interno di un elemento <gi>surface</gi></desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2018-04-15" xml:lang="de">beschreibt eine beliebige zweidimensionale Fläche innerhalb eines
    <gi>surface</gi>-Elements.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.coordinated"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.graphicLike"/>
      <classRef key="model.global"/>
      <elementRef key="surface"/>
      <classRef key="model.linePart"/>
    </alternate>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-10-31" xml:lang="en">indicates the amount by which this zone has been
         rotated clockwise, with respect to the normal orientation of
         the parent <gi>surface</gi> element as implied by the
         dimensions given in the <gi>msDesc</gi> element or by the
         coordinates of the <gi>surface</gi> itself. The orientation
         is expressed in arc degrees.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2018-04-15" xml:lang="de">gibt das Ausmaß der Drehung (im Uhrzeigersinn) dieser <gi>zone</gi> an.
        Als Bezugspunkt gilt dabei die natürliche Ausrichtung des <gi>surface</gi>-Elternelements, die entweder
        im <gi>msDesc</gi>-Element beschrieben ist oder durch die Koordinaten des <gi>surface</gi>-Elements selbst.
        Die Drehung wird in Bogengrad angegeben.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="1"><dataRef key="teidata.numeric"/></datatype>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>0</defaultVal>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-zone-egXML-nw" source="#UND">
      <surface ulx="14.54" uly="16.14" lrx="0" lry="0">
        <graphic url="stone.jpg"/>
        <zone points="4.6,6.3 5.25,5.85 6.2,6.6 8.19222,7.4125 9.89222,6.5875 10.9422,6.1375 11.4422,6.7125 8.21722,8.3125 6.2,7.65"/>
      </surface>
    </egXML>
    <p>This example defines a non-rectangular zone: see the illustration
in section <ptr target="#PH-surfzone"/>.    </p>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-zone-egXML-bw" source="#UND">
      <facsimile>
        <surface ulx="50" uly="20" lrx="400" lry="280">
          <zone ulx="0" uly="0" lrx="500" lry="321">
            <graphic url="graphic.png"/>
          </zone>
        </surface>
      </facsimile>
    </egXML>
    <p>This example defines a zone which has been defined as larger than its parent
surface in order to match the dimensions of the graphic it contains.</p>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="zone-remarks" versionDate="2018-04-08" xml:lang="en">
    <p>The position of every zone for a given surface is always
defined by reference to the coordinate system defined for that
surface. </p>
    <p>A graphic element contained by a zone represents the whole
of the zone.</p>
    <p>A zone may be of any shape. The attribute <att>points</att> may be
used to define a polygonal zone, using the coordinate system defined
by its parent surface.</p>
    <p>A zone is always a closed polygon. Repeating the initial coordinate
    at the end of the sequence is optional. To encode an 
    unclosed path, use the <gi>path</gi> element.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="zone-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La position de chaque zone pour une surface donnée est toujours définie par rapport au système de coordonnées défini pour cette surface. Tout élément graphique contenu par une zone se représente par toute la zone.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="zone-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
要素<gi>zone</gi>が表す場所は全て、左表システムを参照して定義される。
当該要素<gi>zone</gi>に含まれる要素<gi>graphic</gi>は、当該要素
<gi>zone</gi>が表す面全体を示す。
</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="zone-remarks" versionDate="2018-04-15" xml:lang="de">
    <p>Die Position jeder <gi>zone</gi> einer <gi>surface</gi> ist
      immer durch Bezugnahme auf das Koordinatensystem dieser
      <gi>surface</gi> definiert. </p>
    <p>Ein <gi>graphic</gi>-Element innerhalb eines <gi>zone</gi>-Elements
      repräsentiert stets die gesamte <gi>zone</gi>. </p>
    <p>Eine <gi>zone</gi> kann jede beliebige Form haben.
      Das <att>points</att>-Attribute kann genutzt werden, um ein Polygon 
      zu beschreiben. Hierbei gilt das Koordinatensystem des 
      <gi>surface</gi>-Elternelements als Referenz. </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHFAX"/>
    <ptr target="#PHZLAB"/>
  </listRef>
```

^b20

