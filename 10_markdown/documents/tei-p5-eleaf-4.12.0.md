---
type: representation
source-type: document
source: '[[00_sources/tei-p5-eleaf-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 eLeaf
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/eLeaf.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# eLeaf

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5255. Git blob: `ddd27ddf4c2943cf5446792f92872ad5945c36b6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-eLeaf" ident="eLeaf">
  <gloss versionDate="2007-09-24" xml:lang="en">leaf or terminal node of an embedding tree</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">내포 수형도의 단말 노드</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">嵌入樹狀結構的葉節點。</gloss>
  <gloss versionDate="2009-11-17" xml:lang="fr">feuille ou nœud terminal d'un arbre englobant</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">hoja de un árbol integrado.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">foglia di un albero integrato</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">provides explicitly for a leaf of an embedding tree, which may also
be encoded with the <gi>eTree</gi> element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">내포 수형도의 단말 노드를 명시적으로 제공한다. 내포 수형도는 또한 eTree 요소로 부호화될 수 있다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">為嵌入樹狀結構的葉節點所明確提供的元素，也可用元素<gi>eTree</gi>來標記。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">部分木における葉を示す。要素eTree中で使用される。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">la feuille d'un arbre englobant, qui peut aussi être encodée au moyen d'un élément <gi>eTree</gi></desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona explícitamente una hoja de un árbol integrado, que puede ser codificado también con el elemento eTree.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce esplicitamente una foglia di un albero integrato, che può essere codificato anche con l'elemento eTree.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <sequence>
      
        <elementRef key="label" minOccurs="0"/>
      
      
        <classRef key="model.ptrLike" minOccurs="0"/>
      
    </sequence>
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates the value of an embedding leaf, which is a feature
structure or other analytic element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">내포 단말 노드의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個嵌入葉節點值，該嵌入葉節點為一個功能結構或其他分析元素。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de una hoja embute, que es la estructura de rasgo u otro elemento analítico.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">部分木の葉の値を示す。この葉は、素性構造または他の分析に関する要
      素である。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par la feuille de l'arbre englobant ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna alla foglia integrata un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
</attDef>  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eLeaf-egXML-to">
      <eLeaf value="http://an.fsurl.tei/#FSWITH">
        <label>with</label>
      </eLeaf>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eLeaf-egXML-rv">
      <eLeaf value="http://an.fsurl.tei/#FSWITH">
        <label>avec</label>
      </eLeaf>
    </egXML>
  </exemplum>
  <remarks ident="eLeaf-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>eTree</gi> tag may be used if the encoder does not
wish to distinguish by name between nonleaf and leaf nodes in
embedding trees; they are distinguished by their arrangement.</p>
  </remarks>
  <remarks ident="eLeaf-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La balise <gi>eTree</gi> peut être utilisée si l'encodeur ne souhaite pas faire une distinction de nom entre des nœuds terminaux (feuilles) ou non-terminaux dans des arbres englobants ; ils sont distingués par leur disposition.</p>
  </remarks>
  <remarks ident="eLeaf-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    符号化する人が、部分木において葉ノードと非葉ノードを名前で区別した
    くない時に、要素<gi>eTree</gi>は使用されるかもしれない。
    この違いは、配置で決まる。
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
<gloss versionDate="2007-09-24" xml:lang="en">leaf or terminal node of an embedding tree</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">내포 수형도의 단말 노드</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">嵌入樹狀結構的葉節點。</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-11-17" xml:lang="fr">feuille ou nœud terminal d'un arbre englobant</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">hoja de un árbol integrado.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">foglia di un albero integrato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">provides explicitly for a leaf of an embedding tree, which may also
be encoded with the <gi>eTree</gi> element.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">내포 수형도의 단말 노드를 명시적으로 제공한다. 내포 수형도는 또한 eTree 요소로 부호화될 수 있다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">為嵌入樹狀結構的葉節點所明確提供的元素，也可用元素<gi>eTree</gi>來標記。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">部分木における葉を示す。要素eTree中で使用される。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">la feuille d'un arbre englobant, qui peut aussi être encodée au moyen d'un élément <gi>eTree</gi></desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona explícitamente una hoja de un árbol integrado, que puede ser codificado también con el elemento eTree.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce esplicitamente una foglia di un albero integrato, che può essere codificato anche con l'elemento eTree.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <elementRef key="label" minOccurs="0"/>
      
      
        <classRef key="model.ptrLike" minOccurs="0"/>
      
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the value of an embedding leaf, which is a feature
structure or other analytic element.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">내포 단말 노드의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個嵌入葉節點值，該嵌入葉節點為一個功能結構或其他分析元素。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de una hoja embute, que es la estructura de rasgo u otro elemento analítico.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">部分木の葉の値を示す。この葉は、素性構造または他の分析に関する要
      素である。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par la feuille de l'arbre englobant ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna alla foglia integrata un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eLeaf-egXML-to">
      <eLeaf value="http://an.fsurl.tei/#FSWITH">
        <label>with</label>
      </eLeaf>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eLeaf-egXML-rv">
      <eLeaf value="http://an.fsurl.tei/#FSWITH">
        <label>avec</label>
      </eLeaf>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="eLeaf-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>eTree</gi> tag may be used if the encoder does not
wish to distinguish by name between nonleaf and leaf nodes in
embedding trees; they are distinguished by their arrangement.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="eLeaf-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La balise <gi>eTree</gi> peut être utilisée si l'encodeur ne souhaite pas faire une distinction de nom entre des nœuds terminaux (feuilles) ou non-terminaux dans des arbres englobants ; ils sont distingués par leur disposition.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="eLeaf-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    符号化する人が、部分木において葉ノードと非葉ノードを名前で区別した
    くない時に、要素<gi>eTree</gi>は使用されるかもしれない。
    この違いは、配置で決まる。
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

