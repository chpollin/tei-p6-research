---
type: representation
source-type: document
source: '[[00_sources/tei-p5-altgrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 altGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/altGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# altGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9443. Git blob: `2ea69431d4f6fe1189de7e58ef0c5f6d00cfba5b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="linking" xml:id="gi-altGrp" ident="altGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">alternation group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">교체군</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">替換群組</gloss>
  <gloss versionDate="2009-10-05" xml:lang="fr">groupe d'alternatives</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de alternancia</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di alternanza</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">代替選択肢グループ</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups a collection of <gi>alt</gi> elements and possibly pointers.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">교체 요소 및 가능한 포인터의 집합군</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一群替換元素和可能指標。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素altまたはポインタ要素ptrをまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe une collection d'éléments <gi>alt</gi> et,
        éventuellement, de pointeurs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa un conjunto de elementos <gi>alt</gi> y de
        eventuales indicadores.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa un insieme di elementi <gi>alt</gi> ed
        eventuali puntatori</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.pointing.group"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    <sequence>
    <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="alt"/>
      <elementRef key="ptr"/>
    </alternate>  
    </sequence>
  </content>
  <attList>
    <attDef ident="mode" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">states whether the alternations gathered in this collection are exclusive or
                inclusive.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 집합에 모아진 교체의 배타적 또는 총괄적 여부를 진술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明在此集合中的替換物件是專有的或通用的。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素でまとめられたものの、選択度を示す。</desc>
      <desc versionDate="2009-10-06" xml:lang="fr">établit si les alternatives rassemblées dans
                cette collection sont exclusives ou non.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">declara si las alternativas contenidas en el
                conjunto son exclusivas o inclusivas.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">dichiara se le alternative contenute
                nell'insieme sono esclusive o inclusive</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>excl</defaultVal>
      <valList type="closed">
        <valItem ident="excl">
          <gloss versionDate="2007-07-04" xml:lang="en">exclusive</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">배타적</gloss>
          <gloss versionDate="2009-10-05" xml:lang="fr">exclusif</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">esclusivo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">indica que la alternancia es
                        exclusiva, es decir, que aparece sólo una de las posibles alternativas.</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">排他的</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the alternation is exclusive, i.e. that at most one of the
                        alternatives occurs.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">교체가 배타적임을 나타낸다. 즉, 기껏해야 교체집합 중 하나가
                        발생한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">替換物件是專有的，例如最多只出現一個替換。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que la alternancia es exclusiva,
                        es decir aquella en que como máximo unade las alternativas ocurre.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">高々ひとつしか選択できない。</desc>
          <desc versionDate="2009-10-05" xml:lang="fr">indique que l'alternative est
                        exclusive, c'est-à-dire qu'une seule des alternatives proposées est
                        possible.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che l'alternanza è esclusiva,
                        cioè che compare solo una delle possibili alternative</desc>
        </valItem>
        <valItem ident="incl">
          <gloss versionDate="2007-07-04" xml:lang="en">inclusive</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">총괄적</gloss>
          <gloss versionDate="2009-10-05" xml:lang="fr">non exclusif</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">inclusivo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">indica que la alternancia no es
                        exclusiva, es decir, que pueden aparecer una o más de las posibles
                        alternativas.</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">複数可</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the alternation is not exclusive, i.e. that one or more of
                        the alternatives occur.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">교체가 배타적이 아님을 표시한다. 즉, 교체집합 중 하나 이상이
                        발생한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">替換物件不是專有的，例如出現一個或多個替換。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que la alternancia no es
                        exclusiva, es decir que ocurren una o más de las alternativas.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">複数を選択できる。</desc>
          <desc versionDate="2009-10-06" xml:lang="fr">indique que l'alternative n'est pas
                        exclusive, c'est-à-dire qu'une alternative au moins est vraie.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che l'alternanza non è
                        esclusiva, cioè che possono comparire più alternative</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-dh" source="#UND">
      <altGrp mode="excl">
        <alt target="#dm #lt #bb" weights="0.5 0.25 0.25"/>
        <alt target="#rl #db" weights="0.5 0.5"/>
      </altGrp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-vy" source="#UND">
      <altGrp mode="excl">
        <alt target="#fr_dm #fr_lt #fr_bb" weights="0.5 0.25 0.25"/>
        <alt target="#fr_rl #fr_db" weights="0.5 0.5"/>
      </altGrp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-cm" source="#UND">
      <altGrp mode="incl">
        <alt target="#fr_dm #fr_rl" weights="0.90 0.90"/>
        <alt target="#fr_lt #fr_rl" weights="0.5 0.5"/>
        <alt target="#fr_bb #fr_rl" weights="0.5 0.5"/>
        <alt target="#fr_dm #fr_db" weights="0.10 0.10"/>
        <alt target="#fr_lt #fr_db" weights="0.45 0.90"/>
        <alt target="#fr_bb #fr_db" weights="0.45 0.90"/>
      </altGrp>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-qw" source="#UND">
      <altGrp mode="incl">
        <alt target="#dm #rl" weights="0.90 0.90"/>
        <alt target="#lt #rl" weights="0.5 0.5"/>
        <alt target="#bb #rl" weights="0.5 0.5"/>
        <alt target="#dm #db" weights="0.10 0.10"/>
        <alt target="#lt #db" weights="0.45 0.90"/>
        <alt target="#bb #db" weights="0.45 0.90"/>
      </altGrp>
    </egXML>
  </exemplum>
  <remarks ident="altGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Any number of alternations, pointers or extended pointers.</p>
  </remarks>
  <remarks ident="altGrp-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p rend="dataDesc">Un nombre quelconque d'éléments alternatifs, de pointeurs et de pointeurs
            étendus.</p>
  </remarks>
  <remarks ident="altGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 任意数の選択肢、ポインタ、拡張ポインタを示す。 </p>
  </remarks>
  <listRef>
    <ptr target="#SAAT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">alternation group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">교체군</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">替換群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-10-05" xml:lang="fr">groupe d'alternatives</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de alternancia</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di alternanza</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">代替選択肢グループ</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups a collection of <gi>alt</gi> elements and possibly pointers.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">교체 요소 및 가능한 포인터의 집합군</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一群替換元素和可能指標。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素altまたはポインタ要素ptrをまとめる。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe une collection d'éléments <gi>alt</gi> et,
        éventuellement, de pointeurs.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa un conjunto de elementos <gi>alt</gi> y de
        eventuales indicadores.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa un insieme di elementi <gi>alt</gi> ed
        eventuali puntatori</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.pointing.group"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
    <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="alt"/>
      <elementRef key="ptr"/>
    </alternate>  
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">states whether the alternations gathered in this collection are exclusive or
                inclusive.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 집합에 모아진 교체의 배타적 또는 총괄적 여부를 진술한다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明在此集合中的替換物件是專有的或通用的。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素でまとめられたものの、選択度を示す。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-10-06" xml:lang="fr">établit si les alternatives rassemblées dans
                cette collection sont exclusives ou non.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">declara si las alternativas contenidas en el
                conjunto son exclusivas o inclusivas.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">dichiara se le alternative contenute
                nell'insieme sono esclusive o inclusive</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>excl</defaultVal>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="excl">
          <gloss versionDate="2007-07-04" xml:lang="en">exclusive</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">배타적</gloss>
          <gloss versionDate="2009-10-05" xml:lang="fr">exclusif</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">esclusivo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">indica que la alternancia es
                        exclusiva, es decir, que aparece sólo una de las posibles alternativas.</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">排他的</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the alternation is exclusive, i.e. that at most one of the
                        alternatives occurs.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">교체가 배타적임을 나타낸다. 즉, 기껏해야 교체집합 중 하나가
                        발생한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">替換物件是專有的，例如最多只出現一個替換。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que la alternancia es exclusiva,
                        es decir aquella en que como máximo unade las alternativas ocurre.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">高々ひとつしか選択できない。</desc>
          <desc versionDate="2009-10-05" xml:lang="fr">indique que l'alternative est
                        exclusive, c'est-à-dire qu'une seule des alternatives proposées est
                        possible.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che l'alternanza è esclusiva,
                        cioè che compare solo una delle possibili alternative</desc>
        </valItem>
        <valItem ident="incl">
          <gloss versionDate="2007-07-04" xml:lang="en">inclusive</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">총괄적</gloss>
          <gloss versionDate="2009-10-05" xml:lang="fr">non exclusif</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">inclusivo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">indica que la alternancia no es
                        exclusiva, es decir, que pueden aparecer una o más de las posibles
                        alternativas.</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">複数可</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">indicates that the alternation is not exclusive, i.e. that one or more of
                        the alternatives occur.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">교체가 배타적이 아님을 표시한다. 즉, 교체집합 중 하나 이상이
                        발생한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">替換物件不是專有的，例如出現一個或多個替換。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que la alternancia no es
                        exclusiva, es decir que ocurren una o más de las alternativas.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">複数を選択できる。</desc>
          <desc versionDate="2009-10-06" xml:lang="fr">indique que l'alternative n'est pas
                        exclusive, c'est-à-dire qu'une alternative au moins est vraie.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che l'alternanza non è
                        esclusiva, cioè che possono comparire più alternative</desc>
        </valItem>
      </valList>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-dh" source="#UND">
      <altGrp mode="excl">
        <alt target="#dm #lt #bb" weights="0.5 0.25 0.25"/>
        <alt target="#rl #db" weights="0.5 0.5"/>
      </altGrp>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-vy" source="#UND">
      <altGrp mode="excl">
        <alt target="#fr_dm #fr_lt #fr_bb" weights="0.5 0.25 0.25"/>
        <alt target="#fr_rl #fr_db" weights="0.5 0.5"/>
      </altGrp>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-cm" source="#UND">
      <altGrp mode="incl">
        <alt target="#fr_dm #fr_rl" weights="0.90 0.90"/>
        <alt target="#fr_lt #fr_rl" weights="0.5 0.5"/>
        <alt target="#fr_bb #fr_rl" weights="0.5 0.5"/>
        <alt target="#fr_dm #fr_db" weights="0.10 0.10"/>
        <alt target="#fr_lt #fr_db" weights="0.45 0.90"/>
        <alt target="#fr_bb #fr_db" weights="0.45 0.90"/>
      </altGrp>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-altGrp-egXML-qw" source="#UND">
      <altGrp mode="incl">
        <alt target="#dm #rl" weights="0.90 0.90"/>
        <alt target="#lt #rl" weights="0.5 0.5"/>
        <alt target="#bb #rl" weights="0.5 0.5"/>
        <alt target="#dm #db" weights="0.10 0.10"/>
        <alt target="#lt #db" weights="0.45 0.90"/>
        <alt target="#bb #db" weights="0.45 0.90"/>
      </altGrp>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="altGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Any number of alternations, pointers or extended pointers.</p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="altGrp-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p rend="dataDesc">Un nombre quelconque d'éléments alternatifs, de pointeurs et de pointeurs
            étendus.</p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="altGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 任意数の選択肢、ポインタ、拡張ポインタを示す。 </p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SAAT"/>
  </listRef>
```

^b34

