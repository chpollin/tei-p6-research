---
type: representation
source-type: document
source: '[[00_sources/tei-p5-measuregrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 measureGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/measureGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# measureGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7501. Git blob: `b4ecabfbb75d95f5842907537b76a51d01ed2d8b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-measureGrp" ident="measureGrp">
  <gloss versionDate="2007-07-04" xml:lang="en">measure group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">측정 그룹</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">grupo de medida</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">groupe de mesures</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">gruppo di misure</gloss>
  <desc versionDate="2007-10-18" xml:lang="en">contains a group of dimensional specifications which relate to the same object, for example
    the height and width of a manuscript page.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 원고지 페이지의 가로 세로 크기와 같이 동일 개체에 관련된 여러 종류의 측량값의 그룹을
    포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene un grupo de especificaciones dimensionales que
    se relacionan con un mismo objeto, por ejemplo la altura y la anchura de una página de
    manuscrito.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">大きさに関する規格を示す。例えば、手書き資料のページの高さや幅などを 示すためのもの。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un groupe de spécifications des dimensions qui
    concernent un même objet, par exemple la hauteur et la largeur d'une page d'un manuscrit.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene un gruppo di indicazioni dimensionali relative
    allo stesso oggetto, per esempio altezza e larghezza di una pagina di manoscritto</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.measurement"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.measureLike"/>
      </alternate>
    
  </content>
  <!--  <attList>
    <attDef ident="type">
    <gloss/>
    <desc>indicates which aspect of the object is being measured.</desc>
    <desc versionDate="2007-01-21" xml:lang="it">indica quale aspetto dell'oggetto viene misurato.</desc>
    <desc versionDate="2006-10-28" xml:lang="ja">当該計測対象の種類を示す．</desc>
    <datatype>
    <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0" name="data.enumerated"/>
    </datatype>
    <valList type="open">
    <valItem ident="leaves">
    <gloss>dimensions relate to one or more leaves (e.g. a single leaf, a
    gathering, or a separately bound part)</gloss>
    <gloss versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono a uno o più fogli (per esempio un foglio, una raccolta, o una parte rilegata separatamente)</gloss>
    </valItem>
    <valItem ident="ruled">
    <gloss>dimensions relate to the area of a leaf which has been ruled in
    preparation for writing.</gloss>
    <gloss versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla porzione di un foglio sulla quale sono state disegnate delle righe al fine di scriverci</gloss>
    </valItem>
    <valItem ident="pricked">
    <gloss>dimensions relate to the area of a leaf which has been pricked
    out in preparation for ruling (used where this differs significantly
    from the ruled area, or where the ruling is not measurable).</gloss>
    <gloss versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla porzione di un foglio sulla quale è stata indicata la posizione dei fori da praticare al fine di imprimervi delle righe (si usa quando la porzione da rigare è molto diversa da quella già rigata o quando la rigatura non è misurabile)</gloss>
    </valItem>
    <valItem ident="written">
    <gloss>dimensions relate to the area of a leaf which has been written,
    with the height measured from the top of the minims on the top line of
    writing, to the bottom of the minims on the bottom line of writing.</gloss>
    <gloss versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono ad un'area del foglio su cui è stato scritto e la cui altezza è misurata dalla cima degli uncini sulla prima riga scritta fino al fondo degli uncini sull'ultima riga scritta</gloss>
    </valItem>
    <valItem ident="miniatures">
    <gloss>dimensions relate to the miniatures within the manuscript</gloss>
    <gloss versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alle miniature contenute nel manoscritto</gloss>
    </valItem>
    <valItem ident="binding">
    <gloss>dimensions relate to the binding in which the codex or manuscript is contained</gloss>
    <gloss versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla rilegatura nella quale è contenuto il codice o manoscritto</gloss>
    </valItem>
    <valItem ident="box">
    <gloss>dimensions relate to the box or other container in which  the
    manuscript is stored.</gloss>
    <gloss versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla scatola o ad altro contenitore nel quale è custodito il manoscritto</gloss>
    </valItem>
    </valList>
    </attDef>
    </attList>-->
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-measureGrp-egXML-lx">
      <measureGrp type="leaves" unit="mm">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </measureGrp>
      <measureGrp type="ruledArea" unit="mm">
        <height scope="most" quantity="90"/>
        <width scope="most" quantity="48"/>
      </measureGrp>
      <measureGrp type="box" unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
        <depth quantity="6"/>
      </measureGrp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-measureGrp-egXML-em">
      <measureGrp type="leaves" unit="mm">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </measureGrp>
      <measureGrp type="ruledArea" unit="mm">
        <height scope="most" quantity="90"/>
        <width scope="most" quantity="48"/>
      </measureGrp>
      <measureGrp type="box" unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
        <depth quantity="6"/>
      </measureGrp>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-measureGrp-egXML-eb">
      <measureGrp type="頁面" unit="mm">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </measureGrp>
      <measureGrp type="直行或橫隔部份" unit="mm">
        <height scope="most" quantity="90"/>
        <width scope="most" quantity="48"/>
      </measureGrp>
      <measureGrp type="盒" unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
        <depth quantity="6"/>
      </measureGrp>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msdim"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">measure group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">측정 그룹</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">grupo de medida</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">groupe de mesures</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">gruppo di misure</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">contains a group of dimensional specifications which relate to the same object, for example
    the height and width of a manuscript page.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 원고지 페이지의 가로 세로 크기와 같이 동일 개체에 관련된 여러 종류의 측량값의 그룹을
    포함한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene un grupo de especificaciones dimensionales que
    se relacionan con un mismo objeto, por ejemplo la altura y la anchura de una página de
    manuscrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">大きさに関する規格を示す。例えば、手書き資料のページの高さや幅などを 示すためのもの。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient un groupe de spécifications des dimensions qui
    concernent un même objet, par exemple la hauteur et la largeur d'une page d'un manuscrit.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene un gruppo di indicazioni dimensionali relative
    allo stesso oggetto, per esempio altezza e larghezza di una pagina di manoscritto</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.measurement"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.measureLike"/>
      </alternate>
    
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-measureGrp-egXML-lx">
      <measureGrp type="leaves" unit="mm">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </measureGrp>
      <measureGrp type="ruledArea" unit="mm">
        <height scope="most" quantity="90"/>
        <width scope="most" quantity="48"/>
      </measureGrp>
      <measureGrp type="box" unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
        <depth quantity="6"/>
      </measureGrp>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-measureGrp-egXML-em">
      <measureGrp type="leaves" unit="mm">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </measureGrp>
      <measureGrp type="ruledArea" unit="mm">
        <height scope="most" quantity="90"/>
        <width scope="most" quantity="48"/>
      </measureGrp>
      <measureGrp type="box" unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
        <depth quantity="6"/>
      </measureGrp>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-measureGrp-egXML-eb">
      <measureGrp type="頁面" unit="mm">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </measureGrp>
      <measureGrp type="直行或橫隔部份" unit="mm">
        <height scope="most" quantity="90"/>
        <width scope="most" quantity="48"/>
      </measureGrp>
      <measureGrp type="盒" unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
        <depth quantity="6"/>
      </measureGrp>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msdim"/>
  </listRef>
```

^b17

