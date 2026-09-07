---
type: representation
source-type: document
source: '[[00_sources/tei-p5-attref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 attRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/attRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# attRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3134. Git blob: `e0bba5078839cc4cfd400fecbcded8da08a2ce9c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-attRef" ident="attRef">
  <gloss versionDate="2005-04-13" xml:lang="en">attribute pointer</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">속성 포인터</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性指標</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">pointeur d'attribut</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">señalizador del atributo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">puntatore dell'attributo</gloss>
  <desc versionDate="2005-12-02" xml:lang="en">points to the definition of an attribute or group of attributes.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">속성 또는 속성의 그룹에 대한 정의를 가리킨다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到屬性或屬性群組的定義。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">1つまたは複数の属性の定義の場所を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">pointe vers la définition d'un attribut ou d'un groupe d'attributs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">señala a la definición de un atributo o grupo de atributos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rimanda alla definizione di un attributo o gruppo di attributi.</desc>
  <classes>
    <memberOf key="att.global"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="class">
      <desc versionDate="2013-11-16" xml:lang="en">the name of the attribute class</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attList org="choice">
      <attDef ident="name" validUntil="2026-11-13">
        <desc versionDate="2025-12-30" xml:lang="en">the identifier (<att>ident</att>) of the attribute being referred to</desc>
        <desc type="deprecationInfo" xml:lang="en" versionDate="2025-12-30">
          The <att>key</att> attribute is preferred over
          <att>name</att>, as the attribute being referred to is
          referenced by its <att>ident</att>, not its name (which
          might be different).
        </desc>
        <datatype><dataRef key="teidata.name"/></datatype>
      </attDef>
      <attDef ident="key">
        <desc versionDate="2025-12-30" xml:lang="en">the identifier (<att>ident</att>) of the attribute being referred to</desc>
        <datatype><dataRef key="teidata.name"/></datatype>
      </attDef>
    </attList>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attRef-egXML-cw" source="#UND">
      <attRef class="att.global" key="xml:id"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDmodules"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-04-13" xml:lang="en">attribute pointer</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">속성 포인터</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性指標</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">pointeur d'attribut</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">señalizador del atributo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">puntatore dell'attributo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-12-02" xml:lang="en">points to the definition of an attribute or group of attributes.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">속성 또는 속성의 그룹에 대한 정의를 가리킨다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到屬性或屬性群組的定義。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">1つまたは複数の属性の定義の場所を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers la définition d'un attribut ou d'un groupe d'attributs.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala a la definición de un atributo o grupo de atributos.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rimanda alla definizione di un attributo o gruppo di attributi.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
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
<desc versionDate="2013-11-16" xml:lang="en">the name of the attribute class</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2025-12-30" xml:lang="en">the identifier (<att>ident</att>) of the attribute being referred to</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc type="deprecationInfo" xml:lang="en" versionDate="2025-12-30">
          The <att>key</att> attribute is preferred over
          <att>name</att>, as the attribute being referred to is
          referenced by its <att>ident</att>, not its name (which
          might be different).
        </desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2025-12-30" xml:lang="en">the identifier (<att>ident</att>) of the attribute being referred to</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attRef-egXML-cw" source="#UND">
      <attRef class="att.global" key="xml:id"/>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDmodules"/>
  </listRef>
```

^b24

