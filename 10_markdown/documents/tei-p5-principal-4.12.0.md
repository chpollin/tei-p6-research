---
type: representation
source-type: document
source: '[[00_sources/tei-p5-principal-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 principal
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/principal.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# principal

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3195. Git blob: `0ff5370cd73b7e742a7002944d8d04d526b4faa3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-principal" ident="principal">
  <gloss versionDate="2005-01-14" xml:lang="en">principal researcher</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">chercheur principal</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">책임 연구자</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">主導研究者</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Projektleiter</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">investigador principal</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">ricercatore principale</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">supplies the name of the principal researcher responsible for the
creation of an electronic text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient le nom du chercheur  qui est principalement responsable de la création d’un texte électronique.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자 텍스트 생성에 대한 책임을 지는 책임 연구자의 이름을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供負責電子文件製作的主導研究者的姓名。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">電子テキストの生成に責任のある中心的な研究者の名前を示す。</desc>
  <desc versionDate="2016-11-17" xml:lang="de">gibt den Namen des Projektleiters an, der für die Erstellung eines elektronischen Textes verantwortlich ist.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del investigador principal de la creación de un texto electrónico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome del ricercatore principale responsabile della creazione di un documento elettronico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.respLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-principal-egXML-ft">
      <principal ref="http://viaf.org/viaf/105517912">Gary Taylor</principal>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-principal-egXML-qm" source="#fr-ex-Sanctoral-ee">
      <principal xml:id="fr_AEU-2">Anne-Élisabeth Urfels-Capot</principal>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-principal-egXML-yz">
      <principal>蔡元培</principal>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD21"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">principal researcher</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">chercheur principal</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">책임 연구자</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">主導研究者</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Projektleiter</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">investigador principal</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">ricercatore principale</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies the name of the principal researcher responsible for the
creation of an electronic text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient le nom du chercheur  qui est principalement responsable de la création d’un texte électronique.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자 텍스트 생성에 대한 책임을 지는 책임 연구자의 이름을 제시한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供負責電子文件製作的主導研究者的姓名。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">電子テキストの生成に責任のある中心的な研究者の名前を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">gibt den Namen des Projektleiters an, der für die Erstellung eines elektronischen Textes verantwortlich ist.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del investigador principal de la creación de un texto electrónico.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome del ricercatore principale responsabile della creazione di un documento elettronico.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.respLike"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-principal-egXML-ft">
      <principal ref="http://viaf.org/viaf/105517912">Gary Taylor</principal>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-principal-egXML-qm" source="#fr-ex-Sanctoral-ee">
      <principal xml:id="fr_AEU-2">Anne-Élisabeth Urfels-Capot</principal>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-principal-egXML-yz">
      <principal>蔡元培</principal>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD21"/>
  </listRef>
```

^b21

