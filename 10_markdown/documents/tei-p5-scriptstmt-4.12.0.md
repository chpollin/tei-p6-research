---
type: representation
source-type: document
source: '[[00_sources/tei-p5-scriptstmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 scriptStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/scriptStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# scriptStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3586. Git blob: `cb1413ba80463653fc6cfe84546991b126583159`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="spoken" xml:id="gi-scriptStmt" ident="scriptStmt">
  <gloss versionDate="2005-01-14" xml:lang="en">script statement</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">déclaration du script</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">스크립트 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">腳本陳述</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Erklärung zum Skript</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración del guión</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sul copione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a citation giving details of the script used for
a spoken text.</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">contient une citation donnant des détails sur le script à l’origine de la parole. [le terme <q>script</q> est entendu au sens large dans ce document comme tout texte préparatoire à une prise de parole (discours politique, sermon, interview, allocution, conférence, émission, etc.)].</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트에 사용되는 스크립트의 상세 항목을 제시하는 인용을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含口說文本的來源腳本相關細節。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話テキストで使われている台本の詳細に関する引用を示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">enthält einen Zitatbeleg
  mit Angaben zum Skript, das für die Aufnahme eines gesprochenen
  Texts genutzt wurde.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una citación que indica las peculariedades del guión usado en un texto hablado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una citazione con i dettagli del copione utilizzato per un testo orale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.sourceDescPart"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.biblLike"/>
    </alternate>
  </content>
  <constraintSpec ident="scriptStmt-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:scriptStmt"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-scriptStmt-egXML-fo">
      <scriptStmt>
        <bibl>
          <author>Craig Warner</author>
          <title>Strangers on a Train</title>
          <title type="sub">Based on the novel by Patricia Highsmith</title>
          <edition>French's acting edition</edition>
          <idno type="ISBN">978 0 573 01972 2</idno>
          <publisher>Samuel French Ltd</publisher>
        </bibl>
      </scriptStmt>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD32"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">script statement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">déclaration du script</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">스크립트 진술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">腳本陳述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Erklärung zum Skript</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración del guión</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sul copione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a citation giving details of the script used for
a spoken text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">contient une citation donnant des détails sur le script à l’origine de la parole. [le terme <q>script</q> est entendu au sens large dans ce document comme tout texte préparatoire à une prise de parole (discours politique, sermon, interview, allocution, conférence, émission, etc.)].</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트에 사용되는 스크립트의 상세 항목을 제시하는 인용을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含口說文本的來源腳本相關細節。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話テキストで使われている台本の詳細に関する引用を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">enthält einen Zitatbeleg
  mit Angaben zum Skript, das für die Aufnahme eines gesprochenen
  Texts genutzt wurde.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una citación que indica las peculariedades del guión usado en un texto hablado.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una citazione con i dettagli del copione utilizzato per un testo orale.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.sourceDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.biblLike"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="scriptStmt-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:scriptStmt"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-scriptStmt-egXML-fo">
      <scriptStmt>
        <bibl>
          <author>Craig Warner</author>
          <title>Strangers on a Train</title>
          <title type="sub">Based on the novel by Patricia Highsmith</title>
          <edition>French's acting edition</edition>
          <idno type="ISBN">978 0 573 01972 2</idno>
          <publisher>Samuel French Ltd</publisher>
        </bibl>
      </scriptStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD32"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b20

