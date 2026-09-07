---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listevent-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listEvent
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listEvent.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listEvent

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4537. Git blob: `8b9844571a8d908c399ee292fa72802ee8249a26`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-listEvent" ident="listEvent">
  <gloss versionDate="2009-01-21" xml:lang="en">list of events</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">liste d'événements</gloss>
  <gloss versionDate="2021-02-02" xml:lang="it">list di eventi</gloss>
  <desc versionDate="2009-01-21" xml:lang="en">contains a list of descriptions, each of which provides information about an identifiable event.</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient une liste de descriptions, chacune d'entre elles fournissant des informations sur un événement connu.</desc>
  <desc versionDate="2021-02-02" xml:lang="it">contiene una lista di descrizioni, ognuna delle quali fornisce informazioni a proposito di un determinato evento.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.eventLike"/>
    <memberOf key="model.listLike"/>
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
        <classRef key="model.eventLike" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <constraintSpec ident="listEvent-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listEvent"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listEvent-egXML-ad">
      <listEvent>
        <head>Battles of the American Civil War: Kentucky</head>
        <event xml:id="event01" when="1861-09-19">
          <label>Barbourville</label>
          <desc>The Battle of Barbourville was one of the early engagements of
the American Civil War. It occurred September 19, 1861, in Knox
County, Kentucky during the campaign known as the Kentucky Confederate
Offensive. The battle is considered the first Confederate victory in
the commonwealth, and threw a scare into Federal commanders, who
rushed troops to central Kentucky in an effort to repel the invasion,
which was finally thwarted at the <ref target="#event02">Battle of
Camp Wildcat</ref> in October.</desc>
        </event>
        <event xml:id="event02" when="1861-10-21">
          <label>Camp Wild Cat</label>
          <desc>
The Battle of Camp Wildcat (also known as Wildcat Mountain and Camp
Wild Cat) was one of the early engagements of the American Civil
War. It occurred October 21, 1861, in northern Laurel County, Kentucky
during the campaign known as the Kentucky Confederate Offensive. The
battle is considered one of the very first Union victories, and marked
the first engagement of troops in the commonwealth of Kentucky.</desc>
        </event>
        <event xml:id="event03" from="1864-06-11" to="1864-06-12">
          <label>Cynthiana</label>
          <desc>The Battle of Cynthiana (or Kellar’s Bridge) was an engagement
during the American Civil War that was fought on June 11 and 12, 1864,
in Harrison County, Kentucky, near the town of Cynthiana. A part of
Confederate Brigadier General John Hunt Morgan's 1864 Raid into
Kentucky, the battle resulted in a victory by Union forces over the
raiders and saved the town from capture.</desc>
        </event>
      </listEvent>
    </egXML>
  </exemplum>
  <!-- text from wikipedia -->
  <listRef>
    <ptr target="#NDPERSbp"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-21" xml:lang="en">list of events</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="fr">liste d'événements</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2021-02-02" xml:lang="it">list di eventi</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2009-01-21" xml:lang="en">contains a list of descriptions, each of which provides information about an identifiable event.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient une liste de descriptions, chacune d'entre elles fournissant des informations sur un événement connu.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2021-02-02" xml:lang="it">contiene una lista di descrizioni, ognuna delle quali fornisce informazioni a proposito di un determinato evento.</desc>
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
    <memberOf key="model.eventLike"/>
    <memberOf key="model.listLike"/>
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
        <classRef key="model.eventLike" minOccurs="1" maxOccurs="unbounded"/>
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
<constraintSpec ident="listEvent-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listEvent"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listEvent-egXML-ad">
      <listEvent>
        <head>Battles of the American Civil War: Kentucky</head>
        <event xml:id="event01" when="1861-09-19">
          <label>Barbourville</label>
          <desc>The Battle of Barbourville was one of the early engagements of
the American Civil War. It occurred September 19, 1861, in Knox
County, Kentucky during the campaign known as the Kentucky Confederate
Offensive. The battle is considered the first Confederate victory in
the commonwealth, and threw a scare into Federal commanders, who
rushed troops to central Kentucky in an effort to repel the invasion,
which was finally thwarted at the <ref target="#event02">Battle of
Camp Wildcat</ref> in October.</desc>
        </event>
        <event xml:id="event02" when="1861-10-21">
          <label>Camp Wild Cat</label>
          <desc>
The Battle of Camp Wildcat (also known as Wildcat Mountain and Camp
Wild Cat) was one of the early engagements of the American Civil
War. It occurred October 21, 1861, in northern Laurel County, Kentucky
during the campaign known as the Kentucky Confederate Offensive. The
battle is considered one of the very first Union victories, and marked
the first engagement of troops in the commonwealth of Kentucky.</desc>
        </event>
        <event xml:id="event03" from="1864-06-11" to="1864-06-12">
          <label>Cynthiana</label>
          <desc>The Battle of Cynthiana (or Kellar’s Bridge) was an engagement
during the American Civil War that was fought on June 11 and 12, 1864,
in Harrison County, Kentucky, near the town of Cynthiana. A part of
Confederate Brigadier General John Hunt Morgan's 1864 Raid into
Kentucky, the battle resulted in a victory by Union forces over the
raiders and saved the town from capture.</desc>
        </event>
      </listEvent>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSbp"/>
  </listRef>
```

^b11

