---
type: representation
source-type: document
source: '[[00_sources/tei-p5-symbol-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 symbol
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/symbol.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# symbol

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4067. Git blob: `3a75a33501a924f0005e92c79071b453543816a9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-symbol" ident="symbol">
  <gloss versionDate="2007-07-04" xml:lang="en">symbolic value</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">기호 값</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">符號值</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">valeur symbolique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">valor simbólico</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">valore simbolico</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification
  which contains one of a finite list of symbols.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">유한한 목록의 기호 중 하나를 포함하는 자질-값 명세에서 값 부분을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含限定符號列表中的其中一項。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">記号リスト中のいち項目を含む素性値規定のうち、値の部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient un symbole extrait d'une liste finie.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene uno de una lista finita de símbolos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene un simbolo da una lista chiusa di simboli.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="value" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">supplies a symbolic value for the feature, one of a finite list that
may be specified in a feature declaration.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">자질 선언에서 명시될 수 있는 유한한 목록 중 하나인 자질의 기호 값을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供功能的符號值，限定符號列表可在功能宣告中指明。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該組成の記号値を示す。素性宣言のリスト中にあるいち項目になる。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne la valeur symbolique pour le trait,
          extraite d'une liste finie qui peut être spécifiée dans une déclaration de traits.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el valor simbólico para un rasgo, uno de una lista finita que puede ser especificada en una declaración de rasgo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce il valore simbolico del tratto, un valore da una lista che può essere specigicata in una dichiarazione di tratti.</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-symbol-egXML-ng" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-symbol-egXML-de" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FSSY" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">symbolic value</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">기호 값</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">符號值</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">valeur symbolique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">valor simbólico</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">valore simbolico</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification
  which contains one of a finite list of symbols.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">유한한 목록의 기호 중 하나를 포함하는 자질-값 명세에서 값 부분을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含限定符號列表中的其中一項。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">記号リスト中のいち項目を含む素性値規定のうち、値の部分を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient un symbole extrait d'une liste finie.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene uno de una lista finita de símbolos.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene un simbolo da una lista chiusa di simboli.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies a symbolic value for the feature, one of a finite list that
may be specified in a feature declaration.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 선언에서 명시될 수 있는 유한한 목록 중 하나인 자질의 기호 값을 제시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供功能的符號值，限定符號列表可在功能宣告中指明。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該組成の記号値を示す。素性宣言のリスト中にあるいち項目になる。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne la valeur symbolique pour le trait,
          extraite d'une liste finie qui peut être spécifiée dans une déclaration de traits.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el valor simbólico para un rasgo, uno de una lista finita que puede ser especificada en una declaración de rasgo.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il valore simbolico del tratto, un valore da una lista che può essere specigicata in una dichiarazione di tratti.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-symbol-egXML-ng" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-symbol-egXML-de" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSSY" type="div3"/>
  </listRef>
```

^b26

