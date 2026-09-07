---
type: representation
source-type: document
source: '[[00_sources/tei-p5-lacunaend-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 lacunaEnd
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/lacunaEnd.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# lacunaEnd

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2288. Git blob: `5993135f6fa295a2a25c846418efc222007a0d29`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-lacunaEnd" ident="lacunaEnd">
  <gloss versionDate="2020-12-20" xml:lang="en">lacuna end</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">fin d'une lacune</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates the end of a lacuna in a mostly complete textual
witness.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">거의 완성된 비교 대상 텍스트의 공백부 종료를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出於大致完整的文字版本中，一個缺文的結束。</desc>
  <desc versionDate="2008-04-21" xml:lang="ja">殆ど完全である文献中にある脱文の終わりを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique la fin d'une lacune dans le texte d'un
			témoin textuel quasiment complet.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el fin de una laguna en un texto casi completo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica la fine di una lacuna nel testo di un testimone quasi completo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.rdgPart"/>
    <memberOf key="model.rdgPart"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lacunaEnd-egXML-ju">
      <rdg wit="#X"><lacunaEnd/>auctorite</rdg>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lacunaEnd-egXML-zl">
      <rdg wit="#fr_X"><lacunaEnd/>auctorite</rdg>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lacunaEnd-egXML-ta">
      <rdg wit="#X"><lacunaEnd/>傀</rdg>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">lacuna end</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">fin d'une lacune</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the end of a lacuna in a mostly complete textual
witness.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">거의 완성된 비교 대상 텍스트의 공백부 종료를 표시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出於大致完整的文字版本中，一個缺文的結束。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-21" xml:lang="ja">殆ど完全である文献中にある脱文の終わりを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la fin d'une lacune dans le texte d'un
			témoin textuel quasiment complet.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el fin de una laguna en un texto casi completo.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la fine di una lacuna nel testo di un testimone quasi completo.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.rdgPart"/>
    <memberOf key="model.rdgPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lacunaEnd-egXML-ju">
      <rdg wit="#X"><lacunaEnd/>auctorite</rdg>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lacunaEnd-egXML-zl">
      <rdg wit="#fr_X"><lacunaEnd/>auctorite</rdg>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lacunaEnd-egXML-ta">
      <rdg wit="#X"><lacunaEnd/>傀</rdg>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
```

^b15

