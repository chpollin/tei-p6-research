---
type: representation
source-type: document
source: '[[00_sources/tei-p5-inode-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 iNode
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/iNode.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# iNode

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12079. Git blob: `06ba19bcde5f8e5edbabcf22a6b179eb74ed0b73`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-iNode" ident="iNode">
  <gloss versionDate="2005-01-14" xml:lang="en">intermediate (or internal) node</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">중간 (또는 내부) 노드</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">中間 (或內部) 節點</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">nœud intermédiaire (ou interne)</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nodo intermedio (o interno)</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nodo intermedio (o interno)</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents an intermediate (or internal) node of a tree.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수형도의 중간 (또는 내부) 노드를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個樹狀結構的中間 (或內部) 節點。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">木における内部ノードを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente un nœud intermédiaire (ou interne) dans un arbre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa un nodo intermedio (o interno) de un árbol.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta un nodo intermedio (o interno) di un albero.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    
      <elementRef key="label" minOccurs="0"/>
    
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2013-12-21" xml:lang="en">indicates an intermediate node, which is a feature
structure or other analytic element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">중간 노드의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個中間節點值，該節點為一個功能結構或其他分析元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">内部ノードの値を示す。素性構造向け要素または分析向け要素になる。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par le nœud intermédiaire ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el valor de un nodo intermedio, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna a un nodo intermedio un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="children" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">provides a list of identifiers of the elements which are the children of
the intermediate node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">중간 노드의 자식인 요소의 확인소 목록을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供中間節點的子節點之元素識別符碼列表。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該内部ノードの子要素の識別子をまとめたリストを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit une liste des identifiants des
        éléments qui sont les enfants du nœud intermédiaire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona una lista de identificadores de elementos que son hijos de un nodo intermedio.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce una lista di identificatori degli elementi figli del nodo intermedio.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="parent" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">provides the identifier of the element which is the parent of this node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 노드의 부모인 요소의 확인소를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供中間節點的雙親節點的元素識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該ノードの親要素の識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'élément parent
        de ce nœud.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador del elemento padre de un nodo dado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento genitore del nodo.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="ord" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">ordered</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">순서가 있는</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">ordenado</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">ordonné</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">ordinato</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the internal node is ordered.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">내부 노드가 순서가 있는지를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明內部節點是否整齊排列。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該内部ノードが順序付きかどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si le nœud interne est ou non ordonné.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el nodo interno está ordenado o no.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se il nodo interno è ordinato o meno.</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <remarks ident="iNode-attr.ord-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the children of
	the intermediate node are ordered, whereas <val>false</val>
	indicates the are unordered.</p>
        <p>Use if and only if <att>ord</att> is specified as
	<val>partial</val> on the <gi>tree</gi> element and the
	intermediate node has more than one child.</p>
      </remarks>
      <remarks ident="iNode-attr.ord-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que les enfants du nœud intermédiaire sont
ordonnés, alors que la valeur <val>false</val> indique qu'ils ne le sont pas.</p>
        <p>Utiliser si, et seulement si, l'attribut <att>ord</att> de l'élément <gi>tree</gi>a la valeur <val>partial</val> et que le nœud intermédiaire a plus d'un enfant.</p>
      </remarks>
      <remarks ident="iNode-attr.ord-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	属性値<val>true</val>は、当該内部ノードの子要素は順序付きであ
      ることを示す。属性値<val>false</val>は、順序付きでないことを示す。
      </p>
        <p>
	要素<gi>tree</gi>の属性<att>ord</att>が値<att>ord</att>を持ち、
      当該内部ノードが複数の子要素を持つ時のみ、使用される。
      </p>
      </remarks>
    </attDef>
    <attDef ident="follow" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">provides the identifier of
an element which this node follows.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 노드가 따르는 요소의 확인소를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供此節點所尾隨的元素識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該ノードの姉要素の識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'élément que ce nœud suit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador al elemento que precede al nodo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento che precede il nodo.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="iNode-attr.follow-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If the tree is unordered or partially ordered, this attribute
has the property of fixing the relative order of the intermediate node
and the element which is the value of the attribute.</p>
      </remarks>
      <remarks ident="iNode-attr.follow-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si l'arbre n'est pas ordonné ou l'est partiellement, cet attribut a la
                        propriété de fixer l'ordre relatif du nœud intermédiaire et de l'élément
                        indiqué comme valeur de l'attribut.</p>
      </remarks>
      <remarks ident="iNode-attr.follow-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	当該木が順序付きでないか、または部分的な順序付きである場合、当
      該属性は、当該内部ノードや属性の値としてある要素が相対的な順序で
      あることを示す。
      </p>
      </remarks>
    </attDef>
    <attDef ident="outDegree" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the out degree of an intermediate node, the number of its
