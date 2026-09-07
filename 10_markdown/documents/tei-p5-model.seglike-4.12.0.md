---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.seglike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.segLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.segLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.segLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2893. Git blob: `8e1493dcef08edcc0bc3d7561d9201a08bfe7cb7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="model" ident="model.segLike">
  <desc versionDate="2005-10-10" xml:lang="en">groups elements used for arbitrary segmentation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">임의적 분할에 사용되는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集用於隨機分割的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">任意の区分で使用される要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments utilisés pour une segmentation
    arbitraire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos usados por una segmentación arbitraria.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi utilizzati per una segmentazione
    arbitraria</desc>
  <classes>
    
    <memberOf key="model.phrase"/>
    <!--<memberOf key="model.linePart"/>-->
  </classes>
  <remarks ident="model.segLike-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>The principles on which segmentation is carried out, and any special codes or attribute
      values used, should be defined explicitly in the <gi>segmentation</gi> element of the
        <gi>encodingDesc</gi> within the associated TEI header.</p>
  </remarks>
  <remarks ident="model.segLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les principes sur lesquels repose la segmentation, ainsi que tout code particulier ou valeur
      d'attribut utilisée, doivent être définis explicitement dans l'élément <gi>segmentation</gi> de
      l'élément <gi>encodingDesc</gi> situé dans l'En-tête TEI associé.</p>
  </remarks>
  <remarks ident="model.segLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los principios en los cuales se realiza la segmentación, y cualesquiera sean los códigos o
      valores de atributo especiales usados, se deben definir explícitamente en el elemento
        <gi>segmentación</gi> del <gi>encodingDesc</gi> dentro del encabezado TEI asociado.</p>
  </remarks>
  <remarks ident="model.segLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> どの区分、どのコード、どの属性値を使うかを決める原則は、関連する TEIヘダー内の要素<gi>encodingDesc</gi>にある要素
      <gi>segmentation</gi>中で明示的に宣言されるべきである。 </p>
  </remarks>
  <listRef>
    <ptr target="#SASE"/>
    <ptr target="#AILC"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">groups elements used for arbitrary segmentation.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">임의적 분할에 사용되는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集用於隨機分割的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">任意の区分で使用される要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments utilisés pour une segmentation
    arbitraire.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos usados por una segmentación arbitraria.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi utilizzati per una segmentazione
    arbitraria</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.phrase"/>
    <!--<memberOf key="model.linePart"/>-->
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.segLike-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>The principles on which segmentation is carried out, and any special codes or attribute
      values used, should be defined explicitly in the <gi>segmentation</gi> element of the
        <gi>encodingDesc</gi> within the associated TEI header.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.segLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les principes sur lesquels repose la segmentation, ainsi que tout code particulier ou valeur
      d'attribut utilisée, doivent être définis explicitement dans l'élément <gi>segmentation</gi> de
      l'élément <gi>encodingDesc</gi> situé dans l'En-tête TEI associé.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.segLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los principios en los cuales se realiza la segmentación, y cualesquiera sean los códigos o
      valores de atributo especiales usados, se deben definir explícitamente en el elemento
        <gi>segmentación</gi> del <gi>encodingDesc</gi> dentro del encabezado TEI asociado.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.segLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> どの区分、どのコード、どの属性値を使うかを決める原則は、関連する TEIヘダー内の要素<gi>encodingDesc</gi>にある要素
      <gi>segmentation</gi>中で明示的に宣言されるべきである。 </p>
  </remarks>
```

^b12

### Block 13

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SASE"/>
    <ptr target="#AILC"/>
  </listRef>
```

^b13

