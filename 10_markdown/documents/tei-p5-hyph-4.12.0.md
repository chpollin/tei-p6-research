---
type: representation
source-type: document
source: '[[00_sources/tei-p5-hyph-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 hyph
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/hyph.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# hyph

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3380. Git blob: `fab23261c86a7596c45dc9cf9cb9b7ca9b56e71f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-hyph" ident="hyph">
  <gloss versionDate="2005-01-14" xml:lang="en">hyphenation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">하이픈으로 연결하기</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">連字符號</gloss>
  <gloss versionDate="2009-04-07" xml:lang="fr">syllabation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">uso del guión</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">utilizzo del trattino</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a hyphenated form of a dictionary headword, or hyphenation information in some
    other form.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전표제어의 하이픈 연결 형식 또는 다른 형식의 하이픈연결 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個標題字的連字符號形式，或者以其他形式呈現的連字符號資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書の見出しにあるハイフン付き語形、または他の語形にあるハイフン情報 を示す。</desc>
  <desc versionDate="2009-04-07" xml:lang="fr">contient une entrée de dictionnaire comportant des
    marques de césure sous forme de traits d'union ou sous d'autres formes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene alguna forma de uso del guión en el lema de una
    entrada de diccionario, o información relativa al usa del guión.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una forma del lemma separata da un trattino, o
    informazioni sull'uso del trattino in qualche altra forma.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.formPart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyph-egXML-tr">
      <entry>
        <form>
          <orth>competitor</orth>
          <hyph>com|peti|tor</hyph>
          <pron>k@m"petit@(r)</pron>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyph-egXML-yd">
      <entry>
        <form>
          <orth>demi-dieu</orth>
          <hyph>demi|dieu</hyph>
          <pron>[d(th)midjø]</pron>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyph-egXML-tj">
      <entry>
        <form>
          <orth>音</orth>
          <hyph>( 因漢字無法以連字符號拆解，故不提供範例。)</hyph>
          <pron>yin</pron>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DITPFO"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">hyphenation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">하이픈으로 연결하기</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">連字符號</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-04-07" xml:lang="fr">syllabation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">uso del guión</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">utilizzo del trattino</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a hyphenated form of a dictionary headword, or hyphenation information in some
    other form.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전표제어의 하이픈 연결 형식 또는 다른 형식의 하이픈연결 정보를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個標題字的連字符號形式，或者以其他形式呈現的連字符號資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書の見出しにあるハイフン付き語形、または他の語形にあるハイフン情報 を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-07" xml:lang="fr">contient une entrée de dictionnaire comportant des
    marques de césure sous forme de traits d'union ou sous d'autres formes.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene alguna forma de uso del guión en el lema de una
    entrada de diccionario, o información relativa al usa del guión.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una forma del lemma separata da un trattino, o
    informazioni sull'uso del trattino in qualche altra forma.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.formPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyph-egXML-tr">
      <entry>
        <form>
          <orth>competitor</orth>
          <hyph>com|peti|tor</hyph>
          <pron>k@m"petit@(r)</pron>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyph-egXML-yd">
      <entry>
        <form>
          <orth>demi-dieu</orth>
          <hyph>demi|dieu</hyph>
          <pron>[d(th)midjø]</pron>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyph-egXML-tj">
      <entry>
        <form>
          <orth>音</orth>
          <hyph>( 因漢字無法以連字符號拆解，故不提供範例。)</hyph>
          <pron>yin</pron>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO"/>
  </listRef>
```

^b19

