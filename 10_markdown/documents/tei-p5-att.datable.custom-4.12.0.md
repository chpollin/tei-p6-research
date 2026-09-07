---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.datable.custom-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.datable.custom
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.datable.custom.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.datable.custom

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8661. Git blob: `cf011a8e59249feeabcbcc78844fc9d31d2a08bf`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="DATABLECUSTOM" type="atts" predeclare="true" ident="att.datable.custom">
  <desc versionDate="2011-11-11" xml:lang="en">provides attributes for normalization of elements that contain datable events to a custom dating system
    (i.e. other than the Gregorian used by W3 and ISO).</desc>
  <desc versionDate="2019-02-03" xml:lang="ja">年代を特定できるイベントを含む要素を（たとえば、
    W3CやISOで用いられるグレゴリオ暦以外の）なんらかの暦システムで正規化する属性を提供する。</desc>
  <attList>
    <attDef ident="when-custom" usage="opt">
      <desc versionDate="2014-11-19" xml:lang="en">supplies the value of a date or time in some custom standard form.</desc>
      <desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な準形式で、日付や時刻の値を示す。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
      <exemplum xml:lang="en">
        <p>The following are examples of custom date or time formats that are <emph>not</emph> valid ISO or W3C format
                    normalizations, normalized to a different dating system</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-kr">
          <p>Alhazen died in Cairo on the 
            <date when="1040-03-06" when-custom="431-06-12">
              12th day of Jumada t-Tania, 430 AH
            </date>.</p>
          <p>The current world will end at the 
            <date when="2012-12-21" when-custom="13.0.0.0.0">end of B'ak'tun 13</date>.</p>
          <p>The Battle of Meggidu
            (<date when-custom="Thutmose_III:23">23rd year of reign of Thutmose III</date>).</p>
          <p>Esidorus bixit in pace annos LXX plus minus sub
            <date when-custom="Ind:4-10-11">die XI mensis Octobris indictione IIII</date>
               </p>
        </egXML>
        <p>Not all custom date formulations will have Gregorian equivalents.</p>
        <p>The <att>when-custom</att> attribute and other custom dating are not constrained to a datatype by the TEI, but
        individual projects are recommended to regularize and document their dating formats.</p>
      </exemplum>
    </attDef>
    <attDef ident="notBefore-custom" usage="opt">
      <desc versionDate="2011-11-11" xml:lang="en">specifies the earliest possible date for the event in some custom standard form.</desc>
      <desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で、あるイベントに関して「この時点より前ではない」という日付を示す。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="notAfter-custom" usage="opt">
      <desc versionDate="2011-11-11" xml:lang="en">specifies the latest possible date for the event in some custom standard form.</desc>
      <desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で、あるイベントに関して「この時点より後ではない」という日付を示す。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="from-custom" usage="opt">
      <desc versionDate="2014-11-19" xml:lang="en">indicates the starting point of the period in some custom standard form.</desc>
      <desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で期間の開始時点を示す。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-ey">
          <event xml:id="FIRE1" datingMethod="#julian" from-custom="1666-09-02" to-custom="1666-09-05">
            <head>The Great Fire of London</head>
            <p>The Great Fire of London burned through a large part 
          of the city of London.</p>
          </event>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="to-custom" usage="opt">
      <desc versionDate="2014-11-19" xml:lang="en">indicates the ending point of the period in some custom standard form.</desc>
      <desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で期間の終了時点を示す。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="datingPoint" usage="opt">
      <desc versionDate="2011-11-25" xml:lang="en">supplies a pointer to some location defining a named point in time with reference to which the datable item is understood to have occurred.</desc>
      <desc versionDate="2022-05-09" xml:lang="ja">ある時点につけた名前とその事柄が起きたとされる時間をともに定義している場所へのポインタを示す。たとえば、「令和改元」という日付をともなうID付きイベント要素を作成した場合にそのIDに対する参照を行う。</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="datingMethod" usage="opt">
      <desc versionDate="2012-08-15" xml:lang="en">supplies a pointer to a <gi>calendar</gi> element or other
        means of interpreting the values of the custom dating attributes.</desc>
      <desc versionDate="2022-05-09" xml:lang="ja">
          ここで提供するポインタは、<gi>calendar</gi> 要素もしくは日付を示す属性の値を解釈する何らかの方式を指す。</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-jw" source="#STOW">Contayning the Originall, Antiquity, Increaſe, Moderne 
            eſtate, and deſcription of that Citie, written in the yeare 
            <date when-custom="1598" calendar="#julian" datingMethod="#julian">1598</date>. by Iohn Stow 
            Citizen of London.</egXML>
        <p>In this example, the <att>calendar</att> attribute points to a <gi>calendar</gi> element for the 
          Julian calendar, specifying that the text content of the <gi>date</gi> element is a 
          Julian date, and the <att>datingMethod</att> attribute also points to the Julian calendar
          to indicate that the content of the <att>when-custom</att> attribute value is Julian too.</p>
      </exemplum>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-yd">
          <date when="1382-06-28" when-custom="6890-06-20" datingMethod="#creationOfWorld">
            μηνὶ Ἰουνίου εἰς <num>κ</num> ἔτους <num>ςωϞ</num>
          </date>
        </egXML>
        <p>In this example, a date is given in a Mediaeval text measured <q>from the creation of the world</q>, which is normalized
        (in <att>when</att>) to the Gregorian date, but is also normalized (in <att>when-custom</att>) to a
        machine-actionable, numeric version of the date from the Creation.</p>
      </exemplum>
      <remarks ident="att.datable.custom-attr.datingMethod-remarks" versionDate="2015-05-29" xml:lang="en"><p>Note that the <att>datingMethod</att> attribute (unlike
        <att>calendar</att> defined in <ident type="class">att.datable</ident>) defines
        the calendar or dating system to which the date described by the parent element is normalized (i.e. in the  
        <att>when-custom</att> or other <att>X-custom</att> attributes), <emph>not</emph> the calendar of the
        original date in the element.</p></remarks>
      <remarks ident="att.datable.custom-attr.datingMethod-remarks" versionDate="2019-02-13" xml:lang="ja"><p>（<ident type="class">att.datable</ident>で定義される<att>calendar</att> 属性とは違って）
        <att>datingMethod</att>属性が定義するのは、親要素で記述された日付を正規化した暦や暦法であり、
        当該要素中のオリジナルの日付の暦<emph>ではない</emph>。</p></remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#NDDATE"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-11" xml:lang="en">provides attributes for normalization of elements that contain datable events to a custom dating system
    (i.e. other than the Gregorian used by W3 and ISO).</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-02-03" xml:lang="ja">年代を特定できるイベントを含む要素を（たとえば、
    W3CやISOで用いられるグレゴリオ暦以外の）なんらかの暦システムで正規化する属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2014-11-19" xml:lang="en">supplies the value of a date or time in some custom standard form.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な準形式で、日付や時刻の値を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <p>The following are examples of custom date or time formats that are <emph>not</emph> valid ISO or W3C format
                    normalizations, normalized to a different dating system</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-kr">
          <p>Alhazen died in Cairo on the 
            <date when="1040-03-06" when-custom="431-06-12">
              12th day of Jumada t-Tania, 430 AH
            </date>.</p>
          <p>The current world will end at the 
            <date when="2012-12-21" when-custom="13.0.0.0.0">end of B'ak'tun 13</date>.</p>
          <p>The Battle of Meggidu
            (<date when-custom="Thutmose_III:23">23rd year of reign of Thutmose III</date>).</p>
          <p>Esidorus bixit in pace annos LXX plus minus sub
            <date when-custom="Ind:4-10-11">die XI mensis Octobris indictione IIII</date>
               </p>
        </egXML>
        <p>Not all custom date formulations will have Gregorian equivalents.</p>
        <p>The <att>when-custom</att> attribute and other custom dating are not constrained to a datatype by the TEI, but
        individual projects are recommended to regularize and document their dating formats.</p>
      </exemplum>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2011-11-11" xml:lang="en">specifies the earliest possible date for the event in some custom standard form.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で、あるイベントに関して「この時点より前ではない」という日付を示す。</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2011-11-11" xml:lang="en">specifies the latest possible date for the event in some custom standard form.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で、あるイベントに関して「この時点より後ではない」という日付を示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2014-11-19" xml:lang="en">indicates the starting point of the period in some custom standard form.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で期間の開始時点を示す。</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[4]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-ey">
          <event xml:id="FIRE1" datingMethod="#julian" from-custom="1666-09-02" to-custom="1666-09-05">
            <head>The Great Fire of London</head>
            <p>The Great Fire of London burned through a large part 
          of the city of London.</p>
          </event>
        </egXML>
      </exemplum>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2014-11-19" xml:lang="en">indicates the ending point of the period in some custom standard form.</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2019-02-03" xml:lang="ja">何らかの標準的な形式で期間の終了時点を示す。</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[1]`.

```xml
<desc versionDate="2011-11-25" xml:lang="en">supplies a pointer to some location defining a named point in time with reference to which the datable item is understood to have occurred.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[2]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">ある時点につけた名前とその事柄が起きたとされる時間をともに定義している場所へのポインタを示す。たとえば、「令和改元」という日付をともなうID付きイベント要素を作成した場合にそのIDに対する参照を行う。</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[6]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[1]`.

