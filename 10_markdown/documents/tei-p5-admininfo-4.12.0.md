---
type: representation
source-type: document
source: '[[00_sources/tei-p5-admininfo-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 adminInfo
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/adminInfo.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# adminInfo

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5244. Git blob: `e6bf2b48fff0656e3453863e16a51aa43e2d0385`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="ADMININFO" ident="adminInfo">
  <gloss versionDate="2005-01-14" xml:lang="en">administrative information</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">관리 정보</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">行政資訊</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">informations administratives</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">información administrativa.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">informazioni amministrative</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">管理情報</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">administrative Information</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="adminfo.desc">contains information about the present
custody and availability of the manuscript or other object, and also about the record
description itself.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 현재 보관과 이용가능성, 그리고 기록 기술에 관한 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿現在的保管與可利用性資訊，也包含本身的紀錄描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料、またはその記録文書そのものの管理・利用形態についての情
 報を示す。</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">contient, pour le manuscrit en cours de description, les informations sur son détenteur actuel, sur ses conditions d'accès et sur les modalités de sa description.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene información relativa a la gestión y a la disponibilidad del manuscrito y a la descripción misma de la documentación.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative alla gestione e disponibilità del manoscritto e alla descrizione stessa della documentazione.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <!--<rng:choice >
    <rng:ref name="macro.specialPara"/>-->
    <sequence>
      
        <elementRef key="recordHist" minOccurs="0"/>
      
      
        <elementRef key="availability" minOccurs="0"/>
      
      
        <elementRef key="custodialHist" minOccurs="0"/>
      
      
        <classRef key="model.noteLike" minOccurs="0"/>
        <!-- was remarks -->
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADMININFO-egXML-fq" source="#UND">
      <adminInfo>
        <recordHist>
          <source>Record created <date>1 Aug 2004</date>
               </source>
        </recordHist>
        <availability>
          <p>Until 2015 permission to photocopy some materials from this
collection has been limited at the request of the donor. Please ask repository staff for details
if you are interested in obtaining photocopies from Series 1:
Correspondence.</p>
        </availability>
        <custodialHist>
          <p>Collection donated to the Manuscript Library by the Estate of
Edgar Holden in 1993. Donor number: 1993-034.</p>
        </custodialHist>
      </adminInfo>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADMININFO-egXML-jw" source="#fr-ex-BnF-Reliures">
      <adminInfo>
        <recordHist>
          <source>Notice établie à partir du document original</source>
          <change when="2009-10-05" who="Markova">Description mise à jour le <date type="crea">5
                octobre 2009 </date>en vue de l'encodage en TEI des descriptions des reliure de la
              Réserve des livres rares</change>
          <change when="2009-06-01" who="#Le_Bars">Description revue le <date type="maj">1er juin
                2009 </date> par Fabienne Le Bars</change>
          <change when="2009-06-25" who="#Le_Bars">Description validée le<date type="valid">25
                juin 2009</date>par Fabienne Le Bars</change>
        </recordHist>
      </adminInfo>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADMININFO-egXML-fs" source="#UND">
      <adminInfo>
        <recordHist>
          <source>紀錄建立於<date>2004年8月1日</date>
               </source>
        </recordHist>
        <availability>
          <p>2015年以前，非經贈與此書者同意，不得翻印。若對內容有興趣，請洽藏書單位。</p>
        </availability>
        <custodialHist>
          <p>此收藏1993年捐贈於故宮博物院。贈與編號：1993-034。</p>
        </custodialHist>
      </adminInfo>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msadad"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">administrative information</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">관리 정보</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">行政資訊</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">informations administratives</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">información administrativa.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">informazioni amministrative</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">管理情報</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">administrative Information</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="adminfo.desc">contains information about the present
custody and availability of the manuscript or other object, and also about the record
description itself.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 현재 보관과 이용가능성, 그리고 기록 기술에 관한 정보를 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿現在的保管與可利用性資訊，也包含本身的紀錄描述。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料、またはその記録文書そのものの管理・利用形態についての情
 報を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">contient, pour le manuscrit en cours de description, les informations sur son détenteur actuel, sur ses conditions d'accès et sur les modalités de sa description.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene información relativa a la gestión y a la disponibilidad del manuscrito y a la descripción misma de la documentación.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative alla gestione e disponibilità del manoscritto e alla descrizione stessa della documentazione.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!--<rng:choice >
    <rng:ref name="macro.specialPara"/>-->
    <sequence>
      
        <elementRef key="recordHist" minOccurs="0"/>
      
      
        <elementRef key="availability" minOccurs="0"/>
      
      
        <elementRef key="custodialHist" minOccurs="0"/>
      
      
        <classRef key="model.noteLike" minOccurs="0"/>
        <!-- was remarks -->
      
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADMININFO-egXML-fq" source="#UND">
      <adminInfo>
        <recordHist>
          <source>Record created <date>1 Aug 2004</date>
               </source>
        </recordHist>
        <availability>
          <p>Until 2015 permission to photocopy some materials from this
collection has been limited at the request of the donor. Please ask repository staff for details
if you are interested in obtaining photocopies from Series 1:
Correspondence.</p>
        </availability>
        <custodialHist>
          <p>Collection donated to the Manuscript Library by the Estate of
Edgar Holden in 1993. Donor number: 1993-034.</p>
        </custodialHist>
      </adminInfo>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADMININFO-egXML-jw" source="#fr-ex-BnF-Reliures">
      <adminInfo>
        <recordHist>
          <source>Notice établie à partir du document original</source>
          <change when="2009-10-05" who="Markova">Description mise à jour le <date type="crea">5
                octobre 2009 </date>en vue de l'encodage en TEI des descriptions des reliure de la
              Réserve des livres rares</change>
          <change when="2009-06-01" who="#Le_Bars">Description revue le <date type="maj">1er juin
                2009 </date> par Fabienne Le Bars</change>
          <change when="2009-06-25" who="#Le_Bars">Description validée le<date type="valid">25
                juin 2009</date>par Fabienne Le Bars</change>
        </recordHist>
      </adminInfo>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADMININFO-egXML-fs" source="#UND">
      <adminInfo>
        <recordHist>
          <source>紀錄建立於<date>2004年8月1日</date>
               </source>
        </recordHist>
        <availability>
          <p>2015年以前，非經贈與此書者同意，不得翻印。若對內容有興趣，請洽藏書單位。</p>
        </availability>
        <custodialHist>
          <p>此收藏1993年捐贈於故宮博物院。贈與編號：1993-034。</p>
        </custodialHist>
      </adminInfo>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msadad"/>
  </listRef>
```

^b21

