---
type: representation
source-type: document
source: '[[00_sources/tei-p5-age-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 age
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/age.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# age

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6674. Git blob: `d5be5919b7e99c81b5a865cbba1c335c42f6fcfb`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-age" ident="age">
  <gloss xml:lang="en" versionDate="2008-12-09">age</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">âge</gloss>
  <desc versionDate="2006-10-08" xml:lang="en">specifies the age of a person.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 나이를 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明個人的年齡。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物の年齢を示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">précise l'âge d'une personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica la edad de una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica l'età della persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
        <valItem ident="western"/>
        <valItem ident="sui"/>
        <valItem ident="subjective"/>
        <valItem ident="objective"/>
        <valItem ident="inWorld">
          <gloss versionDate="2017-06-08" xml:lang="en">in world</gloss>
          <gloss versionDate="2018-09-08" xml:lang="es">en el mundo</gloss>
          <gloss versionDate="2018-12-20" xml:lang="ja">物語世界</gloss>
          <desc versionDate="2017-06-08" xml:lang="en">age of a fictional character at the time the story takes place, rather than at the time the story is told</desc>
          <desc versionDate="2018-09-08" xml:lang="es">Edad de un personaje ficcional en el tiempo en el que la historia sucede (no en el tiempo en el cual es contada).</desc>
          <desc versionDate="2018-12-20" xml:lang="ja">物語を語る時点ではなく、物語の中の時点における架空の人物の年齢。</desc>
        </valItem>
        <valItem ident="chronological"/>
        <valItem ident="biological"/>
        <valItem ident="psychological"/>
        <valItem ident="functional"/>
      </valList>
    </attDef>
    <attDef ident="value" usage="opt">
      <desc versionDate="2006-10-08" xml:lang="en">supplies a numeric code representing the age or age group.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">나이 또는 연령대를 표시하는 수치 부호를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個代表該年齡或年齡層的數字代碼</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">年齢または年齢層を数値で示す。</desc>
      <desc versionDate="2008-12-09" xml:lang="fr">fournit un code numérique représentant l'âge ou la tranche d'âge.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un código numérico que representa la edad o el intervalo de edad.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un codice numerico che rappresenta l'età o la fascia di età.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="age-attr.value-remarks" versionDate="2006-10-08" xml:lang="en">
        <p>This attribute may be used to complement a more detailed discussion of a person's age in
          the content of the element</p>
      </remarks>
  <remarks ident="age-attr.value-remarks" versionDate="2018-09-08" xml:lang="es"><p>Este atributo debería ser usado para complementar un debate más detallado sobre la edad de la persona en el contenido del elemento</p></remarks>
      <remarks ident="age-attr.value-remarks" versionDate="2008-12-09" xml:lang="fr">
        <p>Cet attribut peut être utilisé pour compléter les détails sur l'âge d'une personne donnés
          dans l'élément.</p>
      </remarks>
      <remarks ident="age-attr.value-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、要素中の内容に既にある、年齢に関する記述をより詳細 に示すために使ってもよい。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-age-egXML-xj" source="#NONE">
      <age value="2" notAfter="1986">under 20 in the early eighties</age>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-age-egXML-ev" source="#NONE">
      <age value="2" notAfter="1986">ayant une vingtaine d'années au début des années 70</age>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-age-egXML-ov" source="#NONE">
      <age value="2" notAfter="1986">在八○年代早期不到二十歲</age>
    </egXML>
  </exemplum>
  <remarks ident="age-remarks" versionDate="2012-03-14" xml:lang="en">
    <p>As with other culturally-constructed traits such as
    sex, the way in which this concept is described in different
    cultural contexts may vary. The normalizing attributes are
    provided as a means of simplifying that variety to Western
    European norms and should not be used where that is
    inappropriate. The content of the element may be used to describe
    the intended concept in more detail, using plain text. </p>
  </remarks>
  <remarks ident="age-remarks" versionDate="2018-12-20" xml:lang="ja">
    <p>性別のような文化的に構築された他の特徴と同様に、このコンセプトが異なる文化的背景の中で記述される方法は様々である。正規化属性は、その種類を西ヨーロッパの基準に単純化する手段として提供され、不適切な箇所では使用しないでください。要素の内容は、プレーンテキストを使用して、意図された概念をより詳細に記述するために使用することができる。</p>
  </remarks>
  <listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss xml:lang="en" versionDate="2008-12-09">age</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">âge</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-10-08" xml:lang="en">specifies the age of a person.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 나이를 명시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明個人的年齡。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物の年齢を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">précise l'âge d'une personne.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la edad de una persona.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'età della persona.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="western"/>
        <valItem ident="sui"/>
        <valItem ident="subjective"/>
        <valItem ident="objective"/>
        <valItem ident="inWorld">
          <gloss versionDate="2017-06-08" xml:lang="en">in world</gloss>
          <gloss versionDate="2018-09-08" xml:lang="es">en el mundo</gloss>
          <gloss versionDate="2018-12-20" xml:lang="ja">物語世界</gloss>
          <desc versionDate="2017-06-08" xml:lang="en">age of a fictional character at the time the story takes place, rather than at the time the story is told</desc>
          <desc versionDate="2018-09-08" xml:lang="es">Edad de un personaje ficcional en el tiempo en el que la historia sucede (no en el tiempo en el cual es contada).</desc>
          <desc versionDate="2018-12-20" xml:lang="ja">物語を語る時点ではなく、物語の中の時点における架空の人物の年齢。</desc>
        </valItem>
        <valItem ident="chronological"/>
        <valItem ident="biological"/>
        <valItem ident="psychological"/>
        <valItem ident="functional"/>
      </valList>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2006-10-08" xml:lang="en">supplies a numeric code representing the age or age group.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">나이 또는 연령대를 표시하는 수치 부호를 제시한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個代表該年齡或年齡層的數字代碼</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">年齢または年齢層を数値で示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">fournit un code numérique représentant l'âge ou la tranche d'âge.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un código numérico que representa la edad o el intervalo de edad.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un codice numerico che rappresenta l'età o la fascia di età.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="age-attr.value-remarks" versionDate="2006-10-08" xml:lang="en">
        <p>This attribute may be used to complement a more detailed discussion of a person's age in
          the content of the element</p>
      </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="age-attr.value-remarks" versionDate="2018-09-08" xml:lang="es"><p>Este atributo debería ser usado para complementar un debate más detallado sobre la edad de la persona en el contenido del elemento</p></remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="age-attr.value-remarks" versionDate="2008-12-09" xml:lang="fr">
        <p>Cet attribut peut être utilisé pour compléter les détails sur l'âge d'une personne donnés
          dans l'élément.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="age-attr.value-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、要素中の内容に既にある、年齢に関する記述をより詳細 に示すために使ってもよい。 </p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-age-egXML-xj" source="#NONE">
      <age value="2" notAfter="1986">under 20 in the early eighties</age>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-age-egXML-ev" source="#NONE">
      <age value="2" notAfter="1986">ayant une vingtaine d'années au début des années 70</age>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-age-egXML-ov" source="#NONE">
      <age value="2" notAfter="1986">在八○年代早期不到二十歲</age>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="age-remarks" versionDate="2012-03-14" xml:lang="en">
    <p>As with other culturally-constructed traits such as
    sex, the way in which this concept is described in different
    cultural contexts may vary. The normalizing attributes are
    provided as a means of simplifying that variety to Western
    European norms and should not be used where that is
    inappropriate. The content of the element may be used to describe
    the intended concept in more detail, using plain text. </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="age-remarks" versionDate="2018-12-20" xml:lang="ja">
    <p>性別のような文化的に構築された他の特徴と同様に、このコンセプトが異なる文化的背景の中で記述される方法は様々である。正規化属性は、その種類を西ヨーロッパの基準に単純化する手段として提供され、不適切な箇所では使用しないでください。要素の内容は、プレーンテキストを使用して、意図された概念をより詳細に記述するために使用することができる。</p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
```

^b31

