---
type: representation
source-type: document
source: '[[00_sources/tei-p5-node-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 node
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/node.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# node

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 20625. Git blob: `aaa3c3a9d21452dd8a2d4764d5491d41625593d2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-node" ident="node">
  <gloss versionDate="2007-06-12" xml:lang="en">node</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">nœud</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">encodes a node, a possibly labeled point in a graph.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">그래프에서 (표지가 붙는 지점일 수도 있는) 노드를 부호화한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記一個節點，一個圖形中可能帶有標籤的點。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">グラフのラベル付きノードを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">encode un nœud, c'est-à-dire un sommet, étiqueté ou non, dans un graphe.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">codifica un nodo, un punto en un gráfico al que se le puede proporiconar una etiqueta.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">codifica un nodo, un punto in un grafo a cui può essere assegnata un'etichetta.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <elementRef key="label" minOccurs="0" maxOccurs="2"/>
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">provides the value of a node, which is a feature structure or
other analytic element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">노드의 값을 제공하며, 이 값은 자질 구조 또는 다른 분석적 요소이다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個節點值，該節點為一個功能結構或其他分析元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">ノードの値を示す。これは、素性構造または他の分析要素である。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par le nœud ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el valor de un nodo, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna al nodo un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">provides a type for a node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">노드의 유형을 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供節點類型。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">ノードの種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le type du nœud.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">define un tipo de nodo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">definisce un tipo di nodo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="initial">
          <desc versionDate="2007-06-27" xml:lang="en">initial node in a transition network</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">전이망에서 시작 노드</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">過境網絡中的起始節點</desc>
          <desc versionDate="2008-04-06" xml:lang="es">nodo inicial en una red de transición</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">遷移ネットワークの初期ノード。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nœud initial dans un réseau de
transition.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">nodo iniziale in una rete di transizione.</desc>
        </valItem>
        <valItem ident="final">
          <desc versionDate="2007-06-27" xml:lang="en">final node in a transition network</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">전이망에서 종료 노드</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">過境網絡中的末端節點</desc>
          <desc versionDate="2008-04-06" xml:lang="es">nodo final en una red de transición</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">遷移ネットワークの最終ノード。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nœud terminal dans un réseau de
transition.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">nodo finale in una rete di transizione.</desc>
        </valItem>
      </valList>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-ze">
          <graph>
            <node xml:id="gnex11" adjTo="#gnex12" adj="#gnex13" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex12" adjFrom="#gnex11" adjTo="#gnex13">
              <label>2</label>
            </node>
            <node xml:id="gnex13" adjFrom="#gnex12" adj="#gnex11" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="adjTo" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">adjacent to</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">로 인접한</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">adyacente a</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">adjacent à</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">adiacente a</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">gives the identifiers of the nodes which are adjacent to the current node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 노드에 인접한 노드의 확인소를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰至當前節點的節點的識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">有向グラフにおける、現行ノードに入るノードの識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne les identifiants des nœuds qui précèdent immédiatement le nœud décrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona los identificadores a los nodos adyacentes al nodo corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna degli identificatori ai nodi adiacenti al nodo corrente.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-gm">
          <graph>
            <node xml:id="gnex21" adjTo="#gnex22" adj="#gnex23" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex22" adjTo="#gnex23">
              <label>2</label>
            </node>
            <node xml:id="gnex23" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="adjFrom" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">adjacent from</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">~로부터 인접한</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">adyacente de</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">adjacent de</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">non adiacente</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">gives the identifiers of the nodes which are adjacent from the current
node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 노드로부터 인접한 노드의 확인소를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰自當前節點的節點的識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">有向グラフにおける、現行ノードから出るノードの識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne les identifiants des nœuds qui suivent immédiatement le nœud décrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona los identificadores a los nodos adyacentes al nodo corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna degli identificatori ai nodi non adiacenti al nodo corrente.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-xu">
          <graph>
            <node xml:id="gnex31" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex32" adjFrom="#gnex31">
              <label>2</label>
            </node>
            <node xml:id="gnex33" adjFrom="#gnex32" adj="#gnex31" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="adj" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">adjacent</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">인접한</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">adyacente</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">adiacente</gloss>
      <gloss versionDate="2009-11-17" xml:lang="fr">adjacent</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">gives the identifiers of the nodes which are both adjacent to and
adjacent from the current node.</desc>
      <desc versionDate="2009-11-17" xml:lang="fr">donne les identifiants des nœuds adjacents au nœud courant.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 노드로 인접한 그리고 현 노드로부터 인접한 노드의 확인소를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰至與相鄰自當前節點的節點的識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">無向グラフにおける、現行ノードに隣接するノードの識別子を示す。</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona los identificadores a los nodos adyacentes al nodo corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna degli identificatori ai nodi adiacenti e non adiacenti al nodo corrente.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-gf">
          <graph>
            <node xml:id="gnex41" adj="#gnex42 #gnex43" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex42" adj="#gnex41 #gnex43">
              <label>2</label>
            </node>
            <node xml:id="gnex43" adj="#gnex42 #gnex41" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
      <remarks ident="node-attr.adj-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>Use this attribute instead of the <att>adjTo</att> and
<att>adjFrom</att> attributes when the graph is undirected and vice
versa if the graph is directed.</p>
      </remarks>
      <remarks ident="node-attr.adj-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Utiliser cet attribut à la place des attributs <att>adjTo</att> et <att>adjFrom</att> quand le graphe n'est pas orienté et vice versa si le graphe est orienté.</p>
      </remarks>
      <remarks ident="node-attr.adj-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該グラフが無向グラフの場合は、属性<att>adjTo</att>や
        <att>adjFrom</att>の代わりに当該属性を使う。当該グラフが有向グ
        ラフの場合は、その逆である。
        </p>
      </remarks>
    </attDef>
    <attDef ident="inDegree" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the in degree of the node, the number of nodes which
are adjacent from the given node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">주어진 노드로부터 인접한 노드의 수인, 노드의 정도를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">節點的向內分支度，即為相鄰自該節點的節點數量。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">現行ノードの入りの次数。すなわち、ノードへ入る辺の数。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le degré entrant du nœud, c'est-à-dire le nombre de nœuds qui précèdent immédiatement le nœud décrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el grado de entrada del nodo, es decir, el número de los nodos no adyacentes al nodo dado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il grado in entrata del nodo, cioè il numero dei nodi non adiacenti al nodo stesso.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-pj">
          <graph>
            <node xml:id="gnex51" adjTo="#gnex52" adj="#gnex53" inDegree="1" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex52" adjFrom="#gnex51" adjTo="#gnex53" inDegree="2">
              <label>2</label>
            </node>
            <node xml:id="gnex53" adjFrom="#gnex52" adj="#gnex51" inDegree="2" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="outDegree" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the out degree of the node, the number of nodes which
are adjacent to the given node.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">주어진 노드에 인접한 노드의 수인, 노드의 정도를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">節點的向外分支度，即為相鄰至該節點的節點數量。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">現行ノードの出の次数。すなわち、ノードから出る辺の数。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le degré sortant du nœud,
        c'est-à-dire le nombre de nœuds qui suivent immédiatement le nœud décrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el grado de salida del nodo, es decir, el número de los nodos no adyacentes al nodo dado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il grado in uscita del nodo, cioè il numero dei nodi adiacenti al nodo stesso.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-ts">
          <graph>
            <node xml:id="gnex61" adjTo="#gnex62" adj="#gnex63" outDegree="2" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex62" adjFrom="#gnex61" adjTo="#gnex63" outDegree="1">
              <label>2</label>
            </node>
            <node xml:id="gnex63" adjFrom="#gnex62" adj="#gnex61" outDegree="2" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="degree" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the degree of the node, the number of arcs with which
the node is incident.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">노드와 함께 나타나는 호의 수인, 노드의 정도를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">節點的分支度，即為節點所附著的線條數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該ノードの次数。すなわち、ノードにある辺の数。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le degré du nœud, c'est-à-dire le nombre d'arcs avec lesquels le nœud est lié.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">define el grado del nodo, es decir,  el número de los arcos incidentes al nodo</desc>
      <desc versionDate="2007-01-21" xml:lang="it">definisce il grado del nodo, cioè il numero degli archi incidenti al nodo.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-yx">
          <graph>
            <node xml:id="gnex71" adjTo="#gnex72" adj="#gnex73" outDegree="1" inDegree="0" degree="1" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex72" adjFrom="#gnex71" adjTo="#gnex73" outDegree="1" inDegree="1" degree="0">
              <label>2</label>
            </node>
            <node xml:id="gnex73" adjFrom="#gnex72" adj="#gnex71" outDegree="0" inDegree="1" degree="1" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
      <remarks ident="node-attr.degree-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>Use this attribute instead of the <att>inDegree</att> and
<att>outDegree</att> attributes when the graph is undirected and vice
versa if the graph is directed.</p>
      </remarks>
      <remarks ident="node-attr.degree-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Utiliser cet attribut à la place des attributs <att>inDegree</att> et <att>outDegree</att> quand le graphe n'est pas orienté et vice versa si le graphe est orienté.</p>
      </remarks>
      <remarks ident="node-attr.degree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該属性は、当該グラフが無向グラフの場合に、属性
      <att>inDegree</att>や<att>outDegree</att>の代わりに使用される。
      有向グラフの場合は、その逆である。
      </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-wf">
      <node xml:id="t6" type="final" inDegree="2" outDegree="0">
        <label>6</label>
      </node>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-nd">
      <node xml:id="fr_t6" type="final" inDegree="2" outDegree="0">
        <label>6</label>
      </node>
    </egXML>
  </exemplum>
  <remarks ident="node-remarks" versionDate="2007-03-02" xml:lang="en">
    <p>Zero, one, or two children <gi>label</gi> elements may be
    present. The first occurrence of <gi>label</gi> provides a label
    for the arc; the second provides a second label for the arc, and
    should be used if a transducer is being encoded whose actions are
    associated with nodes rather than with arcs.</p>
  </remarks>
  <remarks ident="node-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Peuvent être présents un ou deux éléments enfants <gi>label</gi> ou aucun. La première occurrence de l'élément <gi>label</gi> fournit une étiquette pour l'arc ; la seconde
occurrence fournit une deuxième étiquette pour l'arc et doit être utilisée si l'on
encode un transducteur dont les actions sont associées avec des nœuds plutôt
qu'avec des arcs.</p>
  </remarks>
  <remarks ident="node-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    ゼロ以上の子要素<gi>label</gi>をとるかもしれない。最初の要素
      <gi>label</gi>は、辺のラベルを示す。2番目の要素<gi>label</gi>は、
      辺の2つめのラベルを示す。トランスデューサの動作が、辺ではなくノー
      ドに関連して定義される場合に、当該要素が使用されるべきである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#GDGR" type="div1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">node</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">nœud</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">encodes a node, a possibly labeled point in a graph.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그래프에서 (표지가 붙는 지점일 수도 있는) 노드를 부호화한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記一個節點，一個圖形中可能帶有標籤的點。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">グラフのラベル付きノードを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">encode un nœud, c'est-à-dire un sommet, étiqueté ou non, dans un graphe.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">codifica un nodo, un punto en un gráfico al que se le puede proporiconar una etiqueta.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codifica un nodo, un punto in un grafo a cui può essere assegnata un'etichetta.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
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
<desc versionDate="2005-01-14" xml:lang="en">provides the value of a node, which is a feature structure or
other analytic element.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">노드의 값을 제공하며, 이 값은 자질 구조 또는 다른 분석적 요소이다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個節點值，該節點為一個功能結構或其他分析元素。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ノードの値を示す。これは、素性構造または他の分析要素である。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant de l'objet représenté par le nœud ; cet objet peut être une paire nom-valeur ou tout autre élément analytique.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el valor de un nodo, que puede ser una estructura de rasgos u otro elemento de análisis.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna al nodo un valore, che può essere una struttura di tratti o altro elemento di analisi.</desc>
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
<desc versionDate="2005-01-14" xml:lang="en">provides a type for a node.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">노드의 유형을 제공한다.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供節點類型。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ノードの種類を示す。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le type du nœud.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define un tipo de nodo.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un tipo di nodo.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="initial">
          <desc versionDate="2007-06-27" xml:lang="en">initial node in a transition network</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">전이망에서 시작 노드</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">過境網絡中的起始節點</desc>
          <desc versionDate="2008-04-06" xml:lang="es">nodo inicial en una red de transición</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">遷移ネットワークの初期ノード。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nœud initial dans un réseau de
transition.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">nodo iniziale in una rete di transizione.</desc>
        </valItem>
        <valItem ident="final">
          <desc versionDate="2007-06-27" xml:lang="en">final node in a transition network</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">전이망에서 종료 노드</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">過境網絡中的末端節點</desc>
          <desc versionDate="2008-04-06" xml:lang="es">nodo final en una red de transición</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">遷移ネットワークの最終ノード。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nœud terminal dans un réseau de
transition.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">nodo finale in una rete di transizione.</desc>
        </valItem>
      </valList>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-ze">
          <graph>
            <node xml:id="gnex11" adjTo="#gnex12" adj="#gnex13" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex12" adjFrom="#gnex11" adjTo="#gnex13">
              <label>2</label>
            </node>
            <node xml:id="gnex13" adjFrom="#gnex12" adj="#gnex11" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">adjacent to</gloss>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">로 인접한</gloss>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">adyacente a</gloss>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">adjacent à</gloss>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">adiacente a</gloss>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the identifiers of the nodes which are adjacent to the current node.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 노드에 인접한 노드의 확인소를 제시한다.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰至當前節點的節點的識別符碼。</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">有向グラフにおける、現行ノードに入るノードの識別子を示す。</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne les identifiants des nœuds qui précèdent immédiatement le nœud décrit.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona los identificadores a los nodos adyacentes al nodo corriente.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli identificatori ai nodi adiacenti al nodo corrente.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[3]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-gm">
          <graph>
            <node xml:id="gnex21" adjTo="#gnex22" adj="#gnex23" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex22" adjTo="#gnex23">
              <label>2</label>
            </node>
            <node xml:id="gnex23" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">adjacent from</gloss>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">~로부터 인접한</gloss>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">adyacente de</gloss>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">adjacent de</gloss>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">non adiacente</gloss>
```

