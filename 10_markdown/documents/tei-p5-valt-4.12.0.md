---
type: representation
source-type: document
source: '[[00_sources/tei-p5-valt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 vAlt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/vAlt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# vAlt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3178. Git blob: `6ff97c714811ca5314f823d6862060eca9361480`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-vAlt" ident="vAlt">
  <gloss versionDate="2007-07-05" xml:lang="en">value alternation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">값 교체</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">替換值</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">valeur alternative</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">alternancia de valor</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">un'alterazione del valore</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification
  which contains a set of values, only one of which can be valid.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">자질-값 명세의 값 부분으로 값은 집합이다. 그 중 단 하나만 유효한 값이다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含一組值，僅其中一個得為有效值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性値規定において、妥当なひとつの値を表す、値の部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient un jeu de valeurs, dont une seule peut être valide</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene un conjunto de valores, de los cuales sólo uno puede ser válido.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene un insieme di valori, dei quali uno solo può essere valido.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
  <content>
    <sequence>
      
        <classRef key="model.featureVal"/>
      
      
        <classRef key="model.featureVal" minOccurs="1" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vAlt-egXML-ea" source="#UND">
      <f name="gender">
        <vAlt>
          <symbol value="masculine"/>
          <symbol value="neuter"/>
          <symbol value="feminine"/>
        </vAlt>
      </f>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vAlt-egXML-od" source="#UND">
      <f name="gender">
        <vAlt>
          <symbol value="masculine"/>
          <symbol value="neuter"/>
          <symbol value="feminine"/>
        </vAlt>
      </f>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FVALT" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-05" xml:lang="en">value alternation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">값 교체</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">替換值</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">valeur alternative</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">alternancia de valor</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">un'alterazione del valore</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents the value part of a feature-value specification
  which contains a set of values, only one of which can be valid.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질-값 명세의 값 부분으로 값은 집합이다. 그 중 단 하나만 유효한 값이다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，包含一組值，僅其中一個得為有效值。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性値規定において、妥当なひとつの値を表す、値の部分を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui contient un jeu de valeurs, dont une seule peut être valide</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que contiene un conjunto de valores, de los cuales sólo uno puede ser válido.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che contiene un insieme di valori, dei quali uno solo può essere valido.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <classRef key="model.featureVal"/>
      
      
        <classRef key="model.featureVal" minOccurs="1" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vAlt-egXML-ea" source="#UND">
      <f name="gender">
        <vAlt>
          <symbol value="masculine"/>
          <symbol value="neuter"/>
          <symbol value="feminine"/>
        </vAlt>
      </f>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vAlt-egXML-od" source="#UND">
      <f name="gender">
        <vAlt>
          <symbol value="masculine"/>
          <symbol value="neuter"/>
          <symbol value="feminine"/>
        </vAlt>
      </f>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FVALT" type="div3"/>
  </listRef>
```

^b18

