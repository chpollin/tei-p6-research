---
type: representation
source-type: document
source: '[[00_sources/tei-p5-interp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 interp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/interp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# interp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3645. Git blob: `b6c0d575aca1472732f12deef7a70ad83164b5ff`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="gi-interp" ident="interp">
  <gloss versionDate="2005-01-14" xml:lang="en">interpretation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">해석</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">解釋</gloss>
  <gloss versionDate="2008-04-06" xml:lang="ja"/>
  <gloss versionDate="2007-06-12" xml:lang="fr">interprétation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">interpretación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">interpretazione</gloss>
  <desc versionDate="2005-07-30" xml:lang="en">summarizes a specific
  interpretative annotation which can be linked to a span of
  text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 범위에 연결될 수 있는 명시적인 해석적 부호를 요약한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明和某一文字段相連結的特定解釋性註釋。</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">あるテキスト部分とリンクする、特定の解釈的注釈をまとめる。</desc>
  <desc versionDate="2009-02-13" xml:lang="fr">interprétation sous la
  forme d'une annotation concise, pouvant être liée à un passage dans
  un texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">resume una anotación
  interpretativa específica que puede ser conectada con un periodo de
  texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">riassume una specifica
  annotazione interpretativa che può essere associata ad una porzione
  di testo</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.interpLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interp-egXML-el">
      <interp type="structuralunit" xml:id="ana_am">aftermath</interp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interp-egXML-eu">
      <interp type="structuralunit">conséquence</interp>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interp-egXML-lw">
      <interp type="段落架構">結局</interp>
    </egXML>
  </exemplum>
  <remarks ident="interp-remarks" versionDate="2010-01-24" xml:lang="en">
    <p>Generally, each <gi>interp</gi> element carries an
    <att>xml:id</att> attribute. This permits the encoder to
    explicitly associate the interpretation represented by the content
    of an <gi>interp</gi> with any textual element through its
    <att>ana</att> attribute.</p>
    <p>Alternatively (or, in addition) an <gi>interp</gi> may carry an
    <att>inst</att> attribute that points to one or more textual
    elements to which the analysis represented by the content of the
    <gi>interp</gi> applies.</p>
  </remarks>
  <listRef>
    <ptr target="#AISP" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">interpretation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">해석</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">解釋</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="ja"/>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">interprétation</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">interpretación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">interpretazione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-07-30" xml:lang="en">summarizes a specific
  interpretative annotation which can be linked to a span of
  text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 범위에 연결될 수 있는 명시적인 해석적 부호를 요약한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明和某一文字段相連結的特定解釋性註釋。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">あるテキスト部分とリンクする、特定の解釈的注釈をまとめる。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-02-13" xml:lang="fr">interprétation sous la
  forme d'une annotation concise, pouvant être liée à un passage dans
  un texte.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">resume una anotación
  interpretativa específica que puede ser conectada con un periodo de
  texto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">riassume una specifica
  annotazione interpretativa che può essere associata ad una porzione
  di testo</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.interpLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interp-egXML-el">
      <interp type="structuralunit" xml:id="ana_am">aftermath</interp>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interp-egXML-eu">
      <interp type="structuralunit">conséquence</interp>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interp-egXML-lw">
      <interp type="段落架構">結局</interp>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="interp-remarks" versionDate="2010-01-24" xml:lang="en">
    <p>Generally, each <gi>interp</gi> element carries an
    <att>xml:id</att> attribute. This permits the encoder to
    explicitly associate the interpretation represented by the content
    of an <gi>interp</gi> with any textual element through its
    <att>ana</att> attribute.</p>
    <p>Alternatively (or, in addition) an <gi>interp</gi> may carry an
    <att>inst</att> attribute that points to one or more textual
    elements to which the analysis represented by the content of the
    <gi>interp</gi> applies.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AISP" type="div2"/>
  </listRef>
```

^b21

