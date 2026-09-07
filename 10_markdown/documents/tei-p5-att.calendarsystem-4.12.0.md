---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.calendarsystem-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.calendarSystem
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.calendarSystem.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.calendarSystem

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5185. Git blob: `4de7cf2bfd07ada679110625e85dd4ba2e09df94`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tei" type="atts" xml:id="CALENDARSYSTEM" ident="att.calendarSystem">
  <desc versionDate="2023-05-09" xml:lang="en">provides attributes for indicating calendar systems to which a date belongs.</desc>
  <desc versionDate="2023-05-09" xml:lang="it">assegna attributi per indicare i sistemi o calendari ai quali appartiene una data.</desc>
  <attList>
    <attDef ident="calendar" usage="opt">
      <desc versionDate="2021-04-26" xml:lang="en">indicates one or more systems or calendars to which the date represented by the content of this element belongs.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">날짜 표현 시스템 또는 달력 표시 형식을 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明該日期表示所使用的曆法計算系統。</desc>
      <desc versionDate="2019-02-03" xml:lang="ja">この要素を含むコンテントにおける日付の暦やシステムを示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">indique le système ou le calendrier auquel appartient la date exprimée dans le contenu de l'élément.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el sistema o calendario en que se muestra una fecha.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il sistema o calendario al quale la data appartiene.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
      <constraintSpec ident="calendar_attr_on_empty_element" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@calendar]">
            <sch:assert test="string-length( normalize-space(.) ) gt 0"> @calendar indicates one or more
              systems or calendars to which the date represented by the content of this element belongs,
              but this &lt;<sch:name/>> element has no textual content.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-rf">He was born on <date calendar="#gregorian">Feb. 22, 1732</date> (<date calendar="#julian" when="1732-02-22">Feb. 11, 1731/32,
          O.S.</date>).
        </egXML> 
      </exemplum>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-xw">
          He was born on <date calendar="#gregorian #julian" when="1732-02-22">Feb. 22, 1732 
            (Feb. 11, 1731/32, O.S.)</date>.
        </egXML>
      </exemplum>
      <exemplum xml:lang="de">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-na">
          <date calendar="#julian #gregorian" when="1829-05-19">Dienstag 7/19
            Mai</date>.
        </egXML>
      </exemplum>
      <exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-fy" source="#fr-ex-Bouiller_Rapport"> L'année
          1960 fut, en vertu du calendrier grégorien, bissextile ; le 22 juin tomba ainsi le jour de
          l'été, le <date calendar="#gregorian">22 juin</date>. </egXML>
      </exemplum>
      <remarks ident="att.calendarSystem-attr.calendar-remarks" versionDate="2023-09-03" xml:lang="en">
        <p>Note that the <att>calendar</att> attribute declares the calendar
        system used to interpret the textual content of an element,
        as it appears on an original source. It does
        <emph>not</emph> modify the interpretation of the normalization
        attributes provided by <ident type="class">att.datable.w3c</ident>,
        <ident type="class">att.datable.iso</ident>, or <ident type="class">att.datable.custom</ident>. Attributes from those first two
        classes are always interpreted as Gregorian or proleptic Gregorian
        dates, as per the respective standards on which they are based. The
        calender system used to interpret the last (<ident type="class">att.datable.custom</ident>) may be specified with
        <att>datingMethod</att>.</p>
      </remarks>
      <remarks ident="att.calendarSystem-attr.calendar-remarks" versionDate="2019-02-03" xml:lang="ja"><p>
        <att>calendar</att>属性は(<ident type="class">att.datable.custom</ident>クラスで定義される<att>datingMethod</att>属性と異なり、
        親要素によって定義される原資料の日付の暦日システムを定義するものであり、
        どの暦日に日付を正規化するかではない。</p></remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#CONADA"/>
    <ptr target="#NDDATE"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2023-05-09" xml:lang="en">provides attributes for indicating calendar systems to which a date belongs.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-05-09" xml:lang="it">assegna attributi per indicare i sistemi o calendari ai quali appartiene una data.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2021-04-26" xml:lang="en">indicates one or more systems or calendars to which the date represented by the content of this element belongs.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">날짜 표현 시스템 또는 달력 표시 형식을 표시한다.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明該日期表示所使用的曆法計算系統。</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2019-02-03" xml:lang="ja">この要素を含むコンテントにおける日付の暦やシステムを示す。</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">indique le système ou le calendrier auquel appartient la date exprimée dans le contenu de l'élément.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el sistema o calendario en que se muestra una fecha.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il sistema o calendario al quale la data appartiene.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="calendar_attr_on_empty_element" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@calendar]">
            <sch:assert test="string-length( normalize-space(.) ) gt 0"> @calendar indicates one or more
              systems or calendars to which the date represented by the content of this element belongs,
              but this &lt;<sch:name/>> element has no textual content.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-rf">He was born on <date calendar="#gregorian">Feb. 22, 1732</date> (<date calendar="#julian" when="1732-02-22">Feb. 11, 1731/32,
          O.S.</date>).
        </egXML> 
      </exemplum>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-xw">
          He was born on <date calendar="#gregorian #julian" when="1732-02-22">Feb. 22, 1732 
            (Feb. 11, 1731/32, O.S.)</date>.
        </egXML>
      </exemplum>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[3]`.

```xml
<exemplum xml:lang="de">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-na">
          <date calendar="#julian #gregorian" when="1829-05-19">Dienstag 7/19
            Mai</date>.
        </egXML>
      </exemplum>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CALENDARSYSTEM-egXML-fy" source="#fr-ex-Bouiller_Rapport"> L'année
          1960 fut, en vertu du calendrier grégorien, bissextile ; le 22 juin tomba ainsi le jour de
          l'été, le <date calendar="#gregorian">22 juin</date>. </egXML>
      </exemplum>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.calendarSystem-attr.calendar-remarks" versionDate="2023-09-03" xml:lang="en">
        <p>Note that the <att>calendar</att> attribute declares the calendar
        system used to interpret the textual content of an element,
        as it appears on an original source. It does
        <emph>not</emph> modify the interpretation of the normalization
        attributes provided by <ident type="class">att.datable.w3c</ident>,
        <ident type="class">att.datable.iso</ident>, or <ident type="class">att.datable.custom</ident>. Attributes from those first two
        classes are always interpreted as Gregorian or proleptic Gregorian
        dates, as per the respective standards on which they are based. The
        calender system used to interpret the last (<ident type="class">att.datable.custom</ident>) may be specified with
        <att>datingMethod</att>.</p>
      </remarks>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.calendarSystem-attr.calendar-remarks" versionDate="2019-02-03" xml:lang="ja"><p>
        <att>calendar</att>属性は(<ident type="class">att.datable.custom</ident>クラスで定義される<att>datingMethod</att>属性と異なり、
        親要素によって定義される原資料の日付の暦日システムを定義するものであり、
        どの暦日に日付を正規化するかではない。</p></remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONADA"/>
    <ptr target="#NDDATE"/>
  </listRef>
```

^b18

