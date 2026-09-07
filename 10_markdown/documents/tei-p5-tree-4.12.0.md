---
type: representation
source-type: document
source: '[[00_sources/tei-p5-tree-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 tree
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/tree.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# tree

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 14192. Git blob: `b3c1fffdd92b1d32706ca1661ef1b10eeec28998`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-tree" ident="tree">
  <gloss versionDate="2007-06-12" xml:lang="en">tree</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">arbre</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">encodes a tree, which is made up of a root, internal nodes,
leaves, and arcs from root to leaves.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수형도를 부호화하며, 이 수형도는 뿌리, 내부 노드, 단말노드, 그리고 뿌리로부터 단말 노드에 이르는 호로 구성된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記一個樹狀結構，包含根節點、內部節點、葉節點、以及從根到葉的連線。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">根、内部ノード、葉、矢(または辺)から成る木を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">encode un arbre, qui est composé d'une racine, de nœuds internes, de feuilles et d'arcs allant de la racine vers les feuilles.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">codifica un árbol, que se constituye de raíz, nodos internos, hojas, y arcos que conectan raíz y hojas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">codifica un albero, che è costituito da radice, nodi interni, foglie, e archi che collegano radice e foglie.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="label" minOccurs="0"/>
      <sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="leaf"/>
          <elementRef key="iNode"/>
        </alternate>
        <elementRef key="root"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="leaf"/>
          <elementRef key="iNode"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <attList>
    <attDef ident="arity" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the maximum number of children of the root and internal
nodes of the tree.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">뿌리의 자식 노드 및 수형도의 내부 노드의 최대 수를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">根節點所擁有的子節點數以及樹狀結構的內部節點數的最大值。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">木構造における、根や内部ノードが持つ子供の最大数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le nombre maximal d'enfants de la
        racine et des nœuds internes de l'arbre.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">establece el número máximo de hijos (descendientes) de la raíz y de los nodos internos del árbol.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">stabilisce il numero massimo di figli della radice e dei nodi interni dell'albero.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
    </attDef>
    <attDef ident="ord" usage="req">
      <gloss versionDate="2007-07-04" xml:lang="en">ordered</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">순서가 있는</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">ordenado</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">ordonné</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">ordinato</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the tree is ordered, or if it is
partially ordered.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">수형도가 순서가 있는지, 또는 수형도가 부분적으로 순서가 있는지를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明樹狀結構是否整齊排列，或是部分整齊排列。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該木構造が、順序付き木、または半順序付き木であるかどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si l'arbre est ordonné ou non ou s'il l'est partiellement.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el árbol es o no ordenado, o si es parcialmente ordenado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se l'albero è ordinato o parzialmente ordinato.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <!-- cant be boolean because we have to allow for partial ordering -->
      <valList type="closed">
        <valItem ident="true">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that all of the branching nodes of the tree are ordered.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수형도의 모든 분지 노드가 순서가 있음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">樹狀結構的所有分支節點皆整齊排列。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que todos los nodos de ramificación del árbol están ordenados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">木構造中の全ノードは、順序付きであることを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que, dans l'arbre, tous les nœuds d'embranchement sont ordonnés.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che tutti i nodi ramo dell'albero sono ordinati.</desc>
        </valItem>
        <valItem ident="partial">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that some of the branching nodes of the tree are ordered
and some are unordered.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수형도의 분지 노드 중 일부는 순서가 있고, 일부는 순서가 없음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">有些分支節點整齊排列，有些則否。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que algunos de los nodos de ramificación del árbol están ordenados y otros desordenados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">木構造中のノードの一部は順序付きであるが、一部は順序付きでは
          ないことを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que, dans l'arbre, certains
            nœuds d'embranchement sont ordonnés et d'autres non.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che alcuni dei nodi ramo dell'albero sono ordinati e che altri non lo sono.</desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that all of the branching nodes of the tree are
unordered.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수형도의 모든 분지 노드는 순서가 없음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">樹狀結構的所有分支節點皆未整齊排列。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que todos los nodos de ramificación del árbol estan desordenados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">木構造の全ノードは、順序付きではないことを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que, dans l'arbre, tous les
            nœuds d'embranchement sont non ordonnés.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che tutti i nodi ramo dell'albero non sono ordinati.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="order" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the order of the tree, i.e., the number of its nodes.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">수형도의 순서를 제시한다. 즉, 그 노드의 수</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供樹狀結構的次序，例如節點數目。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">木構造の順番を示す。例えば、ノードの番号を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne l'ordre de l'arbre, c'est-à-dire le
        nombre de ses nœuds.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el orden del árbol, es decir, el número de los nodos.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'ordine dell'albero, cioè il numero dei suoi nodi.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="tree-attr.order-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The size of a tree is always one less than its order, hence
