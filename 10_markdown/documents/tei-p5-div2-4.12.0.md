---
type: representation
source-type: document
source: '[[00_sources/tei-p5-div2-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 div2
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/div2.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# div2

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8577. Git blob: `cff1f69c647228035355e1bab95dd4ee4f9a7091`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-div2" ident="div2">
  <gloss versionDate="2005-01-14" xml:lang="en">level-2 text division</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">2 층위 텍스트 구역</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次二</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">division du texte de niveau 2</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de"> Textgliederungsebene -2</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">división textual de segundo nivel</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 2</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a second-level subdivision of the front, body, or back of a
  text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의 두 번째 층위 하위 구역을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的第二層分段。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の第2位のテキスト部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une subdivision de deuxième niveau dans
  le texte prélimaire, dans le corps d’un texte ou dans le texte postliminaire.</desc>
  <desc versionDate="2006-10-18" xml:lang="de"> enthält die zweite Gliederungsebene von Vorspann (front), Kerntext oder Nachspann (back) eines Textes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una subdivisión del segundo nivel en el paratexto inicial, en el cuerpo del texto o en el paratexto final.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una sezione di secondo livello del peritesto iniziale, del corpo del testo, o del peritesto finale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.divLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.div2Like"/>
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
              <classRef key="model.div3Like"/>
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
                <classRef key="model.div3Like"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div2-egXML-jo" source="#COXR-eg-164">
      <div1 n="2" type="part">
        <head>The Second Partition:
        The Cure of Melancholy</head>
        <div2 n="2.1" type="section">
          <div3 n="2.1.1" type="member">
            <div4 n="2.1.1.1" type="subsection">
              <head>Unlawful Cures rejected.</head>
              <p>Inveterate melancholy, howsoever it may seem to
              be a continuate, inexorable disease, hard to be
              cured, accompanying them to their graves most part
              (as <ref target="#a">Montanus</ref> observes), yet many
              times it may be helped... 
              </p>
            </div4>
          </div3>
        </div2>
        <div2 n="2.2" type="section">
          <div3 n="2.2.1" type="member">
            <head>Sect. II. Memb. I</head>
            <p>
            </p>
          </div3>
        </div2>
        <div2 n="2.3" type="section">
          <div3 n="2.3.1" type="member">
            <head>Sect. III. Memb. I</head>
            <p>
            </p>
          </div3>
        </div2>
      </div1>
    </egXML>
    <!-- Burton, Anatomy of Melancholy, 16th ed (1651), Blake, 1836 -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div2-egXML-ff">
      <div1 n="II" type="chapitre">
        <head>Chapitre II. Traitement électronique des données en histoire de la littérature
        française : bilan provisoire</head>
        <div2 n="2.1" type="section">
          <div3 n="2.1.1" type="subsection">
            <div4 n="2.1.1.1" type="article">
              <head>Les objectifs</head>
              <p>Chaque étudiant est convié à parcourir la banque à partir des différentes entrées
              liées au cours magistral qu'il suit en amphithéâtre...</p>
            </div4>
          </div3>
        </div2>
        <div2 n="2.2" type="section">
          <div3 n="2.2.1" type="subsection">
            <head>Sect. II. Subsection I. Exploitation pédagogique de la BDHL</head>
            <p>Pour la plupart des étudiants en Lettres des générations précédentes, un
            enseignement de l'histoire de la littérature allait de soi... </p>
          </div3>
        </div2>
        <div2 n="2.3" type="section">
          <div3 n="2.3.1" type="subsection">
            <head>Sect. III. Subsection I. Etudes permises par la BDHL</head>
            <p>L'existence d'une banque de données, quelle qu'elle soit, permet d'envisager des
            traitements statistiques. </p>
          </div3>
        </div2>
      </div1>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div2-egXML-bo" source="#biblzh-tw_n51-55">
      <div1 n="3" type="part">
        <head>第三章：對話性—文化理論的基石</head>
        <div2 n="3.1" type="section">
          <div3 n="3.1.1" type="member">
            <div4 n="3.1.1.1" type="subsection">
              <head>歷史、社會與佛洛伊德主義</head>
              <p>《述評》開宗明義，運用歷史唯物主義的觀點，批判佛洛伊德主義的反歷史和反社會傾向。巴赫汀指出... </p>
            </div4>
          </div3>
        </div2>
        <div2 n="3.2" type="section">
          <div3 n="3.2.1" type="member">
            <head>打破內在/外在、主觀/客觀的二元對立</head>
            <p>在二○年代的蘇聯文藝界，...</p>
          </div3>
        </div2>
        <div2 n="3.3" type="section">
          <div3 n="3.3.1" type="member">
            <head>建立馬克思主義和社會學詩學</head>
            <p>《社會學詩學》是巴赫汀對話美學的一個目標，...</p>
          </div3>
        </div2>
      </div1>
    </egXML>
  </exemplum>
  <remarks ident="div2-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any sequence of low-level structural elements, possibly grouped
    into lower subdivisions.</p>
  </remarks>
  <remarks ident="div2-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas
    niveau, éventuellement groupés en subdivisions.</p>
  </remarks>
  <remarks ident="div2-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
      下位区分と成りうる一連の構造単位。
    </p>
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
<gloss versionDate="2005-01-14" xml:lang="en">level-2 text division</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">2 층위 텍스트 구역</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">區段層次二</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">division du texte de niveau 2</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de"> Textgliederungsebene -2</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">división textual de segundo nivel</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">partizione testuale di livello 2</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a second-level subdivision of the front, body, or back of a
  text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 전면부, 본문 또는 후면부의 두 번째 층위 하위 구역을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">文本的正文前資訊、正文及正文後資訊的第二層分段。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">前付、本文、後付中の第2位のテキスト部分を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une subdivision de deuxième niveau dans
  le texte prélimaire, dans le corps d’un texte ou dans le texte postliminaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de"> enthält die zweite Gliederungsebene von Vorspann (front), Kerntext oder Nachspann (back) eines Textes.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una subdivisión del segundo nivel en el paratexto inicial, en el cuerpo del texto o en el paratexto final.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una sezione di secondo livello del peritesto iniziale, del corpo del testo, o del peritesto finale.</desc>
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
    <memberOf key="model.div2Like"/>
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
              <classRef key="model.div3Like"/>
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
                <classRef key="model.div3Like"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div2-egXML-jo" source="#COXR-eg-164">
      <div1 n="2" type="part">
        <head>The Second Partition:
        The Cure of Melancholy</head>
        <div2 n="2.1" type="section">
          <div3 n="2.1.1" type="member">
            <div4 n="2.1.1.1" type="subsection">
              <head>Unlawful Cures rejected.</head>
              <p>Inveterate melancholy, howsoever it may seem to
              be a continuate, inexorable disease, hard to be
              cured, accompanying them to their graves most part
              (as <ref target="#a">Montanus</ref> observes), yet many
              times it may be helped... 
              </p>
            </div4>
          </div3>
        </div2>
        <div2 n="2.2" type="section">
          <div3 n="2.2.1" type="member">
            <head>Sect. II. Memb. I</head>
            <p>
            </p>
          </div3>
        </div2>
        <div2 n="2.3" type="section">
          <div3 n="2.3.1" type="member">
            <head>Sect. III. Memb. I</head>
            <p>
            </p>
          </div3>
        </div2>
      </div1>
    </egXML>
    <!-- Burton, Anatomy of Melancholy, 16th ed (1651), Blake, 1836 -->
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div2-egXML-ff">
      <div1 n="II" type="chapitre">
        <head>Chapitre II. Traitement électronique des données en histoire de la littérature
        française : bilan provisoire</head>
        <div2 n="2.1" type="section">
          <div3 n="2.1.1" type="subsection">
            <div4 n="2.1.1.1" type="article">
              <head>Les objectifs</head>
              <p>Chaque étudiant est convié à parcourir la banque à partir des différentes entrées
              liées au cours magistral qu'il suit en amphithéâtre...</p>
            </div4>
          </div3>
        </div2>
        <div2 n="2.2" type="section">
          <div3 n="2.2.1" type="subsection">
            <head>Sect. II. Subsection I. Exploitation pédagogique de la BDHL</head>
            <p>Pour la plupart des étudiants en Lettres des générations précédentes, un
            enseignement de l'histoire de la littérature allait de soi... </p>
          </div3>
        </div2>
        <div2 n="2.3" type="section">
          <div3 n="2.3.1" type="subsection">
            <head>Sect. III. Subsection I. Etudes permises par la BDHL</head>
            <p>L'existence d'une banque de données, quelle qu'elle soit, permet d'envisager des
            traitements statistiques. </p>
          </div3>
        </div2>
      </div1>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-div2-egXML-bo" source="#biblzh-tw_n51-55">
      <div1 n="3" type="part">
        <head>第三章：對話性—文化理論的基石</head>
        <div2 n="3.1" type="section">
          <div3 n="3.1.1" type="member">
            <div4 n="3.1.1.1" type="subsection">
              <head>歷史、社會與佛洛伊德主義</head>
              <p>《述評》開宗明義，運用歷史唯物主義的觀點，批判佛洛伊德主義的反歷史和反社會傾向。巴赫汀指出... </p>
            </div4>
          </div3>
        </div2>
        <div2 n="3.2" type="section">
          <div3 n="3.2.1" type="member">
            <head>打破內在/外在、主觀/客觀的二元對立</head>
            <p>在二○年代的蘇聯文藝界，...</p>
          </div3>
        </div2>
        <div2 n="3.3" type="section">
          <div3 n="3.3.1" type="member">
            <head>建立馬克思主義和社會學詩學</head>
            <p>《社會學詩學》是巴赫汀對話美學的一個目標，...</p>
          </div3>
        </div2>
      </div1>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="div2-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any sequence of low-level structural elements, possibly grouped
    into lower subdivisions.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="div2-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dateDesc">Cet élément contient une séquence d'éléments structurels de bas
    niveau, éventuellement groupés en subdivisions.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="div2-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
      下位区分と成りうる一連の構造単位。
    </p>
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

