---
type: representation
source-type: document
source: '[[00_sources/tei-p5-location-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 location
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/location.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# location

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3781. Git blob: `435e66087650aad9badb19ae7928138ae8e51179`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="location" xml:id="gi-location" module="namesdates">
  <gloss versionDate="2008-12-09" xml:lang="en">location</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">localisation</gloss>
  <desc versionDate="2012-02-14" xml:lang="en">defines the location of a place as a set of geographical coordinates, in terms of other named geo-political entities, or as an address.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다른 이름의 지리-정치적 개체를 통하여 지리적 좌표의 집합으로, 또는 주소로 장소의 위치를 정의한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">define la localización de un lugar como conjunto de coordenadas geográficas, en términos de alguna entidades geopolítica dada, o como dirección.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">地理上の座標集合、地政学上の名前付き実体、アドレスなどにより場所を定 義する。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">définit l'emplacement d'un lieu par des coordonnées géographiques, en termes d'entités nommées dites géopolitiques, ou par une adresse.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">definisce la posizione di un luogo tramite una serie di coordinate geografiche, in termini di entità geopolitiche definite da altri o sotto forma di indirizzo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="precision"/>
      <classRef key="model.labelLike"/>
      <classRef key="model.placeNamePart"/>
      <classRef key="model.offsetLike"/>
      <classRef key="model.measureLike"/>
      <classRef key="model.addressLike"/>
      <classRef key="model.noteLike"/>
      <classRef key="model.biblLike"/>
    </alternate>    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-location-egXML-ot">
      <place>
        <placeName>Abbey Dore</placeName>
        <location>
          <geo>51.969604 -2.893146</geo>
        </location>
      </place>
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-location-egXML-pm">
      <place xml:id="BGbuilding" type="building">
        <placeName>Brasserie Georges</placeName>
        <location>
          <country key="FR"/>
          <settlement type="city">Lyon</settlement>
          <district type="arrondissement">IIème</district>
          <district type="quartier">Perrache</district>
          <placeName type="street"><num>30</num>, Cours de Verdun</placeName>
        </location>
      </place>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-location-egXML-ij">
      <place type="imaginary">
        <placeName>Atlantis</placeName>
        <location>
          <offset>beyond</offset>
          <placeName>The Pillars of <persName>Hercules</persName>
               </placeName>
        </location>
      </place>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDGEOG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">location</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">localisation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-02-14" xml:lang="en">defines the location of a place as a set of geographical coordinates, in terms of other named geo-political entities, or as an address.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다른 이름의 지리-정치적 개체를 통하여 지리적 좌표의 집합으로, 또는 주소로 장소의 위치를 정의한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">define la localización de un lugar como conjunto de coordenadas geográficas, en términos de alguna entidades geopolítica dada, o como dirección.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">地理上の座標集合、地政学上の名前付き実体、アドレスなどにより場所を定 義する。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">définit l'emplacement d'un lieu par des coordonnées géographiques, en termes d'entités nommées dites géopolitiques, ou par une adresse.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">definisce la posizione di un luogo tramite una serie di coordinate geografiche, in termini di entità geopolitiche definite da altri o sotto forma di indirizzo.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="precision"/>
      <classRef key="model.labelLike"/>
      <classRef key="model.placeNamePart"/>
      <classRef key="model.offsetLike"/>
      <classRef key="model.measureLike"/>
      <classRef key="model.addressLike"/>
      <classRef key="model.noteLike"/>
      <classRef key="model.biblLike"/>
    </alternate>    
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-location-egXML-ot">
      <place>
        <placeName>Abbey Dore</placeName>
        <location>
          <geo>51.969604 -2.893146</geo>
        </location>
      </place>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-location-egXML-pm">
      <place xml:id="BGbuilding" type="building">
        <placeName>Brasserie Georges</placeName>
        <location>
          <country key="FR"/>
          <settlement type="city">Lyon</settlement>
          <district type="arrondissement">IIème</district>
          <district type="quartier">Perrache</district>
          <placeName type="street"><num>30</num>, Cours de Verdun</placeName>
        </location>
      </place>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-location-egXML-ij">
      <place type="imaginary">
        <placeName>Atlantis</placeName>
        <location>
          <offset>beyond</offset>
          <placeName>The Pillars of <persName>Hercules</persName>
               </placeName>
        </location>
      </place>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDGEOG"/>
  </listRef>
```

^b14

