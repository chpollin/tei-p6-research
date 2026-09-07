---
type: representation
source-type: document
source: '[[00_sources/tei-p5-analytic-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 analytic
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/analytic.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# analytic

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5027. Git blob: `c47eafd94201d1de3be81517e55de8477ed9e06d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-analytic" ident="analytic">
  <gloss versionDate="2005-01-14" xml:lang="en">analytic level</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">분석적 층위</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">分析層書目</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">niveau analytique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nivel analítico.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">livello analitico</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">分析レベル</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains bibliographic elements describing an item (e.g. an article or poem) published
    within a monograph or journal and not as an independent publication.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">독립 출판이 아닌, 단행본 또는 학술지 내에 포함되어 출판된 항목(예를 들어, 논문 또는 시)을
    기술하는 참고문헌 요소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含某一項目 (例如詩或文章) 的書目元素，該項目並非獨立出版品，而是刊登在專題著作或是期刊當中。</desc>
  <desc versionDate="2022-05-09" xml:lang="ja">独立した出版物ではなく、書籍や雑誌に収録されている作品の書誌情報（例えば論文や詩）を記述する。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient des éléments descriptifs qui décrivent la
    bibliographie d'une ressource (par exemple un poème ou un article de revue) publiée à
    l'intérieur d'une monographie ou d'une ressource et non publiée de façon indépendante.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene los elementos bibliográficos que describen un
    ítem (p.ej. un artículo o un poema) publicado dentro de una monografía o revista y no como una
    publicación independiente.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene elementi bilbiografici che descrivono un'opera
    (ad esempio un articolo a una poesia) pubblicata in una monografia o una rivista e non come
    pubblicazione indipendente.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="author"/>
        <elementRef key="editor"/>
        <elementRef key="respStmt"/>
        <elementRef key="title"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="date"/>
        <elementRef key="textLang"/>
        <elementRef key="idno"/>
        <elementRef key="availability"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-analytic-egXML-sv">
      <biblStruct>
        <analytic>
          <author>Chesnutt, David</author>
          <title>Historical Editions in the States</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <date when="1991-12">(December, 1991):</date>
          </imprint>
            <biblScope>25.6</biblScope>
            <biblScope>377–380</biblScope>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
  <remarks ident="analytic-remarks" versionDate="2012-10-28" xml:lang="en">
    <p rend="dataDesc">May contain titles and statements of responsibility (author, editor, or
      other), in any order.</p>
    <p>The <gi>analytic</gi> element may only occur within a <gi>biblStruct</gi>, where its use
      is mandatory for the description of an analytic level bibliographic item.</p>
  </remarks>
  <remarks ident="analytic-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément peut contenir des titres et des mentions de responsabilité
      (auteur, éditeur scientifique, ou autre), et cela dans n'importe quel ordre.</p>
    <p>L'élément <gi>analytic</gi> n'est disponible qu'à l'intérieur de l'élément
      <gi>biblStruct</gi>, où il faut l'utiliser pour encoder la description bibliographique d'une
      partie composante.</p>
  </remarks>
  <remarks ident="analytic-remarks" versionDate="2018-12-28" xml:lang="ja">
    <p rend="dataDesc">タイトルや権利者(著者、編者など)を、任意の順番で示してよい。 </p>
    <p> 要素<gi>analytic</gi>は、要素<gi>biblStruct</gi>内でのみ使用することができる。分析レベルの書誌情報項目においては必須である。</p>
  </remarks>
  <listRef>
    <ptr target="#COBICOL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">analytic level</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">분석적 층위</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">分析層書目</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">niveau analytique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nivel analítico.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">livello analitico</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">分析レベル</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains bibliographic elements describing an item (e.g. an article or poem) published
    within a monograph or journal and not as an independent publication.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">독립 출판이 아닌, 단행본 또는 학술지 내에 포함되어 출판된 항목(예를 들어, 논문 또는 시)을
    기술하는 참고문헌 요소를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含某一項目 (例如詩或文章) 的書目元素，該項目並非獨立出版品，而是刊登在專題著作或是期刊當中。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">独立した出版物ではなく、書籍や雑誌に収録されている作品の書誌情報（例えば論文や詩）を記述する。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient des éléments descriptifs qui décrivent la
    bibliographie d'une ressource (par exemple un poème ou un article de revue) publiée à
    l'intérieur d'une monographie ou d'une ressource et non publiée de façon indépendante.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene los elementos bibliográficos que describen un
    ítem (p.ej. un artículo o un poema) publicado dentro de una monografía o revista y no como una
    publicación independiente.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene elementi bilbiografici che descrivono un'opera
    (ad esempio un articolo a una poesia) pubblicata in una monografia o una rivista e non come
    pubblicazione indipendente.</desc>
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
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="author"/>
        <elementRef key="editor"/>
        <elementRef key="respStmt"/>
        <elementRef key="title"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="date"/>
        <elementRef key="textLang"/>
        <elementRef key="idno"/>
        <elementRef key="availability"/>
      </alternate>
    
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-analytic-egXML-sv">
      <biblStruct>
        <analytic>
          <author>Chesnutt, David</author>
          <title>Historical Editions in the States</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <date when="1991-12">(December, 1991):</date>
          </imprint>
            <biblScope>25.6</biblScope>
            <biblScope>377–380</biblScope>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="analytic-remarks" versionDate="2012-10-28" xml:lang="en">
    <p rend="dataDesc">May contain titles and statements of responsibility (author, editor, or
      other), in any order.</p>
    <p>The <gi>analytic</gi> element may only occur within a <gi>biblStruct</gi>, where its use
      is mandatory for the description of an analytic level bibliographic item.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="analytic-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément peut contenir des titres et des mentions de responsabilité
      (auteur, éditeur scientifique, ou autre), et cela dans n'importe quel ordre.</p>
    <p>L'élément <gi>analytic</gi> n'est disponible qu'à l'intérieur de l'élément
      <gi>biblStruct</gi>, où il faut l'utiliser pour encoder la description bibliographique d'une
      partie composante.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="analytic-remarks" versionDate="2018-12-28" xml:lang="ja">
    <p rend="dataDesc">タイトルや権利者(著者、編者など)を、任意の順番で示してよい。 </p>
    <p> 要素<gi>analytic</gi>は、要素<gi>biblStruct</gi>内でのみ使用することができる。分析レベルの書誌情報項目においては必須である。</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOL"/>
  </listRef>
```

^b21

