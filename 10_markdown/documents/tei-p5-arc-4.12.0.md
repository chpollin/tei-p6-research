---
type: representation
source-type: document
source: '[[00_sources/tei-p5-arc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 arc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/arc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# arc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6889. Git blob: `b73ad1b99c1f7eb89dedbf4c439cd9901ae4d176`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-arc" ident="arc">
  <gloss versionDate="2007-06-12" xml:lang="en">arc</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">arc</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">encodes an arc, the connection from one node to another in a graph.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">그래프에서 노드 사이를 연결하는 호를 부호화한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記一條弧線，即為圖形中節點與節點之間的連線。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">グラフを構成するノード間の辺を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">encode un arc, la connexion entre deux noeuds dans un graphe.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">codifica un arco, es decir, la conexión entre un nodo y otro al interno de un gráfico</desc>
  <desc versionDate="2007-01-21" xml:lang="it">codifica un arco, cioè il collegamento tra un nodo e l'altro all'interno di un grafo.</desc>
  <classes>
    <memberOf key="att.global"/>
  </classes>
  <content>
    <elementRef key="label" minOccurs="0" maxOccurs="2"/>
  </content>
  <attList>
    <attDef ident="from" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">gives the identifier of the node which is adjacent from this arc.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 호로부터 인접한 노드의 확인소를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰自該線邊的節點的識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該辺が有向である場合、起点となるノードを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant du noeud qui précède
                                        immédiatement cet arc.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador al nodo adyacente al nodo corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore al nodo non adiacente all'arco.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="to" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">gives the identifier of the node which is adjacent to this arc.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 호에 인접한 노드의 확인소를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰至該線邊的節點的識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該辺が有効である場合、終点となるノードを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant du nœud qui suit
                                        immédiatement cet arc.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador al nodo adyacente al nodo corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore al nodo adiacente all'arco.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-arc-egXML-bc" source="#NONE">
      <arc from="#T3" to="#T3">
        <label>OLD</label>
        <label>VIEUX</label>
      </arc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr" source="#NONE">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-arc-egXML-sf">
      <arc from="#fr_T3" to="#T3">
        <label>OLD</label>
        <label>VIEUX</label>
      </arc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-arc-egXML-an" source="#NONE">
      <arc from="#zh-tw_T3" to="#zh-tw_T3">
        <label>OLD</label>
        <label>年老</label>
      </arc>
    </egXML>
  </exemplum>
  <remarks ident="arc-remarks" versionDate="2007-03-02" xml:lang="en">
    <p>The <gi>arc</gi> element must be used if the arcs are labeled.
    Otherwise, arcs can be encoded using the <att>adj</att>,
    <att>adjTo</att> and <att>adjFrom</att> attributes on the
    <gi>node</gi> tags in the graph. Both <gi>arc</gi> tags and
    adjacency attributes can be used, but the resulting encoding would
    be highly redundant.</p>
    <p>Zero, one, or two children <gi>label</gi> elements may be
    present. The first occurrence of <gi>label</gi> provides a label
    for the arc; the second provides a second label for the arc, and
    should be used if a transducer is being encoded.</p>
  </remarks>
  <remarks ident="arc-remarks" versionDate="2009-11-17" xml:lang="fr">
    <p>L'élément <gi>arc</gi> doit être utilisé si les arcs sont étiquetés. Sinon les arcs
                peuvent être encodés en utilisant les attributs <att>adj</att>, <att>adjTo</att> et
                    <att>adjFrom</att> des éléments <gi>node</gi> du graphe. Les éléments
                <gi>arc</gi> et les attributs d'adjacence peuvent être utilisés en même temps mais
                l'encodage qui en résulte serait extrêmement redondant.</p>
    <p>Peuvent être présents un ou deux éléments enfants <gi>label</gi> ou aucun. La première
                occurrence de l'élément <gi>label</gi> fournit une étiquette pour l'arc ; la seconde
                occurrence fournit une deuxième étiquette pour l'arc et doit être utilisée si l'on
                encode un transducteur.</p>
  </remarks>
  <remarks ident="arc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>arc</gi>は、ラベル付き辺の場合には必ず使用される。
      そうでない場合、辺は、要素<gi>node</gi>の属性<att>adj</att>、<att>adjTo</att>、<att>adjFrom</att>として示すことも可能である。
    しかし、この方法は記述が冗長になるかもしれない。
    </p>
    <p>
    要素<gi>label</gi>の数は、0、1、2の場合がある。最初に出現する要素
    <gi>label</gi>には、当該辺のラベルが付与される。2番目に来る要素
    <gi>label</gi>には、当該辺の2番目のラベルが付与される。変換グラフ
    をマークアップする場合には、2番目のラベルが使用されるべきである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#GDGR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">arc</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">arc</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">encodes an arc, the connection from one node to another in a graph.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그래프에서 노드 사이를 연결하는 호를 부호화한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記一條弧線，即為圖形中節點與節點之間的連線。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">グラフを構成するノード間の辺を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">encode un arc, la connexion entre deux noeuds dans un graphe.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">codifica un arco, es decir, la conexión entre un nodo y otro al interno de un gráfico</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codifica un arco, cioè il collegamento tra un nodo e l'altro all'interno di un grafo.</desc>
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
    <elementRef key="label" minOccurs="0" maxOccurs="2"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the identifier of the node which is adjacent from this arc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 호로부터 인접한 노드의 확인소를 제시한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰自該線邊的節點的識別符碼。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該辺が有向である場合、起点となるノードを示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant du noeud qui précède
                                        immédiatement cet arc.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador al nodo adyacente al nodo corriente.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore al nodo non adiacente all'arco.</desc>
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
<desc versionDate="2005-01-14" xml:lang="en">gives the identifier of the node which is adjacent to this arc.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 호에 인접한 노드의 확인소를 제시한다.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰至該線邊的節點的識別符碼。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該辺が有効である場合、終点となるノードを示す。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant du nœud qui suit
                                        immédiatement cet arc.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador al nodo adyacente al nodo corriente.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore al nodo adiacente all'arco.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-arc-egXML-bc" source="#NONE">
      <arc from="#T3" to="#T3">
        <label>OLD</label>
        <label>VIEUX</label>
      </arc>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr" source="#NONE">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-arc-egXML-sf">
      <arc from="#fr_T3" to="#T3">
        <label>OLD</label>
        <label>VIEUX</label>
      </arc>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-arc-egXML-an" source="#NONE">
      <arc from="#zh-tw_T3" to="#zh-tw_T3">
        <label>OLD</label>
        <label>年老</label>
      </arc>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="arc-remarks" versionDate="2007-03-02" xml:lang="en">
    <p>The <gi>arc</gi> element must be used if the arcs are labeled.
    Otherwise, arcs can be encoded using the <att>adj</att>,
    <att>adjTo</att> and <att>adjFrom</att> attributes on the
    <gi>node</gi> tags in the graph. Both <gi>arc</gi> tags and
    adjacency attributes can be used, but the resulting encoding would
    be highly redundant.</p>
    <p>Zero, one, or two children <gi>label</gi> elements may be
    present. The first occurrence of <gi>label</gi> provides a label
    for the arc; the second provides a second label for the arc, and
    should be used if a transducer is being encoded.</p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="arc-remarks" versionDate="2009-11-17" xml:lang="fr">
    <p>L'élément <gi>arc</gi> doit être utilisé si les arcs sont étiquetés. Sinon les arcs
                peuvent être encodés en utilisant les attributs <att>adj</att>, <att>adjTo</att> et
                    <att>adjFrom</att> des éléments <gi>node</gi> du graphe. Les éléments
                <gi>arc</gi> et les attributs d'adjacence peuvent être utilisés en même temps mais
                l'encodage qui en résulte serait extrêmement redondant.</p>
    <p>Peuvent être présents un ou deux éléments enfants <gi>label</gi> ou aucun. La première
                occurrence de l'élément <gi>label</gi> fournit une étiquette pour l'arc ; la seconde
                occurrence fournit une deuxième étiquette pour l'arc et doit être utilisée si l'on
                encode un transducteur.</p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="arc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>arc</gi>は、ラベル付き辺の場合には必ず使用される。
      そうでない場合、辺は、要素<gi>node</gi>の属性<att>adj</att>、<att>adjTo</att>、<att>adjFrom</att>として示すことも可能である。
    しかし、この方法は記述が冗長になるかもしれない。
    </p>
    <p>
    要素<gi>label</gi>の数は、0、1、2の場合がある。最初に出現する要素
    <gi>label</gi>には、当該辺のラベルが付与される。2番目に来る要素
    <gi>label</gi>には、当該辺の2番目のラベルが付与される。変換グラフ
    をマークアップする場合には、2番目のラベルが使用されるべきである。
    </p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDGR"/>
  </listRef>
```

^b34

