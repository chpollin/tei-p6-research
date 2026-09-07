---
type: representation
source-type: document
source: '[[00_sources/tei-p5-eventname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 eventName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/eventName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# eventName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6192. Git blob: `47c6fd207b4e86720604a3a1a8fbc26371160c73`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-eventName" ident="eventName">
  <gloss versionDate="2023-05-02" xml:lang="en">name of an event</gloss>
  <gloss versionDate="2023-05-02" xml:lang="de">Name eines Ereignisses</gloss>
  <desc versionDate="2023-05-02" xml:lang="en">contains a proper noun or noun phrase used to refer to an event.</desc>
  <desc versionDate="2023-05-02" xml:lang="de">enthält einen Eigennamen in Form eines Nomens oder einer Nominalphrase, der verwendet wird, um auf ein Ereignis zu verweisen.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.nameLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-uz">
      <listEvent>
        <event from="1939-09-01" to="1945-09-02">
          <eventName xml:lang="de">Zweiter Weltkrieg</eventName>
          <eventName xml:lang="en">World War II</eventName>
          <idno type="GND">https://d-nb.info/gnd/4079167-1</idno>
          <idno type="Wikidata">https://www.wikidata.org/wiki/Q362</idno>
          <event from="1939-09-01" to="1939-10-06" xml:id="UeberfallAufPolen">
            <eventName xml:lang="de">Überfall auf Polen</eventName>
            <eventName xml:lang="en">Invasion of Poland</eventName>
            <idno type="GND">https://d-nb.info/gnd/4175002-0</idno>
            <idno type="LOC">https://id.loc.gov/authorities/sh85148341</idno>
            <listPlace type="affected">
              <place>
                <placeName xml:lang="pl">Gdańsk</placeName>
                <location><geo>54.350556 18.652778</geo></location>
              </place>
            </listPlace>
          </event>
          <event from="1941-06-22" to="1945-05-09">
            <eventName xml:lang="de">Deutsch-Sowjetischer Krieg</eventName>
            <eventName xml:lang="ru">Великая Отечественная война</eventName>
            <idno type="GND">https://d-nb.info/gnd/4076906-9</idno>
            <idno type="Wikidata">https://www.wikidata.org/wiki/Q189266</idno>
          </event>
        </event>
      </listEvent>
    </egXML>
  </exemplum>
  <exemplum xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-ss">
      <p>Mit dem <eventName ref="#UeberfallAufPolen">Überfall auf Polen</eventName>
        begann der <eventName>Zweite Weltkrieg</eventName>, der in manchen Nachfolgestaaten
        der <placeName>Sowjetunion</placeName> auch als <eventName>Großer Vaterländischer Krieg</eventName>
        (<eventName xml:lang="ru">Великая Отечественная война</eventName>) bekannt ist.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-sp">
      <p>On <date when="1719-03-19">Monday</date>, <rs type="person">she</rs> was writing about the
        <eventName ref="#SecondDefPrague">1618 Defenestration of Prague</eventName> which initiated the
        <rs type="event" ref="#ThirtyYearsWar">long war</rs>.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-gv">
      <event from="2019-09-16" to="2019-09-20" xml:id="tei2019graz">
        <eventName type="full">TEI 2019: What is text, really? TEI and beyond</eventName>
        <eventName type="short">TEI 2019</eventName>
        <note>
          The abstract leading to the <gi>eventName</gi> element is available at <ref target="https://gams.uni-graz.at/o:tei2019.141">https://gams.uni-graz.at/o:tei2019.141</ref>.
          Other related documents are available through <ref target="https://gams.uni-graz.at/tei2019">https://gams.uni-graz.at/tei2019</ref>, as well as in the
          <ref target="https://zenodo.org/communities/tei2019">TEI 2019 Zenodo community</ref>.
        </note>
        <listPerson type="LocalOrganizers">
          <person>
            <persName>
              <surname>Raunig</surname>
              <forename>Elisabeth</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Scholger</surname>
              <forename>Martina</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Scholger</surname>
              <forename>Walter</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Steiner</surname>
              <forename>Elisabeth</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Vogeler</surname>
              <forename>Georg</forename>
            </persName>
          </person>
        </listPerson>
        <place xml:lang="de">
          <placeName>Universität Graz</placeName>
          <location>
            <address>
              <addrLine>ReSoWi Gebäude</addrLine>
              <addrLine>Universitätsstraße 15</addrLine>
              <postCode>8010</postCode>
              <settlement>Graz</settlement>
              <country>Österreich</country>
            </address>
            <geo>15.451651587656 47.078215112534</geo>
          </location>
        </place>
        <listRelation>
          <relation active="#tei2019graz" passive="#AnnualTEIConference" type="CRM" name="P31_is_instance_of" ref="https://www.wikidata.org/wiki/Property:P31"/>
        </listRelation>
      </event>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDEVTN"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2023-05-02" xml:lang="en">name of an event</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2023-05-02" xml:lang="de">Name eines Ereignisses</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2023-05-02" xml:lang="en">contains a proper noun or noun phrase used to refer to an event.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-05-02" xml:lang="de">enthält einen Eigennamen in Form eines Nomens oder einer Nominalphrase, der verwendet wird, um auf ein Ereignis zu verweisen.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.nameLike"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-uz">
      <listEvent>
        <event from="1939-09-01" to="1945-09-02">
          <eventName xml:lang="de">Zweiter Weltkrieg</eventName>
          <eventName xml:lang="en">World War II</eventName>
          <idno type="GND">https://d-nb.info/gnd/4079167-1</idno>
          <idno type="Wikidata">https://www.wikidata.org/wiki/Q362</idno>
          <event from="1939-09-01" to="1939-10-06" xml:id="UeberfallAufPolen">
            <eventName xml:lang="de">Überfall auf Polen</eventName>
            <eventName xml:lang="en">Invasion of Poland</eventName>
            <idno type="GND">https://d-nb.info/gnd/4175002-0</idno>
            <idno type="LOC">https://id.loc.gov/authorities/sh85148341</idno>
            <listPlace type="affected">
              <place>
                <placeName xml:lang="pl">Gdańsk</placeName>
                <location><geo>54.350556 18.652778</geo></location>
              </place>
            </listPlace>
          </event>
          <event from="1941-06-22" to="1945-05-09">
            <eventName xml:lang="de">Deutsch-Sowjetischer Krieg</eventName>
            <eventName xml:lang="ru">Великая Отечественная война</eventName>
            <idno type="GND">https://d-nb.info/gnd/4076906-9</idno>
            <idno type="Wikidata">https://www.wikidata.org/wiki/Q189266</idno>
          </event>
        </event>
      </listEvent>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-ss">
      <p>Mit dem <eventName ref="#UeberfallAufPolen">Überfall auf Polen</eventName>
        begann der <eventName>Zweite Weltkrieg</eventName>, der in manchen Nachfolgestaaten
        der <placeName>Sowjetunion</placeName> auch als <eventName>Großer Vaterländischer Krieg</eventName>
        (<eventName xml:lang="ru">Великая Отечественная война</eventName>) bekannt ist.</p>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-sp">
      <p>On <date when="1719-03-19">Monday</date>, <rs type="person">she</rs> was writing about the
        <eventName ref="#SecondDefPrague">1618 Defenestration of Prague</eventName> which initiated the
        <rs type="event" ref="#ThirtyYearsWar">long war</rs>.</p>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eventName-egXML-gv">
      <event from="2019-09-16" to="2019-09-20" xml:id="tei2019graz">
        <eventName type="full">TEI 2019: What is text, really? TEI and beyond</eventName>
        <eventName type="short">TEI 2019</eventName>
        <note>
          The abstract leading to the <gi>eventName</gi> element is available at <ref target="https://gams.uni-graz.at/o:tei2019.141">https://gams.uni-graz.at/o:tei2019.141</ref>.
          Other related documents are available through <ref target="https://gams.uni-graz.at/tei2019">https://gams.uni-graz.at/tei2019</ref>, as well as in the
          <ref target="https://zenodo.org/communities/tei2019">TEI 2019 Zenodo community</ref>.
        </note>
        <listPerson type="LocalOrganizers">
          <person>
            <persName>
              <surname>Raunig</surname>
              <forename>Elisabeth</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Scholger</surname>
              <forename>Martina</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Scholger</surname>
              <forename>Walter</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Steiner</surname>
              <forename>Elisabeth</forename>
            </persName>
          </person>
          <person>
            <persName>
              <surname>Vogeler</surname>
              <forename>Georg</forename>
            </persName>
          </person>
        </listPerson>
        <place xml:lang="de">
          <placeName>Universität Graz</placeName>
          <location>
            <address>
              <addrLine>ReSoWi Gebäude</addrLine>
              <addrLine>Universitätsstraße 15</addrLine>
              <postCode>8010</postCode>
              <settlement>Graz</settlement>
              <country>Österreich</country>
            </address>
            <geo>15.451651587656 47.078215112534</geo>
          </location>
        </place>
        <listRelation>
          <relation active="#tei2019graz" passive="#AnnualTEIConference" type="CRM" name="P31_is_instance_of" ref="https://www.wikidata.org/wiki/Property:P31"/>
        </listRelation>
      </event>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDEVTN"/>
  </listRef>
```

^b11

