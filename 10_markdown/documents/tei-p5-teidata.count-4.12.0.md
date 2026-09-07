---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.count-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.count
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.count.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.count

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2020. Git blob: `f52255492ba5ceefb586fb5180d4ff77b22397de`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.count">
  <desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values used for a non-negative
integer value used as a count.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">계산으로 사용된 음이 아닌 정수 값의 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍，用於作為總數的非負整數值</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">非負整数値を採る属性値の範囲を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs des attributs exprimant une valeur entière et non négative  utilisé pour des calculs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos para números enteros no negativos usados como un cálculo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per un numero intero non negativo impiegato come computo.</desc>
  <content>
      <dataRef name="nonNegativeInteger"/>
   </content>
  <remarks ident="teidata.count-remarks" versionDate="2016-12-01" xml:lang="en">
      <p>Any positive integer value or zero is permitted</p>
  </remarks>
  <remarks ident="teidata.count-remarks" versionDate="2024-08-08" xml:lang="ja">
      <p>正の整数値（ゼロを含む）のみが許可される。</p>
  </remarks>
  <remarks ident="teidata.count-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Seules des valeurs positives entières sont autorisées.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values used for a non-negative
integer value used as a count.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">계산으로 사용된 음이 아닌 정수 값의 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍，用於作為總數的非負整數值</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">非負整数値を採る属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs des attributs exprimant une valeur entière et non négative  utilisé pour des calculs.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos para números enteros no negativos usados como un cálculo.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per un numero intero non negativo impiegato come computo.</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="nonNegativeInteger"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.count-remarks" versionDate="2016-12-01" xml:lang="en">
      <p>Any positive integer value or zero is permitted</p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.count-remarks" versionDate="2024-08-08" xml:lang="ja">
      <p>正の整数値（ゼロを含む）のみが許可される。</p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.count-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Seules des valeurs positives entières sont autorisées.</p>
  </remarks>
```

^b11

