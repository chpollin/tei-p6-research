---
type: representation
source-type: document
source: '[[00_sources/tei-p5-number-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 number
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/number.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# number

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3434. Git blob: `637a9fabd2303048afea60d0ee173a0a1e90287e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-number" ident="number">
  <gloss versionDate="2007-06-12" xml:lang="en">number</gloss>
  <equiv name="grammaticalNumber" uri="http://www.tc37sc4.org"/>
  <gloss versionDate="2007-06-12" xml:lang="fr">nombre</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates grammatical number associated with a form, as given in a dictionary.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 형태와 관련된 문법적 수를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出單複數形式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書において、語形と関連する文法上の数を示す。</desc>
  <desc versionDate="2009-04-08" xml:lang="fr">indique le nombre grammatical associé à une forme, telle qu'elle est donnée par le dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el número gramatical asociado a una palabra, como viene dado en el diccionario.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica il numero grammaticale associato ad una forma, secondo la modalità del dizionario.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-number-egXML-eu">
      <entry>
        <form>
          <orth>wits</orth>
          <pron>wIts</pron>
        </form>
        <gramGrp>
          <number>pl</number>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-number-egXML-bp">
      <entry>
        <form>
          <orth>épousailles</orth>
          <pron>[epuzaj]</pron>
        </form>
        <gramGrp>
          <number>pl.</number>
          <pos>n.</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-number-egXML-ag">
      <entry>
        <form>
          <orth>wits</orth>
          <pron>wIts</pron>
        </form>
        <gramGrp>
          <number>複數</number>
          <pos>名詞</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="number-remarks" versionDate="2011-04-13" xml:lang="en">
    <p>This element is synonymous with <tag>gram type="num"</tag>.</p>
  </remarks>
  <remarks ident="number-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est synonyme de <tag>gram type="num"</tag>.</p>
  </remarks>
  <remarks ident="number-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、<tag>gram type="num"</tag>と同義である。 </p>
  </remarks>
  <listRef>
    <ptr target="#DITPFO" type="div2"/>
    <ptr target="#DITPGR" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">number</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/equiv[1]`.

```xml
<equiv name="grammaticalNumber" uri="http://www.tc37sc4.org"/>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">nombre</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates grammatical number associated with a form, as given in a dictionary.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 형태와 관련된 문법적 수를 표시한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出單複數形式。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書において、語形と関連する文法上の数を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">indique le nombre grammatical associé à une forme, telle qu'elle est donnée par le dictionnaire.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el número gramatical asociado a una palabra, como viene dado en el diccionario.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il numero grammaticale associato ad una forma, secondo la modalità del dizionario.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
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
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-number-egXML-eu">
      <entry>
        <form>
          <orth>wits</orth>
          <pron>wIts</pron>
        </form>
        <gramGrp>
          <number>pl</number>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-number-egXML-bp">
      <entry>
        <form>
          <orth>épousailles</orth>
          <pron>[epuzaj]</pron>
        </form>
        <gramGrp>
          <number>pl.</number>
          <pos>n.</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-number-egXML-ag">
      <entry>
        <form>
          <orth>wits</orth>
          <pron>wIts</pron>
        </form>
        <gramGrp>
          <number>複數</number>
          <pos>名詞</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="number-remarks" versionDate="2011-04-13" xml:lang="en">
    <p>This element is synonymous with <tag>gram type="num"</tag>.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="number-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est synonyme de <tag>gram type="num"</tag>.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="number-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、<tag>gram type="num"</tag>と同義である。 </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO" type="div2"/>
    <ptr target="#DITPGR" type="div2"/>
  </listRef>
```

^b19

