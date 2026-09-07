---
type: representation
source-type: document
source: '[[00_sources/tei-p5-authority-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 authority
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/authority.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# authority

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3423. Git blob: `8bacd0f888cddfc111bb785af853bae5df2ac505`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-authority" ident="authority">
  <gloss versionDate="2005-01-14" xml:lang="en">release authority</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">responsable de la publication.</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">배포권자</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">供應機構</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Freigabeinstanz</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">responsable de la presentación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">autorità di pubblicazione</gloss>
  <gloss versionDate="2023-08-30" xml:lang="ja">刊行許可元</gloss>
  <desc versionDate="2012-10-22" xml:lang="en">supplies the name of a person or other agency responsible for
  making a work available, other than a publisher or
  distributor.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">donne le nom de la personne ou de l'organisme responsable de la publication d’un fichier électronique, autre qu’un éditeur ou un distributeur.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">출판사 또는 배포자 외에 전자 파일 사용 허가에 대한 권한을 갖는 개인 또는 기관의 이름을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">說明除了出版者或發行者之外，負責提供電子檔案的個人或其他經銷商的名稱。</desc>
  <desc versionDate="2023-08-30" xml:lang="ja">作品の供給に責任のある、出版者や発売者以外の個人または団体の名前を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">gibt die Person oder Instanz (außer Verlag oder Distributor) an, die für den Zugang zu einer Ressource verantwortlich ist.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre de la persona o agente responsable que ha hecho disponible un archivo electrónico, que no es ni el editor ni el distribudor.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome di una persona o di un'organizzazione responsabile della messa a disposizione di un file elettronico, diversa dalll'editore o dal distributore.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.publicationStmtPart.agency"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-authority-egXML-zx">
      <authority>John Smith</authority>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-authority-egXML-ps">
      <authority>A. D.</authority>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-authority-egXML-xx">
      <authority>高行健</authority>
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
<gloss versionDate="2005-01-14" xml:lang="en">release authority</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">responsable de la publication.</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">배포권자</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">供應機構</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Freigabeinstanz</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">responsable de la presentación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">autorità di pubblicazione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-08-30" xml:lang="ja">刊行許可元</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-10-22" xml:lang="en">supplies the name of a person or other agency responsible for
  making a work available, other than a publisher or
  distributor.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">donne le nom de la personne ou de l'organisme responsable de la publication d’un fichier électronique, autre qu’un éditeur ou un distributeur.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">출판사 또는 배포자 외에 전자 파일 사용 허가에 대한 권한을 갖는 개인 또는 기관의 이름을 제시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明除了出版者或發行者之外，負責提供電子檔案的個人或其他經銷商的名稱。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-08-30" xml:lang="ja">作品の供給に責任のある、出版者や発売者以外の個人または団体の名前を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">gibt die Person oder Instanz (außer Verlag oder Distributor) an, die für den Zugang zu einer Ressource verantwortlich ist.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre de la persona o agente responsable que ha hecho disponible un archivo electrónico, que no es ni el editor ni el distribudor.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome di una persona o di un'organizzazione responsabile della messa a disposizione di un file elettronico, diversa dalll'editore o dal distributore.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.publicationStmtPart.agency"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-authority-egXML-zx">
      <authority>John Smith</authority>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-authority-egXML-ps">
      <authority>A. D.</authority>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-authority-egXML-xx">
      <authority>高行健</authority>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD24"/>
  </listRef>
```

^b22

