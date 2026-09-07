---
type: representation
source-type: document
source: '[[00_sources/tei-p5-distributor-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 distributor
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/distributor.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# distributor

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2961. Git blob: `eece2895899c580eda767c1c37b1eddc378bb9fb`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-distributor" ident="distributor">
  <gloss versionDate="2007-06-12" xml:lang="en">distributor</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">diffuseur</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Distributor</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">supplies the name of a person or other agency responsible for the
distribution of a text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">donne le nom d’une personne ou d’un organisme responsable de la diffusion d’un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 배포 권한을 갖는 개인 또는 기관의 이름을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供負責發行文件的個人或其他經銷商的名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストの頒布に責任を持つ人物または団体の名前を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">gibt die Person oder Instanz an, die für die Distribution des Textes verantwortlich ist.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre de la persona o agente responsable de la distribución de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome di una persona o di un'organizzazione responsabile della distribuzione di un testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.imprintPart"/>
    <memberOf key="model.publicationStmtPart.agency"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distributor-egXML-ke">
      <distributor>Oxford Text Archive</distributor>
      <distributor>Redwood and Burn Ltd</distributor>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distributor-egXML-lr">
      <distributor>Laboratoire : Analyse et Traitement Informatique de la Langue Française)</distributor>
      <distributor>Centre National de la Recherche Scientifique</distributor>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distributor-egXML-fn">
      <distributor>中央研究院</distributor>
      <distributor>中華電子佛典協會</distributor>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD24"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">distributor</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">diffuseur</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Distributor</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies the name of a person or other agency responsible for the
distribution of a text.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">donne le nom d’une personne ou d’un organisme responsable de la diffusion d’un texte.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 배포 권한을 갖는 개인 또는 기관의 이름을 제시한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供負責發行文件的個人或其他經銷商的名稱。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストの頒布に責任を持つ人物または団体の名前を示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">gibt die Person oder Instanz an, die für die Distribution des Textes verantwortlich ist.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre de la persona o agente responsable de la distribución de un texto.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome di una persona o di un'organizzazione responsabile della distribuzione di un testo.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.imprintPart"/>
    <memberOf key="model.publicationStmtPart.agency"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distributor-egXML-ke">
      <distributor>Oxford Text Archive</distributor>
      <distributor>Redwood and Burn Ltd</distributor>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distributor-egXML-lr">
      <distributor>Laboratoire : Analyse et Traitement Informatique de la Langue Française)</distributor>
      <distributor>Centre National de la Recherche Scientifique</distributor>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distributor-egXML-fn">
      <distributor>中央研究院</distributor>
      <distributor>中華電子佛典協會</distributor>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD24"/>
  </listRef>
```

^b17

