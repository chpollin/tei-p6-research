---
type: representation
source-type: document
source: '[[00_sources/tei-p5-time-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 time
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/time.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# time

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3267. Git blob: `86e7ef2be58db063a96b94e526acc13e4d86da25`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-time" ident="time">
  <gloss versionDate="2009-01-06" xml:lang="en">time</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">temps</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Zeit</gloss>
  <desc versionDate="2006-03-20" xml:lang="en">contains a phrase defining a time of day in any format.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 형식의, 하루의 시간을 정의하는 구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一組字詞，以任何形式定義時間</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">時間を表す語句を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une expression qui précise un moment de la journée sous n'importe quelle forme.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un sintagma que define un momento del día en cualquier formato.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un sintagma che si riferisce ad un ora del giorno in qualsiasi formato.</desc>
  <desc versionDate="2016-11-25" xml:lang="de">beinhaltet eine Phrase, die eine Uhr- oder Tageszeit in einem beliebigen Format bestimmt.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.calendarSystem"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.duration"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.dateLike"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-time-egXML-kw" source="#CONADA-eg-143">As he sat smiling, the
      quarter struck — <time when="11:45:00">the quarter to twelve</time>.</egXML>
    <!-- Woolf, Mrs Dalloway, p64 -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-time-egXML-kg" source="#fr-ex-Mrejen_Eau"> Bonsoir, il est <time when="00:00:00">minuit</time> ici, l'heure de dormir, et chez vous
    à Paris, il est seulement <time when="07:00:00">7 h.</time> Je te
    rapporterai plein de souvenirs pour te faire partager cette
    expérience unique. </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-time-egXML-do"> 下班火車將於 <time when="11:45:00">差一刻十二點</time>出發。</egXML>
  </exemplum>
  <listRef>
    <ptr target="#CONADA" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="en">time</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">temps</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Zeit</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-03-20" xml:lang="en">contains a phrase defining a time of day in any format.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 형식의, 하루의 시간을 정의하는 구를 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一組字詞，以任何形式定義時間</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間を表す語句を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une expression qui précise un moment de la journée sous n'importe quelle forme.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un sintagma que define un momento del día en cualquier formato.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un sintagma che si riferisce ad un ora del giorno in qualsiasi formato.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">beinhaltet eine Phrase, die eine Uhr- oder Tageszeit in einem beliebigen Format bestimmt.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.calendarSystem"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.duration"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.dateLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-time-egXML-kw" source="#CONADA-eg-143">As he sat smiling, the
      quarter struck — <time when="11:45:00">the quarter to twelve</time>.</egXML>
    <!-- Woolf, Mrs Dalloway, p64 -->
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-time-egXML-kg" source="#fr-ex-Mrejen_Eau"> Bonsoir, il est <time when="00:00:00">minuit</time> ici, l'heure de dormir, et chez vous
    à Paris, il est seulement <time when="07:00:00">7 h.</time> Je te
    rapporterai plein de souvenirs pour te faire partager cette
    expérience unique. </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-time-egXML-do"> 下班火車將於 <time when="11:45:00">差一刻十二點</time>出發。</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONADA" type="div3"/>
  </listRef>
```

^b17

