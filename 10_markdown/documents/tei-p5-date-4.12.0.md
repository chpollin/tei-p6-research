---
type: representation
source-type: document
source: '[[00_sources/tei-p5-date-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 date
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/date.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# date

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5113. Git blob: `bcb5156a698a67c534ba532242ffd972c0b6a726`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-date" ident="date">
  <gloss versionDate="2009-01-06" xml:lang="en">date</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">date</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Datum</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a date in any format.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다양한 형식의 날짜를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何格式的日期表示。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">日付を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une date exprimée dans n'importe quel format.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una fecha en cualquier formato.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una data in qualsiasi foemato.</desc>
  <desc versionDate="2016-11-25" xml:lang="de">enthält ein Datum in beliebigem Format.</desc>
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
    <memberOf key="model.publicationStmtPart.detail"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-vd">
      <date when="1980-02">early February 1980</date>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-wh">
      <date when="1980-02">au début de février 1980</date>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-el" source="#fr-ex-Pascal_Pensees">
      <date when="1654-11-23">L'an de grâce 1654,<lb/> Lundi, 23 novembre, jour de saint Clément,
          pape et martyr et autres au martyrologe, <lb/>Veille de saint Chrysogone, martyr, et
          autres, <lb/> Depuis environ dix heures et demie du soir jusques environ minuit et
        demi.</date>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-tj">
      <date when="1990-09">septembre mcmxc</date>
      <date when="--09">septembre</date>
      <date when="2001-09-11T12:48:00">11 septembre, neuf heures moins douze GMT</date>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-dy"> 他出生於<date calendar="#gregorian">西元2007年12月24日</date> (<date calendar="#chinese" when="2007-12-24"> 丁亥年11月15日</date>).</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-bv">
      <date when="1980-02">西元1980年2月初</date>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-ou"><date when="0637-11">貞觀十一年十一月</date>，唐太宗聽說年輕的武則天長得妖媚嬌艷，楚楚動人，便將她納入宮中，封為四品才人，賜號「武媚」。</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-si">
      <date when="1990-09">西元1990年9月</date>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-rr">Given on the <date when="1977-06-12">Twelfth Day
        of June in the Year of Our Lord One Thousand Nine Hundred and Seventy-seven of the Republic
        the Two Hundredth and first and of the University the Eighty-Sixth.</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-dd">
      <date when="1990-09">September 1990</date>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CONADA" type="div3"/>
    <ptr target="#HD24" type="div3"/>
    <ptr target="#HD6" type="div3"/>
    <ptr target="#COBICOI" type="div3"/>
    <ptr target="#CCAHSE" type="div3"/>
    <ptr target="#NDDATE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="en">date</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">date</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Datum</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a date in any format.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다양한 형식의 날짜를 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何格式的日期表示。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">日付を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une date exprimée dans n'importe quel format.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una fecha en cualquier formato.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una data in qualsiasi foemato.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">enthält ein Datum in beliebigem Format.</desc>
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
    <memberOf key="model.publicationStmtPart.detail"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-vd">
      <date when="1980-02">early February 1980</date>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-wh">
      <date when="1980-02">au début de février 1980</date>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-el" source="#fr-ex-Pascal_Pensees">
      <date when="1654-11-23">L'an de grâce 1654,<lb/> Lundi, 23 novembre, jour de saint Clément,
          pape et martyr et autres au martyrologe, <lb/>Veille de saint Chrysogone, martyr, et
          autres, <lb/> Depuis environ dix heures et demie du soir jusques environ minuit et
        demi.</date>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-tj">
      <date when="1990-09">septembre mcmxc</date>
      <date when="--09">septembre</date>
      <date when="2001-09-11T12:48:00">11 septembre, neuf heures moins douze GMT</date>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-dy"> 他出生於<date calendar="#gregorian">西元2007年12月24日</date> (<date calendar="#chinese" when="2007-12-24"> 丁亥年11月15日</date>).</egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-bv">
      <date when="1980-02">西元1980年2月初</date>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-ou"><date when="0637-11">貞觀十一年十一月</date>，唐太宗聽說年輕的武則天長得妖媚嬌艷，楚楚動人，便將她納入宮中，封為四品才人，賜號「武媚」。</egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-si">
      <date when="1990-09">西元1990年9月</date>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-rr">Given on the <date when="1977-06-12">Twelfth Day
        of June in the Year of Our Lord One Thousand Nine Hundred and Seventy-seven of the Republic
        the Two Hundredth and first and of the University the Eighty-Sixth.</date>
      </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[10]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-date-egXML-dd">
      <date when="1990-09">September 1990</date>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONADA" type="div3"/>
    <ptr target="#HD24" type="div3"/>
    <ptr target="#HD6" type="div3"/>
    <ptr target="#COBICOI" type="div3"/>
    <ptr target="#CCAHSE" type="div3"/>
    <ptr target="#NDDATE"/>
  </listRef>
```

^b24

