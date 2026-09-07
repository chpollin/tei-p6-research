---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.global.meta-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.global.meta
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.global.meta.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.global.meta

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4464. Git blob: `0c5017b5fc256a6ab24a8db202388575fef0a7ca`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="METADATA" type="model" ident="model.global.meta">
  <desc versionDate="2007-10-03" xml:lang="en">groups globally available elements which describe the status of other elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다른 요소의 상태를 기술하며, 전체적으로 이용가능한 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集描述其他元素狀態的空白元素，例如連結或抽象詮釋，或者提供正確度等，且空白元素可能出現於文件任一處。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">他の要素の状態を示す、どこでも使える要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments disponibles globalement qui
    décrivent le statut d'autres éléments.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos vacíos que describen el estatus de otros
    elementos, p.ej. estableciendo grupos de relaciones o interpretaciones abstractas, o bien
    proporcionando indicaciones de certeza, etc., y que pueden aparecer en cualquier punto de un
    documento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi vuoti che descrivono lo status di
    altri elementi, per esempio stabilendo gruppi di collegamenti o interpretazioni astratte, oppure
    fornendo indicazioni di certezza, ecc., e che possono apparire in qualsiasi punto all'interno di
    un documento</desc>
  <classes>
    
    <memberOf key="model.global"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <remarks ident="model.global.meta-remarks" versionDate="2007-10-03" xml:lang="en">
    <p>Elements in this class are typically used to hold groups of links or of abstract
      interpretations, or by provide indications of certainty etc. It may find be convenient to
      localize all metadata elements, for example to contain them within the same divison as the
      elements that they relate to; or to locate them all to a division of their own. They may
      however appear at any point in a TEI text.</p>
  </remarks>
  <remarks ident="model.global.meta-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Les éléments de cette classe sont utilisés pour contenir des groupes de liens ou
      d'interprétations abstraites, ou pour fournir des indications quant à la certitude, etc. Il
      peut être commode de situer tous les éléments contenant des métadonnées, par exemple de les
      rassembler dans la même divison que les éléments auxquels ils sont reliés ; ou de les
      retrouver tous dans la division qui leur est propre. Ils peuvent cependant apparaître à un
      point quelconque d'un texte TEI.</p>
  </remarks>
  <remarks ident="model.global.meta-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los elementos en esta clase se utilizan típicamente para llevar a cabo los grupos de
      conexiones o de interpretaciones abstractas, o bien para proporcionar indicaciones de la
      certeza etc. Puede ser conveniente localizar todos los elementos de los metadatos, por ejemplo
      para contenerlos dentro de la misma división que los elementos con los cuales se relacionan; o
      para localizarlos todos en la división que les es propia. Sin embargo pueden aparecer en
      cualquier momento en un texto de TEI.</p>
  </remarks>
  <remarks ident="model.global.meta-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該クラスの要素は、リンクや確信度といった抽象的解釈をまとめるため に使われる。これは、ユーザがメタデータを記述する際に便利であろう。
      例えば、関連する要素と同じ部分レベル内にあるものまとめたり、関連す る要素を、自身の部分レベル内にまめめたりする場合である。
      しかし、これらは、TEIデータ中では、どこにでも出現可能である。 </p>
  </remarks>
  <listRef>
    <ptr target="#STEC"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups globally available elements which describe the status of other elements.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다른 요소의 상태를 기술하며, 전체적으로 이용가능한 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集描述其他元素狀態的空白元素，例如連結或抽象詮釋，或者提供正確度等，且空白元素可能出現於文件任一處。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">他の要素の状態を示す、どこでも使える要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments disponibles globalement qui
    décrivent le statut d'autres éléments.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos vacíos que describen el estatus de otros
    elementos, p.ej. estableciendo grupos de relaciones o interpretaciones abstractas, o bien
    proporcionando indicaciones de certeza, etc., y que pueden aparecer en cualquier punto de un
    documento.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi vuoti che descrivono lo status di
    altri elementi, per esempio stabilendo gruppi di collegamenti o interpretazioni astratte, oppure
    fornendo indicazioni di certezza, ecc., e che possono apparire in qualsiasi punto all'interno di
    un documento</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.global"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.global.meta-remarks" versionDate="2007-10-03" xml:lang="en">
    <p>Elements in this class are typically used to hold groups of links or of abstract
      interpretations, or by provide indications of certainty etc. It may find be convenient to
      localize all metadata elements, for example to contain them within the same divison as the
      elements that they relate to; or to locate them all to a division of their own. They may
      however appear at any point in a TEI text.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.global.meta-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Les éléments de cette classe sont utilisés pour contenir des groupes de liens ou
      d'interprétations abstraites, ou pour fournir des indications quant à la certitude, etc. Il
      peut être commode de situer tous les éléments contenant des métadonnées, par exemple de les
      rassembler dans la même divison que les éléments auxquels ils sont reliés ; ou de les
      retrouver tous dans la division qui leur est propre. Ils peuvent cependant apparaître à un
      point quelconque d'un texte TEI.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.global.meta-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los elementos en esta clase se utilizan típicamente para llevar a cabo los grupos de
      conexiones o de interpretaciones abstractas, o bien para proporcionar indicaciones de la
      certeza etc. Puede ser conveniente localizar todos los elementos de los metadatos, por ejemplo
      para contenerlos dentro de la misma división que los elementos con los cuales se relacionan; o
      para localizarlos todos en la división que les es propia. Sin embargo pueden aparecer en
      cualquier momento en un texto de TEI.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.global.meta-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該クラスの要素は、リンクや確信度といった抽象的解釈をまとめるため に使われる。これは、ユーザがメタデータを記述する際に便利であろう。
      例えば、関連する要素と同じ部分レベル内にあるものまとめたり、関連す る要素を、自身の部分レベル内にまめめたりする場合である。
      しかし、これらは、TEIデータ中では、どこにでも出現可能である。 </p>
  </remarks>
```

^b12

### Block 13

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
  </listRef>
```

^b13

