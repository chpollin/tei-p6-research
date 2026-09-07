---
type: representation
source-type: document
source: '[[00_sources/tei-p5-cl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 cl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/cl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# cl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3856. Git blob: `e5ba7f6e8049b33083c4f1ddb7114aa0edbd9864`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="gi-cl" ident="cl">
  <gloss versionDate="2005-01-14" xml:lang="en">clause</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">절</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">子句</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">cláusula</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">frase</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">節</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a grammatical clause.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문법적인 절을 표시한다.</desc>
  <gloss versionDate="2009-02-13" xml:lang="fr">proposition</gloss>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個文法上的子句。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">言語学上の節を示す。</desc>
  <desc versionDate="2009-02-13" xml:lang="fr">représente une proposition grammaticale.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa una cláusula gramatical.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresnta la frase grammaticale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum versionDate="2022-11-30" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cl-egXML-jr">
      <l><cl type="relative" function="clause_modifier">Which frightened
          both the heroes so,</cl></l>
      <l><cl>They quite forgot their quarrel.</cl></l>
    </egXML>
  </exemplum>
  <exemplum versionDate="2022-11-30" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cl-egXML-ny">
      <cl>Il nous rejoindra dans
          les jours
      <cl type="relative" function="proposition_relative_déterminative">qui viennent.</cl>
      </cl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cl-egXML-mm">
      <cl type="相關" function="修飾子句">最終他還是原諒了他，<cl>那個曾經陷他於不義的人。</cl>
         </cl>
    </egXML>
  </exemplum>
  <remarks ident="cl-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <att>type</att> attribute may be used to indicate the
type of clause, taking values such as  <val>finite</val>, <val>nonfinite</val>,
<val>declarative</val>, <val>interrogative</val>, <val>relative</val>
etc. as appropriate.</p>
  </remarks>
  <remarks ident="cl-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'attribut <att>type</att> peut être utilisé pour indiquer le type de proposition, avec des valeurs telles que <val>subordonnée</val>, <val>infinitive</val>,
<val>declarative</val>, <val>interrogative</val>, <val>relative</val> etc.</p>
  </remarks>
  <remarks ident="cl-remarks" versionDate="2024-02-28" xml:lang="ja">
    <p><att>type</att> 属性は節のタイプを示すのに用いることができる。
      内容に応じて <val>finite</val>（定形）、<val>nonfinite</val>（不定形）、<val>declarative</val>（平叙）、
      <val>interrogative</val>（疑問）、<val>relative</val>（連体修飾）などの値をとる。</p>
  </remarks>
  <listRef>
    <ptr target="#AILC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">clause</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">절</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">子句</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">cláusula</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">frase</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">節</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a grammatical clause.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문법적인 절을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2009-02-13" xml:lang="fr">proposition</gloss>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個文法上的子句。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">言語学上の節を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-02-13" xml:lang="fr">représente une proposition grammaticale.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa una cláusula gramatical.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresnta la frase grammaticale.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2022-11-30" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cl-egXML-jr">
      <l><cl type="relative" function="clause_modifier">Which frightened
          both the heroes so,</cl></l>
      <l><cl>They quite forgot their quarrel.</cl></l>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2022-11-30" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cl-egXML-ny">
      <cl>Il nous rejoindra dans
          les jours
      <cl type="relative" function="proposition_relative_déterminative">qui viennent.</cl>
      </cl>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cl-egXML-mm">
      <cl type="相關" function="修飾子句">最終他還是原諒了他，<cl>那個曾經陷他於不義的人。</cl>
         </cl>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="cl-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <att>type</att> attribute may be used to indicate the
type of clause, taking values such as  <val>finite</val>, <val>nonfinite</val>,
<val>declarative</val>, <val>interrogative</val>, <val>relative</val>
etc. as appropriate.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="cl-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'attribut <att>type</att> peut être utilisé pour indiquer le type de proposition, avec des valeurs telles que <val>subordonnée</val>, <val>infinitive</val>,
<val>declarative</val>, <val>interrogative</val>, <val>relative</val> etc.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="cl-remarks" versionDate="2024-02-28" xml:lang="ja">
    <p><att>type</att> 属性は節のタイプを示すのに用いることができる。
      内容に応じて <val>finite</val>（定形）、<val>nonfinite</val>（不定形）、<val>declarative</val>（平叙）、
      <val>interrogative</val>（疑問）、<val>relative</val>（連体修飾）などの値をとる。</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AILC"/>
  </listRef>
```

^b23