there is no need for both a <att>size</att> and <att>order</att>
attribute.</p>
      </remarks>
      <remarks ident="tree-attr.order-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La taille d'un arbre étant toujours inférieure d'un à son ordre, il n'est donc pas nécessaire d'avoir en même temps un attribut <att>size</att> et un attribut <att>order</att>.</p>
      </remarks>
      <remarks ident="tree-attr.order-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        木構造中の辺数(サイズ)は、常にノード数(オーダー)より1少ない。
        従って、属性<att>size</att>と<att>order</att>の2つは必要ない。
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tree-egXML-si">
      <tree n="ex2" arity="2" ord="partial" order="13">
        <root xml:id="G-div1" children="#G-plu1 #G-exp1" ord="true">
          <label>/</label>
        </root>
        <iNode xml:id="G-plu1" children="#G-exp2 #G-exp3" parent="#G-div1" ord="false">
          <label>+</label>
        </iNode>
        <iNode xml:id="G-exp1" children="#G-plu2 #G-num2.3" parent="#G-div1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="G-exp2" children="#G-vara1 #G-num2.1" parent="#G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="G-exp3" children="#G-varb1 #G-num2.2" parent="#G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="G-plu2" children="#G-vara2 #G-varb2" parent="#G-exp1" ord="false">
          <label>+</label>
        </iNode>
        <leaf xml:id="G-vara1" parent="#G-exp2">
          <label>a</label>
        </leaf>
        <leaf xml:id="G-num2.1" parent="#G-exp2">
          <label>2</label>
        </leaf>
        <leaf xml:id="G-varb1" parent="#G-exp3">
          <label>b</label>
        </leaf>
        <leaf xml:id="G-num2.2" parent="#G-exp3">
          <label>2</label>
        </leaf>
        <leaf xml:id="G-vara2" parent="#G-plu2">
          <label>a</label>
        </leaf>
        <leaf xml:id="G-varb2" parent="#G-plu2">
          <label>b</label>
        </leaf>
        <leaf xml:id="G-num2.3" parent="#G-exp1">
          <label>2</label>
        </leaf>
      </tree>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tree-egXML-rm">
      <tree n="ex2" arity="2" ord="partial" order="13">
        <root xml:id="fr_G-div1" children="#fr_G-plu1 #fr_G-exp1" ord="true">
          <label>/</label>
        </root>
        <iNode xml:id="fr_G-plu1" children="#fr_G-exp2 #fr_G-exp3" parent="#fr_G-div1" ord="false">
          <label>+</label>
        </iNode>
        <iNode xml:id="fr_G-exp1" children="#fr_G-plu2 #fr_G-num2.3" parent="#fr_G-div1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="fr_G-exp2" children="#fr_G-vara1 #fr_G-num2.1" parent="#fr_G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="fr_G-exp3" children="#fr_G-varb1 #fr_G-num2.2" parent="#fr_G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="fr_G-plu2" children="#fr_G-vara2 #fr_G-varb2" parent="#fr_G-exp1" ord="false">
          <label>+</label>
        </iNode>
        <leaf xml:id="fr_G-vara1" parent="#fr_G-exp2">
          <label>a</label>
        </leaf>
        <leaf xml:id="fr_G-num2.1" parent="#fr_G-exp2">
          <label>2</label>
        </leaf>
        <leaf xml:id="fr_G-varb1" parent="#fr_G-exp3">
          <label>b</label>
        </leaf>
        <leaf xml:id="fr_G-num2.2" parent="#fr_G-exp3">
          <label>2</label>
        </leaf>
        <leaf xml:id="fr_G-vara2" parent="#fr_G-plu2">
          <label>a</label>
        </leaf>
        <leaf xml:id="fr_G-varb2" parent="#fr_G-plu2">
          <label>b</label>
        </leaf>
        <leaf xml:id="fr_G-num2.3" parent="#fr_G-exp1">
          <label>2</label>
        </leaf>
      </tree>
    </egXML>
  </exemplum>
  <remarks ident="tree-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">A root, and zero or more internal nodes and leaves, but if
there is an internal node, there must also be at least one leaf.</p>
  </remarks>
  <remarks ident="tree-remarks" versionDate="2009-11-17" xml:lang="fr">
    <p rend="dataDesc">Il doit y avoir un nœud racine et zéro, un ou plusieurs nœuds internes
      et feuilles. S'il y a un nœud interne, il doit y avoir au moins une feuille.</p>
  </remarks>
  <remarks ident="tree-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    根がひとつ、0以上の内部ノード、複数の葉。但し、内部ノードが1つの
    場合は、葉は1つになる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#GDTR" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">tree</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">arbre</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">encodes a tree, which is made up of a root, internal nodes,
