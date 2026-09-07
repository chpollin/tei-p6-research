---
type: representation
source-type: document
source: '[[00_sources/tei-p5-colloc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 colloc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/colloc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# colloc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2917. Git blob: `8e5ca71d3787b43e0fbdfaac3981e4c45151b8ab`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-colloc" ident="colloc">
  <gloss versionDate="2005-01-14" xml:lang="en">collocate</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">연어</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">組合字</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">collocation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">colocación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">collocato</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">連語</gloss>
  <desc versionDate="2013-04-08" xml:lang="en">contains any sequence of words that co-occur with the headword with significant frequency.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표제어의 연어를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含標題字的組合字。</desc>
  <desc versionDate="2024-02-28" xml:lang="ja">見出し語と高い頻度で共起する任意の単語の連続を含む。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une collocation de l'entrée.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la colocación de un lema</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il collocato di un lemma.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.lexicalRefinement"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-colloc-egXML-mi" xml:lang="fr">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <colloc>de</colloc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-colloc-egXML-oe">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <colloc>de</colloc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-colloc-egXML-ki">
      <entry>
        <form>
          <orth>說</orth>
        </form>
        <gramGrp>
          <colloc>到</colloc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DITPGR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">collocate</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">연어</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">組合字</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">collocation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">colocación</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">collocato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">連語</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-08" xml:lang="en">contains any sequence of words that co-occur with the headword with significant frequency.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표제어의 연어를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含標題字的組合字。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">見出し語と高い頻度で共起する任意の単語の連続を含む。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une collocation de l'entrée.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la colocación de un lema</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il collocato di un lemma.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.lexicalRefinement"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-colloc-egXML-mi" xml:lang="fr">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <colloc>de</colloc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-colloc-egXML-oe">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <colloc>de</colloc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-colloc-egXML-ki">
      <entry>
        <form>
          <orth>說</orth>
        </form>
        <gramGrp>
          <colloc>到</colloc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPGR"/>
  </listRef>
```

^b20