^b48

### Block 49

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the identifiers of the nodes which are adjacent from the current
node.</desc>
```

^b49

### Block 50

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 노드로부터 인접한 노드의 확인소를 제시한다.</desc>
```

^b50

### Block 51

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰自當前節點的節點的識別符碼。</desc>
```

^b51

### Block 52

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">有向グラフにおける、現行ノードから出るノードの識別子を示す。</desc>
```

^b52

### Block 53

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne les identifiants des nœuds qui suivent immédiatement le nœud décrit.</desc>
```

^b53

### Block 54

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona los identificadores a los nodos adyacentes al nodo corriente.</desc>
```

^b54

### Block 55

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli identificatori ai nodi non adiacenti al nodo corrente.</desc>
```

^b55

### Block 56

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b56

### Block 57

XML location: `/elementSpec[1]/attList[1]/attDef[4]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-xu">
          <graph>
            <node xml:id="gnex31" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex32" adjFrom="#gnex31">
              <label>2</label>
            </node>
            <node xml:id="gnex33" adjFrom="#gnex32" adj="#gnex31" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
```

^b57

### Block 58

XML location: `/elementSpec[1]/attList[1]/attDef[5]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">adjacent</gloss>
```

^b58

### Block 59

XML location: `/elementSpec[1]/attList[1]/attDef[5]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">인접한</gloss>
```

^b59

### Block 60

XML location: `/elementSpec[1]/attList[1]/attDef[5]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">adyacente</gloss>
```

^b60

### Block 61

XML location: `/elementSpec[1]/attList[1]/attDef[5]/gloss[4]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">adiacente</gloss>
```

^b61

### Block 62

XML location: `/elementSpec[1]/attList[1]/attDef[5]/gloss[5]`.

```xml
<gloss versionDate="2009-11-17" xml:lang="fr">adjacent</gloss>
```

^b62

### Block 63

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the identifiers of the nodes which are both adjacent to and
adjacent from the current node.</desc>
```

