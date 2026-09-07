---
type: representation
source-type: document
source: '[[00_sources/tei-p5-biblscope-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 biblScope
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/biblScope.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# biblScope

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6186. Git blob: `c6b0134bfe1c874b02c9a6bc32a7bb141195dc5f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-biblScope" ident="biblScope">
  <gloss versionDate="2012-12-13" xml:lang="en">scope of bibliographic reference</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">인용 범위</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">書目引用範圍</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">extension d'une référence bibliographique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">extensión de una cita</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">estensione del riferimento bibliografico</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Geltungsbereich einer bibliografischen Referenz</gloss>
  <gloss versionDate="2023-09-21" xml:lang="ja">典拠参照の範囲</gloss>
  <desc versionDate="2008-01-21" xml:lang="en">defines the scope of a bibliographic reference, for
    example as a list of page numbers, or a named subdivision of a larger work.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 페이지수의 목록 또는 작품의 이름 붙은 하위 성분으로, 문헌 참조의 범위를
    정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明書目參照資訊的範圍，例如標示頁碼列表、或是某著作的分支作品名稱。</desc>
  <desc versionDate="2023-09-21" xml:lang="ja">典拠参照の範囲を示す。例えば、ページ番号や、全体の中で名前を与えられた下位要素など。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">définit l'extension d'une référence bibliographique,
    comme par exemple une liste de numéros de page, ou le nom d'une subdivision d'une oeuvre plus
    grande.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la extensión de una referencia bibliográfica,
    como por ejemplo los números de página u otra subdivisión numerada en la obra mayor.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce l'estensione di un riferimento
    bibliografico, per esempio mediante una lista di numeri di pagina, o il titolo di una parte di
    un'opera più ampia.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">grenzt den Geltungsbereich einer bibliografischen Referenz ein, zum Beispiel in Form von
    Seitenangaben oder benannten Unterabschnitten eines umfangreicheren Werks.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citing"/>
    <memberOf key="model.imprintPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <!--  MDH 2014-12-18: attList and its one attDef for @type now removed after two years of deprecation. -->
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblScope-egXML-dp">
      <biblScope>pp 12–34</biblScope>
      <biblScope unit="page" from="12" to="34"/>
      <biblScope unit="volume">II</biblScope>
      <biblScope unit="page">12</biblScope>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblScope-egXML-xi">
      <biblScope>pp 12–34</biblScope>
      <biblScope unit="page" from="12" to="34"/>
      <biblScope unit="volume">II</biblScope>
      <biblScope unit="page">12</biblScope>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblScope-egXML-je">
      <biblScope>頁數 12–34</biblScope>
      <biblScope unit="頁數" from="12" to="34"/>
      <biblScope unit="冊">II</biblScope>
      <biblScope unit="頁數">12</biblScope>
    </egXML>
  </exemplum>
  <remarks ident="biblScope-remarks" versionDate="2017-03-29" xml:lang="en">
    <p>When a single page is being cited, use the <att>from</att> and <att>to</att> attributes with
      an identical value. When no clear endpoint is provided, the <att>from</att> attribute may be
      used without <att>to</att>; for example a citation such as <q>p. 3ff</q> might be encoded
        <code>&lt;biblScope from="3"&gt;p. 3ff&lt;/biblScope&gt;</code>.</p>
    <p>It is now considered good practice to supply this element as a sibling (rather than a child)
      of <gi>imprint</gi>, since it supplies information which does not constitute part of the
      imprint. </p>
  </remarks>
  <remarks ident="biblScope-remarks" versionDate="2017-06-13" xml:lang="de">
    <p>Wird nur eine einzelne Seite zitiert, erhalten die Attribute <att>from</att> und <att>to</att>
      identische Werte. Gibt es keinen klaren Endpunkt, sollte nur das <att>from</att>-Attribut ohne
      korrespondierendes <att>to</att>-Attribut verwendet werden, zum Beispiel könnte ein Zitat wie
      <q>S. 3ff.</q> als <code>&lt;biblScope from="3"&gt;p. 3ff&lt;/biblScope&gt;</code> kodiert werden.</p>
    <p>Es wird nun als gute Praxis angesehen, dieses Element als Geschwisterelement (anstatt eines
      Kindelements) von <gi>imprint</gi> anzugeben, da es Informationen enthält, die nicht Teil des
      Impressums sind.</p>
  </remarks>
<remarks ident="biblScope-remarks" versionDate="2023-09-21" xml:lang="ja">
    <p>一つのページが引用される場合、<att>from</att>属性と<att>to</att>属性を同じ値で使用すべきである。
        明確な終点が提供されていない場合、<att>from</att>属性は<att>to</att>を使わずに使うことができる。
        例えば、<q>p. 3ff</q>のような引用は、<code>&lt;biblScope from="3"&gt;p. 3ff&lt;/biblScope&gt;</code>となる。</p>
        <p>出版事項の一部を構成しない情報を提供するため、この要素を<gi>imprint</gi>の子ではなく、兄弟として提供するほうが望ましい。</p>
  </remarks>
  <listRef>
    <ptr target="#COBICOB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2012-12-13" xml:lang="en">scope of bibliographic reference</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">인용 범위</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">書目引用範圍</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">extension d'une référence bibliographique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">extensión de una cita</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">estensione del riferimento bibliografico</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Geltungsbereich einer bibliografischen Referenz</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-09-21" xml:lang="ja">典拠参照の範囲</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-01-21" xml:lang="en">defines the scope of a bibliographic reference, for
    example as a list of page numbers, or a named subdivision of a larger work.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어 페이지수의 목록 또는 작품의 이름 붙은 하위 성분으로, 문헌 참조의 범위를
    정의한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明書目參照資訊的範圍，例如標示頁碼列表、或是某著作的分支作品名稱。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-09-21" xml:lang="ja">典拠参照の範囲を示す。例えば、ページ番号や、全体の中で名前を与えられた下位要素など。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">définit l'extension d'une référence bibliographique,
    comme par exemple une liste de numéros de page, ou le nom d'une subdivision d'une oeuvre plus
    grande.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la extensión de una referencia bibliográfica,
    como por ejemplo los números de página u otra subdivisión numerada en la obra mayor.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce l'estensione di un riferimento
    bibliografico, per esempio mediante una lista di numeri di pagina, o il titolo di una parte di
    un'opera più ampia.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">grenzt den Geltungsbereich einer bibliografischen Referenz ein, zum Beispiel in Form von
    Seitenangaben oder benannten Unterabschnitten eines umfangreicheren Werks.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citing"/>
    <memberOf key="model.imprintPart"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblScope-egXML-dp">
      <biblScope>pp 12–34</biblScope>
      <biblScope unit="page" from="12" to="34"/>
      <biblScope unit="volume">II</biblScope>
      <biblScope unit="page">12</biblScope>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblScope-egXML-xi">
      <biblScope>pp 12–34</biblScope>
      <biblScope unit="page" from="12" to="34"/>
      <biblScope unit="volume">II</biblScope>
      <biblScope unit="page">12</biblScope>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblScope-egXML-je">
      <biblScope>頁數 12–34</biblScope>
      <biblScope unit="頁數" from="12" to="34"/>
      <biblScope unit="冊">II</biblScope>
      <biblScope unit="頁數">12</biblScope>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="biblScope-remarks" versionDate="2017-03-29" xml:lang="en">
    <p>When a single page is being cited, use the <att>from</att> and <att>to</att> attributes with
      an identical value. When no clear endpoint is provided, the <att>from</att> attribute may be
      used without <att>to</att>; for example a citation such as <q>p. 3ff</q> might be encoded
        <code>&lt;biblScope from="3"&gt;p. 3ff&lt;/biblScope&gt;</code>.</p>
    <p>It is now considered good practice to supply this element as a sibling (rather than a child)
      of <gi>imprint</gi>, since it supplies information which does not constitute part of the
      imprint. </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="biblScope-remarks" versionDate="2017-06-13" xml:lang="de">
    <p>Wird nur eine einzelne Seite zitiert, erhalten die Attribute <att>from</att> und <att>to</att>
      identische Werte. Gibt es keinen klaren Endpunkt, sollte nur das <att>from</att>-Attribut ohne
      korrespondierendes <att>to</att>-Attribut verwendet werden, zum Beispiel könnte ein Zitat wie
      <q>S. 3ff.</q> als <code>&lt;biblScope from="3"&gt;p. 3ff&lt;/biblScope&gt;</code> kodiert werden.</p>
    <p>Es wird nun als gute Praxis angesehen, dieses Element als Geschwisterelement (anstatt eines
      Kindelements) von <gi>imprint</gi> anzugeben, da es Informationen enthält, die nicht Teil des
      Impressums sind.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="biblScope-remarks" versionDate="2023-09-21" xml:lang="ja">
    <p>一つのページが引用される場合、<att>from</att>属性と<att>to</att>属性を同じ値で使用すべきである。
        明確な終点が提供されていない場合、<att>from</att>属性は<att>to</att>を使わずに使うことができる。
        例えば、<q>p. 3ff</q>のような引用は、<code>&lt;biblScope from="3"&gt;p. 3ff&lt;/biblScope&gt;</code>となる。</p>
        <p>出版事項の一部を構成しない情報を提供するため、この要素を<gi>imprint</gi>の子ではなく、兄弟として提供するほうが望ましい。</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOB"/>
  </listRef>
```

^b25

