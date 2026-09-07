---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.seglike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.segLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.segLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.segLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3824. Git blob: `509bc1e1bce895f636fa1a0361edba8d6007d9a9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.segLike">
  <desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements used for arbitrary segmentation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">임의적 분할을 위해 사용된 요소의 값을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，用於有隨機分割功用的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">任意の部分に使用される要素向けの属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour des éléments utilisés pour une segmentation arbitraire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos a los elementos usados para una segmentación arbitraria.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi usati per una segmentazione arbitraria.</desc>
  <classes>
    <memberOf key="att.datcat"/>
    <memberOf key="att.fragmentable"/>
    
    <memberOf key="att.metrical"/>
  </classes>
  <attList>
    <attDef ident="function" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">function</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">fonction</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">characterizes the function of the segment.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">분절 기능의 특성을 기술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">描述該分割的功能。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該部分の役割を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">caractérise la fonction du segment.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">caracteriza la función de un segmento.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">caratterizza la funzione del segmento.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="att.segLike-attr.function-remarks" versionDate="2013-12-09" xml:lang="en"><p>Attribute values will often vary depending on the type of element to which they are attached. For example,  a <gi>cl</gi>, may take values such as
coordinate, subject, adverbial etc. For a <gi>phr</gi>, such values as
subject, predicate etc. may be more appropriate. Such constraints will typically be implemented by a project-defined customization. </p></remarks>
      <remarks ident="att.segLike-attr.function-remarks" versionDate="2023-09-27" xml:lang="ja"><p>
        属性値は付与された要素のタイプに応じてしばしば変化する。
        たとえば、<gi>cl</gi>は座標や主語、副詞のような値をとることができる。
        <gi>phr</gi>の場合、主語や述語のような値はより適切かもしれない。
        そういった制約は、典型的には、プロジェクトで定義されたカスタマイズとして実装されるだろう。</p></remarks>
<!--      <valDesc versionDate="2009-05-28" xml:lang="fr">Pour un élément <gi>cl</gi>, peut prendre des valeurs telles que coordonné, sujet, adverbial, etc. 
        Pour un élément <gi>phr</gi>, des valeurs telles que sujet, attribut, etc., peuvent être plus appropriées.</valDesc>-->
    </attDef>
  </attList>
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
<desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements used for arbitrary segmentation.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">임의적 분할을 위해 사용된 요소의 값을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，用於有隨機分割功用的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">任意の部分に使用される要素向けの属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour des éléments utilisés pour une segmentation arbitraire.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos a los elementos usados para una segmentación arbitraria.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi usati per una segmentazione arbitraria.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.datcat"/>
    <memberOf key="att.fragmentable"/>
    
    <memberOf key="att.metrical"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="en">function</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">fonction</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">characterizes the function of the segment.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">분절 기능의 특성을 기술한다.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述該分割的功能。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該部分の役割を示す。</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">caractérise la fonction du segment.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">caracteriza la función de un segmento.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">caratterizza la funzione del segmento.</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.segLike-attr.function-remarks" versionDate="2013-12-09" xml:lang="en"><p>Attribute values will often vary depending on the type of element to which they are attached. For example,  a <gi>cl</gi>, may take values such as
coordinate, subject, adverbial etc. For a <gi>phr</gi>, such values as
subject, predicate etc. may be more appropriate. Such constraints will typically be implemented by a project-defined customization. </p></remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.segLike-attr.function-remarks" versionDate="2023-09-27" xml:lang="ja"><p>
        属性値は付与された要素のタイプに応じてしばしば変化する。
        たとえば、<gi>cl</gi>は座標や主語、副詞のような値をとることができる。
        <gi>phr</gi>の場合、主語や述語のような値はより適切かもしれない。
        そういった制約は、典型的には、プロジェクトで定義されたカスタマイズとして実装されるだろう。</p></remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SASE"/>
    <ptr target="#AILC"/>
  </listRef>
```

^b21

