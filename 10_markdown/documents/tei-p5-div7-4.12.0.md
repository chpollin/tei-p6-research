---
type: representation
source-type: document
source: '[[00_sources/tei-p5-div7-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 div7
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/div7.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# div7

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6065. Git blob: `ee5c15e14d6583d45c2824c0f3af79cf2f75e158`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-div7" ident="div7">
  <gloss versionDate="2005-01-14" xml:lang="en">level-7 text division</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">7 층위 텍스트 구역</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次七</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr"> division du texte de niveau 7</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de"> Textgliederungsebene -7</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">división textual de nivel séptimo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 7</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the smallest possible subdivision of the front, body or back of a text, larger than
    a paragraph.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의, 문단보다 큰 가능한 한 가장 작은 하위 구역을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的最低層分段，分段層級高於段落。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の一番小さいレベルのテキスト部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la plus petite subdivision possible dans le
    texte préliminaire, dans le corps d’un texte ou dans le texte postliminaire, plus grande
    néanmoins qu’un paragraphe.</desc>
  <desc versionDate="2006-10-18" xml:lang="de"> enthält die kleinste mögliche Untergliederung von
    Vorspann (front), Kerntext oder Nachspann (back) eines Textes, die größer als ein Absatz ist.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la subdivisión más pequeña, pero más grande que
    un párrafo, del paratexto inicial, del cuerpo del texto o del paratexto final.</desc>
    <desc versionDate="2007-01-21" xml:lang="it">contiene la sezione più ristretta, ma più ampia di un
    paragrafo, del peritesto iniziale, del corpo del testo, o del peritesto finale</desc>
    <classes>
      <memberOf key="att.global"/>
      <memberOf key="att.declaring"/>
      <memberOf key="att.divLike"/>
      <memberOf key="att.typed"/>
      <memberOf key="model.div7Like"/>
    </classes>
    <content>
      <sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
        <sequence minOccurs="0">
          <sequence minOccurs="1" maxOccurs="unbounded">
            <alternate minOccurs="1" maxOccurs="1">
              <elementRef key="schemaSpec"/>
              <classRef key="model.common"/>
            </alternate>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
          <sequence minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.divBottom"/>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
        </sequence>
      </sequence>
    </content>
    <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div7-egXML-sr" source="#divEGs">
        <div2 type="chapter">
          <head>Recipes</head>
          <head>Chapter VI.</head>
          <div3>
            <head>Fruit and vegetable soups</head>
            <p>...</p>
            <div4>
              <head>Stocks for all kinds of soups</head>
              <div5 type="recipe">
                <head>Asparagus soup</head>
                <div6 type="altRecipe">
                  <head>I.</head>
                  <div7>
                    <head>Ingredients</head>
                    <list>
                      <item> ...</item>
                    </list>
                  </div7>
                  <div7>
                    <head>Mode</head>
                    <p>Put the beef, cut into pieces and rolled in flour, into a
                    stewpan...</p>
                  </div7>
                  <!-- ... -->
                </div6>
                <div6 type="altRecipe">
                  <head>II.</head>
                  <div7>
                    <head>Ingredients</head>
                    <list>
                      <item> ...</item>
                    </list>
                  </div7>
                  <div7>
                    <head>Mode</head>
                    <p>Boil the peas, and rub them through a sieve; add the gravy...</p>
                  </div7>
                </div6>
              </div5>
            </div4>
          </div3>
        </div2>
      </egXML>
    </exemplum>
    <remarks ident="div7-remarks" versionDate="2006-07-02" xml:lang="en">
      <p rend="dataDesc">any sequence of low-level structural elements, e.g., paragraphs (<gi>p</gi>),
      lists (<gi>list</gi>), or examples (<gi>eg</gi> or <gi>egXML</gi>).</p>
    </remarks>
    <remarks ident="div7-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas niveau, par
      exemple des paragraphes (<gi>p</gi>), des listes (<gi>list</gi>), ou des exemples (<gi>eg</gi>
      ou <gi>egXML</gi>).</p>
    </remarks>
    <remarks ident="div7-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p rend="dataDesc"> 一連の低レベル構造単位要素。例えば、段落(<gi>p</gi>)、リスト
      (<gi>list</gi>)、用例(<gi>eg</gi>または<gi>egXML</gi>)など。 </p>
    </remarks>
    <listRef>
      <ptr target="#DSDIV2"/>
    </listRef>
  </elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">level-7 text division</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">7 층위 텍스트 구역</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次七</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr"> division du texte de niveau 7</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de"> Textgliederungsebene -7</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">división textual de nivel séptimo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 7</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the smallest possible subdivision of the front, body or back of a text, larger than
    a paragraph.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의, 문단보다 큰 가능한 한 가장 작은 하위 구역을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的最低層分段，分段層級高於段落。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の一番小さいレベルのテキスト部分を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la plus petite subdivision possible dans le
    texte préliminaire, dans le corps d’un texte ou dans le texte postliminaire, plus grande
    néanmoins qu’un paragraphe.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de"> enthält die kleinste mögliche Untergliederung von
    Vorspann (front), Kerntext oder Nachspann (back) eines Textes, die größer als ein Absatz ist.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la subdivisión más pequeña, pero más grande que
    un párrafo, del paratexto inicial, del cuerpo del texto o del paratexto final.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la sezione più ristretta, ma più ampia di un
    paragrafo, del peritesto iniziale, del corpo del testo, o del peritesto finale</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
      <memberOf key="att.global"/>
      <memberOf key="att.declaring"/>
      <memberOf key="att.divLike"/>
      <memberOf key="att.typed"/>
      <memberOf key="model.div7Like"/>
    </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
      <sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
        <sequence minOccurs="0">
          <sequence minOccurs="1" maxOccurs="unbounded">
            <alternate minOccurs="1" maxOccurs="1">
              <elementRef key="schemaSpec"/>
              <classRef key="model.common"/>
            </alternate>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
          <sequence minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.divBottom"/>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
        </sequence>
      </sequence>
    </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div7-egXML-sr" source="#divEGs">
        <div2 type="chapter">
          <head>Recipes</head>
          <head>Chapter VI.</head>
          <div3>
            <head>Fruit and vegetable soups</head>
            <p>...</p>
            <div4>
              <head>Stocks for all kinds of soups</head>
              <div5 type="recipe">
                <head>Asparagus soup</head>
                <div6 type="altRecipe">
                  <head>I.</head>
                  <div7>
                    <head>Ingredients</head>
                    <list>
                      <item> ...</item>
                    </list>
                  </div7>
                  <div7>
                    <head>Mode</head>
                    <p>Put the beef, cut into pieces and rolled in flour, into a
                    stewpan...</p>
                  </div7>
                  <!-- ... -->
                </div6>
                <div6 type="altRecipe">
                  <head>II.</head>
                  <div7>
                    <head>Ingredients</head>
                    <list>
                      <item> ...</item>
                    </list>
                  </div7>
                  <div7>
                    <head>Mode</head>
                    <p>Boil the peas, and rub them through a sieve; add the gravy...</p>
                  </div7>
                </div6>
              </div5>
            </div4>
          </div3>
        </div2>
      </egXML>
    </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="div7-remarks" versionDate="2006-07-02" xml:lang="en">
      <p rend="dataDesc">any sequence of low-level structural elements, e.g., paragraphs (<gi>p</gi>),
      lists (<gi>list</gi>), or examples (<gi>eg</gi> or <gi>egXML</gi>).</p>
    </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="div7-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas niveau, par
      exemple des paragraphes (<gi>p</gi>), des listes (<gi>list</gi>), ou des exemples (<gi>eg</gi>
      ou <gi>egXML</gi>).</p>
    </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="div7-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p rend="dataDesc"> 一連の低レベル構造単位要素。例えば、段落(<gi>p</gi>)、リスト
      (<gi>list</gi>)、用例(<gi>eg</gi>または<gi>egXML</gi>)など。 </p>
    </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
      <ptr target="#DSDIV2"/>
    </listRef>
```

^b22

