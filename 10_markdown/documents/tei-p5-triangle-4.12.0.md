---
type: representation
source-type: document
source: '[[00_sources/tei-p5-triangle-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 triangle
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/triangle.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# triangle

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5555. Git blob: `d98d4948a253763217ef86ee1baaafba26f6e1a8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-triangle" ident="triangle">
  <gloss versionDate="2007-09-24" xml:lang="en">underspecified embedding tree, so called because of its
  characteristic shape when drawn</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">미명시된 내포 수형도, 도출될 때 그 특성적 모양 때문에 그렇게 불린다.</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">不完全嵌入樹狀結構，如同畫出的圖形特徵所顯示。</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">triangle : arbre englobant sommaire, appelé ainsi en raison de sa forme caractéristique quand il est dessiné.</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">árbol integrado insuficientemente especificado, llamado así a causa de la forma característica que asume cuando se diseña.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">albero integrato insufficientemente specificato, così chiamato a causa della caratteristica forma che assume quando viene disegnato</gloss>
  <desc versionDate="2017-06-14" xml:lang="en">provides for an underspecified <gi>eTree</gi>, that is, an <gi>eTree</gi> with
  information left out.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">미명시된 eTree를 제시한다. 즉, 정보가 삭제된 eTree</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">為不完全之<gi>嵌入樹狀結構</gi>所提供的元素，即資訊不足的<gi>嵌入樹狀結構</gi>。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">未定義の部分木(eTree)、すなわち情報が付与されていない部分木を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">désigne un arbre englobant sommaire, c'est-à-dire pour lequel toutes les informations ne sont pas données.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define un eTree insuficientemente especificado, es decir, un eTree con algunas informaciones excluidas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un eTree insufficientemente specificato, cioè un eTree con alcune informazioni escluse.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      
        <elementRef key="label" minOccurs="0"/>
      
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="eTree"/>
          <elementRef key="triangle"/>
          <elementRef key="eLeaf"/>
        </alternate>
      
    </sequence>
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2013-11-21" xml:lang="en">supplies a value
      for the triangle, in the form of the identifier of a feature
structure or other analytic element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">삼각형의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소의 확인소이다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個三角樹狀結構值，該三角樹狀結構為一個功能結構或其他分析元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">省略部分木の値を示す。素性構造または他の分析要素の識別子になる。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par le triangle ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">asigna al triángulo un valor, que puede ser el identificador de una estructura de rasgos u otro elemento de análisis.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna al triangolo un valore, che può essere l'dentificatore di una struttura di tratti o altro elemento di analisi.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-triangle-egXML-ui">
      <triangle>
        <label>NP</label>
        <eLeaf>
          <label>the periscope</label>
        </eLeaf>
      </triangle>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-triangle-egXML-mt">
      <triangle value="#NP">
        <label>NP</label>
        <eLeaf>
          <label>le périscope</label>
        </eLeaf>
      </triangle>
    </egXML>
  </exemplum>
  <remarks ident="triangle-remarks" versionDate="2007-03-02" xml:lang="en">
    <p rend="dataDesc">An optional label followed by zero or more
    embedding trees, triangles, or embedding leafs.</p>
  </remarks>
  <remarks ident="triangle-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">une étiquette facultative suivie de zéro, un ou plusieurs arbres englobants, triangles ou feuilles englobantes.</p>
  </remarks>
  <remarks ident="triangle-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    0以上の部分木、省略部分木、部分木の葉が続く、選択的なラベル。
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
<gloss versionDate="2007-09-24" xml:lang="en">underspecified embedding tree, so called because of its
  characteristic shape when drawn</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">미명시된 내포 수형도, 도출될 때 그 특성적 모양 때문에 그렇게 불린다.</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">不完全嵌入樹狀結構，如同畫出的圖形特徵所顯示。</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">triangle : arbre englobant sommaire, appelé ainsi en raison de sa forme caractéristique quand il est dessiné.</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">árbol integrado insuficientemente especificado, llamado así a causa de la forma característica que asume cuando se diseña.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">albero integrato insufficientemente specificato, così chiamato a causa della caratteristica forma che assume quando viene disegnato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-06-14" xml:lang="en">provides for an underspecified <gi>eTree</gi>, that is, an <gi>eTree</gi> with
  information left out.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">미명시된 eTree를 제시한다. 즉, 정보가 삭제된 eTree</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">為不完全之<gi>嵌入樹狀結構</gi>所提供的元素，即資訊不足的<gi>嵌入樹狀結構</gi>。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">未定義の部分木(eTree)、すなわち情報が付与されていない部分木を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">désigne un arbre englobant sommaire, c'est-à-dire pour lequel toutes les informations ne sont pas données.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define un eTree insuficientemente especificado, es decir, un eTree con algunas informaciones excluidas.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un eTree insufficientemente specificato, cioè un eTree con alcune informazioni escluse.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
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
        </alternate>
      
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-11-21" xml:lang="en">supplies a value
      for the triangle, in the form of the identifier of a feature
structure or other analytic element.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">삼각형의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소의 확인소이다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個三角樹狀結構值，該三角樹狀結構為一個功能結構或其他分析元素。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">省略部分木の値を示す。素性構造または他の分析要素の識別子になる。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par le triangle ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">asigna al triángulo un valor, que puede ser el identificador de una estructura de rasgos u otro elemento de análisis.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna al triangolo un valore, che può essere l'dentificatore di una struttura di tratti o altro elemento di analisi.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-triangle-egXML-ui">
      <triangle>
        <label>NP</label>
        <eLeaf>
          <label>the periscope</label>
        </eLeaf>
      </triangle>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-triangle-egXML-mt">
      <triangle value="#NP">
        <label>NP</label>
        <eLeaf>
          <label>le périscope</label>
        </eLeaf>
      </triangle>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="triangle-remarks" versionDate="2007-03-02" xml:lang="en">
    <p rend="dataDesc">An optional label followed by zero or more
    embedding trees, triangles, or embedding leafs.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="triangle-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">une étiquette facultative suivie de zéro, un ou plusieurs arbres englobants, triangles ou feuilles englobantes.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="triangle-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    0以上の部分木、省略部分木、部分木の葉が続く、選択的なラベル。
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

