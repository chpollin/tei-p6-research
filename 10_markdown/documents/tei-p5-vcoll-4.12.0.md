---
type: representation
source-type: document
source: '[[00_sources/tei-p5-vcoll-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 vColl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/vColl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# vColl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9642. Git blob: `8db39eb81633001a5de55016a103dc5269355d26`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-vColl" ident="vColl">
  <gloss versionDate="2005-09-29" xml:lang="en">collection of values</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">값의 집합</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">值集合</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">collection de valeurs</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de valores</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">raccolta di valori</gloss>
  <desc versionDate="2005-09-29" xml:lang="en">represents the value part of a feature-value specification
  which contains multiple values organized as a set, bag, or list.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">집합, 다중집합 또는 목록으로 구성된 다중치를 포함하는 자질-값 명세에서 값의 부분을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含形成一組、群組或一列表的複合值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性値規定において、複数の値を、集合、バック、リストなどで表す、値の
  部分を示す。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient des valeurs multiples organisées comme un ensemble, un paquet ou une liste.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene valores múltiples organizados como un conjunto, o una lista, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene valori multipli organizzati in un insieme, borsa, o lista.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.complex"/>
  </classes>
  <content>
    
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="fs"/>
          <classRef key="model.featureVal.single"/>
          <elementRef key="vColl"/>
        </alternate>
      
    
  </content>
  <attList>
    <attDef ident="org" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">organization</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">organisation</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
      <desc versionDate="2005-09-29" xml:lang="en">indicates organization of given value or values as <!--
  singleton,--> set, bag or list.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">집합, 다중집합 또는 목록으로 주어진 값 또는 값들의 조직을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明一個或一個以上已知值的組成是一組、群組、或列表。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">付与された値、または、集合、バッグ、リストとしてある値の構造を示
      す。</desc>
      <desc versionDate="2009-04-16" xml:lang="fr">indique l'organisation de la ou des valeurs
          données sous forme d'ensemble, de paquet ou de liste.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la organización del valor o valores dados como conjunto o lista.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il tipo di organizzazione di un dato valore come insieme, borsa o lista.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="set">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the given values are organized as a set.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">주어진 값이 집합으로 조직된  었음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">指出已知值是以一組的形式組成。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indican que los valores dados están ordenados como un conjunto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">集合(順序なし、重複なし)としてある値を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que les valeurs données sont
organisées en ensemble.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che i valori dati sono organizzati in un insieme.</desc>
        </valItem>
        <valItem ident="bag">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the given values are organized as a
bag (multiset).</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">주어진 값이 다중집합으로 조직되었음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">指出已知值是以群組的形式組成。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que los valores dados están ordenados como una bolsa (conjunto múltiple).</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">バック(順序なし、重複あり)としてある値を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que les valeurs données sont
organisées en paquet (de plusieurs ensembles).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che i valori dati sono organizzati in una borsa (insieme multiplo).</desc>
        </valItem>
        <valItem ident="list">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the given values are organized as a
