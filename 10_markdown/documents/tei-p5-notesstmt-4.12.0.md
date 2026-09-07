---
type: representation
source-type: document
source: '[[00_sources/tei-p5-notesstmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 notesStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/notesStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# notesStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4916. Git blob: `5d24bb0cf4b4474cf1ba398758a8272408a9f901`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-notesStmt" ident="notesStmt">
  <gloss versionDate="2007-07-04" xml:lang="en">notes statement</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">mention de notes</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">주석 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">附註陳述</gloss>
    <gloss versionDate="2016-11-17" xml:lang="de">Zusätzliche Anmerkungen</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de notas</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulle note</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">collects together any notes providing information about a text additional to that recorded
    in other parts of the bibliographic description.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">rassemble toutes les notes fournissant des informations
    sur un texte, en plus des informations mentionnées dans d'autres parties de la description
    bibliographique.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">서지 정보 기술의 다른 부분에 기록된 것들 이외에, 텍스트에 관한 정보를 제공하는 주석들을 모아
    놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">收集其他部分的書目描述中所未記載的任何文件相關附註。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該書誌情報の他の場所に記録されているテキストに関する注釈をまとめる。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">fasst Anmerkungen zu einem Text zusammen, zusätzlich zu jenen Informationen, die in anderen Teilen der bibliografischen Beschreibung bereits festgehalten sind.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa algunas notas que proporcionan información sobre
    un texto adicional referido en otras partes de la descripción bibliográfica.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa tutte le note sul testo in aggiunta a quelle
    registrate nelle altre parti della descrizione bibliografica.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <elementRef key="relatedItem"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notesStmt-egXML-nn">
      <notesStmt>
        <note>Historical commentary provided by Mark Cohen</note>
        <note>OCR scanning done at University of Toronto</note>
      </notesStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notesStmt-egXML-zm" source="#fr-ex-Tunis">
      <notesStmt>
        <note>Les photographies, héliogravures et cartes postales colorisées signées Lehnert
            &amp; Landrock, de techniques novatrices, sont réellement des œuvres d'art ; elles
            apportent en outre une documentation considérable sur la Tunisie du début du XXe
          siècle.</note>
      </notesStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notesStmt-egXML-tz">
      <notesStmt>
        <note>歷史評論由馬克．可漢提共</note>
        <note>OCR光學辨識掃描於多倫多大學</note>
      </notesStmt>
    </egXML>
  </exemplum>
  <remarks ident="notesStmt-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Information of different kinds should not be grouped together into the same note.</p>
  </remarks>
  <remarks ident="notesStmt-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>des informations hétérogènes ne doivent pas être regroupées dans une  même note.</p>
  </remarks>
  <remarks ident="notesStmt-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>La información de diversos tipos no se debe agrupar junta en la misma nota.</p>
  </remarks>
  <remarks ident="notesStmt-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 種類が異なる情報は、同じ注釈としてまとめるべきではない。 </p>
  </remarks>
  <remarks ident="notesStmt-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>Informationen unterschiedlicher Art sollten nicht in einer gemeinsamen Anmerkung gruppiert werden.</p>
  </remarks>
  <listRef>
    <ptr target="#HD27"/>
    <ptr target="#HD2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">notes statement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">mention de notes</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">주석 진술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">附註陳述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Zusätzliche Anmerkungen</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de notas</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulle note</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">collects together any notes providing information about a text additional to that recorded
    in other parts of the bibliographic description.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">rassemble toutes les notes fournissant des informations
    sur un texte, en plus des informations mentionnées dans d'autres parties de la description
    bibliographique.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">서지 정보 기술의 다른 부분에 기록된 것들 이외에, 텍스트에 관한 정보를 제공하는 주석들을 모아
    놓는다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">收集其他部分的書目描述中所未記載的任何文件相關附註。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該書誌情報の他の場所に記録されているテキストに関する注釈をまとめる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">fasst Anmerkungen zu einem Text zusammen, zusätzlich zu jenen Informationen, die in anderen Teilen der bibliografischen Beschreibung bereits festgehalten sind.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa algunas notas que proporcionan información sobre
    un texto adicional referido en otras partes de la descripción bibliográfica.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa tutte le note sul testo in aggiunta a quelle
    registrate nelle altre parti della descrizione bibliografica.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <elementRef key="relatedItem"/>
      </alternate>
    
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notesStmt-egXML-nn">
      <notesStmt>
        <note>Historical commentary provided by Mark Cohen</note>
        <note>OCR scanning done at University of Toronto</note>
      </notesStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notesStmt-egXML-zm" source="#fr-ex-Tunis">
      <notesStmt>
        <note>Les photographies, héliogravures et cartes postales colorisées signées Lehnert
            &amp; Landrock, de techniques novatrices, sont réellement des œuvres d'art ; elles
            apportent en outre une documentation considérable sur la Tunisie du début du XXe
          siècle.</note>
      </notesStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-notesStmt-egXML-tz">
      <notesStmt>
        <note>歷史評論由馬克．可漢提共</note>
        <note>OCR光學辨識掃描於多倫多大學</note>
      </notesStmt>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="notesStmt-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Information of different kinds should not be grouped together into the same note.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="notesStmt-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>des informations hétérogènes ne doivent pas être regroupées dans une  même note.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="notesStmt-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>La información de diversos tipos no se debe agrupar junta en la misma nota.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="notesStmt-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 種類が異なる情報は、同じ注釈としてまとめるべきではない。 </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="notesStmt-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>Informationen unterschiedlicher Art sollten nicht in einer gemeinsamen Anmerkung gruppiert werden.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD27"/>
    <ptr target="#HD2"/>
  </listRef>
```

^b26