^b63

### Block 64

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2009-11-17" xml:lang="fr">donne les identifiants des nœuds adjacents au nœud courant.</desc>
```

^b64

### Block 65

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 노드로 인접한 그리고 현 노드로부터 인접한 노드의 확인소를 제시한다.</desc>
```

^b65

### Block 66

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">相鄰至與相鄰自當前節點的節點的識別符碼。</desc>
```

^b66

### Block 67

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">無向グラフにおける、現行ノードに隣接するノードの識別子を示す。</desc>
```

^b67

### Block 68

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona los identificadores a los nodos adyacentes al nodo corriente.</desc>
```

^b68

### Block 69

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli identificatori ai nodi adiacenti e non adiacenti al nodo corrente.</desc>
```

^b69

### Block 70

XML location: `/elementSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b70

### Block 71

XML location: `/elementSpec[1]/attList[1]/attDef[5]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-gf">
          <graph>
            <node xml:id="gnex41" adj="#gnex42 #gnex43" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex42" adj="#gnex41 #gnex43">
              <label>2</label>
            </node>
            <node xml:id="gnex43" adj="#gnex42 #gnex41" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
```

^b71

### Block 72

XML location: `/elementSpec[1]/attList[1]/attDef[5]/remarks[1]`.

```xml
<remarks ident="node-attr.adj-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>Use this attribute instead of the <att>adjTo</att> and
<att>adjFrom</att> attributes when the graph is undirected and vice
versa if the graph is directed.</p>
      </remarks>
