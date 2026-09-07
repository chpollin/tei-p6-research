---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.name-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.name
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.name.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.name

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2471. Git blob: `64bbcac9d141ee5d050269fb7a04e4ba9d65cb06`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.name">
  <desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values expressed as an XML Name.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">XML 이름으로 표현되는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以XML名稱或識別符碼表示</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">XML名前としてある属性値の範囲を定義する。</desc>
  <desc versionDate="2009-05-29" xml:lang="fr">définit la gamme des valeurs d'attribut exprimant
    un nom XML.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos expresados como
    identificador o un nombre en XML.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi espressi come
    identificatore o nome XML</desc>
  <content>
      <dataRef name="Name"/>
   </content>
  <remarks ident="teidata.name-remarks" versionDate="2007-10-18" xml:lang="en">
      <p>Attributes using this datatype must contain a single word which follows the rules defining a
      legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>): for example they
      cannot include whitespace or begin with digits. </p>
  </remarks>
  <remarks ident="teidata.name-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 当該属性は、妥当なXML名前(詳細は <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>を参照)である
      ひとつの単語をとる。例えば、空白文字を含まず、数字が先頭文字にこな いもの。 </p>
  </remarks>
  <remarks ident="teidata.name-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Les attributs utilisant ce type de données doivent contenir un seul mot, qui suit les règles
      de définition d'un nom XML valide (voir <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>) :
      par exemple ils ne peuvent contenir de blancs ou commencer par des chiffres. </p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values expressed as an XML Name.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">XML 이름으로 표현되는 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以XML名稱或識別符碼表示</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">XML名前としてある属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-29" xml:lang="fr">définit la gamme des valeurs d'attribut exprimant
    un nom XML.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos expresados como
    identificador o un nombre en XML.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi espressi come
    identificatore o nome XML</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="Name"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.name-remarks" versionDate="2007-10-18" xml:lang="en">
      <p>Attributes using this datatype must contain a single word which follows the rules defining a
      legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>): for example they
      cannot include whitespace or begin with digits. </p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.name-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 当該属性は、妥当なXML名前(詳細は <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>を参照)である
      ひとつの単語をとる。例えば、空白文字を含まず、数字が先頭文字にこな いもの。 </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.name-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Les attributs utilisant ce type de données doivent contenir un seul mot, qui suit les règles
      de définition d'un nom XML valide (voir <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>) :
      par exemple ils ne peuvent contenir de blancs ou commencer par des chiffres. </p>
  </remarks>
```

^b11

