---
type: representation
source-type: document
source: '[[00_sources/tei-p5-repository-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 repository
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/repository.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# repository

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2369. Git blob: `bdd80273c4ca6cb12c914eb51882bfafdcd9b6cf`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="REPOSITORY" ident="repository">
  <gloss versionDate="2007-06-12" xml:lang="en">repository</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">lieu de conservation</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="repository.desc">contains the name of a repository within which manuscripts or other objects are stored, possibly forming part of an institution.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">기관의 부분을 형성하며, 원고를 보유하고 있는 보유 서고명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含該手稿收藏所在地的名稱，可能是某機構的一部分。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料が収められている収蔵館の名前を示す。恐らく、団体の名前の一
  部である。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le nom d'un dépôt dans lequel des manuscrits
      sont entreposés, et qui peut faire partie d'une institution.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de un depósito, parte o no de una institución, en el que se conservan los manuscritos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un deposito, parte o meno di un'istituzione, nel quale sono conservati i manoscritti.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.naming"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="REPOSITORY-egXML-ak">
      <msIdentifier>
        <settlement>Oxford</settlement>
        <institution>University of Oxford</institution>
        <repository>Bodleian Library</repository>
        <idno>MS. Bodley 406</idno>
      </msIdentifier>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msid"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">repository</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">lieu de conservation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="repository.desc">contains the name of a repository within which manuscripts or other objects are stored, possibly forming part of an institution.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기관의 부분을 형성하며, 원고를 보유하고 있는 보유 서고명을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含該手稿收藏所在地的名稱，可能是某機構的一部分。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料が収められている収蔵館の名前を示す。恐らく、団体の名前の一
  部である。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le nom d'un dépôt dans lequel des manuscrits
      sont entreposés, et qui peut faire partie d'une institution.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de un depósito, parte o no de una institución, en el que se conservan los manuscritos.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un deposito, parte o meno di un'istituzione, nel quale sono conservati i manoscritti.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.naming"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="REPOSITORY-egXML-ak">
      <msIdentifier>
        <settlement>Oxford</settlement>
        <institution>University of Oxford</institution>
        <repository>Bodleian Library</repository>
        <idno>MS. Bodley 406</idno>
      </msIdentifier>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msid"/>
  </listRef>
```

^b13