```

^b72

### Block 73

XML location: `/elementSpec[1]/attList[1]/attDef[5]/remarks[2]`.

```xml
<remarks ident="node-attr.adj-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Utiliser cet attribut à la place des attributs <att>adjTo</att> et <att>adjFrom</att> quand le graphe n'est pas orienté et vice versa si le graphe est orienté.</p>
      </remarks>
```

^b73

### Block 74

XML location: `/elementSpec[1]/attList[1]/attDef[5]/remarks[3]`.

```xml
<remarks ident="node-attr.adj-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該グラフが無向グラフの場合は、属性<att>adjTo</att>や
        <att>adjFrom</att>の代わりに当該属性を使う。当該グラフが有向グ
        ラフの場合は、その逆である。
        </p>
      </remarks>
```

^b74

### Block 75

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the in degree of the node, the number of nodes which
are adjacent from the given node.</desc>
```

^b75

### Block 76

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">주어진 노드로부터 인접한 노드의 수인, 노드의 정도를 제시한다.</desc>
```

^b76

### Block 77

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">節點的向內分支度，即為相鄰自該節點的節點數量。</desc>
```

^b77

### Block 78

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">現行ノードの入りの次数。すなわち、ノードへ入る辺の数。</desc>
```

^b78

### Block 79

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne le degré entrant du nœud, c'est-à-dire le nombre de nœuds qui précèdent immédiatement le nœud décrit.</desc>
```

