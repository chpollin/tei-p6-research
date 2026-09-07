---
type: representation
source-type: document
source: '[[00_sources/tei-p5-figure-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 figure
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/figure.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# figure

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3807. Git blob: `936bbcacf9ddd147c26b7f231982f5c8ff91c28d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="figures" xml:id="gi-figure" ident="figure">
  <gloss versionDate="2007-06-12" xml:lang="en">figure</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">figure</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Abbildung</gloss>
  <desc versionDate="2011-11-05" xml:lang="en">groups elements representing or containing graphic information
  such as an illustration, formula,  or    figure.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">삽화 또는 그림과 같은 시각 정보를 표시하거나 포함하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">所標記的區塊包含圖示、插圖、或圖表。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">図表を示すまたは含む要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments représentant ou contenant une
    information graphique comme une illustration ou une figure.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica un bloque que contiene gráficos, ilustraciones o
    figuras.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una porzione di testo costituita da grafici,
    illustrazioni o figure.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">umfasst Elemente, die grafische Informationen repräsentieren oder beinhalten, wie z. B. eine
    Abbildung, Formel oder Diagramm.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.global"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.headLike"/>
        <classRef key="model.common"/>
        <elementRef key="figDesc"/>
        <classRef key="model.graphicLike"/>
        <classRef key="model.global"/>
        <classRef key="model.divBottom"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figure-egXML-xi">
      <figure>
        <head>The View from the Bridge</head>
        <figDesc>A Whistleresque view showing four or five sailing boats in the foreground, and a
          series of buoys strung out between them.</figDesc>
        <graphic url="http://www.example.org/fig1.png" scale="0.5"/>
      </figure>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figure-egXML-gm" source="#fr-ex-Ernaux-photo">
      <figure>
        <head>La tour rouge, de Giorgio De Chirico</head>
        <figDesc>Le tableau représente un donjon au pied duquel s'étend un espace quasiment vide,
            hormis quelques détails</figDesc>
        <graphic url="http://www.cineclubdecaen.com/cinepho/peint/dechericho/tourrouge.jpg" scale="0.5"/>
      </figure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figure-egXML-re">
      <figure>
        <head>圖一: 橋上的視野</head>
        <figDesc>前景有四五隻風帆，中間一堆救生圈串連。</figDesc>
        <graphic url="http://www.example.org/fig1.png" scale="0.5"/>
      </figure>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FTGRA" type="div1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">figure</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">figure</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Abbildung</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-05" xml:lang="en">groups elements representing or containing graphic information
  such as an illustration, formula,  or    figure.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">삽화 또는 그림과 같은 시각 정보를 표시하거나 포함하는 요소를 모아 놓는다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所標記的區塊包含圖示、插圖、或圖表。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">図表を示すまたは含む要素をまとめる。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments représentant ou contenant une
    information graphique comme une illustration ou une figure.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica un bloque que contiene gráficos, ilustraciones o
    figuras.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una porzione di testo costituita da grafici,
    illustrazioni o figure.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">umfasst Elemente, die grafische Informationen repräsentieren oder beinhalten, wie z. B. eine
    Abbildung, Formel oder Diagramm.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.global"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.headLike"/>
        <classRef key="model.common"/>
        <elementRef key="figDesc"/>
        <classRef key="model.graphicLike"/>
        <classRef key="model.global"/>
        <classRef key="model.divBottom"/>
      </alternate>
    
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figure-egXML-xi">
      <figure>
        <head>The View from the Bridge</head>
        <figDesc>A Whistleresque view showing four or five sailing boats in the foreground, and a
          series of buoys strung out between them.</figDesc>
        <graphic url="http://www.example.org/fig1.png" scale="0.5"/>
      </figure>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figure-egXML-gm" source="#fr-ex-Ernaux-photo">
      <figure>
        <head>La tour rouge, de Giorgio De Chirico</head>
        <figDesc>Le tableau représente un donjon au pied duquel s'étend un espace quasiment vide,
            hormis quelques détails</figDesc>
        <graphic url="http://www.cineclubdecaen.com/cinepho/peint/dechericho/tourrouge.jpg" scale="0.5"/>
      </figure>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figure-egXML-re">
      <figure>
        <head>圖一: 橋上的視野</head>
        <figDesc>前景有四五隻風帆，中間一堆救生圈串連。</figDesc>
        <graphic url="http://www.example.org/fig1.png" scale="0.5"/>
      </figure>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FTGRA" type="div1"/>
  </listRef>
```

^b17

