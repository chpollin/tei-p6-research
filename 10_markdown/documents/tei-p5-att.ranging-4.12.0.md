---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.ranging-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.ranging
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.ranging.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.ranging

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4289. Git blob: `3c5cd40c74786e9cda84f2319ad92f648595d147`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" xml:id="class-attr-ranging" ident="att.ranging">
  <desc versionDate="2009-06-05" xml:lang="en">provides attributes for describing numerical ranges.</desc>
  <desc versionDate="2023-09-27" xml:lang="ja">数値範囲を記述するための属性を提供する。</desc>
  <attList>
    <attDef ident="atLeast">
      <desc versionDate="2009-06-29" xml:lang="en">gives a minimum estimated value for the approximate measurement.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">donne une estimation de la valeur minimum pour la mesure.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">概算推量のための最小推定値を与える。</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="atMost">
      <desc versionDate="2009-06-29" xml:lang="en">gives a maximum estimated value for the approximate measurement.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">donne une estimation de la valeur maximum pour la mesure.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">概算推量のための最大推定値を与える。</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="min">
      <desc versionDate="2009-06-29" xml:lang="en">where the measurement summarizes more than one observation or a range, supplies the minimum value observed.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">lorsque la mesure résume plus d'une observation, fournit la valeur minimum observée.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">1回以上の観察あるいは範囲をまとめた推量において、観察された最小値を提供する。</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="max">
      <desc versionDate="2009-06-29" xml:lang="en">where the measurement summarizes more than one observation or a range, supplies the maximum value observed.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">lorsque la mesure résume plus d'une observation, fournit la valeur maximum observée.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">1回以上の観察あるいは範囲をまとめた推量において、観察された最大値を提供する。</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="confidence">
      <desc versionDate="2012-12-27" xml:lang="en">specifies the degree of statistical confidence (between zero and one) that a value falls within the range specified by <att>min</att> and <att>max</att>, or the proportion of observed values that fall within that range.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja"><att>min</att>と<att>max</att>、で指定された範囲内の値、あるいはその範囲内で観察された値の割合の統計的な信頼度を0から1の値で示す。</desc>
      <datatype><dataRef key="teidata.probability"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ranging-egXML-mr">
      The MS. was lost in transmission by mail from
      <del rend="overstrike"><gap reason="illegible" extent="one or two letters" atLeast="1" atMost="2" unit="chars"/></del>
      Philadelphia to the Graphic office, New York.
    </egXML>
  </exemplum>
  <exemplum versionDate="2022-09-13" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ranging-egXML-li" source="#URF-UBSGlobal">
      Americares has been supporting the health sector in Eastern Europe since 1986,
      and since 1992 has provided <measure atLeast="120000000" unit="USD" commodity="currency">more
      than $120m</measure> in aid to Ukrainians.
    </egXML>
  </exemplum>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2009-06-05" xml:lang="en">provides attributes for describing numerical ranges.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">数値範囲を記述するための属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2009-06-29" xml:lang="en">gives a minimum estimated value for the approximate measurement.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">donne une estimation de la valeur minimum pour la mesure.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">概算推量のための最小推定値を与える。</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2009-06-29" xml:lang="en">gives a maximum estimated value for the approximate measurement.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">donne une estimation de la valeur maximum pour la mesure.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">概算推量のための最大推定値を与える。</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2009-06-29" xml:lang="en">where the measurement summarizes more than one observation or a range, supplies the minimum value observed.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">lorsque la mesure résume plus d'une observation, fournit la valeur minimum observée.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">1回以上の観察あるいは範囲をまとめた推量において、観察された最小値を提供する。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2009-06-29" xml:lang="en">where the measurement summarizes more than one observation or a range, supplies the maximum value observed.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">lorsque la mesure résume plus d'une observation, fournit la valeur maximum observée.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">1回以上の観察あるいは範囲をまとめた推量において、観察された最大値を提供する。</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">specifies the degree of statistical confidence (between zero and one) that a value falls within the range specified by <att>min</att> and <att>max</att>, or the proportion of observed values that fall within that range.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja"><att>min</att>と<att>max</att>、で指定された範囲内の値、あるいはその範囲内で観察された値の割合の統計的な信頼度を0から1の値で示す。</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.probability"/></datatype>
```

^b21

### Block 22

XML location: `/classSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ranging-egXML-mr">
      The MS. was lost in transmission by mail from
      <del rend="overstrike"><gap reason="illegible" extent="one or two letters" atLeast="1" atMost="2" unit="chars"/></del>
      Philadelphia to the Graphic office, New York.
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/classSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2022-09-13" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ranging-egXML-li" source="#URF-UBSGlobal">
      Americares has been supporting the health sector in Eastern Europe since 1986,
      and since 1992 has provided <measure atLeast="120000000" unit="USD" commodity="currency">more
      than $120m</measure> in aid to Ukrainians.
    </egXML>
  </exemplum>
```

^b23

