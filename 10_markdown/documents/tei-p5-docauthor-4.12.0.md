---
type: representation
source-type: document
source: '[[00_sources/tei-p5-docauthor-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 docAuthor
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/docAuthor.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# docAuthor

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5621. Git blob: `cbf1679c301f859ff9f73db35194ec5c0535e5ea`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-docAuthor" ident="docAuthor">
  <gloss versionDate="2005-01-14" xml:lang="en">document author</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문서 저자</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文件作者</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">auteur du document</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Verfasser des Dokuments</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">autor del documento</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">autore del documento</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the name of the author of the document, as given on the
title page (often but not always contained in a byline).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">제목 페이지에 제시되는 문서의 작가명을 포함한다(그러나 종종 작자명 행에 포함되는 것은 아니다.)</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件作者名稱，同於題名頁上顯示的作者名 (經常但不一定出現在署名當中) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">タイトルページにある(一般には署名欄にある)当該文書の著者名を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le nom de l’auteur du document tel qu’il est donné sur la page de titre (ce nom est le plus souvent contenu dans une mention de responsabilité).</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält den Namen des Verfassers des Dokuments, wie auf dem Titelblatt angegeben (häufig, jedoch nicht immer in der Verfasserzeile).</desc>
  <desc versionDate="2021-02-18" xml:lang="es">contiene el nombre del autor del documento, tal y como aparece indicado en el frontispicio (a menudo, pero no siempre, contenido dentro del elemento <gi>byline</gi>).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome dell'autore del documento, come indicato nel frontespizio (spesso ma non sempre contenuto all'interno dell'elemento byline).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docAuthor-egXML-fm" source="#COEDCOR-eg-71">
      <titlePage>
        <docTitle>
          <titlePart>Travels into Several Remote Nations of the World, in Four
Parts.</titlePart>
        </docTitle>
        <byline> By <docAuthor>Lemuel Gulliver</docAuthor>, First a Surgeon,
and then a Captain of several Ships</byline>
      </titlePage>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docAuthor-egXML-dh">
      <titlePage>
        <docTitle>
          <titlePart>Le quart livre de faicts et dict Heroiques du bon
	  Pantagruel</titlePart>
        </docTitle>
        <byline>Composé par <docAuthor>M. François Rabelais</docAuthor> docteur en Medicine.</byline>
      </titlePage>
    </egXML>
  </exemplum>
  <remarks ident="docAuthor-remarks" versionDate="2015-06-28" xml:lang="en">
    <p>The document author's name often occurs within a byline, but
    the <gi>docAuthor</gi> element may be used whether the
    <gi>byline</gi> element is used or not. It should be used only for
    the author(s) of the entire document, not for author(s) of any
    subset or part of it. (Attributions of authorship of a subset or
    part of the document, for example of a chapter in a textbook or an
    article in a newspaper, may be encoded with <gi>byline</gi>
    without <gi>docAuthor</gi>.)</p>
  </remarks>
  <remarks ident="docAuthor-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le nom de l'auteur d'un document apparaît souvent au sein d'un élément
                <gi>byline</gi>, mais l'élément <gi>docAuthor</gi> peut être utilisé même si
                l'élément <gi>byline</gi> n'est pas présent.</p>
  </remarks>
  <remarks ident="docAuthor-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該文書の著者名が署名欄に書かれている場合、要素<gi>byline</gi>
    の使用状況とは関係なく、要素<gi>docAuthor</gi>は使用されることがあ
    る。
    </p>
  </remarks>
  <remarks ident="docAuthor-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Der Name eines Autors eines Dokuments erscheint zwar häufig in einer Verfasserzeile, das
      <gi>docAuthor</gi>-Element kann jedoch auch unabhängig von einem <gi>byline</gi>-Element
      benutzt werden. Es sollte jedoch nur für Autoren des gesamten Dokuments und nicht für Autoren
      von Abschnitten des Dokuments eingesetzt werden. (Für solche Fälle, wie z. B. Beiträge in
      Sammelbänden oder einzelne Zeitungsartikel, kann das <gi>byline</gi>-Element ohne die Angabe
      eines <gi>docAuthor</gi>-Elements benutzt.)</p>
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
<gloss versionDate="2005-01-14" xml:lang="en">document author</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문서 저자</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文件作者</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">auteur du document</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Verfasser des Dokuments</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">autor del documento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">autore del documento</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the name of the author of the document, as given on the
title page (often but not always contained in a byline).</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">제목 페이지에 제시되는 문서의 작가명을 포함한다(그러나 종종 작자명 행에 포함되는 것은 아니다.)</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件作者名稱，同於題名頁上顯示的作者名 (經常但不一定出現在署名當中) 。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">タイトルページにある(一般には署名欄にある)当該文書の著者名を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le nom de l’auteur du document tel qu’il est donné sur la page de titre (ce nom est le plus souvent contenu dans une mention de responsabilité).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält den Namen des Verfassers des Dokuments, wie auf dem Titelblatt angegeben (häufig, jedoch nicht immer in der Verfasserzeile).</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2021-02-18" xml:lang="es">contiene el nombre del autor del documento, tal y como aparece indicado en el frontispicio (a menudo, pero no siempre, contenido dentro del elemento <gi>byline</gi>).</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome dell'autore del documento, come indicato nel frontespizio (spesso ma non sempre contenuto all'interno dell'elemento byline).</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docAuthor-egXML-fm" source="#COEDCOR-eg-71">
      <titlePage>
        <docTitle>
          <titlePart>Travels into Several Remote Nations of the World, in Four