children.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">중간 노드의 정도, 즉, 그 자식의 수를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">中間節點的向外分支度，即為其子節點的數量。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">内部ノードの出の次数(子要素の数)を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le degré sortant d'un nœud intermédiaire, c'est-à-dire le nombre de ses enfants.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el grado de salida del nodo intermedio, es decir, el número de sus hijos.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il grado in uscita di un nodo intermedio, cioè il numero dei suoi figli.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="iNode-attr.outDegree-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The in degree of an intermediate node is always 1.</p>
      </remarks>
      <remarks ident="iNode-attr.outDegree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Le degré entrant d'un nœud intermédiaire est toujours 1. </p>
      </remarks>
      <remarks ident="iNode-attr.outDegree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	内部ノードの入りの次数(親への辺数)は常に1である。
	</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iNode-egXML-og">
      <iNode xml:id="pt1" children="#GD-UP1" parent="#GD-VB1" follow="#GD-PN1" outDegree="1">
        <label>PT</label>
      </iNode>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iNode-egXML-ov">
      <iNode xml:id="fr_pt1" children="#fr_GD-UP1" parent="#fr_GD-VB1" follow="#GD-PN1" outDegree="1">
        <label>PT</label>
      </iNode>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#GDTR" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">intermediate (or internal) node</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">중간 (또는 내부) 노드</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">中間 (或內部) 節點</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">nœud intermédiaire (ou interne)</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nodo intermedio (o interno)</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nodo intermedio (o interno)</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents an intermediate (or internal) node of a tree.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수형도의 중간 (또는 내부) 노드를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個樹狀結構的中間 (或內部) 節點。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">木における内部ノードを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente un nœud intermédiaire (ou interne) dans un arbre.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa un nodo intermedio (o interno) de un árbol.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta un nodo intermedio (o interno) di un albero.</desc>
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
    
      <elementRef key="label" minOccurs="0"/>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">indicates an intermediate node, which is a feature
structure or other analytic element.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">중간 노드의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個中間節點值，該節點為一個功能結構或其他分析元素。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">内部ノードの値を示す。素性構造向け要素または分析向け要素になる。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par le nœud intermédiaire ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el valor de un nodo intermedio, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna a un nodo intermedio un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides a list of identifiers of the elements which are the children of
the intermediate node.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">중간 노드의 자식인 요소의 확인소 목록을 제시한다.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供中間節點的子節點之元素識別符碼列表。</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該内部ノードの子要素の識別子をまとめたリストを示す。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit une liste des identifiants des
        éléments qui sont les enfants du nœud intermédiaire.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una lista de identificadores de elementos que son hijos de un nodo intermedio.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce una lista di identificatori degli elementi figli del nodo intermedio.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides the identifier of the element which is the parent of this node.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 노드의 부모인 요소의 확인소를 제공한다.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供中間節點的雙親節點的元素識別符碼。</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該ノードの親要素の識別子を示す。</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'élément parent
        de ce nœud.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador del elemento padre de un nodo dado.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento genitore del nodo.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">ordered</gloss>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">순서가 있는</gloss>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">ordenado</gloss>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">ordonné</gloss>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">ordinato</gloss>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the internal node is ordered.</desc>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">내부 노드가 순서가 있는지를 표시한다.</desc>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明內部節點是否整齊排列。</desc>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該内部ノードが順序付きかどうかを示す。</desc>
```

^b48

### Block 49

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si le nœud interne est ou non ordonné.</desc>
```

^b49

### Block 50

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el nodo interno está ordenado o no.</desc>
```

^b50

### Block 51

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se il nodo interno è ordinato o meno.</desc>
```

^b51

### Block 52

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b52

### Block 53

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="iNode-attr.ord-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the children of
	the intermediate node are ordered, whereas <val>false</val>
	indicates the are unordered.</p>
        <p>Use if and only if <att>ord</att> is specified as
	<val>partial</val> on the <gi>tree</gi> element and the
	intermediate node has more than one child.</p>
      </remarks>
```

^b53

### Block 54

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[2]`.

```xml
<remarks ident="iNode-attr.ord-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que les enfants du nœud intermédiaire sont
ordonnés, alors que la valeur <val>false</val> indique qu'ils ne le sont pas.</p>
        <p>Utiliser si, et seulement si, l'attribut <att>ord</att> de l'élément <gi>tree</gi>a la valeur <val>partial</val> et que le nœud intermédiaire a plus d'un enfant.</p>
      </remarks>
```