leaves, and arcs from root to leaves.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수형도를 부호화하며, 이 수형도는 뿌리, 내부 노드, 단말노드, 그리고 뿌리로부터 단말 노드에 이르는 호로 구성된다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記一個樹狀結構，包含根節點、內部節點、葉節點、以及從根到葉的連線。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">根、内部ノード、葉、矢(または辺)から成る木を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">encode un arbre, qui est composé d'une racine, de nœuds internes, de feuilles et d'arcs allant de la racine vers les feuilles.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">codifica un árbol, que se constituye de raíz, nodos internos, hojas, y arcos que conectan raíz y hojas.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codifica un albero, che è costituito da radice, nodi interni, foglie, e archi che collegano radice e foglie.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="label" minOccurs="0"/>
      <sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="leaf"/>
          <elementRef key="iNode"/>
        </alternate>
        <elementRef key="root"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="leaf"/>
          <elementRef key="iNode"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the maximum number of children of the root and internal
nodes of the tree.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">뿌리의 자식 노드 및 수형도의 내부 노드의 최대 수를 제시한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">根節點所擁有的子節點數以及樹狀結構的內部節點數的最大值。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">木構造における、根や内部ノードが持つ子供の最大数を示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne le nombre maximal d'enfants de la
        racine et des nœuds internes de l'arbre.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">establece el número máximo de hijos (descendientes) de la raíz y de los nodos internos del árbol.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">stabilisce il numero massimo di figli della radice e dei nodi interni dell'albero.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">ordered</gloss>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">순서가 있는</gloss>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">ordenado</gloss>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">ordonné</gloss>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">ordinato</gloss>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the tree is ordered, or if it is
partially ordered.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수형도가 순서가 있는지, 또는 수형도가 부분적으로 순서가 있는지를 나타낸다.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明樹狀結構是否整齊排列，或是部分整齊排列。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該木構造が、順序付き木、または半順序付き木であるかどうかを示す。</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si l'arbre est ordonné ou non ou s'il l'est partiellement.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el árbol es o no ordenado, o si es parcialmente ordenado.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se l'albero è ordinato o parzialmente ordinato.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="true">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that all of the branching nodes of the tree are ordered.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수형도의 모든 분지 노드가 순서가 있음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">樹狀結構的所有分支節點皆整齊排列。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que todos los nodos de ramificación del árbol están ordenados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">木構造中の全ノードは、順序付きであることを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que, dans l'arbre, tous les nœuds d'embranchement sont ordonnés.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che tutti i nodi ramo dell'albero sono ordinati.</desc>
        </valItem>
        <valItem ident="partial">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that some of the branching nodes of the tree are ordered
and some are unordered.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수형도의 분지 노드 중 일부는 순서가 있고, 일부는 순서가 없음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">有些分支節點整齊排列，有些則否。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que algunos de los nodos de ramificación del árbol están ordenados y otros desordenados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">木構造中のノードの一部は順序付きであるが、一部は順序付きでは
          ないことを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que, dans l'arbre, certains
            nœuds d'embranchement sont ordonnés et d'autres non.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che alcuni dei nodi ramo dell'albero sono ordinati e che altri non lo sono.</desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2007-06-27" xml:lang="en">indicates that all of the branching nodes of the tree are
unordered.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수형도의 모든 분지 노드는 순서가 없음을 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">樹狀結構的所有分支節點皆未整齊排列。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que todos los nodos de ramificación del árbol estan desordenados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">木構造の全ノードは、順序付きではないことを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indique que, dans l'arbre, tous les
            nœuds d'embranchement sont non ordonnés.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che tutti i nodi ramo dell'albero non sono ordinati.</desc>
        </valItem>
      </valList>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the order of the tree, i.e., the number of its nodes.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수형도의 순서를 제시한다. 즉, 그 노드의 수</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供樹狀結構的次序，例如節點數目。</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">木構造の順番を示す。例えば、ノードの番号を示す。</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne l'ordre de l'arbre, c'est-à-dire le
        nombre de ses nœuds.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el orden del árbol, es decir, el número de los nodos.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'ordine dell'albero, cioè il numero dei suoi nodi.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="tree-attr.order-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The size of a tree is always one less than its order, hence
