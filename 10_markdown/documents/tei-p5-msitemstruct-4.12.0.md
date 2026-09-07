---
type: representation
source-type: document
source: '[[00_sources/tei-p5-msitemstruct-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 msItemStruct
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/msItemStruct.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# msItemStruct

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6952. Git blob: `2ae25c8deda60c585938f13e0667eb5505f0e89b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="MSITEMSTRUCT" ident="msItemStruct">
  <gloss versionDate="2007-07-04" xml:lang="en">structured manuscript item</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">구조화된 원고 항목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">elemento estructurado del manuscrito</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description structurée d'un item de manuscrit</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">parte strutturata di manoscritto</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="msitem.desc">contains a structured description for an
  individual work or item within the intellectual content of a manuscript, manuscript part, or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 지적 내용 내에서 개별 작품 또는 항목에 대한 구조화된 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含某單一作品或項目的結構性描述，該作品或項目存在於手稿或手稿部分的智慧內容中。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の知的内容の中に出現する、独立した作品または項目の構造的解
  説を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description structurée d'un item ou d'une
      œuvre, dans le contenu intellectuel d'un manuscrit ou d'une partie d'un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción estructurada de una obra individual o de un objeto al interno del contenido intelectual de un manuscrito o de una de sus partes.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione strutturata di una singola opera o oggetto all'interno del contenuto intellettuale di un manoscritto o di una sua parte.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msClass"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="model.msItemPart"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0">
          <elementRef key="locus"/>
          <elementRef key="locusGrp"/>
        </alternate>
      
      <alternate>
        
          <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        
        <sequence>
          
            <elementRef key="author" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="respStmt" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="title" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="rubric" minOccurs="0"/>
          
          
            <elementRef key="incipit" minOccurs="0"/>
          
          
            <elementRef key="msItemStruct" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="explicit" minOccurs="0"/>
          
          
            <elementRef key="finalRubric" minOccurs="0"/>
          
          
            <elementRef key="colophon" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="decoNote" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="listBibl" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <alternate minOccurs="0" maxOccurs="unbounded">
              <elementRef key="bibl"/>
              <elementRef key="biblStruct"/>
            </alternate>
          
          <elementRef key="filiation" minOccurs="0"/>
            
            <classRef key="model.noteLike" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="textLang" minOccurs="0"/>
          
        </sequence>
      </alternate>
    </sequence>
  </content>
  <exemplum versionDate="2016-03-10" xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEMSTRUCT-egXML-ia">
      <msItemStruct n="2" defective="false" class="#biblComm">
        <locus from="24v" to="97v">24v-97v</locus>
        <author>Apringius de Beja</author>
        <title type="uniform" xml:lang="la">Tractatus in Apocalypsin</title>
        <rubric>Incipit Trac<supplied reason="omitted">ta</supplied>tus 
in apoka<lb/>lipsin eruditissimi uiri <lb/> Apringi ep<ex>iscop</ex>i 
Pacensis eccl<ex>esi</ex>e</rubric>
        <finalRubric>EXPLIC<ex>IT</ex> EXPO<lb/>SITIO APOCALIPSIS 
QVA<ex>M</ex> EXPOSVIT DOM<lb/>NVS APRINGIUS EP<ex>ISCOPU</ex>S.
DEO GR<ex>ACI</ex>AS AGO. FI<lb/>NITO LABORE ISTO.</finalRubric>
        <bibl><ref target="http://amiBibl.xml#Apringius1900">Apringius</ref>, ed. Férotin</bibl>
        <textLang mainLang="la">Latin</textLang>
      </msItemStruct>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEMSTRUCT-egXML-sq">
      <msItemStruct n="2" defective="false" class="#biblComm">
        <locus from="24v" to="97v">24v-97v</locus>
        <author>Apringius de Beja</author>
        <title type="uniform" xml:lang="la">Tractatus in Apocalypsin</title>
        <rubric>Incipit Trac<supplied reason="omitted">ta</supplied>tus in apoka<lb/>lipsin
            eruditissimi uiri <lb/> Apringi ep<ex>iscop</ex>i Pacensis eccl<ex>esi</ex>e</rubric>
        <finalRubric>EXPLIC<ex>IT</ex> EXPO<lb/>SITIO APOCALIPSIS QVA<ex>M</ex>
            EXPOSVIT DOM<lb/>NVS APRINGIUS EP<ex>ISCOPU</ex>S. DEO GR<ex>ACI</ex>AS AGO.
            FI<lb/>NITO LABORE ISTO.</finalRubric>
        <bibl><ref target="http://amiBibl.xml#Apringius1900">Apringius</ref>, ed. Férotin</bibl>
        <textLang mainLang="la">Latin</textLang>
      </msItemStruct>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEMSTRUCT-egXML-ud">
      <msItemStruct>
        <locus from="1" to="4">pp.1-4</locus>
        <author>不詳</author>
        <title xml:lang="zh-TW">麻薯舊社屯外委潘清章等立招給墾批總約字</title>
        <rubric>4號，第九例。</rubric>
        <finalRubric>代筆社記</finalRubric>
        <bibl><ref target="http://catalog.ndap.org.tw/?URN=2155368">數位典藏聯合目錄</ref>，國立臺灣大學圖書館管理</bibl>
        <textLang mainLang="zh-tw">繁體中文</textLang>
      </msItemStruct>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mscoit"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">structured manuscript item</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">구조화된 원고 항목</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">elemento estructurado del manuscrito</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description structurée d'un item de manuscrit</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">parte strutturata di manoscritto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="msitem.desc">contains a structured description for an
  individual work or item within the intellectual content of a manuscript, manuscript part, or other object.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 지적 내용 내에서 개별 작품 또는 항목에 대한 구조화된 기술을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含某單一作品或項目的結構性描述，該作品或項目存在於手稿或手稿部分的智慧內容中。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の知的内容の中に出現する、独立した作品または項目の構造的解
  説を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description structurée d'un item ou d'une
      œuvre, dans le contenu intellectuel d'un manuscrit ou d'une partie d'un manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción estructurada de una obra individual o de un objeto al interno del contenido intelectual de un manuscrito o de una de sus partes.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione strutturata di una singola opera o oggetto all'interno del contenuto intellettuale di un manoscritto o di una sua parte.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msClass"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="model.msItemPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0">
          <elementRef key="locus"/>
          <elementRef key="locusGrp"/>
        </alternate>
      
      <alternate>
        
          <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        
        <sequence>
          
            <elementRef key="author" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="respStmt" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="title" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="rubric" minOccurs="0"/>
          
          
            <elementRef key="incipit" minOccurs="0"/>
          
          
            <elementRef key="msItemStruct" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="explicit" minOccurs="0"/>
          
          
            <elementRef key="finalRubric" minOccurs="0"/>
          
          
            <elementRef key="colophon" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="decoNote" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="listBibl" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <alternate minOccurs="0" maxOccurs="unbounded">
              <elementRef key="bibl"/>
              <elementRef key="biblStruct"/>
            </alternate>
          
          <elementRef key="filiation" minOccurs="0"/>
            
            <classRef key="model.noteLike" minOccurs="0" maxOccurs="unbounded"/>
          
          
            <elementRef key="textLang" minOccurs="0"/>
          
        </sequence>
      </alternate>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2016-03-10" xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEMSTRUCT-egXML-ia">
      <msItemStruct n="2" defective="false" class="#biblComm">
        <locus from="24v" to="97v">24v-97v</locus>
        <author>Apringius de Beja</author>
        <title type="uniform" xml:lang="la">Tractatus in Apocalypsin</title>
        <rubric>Incipit Trac<supplied reason="omitted">ta</supplied>tus 
in apoka<lb/>lipsin eruditissimi uiri <lb/> Apringi ep<ex>iscop</ex>i 
Pacensis eccl<ex>esi</ex>e</rubric>
        <finalRubric>EXPLIC<ex>IT</ex> EXPO<lb/>SITIO APOCALIPSIS 
QVA<ex>M</ex> EXPOSVIT DOM<lb/>NVS APRINGIUS EP<ex>ISCOPU</ex>S.
DEO GR<ex>ACI</ex>AS AGO. FI<lb/>NITO LABORE ISTO.</finalRubric>
        <bibl><ref target="http://amiBibl.xml#Apringius1900">Apringius</ref>, ed. Férotin</bibl>
        <textLang mainLang="la">Latin</textLang>
      </msItemStruct>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEMSTRUCT-egXML-sq">
      <msItemStruct n="2" defective="false" class="#biblComm">
        <locus from="24v" to="97v">24v-97v</locus>
        <author>Apringius de Beja</author>
        <title type="uniform" xml:lang="la">Tractatus in Apocalypsin</title>
        <rubric>Incipit Trac<supplied reason="omitted">ta</supplied>tus in apoka<lb/>lipsin
            eruditissimi uiri <lb/> Apringi ep<ex>iscop</ex>i Pacensis eccl<ex>esi</ex>e</rubric>
        <finalRubric>EXPLIC<ex>IT</ex> EXPO<lb/>SITIO APOCALIPSIS QVA<ex>M</ex>
            EXPOSVIT DOM<lb/>NVS APRINGIUS EP<ex>ISCOPU</ex>S. DEO GR<ex>ACI</ex>AS AGO.
            FI<lb/>NITO LABORE ISTO.</finalRubric>
        <bibl><ref target="http://amiBibl.xml#Apringius1900">Apringius</ref>, ed. Férotin</bibl>
        <textLang mainLang="la">Latin</textLang>
      </msItemStruct>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEMSTRUCT-egXML-ud">
      <msItemStruct>
        <locus from="1" to="4">pp.1-4</locus>
        <author>不詳</author>
        <title xml:lang="zh-TW">麻薯舊社屯外委潘清章等立招給墾批總約字</title>
        <rubric>4號，第九例。</rubric>
        <finalRubric>代筆社記</finalRubric>
        <bibl><ref target="http://catalog.ndap.org.tw/?URN=2155368">數位典藏聯合目錄</ref>，國立臺灣大學圖書館管理</bibl>
        <textLang mainLang="zh-tw">繁體中文</textLang>
      </msItemStruct>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mscoit"/>
  </listRef>
```

^b19

