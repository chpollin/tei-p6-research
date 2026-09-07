---
type: representation
source-type: document
source: '[[00_sources/tei-p5-div6-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 div6
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/div6.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# div6

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6090. Git blob: `8d2400042ca0045a569d4f6b01684fe7bc3f5eb3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-div6" ident="div6">
  <gloss versionDate="2005-01-14" xml:lang="en">level-6 text division</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">6 층위 텍스트 구역</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次六</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">division du texte de niveau 6</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Textgliederungsebene -6</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">división textual de sexto nivel</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 6</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a sixth-level subdivision of the front, body, or back of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의 여섯 번째 층위 하위 구역을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的第六層分段。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の第6位のテキスト部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une subdivision de sixième niveau dans le texte préliminaire, dans le corps d’un texte ou dans le texte postliminaire.</desc>
  <desc versionDate="2006-10-18" xml:lang="de"> enthält die sechste Gliederungsebene von Vorspann (front), Kerntext oder Nachspann (back) eines Textes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una subdivisión del sexto nivel en el paratexto inicial, en el cuerpo del texto o en el paratexto final.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una sezione di sesto livello del peritesto iniziale, del corpo del testo, o del peritesto finale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.divLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.div6Like"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.divTop"/>
        <classRef key="model.global"/>
      </alternate>
      <sequence minOccurs="0">
        <alternate>
          <sequence minOccurs="1" maxOccurs="unbounded">
            <alternate>
              <classRef key="model.div7Like"/>
              <classRef key="model.divGenLike"/>
            </alternate>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
          <sequence>
            <sequence minOccurs="1" maxOccurs="unbounded">
              <alternate minOccurs="1" maxOccurs="1">
                <elementRef key="schemaSpec"/>
                <classRef key="model.common"/>
              </alternate>
              <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
            </sequence>
            <sequence minOccurs="0" maxOccurs="unbounded">
              <alternate>
                <classRef key="model.div7Like"/>
                <classRef key="model.divGenLike"/>
              </alternate>
              <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
            </sequence>
          </sequence>
        </alternate>
        <sequence minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divBottom"/>
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div6-egXML-hu" source="#divEGs">
      <div2 type="chapter">
        <head>Recipes</head>
        <head>Chapter VI.</head>
        <div3>
          <head>Fruit and vegetable soups</head>
          <p>...</p>
          <div4>
            <head>Stocks for all kinds of soups</head>
            <div5 type="recipe">
              <head>Rich strong stock</head>
              <div6>
                <head>Ingredients</head>
                <list>
                  <item>4 lbs of shin of beef,</item>
                  <item>4 lbs of knuckle of veal,</item>
                  <!-- ... -->
                  <item>4 quarts of water</item>
                </list>
              </div6>
              <div6>
                <head>Mode</head>
                <p>Line a delicately clean stewpan... Strain through a very 
                fine hair sieve, or tammy, and it will be fit for use</p>
              </div6>
              <div6>
                <head>Time</head>
                <p>5 hours.</p>
              </div6>
              <div6>
                <head>Average cost</head>
                <p>1s 3d. per quart</p>
              </div6>
            </div5>
            <div5 type="recipe">
              <head>Medium Stock</head>
              <!-- ... -->
            </div5>
          </div4>
          <!-- ... -->
        </div3>
      </div2>
    </egXML>
  </exemplum>
  <remarks ident="div6-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any sequence of low-level structural elements, possibly grouped into lower
    subdivisions.</p>
  </remarks>
  <remarks ident="div6-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas niveau,
    éventuellement groupés en subdivisions.</p>
  </remarks>
  <remarks ident="div6-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 下位区分と成りうる一連の構造単位。 </p>
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
<gloss versionDate="2005-01-14" xml:lang="en">level-6 text division</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">6 층위 텍스트 구역</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次六</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">division du texte de niveau 6</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Textgliederungsebene -6</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">división textual de sexto nivel</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 6</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a sixth-level subdivision of the front, body, or back of a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의 여섯 번째 층위 하위 구역을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的第六層分段。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の第6位のテキスト部分を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une subdivision de sixième niveau dans le texte préliminaire, dans le corps d’un texte ou dans le texte postliminaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de"> enthält die sechste Gliederungsebene von Vorspann (front), Kerntext oder Nachspann (back) eines Textes.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una subdivisión del sexto nivel en el paratexto inicial, en el cuerpo del texto o en el paratexto final.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una sezione di sesto livello del peritesto iniziale, del corpo del testo, o del peritesto finale.</desc>
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
    <memberOf key="model.div6Like"/>
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
        <alternate>
          <sequence minOccurs="1" maxOccurs="unbounded">
            <alternate>
              <classRef key="model.div7Like"/>
              <classRef key="model.divGenLike"/>
            </alternate>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
          <sequence>
            <sequence minOccurs="1" maxOccurs="unbounded">
              <alternate minOccurs="1" maxOccurs="1">
                <elementRef key="schemaSpec"/>
                <classRef key="model.common"/>
              </alternate>
              <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
            </sequence>
            <sequence minOccurs="0" maxOccurs="unbounded">
              <alternate>
                <classRef key="model.div7Like"/>
                <classRef key="model.divGenLike"/>
              </alternate>
              <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
            </sequence>
          </sequence>
        </alternate>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div6-egXML-hu" source="#divEGs">
      <div2 type="chapter">
        <head>Recipes</head>
        <head>Chapter VI.</head>
        <div3>
          <head>Fruit and vegetable soups</head>
          <p>...</p>
          <div4>
            <head>Stocks for all kinds of soups</head>
            <div5 type="recipe">
              <head>Rich strong stock</head>
              <div6>
                <head>Ingredients</head>
                <list>
                  <item>4 lbs of shin of beef,</item>
                  <item>4 lbs of knuckle of veal,</item>
                  <!-- ... -->
                  <item>4 quarts of water</item>
                </list>
              </div6>
              <div6>
                <head>Mode</head>
                <p>Line a delicately clean stewpan... Strain through a very 
                fine hair sieve, or tammy, and it will be fit for use</p>
              </div6>
              <div6>
                <head>Time</head>
                <p>5 hours.</p>
              </div6>
              <div6>
                <head>Average cost</head>
                <p>1s 3d. per quart</p>
              </div6>
            </div5>
            <div5 type="recipe">
              <head>Medium Stock</head>
              <!-- ... -->
            </div5>
          </div4>
          <!-- ... -->
        </div3>
      </div2>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="div6-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any sequence of low-level structural elements, possibly grouped into lower
    subdivisions.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="div6-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas niveau,
    éventuellement groupés en subdivisions.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="div6-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 下位区分と成りうる一連の構造単位。 </p>
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

