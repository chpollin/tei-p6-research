---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.enumerated-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.enumerated
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.enumerated.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.enumerated

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3444. Git blob: `386877895719aca5a05f5ad272455e0365c6fb21`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.enumerated">
  <desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values expressed as a single XML name taken from a list of
    documented possibilities.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">기록된 확률의 목록으로부터 얻어진 단일 XML 이름으로 표현된 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以單字或代號呈現，該單字或代號出自於一份紀錄所有可能性的列表</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">定められた選択肢の一覧から選ばれる単一のXML名前を値域とする属性値を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme de
  valeurs des attributs exprimant un nom XML
    extrait d'une liste de possibilités documentées.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos expresados como
    una única palabra o señal tomada de una lista de posibilidades documentadas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi espressi come
    singola parola o token tratto da una lista di possibilità attestate</desc>
  <content>
      <dataRef key="teidata.word"/>
   </content>
  <remarks ident="teidata.enumerated-remarks" versionDate="2016-12-01" xml:lang="en">
    <p>Attributes using this datatype must contain a single
      <soCalled>word</soCalled> which contains only letters, digits,
      punctuation characters, or symbols: thus it cannot include
      whitespace.</p>
      <p>Typically, the list of documented possibilities will be provided (or exemplified) by a value
      list in the associated attribute specification, expressed with a <gi>valList</gi> element.</p>
  </remarks>
  <remarks ident="teidata.enumerated-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>このデータ型を使用する属性は、このデータ型のために定義されたパターンと一致する単一の単語を含めなければならない。たとえば、空白は含むことはできないが、数字で始まってもよい。定められた選択肢の一覧は、典型的には関連する属性指定のなかで<gi>valList</gi>要素による値のリストの形で提供（または例示）される。</p>
  </remarks>
  <remarks ident="teidata.enumerated-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Les attributs utilisant ce type de données doivent contenir un mot qui suit les règles de
      définition d'un nom XML valide (voir <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>):
      par exemple ils ne peuvent pas contenir des blancs ni commencer par des chiffres. </p>
      <p>Normalement, la liste des possibilités documentées est fournie (ou exemplifiée) par une liste
      de valeurs dans la spécification de l'attribut associé, exprimée par un élément
      <gi>valList</gi>.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values expressed as a single XML name taken from a list of
    documented possibilities.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기록된 확률의 목록으로부터 얻어진 단일 XML 이름으로 표현된 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以單字或代號呈現，該單字或代號出自於一份紀錄所有可能性的列表</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">定められた選択肢の一覧から選ばれる単一のXML名前を値域とする属性値を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme de
  valeurs des attributs exprimant un nom XML
    extrait d'une liste de possibilités documentées.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos expresados como
    una única palabra o señal tomada de una lista de posibilidades documentadas.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi espressi come
    singola parola o token tratto da una lista di possibilità attestate</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef key="teidata.word"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.enumerated-remarks" versionDate="2016-12-01" xml:lang="en">
    <p>Attributes using this datatype must contain a single
      <soCalled>word</soCalled> which contains only letters, digits,
      punctuation characters, or symbols: thus it cannot include
      whitespace.</p>
      <p>Typically, the list of documented possibilities will be provided (or exemplified) by a value
      list in the associated attribute specification, expressed with a <gi>valList</gi> element.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.enumerated-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>このデータ型を使用する属性は、このデータ型のために定義されたパターンと一致する単一の単語を含めなければならない。たとえば、空白は含むことはできないが、数字で始まってもよい。定められた選択肢の一覧は、典型的には関連する属性指定のなかで<gi>valList</gi>要素による値のリストの形で提供（または例示）される。</p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.enumerated-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Les attributs utilisant ce type de données doivent contenir un mot qui suit les règles de
      définition d'un nom XML valide (voir <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>):
      par exemple ils ne peuvent pas contenir des blancs ni commencer par des chiffres. </p>
      <p>Normalement, la liste des possibilités documentées est fournie (ou exemplifiée) par une liste
      de valeurs dans la spécification de l'attribut associé, exprimée par un élément
      <gi>valList</gi>.</p>
  </remarks>
```

^b11

