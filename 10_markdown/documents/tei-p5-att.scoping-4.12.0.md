---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.scoping-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.scoping
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.scoping.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.scoping

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5099. Git blob: `a6028160f8057b4e78261c66ff770728a22ece0f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" xml:id="class-attr-scoping" ident="att.scoping">
  <desc versionDate="2016-03-15" xml:lang="en">provides attributes for selecting particular elements
    within a document.</desc>
  <desc versionDate="2023-09-27" xml:lang="ja">ある文書の中の特定の要素を選択するための属性を提供する。</desc>
  <attList>
    <attDef ident="target" usage="opt">
      <desc versionDate="2021-01-30" xml:lang="en">points at one or more sets of zero or more elements each.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">ある文書の中の特定の要素を選択するための属性を提供する。</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scoping-egXML-cd">Elizabeth went to <persName xml:id="ESSEX">Essex</persName>
          <certainty target="#ESSEX" locus="name" degree="0.6"/>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="match" usage="opt">
      <desc versionDate="2021-01-30" xml:lang="en">supplies an XPath selection pattern using the
        syntax defined in <ptr target="#XSLT3"/> which identifies a set of nodes, selected within
        the context identified by the <att>target</att> attribute if this is supplied, or within the 
        context of the parent element if it is not.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja"><ptr target="#XSLT3"/>に定義された構文を用いて、ノードの集合を指し示す任意の XPath 式を記入する。
        選択範囲は <att>target</att> 属性が与えられた場合はそのコンテクスト、
        なければ親要素のコンテクストとなる。</desc>
      <datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scoping-egXML-pq" source="#UND">
          <gap reason="cancelled">
            <certainty match="@reason" locus="value" cert="low"/>
          </gap>
        </egXML>
      </exemplum>
    </attDef>
  </attList>
  <remarks ident="att.scoping-remarks" versionDate="2021-01-30" xml:lang="en">
    <p>The semantics of this element apply to the nodeset identified by the value of the
      <att>target</att> attribute, possibly modified by the value of the
      <att>match</att> attribute. If more than one identifier is given, the implication is
      that all elements (or nodesets) are intended. The <att>match</att> attribute may also be
      used as a means of identifying groups of elements. </p>
    <p>If <att>target</att> and <att>match</att> are present, <att>target</att> selects an
      element and the XPath expression in <att>match</att> is evaluated in the context of that
      element. If neither attribute is present, the expression applies to its parent element. If
      only <att>target</att> is given, the expression refers to the selected element or nodeset.
      If only <att>match</att> is given, the XPath expression is evaluated in the context of the
      parent element of the bearing element. </p>
    <p>Note that the value of the <att>target</att> attribute may include an XPointer expression
      including an XPath expression (see <ptr target="#SATS"/>). </p>
  </remarks>
  <remarks ident="att.scoping-remarks" versionDate="2023-09-27" xml:lang="ja"><p>確信度の表現は <att>target</att> 属性の値で指定されたノードセットに適用されるが、加えて <att>match</att> 属性の値によって修正されることがある。
    複数の識別子が与えられた場合、それらすべての要素（またはノードセット）を指すものと解される。
    <att>match</att> 属性は要素のグループを指定するために用いることもできる。</p>
    <p><att>target</att> と <att>match</att> 両方がある場合、<att>match</att> の XPath 式は <att>target</att> で選択した要素のコンテクスト内で評価される。どちらの属性もない場合、表現は親要素に適用される。
      <att>target</att> のみ与えられている場合、その選択する要素もしくはノードセットに表現が適用される。
      <att>match</att> のみ与えられている場合、XPath 式はこの属性を含む要素の親要素のコンテクストで評価される。</p>
    <p>なお、<att>target</att> 属性の値には XPath 式を含む XPointer 表現が入りうる（<ptr target="#SATS"/> を参照）。</p></remarks>
  
  
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-03-15" xml:lang="en">provides attributes for selecting particular elements
    within a document.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">ある文書の中の特定の要素を選択するための属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2021-01-30" xml:lang="en">points at one or more sets of zero or more elements each.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">ある文書の中の特定の要素を選択するための属性を提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scoping-egXML-cd">Elizabeth went to <persName xml:id="ESSEX">Essex</persName>
          <certainty target="#ESSEX" locus="name" degree="0.6"/>
        </egXML>
      </exemplum>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2021-01-30" xml:lang="en">supplies an XPath selection pattern using the
        syntax defined in <ptr target="#XSLT3"/> which identifies a set of nodes, selected within
        the context identified by the <att>target</att> attribute if this is supplied, or within the 
        context of the parent element if it is not.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja"><ptr target="#XSLT3"/>に定義された構文を用いて、ノードの集合を指し示す任意の XPath 式を記入する。
        選択範囲は <att>target</att> 属性が与えられた場合はそのコンテクスト、
        なければ親要素のコンテクストとなる。</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[2]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-scoping-egXML-pq" source="#UND">
          <gap reason="cancelled">
            <certainty match="@reason" locus="value" cert="low"/>
          </gap>
        </egXML>
      </exemplum>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.scoping-remarks" versionDate="2021-01-30" xml:lang="en">
    <p>The semantics of this element apply to the nodeset identified by the value of the
      <att>target</att> attribute, possibly modified by the value of the
      <att>match</att> attribute. If more than one identifier is given, the implication is
      that all elements (or nodesets) are intended. The <att>match</att> attribute may also be
      used as a means of identifying groups of elements. </p>
    <p>If <att>target</att> and <att>match</att> are present, <att>target</att> selects an
      element and the XPath expression in <att>match</att> is evaluated in the context of that
      element. If neither attribute is present, the expression applies to its parent element. If
      only <att>target</att> is given, the expression refers to the selected element or nodeset.
      If only <att>match</att> is given, the XPath expression is evaluated in the context of the
      parent element of the bearing element. </p>
    <p>Note that the value of the <att>target</att> attribute may include an XPointer expression
      including an XPath expression (see <ptr target="#SATS"/>). </p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.scoping-remarks" versionDate="2023-09-27" xml:lang="ja"><p>確信度の表現は <att>target</att> 属性の値で指定されたノードセットに適用されるが、加えて <att>match</att> 属性の値によって修正されることがある。
    複数の識別子が与えられた場合、それらすべての要素（またはノードセット）を指すものと解される。
    <att>match</att> 属性は要素のグループを指定するために用いることもできる。</p>
    <p><att>target</att> と <att>match</att> 両方がある場合、<att>match</att> の XPath 式は <att>target</att> で選択した要素のコンテクスト内で評価される。どちらの属性もない場合、表現は親要素に適用される。
      <att>target</att> のみ与えられている場合、その選択する要素もしくはノードセットに表現が適用される。
      <att>match</att> のみ与えられている場合、XPath 式はこの属性を含む要素の親要素のコンテクストで評価される。</p>
    <p>なお、<att>target</att> 属性の値には XPath 式を含む XPointer 表現が入りうる（<ptr target="#SATS"/> を参照）。</p></remarks>
```

^b12

