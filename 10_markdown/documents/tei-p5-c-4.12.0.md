---
type: representation
source-type: document
source: '[[00_sources/tei-p5-c-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 c
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/c.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# c

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3749. Git blob: `1c606def41e8bb1f695d1c2726e7d53995e9b524`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="gi-c" ident="c">
  <gloss versionDate="2005-01-14" xml:lang="en">character</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문자(글자)</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文字符號</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">caractère</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">carácter</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">carattere</gloss>
  <gloss versionDate="2023-09-27" xml:lang="ja">文字</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a character.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문자(글자)를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個文字符號。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">文字を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente un caractère.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa un carácter gráfico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta il carattere.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
  </classes>
  <content>
    <macroRef key="macro.xtext"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-c-egXML-bv" source="#TwN">
      <phr>
        <c>M</c>
        <c>O</c>
        <c>A</c>
        <c>I</c>
        <w>doth</w>
        <w>sway</w>
        <w>my</w>
        <w>life</w>
      </phr>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-c-egXML-bt">
      <c type="punctuation">?</c>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-c-egXML-sd">
      <c type="標點符號">?</c>
    </egXML>
  </exemplum>
  <remarks ident="c-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>Contains a single character, a <gi>g</gi> element, or a
    sequence of graphemes to be treated as a single character. The
    <att>type</att> attribute is used to indicate the function of this
    segmentation, taking values such as <val>letter</val>,
    <val>punctuation</val>, or <val>digit</val> etc. </p>
  </remarks>
  <remarks ident="c-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient un seul caractère, un élément <gi>g</gi> ou une suite de graphèmes à traiter comme
                un seul caractère. L'attribut <att>type</att> est utilisé pour indiquer la fonction de cette segmentation, avec des valeurs telles que <val>letter</val>,
    <val>punctuation</val>, ou <val>digit</val>, etc.</p>
  </remarks>
  <remarks ident="c-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      一つの文字、一つの<gi>g</gi>、あるいは一つの文字として扱われるべき一連の文字素を含む。<att>type</att>属性は、その役割を示す。たとえば<val>letter</val>、<val>punctuation</val>、あるいは<val>digit</val>。
    </p>
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
<gloss versionDate="2005-01-14" xml:lang="en">character</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문자(글자)</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文字符號</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">caractère</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">carácter</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">carattere</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-09-27" xml:lang="ja">文字</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a character.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문자(글자)를 표시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個文字符號。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">文字を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente un caractère.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa un carácter gráfico.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta il carattere.</desc>
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
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.xtext"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-c-egXML-bv" source="#TwN">
      <phr>
        <c>M</c>
        <c>O</c>
        <c>A</c>
        <c>I</c>
        <w>doth</w>
        <w>sway</w>
        <w>my</w>
        <w>life</w>
      </phr>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-c-egXML-bt">
      <c type="punctuation">?</c>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-c-egXML-sd">
      <c type="標點符號">?</c>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="c-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>Contains a single character, a <gi>g</gi> element, or a
    sequence of graphemes to be treated as a single character. The
    <att>type</att> attribute is used to indicate the function of this
    segmentation, taking values such as <val>letter</val>,
    <val>punctuation</val>, or <val>digit</val> etc. </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="c-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient un seul caractère, un élément <gi>g</gi> ou une suite de graphèmes à traiter comme
                un seul caractère. L'attribut <att>type</att> est utilisé pour indiquer la fonction de cette segmentation, avec des valeurs telles que <val>letter</val>,
    <val>punctuation</val>, ou <val>digit</val>, etc.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="c-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      一つの文字、一つの<gi>g</gi>、あるいは一つの文字として扱われるべき一連の文字素を含む。<att>type</att>属性は、その役割を示す。たとえば<val>letter</val>、<val>punctuation</val>、あるいは<val>digit</val>。
    </p>
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

