---
type: representation
source-type: document
source: '[[00_sources/tei-p5-rt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 rt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/rt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# rt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5877. Git blob: `6a4fb3fec292a046e155a91e526c1ff4595896ba`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="rt" xml:id="gi-rt" module="core">
  <gloss versionDate="2021-01-30" xml:lang="en">ruby text</gloss>
  <gloss versionDate="2021-01-31" xml:lang="ja">ルビのテキスト。</gloss>
  <desc versionDate="2020-02-28" xml:lang="en">contains a ruby
    text, an annotation closely associated with a passage of the
    main text.</desc>
  <desc versionDate="2021-01-31" xml:lang="ja">本文の一部と密接な関連を持つ注釈（主に読み方）としてのルビテキストを含む。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
      <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="target" usage="opt">
      <desc versionDate="2021-01-08" xml:lang="en">supplies a pointer to the
        base being glossed by this ruby text.</desc>
      <desc versionDate="2021-01-31" xml:lang="ja">ルビテキストの対象へのポインタを示す。</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <constraintSpec scheme="schematron" ident="rt-target-not-span" xml:lang="en">
        <!-- Note: this constraint should not be necessary, as the
             desired semantics should be something we could describe
             in PureODD using attList/@org. But I don’t think we
             can. —Syd -->
        <desc>Enforce that <emph>either</emph>
          <att>target</att> or both <att>from</att> and
          <att>to</att> (or none) are used, but not
          <att>target</att> in combination with either
          <att>from</att> or <att>to</att>.</desc>
        <constraint>
          <sch:rule context="tei:rt/@target">
            <sch:report test="../@from | ../@to">When @target is present, neither @from nor @to should be.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <remarks ident="rt-attr.target-remarks" versionDate="2020-02-01" xml:lang="en">
        <p>Should point to a single <gi>rb</gi> or an element
          that is inside an <gi>rb</gi>. To refer to multiple
          elements or text nodes at once use <att>from</att> and
          <att>to</att>.</p>
      </remarks>
    </attDef>
    <attDef ident="from" usage="opt">
      <desc versionDate="2021-01-06" xml:lang="en">points to the starting point of the span of text
        being glossed by this ruby text.</desc>
      <desc versionDate="2021-01-31" xml:lang="ja">ルビテキストの対象範囲の始点を示す。</desc>
      <datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
      <constraintSpec scheme="schematron" ident="rt-from" xml:lang="en">
        <!-- Note: this constraint should not be necessary, as the
             desired semantics should be something we could describe
             in PureODD using attList/@org. But I don’t think we
             can. —Syd -->
        <desc>Enforce the presence of <att>to</att> iff there
          is a <att>from</att>.</desc>
        <constraint>
          <sch:rule context="tei:rt/@from">
            <sch:assert test="../@to">When @from is present, the @to attribute of &lt;<sch:name/>> is required.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </attDef>
    <attDef ident="to" usage="opt">
      <desc versionDate="2021-01-06" xml:lang="en">points to the ending point of the span of text
        being glossed.</desc>
      <desc versionDate="2021-01-31" xml:lang="ja">ルビテキストの対象範囲の終点を示す。</desc>
      <datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
      <constraintSpec scheme="schematron" ident="rt-to" xml:lang="en">
        <!-- Note: this constraint should not be necessary, as the
             desired semantics should be something we could describe
             in PureODD using attList/@org. But I don’t think we
             can. —Syd -->
        <desc>Enforce the presence of <att>from</att> iff there
          is a <att>to</att>.</desc>
        <constraint>
          <sch:rule context="tei:rt/@to">
            <sch:assert test="../@from">When @to is present, the @from attribute of &lt;<sch:name/>> is required.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </attDef>
  </attList>
  <!-- More examples to be added. -->
  <exemplum versionDate="2021-02-01" xml:lang="mul">
    <p>The word <mentioned>大統領</mentioned> <mentioned>daitōryō</mentioned>
      (president) is glossed character by character in hiragana to provide a pronunciation guide.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rt-egXML-py">
      <p style="writing-mode: vertical-rl" xml:lang="ja"> 
        <!--...-->
        <ruby><rb>大</rb><rt place="right">だい</rt></ruby>
        <ruby><rb>統</rb><rt place="right">とう</rt></ruby>
        <ruby><rb>領</rb><rt place="right">りょう</rt></ruby>
        <!--...-->
      </p>
    </egXML>
  </exemplum>
  <remarks ident="rt-remarks" versionDate="2021-02-02" xml:lang="en">
    <p>Where the <att>place</att> attribute is not provided on the <gi>rt</gi>
      element, the default assumption is that the 
      ruby gloss is <val>above</val> where the text is horizontal, and to the
      <val>right</val> of the text where it is vertical. </p>
  </remarks>
  <listRef>
    <ptr target="#COHTGRB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2021-01-30" xml:lang="en">ruby text</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2021-01-31" xml:lang="ja">ルビのテキスト。</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-02-28" xml:lang="en">contains a ruby
    text, an annotation closely associated with a passage of the
    main text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2021-01-31" xml:lang="ja">本文の一部と密接な関連を持つ注釈（主に読み方）としてのルビテキストを含む。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
      <macroRef key="macro.phraseSeq"/>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2021-01-08" xml:lang="en">supplies a pointer to the
        base being glossed by this ruby text.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2021-01-31" xml:lang="ja">ルビテキストの対象へのポインタを示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="rt-target-not-span" xml:lang="en">
        <!-- Note: this constraint should not be necessary, as the
             desired semantics should be something we could describe
             in PureODD using attList/@org. But I don’t think we
             can. —Syd -->
        <desc>Enforce that <emph>either</emph>
          <att>target</att> or both <att>from</att> and
          <att>to</att> (or none) are used, but not
          <att>target</att> in combination with either
          <att>from</att> or <att>to</att>.</desc>
        <constraint>
          <sch:rule context="tei:rt/@target">
            <sch:report test="../@from | ../@to">When @target is present, neither @from nor @to should be.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="rt-attr.target-remarks" versionDate="2020-02-01" xml:lang="en">
        <p>Should point to a single <gi>rb</gi> or an element
          that is inside an <gi>rb</gi>. To refer to multiple
          elements or text nodes at once use <att>from</att> and
          <att>to</att>.</p>
      </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2021-01-06" xml:lang="en">points to the starting point of the span of text
        being glossed by this ruby text.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2021-01-31" xml:lang="ja">ルビテキストの対象範囲の始点を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[2]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="rt-from" xml:lang="en">
        <!-- Note: this constraint should not be necessary, as the
             desired semantics should be something we could describe
             in PureODD using attList/@org. But I don’t think we
             can. —Syd -->
        <desc>Enforce the presence of <att>to</att> iff there
          is a <att>from</att>.</desc>
        <constraint>
          <sch:rule context="tei:rt/@from">
            <sch:assert test="../@to">When @from is present, the @to attribute of &lt;<sch:name/>> is required.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2021-01-06" xml:lang="en">points to the ending point of the span of text
        being glossed.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2021-01-31" xml:lang="ja">ルビテキストの対象範囲の終点を示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[3]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="rt-to" xml:lang="en">
        <!-- Note: this constraint should not be necessary, as the
             desired semantics should be something we could describe
             in PureODD using attList/@org. But I don’t think we
             can. —Syd -->
        <desc>Enforce the presence of <att>from</att> iff there
          is a <att>to</att>.</desc>
        <constraint>
          <sch:rule context="tei:rt/@to">
            <sch:assert test="../@from">When @to is present, the @from attribute of &lt;<sch:name/>> is required.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2021-02-01" xml:lang="mul">
    <p>The word <mentioned>大統領</mentioned> <mentioned>daitōryō</mentioned>
      (president) is glossed character by character in hiragana to provide a pronunciation guide.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rt-egXML-py">
      <p style="writing-mode: vertical-rl" xml:lang="ja"> 
        <!--...-->
        <ruby><rb>大</rb><rt place="right">だい</rt></ruby>
        <ruby><rb>統</rb><rt place="right">とう</rt></ruby>
        <ruby><rb>領</rb><rt place="right">りょう</rt></ruby>
        <!--...-->
      </p>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="rt-remarks" versionDate="2021-02-02" xml:lang="en">
    <p>Where the <att>place</att> attribute is not provided on the <gi>rt</gi>
      element, the default assumption is that the 
      ruby gloss is <val>above</val> where the text is horizontal, and to the
      <val>right</val> of the text where it is vertical. </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHTGRB"/>
  </listRef>
```

^b22

