---
type: representation
source-type: document
source: '[[00_sources/tei-p5-crefpattern-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 cRefPattern
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/cRefPattern.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# cRefPattern

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5012. Git blob: `78a9aa877f320c5c024bf26af423c6d36a217880`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-cRefPattern" ident="cRefPattern">
  <gloss versionDate="2007-07-09" xml:lang="en">canonical reference pattern</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">Modèle de référence canonique</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">표준 참조 유형</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">定義如何將標準參照轉換成統一資源識別符 (URI) 。</gloss>
  <gloss versionDate="2018-07-18" xml:lang="de">kanonisches Referenzmodell</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">define cómo convertir una referncia canónica en un URI</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">definisce in che modo convertire un riferimento canonico
    in un URI</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">標準的参照パタン</gloss>
  <desc versionDate="2008-01-13" xml:lang="en">specifies an expression and replacement pattern for transforming a canonical reference into
    a URI.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">spécifie un modèle d’expression et des règles de
    remplacement pour transformer une référence canonique en URI.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 참조를 URI로 변환하기 위한 표현 및 대체 유형을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明將標準參照轉換成統一資源識別符的表示方法與取代模式。</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">標準的形式の参照をURIに変形するための表現・変形パタンを示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">legt einen Ausdruck und ein Ersetzungsmuster für die
    Umwandlung einer kanonischen Referenz in eine URI fest.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica una expresión y un patrón de remplazamiento para
    transformar una referencia canónica en un URI.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica un espressione o un pattern di sostituzione per
    convertire convertire un riferimento canonico in un URI</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.patternReplacement"/>
  </classes>
  <content>
    
      <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cRefPattern-egXML-cp" source="#UND">
      <cRefPattern matchPattern="([1-9A-Za-z]+)\s+([0-9]+):([0-9]+)" replacementPattern="#xpath(//div[@type='book'][@n='$1']/div[@type='chap'][@n='$2']/div[@type='verse'][@n='$3'])"/>
    </egXML>
  </exemplum>
  <remarks ident="cRefPattern-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The result of the substitution may be either an absolute or a relative URI reference. In the
      latter case it is combined with the value of <att>xml:base</att> in force at the place where
      the <att>cRef</att> attribute occurs to form an absolute URI in the usual manner as prescribed
      by <ref target="https://www.w3.org/TR/xmlbase/">XML Base</ref>.</p>
  </remarks>
  <remarks ident="cRefPattern-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le résultat de la substitution peut être la référence à une URI relative ou absolue.
      Dans ce dernier cas, il est combiné avec la valeur de l'attribut <att>xml:base</att> en
      vigueur à la place où apparaît l'attribut <att>cRef</att> pour former une URI absolue selon
      l'usage habituel indiqué par <ref target="https://www.w3.org/TR/xmlbase/">XML Base</ref>.</p>
  </remarks>
  <remarks ident="cRefPattern-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El resultado de la substitución puede ser una referencia URI absoluta o relativa. En el
      último caso se combina con el valor de <att>xml:base</att> en vigor en el lugar donde el
      atributo <att>cRef</att> aparece para formar un URI absoluto de manera común según lo
      prescrito por <ref target="https://www.w3.org/TR/xmlbase/">Base de XML</ref>.</p>
  </remarks>
  <remarks ident="cRefPattern-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 置換による結果は、絶対・相対URIであるかもしれない。相対URIの場合、 <ref target="https://www.w3.org/TR/xmlbase/">XML
      Base</ref>に示され ているように、属性<att>xml:base</att>の値と共に、属性 <att>cRef</att>が絶対URIを示す場所で使用される。 </p>
  </remarks>
  <listRef>
    <ptr target="#HD54M"/>
    <ptr target="#HD54"/>
    <ptr target="#HD54S"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-09" xml:lang="en">canonical reference pattern</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">Modèle de référence canonique</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">표준 참조 유형</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">定義如何將標準參照轉換成統一資源識別符 (URI) 。</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2018-07-18" xml:lang="de">kanonisches Referenzmodell</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">define cómo convertir una referncia canónica en un URI</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">definisce in che modo convertire un riferimento canonico
    in un URI</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">標準的参照パタン</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-01-13" xml:lang="en">specifies an expression and replacement pattern for transforming a canonical reference into
    a URI.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">spécifie un modèle d’expression et des règles de
    remplacement pour transformer une référence canonique en URI.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준 참조를 URI로 변환하기 위한 표현 및 대체 유형을 명시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明將標準參照轉換成統一資源識別符的表示方法與取代模式。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">標準的形式の参照をURIに変形するための表現・変形パタンを示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">legt einen Ausdruck und ein Ersetzungsmuster für die
    Umwandlung einer kanonischen Referenz in eine URI fest.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica una expresión y un patrón de remplazamiento para
    transformar una referencia canónica en un URI.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica un espressione o un pattern di sostituzione per
    convertire convertire un riferimento canonico in un URI</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.patternReplacement"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cRefPattern-egXML-cp" source="#UND">
      <cRefPattern matchPattern="([1-9A-Za-z]+)\s+([0-9]+):([0-9]+)" replacementPattern="#xpath(//div[@type='book'][@n='$1']/div[@type='chap'][@n='$2']/div[@type='verse'][@n='$3'])"/>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="cRefPattern-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The result of the substitution may be either an absolute or a relative URI reference. In the
      latter case it is combined with the value of <att>xml:base</att> in force at the place where
      the <att>cRef</att> attribute occurs to form an absolute URI in the usual manner as prescribed
      by <ref target="https://www.w3.org/TR/xmlbase/">XML Base</ref>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="cRefPattern-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le résultat de la substitution peut être la référence à une URI relative ou absolue.
      Dans ce dernier cas, il est combiné avec la valeur de l'attribut <att>xml:base</att> en
      vigueur à la place où apparaît l'attribut <att>cRef</att> pour former une URI absolue selon
      l'usage habituel indiqué par <ref target="https://www.w3.org/TR/xmlbase/">XML Base</ref>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="cRefPattern-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El resultado de la substitución puede ser una referencia URI absoluta o relativa. En el
      último caso se combina con el valor de <att>xml:base</att> en vigor en el lugar donde el
      atributo <att>cRef</att> aparece para formar un URI absoluto de manera común según lo
      prescrito por <ref target="https://www.w3.org/TR/xmlbase/">Base de XML</ref>.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="cRefPattern-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 置換による結果は、絶対・相対URIであるかもしれない。相対URIの場合、 <ref target="https://www.w3.org/TR/xmlbase/">XML
      Base</ref>に示され ているように、属性<att>xml:base</att>の値と共に、属性 <att>cRef</att>が絶対URIを示す場所で使用される。 </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD54M"/>
    <ptr target="#HD54"/>
    <ptr target="#HD54S"/>
  </listRef>
```

^b24

