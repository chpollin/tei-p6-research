---
type: representation
source-type: document
source: '[[00_sources/tei-p5-datatype-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 datatype
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/datatype.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# datatype

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7925. Git blob: `41501544fe36778e9127eb163d859b68c3488dfb`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-datatype" ident="datatype">
  <gloss versionDate="2007-06-12" xml:lang="en">datatype</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">type de données</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies the declared value for an attribute, by referring to
  any datatype defined by the chosen schema language.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">선택된 스키마 언어에 의해 정의된 데이터 유형을 참조함으로써, 속성에 대한 선언된 값을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指明屬性的公開屬性值，參照到任何所選擇的模型語言所定義的資料類型。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">属性値の型を、当該スキーマ中のデータ型を参照して示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">précise la valeur déclarée d'un attribut en
			faisant référence à un type de données défini dans le langage choisi pour le schéma.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el valor declarado de un atributo haciendo referencia a cualquier tipo de datos definido en el lenguaje elegido para el esquema.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica il valore dichiarato di un attributo facendo riferimento a un qualsiasi tipo di dati definito nel linguaggio scelto per lo schema.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
  </classes>
  <content>
    <alternate>
      <elementRef key="dataRef"/>
      <anyElement require="http://relaxng.org/ns/structure/1.0"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="minOccurs" mode="change">
      <desc versionDate="2020-02-05" xml:lang="en">indicates the minimum number of times this datatype may
      occur in an instance of the attribute being defined.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">정의되고 있는 속성 명시에서 발생할 수 있는 이 유형의 최소 횟수를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該資料類型在所定義的屬性說明中可能出現的最少次數
          。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">属性値としてとる当該データ型の値が出現する最小回数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le nombre minimum d'occurrences
					de ce type de données dans la spécification de l'attribut.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica il numero minimo di volte che questo tipo di dati può verificarsi nella definizione dell'attributo da definire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el mínimo número de veces que los tipo de datos pueden aparecer en la especificación del atributo que se define.</desc>
    </attDef>
    <attDef ident="maxOccurs" mode="change">
      <desc versionDate="2020-02-05" xml:lang="en">indicates the maximum number of times this datatype may
      occur in an instance of the attribute being defined.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">정의되고 있는 속성 명시에서 발생할 수 있는 이 유형의 최대 횟수를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該資料類型在所定義的屬性說明中可能出現的最多次數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該データ型が属性値として出現する最大回数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le nombre maximum d'occurrences
					de ce type de données dans la spécification de l'attribut.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica il numero massimo di volte che questo tipo di dati può verificarsi nella definizione dell'attributo da definire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el máximo número de veces que los tipo de datos pueden aparecer en la especificación del atributo que se define.</desc>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-yv" source="#UND">
      <datatype>
        <dataRef name="token"/>
      </datatype>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-mj" source="#UND">
      <datatype>
        <dataRef name="token"/>
      </datatype>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-yp" source="#UND">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">L'encodage de l'exemple suivant exige que l'attribut défini contienne au moins deux URIs
        dans ses valeurs, comme le cas de l'attribut <att>target</att> dans <gi>join</gi>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-bv" source="#UND">
      <datatype minOccurs="2" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-da" source="#UND">
      <datatype minOccurs="2" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-il" source="#UND">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>The encoding in the following example requires that the
    attribute being defined contain at least two URIs in its value, as
    is the case for the <att>target</att> attribute of
    <gi>join</gi>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-vb" source="#UND">
      <datatype minOccurs="2" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
    </egXML>
  </exemplum>
  <remarks ident="datatype-remarks" versionDate="2016-11-30" xml:lang="en">
    <p>In the TEI scheme, most datatypes are expressed using
    pre-defined TEI macros, which map a name in the form
    <code>teidata.xxxx</code> to a datatype defined by RELAX NG or the W3C Schema Language.</p>
  </remarks>
  <remarks ident="datatype-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans le schéma TEI, la plupart des types de données sont exprimées en utilisant des
                macros TEI prédéfinies, qui font correspondre un nom dans sa forme
                <code>teidata.xxxx</code> à un type de données définies en RELAX NG or XSD.</p>
  </remarks>
  <remarks ident="datatype-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p>
      TEIスキーマでは、殆どのデータ型はあらかじめ定義されたTEIマクロを使用することで表現される。このマクロは<code>teidata.xxxx</code>の形で示された名前を、RELAX NGまたはW3Cスキーマ言語により定義されたデータ型に対応づけている。
    </p>
  </remarks>
  <listRef>
    <ptr target="#DTYPES"/>
    <ptr target="#TDATT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">datatype</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">type de données</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the declared value for an attribute, by referring to
  any datatype defined by the chosen schema language.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">선택된 스키마 언어에 의해 정의된 데이터 유형을 참조함으로써, 속성에 대한 선언된 값을 명시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明屬性的公開屬性值，參照到任何所選擇的模型語言所定義的資料類型。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性値の型を、当該スキーマ中のデータ型を参照して示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise la valeur déclarée d'un attribut en
			faisant référence à un type de données défini dans le langage choisi pour le schéma.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el valor declarado de un atributo haciendo referencia a cualquier tipo de datos definido en el lenguaje elegido para el esquema.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il valore dichiarato di un attributo facendo riferimento a un qualsiasi tipo di dati definito nel linguaggio scelto per lo schema.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <elementRef key="dataRef"/>
      <anyElement require="http://relaxng.org/ns/structure/1.0"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2020-02-05" xml:lang="en">indicates the minimum number of times this datatype may
      occur in an instance of the attribute being defined.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">정의되고 있는 속성 명시에서 발생할 수 있는 이 유형의 최소 횟수를 나타낸다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該資料類型在所定義的屬性說明中可能出現的最少次數
          。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性値としてとる当該データ型の値が出現する最小回数を示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le nombre minimum d'occurrences
					de ce type de données dans la spécification de l'attribut.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica il numero minimo di volte che questo tipo di dati può verificarsi nella definizione dell'attributo da definire.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el mínimo número de veces que los tipo de datos pueden aparecer en la especificación del atributo que se define.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2020-02-05" xml:lang="en">indicates the maximum number of times this datatype may
      occur in an instance of the attribute being defined.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">정의되고 있는 속성 명시에서 발생할 수 있는 이 유형의 최대 횟수를 나타낸다.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該資料類型在所定義的屬性說明中可能出現的最多次數。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該データ型が属性値として出現する最大回数を示す。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le nombre maximum d'occurrences
					de ce type de données dans la spécification de l'attribut.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica il numero massimo di volte che questo tipo di dati può verificarsi nella definizione dell'attributo da definire.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el máximo número de veces que los tipo de datos pueden aparecer en la especificación del atributo que se define.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-yv" source="#UND">
      <datatype>
        <dataRef name="token"/>
      </datatype>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-mj" source="#UND">
      <datatype>
        <dataRef name="token"/>
      </datatype>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-yp" source="#UND">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">L'encodage de l'exemple suivant exige que l'attribut défini contienne au moins deux URIs
        dans ses valeurs, comme le cas de l'attribut <att>target</att> dans <gi>join</gi>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-bv" source="#UND">
      <datatype minOccurs="2" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-da" source="#UND">
      <datatype minOccurs="2" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-il" source="#UND">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <p>The encoding in the following example requires that the
    attribute being defined contain at least two URIs in its value, as
    is the case for the <att>target</att> attribute of
    <gi>join</gi>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-datatype-egXML-vb" source="#UND">
      <datatype minOccurs="2" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="datatype-remarks" versionDate="2016-11-30" xml:lang="en">
    <p>In the TEI scheme, most datatypes are expressed using
    pre-defined TEI macros, which map a name in the form
    <code>teidata.xxxx</code> to a datatype defined by RELAX NG or the W3C Schema Language.</p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="datatype-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans le schéma TEI, la plupart des types de données sont exprimées en utilisant des
                macros TEI prédéfinies, qui font correspondre un nom dans sa forme
                <code>teidata.xxxx</code> à un type de données définies en RELAX NG or XSD.</p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="datatype-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p>
      TEIスキーマでは、殆どのデータ型はあらかじめ定義されたTEIマクロを使用することで表現される。このマクロは<code>teidata.xxxx</code>の形で示された名前を、RELAX NGまたはW3Cスキーマ言語により定義されたデータ型に対応づけている。
    </p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DTYPES"/>
    <ptr target="#TDATT"/>
  </listRef>
```

^b36

