---
type: representation
source-type: document
source: '[[00_sources/tei-p5-publisher-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 publisher
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/publisher.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# publisher

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4285. Git blob: `0cf6092fd8d28df985abed57f1479e29ae9b0983`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-publisher" ident="publisher">
  <gloss xml:lang="en" versionDate="2009-01-06">publisher</gloss>
  <gloss xml:lang="es" versionDate="2023-05-08">editorial</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">éditeur</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Verlag</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides the name of the organization responsible for the publication or distribution of a
        bibliographic item.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">서지 항목의 출판이나 배포에 책임이 있는 기구명을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供負責出版或發行書目項目的機構名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">書誌項目の出版や頒布に責任のある団体の名前を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">donne le nom de l'organisme responsable de la
        publication ou de la distribution d'un élément de la bibliographie.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre de la organización responsable de
        la publicación o la distribución de un elemento bibliográfico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">gibt den Namen der Organisation an, die für die Veröffentlichung und Verbreitung eines
    bibliografischen Objekts verantwortlich ist.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publisher-egXML-bp">
      <imprint>
        <pubPlace>Oxford</pubPlace>
        <publisher>Clarendon Press</publisher>
        <date>1987</date>
      </imprint>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publisher-egXML-tv">
      <imprint>
        <pubPlace>Paris</pubPlace>
        <publisher>Les Éditions de Minuit</publisher>
        <date>2001</date>
      </imprint>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publisher-egXML-wv">
      <imprint>
        <pubPlace>上海</pubPlace>
        <publisher>上海古籍出版社</publisher>
        <date>2008</date>
      </imprint>
    </egXML>
  </exemplum>
  <remarks ident="publisher-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Use the full form of the name by which a company is usually referred to,
            rather than any abbreviation of it which may appear on a title page</p>
  </remarks>
  <remarks ident="publisher-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Utiliser la forme développée du nom au moyen duquel l'organisme est
            habituellement cité, plutôt qu'une abréviation, cette dernière pouvant apparaître sur
            une page de titre.</p>
  </remarks>
  <remarks ident="publisher-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 会社を示す、タイトルページにある省略名ではなく、正式な名前を使う。 </p>
  </remarks>
  <remarks ident="publisher-remarks" versionDate="2017-06-13" xml:lang="de">
    <p rend="dataDesc">Außer bei der Transkription von bibliografischen Angaben, ist der vollständige Name des
      Unternehmens gegenüber einer abgekürzten Version, wie sie etwa auf der gedruckten Titelseite zu
      finden ist, zu bevorzugen.</p>
  </remarks>
  <listRef>
    <ptr target="#COBICOI"/>
    <ptr target="#HD24"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss xml:lang="en" versionDate="2009-01-06">publisher</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss xml:lang="es" versionDate="2023-05-08">editorial</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">éditeur</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Verlag</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides the name of the organization responsible for the publication or distribution of a
        bibliographic item.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">서지 항목의 출판이나 배포에 책임이 있는 기구명을 제시한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供負責出版或發行書目項目的機構名稱。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">書誌項目の出版や頒布に責任のある団体の名前を示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">donne le nom de l'organisme responsable de la
        publication ou de la distribution d'un élément de la bibliographie.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre de la organización responsable de
        la publicación o la distribución de un elemento bibliográfico.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">gibt den Namen der Organisation an, die für die Veröffentlichung und Verbreitung eines
    bibliografischen Objekts verantwortlich ist.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.imprintPart"/>
    <memberOf key="model.publicationStmtPart.agency"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publisher-egXML-bp">
      <imprint>
        <pubPlace>Oxford</pubPlace>
        <publisher>Clarendon Press</publisher>
        <date>1987</date>
      </imprint>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publisher-egXML-tv">
      <imprint>
        <pubPlace>Paris</pubPlace>
        <publisher>Les Éditions de Minuit</publisher>
        <date>2001</date>
      </imprint>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publisher-egXML-wv">
      <imprint>
        <pubPlace>上海</pubPlace>
        <publisher>上海古籍出版社</publisher>
        <date>2008</date>
      </imprint>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="publisher-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Use the full form of the name by which a company is usually referred to,
            rather than any abbreviation of it which may appear on a title page</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="publisher-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Utiliser la forme développée du nom au moyen duquel l'organisme est
            habituellement cité, plutôt qu'une abréviation, cette dernière pouvant apparaître sur
            une page de titre.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="publisher-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 会社を示す、タイトルページにある省略名ではなく、正式な名前を使う。 </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="publisher-remarks" versionDate="2017-06-13" xml:lang="de">
    <p rend="dataDesc">Außer bei der Transkription von bibliografischen Angaben, ist der vollständige Name des
      Unternehmens gegenüber einer abgekürzten Version, wie sie etwa auf der gedruckten Titelseite zu
      finden ist, zu bevorzugen.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOI"/>
    <ptr target="#HD24"/>
  </listRef>
```

^b22

