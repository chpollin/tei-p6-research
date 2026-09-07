---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.xtruthvalue-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.xTruthValue
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.xTruthValue.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.xTruthValue

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2689. Git blob: `dfc844fa4e878627e9e596bd21cb90d8a17f0db4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.xTruthValue">
  <gloss versionDate="2007-07-04" xml:lang="en">extended truth value</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">확장 진리값</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2024-09-02" xml:lang="ja">拡張真理値</gloss>
  <desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values used to express a truth value which may be unknown.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">알려지지 않을 수 있는 진리값을 표현하는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍表示一個可能未知的真實值</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">不明の場合もある真偽値をとる属性値の範囲を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant une vérité potentiellement inconnue.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos usados para
    expresar un valor cierto potencialmente desconocido.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per
    esprimere un valore di verità potenzialmente sconosciuto</desc>
  <content>
      <alternate>
         <dataRef name="boolean"/>
         <valList>
            <valItem ident="unknown"/>
            <valItem ident="inapplicable"/>
         </valList>
      </alternate>
   </content>
  <remarks ident="teidata.xTruthValue-remarks" versionDate="2010-10-29" xml:lang="en">
      <p>In cases where where uncertainty is inappropriate, use the
    datatype <ident type="datatype">teidata.TruthValue</ident>.</p>
  </remarks>
  <remarks ident="teidata.xTruthValue-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p> 不確実性を持つべきではない場合は、データ型<ident type="datatype">teidata.TruthValue</ident>を使用する。 </p>
  </remarks>
  <remarks ident="teidata.xTruthValue-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Dans le cas où l'incertitude n’est pas adaptée, employer plutot
    le type de données <ident>teidata.TruthValue</ident>.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">extended truth value</gloss>
```

^b1

### Block 2

XML location: `/dataSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">확장 진리값</gloss>
```

^b2

### Block 3

XML location: `/dataSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/dataSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2024-09-02" xml:lang="ja">拡張真理値</gloss>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values used to express a truth value which may be unknown.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">알려지지 않을 수 있는 진리값을 표현하는 속성 값 범위를 정의한다.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍表示一個可能未知的真實值</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">不明の場合もある真偽値をとる属性値の範囲を定義する。</desc>
```

^b8

### Block 9

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant une vérité potentiellement inconnue.</desc>
```

^b9

### Block 10

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos usados para
    expresar un valor cierto potencialmente desconocido.</desc>
```

^b10

### Block 11

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per
    esprimere un valore di verità potenzialmente sconosciuto</desc>
```

^b11

### Block 12

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <alternate>
         <dataRef name="boolean"/>
         <valList>
            <valItem ident="unknown"/>
            <valItem ident="inapplicable"/>
         </valList>
      </alternate>
   </content>
```

^b12

### Block 13

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.xTruthValue-remarks" versionDate="2010-10-29" xml:lang="en">
      <p>In cases where where uncertainty is inappropriate, use the
    datatype <ident type="datatype">teidata.TruthValue</ident>.</p>
  </remarks>
```

^b13

### Block 14

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.xTruthValue-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p> 不確実性を持つべきではない場合は、データ型<ident type="datatype">teidata.TruthValue</ident>を使用する。 </p>
  </remarks>
```

^b14

### Block 15

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.xTruthValue-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Dans le cas où l'incertitude n’est pas adaptée, employer plutot
    le type de données <ident>teidata.TruthValue</ident>.</p>
  </remarks>
```

^b15

