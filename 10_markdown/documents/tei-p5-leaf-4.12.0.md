---
type: representation
source-type: document
source: '[[00_sources/tei-p5-leaf-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 leaf
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/leaf.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# leaf

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6377. Git blob: `ba05f904c855e1f60aabefa7807f6645106dbefc`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-leaf" ident="leaf">
  <gloss versionDate="2007-06-12" xml:lang="en">leaf</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">feuille</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">encodes the leaves (terminal nodes) of a tree.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수형도의 단말 노드를 부호화한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記樹狀結構的葉節點 (終端節點) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">木(構造)における葉(終端ノード)を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">encode les feuilles (nœuds terminaux) d'un
			arbre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">codifica las hojas (nodos terminales) de un árbol.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">codifica le foglie (nodi terminali) di un albero.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    
      <elementRef key="label" minOccurs="0"/>
    
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2007-04-22" xml:lang="en">provides a pointer to a feature
structure or other analytic element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">자질 구조 또는 기타 분석적 요소에 대한 포인터를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個連結到功能結構或其他分析元素的指標。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">素性構造または他の分析要素へのポインタを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par la feuille ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador de una estructura de rasgos u otro elemento de análisis.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna alla foglia un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="parent" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">provides the identifier of parent of a leaf.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">단말 노드의 부모의 확인소를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供葉節點的父節點識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">葉の親要素の識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant du parent de la feuille.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador que es padre de una hoja.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore al genitore della foglia.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="follow" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">provides an identifier of an element which this leaf follows.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 단말 노드가 따르는 요소의 확인소를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供此葉節點所尾隨的元素識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該葉の姉要素の識別子を示す。</desc>
      <desc versionDate="2009-11-17" xml:lang="fr">fournit l'identifiant d'un élément que cette feuille suit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador al elemento que precede a la hoja.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento che precede la foglia.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="leaf-attr.follow-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If the tree is unordered or partially ordered, this
attribute has the property of fixing the relative order of the leaf and
the element which is the value of the attribute.</p>
      </remarks>
      <remarks ident="leaf-attr.follow-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Si l'arbre n'est pas ordonné ou l'est partiellement, cet attribut a la propriété de fixer l'ordre relatif de la feuille et de l'élément désigné par l'attribut.</p>
      </remarks>
      <remarks ident="leaf-attr.follow-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該木が順序付きでない、または部分的順序付きである場合、当該属
      性は、当該葉または属性値が示す要素の相対的順序を示す。
      </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-leaf-egXML-qq">
      <leaf xml:id="peri1" parent="#n1">
        <label>periscope</label>
      </leaf>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-leaf-egXML-ap">
      <leaf xml:id="fr_peri1" parent="#fr_n1">
        <label>périscope</label>
      </leaf>
    </egXML>
  </exemplum>
  <remarks ident="leaf-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The in degree of a leaf is always 1, its out degree always
0.</p>
  </remarks>
  <remarks ident="leaf-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le degré entrant d'une feuille est toujours 1, son degré sortant toujours 0.</p>
  </remarks>
  <remarks ident="leaf-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    葉の入り次数は常に1であり、出の次数は常に0となる。
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
<gloss versionDate="2007-06-12" xml:lang="en">leaf</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">feuille</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">encodes the leaves (terminal nodes) of a tree.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수형도의 단말 노드를 부호화한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記樹狀結構的葉節點 (終端節點) 。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">木(構造)における葉(終端ノード)を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">encode les feuilles (nœuds terminaux) d'un
			arbre.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">codifica las hojas (nodos terminales) de un árbol.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codifica le foglie (nodi terminali) di un albero.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <elementRef key="label" minOccurs="0"/>
    
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-04-22" xml:lang="en">provides a pointer to a feature
structure or other analytic element.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 구조 또는 기타 분석적 요소에 대한 포인터를 제공한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個連結到功能結構或其他分析元素的指標。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性構造または他の分析要素へのポインタを示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par la feuille ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador de una estructura de rasgos u otro elemento de análisis.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna alla foglia un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides the identifier of parent of a leaf.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">단말 노드의 부모의 확인소를 제공한다.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供葉節點的父節點識別符碼。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">葉の親要素の識別子を示す。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant du parent de la feuille.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador que es padre de una hoja.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore al genitore della foglia.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides an identifier of an element which this leaf follows.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 단말 노드가 따르는 요소의 확인소를 제공한다.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供此葉節點所尾隨的元素識別符碼。</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該葉の姉要素の識別子を示す。</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2009-11-17" xml:lang="fr">fournit l'identifiant d'un élément que cette feuille suit.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador al elemento que precede a la hoja.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento che precede la foglia.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="leaf-attr.follow-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If the tree is unordered or partially ordered, this
attribute has the property of fixing the relative order of the leaf and
the element which is the value of the attribute.</p>
      </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="leaf-attr.follow-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Si l'arbre n'est pas ordonné ou l'est partiellement, cet attribut a la propriété de fixer l'ordre relatif de la feuille et de l'élément désigné par l'attribut.</p>
      </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="leaf-attr.follow-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該木が順序付きでない、または部分的順序付きである場合、当該属
      性は、当該葉または属性値が示す要素の相対的順序を示す。
      </p>
      </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-leaf-egXML-qq">
      <leaf xml:id="peri1" parent="#n1">
        <label>periscope</label>
      </leaf>
    </egXML>
  </exemplum>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-leaf-egXML-ap">
      <leaf xml:id="fr_peri1" parent="#fr_n1">
        <label>périscope</label>
      </leaf>
    </egXML>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="leaf-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The in degree of a leaf is always 1, its out degree always
0.</p>
  </remarks>
```

^b41

### Block 42

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="leaf-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le degré entrant d'une feuille est toujours 1, son degré sortant toujours 0.</p>
  </remarks>
```

^b42

### Block 43

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="leaf-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    葉の入り次数は常に1であり、出の次数は常に0となる。
    </p>
  </remarks>
```

^b43

### Block 44

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDTR" type="div2"/>
  </listRef>
```

^b44