there is no need for both a <att>size</att> and <att>order</att>
attribute.</p>
      </remarks>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="tree-attr.order-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La taille d'un arbre étant toujours inférieure d'un à son ordre, il n'est donc pas nécessaire d'avoir en même temps un attribut <att>size</att> et un attribut <att>order</att>.</p>
      </remarks>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="tree-attr.order-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        木構造中の辺数(サイズ)は、常にノード数(オーダー)より1少ない。
        従って、属性<att>size</att>と<att>order</att>の2つは必要ない。
        </p>
      </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tree-egXML-si">
      <tree n="ex2" arity="2" ord="partial" order="13">
        <root xml:id="G-div1" children="#G-plu1 #G-exp1" ord="true">
          <label>/</label>
        </root>
        <iNode xml:id="G-plu1" children="#G-exp2 #G-exp3" parent="#G-div1" ord="false">
          <label>+</label>
        </iNode>
        <iNode xml:id="G-exp1" children="#G-plu2 #G-num2.3" parent="#G-div1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="G-exp2" children="#G-vara1 #G-num2.1" parent="#G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="G-exp3" children="#G-varb1 #G-num2.2" parent="#G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="G-plu2" children="#G-vara2 #G-varb2" parent="#G-exp1" ord="false">
          <label>+</label>
        </iNode>
        <leaf xml:id="G-vara1" parent="#G-exp2">
          <label>a</label>
        </leaf>
        <leaf xml:id="G-num2.1" parent="#G-exp2">
          <label>2</label>
        </leaf>
        <leaf xml:id="G-varb1" parent="#G-exp3">
          <label>b</label>
        </leaf>
        <leaf xml:id="G-num2.2" parent="#G-exp3">
          <label>2</label>
        </leaf>
        <leaf xml:id="G-vara2" parent="#G-plu2">
          <label>a</label>
        </leaf>
        <leaf xml:id="G-varb2" parent="#G-plu2">
          <label>b</label>
        </leaf>
        <leaf xml:id="G-num2.3" parent="#G-exp1">
          <label>2</label>
        </leaf>
      </tree>
    </egXML>
  </exemplum>
```

^b45

### Block 46

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tree-egXML-rm">
      <tree n="ex2" arity="2" ord="partial" order="13">
        <root xml:id="fr_G-div1" children="#fr_G-plu1 #fr_G-exp1" ord="true">
          <label>/</label>
        </root>
        <iNode xml:id="fr_G-plu1" children="#fr_G-exp2 #fr_G-exp3" parent="#fr_G-div1" ord="false">
          <label>+</label>
        </iNode>
        <iNode xml:id="fr_G-exp1" children="#fr_G-plu2 #fr_G-num2.3" parent="#fr_G-div1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="fr_G-exp2" children="#fr_G-vara1 #fr_G-num2.1" parent="#fr_G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="fr_G-exp3" children="#fr_G-varb1 #fr_G-num2.2" parent="#fr_G-plu1" ord="true">
          <label>**</label>
        </iNode>
        <iNode xml:id="fr_G-plu2" children="#fr_G-vara2 #fr_G-varb2" parent="#fr_G-exp1" ord="false">
          <label>+</label>
        </iNode>
        <leaf xml:id="fr_G-vara1" parent="#fr_G-exp2">
          <label>a</label>
        </leaf>
        <leaf xml:id="fr_G-num2.1" parent="#fr_G-exp2">
          <label>2</label>
        </leaf>
        <leaf xml:id="fr_G-varb1" parent="#fr_G-exp3">
          <label>b</label>
        </leaf>
        <leaf xml:id="fr_G-num2.2" parent="#fr_G-exp3">
          <label>2</label>
        </leaf>
        <leaf xml:id="fr_G-vara2" parent="#fr_G-plu2">
          <label>a</label>
        </leaf>
        <leaf xml:id="fr_G-varb2" parent="#fr_G-plu2">
          <label>b</label>
        </leaf>
        <leaf xml:id="fr_G-num2.3" parent="#fr_G-exp1">
          <label>2</label>
        </leaf>
      </tree>
    </egXML>
  </exemplum>
```

^b46

### Block 47

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="tree-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">A root, and zero or more internal nodes and leaves, but if
there is an internal node, there must also be at least one leaf.</p>
  </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="tree-remarks" versionDate="2009-11-17" xml:lang="fr">
    <p rend="dataDesc">Il doit y avoir un nœud racine et zéro, un ou plusieurs nœuds internes
      et feuilles. S'il y a un nœud interne, il doit y avoir au moins une feuille.</p>
  </remarks>
```

^b48

### Block 49

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="tree-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    根がひとつ、0以上の内部ノード、複数の葉。但し、内部ノードが1つの
    場合は、葉は1つになる。
    </p>
  </remarks>
```

^b49

### Block 50

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDTR" type="div2"/>
  </listRef>
```

^b50

