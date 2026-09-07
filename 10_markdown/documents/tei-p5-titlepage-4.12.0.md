---
type: representation
source-type: document
source: '[[00_sources/tei-p5-titlepage-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 titlePage
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/titlePage.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# titlePage

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7573. Git blob: `6273fd70c2b3d7920087a1ac7070e40a8a0227c8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-titlePage" ident="titlePage">
  <gloss versionDate="2005-01-14" xml:lang="en">title page</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">제목 페이지</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">題名頁</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">page de titre</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Titelseite</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">frontispicio</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">frontespizio</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the title page of a text, appearing within the front or back matter.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전면부 또는 후면부 자료 내에서 나타나는 텍스트의 제목 페이지를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文本的題名頁，出現在正文前資訊或正文後資訊之中。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">前付や後付中にある、テキストのタイトルページを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la page de titre d’un texte qui figure dans
    les parties liminaires.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält die Titelseite eines Textes, die entweder im
    Vorspann (front) oder Nachspann (back) stehen kann.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el frontispicio de un texto incluido en el
    paratexto inicial o final</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il frontespizio di un testo compreso nel
    peritesto iniziale o finale</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.frontPart"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.titlepagePart"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.titlepagePart"/>
	<classRef key="model.global"/>
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">classifies the title page according to any convenient typology.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">다양한 유형에 따라서 제목 페이지를 분류한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">將題名頁分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">タイトルページを分類する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">classe la page de titre selon la typologie
        appropriée.</desc>
      <desc versionDate="2017-06-19" xml:lang="de">klassifiziert die Titelseite entsprechend einer geeigneten
        Typologie.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica el frontispicio de acuerdo con una
        tipología funcional.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica il frontespizio in base a una tipologia
        funzionale</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="titlePage-attr.type-remarks" versionDate="2009-01-30" xml:lang="en">
        <p>This attribute allows the same element to be used for volume title pages, series title
          pages, etc., as well as for the <soCalled>main</soCalled>
          title page of a work. 
        </p>
      </remarks>
      <remarks ident="titlePage-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut est utile parce que c'est le même élément <gi>titlePage</gi> qui est utilisé
          pour les pages de titre de volumes, de collections, etc., et pour la page de titre
            <soCalled>principale</soCalled> d'un ouvrage.</p>
      </remarks>
      <remarks ident="titlePage-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、いわゆる<soCalled>主</soCalled>タイトルページのよ うに、巻タイトルページや叢書タイトルページなどで使われるものと 同じ要素をとる。 </p>
      </remarks>
      <remarks ident="titlePage-attr.type-remarks" versionDate="2017-06-19" xml:lang="de">
        <p>Dieses Attribut erlaubt es, das Element <gi>titlePage</gi> sowohl für Bandtitelseiten und
          Reihentitelseiten etc. als auch für die eigentliche Haupttitelseite eines Werks zu benutzen. 
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titlePage-egXML-nx" source="#deloneyThom">
      <titlePage>
        <docTitle>
          <titlePart type="main">THOMAS OF Reading.</titlePart>
          <titlePart type="alt">OR, The sixe worthy yeomen of the West.</titlePart>
        </docTitle>
        <docEdition>Now the fourth time corrected and enlarged</docEdition>
        <byline>By T.D.</byline>
        <figure>
          <head>TP</head>
          <p>Thou shalt labor till thou returne to duste</p>
          <figDesc>Printers Ornament used by TP</figDesc>
        </figure>
        <docImprint>Printed at <name type="place">London</name> for <name>T.P.</name>
               <date>1612.</date>
            </docImprint>
      </titlePage>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titlePage-egXML-bw" source="#fr-ex-TEI-simpl">
      <titlePage>
        <docTitle>
          <titlePart type="main"> Histoire du Roi de Bohême</titlePart>
          <titlePart type="sub"> et de ses sept châteaux </titlePart>
        </docTitle>
        <titlePart>Pastiche.</titlePart>
        <byline>Par <docAuthor>Charles Nodier</docAuthor>
            </byline>
        <epigraph>
          <q>O imitatores, servum pecus! </q>
          <bibl>Horat., Epist. I. XIX, 19.</bibl>
        </epigraph>
        <docImprint><name>PARIS</name>, <name>Delangle Frères</name> Éditeurs-libraires,
              <name>Place de la Bourse</name>
            </docImprint>
        <docDate>MDCCCXXX</docDate>
      </titlePage>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titlePage-egXML-hk">
      <titlePage>
        <docTitle>
          <titlePart type="main">紅樓夢</titlePart>
          <titlePart type="alt">又名石頭記</titlePart>
        </docTitle>
        <docEdition>清乾隆四十九年甲辰（1784年）夢覺主人序本正式題為《紅樓夢》，在此之前，此書一般都題為《石頭記》。</docEdition>
        <byline>曹雪芹</byline>
        <figure>
          <head>HL</head>
          <p>紅樓夢圖詠</p>
          <figDesc>清光緒刊本的《紅樓夢》插圖，改琦畫。</figDesc>
        </figure>
        <docImprint>最早的抄本出現於清朝乾隆中期的 <date>甲戌年（1754年）。</date>
            </docImprint>
      </titlePage>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DSTITL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">title page</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">제목 페이지</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">題名頁</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">page de titre</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Titelseite</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">frontispicio</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">frontespizio</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the title page of a text, appearing within the front or back matter.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전면부 또는 후면부 자료 내에서 나타나는 텍스트의 제목 페이지를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文本的題名頁，出現在正文前資訊或正文後資訊之中。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">前付や後付中にある、テキストのタイトルページを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la page de titre d’un texte qui figure dans
    les parties liminaires.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält die Titelseite eines Textes, die entweder im
    Vorspann (front) oder Nachspann (back) stehen kann.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el frontispicio de un texto incluido en el
    paratexto inicial o final</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il frontespizio di un testo compreso nel
    peritesto iniziale o finale</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.frontPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.titlepagePart"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.titlepagePart"/>
	<classRef key="model.global"/>
      </alternate>
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">classifies the title page according to any convenient typology.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다양한 유형에 따라서 제목 페이지를 분류한다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">將題名頁分類。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">タイトルページを分類する。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">classe la page de titre selon la typologie
        appropriée.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">klassifiziert die Titelseite entsprechend einer geeigneten
        Typologie.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica el frontispicio de acuerdo con una
        tipología funcional.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica il frontespizio in base a una tipologia
        funzionale</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="titlePage-attr.type-remarks" versionDate="2009-01-30" xml:lang="en">
        <p>This attribute allows the same element to be used for volume title pages, series title
          pages, etc., as well as for the <soCalled>main</soCalled>
          title page of a work. 
        </p>
      </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="titlePage-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut est utile parce que c'est le même élément <gi>titlePage</gi> qui est utilisé
          pour les pages de titre de volumes, de collections, etc., et pour la page de titre
            <soCalled>principale</soCalled> d'un ouvrage.</p>
      </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="titlePage-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、いわゆる<soCalled>主</soCalled>タイトルページのよ うに、巻タイトルページや叢書タイトルページなどで使われるものと 同じ要素をとる。 </p>
      </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="titlePage-attr.type-remarks" versionDate="2017-06-19" xml:lang="de">
        <p>Dieses Attribut erlaubt es, das Element <gi>titlePage</gi> sowohl für Bandtitelseiten und
          Reihentitelseiten etc. als auch für die eigentliche Haupttitelseite eines Werks zu benutzen. 
        </p>
      </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titlePage-egXML-nx" source="#deloneyThom">
      <titlePage>
        <docTitle>
          <titlePart type="main">THOMAS OF Reading.</titlePart>
          <titlePart type="alt">OR, The sixe worthy yeomen of the West.</titlePart>
        </docTitle>
        <docEdition>Now the fourth time corrected and enlarged</docEdition>
        <byline>By T.D.</byline>
        <figure>
          <head>TP</head>
          <p>Thou shalt labor till thou returne to duste</p>
          <figDesc>Printers Ornament used by TP</figDesc>
        </figure>
        <docImprint>Printed at <name type="place">London</name> for <name>T.P.</name>
               <date>1612.</date>
            </docImprint>
      </titlePage>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titlePage-egXML-bw" source="#fr-ex-TEI-simpl">
      <titlePage>
        <docTitle>
          <titlePart type="main"> Histoire du Roi de Bohême</titlePart>
          <titlePart type="sub"> et de ses sept châteaux </titlePart>
        </docTitle>
        <titlePart>Pastiche.</titlePart>
        <byline>Par <docAuthor>Charles Nodier</docAuthor>
            </byline>
        <epigraph>
          <q>O imitatores, servum pecus! </q>
          <bibl>Horat., Epist. I. XIX, 19.</bibl>
        </epigraph>
        <docImprint><name>PARIS</name>, <name>Delangle Frères</name> Éditeurs-libraires,
              <name>Place de la Bourse</name>
            </docImprint>
        <docDate>MDCCCXXX</docDate>
      </titlePage>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titlePage-egXML-hk">
      <titlePage>
        <docTitle>
          <titlePart type="main">紅樓夢</titlePart>
          <titlePart type="alt">又名石頭記</titlePart>
        </docTitle>
        <docEdition>清乾隆四十九年甲辰（1784年）夢覺主人序本正式題為《紅樓夢》，在此之前，此書一般都題為《石頭記》。</docEdition>
        <byline>曹雪芹</byline>
        <figure>
          <head>HL</head>
          <p>紅樓夢圖詠</p>
          <figDesc>清光緒刊本的《紅樓夢》插圖，改琦畫。</figDesc>
        </figure>
        <docImprint>最早的抄本出現於清朝乾隆中期的 <date>甲戌年（1754年）。</date>
            </docImprint>
      </titlePage>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b34

