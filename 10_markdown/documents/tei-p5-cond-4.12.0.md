---
type: representation
source-type: document
source: '[[00_sources/tei-p5-cond-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 cond
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/cond.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# cond

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5045. Git blob: `5013cbbda42febc0e96dbf02998a7e7443483f52`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-cond" ident="cond">
  <gloss versionDate="2005-01-14" xml:lang="en">conditional feature-structure constraint</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">조건적 자질-구조 제약</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">條件功能結構限制</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">contrainte conditionnelle de structure de traits</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">restricciones de estructura de rasgo condicional</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">vincolo della struttura di tratti condizionato</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">条件付き素性構造制約</gloss>
  <desc versionDate="2007-07-13" xml:lang="en">defines a conditional feature-structure constraint; the consequent
and the antecedent are specified as feature structures or
feature-structure collections; the constraint is satisfied if both the
antecedent and the consequent subsume a given feature
structure, or if the antecedent does not.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">조건적 자질-구조 제약을 정의한다; 후건과 전건은 자질 구조 또는 자질-구조 집합으로 명시된다; 전건과 후건 모두 제시된 자질구조를 포섭하거나 전건이 포섭하지 않는다면 그 제약은 만족된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個條件功能結構限制；結果和前提被指明為功能結構或功能結構群組；若前提和結果皆包含一個已知功能結構、或前提不包含，則結果符合需求。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性構造の条件制約を定義する。前提部と帰結部は、素性構造として定義さ
  れている。前提部と帰結部が共に真であったとき、または前提部が偽であっ
  たときに、当該条件節は真となる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit une contrainte conditionnelle de structure de
      traits ; la conséquence et l'antécédent sont indiqués comme structures de traits ou comme
      groupes de structures de traits ; la contrainte est satisfaite si à la fois l'antécédent et
      la conséquence englobent une structure de traits donnée, ou si l'antécédent ne l'englobe
    pas</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una restricción de estructura de rasgo condicional; el resultante y el antecedente se especifican como estructuras de rasgo o grupos de estructuras de rasgo; la restricción se cumple tanto si tanto el antecedente como el resultante incluyen una estructura de rasgo dada, o si el antecedente no lo hace.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un vincolo della struttura di tratti condizionato; il successivo e l'antecedente sono specificati come strutture di tratti o gruppi di strutture di tratti; il vincolo è soddisfatto se entrambi
    l'antecedente e il successivo sussumono una data struttura di tratti, o se l'antecedente non lo fa..</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
      <elementRef key="then"/>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
    </sequence>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cond-egXML-uk" source="#UND">
      <cond>
        <fs>
          <f name="BAR">
            <symbol value="1"/>
          </f>
        </fs>
        <then/>
        <fs>
          <f name="SUBCAT">
            <binary value="false"/>
          </f>
        </fs>
      </cond>
    </egXML>
  </exemplum>
  <remarks ident="cond-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain an antecedent feature structure, an empty
<gi>then</gi> element, and a consequent feature structure.</p>
    <p/>
  </remarks>
  <remarks ident="cond-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une structure de traits précédente, un élément vide
                    <gi>then</gi> et une structure de traits suivante.</p>
  </remarks>
  <remarks ident="cond-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    内容として、前提部に素性構造、空要素<gi>then</gi>、帰結部に素性構
  造を持つかもしれない。
  </p>
    <p/>
  </remarks>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">conditional feature-structure constraint</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조건적 자질-구조 제약</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">條件功能結構限制</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contrainte conditionnelle de structure de traits</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">restricciones de estructura de rasgo condicional</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">vincolo della struttura di tratti condizionato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">条件付き素性構造制約</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-07-13" xml:lang="en">defines a conditional feature-structure constraint; the consequent
and the antecedent are specified as feature structures or
feature-structure collections; the constraint is satisfied if both the
antecedent and the consequent subsume a given feature
structure, or if the antecedent does not.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">조건적 자질-구조 제약을 정의한다; 후건과 전건은 자질 구조 또는 자질-구조 집합으로 명시된다; 전건과 후건 모두 제시된 자질구조를 포섭하거나 전건이 포섭하지 않는다면 그 제약은 만족된다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個條件功能結構限制；結果和前提被指明為功能結構或功能結構群組；若前提和結果皆包含一個已知功能結構、或前提不包含，則結果符合需求。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性構造の条件制約を定義する。前提部と帰結部は、素性構造として定義さ
  れている。前提部と帰結部が共に真であったとき、または前提部が偽であっ
  たときに、当該条件節は真となる。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit une contrainte conditionnelle de structure de
      traits ; la conséquence et l'antécédent sont indiqués comme structures de traits ou comme
      groupes de structures de traits ; la contrainte est satisfaite si à la fois l'antécédent et
      la conséquence englobent une structure de traits donnée, ou si l'antécédent ne l'englobe
    pas</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una restricción de estructura de rasgo condicional; el resultante y el antecedente se especifican como estructuras de rasgo o grupos de estructuras de rasgo; la restricción se cumple tanto si tanto el antecedente como el resultante incluyen una estructura de rasgo dada, o si el antecedente no lo hace.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un vincolo della struttura di tratti condizionato; il successivo e l'antecedente sono specificati come strutture di tratti o gruppi di strutture di tratti; il vincolo è soddisfatto se entrambi
    l'antecedente e il successivo sussumono una data struttura di tratti, o se l'antecedente non lo fa..</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
      <elementRef key="then"/>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cond-egXML-uk" source="#UND">
      <cond>
        <fs>
          <f name="BAR">
            <symbol value="1"/>
          </f>
        </fs>
        <then/>
        <fs>
          <f name="SUBCAT">
            <binary value="false"/>
          </f>
        </fs>
      </cond>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="cond-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain an antecedent feature structure, an empty
<gi>then</gi> element, and a consequent feature structure.</p>
    <p/>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="cond-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une structure de traits précédente, un élément vide
                    <gi>then</gi> et une structure de traits suivante.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="cond-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    内容として、前提部に素性構造、空要素<gi>then</gi>、帰結部に素性構
  造を持つかもしれない。
  </p>
    <p/>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b21