^b79

### Block 80

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el grado de entrada del nodo, es decir, el número de los nodos no adyacentes al nodo dado.</desc>
```

^b80

### Block 81

XML location: `/elementSpec[1]/attList[1]/attDef[6]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il grado in entrata del nodo, cioè il numero dei nodi non adiacenti al nodo stesso.</desc>
```

^b81

### Block 82

XML location: `/elementSpec[1]/attList[1]/attDef[6]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b82

### Block 83

XML location: `/elementSpec[1]/attList[1]/attDef[6]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-pj">
          <graph>
            <node xml:id="gnex51" adjTo="#gnex52" adj="#gnex53" inDegree="1" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex52" adjFrom="#gnex51" adjTo="#gnex53" inDegree="2">
              <label>2</label>
            </node>
            <node xml:id="gnex53" adjFrom="#gnex52" adj="#gnex51" inDegree="2" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
```

^b83

### Block 84

XML location: `/elementSpec[1]/attList[1]/attDef[7]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the out degree of the node, the number of nodes which
are adjacent to the given node.</desc>
```

^b84

### Block 85

XML location: `/elementSpec[1]/attList[1]/attDef[7]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">주어진 노드에 인접한 노드의 수인, 노드의 정도를 제시한다.</desc>
```

^b85

### Block 86

