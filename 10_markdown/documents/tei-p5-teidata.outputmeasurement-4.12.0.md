---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.outputmeasurement-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.outputMeasurement
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.outputMeasurement.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.outputMeasurement

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3888. Git blob: `3cd29096e91f6510464c9cd7ba7a443f1bb544c4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="data-outputMeasurement" ident="teidata.outputMeasurement">
  <desc versionDate="2013-03-26" xml:lang="en">defines a range of values for use in specifying the size of an object that is intended for
    display.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">웹에서 디스플레이 목적의 대상 크기를 명시하는 값의 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍說明預定呈現在網路上之物件大小</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">表示を意図するオブジェクトの寸法を指定するための値の範囲を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme de valeurs exprimant
    les dimensions d'un objet destiné à être affiché.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una gama de valores para emplearlos en la
    especificación de las dimensiones de un objeto que se ha de incluir in la red.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce una gamma di valori da impiegare nello
    specificare le dimensioni di un oggetto da inserire in rete</desc>
  <content>
      <dataRef name="token" restriction="[\-+]?\d+(\.\d+)?(%|cm|mm|in|pt|pc|px|em|ex|ch|rem|vw|vh|vmin|vmax)"/>
   </content>
  <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-outputMeasurement-egXML-fv">
         <figure>
            <head>The TEI Logo</head>
            <figDesc>Stylized yellow angle brackets with the letters <mentioned>TEI</mentioned> in
          between and <mentioned>text encoding initiative</mentioned> underneath, all on a white
          background.</figDesc>
            <graphic height="600px" width="600px" url="http://www.tei-c.org/logos/TEI-600.jpg"/>
         </figure>
      </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-outputMeasurement-egXML-sq">
         <figure>
            <head>Le logo TEI</head>
            <graphic height="600px" width="600px" url="http://www.tei-c.org/logos/TEI-600.jpg"/>
         </figure>
      </egXML>
  </exemplum>
  <remarks ident="teidata.outputMeasurement-remarks" versionDate="2022-09-27" xml:lang="en">
      <p> These values map directly onto the values used by XSL-FO and CSS. For definitions of the
      units see those specifications; at the time of this writing the most complete list is in the
        <ref target="https://www.w3.org/TR/css-values-3/">CSS3 working draft</ref>.</p>
  </remarks>
  <remarks ident="teidata.outputMeasurement-remarks" versionDate="2022-09-27" xml:lang="ja">
      <p> 当該値は、XSLFOやCSSで使用される値になる。詳細は各規格を参照のこと。 現時点で一番詳細なリストは、 <ref target="https://www.w3.org/TR/css-values-3/"> CSS3 working
      draft</ref>になる。 </p>
  </remarks>
  <remarks ident="teidata.outputMeasurement-remarks" versionDate="2022-09-27" xml:lang="fr">
      <p> Ces valeurs peuvent être reportées directement sur des valeurs utilisées par XSL-FO et CSS. Pour les
      définitions des unités, voir ces spécifications ; à ce jour la
      liste la plus complète est dans un
        <ref target="https://www.w3.org/TR/css-values-3/">CSS3 working draft</ref>.</p>
  </remarks>
  <!-- correct practice would be to add this item to the TEI
bibliography and link to that (LB 2013-03-13) -->
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-03-26" xml:lang="en">defines a range of values for use in specifying the size of an object that is intended for
    display.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">웹에서 디스플레이 목적의 대상 크기를 명시하는 값의 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍說明預定呈現在網路上之物件大小</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">表示を意図するオブジェクトの寸法を指定するための値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme de valeurs exprimant
    les dimensions d'un objet destiné à être affiché.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una gama de valores para emplearlos en la
    especificación de las dimensiones de un objeto que se ha de incluir in la red.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce una gamma di valori da impiegare nello
    specificare le dimensioni di un oggetto da inserire in rete</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="token" restriction="[\-+]?\d+(\.\d+)?(%|cm|mm|in|pt|pc|px|em|ex|ch|rem|vw|vh|vmin|vmax)"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-outputMeasurement-egXML-fv">
         <figure>
            <head>The TEI Logo</head>
            <figDesc>Stylized yellow angle brackets with the letters <mentioned>TEI</mentioned> in
          between and <mentioned>text encoding initiative</mentioned> underneath, all on a white
          background.</figDesc>
            <graphic height="600px" width="600px" url="http://www.tei-c.org/logos/TEI-600.jpg"/>
         </figure>
      </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/dataSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-outputMeasurement-egXML-sq">
         <figure>
            <head>Le logo TEI</head>
            <graphic height="600px" width="600px" url="http://www.tei-c.org/logos/TEI-600.jpg"/>
         </figure>
      </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.outputMeasurement-remarks" versionDate="2022-09-27" xml:lang="en">
      <p> These values map directly onto the values used by XSL-FO and CSS. For definitions of the
      units see those specifications; at the time of this writing the most complete list is in the
        <ref target="https://www.w3.org/TR/css-values-3/">CSS3 working draft</ref>.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.outputMeasurement-remarks" versionDate="2022-09-27" xml:lang="ja">
      <p> 当該値は、XSLFOやCSSで使用される値になる。詳細は各規格を参照のこと。 現時点で一番詳細なリストは、 <ref target="https://www.w3.org/TR/css-values-3/"> CSS3 working
      draft</ref>になる。 </p>
  </remarks>
```

^b12

### Block 13

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.outputMeasurement-remarks" versionDate="2022-09-27" xml:lang="fr">
      <p> Ces valeurs peuvent être reportées directement sur des valeurs utilisées par XSL-FO et CSS. Pour les
      définitions des unités, voir ces spécifications ; à ce jour la
      liste la plus complète est dans un
        <ref target="https://www.w3.org/TR/css-values-3/">CSS3 working draft</ref>.</p>
  </remarks>
```

^b13

