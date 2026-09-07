---
type: representation
source-type: document
source: '[[00_sources/tei-p5-event-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 event
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/event.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# event

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11021. Git blob: `6ca9961cf96675b0771336c18fd54eb635582f3c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-event" ident="event">
  <gloss versionDate="2008-12-09" xml:lang="en">event</gloss>
  <gloss versionDate="2023-05-07" xml:lang="de">Ereignis</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">évènement</gloss>
  <desc versionDate="2023-09-05" xml:lang="en">contains data relating to anything of significance that happens in time.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">任何未必是口說的或溝通上的現象或發生情況，例如偶然的噪音或其他影響溝通的事件。</desc>
  <desc versionDate="2023-09-05" xml:lang="de">enthält Daten mit Bezug zu etwas Bemerkenswertem, das in der Zeit geschieht.</desc>
  <desc versionDate="2023-09-04" xml:lang="es">contiene datos relacionados con cualquier tipo de evento significativo asociado con una persona, lugar u organización.</desc>
  <desc versionDate="2023-05-07" xml:lang="fr">contient des données liées à tout type d'évènement significatif dans l'existence d'une personne, d'un lieu, d'un objet ou d'une organisation.</desc>
  <desc versionDate="2023-09-04" xml:lang="it">contiene dati a proposito di un qualsiasi tipo di evento significativo associato con una persona, luogo o organizzazione.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人生における特定の重要事象の解説を示す。</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인, 장소, 또는 조직과 관련된 중요한 사건에 해당하는 데이터를 포함한다.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.locatable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.eventLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="idno" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
        <elementRef key="eventName" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="linkGrp"/>
        <elementRef key="link"/>
        <elementRef key="idno"/>
      </alternate>
      <classRef key="model.eventLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.personLike" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listPerson" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.placeLike" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listPlace" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <classRef key="model.objectLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-kl">
      <listEvent>
        <event when="1618-05-23" xml:id="SecondDefPrague" where="#Prague">
          <eventName>1618 Defenestration of Prague</eventName>
          <idno>https://www.wikidata.org/wiki/Q13365740</idno>
          <listPerson type="defenstrated">
            <person>
              <persName>Jaroslav Bořita z Martinic</persName>
              <idno type="GND">https://d-nb.info/gnd/116810998</idno>
            </person>
            <person>
              <persName>Vilém Slavata z Chlumu a Košumberka</persName>
              <idno type="GND">https://d-nb.info/gnd/1018376615</idno>
            </person>
            <person>
              <persName>Filip Fabricius</persName>
              <idno type="GND">https://d-nb.info/gnd/133946118</idno>
            </person>
          </listPerson>
          <place xml:id="Prague"><placeName>Prague</placeName></place>
        </event>
        <event from="1618" to="1648" xml:id="ThirtyYearsWar">
          <eventName>Thirty Years’ War</eventName>
          <idno>https://www.wikidata.org/wiki/Q2487</idno>
          <event when="1643-03-19" xml:id="BattleofRocroi" where="#Rocroi">
            <eventName>Battle of Rocroi</eventName>
            <idno type="Wikidata">https://www.wikidata.org/wiki/Q728480</idno>
            <idno type="GND">https://d-nb.info/gnd/4202901-6</idno>
            <place xml:id="Rocroi">
              <placeName>Rocroi</placeName>
              <location><geo decls="#WGS">49.926111 4.522222</geo></location>
            </place>
          </event>
        </event>
      </listEvent>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-hz">
      <person>
        <event type="mat" when="1972-10-12">
          <label>matriculation</label>
        </event>
        <event type="grad" when="1975-06-23">
          <label>graduation</label>
        </event>
      </person>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-aq">
      <person>
        <event type="mat" when="1972-10-12">
          <label>inscription</label>
        </event>
        <event type="grad" when="1975-06-23">
          <label>diplômé</label>
        </event>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-lo">
      <person>
        <event type="mat" when="1972-10-12">
          <label>入學</label>
        </event>
        <event type="grad" when="1975-06-23">
          <label>畢業</label>
        </event>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="de-AT">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-kv">
      <listEvent type="generated">
        <event xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001" ref="https://mrp.oeaw.ac.at/pages/show.html?directory=editions&amp;document=MRP-1-1-01-0-18480401-P-0001.xml" type="session">
          <head>Nr. 1 Ministerrat, Wien, 1. April 1848</head>
          <label>Ministerratssitzung <date when="1848-04-01">1848-04-01</date>, aus Band 1 1/1, März 1848–21. November 1848</label>
          <listEvent type="agenda_items">
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_1">
              <label>I. Enthebung Baron Karl Friedrich v. Kübecks als Finanzminister und Ernennung des Freiherrn Philipp v. Krauß zu seinem Nachfolger</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_2">
              <label>II. Ernennung FML. Peter Zaninis zum Kriegsminister</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_3">
              <label>III. Öffentliche Erklärung über die konstitutionellen Grundsätze; Umformung des Staatsrates</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_4">
              <label>IV. Kriegserklärung Sardiniens; Vorgehen Radetzkys; Bestellung eines Hofkommissärs für Lombardo-Venetien</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_5">
              <label>V. Beeidigung der Minister</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_6">
              <label>VI. Tumulte im Kärntnertortheater</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_7">
              <label>VII. Bewegung der tschechischen demokratischen Partei; Berufung Paul Josef Safaiřiks nach Wien</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_8">
              <label>VIII. Behandlung der aus Lombardo-Venetien vertriebenen Justiz- und politischen Beamten</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_9">
              <label>IX. Besetzung der Landeschef- und Ständepräsidentenposten in Prag; böhmische Deputation in Wien</label>
            </event>
          </listEvent>
          <listPerson type="attendants">
            <person role="chair"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8141"><surname>Kolowrat</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8145"><surname>Ficquelmont</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8154"><surname>Taaffe</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8148"><surname>Pillersdorf</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8151"><surname>Sommaruga</surname></persName></person>
            <person role="signed-protocol"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8141"><surname>Kolowrat</surname></persName><note>BdE. <date when="1848-04-02">2. 4.</date></note></person>
            <person role="signed-protocol"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/9251"><surname>Franz Karl</surname></persName><note>BdE. <date when="1848-04-02">2. 4.</date></note></person>
          </listPerson>
          <listPlace>
            <place xml:id="Wien">
              <placeName xml:lang="de">Wien</placeName>
              <placeName xml:lang="en">Vienna</placeName>
              <location>
                <geo>48.208199 16.37169</geo>
              </location>
              <idno type="GeoNames">https://sws.geonames.org/2761369</idno>
            </place>
          </listPlace>
        </event>
        <!-- ... -->
      </listEvent>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPERSbp"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">event</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2023-05-07" xml:lang="de">Ereignis</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">évènement</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2023-09-05" xml:lang="en">contains data relating to anything of significance that happens in time.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">任何未必是口說的或溝通上的現象或發生情況，例如偶然的噪音或其他影響溝通的事件。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2023-09-05" xml:lang="de">enthält Daten mit Bezug zu etwas Bemerkenswertem, das in der Zeit geschieht.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-09-04" xml:lang="es">contiene datos relacionados con cualquier tipo de evento significativo asociado con una persona, lugar u organización.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-05-07" xml:lang="fr">contient des données liées à tout type d'évènement significatif dans l'existence d'une personne, d'un lieu, d'un objet ou d'une organisation.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2023-09-04" xml:lang="it">contiene dati a proposito di un qualsiasi tipo di evento significativo associato con una persona, luogo o organizzazione.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人生における特定の重要事象の解説を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인, 장소, 또는 조직과 관련된 중요한 사건에 해당하는 데이터를 포함한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.locatable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.eventLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="idno" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
        <elementRef key="eventName" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="linkGrp"/>
        <elementRef key="link"/>
        <elementRef key="idno"/>
      </alternate>
      <classRef key="model.eventLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.personLike" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listPerson" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.placeLike" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listPlace" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <classRef key="model.objectLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
    </sequence>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-kl">
      <listEvent>
        <event when="1618-05-23" xml:id="SecondDefPrague" where="#Prague">
          <eventName>1618 Defenestration of Prague</eventName>
          <idno>https://www.wikidata.org/wiki/Q13365740</idno>
          <listPerson type="defenstrated">
            <person>
              <persName>Jaroslav Bořita z Martinic</persName>
              <idno type="GND">https://d-nb.info/gnd/116810998</idno>
            </person>
            <person>
              <persName>Vilém Slavata z Chlumu a Košumberka</persName>
              <idno type="GND">https://d-nb.info/gnd/1018376615</idno>
            </person>
            <person>
              <persName>Filip Fabricius</persName>
              <idno type="GND">https://d-nb.info/gnd/133946118</idno>
            </person>
          </listPerson>
          <place xml:id="Prague"><placeName>Prague</placeName></place>
        </event>
        <event from="1618" to="1648" xml:id="ThirtyYearsWar">
          <eventName>Thirty Years’ War</eventName>
          <idno>https://www.wikidata.org/wiki/Q2487</idno>
          <event when="1643-03-19" xml:id="BattleofRocroi" where="#Rocroi">
            <eventName>Battle of Rocroi</eventName>
            <idno type="Wikidata">https://www.wikidata.org/wiki/Q728480</idno>
            <idno type="GND">https://d-nb.info/gnd/4202901-6</idno>
            <place xml:id="Rocroi">
              <placeName>Rocroi</placeName>
              <location><geo decls="#WGS">49.926111 4.522222</geo></location>
            </place>
          </event>
        </event>
      </listEvent>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-hz">
      <person>
        <event type="mat" when="1972-10-12">
          <label>matriculation</label>
        </event>
        <event type="grad" when="1975-06-23">
          <label>graduation</label>
        </event>
      </person>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-aq">
      <person>
        <event type="mat" when="1972-10-12">
          <label>inscription</label>
        </event>
        <event type="grad" when="1975-06-23">
          <label>diplômé</label>
        </event>
      </person>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-lo">
      <person>
        <event type="mat" when="1972-10-12">
          <label>入學</label>
        </event>
        <event type="grad" when="1975-06-23">
          <label>畢業</label>
        </event>
      </person>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="de-AT">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-event-egXML-kv">
      <listEvent type="generated">
        <event xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001" ref="https://mrp.oeaw.ac.at/pages/show.html?directory=editions&amp;document=MRP-1-1-01-0-18480401-P-0001.xml" type="session">
          <head>Nr. 1 Ministerrat, Wien, 1. April 1848</head>
          <label>Ministerratssitzung <date when="1848-04-01">1848-04-01</date>, aus Band 1 1/1, März 1848–21. November 1848</label>
          <listEvent type="agenda_items">
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_1">
              <label>I. Enthebung Baron Karl Friedrich v. Kübecks als Finanzminister und Ernennung des Freiherrn Philipp v. Krauß zu seinem Nachfolger</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_2">
              <label>II. Ernennung FML. Peter Zaninis zum Kriegsminister</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_3">
              <label>III. Öffentliche Erklärung über die konstitutionellen Grundsätze; Umformung des Staatsrates</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_4">
              <label>IV. Kriegserklärung Sardiniens; Vorgehen Radetzkys; Bestellung eines Hofkommissärs für Lombardo-Venetien</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_5">
              <label>V. Beeidigung der Minister</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_6">
              <label>VI. Tumulte im Kärntnertortheater</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_7">
              <label>VII. Bewegung der tschechischen demokratischen Partei; Berufung Paul Josef Safaiřiks nach Wien</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_8">
              <label>VIII. Behandlung der aus Lombardo-Venetien vertriebenen Justiz- und politischen Beamten</label>
            </event>
            <event type="agenda_item" xml:id="mrp-events-MRP-1-1-01-0-18480401-P-0001-top_1_1_1_9">
              <label>IX. Besetzung der Landeschef- und Ständepräsidentenposten in Prag; böhmische Deputation in Wien</label>
            </event>
          </listEvent>
          <listPerson type="attendants">
            <person role="chair"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8141"><surname>Kolowrat</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8145"><surname>Ficquelmont</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8154"><surname>Taaffe</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8148"><surname>Pillersdorf</surname></persName></person>
            <person role="attendant"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8151"><surname>Sommaruga</surname></persName></person>
            <person role="signed-protocol"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/8141"><surname>Kolowrat</surname></persName><note>BdE. <date when="1848-04-02">2. 4.</date></note></person>
            <person role="signed-protocol"><persName ref="https://mpr.acdh.oeaw.ac.at/entity/9251"><surname>Franz Karl</surname></persName><note>BdE. <date when="1848-04-02">2. 4.</date></note></person>
          </listPerson>
          <listPlace>
            <place xml:id="Wien">
              <placeName xml:lang="de">Wien</placeName>
              <placeName xml:lang="en">Vienna</placeName>
              <location>
                <geo>48.208199 16.37169</geo>
              </location>
              <idno type="GeoNames">https://sws.geonames.org/2761369</idno>
            </place>
          </listPlace>
        </event>
        <!-- ... -->
      </listEvent>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSbp"/>
  </listRef>
```

^b19

