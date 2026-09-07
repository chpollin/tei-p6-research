---
type: representation
source-type: document
source: '[[00_sources/tei-p5-pubplace-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 pubPlace
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/pubPlace.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# pubPlace

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2843. Git blob: `f9b5e4f0c231692c48e76757181a2394021c6ced`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-pubPlace" ident="pubPlace">
  <gloss versionDate="2007-07-04" xml:lang="en">publication place</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">출판지</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">lugar de la publicación</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">lieu de publication</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">luogo di pubblicazione</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Verlagsort</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the name of the place where a bibliographic item was published.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">서지 대상이 출판된 장소명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含書目項目的出版地名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">書誌項目が出版された場所の名前を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient le nom du lieu d'une publication.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre del lugar de publicación de un
        elemento bibliográfico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome del luogo in cui un'unità
        bibliografica è stata pubblicata</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält den Namen des Orts, an dem ein bibliografisches Objekt veröffentlicht wurde.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.naming"/>
    <memberOf key="model.imprintPart"/>
    <memberOf key="model.publicationStmtPart.detail"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pubPlace-egXML-ev">
      <publicationStmt>
        <publisher>Oxford University Press</publisher>
        <pubPlace>Oxford</pubPlace>
        <date>1989</date>
      </publicationStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pubPlace-egXML-fg">
      <publicationStmt>
        <publisher>Editions Denoëll</publisher>
        <pubPlace>Paris</pubPlace>
        <date>1975</date>
      </publicationStmt>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COBICOI" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">publication place</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">출판지</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">lugar de la publicación</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">lieu de publication</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">luogo di pubblicazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Verlagsort</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the name of the place where a bibliographic item was published.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">서지 대상이 출판된 장소명을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含書目項目的出版地名稱。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">書誌項目が出版された場所の名前を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient le nom du lieu d'une publication.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre del lugar de publicación de un
        elemento bibliográfico.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome del luogo in cui un'unità
        bibliografica è stata pubblicata</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält den Namen des Orts, an dem ein bibliografisches Objekt veröffentlicht wurde.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.naming"/>
    <memberOf key="model.imprintPart"/>
    <memberOf key="model.publicationStmtPart.detail"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pubPlace-egXML-ev">
      <publicationStmt>
        <publisher>Oxford University Press</publisher>
        <pubPlace>Oxford</pubPlace>
        <date>1989</date>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pubPlace-egXML-fg">
      <publicationStmt>
        <publisher>Editions Denoëll</publisher>
        <pubPlace>Paris</pubPlace>
        <date>1975</date>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOI" type="div2"/>
  </listRef>
```

^b20