Parts.</titlePart>
        </docTitle>
        <byline> By <docAuthor>Lemuel Gulliver</docAuthor>, First a Surgeon,
and then a Captain of several Ships</byline>
      </titlePage>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docAuthor-egXML-dh">
      <titlePage>
        <docTitle>
          <titlePart>Le quart livre de faicts et dict Heroiques du bon
	  Pantagruel</titlePart>
        </docTitle>
        <byline>Composé par <docAuthor>M. François Rabelais</docAuthor> docteur en Medicine.</byline>
      </titlePage>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="docAuthor-remarks" versionDate="2015-06-28" xml:lang="en">
    <p>The document author's name often occurs within a byline, but
    the <gi>docAuthor</gi> element may be used whether the
    <gi>byline</gi> element is used or not. It should be used only for
    the author(s) of the entire document, not for author(s) of any
    subset or part of it. (Attributions of authorship of a subset or
    part of the document, for example of a chapter in a textbook or an
    article in a newspaper, may be encoded with <gi>byline</gi>
    without <gi>docAuthor</gi>.)</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="docAuthor-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le nom de l'auteur d'un document apparaît souvent au sein d'un élément
                <gi>byline</gi>, mais l'élément <gi>docAuthor</gi> peut être utilisé même si
                l'élément <gi>byline</gi> n'est pas présent.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="docAuthor-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該文書の著者名が署名欄に書かれている場合、要素<gi>byline</gi>
    の使用状況とは関係なく、要素<gi>docAuthor</gi>は使用されることがあ
    る。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="docAuthor-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Der Name eines Autors eines Dokuments erscheint zwar häufig in einer Verfasserzeile, das
      <gi>docAuthor</gi>-Element kann jedoch auch unabhängig von einem <gi>byline</gi>-Element
      benutzt werden. Es sollte jedoch nur für Autoren des gesamten Dokuments und nicht für Autoren
      von Abschnitten des Dokuments eingesetzt werden. (Für solche Fälle, wie z. B. Beiträge in
      Sammelbänden oder einzelne Zeitungsartikel, kann das <gi>byline</gi>-Element ohne die Angabe
      eines <gi>docAuthor</gi>-Elements benutzt.)</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b24

