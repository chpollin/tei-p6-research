---
type: representation
source-type: document
source: '[[00_sources/tei-p5-bicond-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 bicond
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/bicond.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# bicond

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4248. Git blob: `109ce6842aabf8b1aad346cf1649558369ec5b01`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-bicond" ident="bicond">
  <gloss versionDate="2005-01-14" xml:lang="en">bi-conditional feature-structure constraint</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">이중 조건 자질-구조 제약</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">雙條件功能結構限制</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">contrainte bi-conditionnelle de structure de traits</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">restricciones de estructura de rasgo bicondicional</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">vincolo di struttura di tratti bi-condizionato</gloss>
  <gloss versionDate="2023-09-21" xml:lang="ja">必要十分な素性構造の制約</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">defines a biconditional feature-structure constraint; both
consequent and antecedent are specified as feature structures or groups
of feature structures; the constraint is satisfied if both
subsume a given feature structure, or if both do not.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">이중 조건 자질-구조 제약을 정의한다; 전건과 후건 모두 자질 구조 또는 자질 구조 집합으로 명시된다; 전건과 후건 모두 주어진 자질 구조를 포섭하거나 둘 다 포섭하지 않는다면 이 제약은 만족된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個雙條件功能結構限制；結果和前提被指明為功能結構或功能結構群組；若兩者皆包含一個已知功能結構、或兩者皆不包含，則結果符合需求。</desc>
  <desc versionDate="2023-09-21" xml:lang="ja">素性構造の制約を必要十分条件として定義する。
    前提部と帰結部は、素性構造またはそのグループとして定義される。
    当該制約は、与えられた前提部と帰結部の素性構造が共に真であるか、またはともに偽である場合に、満たされる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit une contrainte bi-conditionnelle de structure
      de traits ; la conséquence et l'antécédent sont tous deux indiqués comme structures de
      traits ou comme groupes de structures de traits ; la contrainte est satisfaite si chacun des
      deux englobe une structure de traits donnée, ou si aucun ne le fait.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una restricción de estructura de rasgo bicondicional; tanto el resultante como el antecedente se especifican como estructuras de rasgos o grupos de estructuras de rasgos; la restricción se cumple si ambos se dan en la estructura de rasgo o si no se da ninguno de ellos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un vincolo della struttura di tratti bi-condizionato; sia il successivo che l'antecedente sono specificati come strutture di tratti o gruppi di strutture di tratti; il vincolo è soddisfatto se entrambi
    una data struttura di tratti, o se entrambi non mlo fanno.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
      <elementRef key="iff"/>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
    </sequence>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bicond-egXML-bg" source="#UND">
      <bicond>
        <fs>
          <f name="FOO">
            <symbol value="42"/>
          </f>
        </fs>
        <iff/>
        <fs>
          <f name="BAR">
            <binary value="true"/>
          </f>
        </fs>
      </bicond>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">bi-conditional feature-structure constraint</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">이중 조건 자질-구조 제약</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">雙條件功能結構限制</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contrainte bi-conditionnelle de structure de traits</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">restricciones de estructura de rasgo bicondicional</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">vincolo di struttura di tratti bi-condizionato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-09-21" xml:lang="ja">必要十分な素性構造の制約</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">defines a biconditional feature-structure constraint; both
consequent and antecedent are specified as feature structures or groups
of feature structures; the constraint is satisfied if both
subsume a given feature structure, or if both do not.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이중 조건 자질-구조 제약을 정의한다; 전건과 후건 모두 자질 구조 또는 자질 구조 집합으로 명시된다; 전건과 후건 모두 주어진 자질 구조를 포섭하거나 둘 다 포섭하지 않는다면 이 제약은 만족된다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個雙條件功能結構限制；結果和前提被指明為功能結構或功能結構群組；若兩者皆包含一個已知功能結構、或兩者皆不包含，則結果符合需求。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-09-21" xml:lang="ja">素性構造の制約を必要十分条件として定義する。
    前提部と帰結部は、素性構造またはそのグループとして定義される。
    当該制約は、与えられた前提部と帰結部の素性構造が共に真であるか、またはともに偽である場合に、満たされる。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit une contrainte bi-conditionnelle de structure
      de traits ; la conséquence et l'antécédent sont tous deux indiqués comme structures de
      traits ou comme groupes de structures de traits ; la contrainte est satisfaite si chacun des
      deux englobe une structure de traits donnée, ou si aucun ne le fait.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una restricción de estructura de rasgo bicondicional; tanto el resultante como el antecedente se especifican como estructuras de rasgos o grupos de estructuras de rasgos; la restricción se cumple si ambos se dan en la estructura de rasgo o si no se da ninguno de ellos.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un vincolo della struttura di tratti bi-condizionato; sia il successivo che l'antecedente sono specificati come strutture di tratti o gruppi di strutture di tratti; il vincolo è soddisfatto se entrambi
    una data struttura di tratti, o se entrambi non mlo fanno.</desc>
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
      <elementRef key="iff"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bicond-egXML-bg" source="#UND">
      <bicond>
        <fs>
          <f name="FOO">
            <symbol value="42"/>
          </f>
        </fs>
        <iff/>
        <fs>
          <f name="BAR">
            <binary value="true"/>
          </f>
        </fs>
      </bicond>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b18