```xml
<desc versionDate="2012-08-15" xml:lang="en">supplies a pointer to a <gi>calendar</gi> element or other
        means of interpreting the values of the custom dating attributes.</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[2]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">
          ここで提供するポインタは、<gi>calendar</gi> 要素もしくは日付を示す属性の値を解釈する何らかの方式を指す。</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[7]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[7]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-jw" source="#STOW">Contayning the Originall, Antiquity, Increaſe, Moderne 
            eſtate, and deſcription of that Citie, written in the yeare 
            <date when-custom="1598" calendar="#julian" datingMethod="#julian">1598</date>. by Iohn Stow 
            Citizen of London.</egXML>
        <p>In this example, the <att>calendar</att> attribute points to a <gi>calendar</gi> element for the 
          Julian calendar, specifying that the text content of the <gi>date</gi> element is a 
          Julian date, and the <att>datingMethod</att> attribute also points to the Julian calendar
          to indicate that the content of the <att>when-custom</att> attribute value is Julian too.</p>
      </exemplum>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[7]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DATABLECUSTOM-egXML-yd">
          <date when="1382-06-28" when-custom="6890-06-20" datingMethod="#creationOfWorld">
            μηνὶ Ἰουνίου εἰς <num>κ</num> ἔτους <num>ςωϞ</num>
          </date>
        </egXML>
        <p>In this example, a date is given in a Mediaeval text measured <q>from the creation of the world</q>, which is normalized
        (in <att>when</att>) to the Gregorian date, but is also normalized (in <att>when-custom</att>) to a
        machine-actionable, numeric version of the date from the Creation.</p>
      </exemplum>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[7]/remarks[1]`.

```xml
<remarks ident="att.datable.custom-attr.datingMethod-remarks" versionDate="2015-05-29" xml:lang="en"><p>Note that the <att>datingMethod</att> attribute (unlike
        <att>calendar</att> defined in <ident type="class">att.datable</ident>) defines
        the calendar or dating system to which the date described by the parent element is normalized (i.e. in the  
        <att>when-custom</att> or other <att>X-custom</att> attributes), <emph>not</emph> the calendar of the
        original date in the element.</p></remarks>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[7]/remarks[2]`.

```xml
<remarks ident="att.datable.custom-attr.datingMethod-remarks" versionDate="2019-02-13" xml:lang="ja"><p>（<ident type="class">att.datable</ident>で定義される<att>calendar</att> 属性とは違って）
        <att>datingMethod</att>属性が定義するのは、親要素で記述された日付を正規化した暦や暦法であり、
        当該要素中のオリジナルの日付の暦<emph>ではない</emph>。</p></remarks>
```

^b29

### Block 30

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDDATE"/>
  </listRef>
```

^b30

