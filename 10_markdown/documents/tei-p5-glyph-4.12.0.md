---
type: representation
source-type: document
source: '[[00_sources/tei-p5-glyph-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 glyph
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/glyph.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# glyph

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2992. Git blob: `7b80b55ca257d124c37d232283add9d297c3ef2b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="glyph" module="gaiji" xml:id="GLYPH">
  <gloss versionDate="2005-01-14" xml:lang="en">character glyph</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">그림 문자</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文字的形體</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">glyphe d'un caractère</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">pictograma</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">glifo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides descriptive information about a character
  glyph<!-- which is not
  otherwise available in the document character set-->.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">그림 문자에 관한 기술적 정보를 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一種字體的描述性資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">グリフの解説を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des informations descriptives sur un glyphe.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona información descriptiva sobre un pictograma.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni descrittive su di un glifo.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="unicodeProp"/>
      <elementRef key="unihanProp"/>
      <elementRef key="localProp"/>
      <elementRef key="mapping"/>
      <elementRef key="figure"/>
      <classRef key="model.graphicLike"/>
      <classRef key="model.noteLike"/>
      <classRef key="model.descLike"/>
    </alternate>
  </content>
  <exemplum versionDate="2019-07-01" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GLYPH-egXML-hc">
      <glyph xml:id="rstroke">
        <localProp name="Name" value="LATIN SMALL LETTER R WITH A FUNNY STROKE"/>
        <localProp name="entity" value="rstroke"/>
        <figure>
          <graphic url="glyph-rstroke.png"/>
        </figure>
      </glyph>
    </egXML>
  </exemplum>
  <exemplum versionDate="2019-07-01" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GLYPH-egXML-hv">
      <glyph xml:id="fr_napos">
        <localProp name="nom" value="N latin minuscule précédé d'une apostrophe"/>
        <localProp name="entity" value="napos"/>
        <graphic url="glyph-napos.png"/>
      </glyph>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#D25-20"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">character glyph</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">그림 문자</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文字的形體</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">glyphe d'un caractère</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">pictograma</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">glifo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides descriptive information about a character
  glyph<!-- which is not
  otherwise available in the document character set-->.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그림 문자에 관한 기술적 정보를 제공한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一種字體的描述性資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">グリフの解説を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des informations descriptives sur un glyphe.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona información descriptiva sobre un pictograma.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni descrittive su di un glifo.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="unicodeProp"/>
      <elementRef key="unihanProp"/>
      <elementRef key="localProp"/>
      <elementRef key="mapping"/>
      <elementRef key="figure"/>
      <classRef key="model.graphicLike"/>
      <classRef key="model.noteLike"/>
      <classRef key="model.descLike"/>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2019-07-01" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GLYPH-egXML-hc">
      <glyph xml:id="rstroke">
        <localProp name="Name" value="LATIN SMALL LETTER R WITH A FUNNY STROKE"/>
        <localProp name="entity" value="rstroke"/>
        <figure>
          <graphic url="glyph-rstroke.png"/>
        </figure>
      </glyph>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2019-07-01" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GLYPH-egXML-hv">
      <glyph xml:id="fr_napos">
        <localProp name="nom" value="N latin minuscule précédé d'une apostrophe"/>
        <localProp name="entity" value="napos"/>
        <graphic url="glyph-napos.png"/>
      </glyph>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#D25-20"/>
  </listRef>
```

^b18

