---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.key-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.key
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.key.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.key

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4015. Git blob: `dc9b39f3e7c2fbf4024fdcb8748857eb9d03f148`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.key">
  <desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values expressing a coded value by means of an arbitrary
    identifier, typically taken from a set of externally-defined possibilities.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">임의의 확인소에 의해 부호화된 값을 표현하는 속성 값 범위를 정의하며, 이것은 일반적으로 외부 정의
    확률의 집합에서 얻어진다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以隨機識別碼來表示一個編碼值，該識別碼通常來自一組外部定義的可能性</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">任意の識別子により属性値の範囲が定義される。典型例は、外部で定義され ているものから値がとられる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs exprimant une
    valeur encodée au moyen d'un identifiant arbitraire, typiquement emprunté à un ensemble de
    possibilités définies extérieurement</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que expresan un
    valor codificado a través de un identificador arbitrario obtenido, normalmente, de un conjunto
    de posibilidades definidas exteriormente.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi che esprimono
    un valore codificato tramite un identificatore arbitrario tratto, di solito, da un insieme di
    possibilità definite esternamente</desc>
  <content>
      <dataRef name="string"/>
   </content>
  <remarks ident="teidata.key-remarks" versionDate="2005-10-18" xml:lang="en">
      <p>Information about the set of possible values for an attribute using this datatype may (but
      need not) be documented in the document header. Externally defined constraints, for example
      that values should be legal keys in an external database system, cannot usually be enforced by
      a TEI system. Similarly, because the key is externally defined, no constraint other than a
      requirement that it consist of Unicode characters is possible. </p>
  </remarks>
  <remarks ident="teidata.key-remarks" xml:lang="ja" versionDate="2008-04-05">
      <p> 当該データ型で定義される属性値に関する情報は、(必須ではないが)当該 文書のヘダーに記述されるかもしれない。外部で定義されている制約、例
      えば、外部のデータベースシステムにあるキーの定義は、一般には、(そ のままでは)TEIシステムでは使うことができない。また、このキーは外部
      で定義されているので、ユニコード文字を使用するという制約以外の制約 を採用することも可能になる。 </p>
  </remarks>
  <remarks ident="teidata.key-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Les informations sur le jeu de valeurs possibles pour un attribut utilisant ce type de
      données peuvent (mais cela n'est pas nécessaire) être documentées dans l'en-tête TEI du document.
      Des contraintes définies de façon externe, par exemple le fait que les valeurs doivent être
      des clés valides dans une base de données externe, ne peuvent être appliquées habituellement par un
      système TEI. De même, parce que la clé est définie de façon externe, aucune contrainte autre
      que la nécessité d'être constituée de caractères Unicode n'est possible. </p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values expressing a coded value by means of an arbitrary
    identifier, typically taken from a set of externally-defined possibilities.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">임의의 확인소에 의해 부호화된 값을 표현하는 속성 값 범위를 정의하며, 이것은 일반적으로 외부 정의
    확률의 집합에서 얻어진다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以隨機識別碼來表示一個編碼值，該識別碼通常來自一組外部定義的可能性</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">任意の識別子により属性値の範囲が定義される。典型例は、外部で定義され ているものから値がとられる。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs exprimant une
    valeur encodée au moyen d'un identifiant arbitraire, typiquement emprunté à un ensemble de
    possibilités définies extérieurement</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que expresan un
    valor codificado a través de un identificador arbitrario obtenido, normalmente, de un conjunto
    de posibilidades definidas exteriormente.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi che esprimono
    un valore codificato tramite un identificatore arbitrario tratto, di solito, da un insieme di
    possibilità definite esternamente</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="string"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.key-remarks" versionDate="2005-10-18" xml:lang="en">
      <p>Information about the set of possible values for an attribute using this datatype may (but
      need not) be documented in the document header. Externally defined constraints, for example
      that values should be legal keys in an external database system, cannot usually be enforced by
      a TEI system. Similarly, because the key is externally defined, no constraint other than a
      requirement that it consist of Unicode characters is possible. </p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.key-remarks" xml:lang="ja" versionDate="2008-04-05">
      <p> 当該データ型で定義される属性値に関する情報は、(必須ではないが)当該 文書のヘダーに記述されるかもしれない。外部で定義されている制約、例
      えば、外部のデータベースシステムにあるキーの定義は、一般には、(そ のままでは)TEIシステムでは使うことができない。また、このキーは外部
      で定義されているので、ユニコード文字を使用するという制約以外の制約 を採用することも可能になる。 </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.key-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Les informations sur le jeu de valeurs possibles pour un attribut utilisant ce type de
      données peuvent (mais cela n'est pas nécessaire) être documentées dans l'en-tête TEI du document.
      Des contraintes définies de façon externe, par exemple le fait que les valeurs doivent être
      des clés valides dans une base de données externe, ne peuvent être appliquées habituellement par un
      système TEI. De même, parce que la clé est définie de façon externe, aucune contrainte autre
      que la nécessité d'être constituée de caractères Unicode n'est possible. </p>
  </remarks>
```

^b11

