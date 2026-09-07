---
type: representation
source-type: document
source: '[[00_sources/tei-p5-numeric-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 numeric
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/numeric.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# numeric

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8311. Git blob: `fc6fdd83a9660141f43679a3f111600792d3185a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-numeric" ident="numeric">
  <gloss versionDate="2007-07-04" xml:lang="en">numeric value</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">수치</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">數值</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">valeur numérique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">valor numérico</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">un valore numerico</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification
  which contains a numeric value or range.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수치 또는 숫자 범위를 포함하는 자질-값 명세에서 값의 부분을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含一個數值或數值範圍。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性値定義における値を示す。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient une valeur ou une série numériques.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene un valor numérico o de intervalo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene un valore o una gamma di valori numerici.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="value" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">supplies a lower bound for the numeric value represented,
      and also (if <att>max</att> is not supplied) its upper bound.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">표시된 수치의 하한값과 (<att>max</att>이 제시되지 않았다면) 그 상한값을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供所表示數值的底限，以及 (若無標明<att>max</att>) 其上限。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">与えられている数値の下限を示す。または、(属性<att>max</att>が付
      与されていない場合には)値の上限を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne une limite inférieure pour la valeur
          numérique représentée et aussi (si<att>max</att> n'est pas donné) sa limite supérieure.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el límite inferior para el valor numérico representado, y también (si no se proporciona <att>max</att>) su límite superior.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un limite inferiore al valore numerico rappresentato e anche (qualora l'attributo <att>max</att> (maz) non sia presente) il limite superiore.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="max" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">supplies an upper bound for the numeric value represented.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">표시된 수치에 대한 상한값을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供所表示數值的上限。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">与えられている数値の上限を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne une limite supérieure pour la valeur
          numérique représentée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el límite superior para el valor numérico representado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un superiore inferiore al valore numerico rappresentato.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="trunc" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies whether the value represented should be
	  truncated to give an integer value.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">표시된 값이 정수 표현을 위해 끝수를 버린 것인지의 여부를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明是否應將該數值四捨五入而取得一個整數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該数値が整数値へ丸められるかどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie si la valeur représentée doit être
          tronquée pour donner un nombre entier.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica si el valor representado debe ser truncado para dar un valor entero.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se il valore rappresentato debba essere troncato per ottenere un numero intero.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-rl" source="#UND">
      <numeric value="42"/>
    </egXML>
    <p>This represents the numeric value 42.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-gc" source="#UND">
      <numeric value="42"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Ceci représente la valeur numérique 42.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-lj" source="#UND">
      <numeric value="42.45" max="50" trunc="true"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Ceci représente n'importe laquelle des neuf valeurs des entiers possibles entre 42 et 50
        inclus. Si l'attribut <att> trunc</att> avait eu la valeur FALSE, cet exemple aurait
        représenté n'importe lequel des nombres infinis ayant des valeurs numériques comprises entre
        42.45 et 50.0</p>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-gr" source="#UND">
      <numeric value="42"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-ti" source="#UND">
      <numeric value="42.45" max="50" trunc="true"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-ve" source="#UND">
      <numeric value="42.45" max="50" trunc="true"/>
    </egXML>
    <p>This represents any of the nine possible integer values between 42 and 50
  inclusive. If the <att>trunc</att> attribute had the value FALSE,
  this example would represent any of the infinite number of numeric values between 42.45 and
  50.0</p>
  </exemplum>
  <remarks ident="numeric-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>It is an error to supply the <att>max</att> attribute
in the absence of a value for the <att>value</att> attribute.</p>
  </remarks>
  <remarks ident="numeric-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>C'est une erreur d'utiliser l'attribut <att>max</att> s'il n'y a pas de valeur pour
                l'attribut <att>value</att>.</p>
  </remarks>
  <remarks ident="numeric-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>value</att>に値がないところで属性<att>max</att>があるとエ
    ラーになる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#FSSY" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">numeric value</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">수치</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">數值</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">valeur numérique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">valor numérico</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">un valore numerico</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification
  which contains a numeric value or range.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수치 또는 숫자 범위를 포함하는 자질-값 명세에서 값의 부분을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含一個數值或數值範圍。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性値定義における値を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient une valeur ou une série numériques.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene un valor numérico o de intervalo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene un valore o una gamma di valori numerici.</desc>
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
<desc versionDate="2005-01-14" xml:lang="en">supplies a lower bound for the numeric value represented,
      and also (if <att>max</att> is not supplied) its upper bound.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표시된 수치의 하한값과 (<att>max</att>이 제시되지 않았다면) 그 상한값을 제시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供所表示數值的底限，以及 (若無標明<att>max</att>) 其上限。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">与えられている数値の下限を示す。または、(属性<att>max</att>が付
      与されていない場合には)値の上限を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne une limite inférieure pour la valeur
          numérique représentée et aussi (si<att>max</att> n'est pas donné) sa limite supérieure.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el límite inferior para el valor numérico representado, y también (si no se proporciona <att>max</att>) su límite superior.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un limite inferiore al valore numerico rappresentato e anche (qualora l'attributo <att>max</att> (maz) non sia presente) il limite superiore.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies an upper bound for the numeric value represented.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표시된 수치에 대한 상한값을 제시한다.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供所表示數值的上限。</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">与えられている数値の上限を示す。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne une limite supérieure pour la valeur
          numérique représentée.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el límite superior para el valor numérico representado.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un superiore inferiore al valore numerico rappresentato.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies whether the value represented should be
	  truncated to give an integer value.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표시된 값이 정수 표현을 위해 끝수를 버린 것인지의 여부를 명시한다.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明是否應將該數值四捨五入而取得一個整數。</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該数値が整数値へ丸められるかどうかを示す。</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie si la valeur représentée doit être
          tronquée pour donner un nombre entier.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica si el valor representado debe ser truncado para dar un valor entero.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se il valore rappresentato debba essere troncato per ottenere un numero intero.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-rl" source="#UND">
      <numeric value="42"/>
    </egXML>
    <p>This represents the numeric value 42.</p>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-gc" source="#UND">
      <numeric value="42"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Ceci représente la valeur numérique 42.</p>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-lj" source="#UND">
      <numeric value="42.45" max="50" trunc="true"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Ceci représente n'importe laquelle des neuf valeurs des entiers possibles entre 42 et 50
        inclus. Si l'attribut <att> trunc</att> avait eu la valeur FALSE, cet exemple aurait
        représenté n'importe lequel des nombres infinis ayant des valeurs numériques comprises entre
        42.45 et 50.0</p>
  </exemplum>
```

^b42

### Block 43

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-gr" source="#UND">
      <numeric value="42"/>
    </egXML>
  </exemplum>
```

^b43

### Block 44

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-ti" source="#UND">
      <numeric value="42.45" max="50" trunc="true"/>
    </egXML>
  </exemplum>
```

^b44

### Block 45

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-numeric-egXML-ve" source="#UND">
      <numeric value="42.45" max="50" trunc="true"/>
    </egXML>
    <p>This represents any of the nine possible integer values between 42 and 50
  inclusive. If the <att>trunc</att> attribute had the value FALSE,
  this example would represent any of the infinite number of numeric values between 42.45 and
  50.0</p>
  </exemplum>
```

^b45

### Block 46

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="numeric-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>It is an error to supply the <att>max</att> attribute
in the absence of a value for the <att>value</att> attribute.</p>
  </remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="numeric-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>C'est une erreur d'utiliser l'attribut <att>max</att> s'il n'y a pas de valeur pour
                l'attribut <att>value</att>.</p>
  </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="numeric-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>value</att>に値がないところで属性<att>max</att>があるとエ
    ラーになる。
    </p>
  </remarks>
```

^b48

### Block 49

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSSY" type="div3"/>
  </listRef>
```

^b49