XML location: `/elementSpec[1]/attList[1]/attDef[7]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">節點的向外分支度，即為相鄰至該節點的節點數量。</desc>
```

^b86

### Block 87

XML location: `/elementSpec[1]/attList[1]/attDef[7]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">現行ノードの出の次数。すなわち、ノードから出る辺の数。</desc>
```

^b87

### Block 88

XML location: `/elementSpec[1]/attList[1]/attDef[7]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne le degré sortant du nœud,
        c'est-à-dire le nombre de nœuds qui suivent immédiatement le nœud décrit.</desc>
```

^b88

### Block 89

XML location: `/elementSpec[1]/attList[1]/attDef[7]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el grado de salida del nodo, es decir, el número de los nodos no adyacentes al nodo dado.</desc>
```

^b89

### Block 90

XML location: `/elementSpec[1]/attList[1]/attDef[7]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il grado in uscita del nodo, cioè il numero dei nodi adiacenti al nodo stesso.</desc>
```

^b90

### Block 91

XML location: `/elementSpec[1]/attList[1]/attDef[7]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b91

### Block 92

XML location: `/elementSpec[1]/attList[1]/attDef[7]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-ts">
          <graph>
            <node xml:id="gnex61" adjTo="#gnex62" adj="#gnex63" outDegree="2" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex62" adjFrom="#gnex61" adjTo="#gnex63" outDegree="1">
              <label>2</label>
            </node>
            <node xml:id="gnex63" adjFrom="#gnex62" adj="#gnex61" outDegree="2" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
```

^b92

### Block 93

XML location: `/elementSpec[1]/attList[1]/attDef[8]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the degree of the node, the number of arcs with which
the node is incident.</desc>
```

^b93

### Block 94

XML location: `/elementSpec[1]/attList[1]/attDef[8]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">노드와 함께 나타나는 호의 수인, 노드의 정도를 제시한다.</desc>
```

^b94

### Block 95

XML location: `/elementSpec[1]/attList[1]/attDef[8]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">節點的分支度，即為節點所附著的線條數。</desc>
```

^b95

### Block 96

XML location: `/elementSpec[1]/attList[1]/attDef[8]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該ノードの次数。すなわち、ノードにある辺の数。</desc>
```

^b96

### Block 97

XML location: `/elementSpec[1]/attList[1]/attDef[8]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne le degré du nœud, c'est-à-dire le nombre d'arcs avec lesquels le nœud est lié.</desc>
```

^b97

### Block 98

XML location: `/elementSpec[1]/attList[1]/attDef[8]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define el grado del nodo, es decir,  el número de los arcos incidentes al nodo</desc>
```

^b98

### Block 99

XML location: `/elementSpec[1]/attList[1]/attDef[8]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce il grado del nodo, cioè il numero degli archi incidenti al nodo.</desc>
```

^b99

### Block 100

XML location: `/elementSpec[1]/attList[1]/attDef[8]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b100

