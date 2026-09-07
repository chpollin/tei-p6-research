---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.declaring-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.declaring
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.declaring.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.declaring

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5168. Git blob: `675c418bc86d468ab90a9dab2936e2c4021c262b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tei" xml:id="DECLING" type="atts" ident="att.declaring">
  <desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements which may be independently associated with a particular declarable element within the header, thus overriding the inherited default for that element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">헤더에서 선언 가능한 어떤 요소와 독립적으로 연관될 수 있는 속성을 제공한다. 이를 통해 그 요소의 상속된 기본값은 무효가 된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素屬性，這些元素可單獨與標頭中一特定可宣告元素相關連，因此超越該特定元素本身的預設值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">TEIヘダーにある特定の宣言可能要素向けの属性を示す。これにより、当該
  要素の継承値を上書きすることになる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour les éléments qui peuvent
    être associés  indépendamment à un élément particulier déclarable dans l'en-tête TEI, ignorant
      ainsi la valeur dont cet élément devrait hériter par défaut.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos a los elementos que pueden ser asociados autonomamente a un elemento determinado declarado en el encabezado, no teniendo en cuenta el default heredato por aquel elemento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna attributi agli elementi che possono essere autonomamente associati a un determinato elemento dichiarato nell'intestazione, non tenendo conto del default ereditato per quell'elemento.</desc>
  <attList>
    <attDef ident="decls" usage="opt">
      <gloss versionDate="2022-05-05" xml:lang="en">declarations</gloss>
      <gloss versionDate="2022-05-05" xml:lang="fr">déclarations</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">identifies one or more <term>declarable elements</term> within the
header, which are understood to apply to the element bearing this
attribute and its content.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">헤더 내의 하나 이상의 <term>declarable elements</term>을 식별하며, 이 속성과 내용을 포함하는 요소에 적용되는 것으로 간주된다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明標頭內一個或多個可宣告元素，可應用於帶有此屬性與內容的元素上。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">TEIヘダーにある、1つ以上の<term>宣言可能要素</term>を示す。
      当該属性を持つ要素や内容に適応されると解釈される。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">identifie un ou plusieurs<term>éléments
            déclarables</term> dans l'en-tête TEI, qui sont destinés à s'appliquer à l'élément
          portant cet attribut et à son contenu.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica uno o más <term>elementos declarables</term> al interno del encabezado, los cuales son válidos para el elemento al cual es adscrito el atributo en cuestión y su contenido.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica uno o più <term>elementi dichiarabili</term> all'interno dell'intestazione,
i quali sono validi per l'elemento a cui è assegnato l'attributo in questione e il suo contenuto</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <remarks ident="att.declaring-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>The rules governing the association of declarable elements
with individual parts of a TEI text are fully defined in chapter <ptr target="#CCAS"/>.</p>
  </remarks>
  <remarks ident="att.declaring-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les règles régissant l'association d'éléments déclarables avec des parties
                individuelles d'un texte TEI sont entièrement définies au chapitre <ptr target="#CCAS"/>.</p>
  </remarks>
  <remarks ident="att.declaring-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Las reglas que gobiernan la asociación de los elementos declarables con las partes individuales de un texto de TEI se definen completamente en el capítulo <ptr target="#CCAS"/>.</p>
  </remarks>
  <remarks ident="att.declaring-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    宣言可能要素の関連性を決める規則については、<ptr target="#CCAS"/>
        を参照のこと。
     </p>
  </remarks>
  <listRef>
    <ptr target="#CCAS"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements which may be independently associated with a particular declarable element within the header, thus overriding the inherited default for that element.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">헤더에서 선언 가능한 어떤 요소와 독립적으로 연관될 수 있는 속성을 제공한다. 이를 통해 그 요소의 상속된 기본값은 무효가 된다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素屬性，這些元素可單獨與標頭中一特定可宣告元素相關連，因此超越該特定元素本身的預設值。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">TEIヘダーにある特定の宣言可能要素向けの属性を示す。これにより、当該
  要素の継承値を上書きすることになる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour les éléments qui peuvent
    être associés  indépendamment à un élément particulier déclarable dans l'en-tête TEI, ignorant
      ainsi la valeur dont cet élément devrait hériter par défaut.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos a los elementos que pueden ser asociados autonomamente a un elemento determinado declarado en el encabezado, no teniendo en cuenta el default heredato por aquel elemento.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna attributi agli elementi che possono essere autonomamente associati a un determinato elemento dichiarato nell'intestazione, non tenendo conto del default ereditato per quell'elemento.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2022-05-05" xml:lang="en">declarations</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2022-05-05" xml:lang="fr">déclarations</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">identifies one or more <term>declarable elements</term> within the
header, which are understood to apply to the element bearing this
attribute and its content.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">헤더 내의 하나 이상의 <term>declarable elements</term>을 식별하며, 이 속성과 내용을 포함하는 요소에 적용되는 것으로 간주된다.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明標頭內一個或多個可宣告元素，可應用於帶有此屬性與內容的元素上。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">TEIヘダーにある、1つ以上の<term>宣言可能要素</term>を示す。
      当該属性を持つ要素や内容に適応されると解釈される。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">identifie un ou plusieurs<term>éléments
            déclarables</term> dans l'en-tête TEI, qui sont destinés à s'appliquer à l'élément
          portant cet attribut et à son contenu.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica uno o más <term>elementos declarables</term> al interno del encabezado, los cuales son válidos para el elemento al cual es adscrito el atributo en cuestión y su contenido.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica uno o più <term>elementi dichiarabili</term> all'interno dell'intestazione,
i quali sono validi per l'elemento a cui è assegnato l'attributo in questione e il suo contenuto</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.declaring-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>The rules governing the association of declarable elements
with individual parts of a TEI text are fully defined in chapter <ptr target="#CCAS"/>.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.declaring-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les règles régissant l'association d'éléments déclarables avec des parties
                individuelles d'un texte TEI sont entièrement définies au chapitre <ptr target="#CCAS"/>.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.declaring-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Las reglas que gobiernan la asociación de los elementos declarables con las partes individuales de un texto de TEI se definen completamente en el capítulo <ptr target="#CCAS"/>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="att.declaring-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    宣言可能要素の関連性を決める規則については、<ptr target="#CCAS"/>
        を参照のこと。
     </p>
  </remarks>
```

^b21

### Block 22

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAS"/>
  </listRef>
```

^b22

