---
type: representation
source-type: document
source: '[[00_sources/tei-p5-titlestmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 titleStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/titleStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# titleStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4627. Git blob: `f042d0dbcad4c888bd55b608e75d061d73b7add6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-titleStmt" ident="titleStmt">
  <gloss versionDate="2005-01-14" xml:lang="en">title statement</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">mention de titre</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">제목 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">題名陳述</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Angaben zum Titel</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración del título</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sul titolo</gloss>
  <desc versionDate="2012-04-17" xml:lang="en">groups information about the title of a work and those responsible for its content.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">regroupe les informations sur le titre d’une œuvre et
    les personnes ou institutions responsables de son contenu intellectuel.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">저작의 제목 그리고 지적 내용에 대한 책임에 관한 정보를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集關於作品標題與作品智慧內容責任歸屬的資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">作品や知的内容に責任のあるもののタイトルに関する情報をまとめる。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">umfasst Angaben zum Titel eines Werks und zu den für
    seinen Inhalt Verantwortlichen.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa la información referente al título de una obra y a
    los responsables de su contenido intelectual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni sul titolo di un'opera e sulle
    responsabilità del suo contenuto intellettuale.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      <elementRef key="title" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.respLike" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titleStmt-egXML-pk">
      <titleStmt>
        <title>Capgrave's Life of St. John Norbert: a machine-readable transcription</title>
        <respStmt>
          <resp>compiled by</resp>
          <name>P.J. Lucas</name>
        </respStmt>
      </titleStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titleStmt-egXML-jj" source="#fr-ex-Sanctoral-ee">
      <titleStmt>
        <title>Le sanctoral du lectionnaire de l'office dominicain (1254-1256)</title>
        <funder>2008—..., École nationale des chartes</funder>
        <principal>Anne-Élisabeth Urfels-Capot</principal>
        <respStmt>
          <resp>responsable des publications</resp>
          <name>Olivier Canteaut (École nationale des chartes)</name>
        </respStmt>
        <respStmt>
          <resp> 2009—..., Éditeur électronique : du TEI à l'écran</resp>
          <name ref="vincent.jolivet@enc.sorbonne.fr">Vincent Jolivet (École nationale
              des chartes)</name>
        </respStmt>
        <respStmt>
          <resp>2009, Éditeur scientifique</resp>
          <name ref="pascale.bourgain@enc.sorbonne.fr">Pascale Bourgain (École
              nationale des chartes)</name>
        </respStmt>
        <respStmt>
          <resp>2008, Conversion du document bureautique vers TEI</resp>
          <name ref="frederic.glorieux@enc.sorbonne.fr">Frédéric Glorieux (École
              nationale des chartes)</name>
        </respStmt>
      </titleStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titleStmt-egXML-vb">
      <titleStmt>
        <title>Taisho Tripitaka, Electronic version, No. 251 般若波羅蜜多心經</title>
        <respStmt>
          <resp>電子化</resp>
          <name>中華電子佛典協會</name>
        </respStmt>
      </titleStmt>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD21"/>
    <ptr target="#HD2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">title statement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">mention de titre</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">제목 진술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">題名陳述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angaben zum Titel</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración del título</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sul titolo</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-04-17" xml:lang="en">groups information about the title of a work and those responsible for its content.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">regroupe les informations sur le titre d’une œuvre et
    les personnes ou institutions responsables de son contenu intellectuel.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">저작의 제목 그리고 지적 내용에 대한 책임에 관한 정보를 모아 놓는다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集關於作品標題與作品智慧內容責任歸屬的資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">作品や知的内容に責任のあるもののタイトルに関する情報をまとめる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">umfasst Angaben zum Titel eines Werks und zu den für
    seinen Inhalt Verantwortlichen.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa la información referente al título de una obra y a
    los responsables de su contenido intelectual.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni sul titolo di un'opera e sulle
    responsabilità del suo contenuto intellettuale.</desc>
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
    <sequence>
      <elementRef key="title" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.respLike" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titleStmt-egXML-pk">
      <titleStmt>
        <title>Capgrave's Life of St. John Norbert: a machine-readable transcription</title>
        <respStmt>
          <resp>compiled by</resp>
          <name>P.J. Lucas</name>
        </respStmt>
      </titleStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titleStmt-egXML-jj" source="#fr-ex-Sanctoral-ee">
      <titleStmt>
        <title>Le sanctoral du lectionnaire de l'office dominicain (1254-1256)</title>
        <funder>2008—..., École nationale des chartes</funder>
        <principal>Anne-Élisabeth Urfels-Capot</principal>
        <respStmt>
          <resp>responsable des publications</resp>
          <name>Olivier Canteaut (École nationale des chartes)</name>
        </respStmt>
        <respStmt>
          <resp> 2009—..., Éditeur électronique : du TEI à l'écran</resp>
          <name ref="vincent.jolivet@enc.sorbonne.fr">Vincent Jolivet (École nationale
              des chartes)</name>
        </respStmt>
        <respStmt>
          <resp>2009, Éditeur scientifique</resp>
          <name ref="pascale.bourgain@enc.sorbonne.fr">Pascale Bourgain (École
              nationale des chartes)</name>
        </respStmt>
        <respStmt>
          <resp>2008, Conversion du document bureautique vers TEI</resp>
          <name ref="frederic.glorieux@enc.sorbonne.fr">Frédéric Glorieux (École
              nationale des chartes)</name>
        </respStmt>
      </titleStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-titleStmt-egXML-vb">
      <titleStmt>
        <title>Taisho Tripitaka, Electronic version, No. 251 般若波羅蜜多心經</title>
        <respStmt>
          <resp>電子化</resp>
          <name>中華電子佛典協會</name>
        </respStmt>
      </titleStmt>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD21"/>
    <ptr target="#HD2"/>
  </listRef>
```

^b21