### Block 101

XML location: `/elementSpec[1]/attList[1]/attDef[8]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-yx">
          <graph>
            <node xml:id="gnex71" adjTo="#gnex72" adj="#gnex73" outDegree="1" inDegree="0" degree="1" type="initial">
              <label>1</label>
            </node>
            <node xml:id="gnex72" adjFrom="#gnex71" adjTo="#gnex73" outDegree="1" inDegree="1" degree="0">
              <label>2</label>
            </node>
            <node xml:id="gnex73" adjFrom="#gnex72" adj="#gnex71" outDegree="0" inDegree="1" degree="1" type="final">
              <label>3</label>
            </node>
          </graph>
        </egXML>
      </exemplum>
```

^b101

### Block 102

XML location: `/elementSpec[1]/attList[1]/attDef[8]/remarks[1]`.

```xml
<remarks ident="node-attr.degree-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>Use this attribute instead of the <att>inDegree</att> and
<att>outDegree</att> attributes when the graph is undirected and vice
versa if the graph is directed.</p>
      </remarks>
```

^b102

### Block 103

XML location: `/elementSpec[1]/attList[1]/attDef[8]/remarks[2]`.

```xml
<remarks ident="node-attr.degree-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Utiliser cet attribut à la place des attributs <att>inDegree</att> et <att>outDegree</att> quand le graphe n'est pas orienté et vice versa si le graphe est orienté.</p>
      </remarks>
```

^b103

### Block 104

XML location: `/elementSpec[1]/attList[1]/attDef[8]/remarks[3]`.

```xml
<remarks ident="node-attr.degree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該属性は、当該グラフが無向グラフの場合に、属性
      <att>inDegree</att>や<att>outDegree</att>の代わりに使用される。
      有向グラフの場合は、その逆である。
      </p>
      </remarks>
```

^b104

### Block 105

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-wf">
      <node xml:id="t6" type="final" inDegree="2" outDegree="0">
        <label>6</label>
      </node>
    </egXML>
  </exemplum>
```

^b105

### Block 106

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-node-egXML-nd">
      <node xml:id="fr_t6" type="final" inDegree="2" outDegree="0">
        <label>6</label>
      </node>
    </egXML>
  </exemplum>
```

^b106

### Block 107

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="node-remarks" versionDate="2007-03-02" xml:lang="en">
    <p>Zero, one, or two children <gi>label</gi> elements may be
    present. The first occurrence of <gi>label</gi> provides a label
    for the arc; the second provides a second label for the arc, and
    should be used if a transducer is being encoded whose actions are
    associated with nodes rather than with arcs.</p>
  </remarks>
```

^b107

### Block 108

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="node-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Peuvent être présents un ou deux éléments enfants <gi>label</gi> ou aucun. La première occurrence de l'élément <gi>label</gi> fournit une étiquette pour l'arc ; la seconde
occurrence fournit une deuxième étiquette pour l'arc et doit être utilisée si l'on
encode un transducteur dont les actions sont associées avec des nœuds plutôt
qu'avec des arcs.</p>
  </remarks>
```

^b108

### Block 109

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="node-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    ゼロ以上の子要素<gi>label</gi>をとるかもしれない。最初の要素
      <gi>label</gi>は、辺のラベルを示す。2番目の要素<gi>label</gi>は、
      辺の2つめのラベルを示す。トランスデューサの動作が、辺ではなくノー
      ドに関連して定義される場合に、当該要素が使用されるべきである。
    </p>
  </remarks>
```

^b109

### Block 110

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDGR" type="div1"/>
  </listRef>
```

^b110

