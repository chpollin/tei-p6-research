---
type: representation
source-type: document
source: '[[00_sources/tei-p5-material-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 material
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/material.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# material

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5231. Git blob: `0658d5abae226912a1a0ac9040ab7cc20093b391`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="MATERIAL" ident="material">
  <gloss versionDate="2009-04-17" xml:lang="en">material</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">matériau</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="material.desc">contains a word or phrase describing the material of which the object being described is composed.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고(또는 원고의 일부)를 구성하는 자료를 기술하는 단어 또는 구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">用一個字詞描述手稿 (或手稿部分) 的組成材料。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料を構成する素材を表す語句を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un mot ou une expression décrivant le ou les matériau(x)
  utilisé(s) pour fabriquer un manuscrit (ou une partie d'un manuscrit).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o sintagma que describe el material del que se compone un manuscrito (o parte del manuscrito).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una parola o un'espressione che descrive il materiale di cui è composto un manoscritto (o una sua parte).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="function">
      <desc versionDate="2020-11-12" xml:lang="en">describes the
      function or use of the material in relation to the object
      as a whole.</desc>
      <datatype minOccurs="1" maxOccurs="1">
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
        <valItem ident="binding">
          <desc versionDate="2020-11-12" xml:lang="en">covering
          material of a codex</desc>
        </valItem>
        <valItem ident="endband">
          <desc versionDate="2020-11-12" xml:lang="en">sewing at the
          head or tail of the codex spine to strengthen the binding,
          often decorative</desc>
        </valItem>
        <valItem ident="slipcase">
          <desc versionDate="2020-11-12" xml:lang="en">removable
          protective cover for a set of one or more codices</desc>
        </valItem>
        <valItem ident="support">
          <desc versionDate="2020-11-12" xml:lang="en">the surface for writing</desc>
        </valItem>
        <valItem ident="tie">
          <desc versionDate="2020-11-12" xml:lang="en">a ribbon or
          string used to bind or close a codex or rolled scroll</desc>
        </valItem>
      </valList>
      <remarks ident="material-attr.function-remarks" versionDate="2020-11-12" xml:lang="en">
        <p>The sample values here are for descriptive bibliography.
        Other sets of sample values might include <val>armrests</val>,
        <val>legs</val>, <val>tabletop</val>, <val>pan</val>, and
        <val>back</val> for furniture; or <val>wall</val>,
        <val>floor</val>, <val>window</val>, <val>column</val>,
        <val>ceiling</val>, <val>roof</val>, <val>stairs</val>,
        <val>chimney</val> for architecture.</p>
      </remarks>
    </attDef>
    <attDef ident="target">
      <desc versionDate="2013-04-16" xml:lang="en">identifies one or more elements to which the metamark applies.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MATERIAL-egXML-it">
      <physDesc>
        <p><material>Parchment</material> leaves with a
        <material>sharkskin</material> binding.</p>
      </physDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MATERIAL-egXML-my" source="#fr-ex-BnF-Reliures">
      <p><index indexName="typo_decor"><term>Entrelacs géométriques</term></index> Reliure en <material>maroquin</material> brun jaspé</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MATERIAL-egXML-et">
      <physDesc>
        <p><material>羊皮</material> 頁面用
        <material>鯊魚皮</material>
        捆綁</p>
      </physDesc>
    </egXML>
  </exemplum>
  <remarks ident="material-remarks" versionDate="2010-05-06" xml:lang="en">
    <p>The <att>ref</att> attribute may be used to point to one
    or more items within a
    taxonomy of types of material, defined either internally or
    externally.</p>
  </remarks>
  <listRef>
    <ptr target="#msmat"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="en">material</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">matériau</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="material.desc">contains a word or phrase describing the material of which the object being described is composed.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고(또는 원고의 일부)를 구성하는 자료를 기술하는 단어 또는 구를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用一個字詞描述手稿 (或手稿部分) 的組成材料。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料を構成する素材を表す語句を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un mot ou une expression décrivant le ou les matériau(x)
  utilisé(s) pour fabriquer un manuscrit (ou une partie d'un manuscrit).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o sintagma que describe el material del que se compone un manuscrito (o parte del manuscrito).</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una parola o un'espressione che descrive il materiale di cui è composto un manoscritto (o una sua parte).</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2020-11-12" xml:lang="en">describes the
      function or use of the material in relation to the object
      as a whole.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="1">
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="binding">
          <desc versionDate="2020-11-12" xml:lang="en">covering
          material of a codex</desc>
        </valItem>
        <valItem ident="endband">
          <desc versionDate="2020-11-12" xml:lang="en">sewing at the
          head or tail of the codex spine to strengthen the binding,
          often decorative</desc>
        </valItem>
        <valItem ident="slipcase">
          <desc versionDate="2020-11-12" xml:lang="en">removable
          protective cover for a set of one or more codices</desc>
        </valItem>
        <valItem ident="support">
          <desc versionDate="2020-11-12" xml:lang="en">the surface for writing</desc>
        </valItem>
        <valItem ident="tie">
          <desc versionDate="2020-11-12" xml:lang="en">a ribbon or
          string used to bind or close a codex or rolled scroll</desc>
        </valItem>
      </valList>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="material-attr.function-remarks" versionDate="2020-11-12" xml:lang="en">
        <p>The sample values here are for descriptive bibliography.
        Other sets of sample values might include <val>armrests</val>,
        <val>legs</val>, <val>tabletop</val>, <val>pan</val>, and
        <val>back</val> for furniture; or <val>wall</val>,
        <val>floor</val>, <val>window</val>, <val>column</val>,
        <val>ceiling</val>, <val>roof</val>, <val>stairs</val>,
        <val>chimney</val> for architecture.</p>
      </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en">identifies one or more elements to which the metamark applies.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MATERIAL-egXML-it">
      <physDesc>
        <p><material>Parchment</material> leaves with a
        <material>sharkskin</material> binding.</p>
      </physDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MATERIAL-egXML-my" source="#fr-ex-BnF-Reliures">
      <p><index indexName="typo_decor"><term>Entrelacs géométriques</term></index> Reliure en <material>maroquin</material> brun jaspé</p>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MATERIAL-egXML-et">
      <physDesc>
        <p><material>羊皮</material> 頁面用
        <material>鯊魚皮</material>
        捆綁</p>
      </physDesc>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="material-remarks" versionDate="2010-05-06" xml:lang="en">
    <p>The <att>ref</att> attribute may be used to point to one
    or more items within a
    taxonomy of types of material, defined either internally or
    externally.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msmat"/>
  </listRef>
```

^b22

