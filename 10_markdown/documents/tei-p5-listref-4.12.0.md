---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4556. Git blob: `d247318aa1e32542e38ca282d3eaa7ef15108ab6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="LISTREF" ident="listRef">
  <gloss versionDate="2005-01-14" xml:lang="en">list of references</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">참조 목록</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">參照列表</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">liste de références</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">lista de referencias</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">lista di riferimenti</gloss>
  <desc versionDate="2022-03-11" xml:lang="en">supplies a list of significant references in the current document or elsewhere.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">현 문서 또는 그 밖의 어디든지 이 요소는 논의된 위치에 대한 중요한 참조 목록을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個重要參照的列表，這些參照連結到詳述此元素的位置，在此文件裡或是其他地方。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">場所への参照のリストを示す。当該文書中でも外部文書でもよい。</desc>
  <desc versionDate="2022-03-11" xml:lang="fr">fournit une liste de références signifiantes dans le document courant ou ailleurs.</desc>
  <desc versionDate="2022-03-11" xml:lang="es">proporciona una lista de referencias significativas a
    puntos en el documento corriente u otro lugar.</desc>
  <desc versionDate="2022-03-11" xml:lang="it">fornisce una lista di riferimenti significativi a punti
    nel documento corrente o altrove.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.ptrLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.ptrLike" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
 <constraintSpec ident="TagDocsNestinglistRef" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="( tei:classSpec | tei:dataSpec | tei:elementSpec | tei:macroSpec | tei:moduleSpec | tei:schemaSpec | tei:specGrp )/tei:listRef">
        <sch:report test="tei:listRef">In the context of tagset documentation, the &lt;listRef> element must not self-nest.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="TagDocslistRefChildren" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="( tei:classSpec | tei:dataSpec | tei:elementSpec | tei:macroSpec | tei:moduleSpec | tei:schemaSpec | tei:specGrp )/tei:listRef/tei:ptr | ( tei:classSpec | tei:dataSpec | tei:elementSpec | tei:macroSpec | tei:moduleSpec | tei:schemaSpec | tei:specGrp )/tei:listRef/tei:ref">
        <sch:assert test="@target and not( matches( @target,'\s') )">In the context of tagset documentation, each &lt;ptr> or &lt;ref> element inside a &lt;listRef> must have a @target attribute with only 1 pointer as its value.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LISTREF-egXML-bd" source="#UND">
      <listRef>
        <ptr target="#ddc12"/>
      </listRef>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LISTREF-egXML-xj" source="#UND">
      <listRef>
        <ptr target="#fr_ddc12"/>
      </listRef>
    </egXML>
  </exemplum>
  <remarks ident="listRef-remarks" versionDate="2022-03-11" xml:lang="en">
    <p>When <gi>listRef</gi> is used in the context of <ident type="module">tagdocs</ident>, further restrictons apply:
    <list>
      <item>It may only contain <gi>ptr</gi> or <gi>ref</gi>
        elements.</item>
      <item>Each <gi>ptr</gi> or <gi>ref</gi> child should bear a
        <att>target</att> attribute, the value of which should be a
        single URI pointer.</item>
    </list>
    </p>
  </remarks>
  <listRef>
    <ptr target="#TDcrystalsCEdc"/>
    <ptr target="#IM-unified"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">list of references</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">참조 목록</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">參照列表</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">liste de références</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">lista de referencias</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">lista di riferimenti</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2022-03-11" xml:lang="en">supplies a list of significant references in the current document or elsewhere.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 문서 또는 그 밖의 어디든지 이 요소는 논의된 위치에 대한 중요한 참조 목록을 제공한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個重要參照的列表，這些參照連結到詳述此元素的位置，在此文件裡或是其他地方。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">場所への参照のリストを示す。当該文書中でも外部文書でもよい。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2022-03-11" xml:lang="fr">fournit une liste de références signifiantes dans le document courant ou ailleurs.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-03-11" xml:lang="es">proporciona una lista de referencias significativas a
    puntos en el documento corriente u otro lugar.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2022-03-11" xml:lang="it">fornisce una lista di riferimenti significativi a punti
    nel documento corrente o altrove.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.ptrLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.ptrLike" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="TagDocsNestinglistRef" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="( tei:classSpec | tei:dataSpec | tei:elementSpec | tei:macroSpec | tei:moduleSpec | tei:schemaSpec | tei:specGrp )/tei:listRef">
        <sch:report test="tei:listRef">In the context of tagset documentation, the &lt;listRef> element must not self-nest.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="TagDocslistRefChildren" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="( tei:classSpec | tei:dataSpec | tei:elementSpec | tei:macroSpec | tei:moduleSpec | tei:schemaSpec | tei:specGrp )/tei:listRef/tei:ptr | ( tei:classSpec | tei:dataSpec | tei:elementSpec | tei:macroSpec | tei:moduleSpec | tei:schemaSpec | tei:specGrp )/tei:listRef/tei:ref">
        <sch:assert test="@target and not( matches( @target,'\s') )">In the context of tagset documentation, each &lt;ptr> or &lt;ref> element inside a &lt;listRef> must have a @target attribute with only 1 pointer as its value.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LISTREF-egXML-bd" source="#UND">
      <listRef>
        <ptr target="#ddc12"/>
      </listRef>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LISTREF-egXML-xj" source="#UND">
      <listRef>
        <ptr target="#fr_ddc12"/>
      </listRef>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listRef-remarks" versionDate="2022-03-11" xml:lang="en">
    <p>When <gi>listRef</gi> is used in the context of <ident type="module">tagdocs</ident>, further restrictons apply:
    <list>
      <item>It may only contain <gi>ptr</gi> or <gi>ref</gi>
        elements.</item>
      <item>Each <gi>ptr</gi> or <gi>ref</gi> child should bear a
        <att>target</att> attribute, the value of which should be a
        single URI pointer.</item>
    </list>
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDcrystalsCEdc"/>
    <ptr target="#IM-unified"/>
  </listRef>
```

^b21

