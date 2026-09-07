---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.namespaceable-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.namespaceable
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.namespaceable.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.namespaceable

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3183. Git blob: `f8ade9031bbacd9213aef4148b2629ddb6333135`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" type="atts" ident="att.namespaceable">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes indicating the target namespace for an object being created.</desc>
  <desc versionDate="2022-08-26" xml:lang="ja">作成されているオブジェクトが対象とする名前空間を示す属性を提供する。</desc>
  <attList>
    <attDef ident="ns" usage="opt">
      <gloss versionDate="2012-10-21" xml:lang="en">namespace</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">이름 공간</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW">名稱空間</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">espace de noms</gloss>
      <gloss versionDate="2007-05-04" xml:lang="es">espacio de nombre</gloss>
      <gloss versionDate="2007-01-21" xml:lang="it">spazio del nome</gloss>
      <gloss versionDate="2022-08-26" xml:lang="ja">名前空間</gloss>
      <desc versionDate="2023-02-07" xml:lang="en">specifies the namespace to which the element(s) being specified belongs.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 요소가 소속된 이름 공간을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明該元素所屬的名稱空間。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素が属する名前空間を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise l'espace de noms auquel appartient cet élément.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el espacio de nombre al que pertenece tal elemento.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica lo spazio del nome al quale appartiene tale elemento.</desc>
      <datatype minOccurs="0" maxOccurs="1"><dataRef key="teidata.namespace"/></datatype>
      <defaultVal>http://www.tei-c.org/ns/1.0</defaultVal>
      <remarks ident="att.namespaceable-attr.ns-remarks" versionDate="2023-02-07" xml:lang="en">
        <p>When specified on an <gi>elementSpec</gi>, this attribute
        specifies the namespace of the element being added, deleted,
        replaced, or changed. When specified on a <gi>schemaSpec</gi>,
        this attribute specifies the namespace of every element that
        is added, deleted, replaced, or changed by
        <gi>elementSpec</gi> children of the <gi>schemaSpec</gi>, or
        by <gi>elementSpec</gi>s referred to by <gi>specGrpRef</gi>
        children of the <gi>schemaSpec</gi>, <emph>unless</emph>
        overridden by an <att>ns</att> attribute on the
        <gi>elementSpec</gi>.</p>
        <p>Note that the value of <att>ns</att> of <gi>attDef</gi> is
        <emph>not</emph> inherited from its ancestors.</p>
      </remarks>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes indicating the target namespace for an object being created.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2022-08-26" xml:lang="ja">作成されているオブジェクトが対象とする名前空間を示す属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2012-10-21" xml:lang="en">namespace</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">이름 공간</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">名稱空間</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">espace de noms</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">espacio de nombre</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">spazio del nome</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[7]`.

```xml
<gloss versionDate="2022-08-26" xml:lang="ja">名前空間</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2023-02-07" xml:lang="en">specifies the namespace to which the element(s) being specified belongs.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 요소가 소속된 이름 공간을 명시한다.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明該元素所屬的名稱空間。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素が属する名前空間を示す。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise l'espace de noms auquel appartient cet élément.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el espacio de nombre al que pertenece tal elemento.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica lo spazio del nome al quale appartiene tale elemento.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="1"><dataRef key="teidata.namespace"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>http://www.tei-c.org/ns/1.0</defaultVal>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.namespaceable-attr.ns-remarks" versionDate="2023-02-07" xml:lang="en">
        <p>When specified on an <gi>elementSpec</gi>, this attribute
        specifies the namespace of the element being added, deleted,
        replaced, or changed. When specified on a <gi>schemaSpec</gi>,
        this attribute specifies the namespace of every element that
        is added, deleted, replaced, or changed by
        <gi>elementSpec</gi> children of the <gi>schemaSpec</gi>, or
        by <gi>elementSpec</gi>s referred to by <gi>specGrpRef</gi>
        children of the <gi>schemaSpec</gi>, <emph>unless</emph>
        overridden by an <att>ns</att> attribute on the
        <gi>elementSpec</gi>.</p>
        <p>Note that the value of <att>ns</att> of <gi>attDef</gi> is
        <emph>not</emph> inherited from its ancestors.</p>
      </remarks>
```

^b19

