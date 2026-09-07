---
type: representation
source-type: document
source: '[[00_sources/tei-p5-docedition-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 docEdition
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/docEdition.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# docEdition

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3979. Git blob: `69666d90314ba4d3053586a1ae4f827046648c15`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-docEdition" ident="docEdition">
  <gloss versionDate="2005-01-14" xml:lang="en">document edition</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문서 편집</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文件版本</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">édition du document</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Ausgabe des Dokuments</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">edición del documento</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">edizione del documento</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an edition statement as presented on a title page of a
document.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문서의 제목 페이지에 제시되는 편집 진술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一份版本陳述，與文件題名頁所顯示的相同。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">タイトルページにある当該文書の版を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une mention d’édition telle qu’elle
            figure sur la page de titre d’un document.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält Angaben zur Ausgabe, entsprechend den Informationen auf dem Titelblatt eines
    Dokuments.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una declaración editorial como la contiene el frontispicio de un documento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una dichiarazione editoriale così come riportata nel frontespizio di un documento.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docEdition-egXML-ti">
      <docEdition>The Third edition Corrected</docEdition>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docEdition-egXML-jv">
      <docEdition>3e Edition Augmentée</docEdition>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docEdition-egXML-up">
      <docEdition>修訂第三版</docEdition>
    </egXML>
  </exemplum>
  <remarks ident="docEdition-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Cf. the <gi>edition</gi> element of bibliographic
citation.  As usual, the shorter name has been given to the
more frequent element.</p>
  </remarks>
  <remarks ident="docEdition-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Voir l'élément <gi>edition</gi> dans une citation bibliographique. Comme d'habitude,
                un nom abrégé a été donné à l'élément le plus fréquent.</p>
  </remarks>
  <remarks ident="docEdition-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>edition</gi>も参照のこと。一般には、よく使われる要素により
    簡単な名前が記述される。
    </p>
  </remarks>
  <remarks ident="docEdition-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Vgl. das <gi>edition</gi>-Element für bibliografische Angaben. Wie üblich wurde der kürzere Name
      für das häufiger benutzte Element verwendet.</p>
  </remarks>
  <listRef>
    <ptr target="#DSTITL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">document edition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문서 편집</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文件版本</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">édition du document</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Ausgabe des Dokuments</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">edición del documento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">edizione del documento</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an edition statement as presented on a title page of a
document.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문서의 제목 페이지에 제시되는 편집 진술을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一份版本陳述，與文件題名頁所顯示的相同。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">タイトルページにある当該文書の版を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une mention d’édition telle qu’elle
            figure sur la page de titre d’un document.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält Angaben zur Ausgabe, entsprechend den Informationen auf dem Titelblatt eines
    Dokuments.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una declaración editorial como la contiene el frontispicio de un documento.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una dichiarazione editoriale così come riportata nel frontespizio di un documento.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docEdition-egXML-ti">
      <docEdition>The Third edition Corrected</docEdition>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docEdition-egXML-jv">
      <docEdition>3e Edition Augmentée</docEdition>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docEdition-egXML-up">
      <docEdition>修訂第三版</docEdition>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="docEdition-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Cf. the <gi>edition</gi> element of bibliographic
citation.  As usual, the shorter name has been given to the
more frequent element.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="docEdition-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Voir l'élément <gi>edition</gi> dans une citation bibliographique. Comme d'habitude,
                un nom abrégé a été donné à l'élément le plus fréquent.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="docEdition-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>edition</gi>も参照のこと。一般には、よく使われる要素により
    簡単な名前が記述される。
    </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="docEdition-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Vgl. das <gi>edition</gi>-Element für bibliografische Angaben. Wie üblich wurde der kürzere Name
      für das häufiger benutzte Element verwendet.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b25

