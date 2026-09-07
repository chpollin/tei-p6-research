---
type: representation
source-type: document
source: '[[00_sources/tei-p5-m-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 m
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/m.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# m

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4463. Git blob: `2ea15178967dd152d50ee07d975ca27c9c2062a4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="gi-m" ident="m">
  <gloss versionDate="2005-01-14" xml:lang="en">morpheme</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">형태소</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">語素</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">morphème</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">morfema</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">morfema</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a grammatical morpheme.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문법적인 형태소를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示文法上的語素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">言語学上の形態素を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente un morphème grammatical.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa un morfema gramatical.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta il morfema grammaticale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.hiLike"/>
        <elementRef key="seg"/>
        <elementRef key="m"/>
        <elementRef key="c"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <attList>
    <attDef ident="baseForm" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">supplies the morpheme's base form.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">형태소의 기본형을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該語素的基本形式。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">形態素の基形を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">identifie la forme de base du morphème.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica la forma base del morfema</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica la forma base del morfema.</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-m-egXML-iy">
      <w type="adjective">
        <w type="noun">
          <m type="prefix" baseForm="con">com</m>
          <m type="root">fort</m>
        </w>
        <m type="suffix">able</m>
      </w>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-m-egXML-mi">
      <w type="adjective">
        <w type="noun">
          <m type="prefix" baseForm="con">con</m>
          <m type="root">fort</m>
        </w>
        <m type="suffix">able</m>
      </w>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-m-egXML-lg">
      <w type="形容詞">
        <w type="名詞">
          <m type="字首" baseForm="con">com</m>
          <m type="字根">fort</m>
        </w>
        <m type="字尾">able</m>
      </w>
    </egXML>
  </exemplum>
  <remarks ident="m-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <att>type</att> attribute may be used to indicate the type of morpheme, taking values
      such as <val>clitic</val>, <val>prefix</val>, <val>stem</val>, etc. as appropriate.</p>
  </remarks>
  <remarks ident="m-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'attribut <att>type</att> peut être utilisé pour préciser le type de morphème, avec des
      valeurs telles que <val>clitique</val>, <val>préfixe</val>, <val>stemma</val>, etc. selon le cas.</p>
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
<gloss versionDate="2005-01-14" xml:lang="en">morpheme</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">형태소</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">語素</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">morphème</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">morfema</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">morfema</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a grammatical morpheme.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문법적인 형태소를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示文法上的語素。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">言語学上の形態素を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente un morphème grammatical.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa un morfema gramatical.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta il morfema grammaticale.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.hiLike"/>
        <elementRef key="seg"/>
        <elementRef key="m"/>
        <elementRef key="c"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies the morpheme's base form.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">형태소의 기본형을 명시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該語素的基本形式。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">形態素の基形を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">identifie la forme de base du morphème.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica la forma base del morfema</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica la forma base del morfema.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-m-egXML-iy">
      <w type="adjective">
        <w type="noun">
          <m type="prefix" baseForm="con">com</m>
          <m type="root">fort</m>
        </w>
        <m type="suffix">able</m>
      </w>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-m-egXML-mi">
      <w type="adjective">
        <w type="noun">
          <m type="prefix" baseForm="con">con</m>
          <m type="root">fort</m>
        </w>
        <m type="suffix">able</m>
      </w>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-m-egXML-lg">
      <w type="形容詞">
        <w type="名詞">
          <m type="字首" baseForm="con">com</m>
          <m type="字根">fort</m>
        </w>
        <m type="字尾">able</m>
      </w>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="m-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <att>type</att> attribute may be used to indicate the type of morpheme, taking values
      such as <val>clitic</val>, <val>prefix</val>, <val>stem</val>, etc. as appropriate.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="m-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'attribut <att>type</att> peut être utilisé pour préciser le type de morphème, avec des
      valeurs telles que <val>clitique</val>, <val>préfixe</val>, <val>stemma</val>, etc. selon le cas.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AILC"/>
  </listRef>
```

^b29