list.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">주어진 값이 목록으로 조직되었음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">指出已知值是以列表的形式組成。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indican que los valores dados están ordenados como una lista.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">リスト(順序あり、重複あり)としてある値を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que les valeurs données sont
organisées en liste.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che i valori dati sono organizzati secondo una lista.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-ls">
      <f name="name">
        <vColl>
          <string>Jean</string>
          <string>Luc</string>
          <string>Godard</string>
        </vColl>
      </f>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-tx">
      <f name="name">
        <vColl>
          <string>Jean</string>
          <string>Luc</string>
          <string>Godard</string>
        </vColl>
      </f>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-fe" source="#UND">
      <fs>
        <f name="lex">
          <symbol value="auxquels"/>
        </f>
        <f name="maf">
          <vColl org="list">
            <fs>
              <f name="cat">
                <symbol value="prep"/>
              </f>
            </fs>
            <fs>
              <f name="cat">
                <symbol value="pronoun"/>
              </f>
              <f name="kind">
                <symbol value="rel"/>
              </f>
              <f name="num">
                <symbol value="pl"/>
              </f>
              <f name="gender">
                <symbol value="masc"/>
              </f>
            </fs>
          </vColl>
        </f>
      </fs>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-cx">
      <f name="name">
        <vColl>
          <string>楊過</string>
          <string>小龍女</string>
          <string>李莫愁</string>
        </vColl>
      </f>
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-sp" source="#UND">
      <fs>
        <f name="lex">
          <symbol value="auxquels"/>
        </f>
        <f name="maf">
          <vColl org="list">
            <fs>
              <f name="cat">
                <symbol value="prep"/>
              </f>
            </fs>
            <fs>
              <f name="cat">
                <symbol value="pronoun"/>
              </f>
              <f name="kind">
                <symbol value="rel"/>
              </f>
              <f name="num">
                <symbol value="pl"/>
              </f>
              <f name="gender">
                <symbol value="masc"/>
              </f>
            </fs>
          </vColl>
        </f>
      </fs>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FSSS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-09-29" xml:lang="en">collection of values</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">값의 집합</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">值集合</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">collection de valeurs</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de valores</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">raccolta di valori</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-09-29" xml:lang="en">represents the value part of a feature-value specification
  which contains multiple values organized as a set, bag, or list.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">집합, 다중집합 또는 목록으로 구성된 다중치를 포함하는 자질-값 명세에서 값의 부분을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含形成一組、群組或一列表的複合值。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性値規定において、複数の値を、集合、バック、リストなどで表す、値の
  部分を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient des valeurs multiples organisées comme un ensemble, un paquet ou une liste.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene valores múltiples organizados como un conjunto, o una lista, etc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene valori multipli organizzati in un insieme, borsa, o lista.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.complex"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="fs"/>
          <classRef key="model.featureVal.single"/>
          <elementRef key="vColl"/>
        </alternate>
      
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">organization</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">organisation</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-09-29" xml:lang="en">indicates organization of given value or values as <!--
  singleton,--> set, bag or list.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">집합, 다중집합 또는 목록으로 주어진 값 또는 값들의 조직을 나타낸다.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明一個或一個以上已知值的組成是一組、群組、或列表。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">付与された値、または、集合、バッグ、リストとしてある値の構造を示
      す。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">indique l'organisation de la ou des valeurs
          données sous forme d'ensemble, de paquet ou de liste.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la organización del valor o valores dados como conjunto o lista.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il tipo di organizzazione di un dato valore come insieme, borsa o lista.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="set">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the given values are organized as a set.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">주어진 값이 집합으로 조직된  었음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">指出已知值是以一組的形式組成。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indican que los valores dados están ordenados como un conjunto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">集合(順序なし、重複なし)としてある値を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que les valeurs données sont
organisées en ensemble.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che i valori dati sono organizzati in un insieme.</desc>
        </valItem>
        <valItem ident="bag">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the given values are organized as a
bag (multiset).</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">주어진 값이 다중집합으로 조직되었음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">指出已知值是以群組的形式組成。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que los valores dados están ordenados como una bolsa (conjunto múltiple).</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">バック(順序なし、重複あり)としてある値を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que les valeurs données sont
organisées en paquet (de plusieurs ensembles).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che i valori dati sono organizzati in una borsa (insieme multiplo).</desc>
        </valItem>
        <valItem ident="list">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the given values are organized as a
list.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">주어진 값이 목록으로 조직되었음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">指出已知值是以列表的形式組成。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indican que los valores dados están ordenados como una lista.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">リスト(順序あり、重複あり)としてある値を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que les valeurs données sont
organisées en liste.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che i valori dati sono organizzati secondo una lista.</desc>
        </valItem>
      </valList>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-ls">
      <f name="name">
        <vColl>
          <string>Jean</string>
          <string>Luc</string>
          <string>Godard</string>
        </vColl>
      </f>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-tx">
      <f name="name">
        <vColl>
          <string>Jean</string>
          <string>Luc</string>
          <string>Godard</string>
        </vColl>
      </f>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-fe" source="#UND">
      <fs>
        <f name="lex">
          <symbol value="auxquels"/>
        </f>
        <f name="maf">
          <vColl org="list">
            <fs>
              <f name="cat">
                <symbol value="prep"/>
              </f>
            </fs>
            <fs>
              <f name="cat">
                <symbol value="pronoun"/>
              </f>
              <f name="kind">
                <symbol value="rel"/>
              </f>
              <f name="num">
                <symbol value="pl"/>
              </f>
              <f name="gender">
                <symbol value="masc"/>
              </f>
            </fs>
          </vColl>
        </f>
      </fs>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-cx">
      <f name="name">
        <vColl>
          <string>楊過</string>
          <string>小龍女</string>
          <string>李莫愁</string>
        </vColl>
      </f>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vColl-egXML-sp" source="#UND">
      <fs>
        <f name="lex">
          <symbol value="auxquels"/>
        </f>
        <f name="maf">
          <vColl org="list">
            <fs>
              <f name="cat">
                <symbol value="prep"/>
              </f>
            </fs>
            <fs>
              <f name="cat">
                <symbol value="pronoun"/>
              </f>
              <f name="kind">
                <symbol value="rel"/>
              </f>
              <f name="num">
                <symbol value="pl"/>
              </f>
              <f name="gender">
                <symbol value="masc"/>
              </f>
            </fs>
          </vColl>
        </f>
      </fs>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSSS"/>
  </listRef>
```

^b35

