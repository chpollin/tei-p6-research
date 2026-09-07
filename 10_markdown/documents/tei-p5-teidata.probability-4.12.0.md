---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.probability-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.probability
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.probability.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.probability

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2346. Git blob: `979bb3d6eb9467cec09fb6255211130066f9ecda`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.probability">
  <desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values expressing a probability.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">확률을 표현하는 속성 값의 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義表示可能性的屬性值範圍</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">出現度を示す属性値の範囲を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs exprimant une
    probabilité.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que exprimen un
    grado de probabilidad.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi che esprimono
    una probabilità</desc>
  <content>
    <dataRef name="double">
      <dataFacet name="minInclusive" value="0"/>
      <dataFacet name="maxInclusive" value="1"/>
    </dataRef>
  </content>
  <remarks ident="teidata.probability-remarks" versionDate="2005-10-18" xml:lang="en">
      <p>Probability is expressed
       as a real number between 0 and 1;  0  representing <mentioned>certainly false</mentioned> and 1 representing <mentioned>certainly
        true</mentioned>.</p>
  </remarks>
  <remarks ident="teidata.probability-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p>出現度は、0から1までの実数で表現される。0は <mentioned>確実に偽</mentioned>、1は、 <mentioned>確実に真</mentioned>を示す。 </p>
  </remarks>
  <remarks ident="teidata.probability-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Le degré de probabilité est exprimé
       par un nombre réel entre 0 et 1 ;
     0       représentant <mentioned>certainement faux</mentioned> et 1 <mentioned>certainement
        vrai</mentioned>.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values expressing a probability.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">확률을 표현하는 속성 값의 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義表示可能性的屬性值範圍</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">出現度を示す属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs exprimant une
    probabilité.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que exprimen un
    grado de probabilidad.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi che esprimono
    una probabilità</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <dataRef name="double">
      <dataFacet name="minInclusive" value="0"/>
      <dataFacet name="maxInclusive" value="1"/>
    </dataRef>
  </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.probability-remarks" versionDate="2005-10-18" xml:lang="en">
      <p>Probability is expressed
       as a real number between 0 and 1;  0  representing <mentioned>certainly false</mentioned> and 1 representing <mentioned>certainly
        true</mentioned>.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.probability-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p>出現度は、0から1までの実数で表現される。0は <mentioned>確実に偽</mentioned>、1は、 <mentioned>確実に真</mentioned>を示す。 </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.probability-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Le degré de probabilité est exprimé
       par un nombre réel entre 0 et 1 ;
     0       représentant <mentioned>certainement faux</mentioned> et 1 <mentioned>certainement
        vrai</mentioned>.</p>
  </remarks>
```

^b11

