---
type: representation
source-type: document
source: '[[00_sources/tei-p5-msitem-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 msItem
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/msItem.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# msItem

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5149. Git blob: `982e6ef9f63535bdbbb50abb62936fc6db973dce`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="MSITEM" ident="msItem">
  <gloss versionDate="2007-07-04" xml:lang="en">manuscript item</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">원고 항목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">elemento del manuscrito</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">item de manuscrit</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">parte di manoscritto</gloss>
  <desc versionDate="2018-11-19" xml:lang="en">describes an individual work or item within the intellectual
  content of a manuscript, manuscript part, or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 지적 내용 내에서 개별 작품 또는 항목을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿或手稿部分的智慧內容中所包含的單一作品或項目。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の知的内容の中に出現する、独立した作品または項目を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit une œuvre ou un item individualisés dans le
      contenu intellectuel d'un manuscrit ou d'une partie de manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe una obra individual o un elemento al interno del contenido intelectual de un manuscrito o de una de sus partes.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive una singola opera o oggetto all'interno del contenuto intellettuale di un manoscritto o di una sua parte.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msClass"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="model.msItemPart"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="locus"/>
          <elementRef key="locusGrp"/>
        </alternate>
      
      <alternate>
        
          <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        
        
          <alternate minOccurs="1" maxOccurs="unbounded">
            <classRef key="model.titlepagePart"/>
            <classRef key="model.msItemPart"/>
            <classRef key="model.global"/>
          </alternate>
        
      </alternate>
    </sequence>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEM-egXML-pn" xml:lang="non">
      <msItem class="#saga">
        <locus>ff. 1r-24v</locus>
        <title>Agrip af Noregs konunga sögum</title>
        <incipit>regi oc h<ex>ann</ex> setiho
<gap reason="illegible" extent="7"/>sc 
heim se<ex>m</ex> þio</incipit>
        <explicit>h<ex>on</ex> hev<ex>er</ex> 
               <ex>oc</ex>þa buit hesta .ij. aNan viþ 
fé enh<ex>on</ex>o<ex>m</ex> aNan til
reiþ<ex>ar</ex>
            </explicit>
        <textLang mainLang="non">Old Norse/Icelandic</textLang>
      </msItem>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEM-egXML-vl" source="#fr-ex-BnF-Reliures">
      <msContents>
        <msItem>
          <!-- pour le traitement des recueils la solution possible est de répéter l'élément <msItem>  -->
          <docAuthor>
            <surname>Longus</surname>
          </docAuthor>
          <docTitle>
            <titlePart type="main">Les amours pastorales de Daphnis et Chloé</titlePart>
          </docTitle>
          <docImprint>
            <pubPlace>Paris</pubPlace>
            <publisher>[Jacques Quillau]</publisher>
          </docImprint>
          <docDate when="1718">1718</docDate>
          <note>in-8°.</note>
          <!-- in-32°; in-24°; in-16°; in-8°; in-4°; in-folio; gr. folio -->
          <note>Exemplaire réglé.</note>
          <note>
            <ref target="http://catalogue.bnf.fr/ark:/12148/cb30831232s">Notice bibliographique
                dans le Catalogue général</ref>
          </note>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEM-egXML-ym">
      <msItem>
        <locus>f.495</locus>
        <title>台灣隨筆</title>
        <incipit>幾荷蘭人由洋中來，假地日本，久而不帰，遂築城而有之。</incipit>
        <explicit>惟商舶可以航海，凡使節往來咸藉之。</explicit>
        <textLang mainLang="zh-tw">繁體中文</textLang>
      </msItem>
      <!-- http://catalog.ndap.org.tw/?URN=2155367 -->
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
<gloss versionDate="2007-07-04" xml:lang="en">manuscript item</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">원고 항목</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">elemento del manuscrito</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">item de manuscrit</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">parte di manoscritto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-11-19" xml:lang="en">describes an individual work or item within the intellectual
  content of a manuscript, manuscript part, or other object.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 지적 내용 내에서 개별 작품 또는 항목을 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿或手稿部分的智慧內容中所包含的單一作品或項目。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の知的内容の中に出現する、独立した作品または項目を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit une œuvre ou un item individualisés dans le
      contenu intellectuel d'un manuscrit ou d'une partie de manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe una obra individual o un elemento al interno del contenido intelectual de un manuscrito o de una de sus partes.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive una singola opera o oggetto all'interno del contenuto intellettuale di un manoscritto o di una sua parte.</desc>
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
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="locus"/>
          <elementRef key="locusGrp"/>
        </alternate>
      
      <alternate>
        
          <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        
        
          <alternate minOccurs="1" maxOccurs="unbounded">
            <classRef key="model.titlepagePart"/>
            <classRef key="model.msItemPart"/>
            <classRef key="model.global"/>
          </alternate>
        
      </alternate>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEM-egXML-pn" xml:lang="non">
      <msItem class="#saga">
        <locus>ff. 1r-24v</locus>
        <title>Agrip af Noregs konunga sögum</title>
        <incipit>regi oc h<ex>ann</ex> setiho
<gap reason="illegible" extent="7"/>sc 
heim se<ex>m</ex> þio</incipit>
        <explicit>h<ex>on</ex> hev<ex>er</ex> 
               <ex>oc</ex>þa buit hesta .ij. aNan viþ 
fé enh<ex>on</ex>o<ex>m</ex> aNan til
reiþ<ex>ar</ex>
            </explicit>
        <textLang mainLang="non">Old Norse/Icelandic</textLang>
      </msItem>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEM-egXML-vl" source="#fr-ex-BnF-Reliures">
      <msContents>
        <msItem>
          <!-- pour le traitement des recueils la solution possible est de répéter l'élément <msItem>  -->
          <docAuthor>
            <surname>Longus</surname>
          </docAuthor>
          <docTitle>
            <titlePart type="main">Les amours pastorales de Daphnis et Chloé</titlePart>
          </docTitle>
          <docImprint>
            <pubPlace>Paris</pubPlace>
            <publisher>[Jacques Quillau]</publisher>
          </docImprint>
          <docDate when="1718">1718</docDate>
          <note>in-8°.</note>
          <!-- in-32°; in-24°; in-16°; in-8°; in-4°; in-folio; gr. folio -->
          <note>Exemplaire réglé.</note>
          <note>
            <ref target="http://catalogue.bnf.fr/ark:/12148/cb30831232s">Notice bibliographique
                dans le Catalogue général</ref>
          </note>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSITEM-egXML-ym">
      <msItem>
        <locus>f.495</locus>
        <title>台灣隨筆</title>
        <incipit>幾荷蘭人由洋中來，假地日本，久而不帰，遂築城而有之。</incipit>
        <explicit>惟商舶可以航海，凡使節往來咸藉之。</explicit>
        <textLang mainLang="zh-tw">繁體中文</textLang>
      </msItem>
      <!-- http://catalog.ndap.org.tw/?URN=2155367 -->
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

