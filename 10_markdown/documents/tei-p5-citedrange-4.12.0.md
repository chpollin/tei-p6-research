---
type: representation
source-type: document
source: '[[00_sources/tei-p5-citedrange-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 citedRange
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/citedRange.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# citedRange

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2730. Git blob: `2b3cbccb4db72564c01d561adfcfe43210e7f309`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-citedRange" ident="citedRange">
  <gloss versionDate="2012-12-13" xml:lang="en">cited range</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">引用範囲</gloss>
  <desc versionDate="2012-12-13" xml:lang="en">defines the range of cited content, often represented by pages or other units.</desc>
  <desc versionDate="2024-02-28" xml:lang="ja">しばしばページやその他の単位で表される、引用の範囲を定める。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citing"/>
    <memberOf key="att.pointing"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citedRange-egXML-we">
      <citedRange>pp 12–13</citedRange>
      <citedRange unit="page" from="12" to="13"/>
      <citedRange unit="volume">II</citedRange>
      <citedRange unit="page">12</citedRange>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citedRange-egXML-yk">
      <bibl><ptr target="#mueller01"/>, <citedRange target="http://example.com/mueller3.xml#page4">vol. 3, pp.
        4-5</citedRange></bibl>
    </egXML>
  </exemplum>
  <remarks ident="citedRange-remarks" versionDate="2017-03-29" xml:lang="en">
    <p>When a single page is being cited, use the <att>from</att> and <att>to</att> attributes with
      an identical value. When no clear endpoint is provided, the <att>from</att> attribute may be
      used without <att>to</att>; for example a citation such as <q>p. 3ff</q> might be encoded
      <code>&lt;citedRange from="3"&gt;p. 3ff&lt;/citedRange&gt;</code>.</p>
  </remarks>
  <remarks ident="citedRange-remarks" versionDate="2024-02-28" xml:lang="ja"><p>1頁だけ引用された時は、同一の値を伴う<att>from</att>と<att>to</att>の属性を用いる。引用の終わりが与えられていない場合は、<att>from</att>属性は、<att>to</att>なしで用いることが許されている。例えば、<q>p. 3ff</q>のような引用は<code>&lt;citedRange from="3"&gt;p. 3ff&lt;/citedRange&gt;</code>と符号化されうる。</p></remarks>
  <listRef>
    <ptr target="#COBICOB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2012-12-13" xml:lang="en">cited range</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">引用範囲</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-13" xml:lang="en">defines the range of cited content, often represented by pages or other units.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">しばしばページやその他の単位で表される、引用の範囲を定める。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citing"/>
    <memberOf key="att.pointing"/>
    <memberOf key="model.biblPart"/>
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
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citedRange-egXML-we">
      <citedRange>pp 12–13</citedRange>
      <citedRange unit="page" from="12" to="13"/>
      <citedRange unit="volume">II</citedRange>
      <citedRange unit="page">12</citedRange>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citedRange-egXML-yk">
      <bibl><ptr target="#mueller01"/>, <citedRange target="http://example.com/mueller3.xml#page4">vol. 3, pp.
        4-5</citedRange></bibl>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="citedRange-remarks" versionDate="2017-03-29" xml:lang="en">
    <p>When a single page is being cited, use the <att>from</att> and <att>to</att> attributes with
      an identical value. When no clear endpoint is provided, the <att>from</att> attribute may be
      used without <att>to</att>; for example a citation such as <q>p. 3ff</q> might be encoded
      <code>&lt;citedRange from="3"&gt;p. 3ff&lt;/citedRange&gt;</code>.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="citedRange-remarks" versionDate="2024-02-28" xml:lang="ja"><p>1頁だけ引用された時は、同一の値を伴う<att>from</att>と<att>to</att>の属性を用いる。引用の終わりが与えられていない場合は、<att>from</att>属性は、<att>to</att>なしで用いることが許されている。例えば、<q>p. 3ff</q>のような引用は<code>&lt;citedRange from="3"&gt;p. 3ff&lt;/citedRange&gt;</code>と符号化されうる。</p></remarks>
```

^b10

### Block 11

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOB"/>
  </listRef>
```

^b11