^b54

### Block 55

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[3]`.

```xml
<remarks ident="iNode-attr.ord-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	属性値<val>true</val>は、当該内部ノードの子要素は順序付きであ
      ることを示す。属性値<val>false</val>は、順序付きでないことを示す。
      </p>
        <p>
	要素<gi>tree</gi>の属性<att>ord</att>が値<att>ord</att>を持ち、
      当該内部ノードが複数の子要素を持つ時のみ、使用される。
      </p>
      </remarks>
```

^b55

### Block 56

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides the identifier of
an element which this node follows.</desc>
```

^b56

### Block 57

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 노드가 따르는 요소의 확인소를 제공한다.</desc>
```

^b57

### Block 58

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供此節點所尾隨的元素識別符碼。</desc>
```

^b58

### Block 59

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該ノードの姉要素の識別子を示す。</desc>
```

^b59

### Block 60

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'élément que ce nœud suit.</desc>
```

^b60

### Block 61

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador al elemento que precede al nodo.</desc>
```

^b61

### Block 62

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento che precede il nodo.</desc>
```

^b62

### Block 63

XML location: `/elementSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b63

### Block 64

XML location: `/elementSpec[1]/attList[1]/attDef[5]/remarks[1]`.

```xml
<remarks ident="iNode-attr.follow-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If the tree is unordered or partially ordered, this attribute
has the property of fixing the relative order of the intermediate node
and the element which is the value of the attribute.</p>
      </remarks>
```

^b64

### Block 65

XML location: `/elementSpec[1]/attList[1]/attDef[5]/remarks[2]`.

```xml
<remarks ident="iNode-attr.follow-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si l'arbre n'est pas ordonné ou l'est partiellement, cet attribut a la
                        propriété de fixer l'ordre relatif du nœud intermédiaire et de l'élément
                        indiqué comme valeur de l'attribut.</p>
      </remarks>
```

^b65

### Block 66

XML location: `/elementSpec[1]/attList[1]/attDef[5]/remarks[3]`.

```xml
<remarks ident="iNode-attr.follow-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	当該木が順序付きでないか、または部分的な順序付きである場合、当
      該属性は、当該内部ノードや属性の値としてある要素が相対的な順序で
      あることを示す。
      </p>
      </remarks>
```

^b66

### Block 67

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the out degree of an intermediate node, the number of its
children.</desc>
```

^b67

### Block 68

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">중간 노드의 정도, 즉, 그 자식의 수를 제시한다.</desc>
```

^b68

### Block 69

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">中間節點的向外分支度，即為其子節點的數量。</desc>
```

^b69

### Block 70

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">内部ノードの出の次数(子要素の数)を示す。</desc>
```

^b70

### Block 71

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne le degré sortant d'un nœud intermédiaire, c'est-à-dire le nombre de ses enfants.</desc>
```

^b71

### Block 72

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el grado de salida del nodo intermedio, es decir, el número de sus hijos.</desc>
```

^b72

### Block 73

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il grado in uscita di un nodo intermedio, cioè il numero dei suoi figli.</desc>
```

^b73

### Block 74

XML location: `/elementSpec[1]/attList[1]/attDef[6]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b74

### Block 75

XML location: `/elementSpec[1]/attList[1]/attDef[6]/remarks[1]`.

```xml
<remarks ident="iNode-attr.outDegree-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The in degree of an intermediate node is always 1.</p>
      </remarks>
```

^b75

### Block 76

XML location: `/elementSpec[1]/attList[1]/attDef[6]/remarks[2]`.

```xml
<remarks ident="iNode-attr.outDegree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Le degré entrant d'un nœud intermédiaire est toujours 1. </p>
      </remarks>
```

^b76

### Block 77

XML location: `/elementSpec[1]/attList[1]/attDef[6]/remarks[3]`.

```xml
<remarks ident="iNode-attr.outDegree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	内部ノードの入りの次数(親への辺数)は常に1である。
	</p>
      </remarks>
```

^b77

### Block 78

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iNode-egXML-og">
      <iNode xml:id="pt1" children="#GD-UP1" parent="#GD-VB1" follow="#GD-PN1" outDegree="1">
        <label>PT</label>
      </iNode>
    </egXML>
  </exemplum>
```

^b78

### Block 79

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iNode-egXML-ov">
      <iNode xml:id="fr_pt1" children="#fr_GD-UP1" parent="#fr_GD-VB1" follow="#GD-PN1" outDegree="1">
        <label>PT</label>
      </iNode>
    </egXML>
  </exemplum>
```

^b79

### Block 80

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDTR" type="div2"/>
  </listRef>
```

^b80

