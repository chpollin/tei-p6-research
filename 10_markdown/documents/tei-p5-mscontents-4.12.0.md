---
type: representation
source-type: document
source: '[[00_sources/tei-p5-mscontents-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 msContents
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/msContents.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# msContents

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10148. Git blob: `5b25405c2ad66615d6b30328674fdc917d1ca88a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="MSCONTENTS" ident="msContents">
  <gloss versionDate="2007-07-04" xml:lang="en">manuscript contents</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">원고 내용</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">contenido del manuscrito</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">contenu du manuscrit</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">contenuto del manoscritto</gloss>
  <desc versionDate="2018-10-26" xml:lang="en" xml:id="mscontents.desc">describes the intellectual content of a manuscript, manuscript
    part, or other object either as a series of paragraphs or as a series of structured manuscript items.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일련의 문단으로 또는 일련의 구조화된 원고 항목으로 원고 또는 원고 일부의 지적 내용을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿或手稿部分的智慧內容，可以是一系列的文字段落，或是一系列有組織的手稿項目。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の知的内容を、一連の段落または一連の構造化された手書き資料 項目として示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit le contenu intellectuel d'un manuscrit ou d'une
    partie d'un manuscrit, soit en une série de paragraphes <term>p</term>, soit sous la forme d'une
    série d'éléments structurés <term>msItem</term> concernant les items du manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe el contenido intelectual de un manuscrito o
    parte de un manuscrito, a través de párrafos o fragemtos del manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive il contenuto intellettuale di un manoscritto o
    di una sua parte tramite una serie di paragrafi o brani del manoscritto</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msClass"/>
    <memberOf key="att.msExcerpt"/>
  </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="textLang" minOccurs="0"/>
        
        
          <elementRef key="titlePage" minOccurs="0"/>
        
        
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="msItem"/>
            <elementRef key="msItemStruct"/>
          </alternate>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-wm">
      <msContents class="#sermons">
        <p>A collection of Lollard sermons</p>
      </msContents>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-jd" source="#fr-ex-BnF-Reliures">
      <msContents>
        <msItem>
          <!-- pour le traitement des recueils la solution possible est de répéter l'élément <msItem>  -->
          <docAuthor>
            <forename>Guillaume de Lorris </forename>
          </docAuthor>
          <docAuthor>
            <forename>Jean de Meung</forename>
          </docAuthor>
          <docTitle>
            <titlePart type="main">Le Rommant de la rose</titlePart>
            <titlePart type="sub"/>
          </docTitle>
          <docImprint>
            <pubPlace>Paris</pubPlace>
            <publisher>Antoine Vérard</publisher>
          </docImprint>
          <docDate when="1497">1497 ou 1498</docDate>
          <note>
            <date notBefore="1497-01-01" notAfter="1498-12-31"/>
          </note>
          <note>in-2°.</note>
          <!-- in-32°; in-24°; in-16°; in-8°; in-4°; in-folio; gr. folio -->
          <note>Exemplaire sur vélin, enluminé, « vraisemblablement dans l’atelier d’Antoine
              Vérard » <ref target="#fr_bib06">(Charon 1988, n° 3)</ref>
               </note>
          <note>
            <ref target="http://catalogue.bnf.fr/ark:/12148/cb305575966">Notice bibliographique
                dans le Catalogue général</ref>
          </note>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-en" source="#fr-ex-BnF-Reliures">
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-xf">
      <msContents>
        <p>金剛般若波羅蜜經</p>
      </msContents>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-sz" source="#biblzh-tw_n46">
      <msContents>
        <msItem n="1">
          <locus>fols. 109-119</locus>
          <title>金剛般若經依天親菩薩論贊略釋秦本義記卷上</title>
          <bibl>
            <title>大正新脩大藏經第85冊</title>
            <biblScope>10</biblScope>
          </bibl>
        </msItem>
        <msItem n="2">
          <locus>fols. 120-129</locus>
          <title xml:lang="zh-TW">金剛經疏</title>
          <bibl>
            <title>大正新脩大藏經第85冊</title>
            <biblScope>10</biblScope>
          </bibl>
        </msItem>
        <msItem n="3">
          <locus>fol. 1-1070</locus>
          <title>大般若波羅蜜多經</title>
          <bibl>
            <title>大正新脩大藏經第5冊</title>
            <biblScope>1070</biblScope>
          </bibl>
        </msItem>
        <msItem n="4">
          <locus>fols. 771-775</locus>
          <title>佛說能斷金剛般若波羅蜜多經</title>
          <bibl>
            <title>大正新脩大藏經第8冊</title>
            <biblScope>6</biblScope>
          </bibl>
        </msItem>
        <msItem n="5">
          <locus>fols. 752-757</locus>
          <bibl>
            <title>金剛般若波羅蜜經</title>
            <title>大正新脩大藏經第8冊</title>
            <biblScope>6</biblScope>
          </bibl>
        </msItem>
        <msItem n="6">
          <locus>fols. 1-8</locus>
          <title>梁朝傅大士頌金剛經</title>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-ti">
      <msContents>
        <msItem n="1">
          <locus>fols. 5r-7v</locus>
          <title>An ABC</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>239</biblScope>
          </bibl>
        </msItem>
        <msItem n="2">
          <locus>fols. 7v-8v</locus>
          <title xml:lang="frm">Lenvoy de Chaucer a Scogan</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>3747</biblScope>
          </bibl>
        </msItem>
        <msItem n="3">
          <locus>fol. 8v</locus>
          <title>Truth</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>809</biblScope>
          </bibl>
        </msItem>
        <msItem n="4">
          <locus>fols. 8v-10v</locus>
          <title>Birds Praise of Love</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>1506</biblScope>
          </bibl>
        </msItem>
        <msItem n="5">
          <locus>fols. 10v-11v</locus>
          <title xml:lang="la">De amico ad amicam</title>
          <title xml:lang="la">Responcio</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>16 &amp; 19</biblScope>
          </bibl>
        </msItem>
        <msItem n="6">
          <locus>fols. 14r-126v</locus>
          <title>Troilus and Criseyde</title>
          <note>Bk. 1:71-Bk. 5:1701, with additional losses due to mutilation throughout</note>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
  <remarks ident="msContents-remarks" versionDate="2009-04-17" xml:lang="en">
    <p>Unless it contains a simple prose description, this element should contain at least one of
      the elements <gi>summary</gi>, <gi>msItem</gi>, or <gi>msItemStruct</gi>. This constraint is
      not currently enforced by the schema.</p>
  </remarks>
  <remarks ident="msContents-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>A moins qu'il ne contienne une description en texte libre, cet élément doit contenir au moins
      l'un des éléments <gi>summary</gi>, <gi>msItem</gi> ou <gi>msItemStruct</gi>. Actuellement le schéma ne rend pas obligatoire cette contrainte.</p>
  </remarks>
  <listRef>
    <ptr target="#msco"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">manuscript contents</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">원고 내용</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">contenido del manuscrito</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contenu du manuscrit</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">contenuto del manoscritto</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-10-26" xml:lang="en" xml:id="mscontents.desc">describes the intellectual content of a manuscript, manuscript
    part, or other object either as a series of paragraphs or as a series of structured manuscript items.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일련의 문단으로 또는 일련의 구조화된 원고 항목으로 원고 또는 원고 일부의 지적 내용을 기술한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿或手稿部分的智慧內容，可以是一系列的文字段落，或是一系列有組織的手稿項目。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の知的内容を、一連の段落または一連の構造化された手書き資料 項目として示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit le contenu intellectuel d'un manuscrit ou d'une
    partie d'un manuscrit, soit en une série de paragraphes <term>p</term>, soit sous la forme d'une
    série d'éléments structurés <term>msItem</term> concernant les items du manuscrit.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe el contenido intelectual de un manuscrito o
    parte de un manuscrito, a través de párrafos o fragemtos del manuscrito.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il contenuto intellettuale di un manoscritto o
    di una sua parte tramite una serie di paragrafi o brani del manoscritto</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msClass"/>
    <memberOf key="att.msExcerpt"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="textLang" minOccurs="0"/>
        
        
          <elementRef key="titlePage" minOccurs="0"/>
        
        
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="msItem"/>
            <elementRef key="msItemStruct"/>
          </alternate>
        
      </sequence>
    </alternate>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-wm">
      <msContents class="#sermons">
        <p>A collection of Lollard sermons</p>
      </msContents>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-jd" source="#fr-ex-BnF-Reliures">
      <msContents>
        <msItem>
          <!-- pour le traitement des recueils la solution possible est de répéter l'élément <msItem>  -->
          <docAuthor>
            <forename>Guillaume de Lorris </forename>
          </docAuthor>
          <docAuthor>
            <forename>Jean de Meung</forename>
          </docAuthor>
          <docTitle>
            <titlePart type="main">Le Rommant de la rose</titlePart>
            <titlePart type="sub"/>
          </docTitle>
          <docImprint>
            <pubPlace>Paris</pubPlace>
            <publisher>Antoine Vérard</publisher>
          </docImprint>
          <docDate when="1497">1497 ou 1498</docDate>
          <note>
            <date notBefore="1497-01-01" notAfter="1498-12-31"/>
          </note>
          <note>in-2°.</note>
          <!-- in-32°; in-24°; in-16°; in-8°; in-4°; in-folio; gr. folio -->
          <note>Exemplaire sur vélin, enluminé, « vraisemblablement dans l’atelier d’Antoine
              Vérard » <ref target="#fr_bib06">(Charon 1988, n° 3)</ref>
               </note>
          <note>
            <ref target="http://catalogue.bnf.fr/ark:/12148/cb305575966">Notice bibliographique
                dans le Catalogue général</ref>
          </note>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-en" source="#fr-ex-BnF-Reliures">
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

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-xf">
      <msContents>
        <p>金剛般若波羅蜜經</p>
      </msContents>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-sz" source="#biblzh-tw_n46">
      <msContents>
        <msItem n="1">
          <locus>fols. 109-119</locus>
          <title>金剛般若經依天親菩薩論贊略釋秦本義記卷上</title>
          <bibl>
            <title>大正新脩大藏經第85冊</title>
            <biblScope>10</biblScope>
          </bibl>
        </msItem>
        <msItem n="2">
          <locus>fols. 120-129</locus>
          <title xml:lang="zh-TW">金剛經疏</title>
          <bibl>
            <title>大正新脩大藏經第85冊</title>
            <biblScope>10</biblScope>
          </bibl>
        </msItem>
        <msItem n="3">
          <locus>fol. 1-1070</locus>
          <title>大般若波羅蜜多經</title>
          <bibl>
            <title>大正新脩大藏經第5冊</title>
            <biblScope>1070</biblScope>
          </bibl>
        </msItem>
        <msItem n="4">
          <locus>fols. 771-775</locus>
          <title>佛說能斷金剛般若波羅蜜多經</title>
          <bibl>
            <title>大正新脩大藏經第8冊</title>
            <biblScope>6</biblScope>
          </bibl>
        </msItem>
        <msItem n="5">
          <locus>fols. 752-757</locus>
          <bibl>
            <title>金剛般若波羅蜜經</title>
            <title>大正新脩大藏經第8冊</title>
            <biblScope>6</biblScope>
          </bibl>
        </msItem>
        <msItem n="6">
          <locus>fols. 1-8</locus>
          <title>梁朝傅大士頌金剛經</title>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSCONTENTS-egXML-ti">
      <msContents>
        <msItem n="1">
          <locus>fols. 5r-7v</locus>
          <title>An ABC</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>239</biblScope>
          </bibl>
        </msItem>
        <msItem n="2">
          <locus>fols. 7v-8v</locus>
          <title xml:lang="frm">Lenvoy de Chaucer a Scogan</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>3747</biblScope>
          </bibl>
        </msItem>
        <msItem n="3">
          <locus>fol. 8v</locus>
          <title>Truth</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>809</biblScope>
          </bibl>
        </msItem>
        <msItem n="4">
          <locus>fols. 8v-10v</locus>
          <title>Birds Praise of Love</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>1506</biblScope>
          </bibl>
        </msItem>
        <msItem n="5">
          <locus>fols. 10v-11v</locus>
          <title xml:lang="la">De amico ad amicam</title>
          <title xml:lang="la">Responcio</title>
          <bibl>
            <title>IMEV</title>
            <biblScope>16 &amp; 19</biblScope>
          </bibl>
        </msItem>
        <msItem n="6">
          <locus>fols. 14r-126v</locus>
          <title>Troilus and Criseyde</title>
          <note>Bk. 1:71-Bk. 5:1701, with additional losses due to mutilation throughout</note>
        </msItem>
      </msContents>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="msContents-remarks" versionDate="2009-04-17" xml:lang="en">
    <p>Unless it contains a simple prose description, this element should contain at least one of
      the elements <gi>summary</gi>, <gi>msItem</gi>, or <gi>msItemStruct</gi>. This constraint is
      not currently enforced by the schema.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="msContents-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>A moins qu'il ne contienne une description en texte libre, cet élément doit contenir au moins
      l'un des éléments <gi>summary</gi>, <gi>msItem</gi> ou <gi>msItemStruct</gi>. Actuellement le schéma ne rend pas obligatoire cette contrainte.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msco"/>
  </listRef>
```

^b23

