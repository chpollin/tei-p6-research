---
type: representation
source-type: document
source: '[[00_sources/tei-p5-back-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 back
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/back.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# back

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8769. Git blob: `11cba7c2e8eb4148795ba99e4832dc4cd8f2d011`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-back" ident="back">
  <gloss versionDate="2005-01-14" xml:lang="en">back matter</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">후면부 내용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">正文後資訊</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">texte annexe</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Nachspann (back)</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">paratexto final</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">peritesto finale</gloss>
  <gloss versionDate="2023-09-21" xml:lang="ja">後付</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains any appendixes, etc. following the main part
  of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 주요부 뒤에 오는 부록 등을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在正文之後，包含附錄等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">後付。本文の後に続く付録などを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient tout supplément placé après la partie
  principale d'un texte : appendice, etc.</desc>
  <desc versionDate="2006-10-18" xml:lang="de">enthält Anhänge jeglicher Art, die auf den Hauptteil
  eines Textes folgen.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de apéndice, etc. que aparece
  detrás del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene qualsiasi appendice che segua il testo vero
  e proprio</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.frontPart"/>
        <classRef key="model.pLike.front"/>
        <classRef key="model.pLike"/>
        <classRef key="model.listLike"/>
        <classRef key="model.global"/>
      </alternate>
      <alternate minOccurs="0">
        <sequence>
          <classRef key="model.div1Like"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.frontPart"/>
            <classRef key="model.div1Like"/>
            <classRef key="model.global"/>
          </alternate>
        </sequence>
        <sequence>
          <classRef key="model.divLike"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.frontPart"/>
            <classRef key="model.divLike"/>
            <classRef key="model.global"/>
          </alternate>
        </sequence>
      </alternate>
      <sequence minOccurs="0">
        <classRef key="model.divBottomPart"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divBottomPart"/>
          <classRef key="model.global"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-back-egXML-ep" source="#G2S">
      <back>
        <div type="appendix">
          <head>The Golden Dream or, the Ingenuous Confession</head>
          <p>TO shew the Depravity of human Nature, and how apt the Mind is to be misled by Trinkets
          and false Appearances, Mrs. Two-Shoes does acknowledge, that after she became rich, she
          had like to have been, too fond of Money <!-- .... -->
          </p>
        </div>
        <!-- ... -->
        <div type="epistle">
          <head>A letter from the Printer, which he desires may be inserted</head>
          <salute>Sir.</salute>
          <p>I have done with your Copy, so you may return it to the Vatican, if you please;
          <!-- ... -->
          </p>
        </div>
        <div type="advert">
          <head>The Books usually read by the Scholars of Mrs Two-Shoes are these and are sold at Mr
          Newbery's at the Bible and Sun in St Paul's Church-yard.</head>
          <list>
            <item n="1">The Christmas Box, Price 1d.</item>
            <item n="2">The History of Giles Gingerbread, 1d.</item>
            <!-- ... -->
            <item n="42">A Curious Collection of Travels, selected from the Writers of all Nations,
            10 Vol, Pr. bound 1l.</item>
          </list>
        </div>
        <div type="advert">
          <head>By the KING's Royal Patent, Are sold by J. NEWBERY, at the Bible and Sun in St.
          Paul's Church-Yard.</head>
          <list>
            <item n="1">Dr. James's Powders for Fevers, the Small-Pox, Measles, Colds, &amp;c. 2s.
            6d</item>
            <item n="2">Dr. Hooper's Female Pills, 1s.</item>
            <!-- ... -->
          </list>
        </div>
      </back>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-back-egXML-zk" source="#fr-ex-Lery">
      <back>
        <div n="1" type="appendice">
          <head>APPENDICE I </head>
          <head>CHAPITRE XV bis </head>
          <p>Des cruautez exercées par les Turcs, et autres peuples : et nommément par les
          Espagnols, beaucoup plus barbares que les Sauvages mesmes </p>
          <p>Premierement Chalcondile en son histoire de la decadence de l'Empire des Grecs, ...</p>
        </div>
        <div n="2" type="appendice">
          <head> Appendice 2</head>
          <head>Advertissement de l'autheur</head>
          <p>Outre les augmentations bien amples, et la revision beaucoup plus exacte que je n'avoye
          fait és precedentes Editions, j'ai pour le contentement des Lecteurs, plusieurs endroits
          de ceste quatrieme et derniere monstré ...</p>
        </div>
      </back>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-back-egXML-fr" source="#biblzh-tw_n50">
      <back>
        <div1 type="appendix">
          <head>臺灣現代詩論戰史資料彙編</head>
          <p>現代詩論戰史第一階段</p>
        </div1>
        <div1 type="epistle">
          <head>白先勇致瘂弦洛夫</head>
          <salute>您好，</salute>
          <p>您的副本我已使用完畢，可以歸還了，麻煩您。</p>
        </div1>
        <div1 type="advert">
          <head>本論文提及的專書，可於台灣各大書店詢問訂購。</head>
          <list>
            <item n="1">陳芳明《詩與現實》，台北：洪範，1983。</item>
            <item n="2">洛夫《詩人之鏡》，台北：大業，1969。</item>
            <item n="42">廖炳惠《回顧現代》，台北：麥田，1994。</item>
          </list>
        </div1>
        <div1 type="advert">
          <head><hi rend="center">詩集、詩選</hi>也可於網路書店購得。</head>
          <list>
            <item n="1">余光中《天狼星》，台北：洪範，1976。</item>
            <item n="2">席慕蓉著《無怨的青春》，台北，大地，1983。</item>
          </list>
        </div1>
      </back>
    </egXML>
  </exemplum>
  <remarks ident="back-remarks" versionDate="2015-01-30" xml:lang="en">
    <p>Because cultural conventions differ as to which elements are grouped as back matter and which
    as front matter, the content models for the <gi>back</gi> and <gi>front</gi> elements are
    identical.</p>
  </remarks>
  <remarks ident="back-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le modèle de contenu de l'élément <gi>back</gi> est identique à celui de l'élément
    <gi>front</gi>, ce qui permet de rendre compte de pratiques éditoriales qui ont évolué avec
    l'histoire culturelle.</p>
  </remarks>
  <remarks ident="back-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p>どのような内容が後付あるいは前付とされるかは文化的慣習で異なるため、<gi>back</gi>と<gi>front</gi>の内容モデルは同一である。</p>
  </remarks>
  <remarks ident="back-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Aufgrund von unterschiedlichen kulturellen Konventionen, die Angaben in Vorspann und Nachspann
    betreffend, sind die Inhaltsmodelle für die Elemente <gi>front</gi> und <gi>back</gi>
    identisch.</p>
  </remarks>
  <listRef>
    <ptr target="#DSBACK"/>
    <ptr target="#DS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">back matter</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">후면부 내용</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">正文後資訊</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">texte annexe</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Nachspann (back)</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">paratexto final</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">peritesto finale</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-09-21" xml:lang="ja">後付</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains any appendixes, etc. following the main part
  of a text.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 주요부 뒤에 오는 부록 등을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在正文之後，包含附錄等。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">後付。本文の後に続く付録などを示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient tout supplément placé après la partie
  principale d'un texte : appendice, etc.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">enthält Anhänge jeglicher Art, die auf den Hauptteil
  eines Textes folgen.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de apéndice, etc. que aparece
  detrás del texto.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene qualsiasi appendice che segua il testo vero
  e proprio</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.frontPart"/>
        <classRef key="model.pLike.front"/>
        <classRef key="model.pLike"/>
        <classRef key="model.listLike"/>
        <classRef key="model.global"/>
      </alternate>
      <alternate minOccurs="0">
        <sequence>
          <classRef key="model.div1Like"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.frontPart"/>
            <classRef key="model.div1Like"/>
            <classRef key="model.global"/>
          </alternate>
        </sequence>
        <sequence>
          <classRef key="model.divLike"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.frontPart"/>
            <classRef key="model.divLike"/>
            <classRef key="model.global"/>
          </alternate>
        </sequence>
      </alternate>
      <sequence minOccurs="0">
        <classRef key="model.divBottomPart"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divBottomPart"/>
          <classRef key="model.global"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-back-egXML-ep" source="#G2S">
      <back>
        <div type="appendix">
          <head>The Golden Dream or, the Ingenuous Confession</head>
          <p>TO shew the Depravity of human Nature, and how apt the Mind is to be misled by Trinkets
          and false Appearances, Mrs. Two-Shoes does acknowledge, that after she became rich, she
          had like to have been, too fond of Money <!-- .... -->
          </p>
        </div>
        <!-- ... -->
        <div type="epistle">
          <head>A letter from the Printer, which he desires may be inserted</head>
          <salute>Sir.</salute>
          <p>I have done with your Copy, so you may return it to the Vatican, if you please;
          <!-- ... -->
          </p>
        </div>
        <div type="advert">
          <head>The Books usually read by the Scholars of Mrs Two-Shoes are these and are sold at Mr
          Newbery's at the Bible and Sun in St Paul's Church-yard.</head>
          <list>
            <item n="1">The Christmas Box, Price 1d.</item>
            <item n="2">The History of Giles Gingerbread, 1d.</item>
            <!-- ... -->
            <item n="42">A Curious Collection of Travels, selected from the Writers of all Nations,
            10 Vol, Pr. bound 1l.</item>
          </list>
        </div>
        <div type="advert">
          <head>By the KING's Royal Patent, Are sold by J. NEWBERY, at the Bible and Sun in St.
          Paul's Church-Yard.</head>
          <list>
            <item n="1">Dr. James's Powders for Fevers, the Small-Pox, Measles, Colds, &amp;c. 2s.
            6d</item>
            <item n="2">Dr. Hooper's Female Pills, 1s.</item>
            <!-- ... -->
          </list>
        </div>
      </back>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-back-egXML-zk" source="#fr-ex-Lery">
      <back>
        <div n="1" type="appendice">
          <head>APPENDICE I </head>
          <head>CHAPITRE XV bis </head>
          <p>Des cruautez exercées par les Turcs, et autres peuples : et nommément par les
          Espagnols, beaucoup plus barbares que les Sauvages mesmes </p>
          <p>Premierement Chalcondile en son histoire de la decadence de l'Empire des Grecs, ...</p>
        </div>
        <div n="2" type="appendice">
          <head> Appendice 2</head>
          <head>Advertissement de l'autheur</head>
          <p>Outre les augmentations bien amples, et la revision beaucoup plus exacte que je n'avoye
          fait és precedentes Editions, j'ai pour le contentement des Lecteurs, plusieurs endroits
          de ceste quatrieme et derniere monstré ...</p>
        </div>
      </back>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-back-egXML-fr" source="#biblzh-tw_n50">
      <back>
        <div1 type="appendix">
          <head>臺灣現代詩論戰史資料彙編</head>
          <p>現代詩論戰史第一階段</p>
        </div1>
        <div1 type="epistle">
          <head>白先勇致瘂弦洛夫</head>
          <salute>您好，</salute>
          <p>您的副本我已使用完畢，可以歸還了，麻煩您。</p>
        </div1>
        <div1 type="advert">
          <head>本論文提及的專書，可於台灣各大書店詢問訂購。</head>
          <list>
            <item n="1">陳芳明《詩與現實》，台北：洪範，1983。</item>
            <item n="2">洛夫《詩人之鏡》，台北：大業，1969。</item>
            <item n="42">廖炳惠《回顧現代》，台北：麥田，1994。</item>
          </list>
        </div1>
        <div1 type="advert">
          <head><hi rend="center">詩集、詩選</hi>也可於網路書店購得。</head>
          <list>
            <item n="1">余光中《天狼星》，台北：洪範，1976。</item>
            <item n="2">席慕蓉著《無怨的青春》，台北，大地，1983。</item>
          </list>
        </div1>
      </back>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="back-remarks" versionDate="2015-01-30" xml:lang="en">
    <p>Because cultural conventions differ as to which elements are grouped as back matter and which
    as front matter, the content models for the <gi>back</gi> and <gi>front</gi> elements are
    identical.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="back-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le modèle de contenu de l'élément <gi>back</gi> est identique à celui de l'élément
    <gi>front</gi>, ce qui permet de rendre compte de pratiques éditoriales qui ont évolué avec
    l'histoire culturelle.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="back-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p>どのような内容が後付あるいは前付とされるかは文化的慣習で異なるため、<gi>back</gi>と<gi>front</gi>の内容モデルは同一である。</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="back-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Aufgrund von unterschiedlichen kulturellen Konventionen, die Angaben in Vorspann und Nachspann
    betreffend, sind die Inhaltsmodelle für die Elemente <gi>front</gi> und <gi>back</gi>
    identisch.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSBACK"/>
    <ptr target="#DS"/>
  </listRef>
```

^b26

