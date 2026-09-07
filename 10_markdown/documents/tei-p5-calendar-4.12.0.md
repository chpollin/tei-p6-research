---
type: representation
source-type: document
source: '[[00_sources/tei-p5-calendar-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 calendar
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/calendar.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# calendar

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2798. Git blob: `12afabaf5fc6f5d87fb0709aaea73be05a20f78f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-calendar" ident="calendar">
  <gloss versionDate="2007-01-21" xml:lang="en">calendar</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">calendrier</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">calendario</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">calendario</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">暦</gloss>
  <desc versionDate="2011-04-13" xml:lang="en">describes a calendar or dating system used in a dating formula in the text.</desc>
  <desc versionDate="2022-02-23" xml:lang="es">describe un calendario o sistema de datación usado en una fórmula de datación en el texto.</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">テキスト中での日付の書式で用いられる暦日法を記述する。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>    
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-kl">
      <calendarDesc>
        <calendar xml:id="julianEngland">
          <p>Julian Calendar (including proleptic)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-hp">
      <calendarDesc>
        <calendar xml:id="egyptian" target="http://en.wikipedia.org/wiki/Egyptian_calendar">
          <p>Egyptian calendar (as defined by Wikipedia)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="es">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-zi">
      <calendarDesc>
        <calendar xml:id="juliano">
          <p>Calendario juliano (incluido el proléptico)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="es">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-rg">
      <calendarDesc>
        <calendar xml:id="egipcio" target="http://en.wikipedia.org/wiki/Egyptian_calendar">
          <p>Calendario egipcio (tal como lo define Wikipedia)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD44"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="en">calendar</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">calendrier</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">calendario</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">calendario</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">暦</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-04-13" xml:lang="en">describes a calendar or dating system used in a dating formula in the text.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2022-02-23" xml:lang="es">describe un calendario o sistema de datación usado en una fórmula de datación en el texto.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">テキスト中での日付の書式で用いられる暦日法を記述する。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>    
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-kl">
      <calendarDesc>
        <calendar xml:id="julianEngland">
          <p>Julian Calendar (including proleptic)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-hp">
      <calendarDesc>
        <calendar xml:id="egyptian" target="http://en.wikipedia.org/wiki/Egyptian_calendar">
          <p>Egyptian calendar (as defined by Wikipedia)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="es">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-zi">
      <calendarDesc>
        <calendar xml:id="juliano">
          <p>Calendario juliano (incluido el proléptico)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="es">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendar-egXML-rg">
      <calendarDesc>
        <calendar xml:id="egipcio" target="http://en.wikipedia.org/wiki/Egyptian_calendar">
          <p>Calendario egipcio (tal como lo define Wikipedia)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD44"/>
  </listRef>
```

^b15

