---
type: representation
source-type: document
source: '[[00_sources/tei-p5-imprimatur-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 imprimatur
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/imprimatur.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# imprimatur

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3017. Git blob: `a1adcc3529b4a274d8c428ffb6a9313ce06e4e47`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-imprimatur" ident="imprimatur">
  <gloss versionDate="2017-06-19" xml:lang="en">imprimatur</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Imprimatur</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a formal statement authorizing the publication of a work, sometimes required to
    appear on a title page or its verso.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">작품 출판을 인가하는 공식적 진술. 이는 제목 페이지 또는 그 이면에 나타나도록 종종 요구된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含作品出版的正式授權聲明，有時必須出現在題名頁或反頁上。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">作品の出版に関する公式の情報を示す。場合によっては、タイトルページや その左ページに出現する必要がある。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une mention formalisée autorisant la publication
    d’un ouvrage, parfois exigée sur une page de titre ou à son verso.</desc>
  <desc versionDate="2006-10-18" xml:lang="de">enthält eine formelle Erklärung zur Autorisation der
    Veröffentlichung, die manchmal auf der Titel- oder Rückseite erscheinen muss.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una declaración formal que autoriza la
    publicazione de una obra, normalmente contenida en el recto o en el verso del frontispicio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una dichiarazione formale che autorizza la
    pubblicazione di un'opera, di solito riportata sul recto o sul verso del frontespizio</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprimatur-egXML-sr">
      <imprimatur>Licensed and entred acording to Order.</imprimatur>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprimatur-egXML-hu" source="#fr-ex-catechisme">
      <imprimatur>Paris, 20 juin 1968; E. Berrat, Vicaire général.</imprimatur>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprimatur-egXML-ar">
      <imprimatur>版權所有 翻印必究</imprimatur>
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
<gloss versionDate="2017-06-19" xml:lang="en">imprimatur</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Imprimatur</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a formal statement authorizing the publication of a work, sometimes required to
    appear on a title page or its verso.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">작품 출판을 인가하는 공식적 진술. 이는 제목 페이지 또는 그 이면에 나타나도록 종종 요구된다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含作品出版的正式授權聲明，有時必須出現在題名頁或反頁上。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">作品の出版に関する公式の情報を示す。場合によっては、タイトルページや その左ページに出現する必要がある。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une mention formalisée autorisant la publication
    d’un ouvrage, parfois exigée sur une page de titre ou à son verso.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">enthält eine formelle Erklärung zur Autorisation der
    Veröffentlichung, die manchmal auf der Titel- oder Rückseite erscheinen muss.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una declaración formal que autoriza la
    publicazione de una obra, normalmente contenida en el recto o en el verso del frontispicio.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una dichiarazione formale che autorizza la
    pubblicazione di un'opera, di solito riportata sul recto o sul verso del frontespizio</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprimatur-egXML-sr">
      <imprimatur>Licensed and entred acording to Order.</imprimatur>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprimatur-egXML-hu" source="#fr-ex-catechisme">
      <imprimatur>Paris, 20 juin 1968; E. Berrat, Vicaire général.</imprimatur>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprimatur-egXML-ar">
      <imprimatur>版權所有 翻印必究</imprimatur>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b16

