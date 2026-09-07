---
type: representation
source-type: document
source: '[[00_sources/tei-p5-rb-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 rb
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/rb.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# rb

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1628. Git blob: `c6db9ca52eb74a48188a57174d3d11181d472d44`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="rb" xml:id="gi-rb" module="core">
  <gloss versionDate="2021-01-30" xml:lang="en">ruby base</gloss>
  <gloss versionDate="2021-01-31" xml:lang="ja">ルビの対象となるテキスト。</gloss>
  <desc versionDate="2020-02-28" xml:lang="en">contains the
    base text annotated by a ruby gloss.</desc>
  <desc versionDate="2021-01-31" xml:lang="ja">一つ以上のルビの対象となるテキストを含む。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
      <macroRef key="macro.phraseSeq"/>
  </content>
  <!-- More examples to be added. -->
    <exemplum versionDate="2021-02-02" xml:lang="mul">
      <p>The word <mentioned>你 好</mentioned> <mentioned>nǐ hǎo</mentioned>
        (hello) is glossed in pinyin to provide a pronunciation guide.</p>
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rb-egXML-pg">
        <p xml:lang="zh">
          <!--...-->
          <ruby><rb>你</rb><rt place="above">nǐ</rt></ruby>
          <ruby><rb>好</rb><rt place="above">hǎo</rt></ruby>
          <!--...-->
        </p>
        
    </egXML></exemplum>
  
  <listRef>
    <ptr target="#COHTGRB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2021-01-30" xml:lang="en">ruby base</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2021-01-31" xml:lang="ja">ルビの対象となるテキスト。</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-02-28" xml:lang="en">contains the
    base text annotated by a ruby gloss.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2021-01-31" xml:lang="ja">一つ以上のルビの対象となるテキストを含む。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
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

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2021-02-02" xml:lang="mul">
      <p>The word <mentioned>你 好</mentioned> <mentioned>nǐ hǎo</mentioned>
        (hello) is glossed in pinyin to provide a pronunciation guide.</p>
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rb-egXML-pg">
        <p xml:lang="zh">
          <!--...-->
          <ruby><rb>你</rb><rt place="above">nǐ</rt></ruby>
          <ruby><rb>好</rb><rt place="above">hǎo</rt></ruby>
          <!--...-->
        </p>
        
    </egXML></exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHTGRB"/>
  </listRef>
```

^b8

