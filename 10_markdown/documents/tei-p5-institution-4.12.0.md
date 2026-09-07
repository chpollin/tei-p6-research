---
type: representation
source-type: document
source: '[[00_sources/tei-p5-institution-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 institution
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/institution.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# institution

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2612. Git blob: `9f51c75daae058c145493e5e5feaf7325e65ab7e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="INSTITUTION" ident="institution">
  <gloss versionDate="2007-06-12" xml:lang="en">institution</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">institution</gloss>
  <gloss versionDate="2022-09-25" xml:lang="de">Institution</gloss>
  <desc versionDate="2019-01-17" xml:lang="en">contains the name of an organization such as a university or
  library, with which a manuscript or other object is identified, generally its holding institution.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">식별된 원고를 보유하고 있는 대학교 또는 대학 도서관과 같은 조직의 이름을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個組織名稱，例如大學或圖書館，手稿屬於該組織，通常是手稿所在地。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料を特定する、一般にはそれを所蔵する大学や図書館といった組織 の名前を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le nom d'un organisme (comme une université
      ou une bibliothèque), avec lequel un manuscrit est identifié ; en général c'est le nom de
      l'institution qui conserve ce manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de una organización (una universidad o una biblioteca por ejemplo) donde se encuentra el manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'organizzazione (per esempio un'università o una biblioteca) nella quale si trova il deposito del manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.naming"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INSTITUTION-egXML-xp">
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
<gloss versionDate="2007-06-12" xml:lang="en">institution</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">institution</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2022-09-25" xml:lang="de">Institution</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en">contains the name of an organization such as a university or
  library, with which a manuscript or other object is identified, generally its holding institution.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">식별된 원고를 보유하고 있는 대학교 또는 대학 도서관과 같은 조직의 이름을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個組織名稱，例如大學或圖書館，手稿屬於該組織，通常是手稿所在地。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料を特定する、一般にはそれを所蔵する大学や図書館といった組織 の名前を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le nom d'un organisme (comme une université
      ou une bibliothèque), avec lequel un manuscrit est identifié ; en général c'est le nom de
      l'institution qui conserve ce manuscrit.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de una organización (una universidad o una biblioteca por ejemplo) donde se encuentra el manuscrito.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'organizzazione (per esempio un'università o una biblioteca) nella quale si trova il deposito del manoscritto.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.naming"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INSTITUTION-egXML-xp">
      <msIdentifier>
        <settlement>Oxford</settlement>
        <institution>University of Oxford</institution>
        <repository>Bodleian Library</repository>
        <idno>MS. Bodley 406</idno>
      </msIdentifier>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msid"/>
  </listRef>
```

^b14

