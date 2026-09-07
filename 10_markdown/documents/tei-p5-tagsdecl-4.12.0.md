---
type: representation
source-type: document
source: '[[00_sources/tei-p5-tagsdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 tagsDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/tagsDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# tagsDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4236. Git blob: `39acf1d9dab08836739c8526b05a17ebd107f456`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-tagsDecl" ident="tagsDecl">
  <gloss versionDate="2005-01-14" xml:lang="en">tagging declaration</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">déclaration de balisage</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">태깅 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">標誌宣告</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Beschreibung des Tag-Gebrauchs</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración del etiquetado</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dighiarazione sulla marcatura</gloss>
  <desc versionDate="2007-04-27" xml:lang="en">provides detailed information about the tagging applied to a document.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">donne l’information détaillée sur le balisage appliqué à un document .</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문서에 적용된 태깅에 관한 정보를 상세하게 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供關於應用在XML文件中的標誌的詳細資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">タグ付けに関する詳細な情報を示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">liefert detaillierte
  Angaben zum Gebrauch von Tags, die in einem Dokument verwendet werden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona información pormenorizada sobre el etiquetado aplicado a un documento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni dettagliate sulla mercatura applicata ad un documento SGML o XML.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <sequence>      
      <elementRef key="rendition" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="namespace" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <attList>
    <attDef ident="partial" usage="rec">
      <desc versionDate="2015-01-29" xml:lang="en">indicates whether
      the element types listed exhaustively include all those found
      within <gi>text</gi>, or represent only a subset.</desc>
      <datatype minOccurs="1" maxOccurs="1"><dataRef key="teidata.truthValue"/></datatype>
      <remarks ident="tagsDecl-attr.partial-remarks" versionDate="2015-01-29" xml:lang="en">
	<p>TEI recommended practice is to specify this attribute. When
	the <gi>tagUsage</gi> elements inside <gi>tagsDecl</gi> are
	used to list each of the element types in the associated
	<gi>text</gi>, the value should be given as <val>false</val>.
	When the <gi>tagUsage</gi> elements inside <gi>tagsDecl</gi>
	are used to provide usage information or default renditions
	for only a subset of the elements types within the associated
	<gi>text</gi>, the value should be <val>true</val>.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum versionDate="2016-12-05" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tagsDecl-egXML-eu">
      <tagsDecl partial="true">
        <rendition xml:id="rend-it" scheme="css" selector="emph, hi, name, title">font-style: italic;</rendition>
        <namespace name="http://www.tei-c.org/ns/1.0">
          <tagUsage gi="hi" occurs="467"/>
          <tagUsage gi="title" occurs="45"/>
        </namespace>
        <namespace name="http://docbook.org/ns/docbook">
          <tagUsage gi="para" occurs="10"/>
        </namespace>
      </tagsDecl>
    </egXML>
    <p>If the <att>partial</att> attribute were not specified here, the implication would be that
    the document in question contains only <gi>hi</gi>, <gi>title</gi>, and <gi>para</gi> elements.</p>
  </exemplum>
  <listRef>
    <ptr target="#HD57"/>
    <ptr target="#HD5"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">tagging declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">déclaration de balisage</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">태깅 선언</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">標誌宣告</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Beschreibung des Tag-Gebrauchs</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración del etiquetado</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dighiarazione sulla marcatura</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-27" xml:lang="en">provides detailed information about the tagging applied to a document.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">donne l’information détaillée sur le balisage appliqué à un document .</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문서에 적용된 태깅에 관한 정보를 상세하게 제공한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供關於應用在XML文件中的標誌的詳細資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">タグ付けに関する詳細な情報を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">liefert detaillierte
  Angaben zum Gebrauch von Tags, die in einem Dokument verwendet werden.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona información pormenorizada sobre el etiquetado aplicado a un documento.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni dettagliate sulla mercatura applicata ad un documento SGML o XML.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>      
      <elementRef key="rendition" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="namespace" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2015-01-29" xml:lang="en">indicates whether
      the element types listed exhaustively include all those found
      within <gi>text</gi>, or represent only a subset.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="1"><dataRef key="teidata.truthValue"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="tagsDecl-attr.partial-remarks" versionDate="2015-01-29" xml:lang="en">
	<p>TEI recommended practice is to specify this attribute. When
	the <gi>tagUsage</gi> elements inside <gi>tagsDecl</gi> are
	used to list each of the element types in the associated
	<gi>text</gi>, the value should be given as <val>false</val>.
	When the <gi>tagUsage</gi> elements inside <gi>tagsDecl</gi>
	are used to provide usage information or default renditions
	for only a subset of the elements types within the associated
	<gi>text</gi>, the value should be <val>true</val>.</p>
      </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2016-12-05" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tagsDecl-egXML-eu">
      <tagsDecl partial="true">
        <rendition xml:id="rend-it" scheme="css" selector="emph, hi, name, title">font-style: italic;</rendition>
        <namespace name="http://www.tei-c.org/ns/1.0">
          <tagUsage gi="hi" occurs="467"/>
          <tagUsage gi="title" occurs="45"/>
        </namespace>
        <namespace name="http://docbook.org/ns/docbook">
          <tagUsage gi="para" occurs="10"/>
        </namespace>
      </tagsDecl>
    </egXML>
    <p>If the <att>partial</att> attribute were not specified here, the implication would be that
    the document in question contains only <gi>hi</gi>, <gi>title</gi>, and <gi>para</gi> elements.</p>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD57"/>
    <ptr target="#HD5"/>
  </listRef>
```

^b22

