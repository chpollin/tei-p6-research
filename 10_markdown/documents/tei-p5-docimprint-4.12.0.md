---
type: representation
source-type: document
source: '[[00_sources/tei-p5-docimprint-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 docImprint
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/docImprint.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# docImprint

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7232. Git blob: `41f41e6b8a0b870221905a5d165b1b289fec7d0c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-docImprint" ident="docImprint">
  <gloss versionDate="2005-01-14" xml:lang="en">document imprint</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문서 간기</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文件出版說明</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">mention d'impression</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Impressum des Dokuments</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de imprenta</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">sigla editoriale del documento</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the imprint statement (place and date of publication,
publisher name), as given
(usually) at the foot of a title page.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">대개 제목 페이지 아래에 제시되는 인쇄 판 진술(출판 장소와 날짜, 출판사명)을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件出版陳述 (出版日期、地點以及出版公司名稱) ，同於 (通常) 題名頁尾所顯示的出版資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">刊記にある出版関連情報を示す。例えば、出版日、出版者名など。一般には
  タイトルページの下にある。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la mention d'impression 
            de l'éditeur (lieu et date de publication, nom de l’éditeur), telle qu’elle est
            généralement donnée au bas de la page de titre.</desc>
  <desc versionDate="2017-06-25" xml:lang="de">enthält das Impressum (Erscheinungsort und -datum, Verlag), das (üblicherweise) am unteren Rand der Titelseite steht.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la declaración de la publicación (lugar y fecha de publicación, casa editorial) tal y como consta al pie del frontispicio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la dichiarazione di pubblicazione (luogo e data di pubblicazione, casa editrice) così come riportata di norma in fondo al frontespizio.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <elementRef key="pubPlace"/>
        <elementRef key="docDate"/>
        <elementRef key="publisher"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-ad">
      <docImprint>Oxford, Clarendon Press, 1987</docImprint>
    </egXML>
    <p>Imprints may be somewhat more complex:
<egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-yw"><docImprint><pubPlace>London</pubPlace>
Printed for <name>E. Nutt</name>,
at 
<pubPlace>Royal Exchange</pubPlace>;
<name>J. Roberts</name> in 
<pubPlace>wick-Lane</pubPlace>;
<name>A. Dodd</name> without 
<pubPlace>Temple-Bar</pubPlace>;
and <name>J. Graves</name> in 
<pubPlace>St. James's-street.</pubPlace>
               <date>1722.</date>
            </docImprint></egXML>
      </p>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-jw">
      <docImprint>Oxford, Clarendon Press, 1987</docImprint>
    </egXML>
    <p>Das Impressum kann auch etwas komplexer sein:
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-db"><docImprint><pubPlace>London</pubPlace>
        Printed for <name>E. Nutt</name>,
        at 
        <pubPlace>Royal Exchange</pubPlace>;
        <name>J. Roberts</name> in 
        <pubPlace>wick-Lane</pubPlace>;
        <name>A. Dodd</name> without 
        <pubPlace>Temple-Bar</pubPlace>;
        and <name>J. Graves</name> in 
        <pubPlace>St. James's-street.</pubPlace>
        <date>1722.</date>
      </docImprint></egXML>
    </p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-dt">
      <docImprint>2006, Les Editions Trintexte, Trinity College, Toronto, Canada M5S
        1H8</docImprint>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <p>La description de l'impression est parfois plus complexe:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-od">
      <docImprint><pubPlace>PARIS</pubPlace>, <name>Delangle Frères</name> Éditeurs-libraires,
            <pubPlace>Place de la Bourse</pubPlace>
        </docImprint>
      <docDate>MDCCCXXX</docDate>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-zy">
      <docImprint>上海：中華書局，2001年。</docImprint>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-si">
      <docImprint><date>1995</date>年初版發行於<pubPlace>台北</pubPlace>：<pubPlace>麥田出版</pubPlace>，<name>王德威</name>主編 ; 另外亦出版於<pubPlace>香港</pubPlace>： <pubPlace>城邦</pubPlace>; <pubPlace>馬來西亞</pubPlace>：<pubPlace>城邦</pubPlace>。</docImprint>
    </egXML>
  </exemplum>
  <remarks ident="docImprint-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Cf. the <gi>imprint</gi> element of bibliographic
citations.  As with title, author, and editions, the shorter name is
reserved for the element likely to be used more often.</p>
  </remarks>
  <remarks ident="docImprint-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Voir l'élément <gi>imprint</gi> dans une citation bibliographique. Comme pour le
                titre, l'auteur, et la mention d'édition, le nom le plus court est réservé à
                l'élément le plus fréquemment utilisé.</p>
  </remarks>
  <remarks ident="docImprint-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    書誌情報向けの要素<gi>imprint</gi>も参照のこと。タイトル、著者名、
    版については、よく使われる要素により簡単な名前が記述される。
    </p>
  </remarks>
  <remarks ident="docImprint-remarks" versionDate="2017-06-25" xml:lang="de">
    <p>Vgl. das <gi>imprint</gi>-Element für bibliografische Angaben. Wie bei <gi>title</gi>,
      <gi>author</gi> und <gi>edition</gi> ist der kürzere Name für das häufiger benutzte Element
      reserviert.</p>
  </remarks>
  <listRef>
    <ptr target="#DSTITL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">document imprint</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문서 간기</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文件出版說明</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">mention d'impression</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Impressum des Dokuments</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de imprenta</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">sigla editoriale del documento</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the imprint statement (place and date of publication,
publisher name), as given
(usually) at the foot of a title page.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">대개 제목 페이지 아래에 제시되는 인쇄 판 진술(출판 장소와 날짜, 출판사명)을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件出版陳述 (出版日期、地點以及出版公司名稱) ，同於 (通常) 題名頁尾所顯示的出版資訊。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">刊記にある出版関連情報を示す。例えば、出版日、出版者名など。一般には
  タイトルページの下にある。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la mention d'impression 
            de l'éditeur (lieu et date de publication, nom de l’éditeur), telle qu’elle est
            généralement donnée au bas de la page de titre.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">enthält das Impressum (Erscheinungsort und -datum, Verlag), das (üblicherweise) am unteren Rand der Titelseite steht.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la declaración de la publicación (lugar y fecha de publicación, casa editorial) tal y como consta al pie del frontispicio.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la dichiarazione di pubblicazione (luogo e data di pubblicazione, casa editrice) così come riportata di norma in fondo al frontespizio.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <elementRef key="pubPlace"/>
        <elementRef key="docDate"/>
        <elementRef key="publisher"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-ad">
      <docImprint>Oxford, Clarendon Press, 1987</docImprint>
    </egXML>
    <p>Imprints may be somewhat more complex:
<egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-yw"><docImprint><pubPlace>London</pubPlace>
Printed for <name>E. Nutt</name>,
at 
<pubPlace>Royal Exchange</pubPlace>;
<name>J. Roberts</name> in 
<pubPlace>wick-Lane</pubPlace>;
<name>A. Dodd</name> without 
<pubPlace>Temple-Bar</pubPlace>;
and <name>J. Graves</name> in 
<pubPlace>St. James's-street.</pubPlace>
               <date>1722.</date>
            </docImprint></egXML>
      </p>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-jw">
      <docImprint>Oxford, Clarendon Press, 1987</docImprint>
    </egXML>
    <p>Das Impressum kann auch etwas komplexer sein:
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-db"><docImprint><pubPlace>London</pubPlace>
        Printed for <name>E. Nutt</name>,
        at 
        <pubPlace>Royal Exchange</pubPlace>;
        <name>J. Roberts</name> in 
        <pubPlace>wick-Lane</pubPlace>;
        <name>A. Dodd</name> without 
        <pubPlace>Temple-Bar</pubPlace>;
        and <name>J. Graves</name> in 
        <pubPlace>St. James's-street.</pubPlace>
        <date>1722.</date>
      </docImprint></egXML>
    </p>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-dt">
      <docImprint>2006, Les Editions Trintexte, Trinity College, Toronto, Canada M5S
        1H8</docImprint>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="fr">
    <p>La description de l'impression est parfois plus complexe:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-od">
      <docImprint><pubPlace>PARIS</pubPlace>, <name>Delangle Frères</name> Éditeurs-libraires,
            <pubPlace>Place de la Bourse</pubPlace>
        </docImprint>
      <docDate>MDCCCXXX</docDate>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-zy">
      <docImprint>上海：中華書局，2001年。</docImprint>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docImprint-egXML-si">
      <docImprint><date>1995</date>年初版發行於<pubPlace>台北</pubPlace>：<pubPlace>麥田出版</pubPlace>，<name>王德威</name>主編 ; 另外亦出版於<pubPlace>香港</pubPlace>： <pubPlace>城邦</pubPlace>; <pubPlace>馬來西亞</pubPlace>：<pubPlace>城邦</pubPlace>。</docImprint>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="docImprint-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Cf. the <gi>imprint</gi> element of bibliographic
citations.  As with title, author, and editions, the shorter name is
reserved for the element likely to be used more often.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="docImprint-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Voir l'élément <gi>imprint</gi> dans une citation bibliographique. Comme pour le
                titre, l'auteur, et la mention d'édition, le nom le plus court est réservé à
                l'élément le plus fréquemment utilisé.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="docImprint-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    書誌情報向けの要素<gi>imprint</gi>も参照のこと。タイトル、著者名、
    版については、よく使われる要素により簡単な名前が記述される。
    </p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="docImprint-remarks" versionDate="2017-06-25" xml:lang="de">
    <p>Vgl. das <gi>imprint</gi>-Element für bibliografische Angaben. Wie bei <gi>title</gi>,
      <gi>author</gi> und <gi>edition</gi> ist der kürzere Name für das häufiger benutzte Element
      reserviert.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b28

