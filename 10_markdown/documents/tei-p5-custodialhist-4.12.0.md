---
type: representation
source-type: document
source: '[[00_sources/tei-p5-custodialhist-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 custodialHist
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/custodialHist.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# custodialHist

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4695. Git blob: `05c9d5cf52ae2ce1a5aabc37d716e317e80506d0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="CUSTODIALHIST" ident="custodialHist">
  <gloss versionDate="2007-07-04" xml:lang="en">custodial history</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">보관 이력</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">historial de la custodia</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">histoire de la conservation</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">storia della conservazione</gloss>
  <gloss versionDate="2024-08-08" xml:lang="ja">保管履歴</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="custhist.desc">contains a description of a manuscript or other object's custodial history, either
as running prose or as a series of dated custodial events.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">연속적 산문체 또는 일련의 날짜가 표시된 보관 관련 사건을 통해서 원고의 보관 이력에 대한 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿保管歷史的描述，可以是篇章、或是一連串註明日期的保管事件。</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">手書き資料の保管履歴を示す。散文形式または一連の日付つき履歴で示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur l'histoire de la
      conservation, soit en texte libre, soit sous la forme d'une série d'éléments
      <gi>custEvent</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de la historia de la conservación del manuscrito en forma de prosa o come serie de eventos fechados relativos a la gestión del manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione della storia della conservazione del manoscritto sotto forma di prosa o come serie di eventi datati relativi alla gestione del manoscritto stesso.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      
        <elementRef key="custEvent" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTODIALHIST-egXML-gf">
      <custodialHist>
        <custEvent type="conservation" notBefore="1961-03" notAfter="1963-02">
Conserved between March 1961 and February 1963 at 
Birgitte Dalls Konserveringsværksted.</custEvent>
        <custEvent type="photography" notBefore="1988-05-01" notAfter="1988-05-30">
Photographed in 
May 1988 by AMI/FA.</custEvent>
        <custEvent type="transfer-dispatch" notBefore="1989-11-13" notAfter="1989-11-13">
Dispatched to Iceland 
13 November 1989.</custEvent>
      </custodialHist>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTODIALHIST-egXML-np">
      <custodialHist>
        <custEvent type="conservation" notBefore="1961-03" notAfter="1963-02"> Conserved between
            March 1961 and February 1963 at Birgitte Dalls Konserveringsværksted.</custEvent>
        <custEvent type="photography" notBefore="1988-05-01" notAfter="1988-05-30"> Photographed
            in May 1988 by AMI/FA.</custEvent>
        <custEvent type="transfer-dispatch" notBefore="1989-11-13" notAfter="1989-11-13">
            Dispatched to Iceland 13 November 1989.</custEvent>
      </custodialHist>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTODIALHIST-egXML-kq">
      <custodialHist>
        <custEvent type="conservation" notBefore="1961-03" notAfter="1963-02"> 1961年3月至1963年2月保存於北京國家文物典藏館</custEvent>
        <custEvent type="photography" notBefore="1988-05-01" notAfter="1988-05-30">1988年5月由國家攝影協會攝製</custEvent>
        <custEvent type="transfer-dispatch" notBefore="1989-11-13" notAfter="1989-11-13"> 1989年11月13日發送至冰島</custEvent>
      </custodialHist>
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
<gloss versionDate="2007-07-04" xml:lang="en">custodial history</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">보관 이력</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">historial de la custodia</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">histoire de la conservation</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">storia della conservazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-08-08" xml:lang="ja">保管履歴</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="custhist.desc">contains a description of a manuscript or other object's custodial history, either
as running prose or as a series of dated custodial events.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">연속적 산문체 또는 일련의 날짜가 표시된 보관 관련 사건을 통해서 원고의 보관 이력에 대한 기술을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿保管歷史的描述，可以是篇章、或是一連串註明日期的保管事件。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">手書き資料の保管履歴を示す。散文形式または一連の日付つき履歴で示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur l'histoire de la
      conservation, soit en texte libre, soit sous la forme d'une série d'éléments
      <gi>custEvent</gi>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de la historia de la conservación del manuscrito en forma de prosa o come serie de eventos fechados relativos a la gestión del manuscrito.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione della storia della conservazione del manoscritto sotto forma di prosa o come serie di eventi datati relativi alla gestione del manoscritto stesso.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      
        <elementRef key="custEvent" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTODIALHIST-egXML-gf">
      <custodialHist>
        <custEvent type="conservation" notBefore="1961-03" notAfter="1963-02">
Conserved between March 1961 and February 1963 at 
Birgitte Dalls Konserveringsværksted.</custEvent>
        <custEvent type="photography" notBefore="1988-05-01" notAfter="1988-05-30">
Photographed in 
May 1988 by AMI/FA.</custEvent>
        <custEvent type="transfer-dispatch" notBefore="1989-11-13" notAfter="1989-11-13">
Dispatched to Iceland 
13 November 1989.</custEvent>
      </custodialHist>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTODIALHIST-egXML-np">
      <custodialHist>
        <custEvent type="conservation" notBefore="1961-03" notAfter="1963-02"> Conserved between
            March 1961 and February 1963 at Birgitte Dalls Konserveringsværksted.</custEvent>
        <custEvent type="photography" notBefore="1988-05-01" notAfter="1988-05-30"> Photographed
            in May 1988 by AMI/FA.</custEvent>
        <custEvent type="transfer-dispatch" notBefore="1989-11-13" notAfter="1989-11-13">
            Dispatched to Iceland 13 November 1989.</custEvent>
      </custodialHist>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CUSTODIALHIST-egXML-kq">
      <custodialHist>
        <custEvent type="conservation" notBefore="1961-03" notAfter="1963-02"> 1961年3月至1963年2月保存於北京國家文物典藏館</custEvent>
        <custEvent type="photography" notBefore="1988-05-01" notAfter="1988-05-30">1988年5月由國家攝影協會攝製</custEvent>
        <custEvent type="transfer-dispatch" notBefore="1989-11-13" notAfter="1989-11-13"> 1989年11月13日發送至冰島</custEvent>
      </custodialHist>
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

