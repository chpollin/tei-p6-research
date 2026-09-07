---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listobject-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listObject
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listObject.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listObject

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5317. Git blob: `8a38911163f6e38b0c6990c3c1dd9a1aae26f9cb`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-listObject" ident="listObject">
  <gloss versionDate="2018-07-15" xml:lang="en">list of objects</gloss>
  <gloss versionDate="2019-01-22" xml:lang="de">Liste der Objekte</gloss>
  <gloss versionDate="2021-02-02" xml:lang="it">lista di oggetti</gloss>
  <desc versionDate="2019-01-22" xml:lang="en">contains a list of descriptions, each of which provides information about an
    identifiable physical object.</desc>
  <desc versionDate="2019-01-22" xml:lang="de">enthält eine Liste von Beschreibungen, die jeweils Informationen zu einem identifizierbaren physischen Objekt liefern.</desc>
  <desc versionDate="2021-02-02" xml:lang="it">contiene una lista di descrizioni, ognuna delle quali fornisce informazioni a proposito di un determinato oggetto fisico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
    <memberOf key="model.objectLike"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.objectLike" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <constraintSpec ident="listObject-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listObject"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listObject-egXML-ys" source="#UND">
      <listObject>
        <object xml:id="AlfredJewel">
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
          <physDesc>
            <p> The Alfred Jewel is about 6.4 cm in length and is made of combination of filigreed <material>gold</material>
              surrounding a polished teardrop shaped piece of transparent <material>quartz</material>. Underneath the rock crystal
              is a cloisonné enamel image of a man with ecclesiastical symbols. The sides of the jewel holding the crystal in
              place contain an openwork inscription saying "AELFRED MEC HEHT GEWYRCAN", meaning 'Alfred ordered me made'. </p>
          </physDesc>
          <history>
            <origin>It is generally accepted that the Alfred Jewel dates from the <origDate>late 9th Century</origDate> and was
              most likely made in <origPlace>England</origPlace>. </origin>
            <provenance when="1693">The jewel was discovered in 1693 at Petherton Park, North Petherton in the English county of
              Somerset, on land owned by Sir Thomas Wroth. North Petherton is about 8 miles away from Athelney, where King Alfred
              founded a monastery. </provenance>
            <provenance when="1698">A description of the Alfred Jewel was first published in 1698, in the Philosophical
              Transactions of the Royal Society.</provenance>
            <acquisition> It was bequeathed to Oxford University by Colonel Nathaniel Palmer (c. 1661-1718) and today is in the
              Ashmolean Museum in Oxford. </acquisition>
          </history>
        </object>
      </listObject>
    </egXML>
  </exemplum>
  <remarks ident="listObject-remarks" versionDate="2019-01-22" xml:lang="en">
    <p rend="dataDesc">The <att>type</att> attribute may be used to distinguish different types of objects.</p>
  </remarks>
  <remarks ident="listObject-remarks" versionDate="2019-01-22" xml:lang="de">
    <p rend="dataDesc">Das <att>type</att>-Attribut kann verwendet werden, um unterschiedliche Typen von Objekten zu unterscheiden.</p>
  </remarks>


  <listRef>
    <ptr target="#NDOBJ"/>
  </listRef>

</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2018-07-15" xml:lang="en">list of objects</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2019-01-22" xml:lang="de">Liste der Objekte</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2021-02-02" xml:lang="it">lista di oggetti</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-22" xml:lang="en">contains a list of descriptions, each of which provides information about an
    identifiable physical object.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-01-22" xml:lang="de">enthält eine Liste von Beschreibungen, die jeweils Informationen zu einem identifizierbaren physischen Objekt liefern.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2021-02-02" xml:lang="it">contiene una lista di descrizioni, ognuna delle quali fornisce informazioni a proposito di un determinato oggetto fisico.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
    <memberOf key="model.objectLike"/>
  </classes>
```

^b7

### Block 8

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.objectLike" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
```

^b8

### Block 9

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="listObject-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listObject"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listObject-egXML-ys" source="#UND">
      <listObject>
        <object xml:id="AlfredJewel">
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
          <physDesc>
            <p> The Alfred Jewel is about 6.4 cm in length and is made of combination of filigreed <material>gold</material>
              surrounding a polished teardrop shaped piece of transparent <material>quartz</material>. Underneath the rock crystal
              is a cloisonné enamel image of a man with ecclesiastical symbols. The sides of the jewel holding the crystal in
              place contain an openwork inscription saying "AELFRED MEC HEHT GEWYRCAN", meaning 'Alfred ordered me made'. </p>
          </physDesc>
          <history>
            <origin>It is generally accepted that the Alfred Jewel dates from the <origDate>late 9th Century</origDate> and was
              most likely made in <origPlace>England</origPlace>. </origin>
            <provenance when="1693">The jewel was discovered in 1693 at Petherton Park, North Petherton in the English county of
              Somerset, on land owned by Sir Thomas Wroth. North Petherton is about 8 miles away from Athelney, where King Alfred
              founded a monastery. </provenance>
            <provenance when="1698">A description of the Alfred Jewel was first published in 1698, in the Philosophical
              Transactions of the Royal Society.</provenance>
            <acquisition> It was bequeathed to Oxford University by Colonel Nathaniel Palmer (c. 1661-1718) and today is in the
              Ashmolean Museum in Oxford. </acquisition>
          </history>
        </object>
      </listObject>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listObject-remarks" versionDate="2019-01-22" xml:lang="en">
    <p rend="dataDesc">The <att>type</att> attribute may be used to distinguish different types of objects.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="listObject-remarks" versionDate="2019-01-22" xml:lang="de">
    <p rend="dataDesc">Das <att>type</att>-Attribut kann verwendet werden, um unterschiedliche Typen von Objekten zu unterscheiden.</p>
  </remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDOBJ"/>
  </listRef>
```

^b13

