---
type: representation
source-type: document
source: '[[00_sources/tei-p5-group-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 group
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/group.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# group

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5623. Git blob: `e1e377717ee33cdc181147895b6084c4a05bb382`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-group" ident="group">
  <gloss versionDate="2007-06-12" xml:lang="en">group</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">groupe</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Gruppierung</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the body of a composite text, grouping together a sequence of distinct texts (or
    groups of such texts) which are regarded as a unit for some purpose, for example the collected
    works of an author, a sequence of prose essays, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 목적의 단위로 간주되는 일련의 서로 다른 텍스트(또는 그러한 텍스트군)를 모아 놓은 혼합 텍스트의
    본문을 포함한다. 예를 들어, 한 작가의 선집, 일련의 수필 등.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含複合文本的正文，所匯集的一連串單一文件 (或文件群組)
    ，因為某特殊目的被視為一個整體，例如一個作者的作品集合、一連串的散文集等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ある単位として独立している個別テキストをまとめた複合テキストを示す。 例えば、ある著者の作品集やエッセイ集など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un ensemble de textes distincts (ou des groupes de textes de ce type), considérés comme formant une
    unité, par exemple pour présenter les œuvres complètes d’un auteur, une
    suite d’essais en prose, etc.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält den Textkörper eines aus mehreren Einzeltexten bestehenden Textes, (oder eine Reihe
    solcher Texte), die zusammen als Einheit gesehen werden, zum Beispiel die gesammelten Werke
    eines Autors, eine Reihe von Prosastücken, etc.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el cuerpo de un texto compuesto, es decir, que
    agrupa un conjunto de textos distintos (o grupos de textos) considerados como una unidad por
    criterios determinados, por ejemplo la obra completa de un autor, una serie de ensayos, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il corpo di un testo composito, che raggruppa
    cioè un insieme di testi distinti (o più insiemi di testi) considerati come unità per
    determinati scopi, per esempio l'opera completa di un autore, una serie di saggi, ecc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence>
        <alternate>
          <elementRef key="text"/>
          <elementRef key="group"/>
        </alternate>
        
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="text"/>
            <elementRef key="group"/>
            <classRef key="model.global"/>
          </alternate>
        
      </sequence>
      
        <classRef key="model.divBottom" minOccurs="0" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-group-egXML-dr" valid="feasible" source="#UND">
      <text>
        <!-- Section on Alexander Pope starts -->
        <front>
          <!-- biographical notice by editor -->
        </front>
        <group>
          <text>
            <!-- first poem -->
          </text>
          <text>
            <!-- second poem -->
          </text>
        </group>
      </text>
      <!-- end of Pope section-->
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-group-egXML-le" valid="feasible" source="#UND">
      <TEI>
        <teiHeader>
          <!--[ en-tête du texte composite ]-->
        </teiHeader>
        <text>
          <front>
            <!--[ partie préliminaire du texte composite  ]-->
          </front>
          <group>
            <text>
              <front>
                <!--[ partie préliminaire du premier texte ]-->
              </front>
              <body>
                <!--[ corps  du premier texte ]-->
              </body>
              <back>
                <!--[ annexe  du premier texte ]-->
              </back>
            </text>
            <text>
              <front>
                <!--[ partie préliminaire du deuxième texte ]-->
              </front>
              <body>
                <!--[ corps du deuxième texte ]-->
              </body>
              <back>
                <!--[ annexe du deuxième texte ]-->
              </back>
            </text>
            <!--[ encore de textes, simples ou composites  ]-->
          </group>
          <back>
            <!--[ annexe du texte composite  ]-->
          </back>
        </text>
      </TEI>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DS"/>
    <ptr target="#DSGRP"/>
    <ptr target="#CCDEF"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">groupe</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Gruppierung</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the body of a composite text, grouping together a sequence of distinct texts (or
    groups of such texts) which are regarded as a unit for some purpose, for example the collected
    works of an author, a sequence of prose essays, etc.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 목적의 단위로 간주되는 일련의 서로 다른 텍스트(또는 그러한 텍스트군)를 모아 놓은 혼합 텍스트의
    본문을 포함한다. 예를 들어, 한 작가의 선집, 일련의 수필 등.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含複合文本的正文，所匯集的一連串單一文件 (或文件群組)
    ，因為某特殊目的被視為一個整體，例如一個作者的作品集合、一連串的散文集等。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ある単位として独立している個別テキストをまとめた複合テキストを示す。 例えば、ある著者の作品集やエッセイ集など。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un ensemble de textes distincts (ou des groupes de textes de ce type), considérés comme formant une
    unité, par exemple pour présenter les œuvres complètes d’un auteur, une
    suite d’essais en prose, etc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält den Textkörper eines aus mehreren Einzeltexten bestehenden Textes, (oder eine Reihe
    solcher Texte), die zusammen als Einheit gesehen werden, zum Beispiel die gesammelten Werke
    eines Autors, eine Reihe von Prosastücken, etc.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el cuerpo de un texto compuesto, es decir, que
    agrupa un conjunto de textos distintos (o grupos de textos) considerados como una unidad por
    criterios determinados, por ejemplo la obra completa de un autor, una serie de ensayos, etc.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il corpo di un testo composito, che raggruppa
    cioè un insieme di testi distinti (o più insiemi di testi) considerati come unità per
    determinati scopi, per esempio l'opera completa di un autore, una serie di saggi, ecc.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence>
        <alternate>
          <elementRef key="text"/>
          <elementRef key="group"/>
        </alternate>
        
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="text"/>
            <elementRef key="group"/>
            <classRef key="model.global"/>
          </alternate>
        
      </sequence>
      
        <classRef key="model.divBottom" minOccurs="0" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-group-egXML-dr" valid="feasible" source="#UND">
      <text>
        <!-- Section on Alexander Pope starts -->
        <front>
          <!-- biographical notice by editor -->
        </front>
        <group>
          <text>
            <!-- first poem -->
          </text>
          <text>
            <!-- second poem -->
          </text>
        </group>
      </text>
      <!-- end of Pope section-->
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-group-egXML-le" valid="feasible" source="#UND">
      <TEI>
        <teiHeader>
          <!--[ en-tête du texte composite ]-->
        </teiHeader>
        <text>
          <front>
            <!--[ partie préliminaire du texte composite  ]-->
          </front>
          <group>
            <text>
              <front>
                <!--[ partie préliminaire du premier texte ]-->
              </front>
              <body>
                <!--[ corps  du premier texte ]-->
              </body>
              <back>
                <!--[ annexe  du premier texte ]-->
              </back>
            </text>
            <text>
              <front>
                <!--[ partie préliminaire du deuxième texte ]-->
              </front>
              <body>
                <!--[ corps du deuxième texte ]-->
              </body>
              <back>
                <!--[ annexe du deuxième texte ]-->
              </back>
            </text>
            <!--[ encore de textes, simples ou composites  ]-->
          </group>
          <back>
            <!--[ annexe du texte composite  ]-->
          </back>
        </text>
      </TEI>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DS"/>
    <ptr target="#DSGRP"/>
    <ptr target="#CCDEF"/>
  </listRef>
```

^b16

