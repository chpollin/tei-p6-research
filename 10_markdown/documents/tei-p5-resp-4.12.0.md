---
type: representation
source-type: document
source: '[[00_sources/tei-p5-resp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 resp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/resp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# resp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5149. Git blob: `e73e240c5a3a395c6afc96c3b0fa4674134f9a7e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-resp" ident="resp">
  <gloss versionDate="2007-07-04" xml:lang="en">responsibility</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">책임성</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">responsabilidad</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">responsabilité</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">responsabilità</gloss>
  <gloss versionDate="2017-06-04" xml:lang="de">Verantwortlichkeit</gloss>
  <desc versionDate="2011-11-16" xml:lang="en">contains a phrase describing the nature of a person's intellectual responsibility, or an organization's role in the production or distribution of a work.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 지적 책임성에 관한 특성을 기술하는 구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個詞彙，來描述個人智慧責任的類型。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物の知的責任の性質を表す一節を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une expression décrivant la nature de la responsabilité intellectuelle d'une personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un sintagma que describe la naturaleza de la responsabilidad intelectual de una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una frase che descrive la natura della responsabilità intellettuale di una persona.</desc>
  <desc versionDate="2017-06-04" xml:lang="de">enthält eine Phrase, die die Art der intellektuellen Verantwortung einer Person oder die Rolle einer Organisation bei der Herstellung oder Distribution eines Werkes beschreibt.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-resp-egXML-yc">
      <respStmt>
        <resp ref="http://id.loc.gov/vocabulary/relators/com.html">compiler</resp>
        <name>Edward Child</name>
      </respStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-resp-egXML-my">
      <respStmt>
        <resp>compilateur</resp>
        <name>Edward Child</name>
      </respStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-resp-egXML-ve">
      <respStmt>
        <resp>編輯</resp>
        <name>林偉</name>
      </respStmt>
    </egXML>
  </exemplum>
  <remarks ident="resp-remarks" versionDate="2016-04-01" xml:lang="en">
    <p>The attribute <att>ref</att>, inherited from the class <ident type="class">att.canonical</ident> may be used to indicate the kind of responsibility in a normalized
      form by referring directly to a
      standardized list of responsibility types, such as that maintained by a naming authority, for
      example the list maintained at <ptr target="http://www.loc.gov/marc/relators/relacode.html"/>
      for bibliographic usage.</p>
  </remarks>
  <remarks ident="resp-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>Les attributs <att>key</att> or <att>ref</att>, issus de la classe <ident type="class">att.canonical</ident>, peuvent être utilisés pour indiquer le type de responsabilité sous
      une forme normalisée, en faisant référence directement (par l'utilisation de <att>ref</att>)
      ou indirectement (par l'utilisation de <att>key</att>) à une liste normalisée contenant des types de
      responsabilité, comme celle qui est maintenue par une autorité de nommage, par exemple la
      liste <ptr target="http://www.loc.gov/marc/relators/relacode.html"/> à usage bibliographique.
    </p>
  </remarks>
  <remarks ident="resp-remarks" versionDate="2017-06-04" xml:lang="de">
    <p>Das <att>ref</att>-Attribut, das aus der Klasse <ident type="class">att.canonical</ident>
      vererbt wird, kann benutzt werden, um die Art der Verantwortlichkeit in normalisierter Form zu
      beschreiben. Es verweist direkt auf eine standardisierte Liste von Verantwortlichkeitstypen, wie
      sie z. B. in Normdatensätzen gepflegt werden, wie zum Beispiel folgende Liste für
      bibliografische Zwecke: <ptr target="http://www.loc.gov/marc/relators/relacode.html"/>.</p>
  </remarks>
  <listRef>
    <ptr target="#COBICOR"/>
    <ptr target="#HD21"/>
    <ptr target="#HD22"/>
    <ptr target="#HD26"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">responsibility</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">책임성</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">responsabilidad</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">responsabilité</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">responsabilità</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-04" xml:lang="de">Verantwortlichkeit</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-16" xml:lang="en">contains a phrase describing the nature of a person's intellectual responsibility, or an organization's role in the production or distribution of a work.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 지적 책임성에 관한 특성을 기술하는 구를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個詞彙，來描述個人智慧責任的類型。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物の知的責任の性質を表す一節を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une expression décrivant la nature de la responsabilité intellectuelle d'une personne.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un sintagma que describe la naturaleza de la responsabilidad intelectual de una persona.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una frase che descrive la natura della responsabilità intellettuale di una persona.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-04" xml:lang="de">enthält eine Phrase, die die Art der intellektuellen Verantwortung einer Person oder die Rolle einer Organisation bei der Herstellung oder Distribution eines Werkes beschreibt.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-resp-egXML-yc">
      <respStmt>
        <resp ref="http://id.loc.gov/vocabulary/relators/com.html">compiler</resp>
        <name>Edward Child</name>
      </respStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-resp-egXML-my">
      <respStmt>
        <resp>compilateur</resp>
        <name>Edward Child</name>
      </respStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-resp-egXML-ve">
      <respStmt>
        <resp>編輯</resp>
        <name>林偉</name>
      </respStmt>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="resp-remarks" versionDate="2016-04-01" xml:lang="en">
    <p>The attribute <att>ref</att>, inherited from the class <ident type="class">att.canonical</ident> may be used to indicate the kind of responsibility in a normalized
      form by referring directly to a
      standardized list of responsibility types, such as that maintained by a naming authority, for
      example the list maintained at <ptr target="http://www.loc.gov/marc/relators/relacode.html"/>
      for bibliographic usage.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="resp-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>Les attributs <att>key</att> or <att>ref</att>, issus de la classe <ident type="class">att.canonical</ident>, peuvent être utilisés pour indiquer le type de responsabilité sous
      une forme normalisée, en faisant référence directement (par l'utilisation de <att>ref</att>)
      ou indirectement (par l'utilisation de <att>key</att>) à une liste normalisée contenant des types de
      responsabilité, comme celle qui est maintenue par une autorité de nommage, par exemple la
      liste <ptr target="http://www.loc.gov/marc/relators/relacode.html"/> à usage bibliographique.
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="resp-remarks" versionDate="2017-06-04" xml:lang="de">
    <p>Das <att>ref</att>-Attribut, das aus der Klasse <ident type="class">att.canonical</ident>
      vererbt wird, kann benutzt werden, um die Art der Verantwortlichkeit in normalisierter Form zu
      beschreiben. Es verweist direkt auf eine standardisierte Liste von Verantwortlichkeitstypen, wie
      sie z. B. in Normdatensätzen gepflegt werden, wie zum Beispiel folgende Liste für
      bibliografische Zwecke: <ptr target="http://www.loc.gov/marc/relators/relacode.html"/>.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOR"/>
    <ptr target="#HD21"/>
    <ptr target="#HD22"/>
    <ptr target="#HD26"/>
  </listRef>
```

^b24

