---
type: representation
source-type: document
source: '[[00_sources/tei-p5-objectidentifier-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 objectIdentifier
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/objectIdentifier.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# objectIdentifier

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3280. Git blob: `fae43786022b5f1ee526c50f89bb6d15e0cefdfd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="objectIdentifier" ident="objectIdentifier">
  <gloss versionDate="2018-11-19" xml:lang="en">object identifier</gloss>
  <gloss versionDate="2019-01-22" xml:lang="de">Objektidentifikator</gloss>
  <desc versionDate="2018-10-26" xml:lang="en" xml:id="objectIdentifier.desc">groups one or more identifiers or pieces of locating information concerning a single object.</desc>
  <desc versionDate="2019-01-22" xml:lang="de">gruppiert einen oder mehrere Identifikatoren oder Teile von Lokalisierungsinformationen, die ein einzelnes Objekt betreffen.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.placeNamePart"/>
      <elementRef key="institution"/>
      <elementRef key="repository"/>
      <elementRef key="collection"/>
      <elementRef key="idno"/>
      <elementRef key="msName"/>
      <elementRef key="objectName"/>
      <elementRef key="altIdentifier"/>
      <elementRef key="address"/>
    </alternate>
   </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="objectIdentifier-egXML-sx">
      <objectIdentifier>
        <country>United Kingdom</country>
        <region>Oxfordshire</region>
        <settlement>Oxford</settlement>
        <institution>University of Oxford</institution>
        <repository>Ashmolean Museum</repository>
        <collection>English Treasures</collection>
        <idno type="ashmolean">AN1836p.135.371</idno>
        <idno type="wikipedia">https://en.wikipedia.org/wiki/Alfred_Jewel</idno>
        <objectName>Alfred Jewel</objectName>
      </objectIdentifier>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="objectIdentifier-egXML-xl">
      <object xml:id="Excalibur-MultipleNames">
        <objectIdentifier>
          <objectName type="main">Excalibur</objectName>
          <objectName type="alt">Caliburn</objectName>
          <objectName xml:lang="cy">Caledfwlch</objectName>
          <objectName xml:lang="cnx">Calesvol</objectName>
          <objectName xml:lang="br">Kaledvoulc'h</objectName>
          <objectName xml:lang="la">Caliburnus</objectName>
          <country>Wales</country> 
        </objectIdentifier>
        <p>Excalibur is the name for the legendary sword of King Arthur, in Welsh it is called Caledfwlch, 
          in Cornish it is called Calesvol, in Breton it is called Kaledvoulc'h, and in Latin it is called Caliburnus.
          In some versions Excalibur's blade was engraved with phrases on opposite sides which in translation read: 
          "Take me up" and "Cast me away" (or similar).</p>
      </object>
    </egXML>
   </exemplum>
  <listRef>
    <ptr target="#NDOBJ"/>
  </listRef>
  
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2018-11-19" xml:lang="en">object identifier</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2019-01-22" xml:lang="de">Objektidentifikator</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-10-26" xml:lang="en" xml:id="objectIdentifier.desc">groups one or more identifiers or pieces of locating information concerning a single object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-01-22" xml:lang="de">gruppiert einen oder mehrere Identifikatoren oder Teile von Lokalisierungsinformationen, die ein einzelnes Objekt betreffen.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.placeNamePart"/>
      <elementRef key="institution"/>
      <elementRef key="repository"/>
      <elementRef key="collection"/>
      <elementRef key="idno"/>
      <elementRef key="msName"/>
      <elementRef key="objectName"/>
      <elementRef key="altIdentifier"/>
      <elementRef key="address"/>
    </alternate>
   </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="objectIdentifier-egXML-sx">
      <objectIdentifier>
        <country>United Kingdom</country>
        <region>Oxfordshire</region>
        <settlement>Oxford</settlement>
        <institution>University of Oxford</institution>
        <repository>Ashmolean Museum</repository>
        <collection>English Treasures</collection>
        <idno type="ashmolean">AN1836p.135.371</idno>
        <idno type="wikipedia">https://en.wikipedia.org/wiki/Alfred_Jewel</idno>
        <objectName>Alfred Jewel</objectName>
      </objectIdentifier>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="objectIdentifier-egXML-xl">
      <object xml:id="Excalibur-MultipleNames">
        <objectIdentifier>
          <objectName type="main">Excalibur</objectName>
          <objectName type="alt">Caliburn</objectName>
          <objectName xml:lang="cy">Caledfwlch</objectName>
          <objectName xml:lang="cnx">Calesvol</objectName>
          <objectName xml:lang="br">Kaledvoulc'h</objectName>
          <objectName xml:lang="la">Caliburnus</objectName>
          <country>Wales</country> 
        </objectIdentifier>
        <p>Excalibur is the name for the legendary sword of King Arthur, in Welsh it is called Caledfwlch, 
          in Cornish it is called Calesvol, in Breton it is called Kaledvoulc'h, and in Latin it is called Caliburnus.
          In some versions Excalibur's blade was engraved with phrases on opposite sides which in translation read: 
          "Take me up" and "Cast me away" (or similar).</p>
      </object>
    </egXML>
   </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDOBJ"/>
  </listRef>
```

^b9

