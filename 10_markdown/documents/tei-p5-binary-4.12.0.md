---
type: representation
source-type: document
source: '[[00_sources/tei-p5-binary-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 binary
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/binary.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# binary

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5214. Git blob: `3ebbcd8d5e9c572daadd1f751bca2a80ccba3536`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-binary" ident="binary">
  <gloss versionDate="2005-01-14" xml:lang="en">binary value</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">이진 값</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">二元值</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">valeur binaire</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">valor binario</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">un valore binario</gloss>
  <gloss versionDate="2023-09-21" xml:lang="ja">二値</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification which can contain either
  of exactly two possible values.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">정확히 두 가지 가능한 값 중 하나를 포함할 수 있는 자질-값 명세에서 값의 부분을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，可包含確切兩種可能值中的其中一種。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">二値として、素性値を示す。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">représente la partie <q>valeur</q> d'une spécification
      trait-valeur qui peut contenir l'une ou l'autre des deux valeurs possibles.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que puede contener cualquier de los dos valores posibles.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che può contenere uno di soltanto due possibili valori.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="value" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">supplies a binary value.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이진 값을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個二元值</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">二値で値を示す。</desc>
      <desc versionDate="2009-04-16" xml:lang="fr">fournit une valeur binaire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un valor binario</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un valore binario.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
<remarks ident="binary-attr.value-remarks" versionDate="2013-12-21" xml:lang="en"><p>This attribute has a datatype of <ident type="datatype">teidata.truthValue</ident>, which
may be represented by the values <val>1</val> or
    <val>true</val>, or <val>0</val> or <val>false</val>.</p>
</remarks>
<remarks ident="binary-attr.value-remarks" versionDate="2023-09-21" xml:lang="ja"><p>この属性は<ident type="datatype">teidata.truthValue</ident>のデータ型を持つ。
  その値は、<val>1</val>か<val>true</val>、あるいは<val>0</val>か<val>false</val>で表現される。</p>
</remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-binary-egXML-oa" source="#UND">
      <f name="strident">
        <binary value="true"/>
      </f>
      <f name="exclusive">
        <binary value="false"/>
      </f>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-binary-egXML-ab" source="#UND">
      <f name="strident">
        <binary value="true"/>
      </f>
      <f name="exclusive">
        <binary value="false"/>
      </f>
    </egXML>
  </exemplum>
  <remarks ident="binary-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The value attribute may take any value permitted for
  attributes of the W3C datatype Boolean: this includes for example 
the strings
  <code>true</code> or <code>1</code> which are
  equivalent. </p>
  </remarks>
  <remarks ident="binary-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>value</att> peut prendre n'importe quelle valeur acceptée pour les
                attributs de type booléen dans les recommandations du W3C : cela inclut par exemple
                les chaînes <code>true</code> ou <code>1</code> qui sont équivalentes. </p>
  </remarks>
  <remarks ident="binary-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該属性値は、W3Cのデータ型「論理値」になる。例えば、文字列
    <code>true</code>や、その同値である<code>1</code>をとる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#FSBI" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">binary value</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">이진 값</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">二元值</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">valeur binaire</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">valor binario</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">un valore binario</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-09-21" xml:lang="ja">二値</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification which can contain either
  of exactly two possible values.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">정확히 두 가지 가능한 값 중 하나를 포함할 수 있는 자질-값 명세에서 값의 부분을 표시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，可包含確切兩種可能值中的其中一種。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">二値として、素性値を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">représente la partie <q>valeur</q> d'une spécification
      trait-valeur qui peut contenir l'une ou l'autre des deux valeurs possibles.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que puede contener cualquier de los dos valores posibles.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che può contenere uno di soltanto due possibili valori.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies a binary value.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이진 값을 제시한다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個二元值</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">二値で値を示す。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">fournit une valeur binaire.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un valor binario</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un valore binario.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="binary-attr.value-remarks" versionDate="2013-12-21" xml:lang="en"><p>This attribute has a datatype of <ident type="datatype">teidata.truthValue</ident>, which
may be represented by the values <val>1</val> or
    <val>true</val>, or <val>0</val> or <val>false</val>.</p>
</remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="binary-attr.value-remarks" versionDate="2023-09-21" xml:lang="ja"><p>この属性は<ident type="datatype">teidata.truthValue</ident>のデータ型を持つ。
  その値は、<val>1</val>か<val>true</val>、あるいは<val>0</val>か<val>false</val>で表現される。</p>
</remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-binary-egXML-oa" source="#UND">
      <f name="strident">
        <binary value="true"/>
      </f>
      <f name="exclusive">
        <binary value="false"/>
      </f>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-binary-egXML-ab" source="#UND">
      <f name="strident">
        <binary value="true"/>
      </f>
      <f name="exclusive">
        <binary value="false"/>
      </f>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="binary-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The value attribute may take any value permitted for
  attributes of the W3C datatype Boolean: this includes for example 
the strings
  <code>true</code> or <code>1</code> which are
  equivalent. </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="binary-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>value</att> peut prendre n'importe quelle valeur acceptée pour les
                attributs de type booléen dans les recommandations du W3C : cela inclut par exemple
                les chaînes <code>true</code> ou <code>1</code> qui sont équivalentes. </p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="binary-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該属性値は、W3Cのデータ型「論理値」になる。例えば、文字列
    <code>true</code>や、その同値である<code>1</code>をとる。
    </p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSBI" type="div3"/>
  </listRef>
```

^b32

