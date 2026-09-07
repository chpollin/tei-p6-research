---
type: representation
source-type: document
source: '[[00_sources/tei-p5-root-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 root
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/root.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# root

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9657. Git blob: `3895f042abd3e232f0848c2a69b7a210cfe9c5d9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-root" ident="root">
  <gloss versionDate="2005-01-14" xml:lang="en">root node</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">뿌리 노드</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">根節點</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">nœud racine</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nodo raíz</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nodo radice</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents the root node of a tree.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수형도의 뿌리 노드를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">樹狀結構的根節點。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">木の根要素を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente le nœud racine d'un arbre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa el nodo raíz de un árbol.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta il nodo radice di un albero.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    
      <elementRef key="label" minOccurs="0"/>
    
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2013-12-06" xml:lang="en">identifies the root node of the network by pointing to a feature structure or
other analytic element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">뿌리의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個根節點值，該跟節點為一個功能結構或其他分析元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該根要素の値絵お示す。これは、素性構造または他の分析要素となる。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par la racine ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el valor de la raíz, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna alla radice un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="children" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">identifies the elements which are the children of the root node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">뿌리 노드의 자식인 요소의 확인소 목록을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供根節點的子節點元素識別符碼列表。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該根要素の子要素となる要素の識別子のリストを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit la liste des identifiants des éléments qui sont les enfants du nœud racine.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona una lista de identificadores de elementos que son hijos (descendientes) de la raíz.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce una lista di identificatori degli elementi figli del nodo radice.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="root-attr.children-remarks" versionDate="2013-12-06" xml:lang="en">
        <p>If the root has no children (i.e., the tree is
<soCalled>trivial</soCalled>), then the <att>children</att>
attribute should be omitted.  </p>
      </remarks>
      <remarks ident="root-attr.children-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si le nœud racine n'a pas d'enfants (c'est-à-dire que l'arbre est <soCalled>trivial</soCalled>), l'attribut <att>children</att> devrait être omis. </p>
      </remarks>
      <remarks ident="root-attr.children-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該根要素が子要素を持たない場合、属性<att>children</att>は必
        ず省略される。技術的な理由から、<tag>root children=''</tag>の
        様には定義できない。
        </p>
      </remarks>
    </attDef>
    <attDef ident="ord" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">ordered</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">순서가 있는</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">ordenado</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">ordonné</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">ordinato</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the root is ordered.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">뿌리가 순서가 있는지의 여부를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明根節點是否整齊排列。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該根要素が、順序付きかどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si la racine est ordonnée ou non.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si la raíz es o no ordenada.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se la radice è ordinata.</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <remarks ident="root-attr.ord-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the children of
          the root are ordered, whereas <val>false</val> indicates the
          are unordered.</p>
        <p>Use if and only if <att>ord</att> is specified as
	  <val>partial</val> on the <gi>tree</gi> element and the root
	  has more than one child.</p>
      </remarks>
      <remarks ident="root-attr.ord-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>La valeur <val>true</val> indique que les enfants d'un nœud racine sont ordonnés, alors que la valeur <val>false</val> indique qu'ils ne le sont pas.</p>
        <p>Utiliser si, et seulement si, l'attribut <att>ord</att> de l'élément <gi>tree</gi> a la valeur <val>partial</val> et que la racine a plus d'un enfant.</p>
      </remarks>
      <remarks ident="root-attr.ord-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性値<val>true</val>は、当該根要素の子要素が順序付きであるこ
        とを示し、属性値<val>false</val>は、順序付きでないことを示す。
        </p>
        <p>
        要素<gi>tree</gi>の属性<att>ord</att>の値が<val>partial</val>
        で、当該根要素が複数の子要素を持つ場合にのみ、使用される。
        </p>
      </remarks>
    </attDef>
    <attDef ident="outDegree" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the out degree of the root, the number of its children.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">뿌리의 정도, 즉, 그 자식의 수를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">根節點的向外分支度，即為其子節點的數量。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該根要素の出の次数、すなわち子要素の数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le degré sortant de la racine, c'est-à-dire le nombre de ses enfants.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el grado en salida de la raíz, es decir, el número de hijos de esta.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il grado in uscita della radice, cioè il numero dei suoi figli.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="root-attr.outDegree-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The in degree of the root is always 0.</p>
      </remarks>
      <remarks ident="root-attr.outDegree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Le degré entrant du nœud racine est toujours 0.</p>
      </remarks>
      <remarks ident="root-attr.outDegree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該根要素の入りの次数は、常に0。
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-root-egXML-lm">
      <root xml:id="vp1" children="#vb1 #pn1" outDegree="2">
        <label>VP</label>
      </root>
      <leaf xml:id="vb1"/>
      <leaf xml:id="pn1"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-root-egXML-pi">
      <root xml:id="fr_vp1" children="#fr_vb1 #fr_pn1" outDegree="2">
        <label>VP</label>
      </root>
      <leaf xml:id="fr_vb1"/>
      <leaf xml:id="fr_pn1"/>
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
<gloss versionDate="2005-01-14" xml:lang="en">root node</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">뿌리 노드</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">根節點</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">nœud racine</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nodo raíz</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nodo radice</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents the root node of a tree.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수형도의 뿌리 노드를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">樹狀結構的根節點。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">木の根要素を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente le nœud racine d'un arbre.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa el nodo raíz de un árbol.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta il nodo radice di un albero.</desc>
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
<desc versionDate="2013-12-06" xml:lang="en">identifies the root node of the network by pointing to a feature structure or
other analytic element.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">뿌리의 값을 제시하며, 그 값은 자질 구조 또는 기타 분석적 요소이다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個根節點值，該跟節點為一個功能結構或其他分析元素。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該根要素の値絵お示す。これは、素性構造または他の分析要素となる。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par la racine ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el valor de la raíz, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna alla radice un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
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
<desc versionDate="2005-01-14" xml:lang="en">identifies the elements which are the children of the root node.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">뿌리 노드의 자식인 요소의 확인소 목록을 제시한다.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供根節點的子節點元素識別符碼列表。</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該根要素の子要素となる要素の識別子のリストを示す。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit la liste des identifiants des éléments qui sont les enfants du nœud racine.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una lista de identificadores de elementos que son hijos (descendientes) de la raíz.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce una lista di identificatori degli elementi figli del nodo radice.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="root-attr.children-remarks" versionDate="2013-12-06" xml:lang="en">
        <p>If the root has no children (i.e., the tree is
<soCalled>trivial</soCalled>), then the <att>children</att>
attribute should be omitted.  </p>
      </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="root-attr.children-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si le nœud racine n'a pas d'enfants (c'est-à-dire que l'arbre est <soCalled>trivial</soCalled>), l'attribut <att>children</att> devrait être omis. </p>
      </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="root-attr.children-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該根要素が子要素を持たない場合、属性<att>children</att>は必
        ず省略される。技術的な理由から、<tag>root children=''</tag>の
        様には定義できない。
        </p>
      </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">ordered</gloss>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">순서가 있는</gloss>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">ordenado</gloss>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">ordonné</gloss>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">ordinato</gloss>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the root is ordered.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">뿌리가 순서가 있는지의 여부를 제시한다.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明根節點是否整齊排列。</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該根要素が、順序付きかどうかを示す。</desc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si la racine est ordonnée ou non.</desc>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si la raíz es o no ordenada.</desc>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se la radice è ordinata.</desc>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="root-attr.ord-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the children of
          the root are ordered, whereas <val>false</val> indicates the
          are unordered.</p>
        <p>Use if and only if <att>ord</att> is specified as
	  <val>partial</val> on the <gi>tree</gi> element and the root
	  has more than one child.</p>
      </remarks>
```

