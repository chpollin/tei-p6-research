---
type: representation
source-type: document
source: '[[00_sources/tei-p5-doctitle-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 docTitle
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/docTitle.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# docTitle

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3876. Git blob: `270047f4f83637834b959ad851bb38c6563a8717`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-docTitle" ident="docTitle">
  <gloss versionDate="2005-01-14" xml:lang="en">document title</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문서 제목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文件題名</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">titre du document</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Dokumenttitel</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">título del documento</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">titolo del documento</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the title of a document, including all its
constituents, as given on a title page.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">제목 페이지에 제시되는 모든 구성성분을 포함한 문서의 제목을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件題名，包含所有組成部分，同於題名頁上所顯示的題名。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該文書のタイトルを示す。タイトルページにあるタイトルの全情報を含む。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le titre d’un document, incluant la
            totalité de ses composants tels qu’ils sont donnés sur la page de titre.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält den Titel eines Dokuments, einschließlich aller Bestandteile, wie sie auf dem Titelblatt
    angegeben sind.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el título del documento incluyendo todos sus elementos constitutivos, como especificado en el frontispicio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il titolo del documento in tutti i suoi elementi costitutivi, come specificato nel frontespizio.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <sequence>
      
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <elementRef key="titlePart"/>
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docTitle-egXML-ty" source="#SAPTEG-eg-3">
      <docTitle>
        <titlePart type="main">The DUNCIAD, VARIOURVM.</titlePart>
        <titlePart type="sub">WITH THE PROLEGOMENA of SCRIBLERUS.</titlePart>
      </docTitle>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docTitle-egXML-sq" source="#fr-ex-Perec-choses">
      <docTitle>
        <titlePart type="main">LES CHOSES</titlePart>
        <titlePart type="sub">Une histoire des années soixante.</titlePart>
      </docTitle>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docTitle-egXML-ak">
      <docTitle>
        <titlePart type="main">食物的歷史</titlePart>
        <titlePart type="sub">透視人類的飲食與文明 </titlePart>
      </docTitle>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DSTITL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">document title</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문서 제목</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文件題名</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">titre du document</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Dokumenttitel</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">título del documento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">titolo del documento</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the title of a document, including all its
constituents, as given on a title page.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">제목 페이지에 제시되는 모든 구성성분을 포함한 문서의 제목을 제시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件題名，包含所有組成部分，同於題名頁上所顯示的題名。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該文書のタイトルを示す。タイトルページにあるタイトルの全情報を含む。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le titre d’un document, incluant la
            totalité de ses composants tels qu’ils sont donnés sur la page de titre.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält den Titel eines Dokuments, einschließlich aller Bestandteile, wie sie auf dem Titelblatt
    angegeben sind.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el título del documento incluyendo todos sus elementos constitutivos, como especificado en el frontispicio.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il titolo del documento in tutti i suoi elementi costitutivi, come specificato nel frontespizio.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <elementRef key="titlePart"/>
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docTitle-egXML-ty" source="#SAPTEG-eg-3">
      <docTitle>
        <titlePart type="main">The DUNCIAD, VARIOURVM.</titlePart>
        <titlePart type="sub">WITH THE PROLEGOMENA of SCRIBLERUS.</titlePart>
      </docTitle>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docTitle-egXML-sq" source="#fr-ex-Perec-choses">
      <docTitle>
        <titlePart type="main">LES CHOSES</titlePart>
        <titlePart type="sub">Une histoire des années soixante.</titlePart>
      </docTitle>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docTitle-egXML-ak">
      <docTitle>
        <titlePart type="main">食物的歷史</titlePart>
        <titlePart type="sub">透視人類的飲食與文明 </titlePart>
      </docTitle>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b21

