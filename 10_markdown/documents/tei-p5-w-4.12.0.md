---
type: representation
source-type: document
source: '[[00_sources/tei-p5-w-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 w
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/w.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# w

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5017. Git blob: `250be418731c110a223fe9936f8ee7a2f57fb114`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="gi-w" ident="w">
  <gloss versionDate="2005-01-14" xml:lang="en">word</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">단어</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">單字</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">mot</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">palabra</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">parola</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Wort</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a grammatical (not necessarily orthographic) word.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문법적 (반드시 철자상이 아닌) 단어를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示文法上 (但未必是拼字法上) 定義的單字。</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">文法上の語を示す(正書形である必要はない)。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente un mot grammatical (pas nécessairement orthographique).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa una palabra gramatical (no necesariamente ortográfica)</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta la parola grammaticale (non necessariamente in modo ortografico).</desc>
  <desc versionDate="2017-06-19" xml:lang="de">repräsentiert ein grammatisches (nicht unbedingt orthografisches) Wort.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.linguistic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <elementRef key="seg"/>
      <elementRef key="w"/>
      <elementRef key="m"/>
      <elementRef key="c"/>
      <elementRef key="pc"/>
      <classRef key="model.global"/>
      <classRef key="model.lPart"/>
      <classRef key="model.hiLike"/>
      <classRef key="model.pPart.edit"/>
    </alternate>
  </content>
  <exemplum versionDate="2018-02-15" xml:lang="en">
    <p>This example is adapted from the Folger Library’s Early Modern
    English Drama version of <ref target="https://emed.folger.edu/wits">The Wits: a Comedy</ref> by
    William Davenant.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-w-egXML-yw" source="#WD-TWac">
      <l>
        <w lemma="it" pos="pn" xml:id="A19883-003-a-0100">IT</w>
        <w lemma="have" pos="vvz" xml:id="A19883-003-a-0110">hath</w>
        <w lemma="be" pos="vvn" xml:id="A19883-003-a-0120">been</w>
        <w lemma="say" pos="vvn" xml:id="A19883-003-a-0130">said</w>
        <w lemma="of" pos="acp-p" xml:id="A19883-003-a-0140">of</w>
        <w lemma="old" pos="j" xml:id="A19883-003-a-0150">old</w>
        <pc xml:id="A19883-003-a-0160">,</pc>
        <w lemma="that" pos="cs" xml:id="A19883-003-a-0170">that</w>
        <w lemma="play" pos="vvz" xml:id="A19883-003-a-0180">
          <choice>
            <orig>Playes</orig>
            <reg>Plays</reg>
          </choice>
        </w>
        <w lemma="be" pos="vvb" xml:id="A19883-003-a-0190">are</w>
        <w lemma="feast" pos="n2" xml:id="A19883-003-a-0200">Feasts</w>
        <pc xml:id="A19883-003-a-0210">,</pc>
      </l>
      <l xml:id="A19883-e100220">
        <w lemma="poet" pos="n2" xml:id="A19883-003-a-0220">Poets</w>
        <w lemma="the" pos="d" xml:id="A19883-003-a-0230">the</w>
        <w lemma="cook" pos="n2" xml:id="A19883-003-a-0240">
          <choice>
            <orig>Cookes</orig>
            <reg>Cooks</reg>
          </choice>
        </w>
        <pc xml:id="A19883-003-a-0250">,</pc>
        <w lemma="and" pos="cc" xml:id="A19883-003-a-0260">and</w>
        <w lemma="the" pos="d" xml:id="A19883-003-a-0270">the</w>
        <w lemma="spectator" pos="n2" xml:id="A19883-003-a-0280">Spectators</w>
        <w lemma="guest" pos="n2" xml:id="A19883-003-a-0290">Guests</w>
        <pc xml:id="A19883-003-a-0300">,</pc>
      </l>
      <l xml:id="A19883-e100230">
        <w lemma="the" pos="d" xml:id="A19883-003-a-0310">The</w>
        <w lemma="actor" pos="n2" xml:id="A19883-003-a-0320">Actors</w>
        <w lemma="waiter" pos="n2" xml:id="A19883-003-a-0330">Waiters</w>
        <pc xml:id="A19883-003-a-0340">:</pc>
	<!-- ... -->
      </l>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#AILC"/>
    <ptr target="#AILALW"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">word</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">단어</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">單字</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">mot</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">palabra</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">parola</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Wort</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a grammatical (not necessarily orthographic) word.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문법적 (반드시 철자상이 아닌) 단어를 표시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示文法上 (但未必是拼字法上) 定義的單字。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">文法上の語を示す(正書形である必要はない)。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente un mot grammatical (pas nécessairement orthographique).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa una palabra gramatical (no necesariamente ortográfica)</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta la parola grammaticale (non necessariamente in modo ortografico).</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">repräsentiert ein grammatisches (nicht unbedingt orthografisches) Wort.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.linguistic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <elementRef key="seg"/>
      <elementRef key="w"/>
      <elementRef key="m"/>
      <elementRef key="c"/>
      <elementRef key="pc"/>
      <classRef key="model.global"/>
      <classRef key="model.lPart"/>
      <classRef key="model.hiLike"/>
      <classRef key="model.pPart.edit"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2018-02-15" xml:lang="en">
    <p>This example is adapted from the Folger Library’s Early Modern
    English Drama version of <ref target="https://emed.folger.edu/wits">The Wits: a Comedy</ref> by
    William Davenant.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-w-egXML-yw" source="#WD-TWac">
      <l>
        <w lemma="it" pos="pn" xml:id="A19883-003-a-0100">IT</w>
        <w lemma="have" pos="vvz" xml:id="A19883-003-a-0110">hath</w>
        <w lemma="be" pos="vvn" xml:id="A19883-003-a-0120">been</w>
        <w lemma="say" pos="vvn" xml:id="A19883-003-a-0130">said</w>
        <w lemma="of" pos="acp-p" xml:id="A19883-003-a-0140">of</w>
        <w lemma="old" pos="j" xml:id="A19883-003-a-0150">old</w>
        <pc xml:id="A19883-003-a-0160">,</pc>
        <w lemma="that" pos="cs" xml:id="A19883-003-a-0170">that</w>
        <w lemma="play" pos="vvz" xml:id="A19883-003-a-0180">
          <choice>
            <orig>Playes</orig>
            <reg>Plays</reg>
          </choice>
        </w>
        <w lemma="be" pos="vvb" xml:id="A19883-003-a-0190">are</w>
        <w lemma="feast" pos="n2" xml:id="A19883-003-a-0200">Feasts</w>
        <pc xml:id="A19883-003-a-0210">,</pc>
      </l>
      <l xml:id="A19883-e100220">
        <w lemma="poet" pos="n2" xml:id="A19883-003-a-0220">Poets</w>
        <w lemma="the" pos="d" xml:id="A19883-003-a-0230">the</w>
        <w lemma="cook" pos="n2" xml:id="A19883-003-a-0240">
          <choice>
            <orig>Cookes</orig>
            <reg>Cooks</reg>
          </choice>
        </w>
        <pc xml:id="A19883-003-a-0250">,</pc>
        <w lemma="and" pos="cc" xml:id="A19883-003-a-0260">and</w>
        <w lemma="the" pos="d" xml:id="A19883-003-a-0270">the</w>
        <w lemma="spectator" pos="n2" xml:id="A19883-003-a-0280">Spectators</w>
        <w lemma="guest" pos="n2" xml:id="A19883-003-a-0290">Guests</w>
        <pc xml:id="A19883-003-a-0300">,</pc>
      </l>
      <l xml:id="A19883-e100230">
        <w lemma="the" pos="d" xml:id="A19883-003-a-0310">The</w>
        <w lemma="actor" pos="n2" xml:id="A19883-003-a-0320">Actors</w>
        <w lemma="waiter" pos="n2" xml:id="A19883-003-a-0330">Waiters</w>
        <pc xml:id="A19883-003-a-0340">:</pc>
	<!-- ... -->
      </l>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AILC"/>
    <ptr target="#AILALW"/>
  </listRef>
```

^b19

