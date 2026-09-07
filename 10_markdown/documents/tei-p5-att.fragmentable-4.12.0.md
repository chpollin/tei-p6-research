---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.fragmentable-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.fragmentable
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.fragmentable.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.fragmentable

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4765. Git blob: `a3e63925a48c1b15a2b487a00d66bd9d4b1da25e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" ident="att.fragmentable">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes for representing
    fragmentation of a structural element, typically as 
  a consequence of some overlapping hierarchy.</desc>
  <desc versionDate="2019-06-16" xml:lang="ja">通常は階層関係のオーバーラップなどに起因する、構造を持つ要素の断片化を表現するための属性を与える。</desc>
  <attList>
    <attDef ident="part" usage="opt">
      <desc versionDate="2013-06-21" xml:lang="en">specifies whether or not its parent element is fragmented
      in some way, typically by some other overlapping structure: for
      example a speech which is divided between two or more verse
      stanzas, a paragraph which is split across a page division, a
      verse line which is divided between two speakers.</desc>
      <desc versionDate="2019-06-16" xml:lang="ja">通常は他の階層関係のオーバーラップなどに起因して、親要素が何らかの形で断片化されているかどうかを示す。例えば、二つ以上の韻文詩で分割された発話、頁区切りをまたぐ段落、二人の話者に分割された韻文の一行など。</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <!--@validUntil not allowed on defaultVal. Still working on a way to deprecate this.-->
      <!--<defaultVal validUntil="2017-06-03">N</defaultVal>-->
      <defaultVal>N</defaultVal>
      <valList type="closed">
        <valItem ident="Y">
          <gloss versionDate="2013-01-07" xml:lang="en">yes</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">はい</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">the element is fragmented in some (unspecified) respect</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">要素はいくつかの（不特定の）点で断片化されている。</desc>
        </valItem>
        <valItem ident="N">
          <gloss versionDate="2013-01-07" xml:lang="en">no</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">いいえ</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">the element is not fragmented, or no claim is made as to its completeness</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">要素が断片化されていないか、または完全性についての主張はない。</desc>
        </valItem>
        <valItem ident="I">
          <gloss versionDate="2013-01-07" xml:lang="en">initial</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">最初の</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">this is the initial part of a fragmented element</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">これは断片化された要素の最初の部分を示す。</desc>
        </valItem>
        <valItem ident="M">
          <gloss versionDate="2013-01-07" xml:lang="en">medial</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">中間の</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">this is a medial part of a fragmented element</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">これは断片化された要素の中間の部分を示す。</desc>
        </valItem>
        <valItem ident="F">
          <gloss versionDate="2013-01-07" xml:lang="en">final</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">最後の</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">this is the final part of a fragmented element</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">これは断片化された要素の最後の部分を示す。</desc>
        </valItem>
      </valList>
      <remarks ident="att.fragmentable-attr.part-remarks" versionDate="2013-01-07" xml:lang="en">
        <p>The values <val>I</val>, <val>M</val>, or <val>F</val>
        should be used only where it is clear how the element may
        be reconstituted.</p>
      </remarks>
      <remarks ident="att.fragmentable-attr.part-remarks" versionDate="2019-06-08" xml:lang="ja"><p><val>I</val>、<val>M</val>、または<val>F</val>という値は、要素の再構成方法が明らかな場合にのみ使用する。</p></remarks>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes for representing
    fragmentation of a structural element, typically as 
  a consequence of some overlapping hierarchy.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-06-16" xml:lang="ja">通常は階層関係のオーバーラップなどに起因する、構造を持つ要素の断片化を表現するための属性を与える。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-06-21" xml:lang="en">specifies whether or not its parent element is fragmented
      in some way, typically by some other overlapping structure: for
      example a speech which is divided between two or more verse
      stanzas, a paragraph which is split across a page division, a
      verse line which is divided between two speakers.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2019-06-16" xml:lang="ja">通常は他の階層関係のオーバーラップなどに起因して、親要素が何らかの形で断片化されているかどうかを示す。例えば、二つ以上の韻文詩で分割された発話、頁区切りをまたぐ段落、二人の話者に分割された韻文の一行など。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>N</defaultVal>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="Y">
          <gloss versionDate="2013-01-07" xml:lang="en">yes</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">はい</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">the element is fragmented in some (unspecified) respect</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">要素はいくつかの（不特定の）点で断片化されている。</desc>
        </valItem>
        <valItem ident="N">
          <gloss versionDate="2013-01-07" xml:lang="en">no</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">いいえ</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">the element is not fragmented, or no claim is made as to its completeness</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">要素が断片化されていないか、または完全性についての主張はない。</desc>
        </valItem>
        <valItem ident="I">
          <gloss versionDate="2013-01-07" xml:lang="en">initial</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">最初の</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">this is the initial part of a fragmented element</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">これは断片化された要素の最初の部分を示す。</desc>
        </valItem>
        <valItem ident="M">
          <gloss versionDate="2013-01-07" xml:lang="en">medial</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">中間の</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">this is a medial part of a fragmented element</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">これは断片化された要素の中間の部分を示す。</desc>
        </valItem>
        <valItem ident="F">
          <gloss versionDate="2013-01-07" xml:lang="en">final</gloss>
          <gloss versionDate="2019-06-08" xml:lang="ja">最後の</gloss>
          <desc versionDate="2013-01-07" xml:lang="en">this is the final part of a fragmented element</desc>
          <desc versionDate="2019-06-08" xml:lang="ja">これは断片化された要素の最後の部分を示す。</desc>
        </valItem>
      </valList>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.fragmentable-attr.part-remarks" versionDate="2013-01-07" xml:lang="en">
        <p>The values <val>I</val>, <val>M</val>, or <val>F</val>
        should be used only where it is clear how the element may
        be reconstituted.</p>
      </remarks>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.fragmentable-attr.part-remarks" versionDate="2019-06-08" xml:lang="ja"><p><val>I</val>、<val>M</val>、または<val>F</val>という値は、要素の再構成方法が明らかな場合にのみ使用する。</p></remarks>
```

^b9

