---
type: representation
source-type: document
source: '[[00_sources/tei-p5-calendardesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 calendarDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/calendarDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# calendarDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6657. Git blob: `d294ab536e209aa5e639615174c09076490c9696`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-calendarDesc" ident="calendarDesc">
  <gloss versionDate="2011-08-12" xml:lang="en">calendar description</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción de las calendarios</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description des calendriers</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione delle calendari</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">暦の記述</gloss>
  <desc versionDate="2011-08-12" xml:lang="en">contains a description of the calendar system used in any
  dating expression found in the text.</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description des différents calendriers
    utilisés dans des dates écrits dans un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de todos los diferentes
    calendarios usados en un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dei diversi calendari usati in
    un manoscritto</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">テキスト中に見いだされた日付表現において用いられる暦日法の記述。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    
      <elementRef key="calendar" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendarDesc-egXML-fv">
      <calendarDesc>
        <calendar xml:id="cal_AD">
          <p>Anno Domini (Christian Era)</p>
        </calendar>
        <calendar xml:id="cal_AH">
          <p>Anno Hegirae (Muhammedan Era)</p>
        </calendar>
        <calendar xml:id="cal_AME">
          <p>Mauludi Era (solar years since Mohammed's birth)</p>
        </calendar>
        <calendar xml:id="cal_AM">
          <p>Anno Mundi (Jewish Calendar)</p>
        </calendar>
        <calendar xml:id="cal_AP">
          <p>Anno Persici</p>
        </calendar>
        <calendar xml:id="cal_AS">
          <p>Aji Saka Era (Java)</p>
        </calendar>
        <calendar xml:id="cal_BE">
          <p>Buddhist Era</p>
        </calendar>
        <calendar xml:id="cal_CB">
          <p>Cooch Behar Era</p>
        </calendar>
        <calendar xml:id="cal_CE">
          <p>Common Era</p>
        </calendar>
        <calendar xml:id="cal_CL">
          <p>Chinese Lunar Era</p>
        </calendar>
        <calendar xml:id="cal_CS">
          <p>Chula Sakarat Era</p>
        </calendar>
        <calendar xml:id="cal_EE">
          <p>Ethiopian Era</p>
        </calendar>
        <calendar xml:id="cal_FE">
          <p>Fasli Era</p>
        </calendar>
        <calendar xml:id="cal_ISO">
          <p>ISO 8601 calendar</p>
        </calendar>
        <calendar xml:id="cal_JE">
          <p>Japanese Calendar</p>
        </calendar>
        <calendar xml:id="cal_KE">
          <p>Khalsa Era (Sikh calendar)</p>
        </calendar>
        <calendar xml:id="cal_KY">
          <p>Kali Yuga</p>
        </calendar>
        <calendar xml:id="cal_ME">
          <p>Malabar Era</p>
        </calendar>
        <calendar xml:id="cal_MS">
          <p>Monarchic Solar Era</p>
        </calendar>
        <calendar xml:id="cal_NS">
          <p>Nepal Samwat Era</p>
        </calendar>
        <calendar xml:id="cal_OS">
          <p>Old Style (Julian Calendar)</p>
        </calendar>
        <calendar xml:id="cal_RS">
          <p>Rattanakosin (Bangkok) Era</p>
        </calendar>
        <calendar xml:id="cal_SE">
          <p>Saka Era</p>
        </calendar>
        <calendar xml:id="cal_SH">
          <p>Mohammedan Solar Era (Iran)</p>
        </calendar>
        <calendar xml:id="cal_SS">
          <p>Saka Samvat</p>
        </calendar>
        <calendar xml:id="cal_TE">
          <p>Tripurabda Era</p>
        </calendar>
        <calendar xml:id="cal_VE">
          <p>Vikrama Era</p>
        </calendar>
        <calendar xml:id="cal_VS">
          <p>Vikrama Samvat Era</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendarDesc-egXML-xh">
      <calendarDesc>
        <calendar xml:id="cal_Gregorian">
          <p>Gregorian calendar</p>
        </calendar>
        <calendar xml:id="cal_Julian">
          <p>Julian calendar</p>
        </calendar>
        <calendar xml:id="cal_Islamic">
          <p>Islamic or Muslim (hijri) lunar calendar</p>
        </calendar>
        <calendar xml:id="cal_Hebrew">
          <p>Hebrew or Jewish lunisolar calendar</p>
        </calendar>
        <calendar xml:id="cal_Revolutionary">
          <p>French Revolutionary calendar</p>
        </calendar>
        <calendar xml:id="cal_Iranian">
          <p>Iranian or Persian (Jalaali) solar calendar</p>
        </calendar>
        <calendar xml:id="cal_Coptic">
          <p>Coptic or Alexandrian calendar</p>
        </calendar>
        <calendar xml:id="cal_Chinese">
          <p>Chinese lunisolar calendar</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendarDesc-egXML-vg">
      <calendarDesc>
        <calendar xml:id="cal_Egyptian" target="http://en.wikipedia.org/wiki/Egyptian_calendar">
          <p>Egyptian calendar (as defined by Wikipedia)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
  <remarks ident="calendarDesc-remarks" versionDate="2011-08-12" xml:lang="en">
    <p>In the first example above, calendars and short codes for 
      <att>xml:id</att>s are  from W3 guidelines at 
      <ref>http://www.w3.org/TR/xpath-functions-11/#lang-cal-country</ref>
      </p>
  </remarks>
  <remarks ident="calendarDesc-remarks" versionDate="2023-10-02" xml:lang="ja"><p>ひとつめの例での、暦の名と<att>xml:id</att>の略号は、
    <ref>http://www.w3.org/TR/xpath-functions-11/#lang-cal-country</ref>におけるW3Cガイドラインから来ている。</p></remarks>
  
  <listRef>
    <ptr target="#HD4"/>
    <ptr target="#HD44"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2011-08-12" xml:lang="en">calendar description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">descripción de las calendarios</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description des calendriers</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione delle calendari</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">暦の記述</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-08-12" xml:lang="en">contains a description of the calendar system used in any
  dating expression found in the text.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description des différents calendriers
    utilisés dans des dates écrits dans un manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de todos los diferentes
    calendarios usados en un manuscrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dei diversi calendari usati in
    un manoscritto</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">テキスト中に見いだされた日付表現において用いられる暦日法の記述。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <elementRef key="calendar" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendarDesc-egXML-fv">
      <calendarDesc>
        <calendar xml:id="cal_AD">
          <p>Anno Domini (Christian Era)</p>
        </calendar>
        <calendar xml:id="cal_AH">
          <p>Anno Hegirae (Muhammedan Era)</p>
        </calendar>
        <calendar xml:id="cal_AME">
          <p>Mauludi Era (solar years since Mohammed's birth)</p>
        </calendar>
        <calendar xml:id="cal_AM">
          <p>Anno Mundi (Jewish Calendar)</p>
        </calendar>
        <calendar xml:id="cal_AP">
          <p>Anno Persici</p>
        </calendar>
        <calendar xml:id="cal_AS">
          <p>Aji Saka Era (Java)</p>
        </calendar>
        <calendar xml:id="cal_BE">
          <p>Buddhist Era</p>
        </calendar>
        <calendar xml:id="cal_CB">
          <p>Cooch Behar Era</p>
        </calendar>
        <calendar xml:id="cal_CE">
          <p>Common Era</p>
        </calendar>
        <calendar xml:id="cal_CL">
          <p>Chinese Lunar Era</p>
        </calendar>
        <calendar xml:id="cal_CS">
          <p>Chula Sakarat Era</p>
        </calendar>
        <calendar xml:id="cal_EE">
          <p>Ethiopian Era</p>
        </calendar>
        <calendar xml:id="cal_FE">
          <p>Fasli Era</p>
        </calendar>
        <calendar xml:id="cal_ISO">
          <p>ISO 8601 calendar</p>
        </calendar>
        <calendar xml:id="cal_JE">
          <p>Japanese Calendar</p>
        </calendar>
        <calendar xml:id="cal_KE">
          <p>Khalsa Era (Sikh calendar)</p>
        </calendar>
        <calendar xml:id="cal_KY">
          <p>Kali Yuga</p>
        </calendar>
        <calendar xml:id="cal_ME">
          <p>Malabar Era</p>
        </calendar>
        <calendar xml:id="cal_MS">
          <p>Monarchic Solar Era</p>
        </calendar>
        <calendar xml:id="cal_NS">
          <p>Nepal Samwat Era</p>
        </calendar>
        <calendar xml:id="cal_OS">
          <p>Old Style (Julian Calendar)</p>
        </calendar>
        <calendar xml:id="cal_RS">
          <p>Rattanakosin (Bangkok) Era</p>
        </calendar>
        <calendar xml:id="cal_SE">
          <p>Saka Era</p>
        </calendar>
        <calendar xml:id="cal_SH">
          <p>Mohammedan Solar Era (Iran)</p>
        </calendar>
        <calendar xml:id="cal_SS">
          <p>Saka Samvat</p>
        </calendar>
        <calendar xml:id="cal_TE">
          <p>Tripurabda Era</p>
        </calendar>
        <calendar xml:id="cal_VE">
          <p>Vikrama Era</p>
        </calendar>
        <calendar xml:id="cal_VS">
          <p>Vikrama Samvat Era</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendarDesc-egXML-xh">
      <calendarDesc>
        <calendar xml:id="cal_Gregorian">
          <p>Gregorian calendar</p>
        </calendar>
        <calendar xml:id="cal_Julian">
          <p>Julian calendar</p>
        </calendar>
        <calendar xml:id="cal_Islamic">
          <p>Islamic or Muslim (hijri) lunar calendar</p>
        </calendar>
        <calendar xml:id="cal_Hebrew">
          <p>Hebrew or Jewish lunisolar calendar</p>
        </calendar>
        <calendar xml:id="cal_Revolutionary">
          <p>French Revolutionary calendar</p>
        </calendar>
        <calendar xml:id="cal_Iranian">
          <p>Iranian or Persian (Jalaali) solar calendar</p>
        </calendar>
        <calendar xml:id="cal_Coptic">
          <p>Coptic or Alexandrian calendar</p>
        </calendar>
        <calendar xml:id="cal_Chinese">
          <p>Chinese lunisolar calendar</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-calendarDesc-egXML-vg">
      <calendarDesc>
        <calendar xml:id="cal_Egyptian" target="http://en.wikipedia.org/wiki/Egyptian_calendar">
          <p>Egyptian calendar (as defined by Wikipedia)</p>
        </calendar>
      </calendarDesc>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="calendarDesc-remarks" versionDate="2011-08-12" xml:lang="en">
    <p>In the first example above, calendars and short codes for 
      <att>xml:id</att>s are  from W3 guidelines at 
      <ref>http://www.w3.org/TR/xpath-functions-11/#lang-cal-country</ref>
      </p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="calendarDesc-remarks" versionDate="2023-10-02" xml:lang="ja"><p>ひとつめの例での、暦の名と<att>xml:id</att>の略号は、
    <ref>http://www.w3.org/TR/xpath-functions-11/#lang-cal-country</ref>におけるW3Cガイドラインから来ている。</p></remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD4"/>
    <ptr target="#HD44"/>
  </listRef>
```

^b18

