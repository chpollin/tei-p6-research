---
type: representation
source-type: document
source: '[[00_sources/tei-p5-etree-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 eTree
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/eTree.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# eTree

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6008. Git blob: `95361e7bd1b25521e373ffd167ed7773753f9d98`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-eTree" ident="eTree">
  <gloss versionDate="2005-01-14" xml:lang="en">embedding tree</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">내포 수형도</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">嵌入樹狀結構</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">arbre englobant</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">árbol integrado</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">albero integrato</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">provides an alternative to the <gi>tree</gi> element for representing ordered rooted tree structures.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">순서가 있고 뿌리가 있는 수형 구조를 표시하기 위해 수형도 요소에 대체안을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供樹元素的替換，用來表示整齊具有根節點的樹狀結構。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">順序付き根付き木を構成する部分木を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">élément à utiliser lorsqu'on a besoin d'imbriquer
    plusieurs structures arborescentes à racine et ordonnées, pour encoder chacune de ces structures (en effet, il n'est pas possible d'imbriquer des éléments <gi>tree</gi>).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa una alternativa al elemento árbol para la representación de estructuras del tipo árbol enraizado ordenado</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rapresenta un'alternativa all'elemento albero per la rappresentazione di strutture del tipo albero radicato ordinato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="label" minOccurs="0"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="eTree"/>
        <elementRef key="triangle"/>
        <elementRef key="eLeaf"/>
        <classRef key="model.ptrLike"/>
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">provides the value of an embedding tree, which is a feature
structure or other analytic element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">내포 수형도의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個嵌入樹狀結構值，該嵌入樹狀結構為一個功能結構或其他分析元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該部分木の値を示す。素性構造または他の分析に関する要素になる。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par l'arbre englobant ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">adscribe al árbol integrado un valor, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna all'albero integrato un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eTree-egXML-kt">
      <eTree n="ex1">
        <label>PP</label>
        <eTree>
          <label>P</label>
          <eLeaf>
            <label>with</label>
          </eLeaf>
        </eTree>
        <eTree>
          <label>NP</label>
          <eTree>
            <label>Art</label>
            <eLeaf>
              <label>the</label>
            </eLeaf>
          </eTree>
          <eTree>
            <label>N</label>
            <eLeaf>
              <label>periscope</label>
            </eLeaf>
          </eTree>
        </eTree>
      </eTree>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eTree-egXML-bq">
      <eTree n="ex1">
        <label>PP</label>
        <eTree>
          <label>P</label>
          <eLeaf>
            <label>avec</label>
          </eLeaf>
        </eTree>
        <eTree>
          <label>NP</label>
          <eTree>
            <label>Art</label>
            <eLeaf>
              <label>le</label>
            </eLeaf>
          </eTree>
          <eTree>
            <label>N</label>
            <eLeaf>
              <label>périscope</label>
            </eLeaf>
          </eTree>
        </eTree>
      </eTree>
    </egXML>
  </exemplum>
  <remarks ident="eTree-remarks" versionDate="2007-03-02" xml:lang="en">
    <p rend="dataDesc">an optional label followed by zero or more
    embedding trees, triangles, or embedding leafs.</p>
  </remarks>
  <remarks ident="eTree-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">une étiquette facultative suivie de zéro, un ou plusieurs arbres englobants, triangles ou feuilles englobantes.</p>
  </remarks>
  <remarks ident="eTree-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    ひとつ以上の部分木や部分木の葉に続いて、選択的にラベルをとる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#GDAT" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">embedding tree</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">내포 수형도</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">嵌入樹狀結構</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">arbre englobant</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">árbol integrado</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">albero integrato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">provides an alternative to the <gi>tree</gi> element for representing ordered rooted tree structures.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">순서가 있고 뿌리가 있는 수형 구조를 표시하기 위해 수형도 요소에 대체안을 제시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供樹元素的替換，用來表示整齊具有根節點的樹狀結構。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">順序付き根付き木を構成する部分木を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">élément à utiliser lorsqu'on a besoin d'imbriquer
    plusieurs structures arborescentes à racine et ordonnées, pour encoder chacune de ces structures (en effet, il n'est pas possible d'imbriquer des éléments <gi>tree</gi>).</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa una alternativa al elemento árbol para la representación de estructuras del tipo árbol enraizado ordenado</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rapresenta un'alternativa all'elemento albero per la rappresentazione di strutture del tipo albero radicato ordinato.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="label" minOccurs="0"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="eTree"/>
        <elementRef key="triangle"/>
        <elementRef key="eLeaf"/>
        <classRef key="model.ptrLike"/>
      </alternate>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides the value of an embedding tree, which is a feature
structure or other analytic element.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">내포 수형도의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個嵌入樹狀結構值，該嵌入樹狀結構為一個功能結構或其他分析元素。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該部分木の値を示す。素性構造または他の分析に関する要素になる。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par l'arbre englobant ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">adscribe al árbol integrado un valor, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna all'albero integrato un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eTree-egXML-kt">
      <eTree n="ex1">
        <label>PP</label>
        <eTree>
          <label>P</label>
          <eLeaf>
            <label>with</label>
          </eLeaf>
        </eTree>
        <eTree>
          <label>NP</label>
          <eTree>
            <label>Art</label>
            <eLeaf>
              <label>the</label>
            </eLeaf>
          </eTree>
          <eTree>
            <label>N</label>
            <eLeaf>
              <label>periscope</label>
            </eLeaf>
          </eTree>
        </eTree>
      </eTree>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eTree-egXML-bq">
      <eTree n="ex1">
        <label>PP</label>
        <eTree>
          <label>P</label>
          <eLeaf>
            <label>avec</label>
          </eLeaf>
        </eTree>
        <eTree>
          <label>NP</label>
          <eTree>
            <label>Art</label>
            <eLeaf>
              <label>le</label>
            </eLeaf>
          </eTree>
          <eTree>
            <label>N</label>
            <eLeaf>
              <label>périscope</label>
            </eLeaf>
          </eTree>
        </eTree>
      </eTree>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="eTree-remarks" versionDate="2007-03-02" xml:lang="en">
    <p rend="dataDesc">an optional label followed by zero or more
    embedding trees, triangles, or embedding leafs.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="eTree-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">une étiquette facultative suivie de zéro, un ou plusieurs arbres englobants, triangles ou feuilles englobantes.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="eTree-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    ひとつ以上の部分木や部分木の葉に続いて、選択的にラベルをとる。
    </p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDAT" type="div2"/>
  </listRef>
```

^b29