^b48

### Block 49

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="root-attr.ord-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>La valeur <val>true</val> indique que les enfants d'un nœud racine sont ordonnés, alors que la valeur <val>false</val> indique qu'ils ne le sont pas.</p>
        <p>Utiliser si, et seulement si, l'attribut <att>ord</att> de l'élément <gi>tree</gi> a la valeur <val>partial</val> et que la racine a plus d'un enfant.</p>
      </remarks>
```

^b49

### Block 50

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="root-attr.ord-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性値<val>true</val>は、当該根要素の子要素が順序付きであるこ
        とを示し、属性値<val>false</val>は、順序付きでないことを示す。
        </p>
        <p>
        要素<gi>tree</gi>の属性<att>ord</att>の値が<val>partial</val>
        で、当該根要素が複数の子要素を持つ場合にのみ、使用される。
        </p>
      </remarks>
```

^b50

### Block 51

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the out degree of the root, the number of its children.</desc>
```

^b51

### Block 52

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">뿌리의 정도, 즉, 그 자식의 수를 제시한다.</desc>
```

^b52

### Block 53

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">根節點的向外分支度，即為其子節點的數量。</desc>
```

^b53

### Block 54

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該根要素の出の次数、すなわち子要素の数を示す。</desc>
```

^b54

### Block 55

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne le degré sortant de la racine, c'est-à-dire le nombre de ses enfants.</desc>
```

^b55

### Block 56

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el grado en salida de la raíz, es decir, el número de hijos de esta.</desc>
```

^b56

### Block 57

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il grado in uscita della radice, cioè il numero dei suoi figli.</desc>
```

^b57

### Block 58

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b58

### Block 59

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="root-attr.outDegree-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The in degree of the root is always 0.</p>
      </remarks>
```

^b59

### Block 60

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[2]`.

```xml
<remarks ident="root-attr.outDegree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Le degré entrant du nœud racine est toujours 0.</p>
      </remarks>
```

^b60

### Block 61

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[3]`.

```xml
<remarks ident="root-attr.outDegree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該根要素の入りの次数は、常に0。
        </p>
      </remarks>
```

^b61

### Block 62

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-root-egXML-lm">
      <root xml:id="vp1" children="#vb1 #pn1" outDegree="2">
        <label>VP</label>
      </root>
      <leaf xml:id="vb1"/>
      <leaf xml:id="pn1"/>
    </egXML>
  </exemplum>
```

^b62

### Block 63

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-root-egXML-pi">
      <root xml:id="fr_vp1" children="#fr_vb1 #fr_pn1" outDegree="2">
        <label>VP</label>
      </root>
      <leaf xml:id="fr_vb1"/>
      <leaf xml:id="fr_pn1"/>
    </egXML>
  </exemplum>
```

^b63

### Block 64

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDTR" type="div2"/>
  </listRef>
```

^b64

