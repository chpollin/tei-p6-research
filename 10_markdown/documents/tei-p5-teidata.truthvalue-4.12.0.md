---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.truthvalue-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.truthValue
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.truthValue.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.truthValue

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2966. Git blob: `0f9bda77b9691ecf0912bea9540aecedc4e2578d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.truthValue">
  <desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values used to express a truth
value.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">진리값을 표현하는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍表示一個可能未知的真實值</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">真偽値を示す属性値の範囲を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant la vérité d'une proposition.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos usados para expresar un valor cierto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per esprimere un valore di verità.</desc>
  <content>
      <dataRef name="boolean"/>
   </content>
  <remarks ident="teidata.truthValue-remarks" versionDate="2013-11-01" xml:lang="en">
      <p>The possible values of this datatype are <val>1</val> or
    <val>true</val>, or <val>0</val> or <val>false</val>.</p>
      <p>This datatype applies only for cases where uncertainty is
    inappropriate; if the attribute concerned may have a value other
    than true or false, e.g. <val>unknown</val>, or
    <val>inapplicable</val>, it should have the extended version of
    this datatype: <ident type="datatype">teidata.xTruthValue</ident>.</p>
  </remarks>
  <remarks ident="teidata.truthValue-remarks" xml:lang="ja" versionDate="2024-09-02">
      <p>
        このデータ型が取り得る値は、<val>1</val>または<val>true</val>または<val>0</val>または<val>false</val>である。曖昧な値が許されない場合に使われるデータ型である。属性値が真偽値でない場合、例えば<val>unknown</val>や<val>inapplicable</val>の場合には、当該データ型の拡張版である<ident type="datatype">data.xTruthValue</ident>を使うべきである。
    </p>
  </remarks>
  <remarks ident="teidata.truthValue-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Ce type de données ne s'applique que dans les cas où l'incertitude est 
      inappropriée ; c’est-à-dire si l'attribut concerné peut avoir une valeur autre 
      que vrai ou faux, par ex. <val>inconnu</val>, ou <val>inapplicable</val>, il devrait  alors y
      avoir la version étendue de ce  type de données : teidata.xTruthValue.
    </p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values used to express a truth
value.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">진리값을 표현하는 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍表示一個可能未知的真實值</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">真偽値を示す属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant la vérité d'une proposition.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos usados para expresar un valor cierto.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per esprimere un valore di verità.</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="boolean"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.truthValue-remarks" versionDate="2013-11-01" xml:lang="en">
      <p>The possible values of this datatype are <val>1</val> or
    <val>true</val>, or <val>0</val> or <val>false</val>.</p>
      <p>This datatype applies only for cases where uncertainty is
    inappropriate; if the attribute concerned may have a value other
    than true or false, e.g. <val>unknown</val>, or
    <val>inapplicable</val>, it should have the extended version of
    this datatype: <ident type="datatype">teidata.xTruthValue</ident>.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.truthValue-remarks" xml:lang="ja" versionDate="2024-09-02">
      <p>
        このデータ型が取り得る値は、<val>1</val>または<val>true</val>または<val>0</val>または<val>false</val>である。曖昧な値が許されない場合に使われるデータ型である。属性値が真偽値でない場合、例えば<val>unknown</val>や<val>inapplicable</val>の場合には、当該データ型の拡張版である<ident type="datatype">data.xTruthValue</ident>を使うべきである。
    </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.truthValue-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Ce type de données ne s'applique que dans les cas où l'incertitude est 
      inappropriée ; c’est-à-dire si l'attribut concerné peut avoir une valeur autre 
      que vrai ou faux, par ex. <val>inconnu</val>, ou <val>inapplicable</val>, il devrait  alors y
      avoir la version étendue de ce  type de données : teidata.xTruthValue.
    </p>
  </remarks>
```

^b11

