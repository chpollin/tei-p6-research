---
type: representation
source-type: document
source: '[[00_sources/tei-p5-div3-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 div3
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/div3.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# div3

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7009. Git blob: `e0d6e7e17d2443c787d5053ac90f9284c84e2cd3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-div3" ident="div3">
  <gloss versionDate="2005-01-14" xml:lang="en">level-3 text division</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">3 층위 텍스트 구역</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次三</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">division du texte de niveau 3</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de"> Textgliederungsebene -3</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">división textual de tercer nivel</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 3</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a third-level subdivision of the front, body, or back of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의 세 번째 층위 하위 구역을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的第三層分段。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の第3位のテキスト部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une subdivision de troisième niveau dans
  le texte préliminaire, dans le corps d’un texte ou dans le texte postliminaire.</desc>
  <desc versionDate="2006-10-18" xml:lang="de"> enthält die dritte Gliederungsebene von Vorspann
  (front), Kerntext oder Nachspann (back) eines Textes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una subdivisión de tercer nivel en el paratexto
  inicial, en el cuerpo del texto o en el paratexto final.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una sezione di terzo livello del peritesto
  iniziale, del corpo del testo, o del peritesto finale</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.divLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.div3Like"/>
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
              <classRef key="model.div4Like"/>
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
                <classRef key="model.div4Like"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div3-egXML-kf" source="#COXR-eg-164">
      <div2 n="2.2" type="section">
        <div3 n="2.2.1" type="member">
          <head>Sect. II. Memb. I</head>
          <p> </p>
        </div3>
        <div3 n="2.2.2" type="member">
          <head>Memb. II Retention and Evacuation rectified.</head>
          <p> </p>
        </div3>
        <div3 n="2.2.3" type="member">
          <head>Memb. III Ayr rectified. With a digression of the Ayr.</head>
          <p> </p>
        </div3>
      </div2>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div3-egXML-gt">
      <div2 n="2.2" type="section">
        <div3 n="2.2.1" type="subsection">
          <head>Sect. II. Subsect. I Dictionnaires. </head>
          <p> C'est un recueil de mots rangés dans un ordre convenu...</p>
        </div3>
        <div3 n="2.2.2" type="subsection">
          <head>Sect. II. Subsect. II. Qu'est-ce qu'un dictionnaire de langue ? .</head>
          <p>Un dictionnaire de langue est un dictionnaire donnant les mots d'une langue et leurs
          emplois...</p>
        </div3>
        <div3 n="2.2.3" type="subsection">
          <head>Sect. II. Subsect. III. Qu'est-ce qu'un dictionnaire encyclopédique ? </head>
          <p>Un dictionnaire encyclopédique est un dictionnaire qui contient des renseignements
          sur les choses, sur les idées </p>
        </div3>
      </div2>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div3-egXML-vd" source="#biblzh-tw_n51-55">
      <div2 n="3.2" type="section">
        <div3 n="3.2.1" type="member">
          <head>打破內在/外在、主觀/客觀的二元對立</head>
          <p>在二○年代的蘇聯文藝界，...</p>
        </div3>
        <div3 n="3.2.2" type="member">
          <head>交流：藝術話語與生活話語的共性</head>
          <p>林林總總的文理理論圍繞著作者、作品和讀者的關係問題，...</p>
        </div3>
        <div3 n="2.2.3" type="member">
          <head>言談和音調</head>
          <p>在這裡，巴赫汀為言談做了一個大膽的定義：...</p>
        </div3>
      </div2>
    </egXML>
  </exemplum>
  <remarks ident="div3-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any sequence of low-level structural elements, possibly grouped into lower
    subdivisions.</p>
  </remarks>
  <remarks ident="div3-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas niveau,
    éventuellement groupés en subdivisions.</p>
  </remarks>
  <remarks ident="div3-remarks" versionDate="2008-04-05" xml:lang="ja">
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
<gloss versionDate="2005-01-14" xml:lang="en">level-3 text division</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">3 층위 텍스트 구역</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次三</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">division du texte de niveau 3</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de"> Textgliederungsebene -3</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">división textual de tercer nivel</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 3</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a third-level subdivision of the front, body, or back of a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의 세 번째 층위 하위 구역을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的第三層分段。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の第3位のテキスト部分を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une subdivision de troisième niveau dans
  le texte préliminaire, dans le corps d’un texte ou dans le texte postliminaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de"> enthält die dritte Gliederungsebene von Vorspann
  (front), Kerntext oder Nachspann (back) eines Textes.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una subdivisión de tercer nivel en el paratexto
  inicial, en el cuerpo del texto o en el paratexto final.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una sezione di terzo livello del peritesto
  iniziale, del corpo del testo, o del peritesto finale</desc>
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
    <memberOf key="model.div3Like"/>
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
              <classRef key="model.div4Like"/>
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
                <classRef key="model.div4Like"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div3-egXML-kf" source="#COXR-eg-164">
      <div2 n="2.2" type="section">
        <div3 n="2.2.1" type="member">
          <head>Sect. II. Memb. I</head>
          <p> </p>
        </div3>
        <div3 n="2.2.2" type="member">
          <head>Memb. II Retention and Evacuation rectified.</head>
          <p> </p>
        </div3>
        <div3 n="2.2.3" type="member">
          <head>Memb. III Ayr rectified. With a digression of the Ayr.</head>
          <p> </p>
        </div3>
      </div2>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div3-egXML-gt">
      <div2 n="2.2" type="section">
        <div3 n="2.2.1" type="subsection">
          <head>Sect. II. Subsect. I Dictionnaires. </head>
          <p> C'est un recueil de mots rangés dans un ordre convenu...</p>
        </div3>
        <div3 n="2.2.2" type="subsection">
          <head>Sect. II. Subsect. II. Qu'est-ce qu'un dictionnaire de langue ? .</head>
          <p>Un dictionnaire de langue est un dictionnaire donnant les mots d'une langue et leurs
          emplois...</p>
        </div3>
        <div3 n="2.2.3" type="subsection">
          <head>Sect. II. Subsect. III. Qu'est-ce qu'un dictionnaire encyclopédique ? </head>
          <p>Un dictionnaire encyclopédique est un dictionnaire qui contient des renseignements
          sur les choses, sur les idées </p>
        </div3>
      </div2>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div3-egXML-vd" source="#biblzh-tw_n51-55">
      <div2 n="3.2" type="section">
        <div3 n="3.2.1" type="member">
          <head>打破內在/外在、主觀/客觀的二元對立</head>
          <p>在二○年代的蘇聯文藝界，...</p>
        </div3>
        <div3 n="3.2.2" type="member">
          <head>交流：藝術話語與生活話語的共性</head>
          <p>林林總總的文理理論圍繞著作者、作品和讀者的關係問題，...</p>
        </div3>
        <div3 n="2.2.3" type="member">
          <head>言談和音調</head>
          <p>在這裡，巴赫汀為言談做了一個大膽的定義：...</p>
        </div3>
      </div2>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="div3-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any sequence of low-level structural elements, possibly grouped into lower
    subdivisions.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="div3-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas niveau,
    éventuellement groupés en subdivisions.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="div3-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 下位区分と成りうる一連の構造単位。 </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSDIV2"/>
  </listRef>
```

^b24

