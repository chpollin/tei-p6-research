---
type: representation
source-type: document
source: '[[00_sources/tei-p5-custevent-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 custEvent
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/custEvent.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# custEvent

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3006. Git blob: `43b5c5adef455a50fd6e82673cbbc45d76ed9932`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="CUSTEVENT" ident="custEvent">
  <gloss versionDate="2007-07-04" xml:lang="en">custodial event</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">보관 사건</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">acontecimiento de la custodia</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">événement dans la conservation</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">evento legato alla conservazione</gloss>
  <gloss versionDate="2024-08-08" xml:lang="ja">保管中のイベント</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="custevent.desc">describes a single event during the custodial history of a manuscript or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 보관 이력 중 단일 사건에 대하여 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿保管歷史中的單一事件。</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">手書き資料の保管履歴における、ひとつの事象を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit un événement dans l'histoire de la conservation du manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe un único evento en la historia de la conservación de un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive un singolo evento nella storia della conservazione di un manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTEVENT-egXML-wn">
      <custEvent type="photography">Photographed by David Cooper on <date>12 Dec 1964</date>
         </custEvent>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTEVENT-egXML-bk">
      <custEvent type="photography">Photographed by David Cooper on <date>12 Dec
        1964</date>
         </custEvent>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTEVENT-egXML-se">
      <custEvent type="photography">大衛．庫柏攝於<date>1964年12月12日</date>
         </custEvent>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msadch"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">custodial event</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">보관 사건</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">acontecimiento de la custodia</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">événement dans la conservation</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">evento legato alla conservazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-08-08" xml:lang="ja">保管中のイベント</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="custevent.desc">describes a single event during the custodial history of a manuscript or other object.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 보관 이력 중 단일 사건에 대하여 기술한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿保管歷史中的單一事件。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">手書き資料の保管履歴における、ひとつの事象を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit un événement dans l'histoire de la conservation du manuscrit.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe un único evento en la historia de la conservación de un manuscrito.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive un singolo evento nella storia della conservazione di un manoscritto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTEVENT-egXML-wn">
      <custEvent type="photography">Photographed by David Cooper on <date>12 Dec 1964</date>
         </custEvent>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTEVENT-egXML-bk">
      <custEvent type="photography">Photographed by David Cooper on <date>12 Dec
        1964</date>
         </custEvent>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTEVENT-egXML-se">
      <custEvent type="photography">大衛．庫柏攝於<date>1964年12月12日</date>
         </custEvent>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msadch"/>
  </listRef>
```

^b20

