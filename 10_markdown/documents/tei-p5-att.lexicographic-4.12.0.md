---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.lexicographic-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.lexicographic
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.lexicographic.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.lexicographic

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9961. Git blob: `410bd45b323a695a110c8392289aa5cbeb2e9b29`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="DIGLOBAL" type="atts" ident="att.lexicographic">
  <desc versionDate="2018-09-08" xml:lang="en">provides a set of attributes for specifying standard and normalized values, grammatical functions, alternate or equivalent forms, and information about composite parts.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전용 기본 태그 세트의 요소에서 이용 가능한 전반적 속성들의 집합을 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一組全域屬性值，可用於字典的基礎標籤組之元素上。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書向けのタグ集合にある要素に付与可能な、グローバル属性を定義する。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">définit un ensemble d'attributs globaux disponibles pour les éléments appartenant à l'ensemble des balises de base dédié aux dictionnaires.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define el conjunto de  atributos globales posibles para los elementos del conjunto de etiquetas base para diccionarios</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi globali disponibili per gli elementi dell'insieme base di marcatori per i dizionari.</desc>
  <classes>
    
    <memberOf key="att.datcat"/>
    <memberOf key="att.lexicographic.normalized"/>
  </classes>
  <attList>
    <attDef ident="expand" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">expand</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">développé</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">gives an expanded form of information presented more concisely in the dictionary.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사전에서 더 간결하게 제시된 정보의 확장형을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一形式擴充的資訊，其以較簡潔的方式呈現於字典中</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">辞書中では簡易表記されているものの完全記述を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne une forme développée de l'information présentée de manière plus concise dans le dictionnaire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona de manera expandida la información presentada brevemente en el diccionario</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce la forma estesa dellel informazioni presentate in modo più coinciso nel dizionario.</desc>
    <datatype>  <!--      <textNode/> see stylesheets issue #236 --> 
      <dataRef key="teidata.text"/>
     </datatype> 
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIGLOBAL-egXML-ez" source="#NONE">
          <gramGrp>
            <pos expand="noun">n</pos>
          </gramGrp>
        </egXML>
      </exemplum>
      <exemplum versionDate="2016-05-24" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIGLOBAL-egXML-ey" source="#NONE">
          <gramGrp>
            <pos expand="nom">n.</pos>
          </gramGrp>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="split" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">split</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">graphies distinctes</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">gives the list of split values for a merged form.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">통합형에 대한 분리 값의 목록을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一合併形式的split值列表</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">構成部分をリストで示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">donne la liste des valeurs distinctes d'une forme fusionnée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona una lista de valores de abertura para una forma fusionada</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce la lista dei valori suddivisi di una forma unita.</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
    </attDef>
    <attDef ident="value" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">value</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">valeur</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">gives a value which lacks any realization in the printed source text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">인쇄된 원본 텍스트에서 누락된 값을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個尚未在書面來源文件中呈現的屬性值</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">印刷されているテキスト上では欠如している情報を示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">indique une valeur qui manque à un quelconque fragment du texte source imprimé.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un valor que carece de cualquier realización en el texto fuente impreso</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un valore privo di qualsiasi realizzazione nel testo di origine a mezzo stampa.</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
    </attDef>
    <attDef ident="location" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">location</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">localisation</gloss>
      <desc versionDate="2013-12-08" xml:lang="en">indicates an <gi>anchor</gi> element typically elsewhere in the document, but possibly in another document, 
                which is the original location of this component.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">문서의 다른 위치에서 이 성분의 원본 위치를 지시하는 <gi>anchor</gi> 요소에 대한 참조를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">參照到文件中的元素<gi>anchor</gi>，指出此元件的原文位置。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素の元の場所を特定する要素<gi>anchor</gi>への参照を示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">fournit une référence à un élément <gi>anchor</gi> se trouvant ailleurs dans le document TEI, pour indiquer la localisation de ce composant.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona una referencia a un elemento <gi>anchor</gi> que aparece en algún punto del documento indicando la localización original de ese componente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un riferimento per un elemento <gi>anchor</gi> in una altra porzione del documento indicando la localizzazione origiraria del componente.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="mergedIn" usage="opt">
      <gloss versionDate="2020-12-20" xml:lang="en">merged into</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">fusionné</gloss>
      <desc versionDate="2007-07-04" xml:lang="en">gives a reference to another element, where the original appears as a merged form.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">다른 요소에 대한 참조를 제시하며, 여기서 원본은 통합형이다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona una referencia a otro elemento, donde el original aparece como una forma combinada.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">元データが統合されて出現している、ある要素への参照を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">donne une référence à un autre élément, où
l'original apparaît comme une forme fusionnée.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">fa riferimento a un altro elemento, laddove quello originale si presenti come forma risultanteda una fusione.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="opt" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">optional</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">수의적</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">facultativo</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">facultatif</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">facoltativo</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">indicates whether the element is optional or not.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">요소가 수의적인지 아닌지를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素是否必備</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素が選択的かどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si l'élément est facultatif ou pas.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el elemento es opcional o no.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se l'elemento è opzionale o meno.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
      <defaultVal>false</defaultVal>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#DIEN" type="div3"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-09-08" xml:lang="en">provides a set of attributes for specifying standard and normalized values, grammatical functions, alternate or equivalent forms, and information about composite parts.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전용 기본 태그 세트의 요소에서 이용 가능한 전반적 속성들의 집합을 정의한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一組全域屬性值，可用於字典的基礎標籤組之元素上。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書向けのタグ集合にある要素に付与可能な、グローバル属性を定義する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">définit un ensemble d'attributs globaux disponibles pour les éléments appartenant à l'ensemble des balises de base dédié aux dictionnaires.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define el conjunto de  atributos globales posibles para los elementos del conjunto de etiquetas base para diccionarios</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi globali disponibili per gli elementi dell'insieme base di marcatori per i dizionari.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="att.datcat"/>
    <memberOf key="att.lexicographic.normalized"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="en">expand</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">développé</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">gives an expanded form of information presented more concisely in the dictionary.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전에서 더 간결하게 제시된 정보의 확장형을 제시한다.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一形式擴充的資訊，其以較簡潔的方式呈現於字典中</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書中では簡易表記されているものの完全記述を示す。</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne une forme développée de l'information présentée de manière plus concise dans le dictionnaire.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona de manera expandida la información presentada brevemente en el diccionario</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce la forma estesa dellel informazioni presentate in modo più coinciso nel dizionario.</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>  <!--      <textNode/> see stylesheets issue #236 --> 
      <dataRef key="teidata.text"/>
     </datatype>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIGLOBAL-egXML-ez" source="#NONE">
          <gramGrp>
            <pos expand="noun">n</pos>
          </gramGrp>
        </egXML>
      </exemplum>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum versionDate="2016-05-24" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIGLOBAL-egXML-ey" source="#NONE">
          <gramGrp>
            <pos expand="nom">n.</pos>
          </gramGrp>
        </egXML>
      </exemplum>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="en">split</gloss>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">graphies distinctes</gloss>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">gives the list of split values for a merged form.</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">통합형에 대한 분리 값의 목록을 제시한다.</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一合併形式的split值列表</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">構成部分をリストで示す。</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">donne la liste des valeurs distinctes d'une forme fusionnée.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una lista de valores de abertura para una forma fusionada</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce la lista dei valori suddivisi di una forma unita.</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="en">value</gloss>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">valeur</gloss>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">gives a value which lacks any realization in the printed source text.</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인쇄된 원본 텍스트에서 누락된 값을 제시한다.</desc>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個尚未在書面來源文件中呈現的屬性值</desc>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">印刷されているテキスト上では欠如している情報を示す。</desc>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">indique une valeur qui manque à un quelconque fragment du texte source imprimé.</desc>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un valor que carece de cualquier realización en el texto fuente impreso</desc>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un valore privo di qualsiasi realizzazione nel testo di origine a mezzo stampa.</desc>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[4]/gloss[1]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="en">location</gloss>
```

^b41

### Block 42

XML location: `/classSpec[1]/attList[1]/attDef[4]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">localisation</gloss>
```

^b42

### Block 43

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2013-12-08" xml:lang="en">indicates an <gi>anchor</gi> element typically elsewhere in the document, but possibly in another document, 
                which is the original location of this component.</desc>
```

^b43

### Block 44

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문서의 다른 위치에서 이 성분의 원본 위치를 지시하는 <gi>anchor</gi> 요소에 대한 참조를 제공한다.</desc>
```

^b44

### Block 45

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">參照到文件中的元素<gi>anchor</gi>，指出此元件的原文位置。</desc>
```

^b45

### Block 46

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素の元の場所を特定する要素<gi>anchor</gi>への参照を示す。</desc>
```

^b46

### Block 47

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">fournit une référence à un élément <gi>anchor</gi> se trouvant ailleurs dans le document TEI, pour indiquer la localisation de ce composant.</desc>
```

^b47

### Block 48

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una referencia a un elemento <gi>anchor</gi> que aparece en algún punto del documento indicando la localización original de ese componente.</desc>
```

^b48

### Block 49

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un riferimento per un elemento <gi>anchor</gi> in una altra porzione del documento indicando la localizzazione origiraria del componente.</desc>
```

^b49

### Block 50

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b50

### Block 51

XML location: `/classSpec[1]/attList[1]/attDef[5]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">merged into</gloss>
```

^b51

### Block 52

XML location: `/classSpec[1]/attList[1]/attDef[5]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">fusionné</gloss>
```

^b52

### Block 53

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2007-07-04" xml:lang="en">gives a reference to another element, where the original appears as a merged form.</desc>
```

^b53

### Block 54

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다른 요소에 대한 참조를 제시하며, 여기서 원본은 통합형이다.</desc>
```

^b54

### Block 55

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona una referencia a otro elemento, donde el original aparece como una forma combinada.</desc>
```

^b55

### Block 56

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元データが統合されて出現している、ある要素への参照を示す。</desc>
```

^b56

### Block 57

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">donne une référence à un autre élément, où
l'original apparaît comme une forme fusionnée.</desc>
```

^b57

### Block 58

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">fa riferimento a un altro elemento, laddove quello originale si presenti come forma risultanteda una fusione.</desc>
```

^b58

### Block 59

XML location: `/classSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b59

### Block 60

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">optional</gloss>
```

^b60

### Block 61

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">수의적</gloss>
```

^b61

### Block 62

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">facultativo</gloss>
```

^b62

### Block 63

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[4]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">facultatif</gloss>
```

^b63

### Block 64

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">facoltativo</gloss>
```

^b64

### Block 65

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates whether the element is optional or not.</desc>
```

^b65

### Block 66

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소가 수의적인지 아닌지를 나타낸다.</desc>
```

^b66

### Block 67

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素是否必備</desc>
```

^b67

### Block 68

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素が選択的かどうかを示す。</desc>
```

^b68

### Block 69

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si l'élément est facultatif ou pas.</desc>
```

^b69

### Block 70

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el elemento es opcional o no.</desc>
```

^b70

### Block 71

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se l'elemento è opzionale o meno.</desc>
```

^b71

### Block 72

XML location: `/classSpec[1]/attList[1]/attDef[6]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b72

### Block 73

XML location: `/classSpec[1]/attList[1]/attDef[6]/defaultVal[1]`.

```xml
<defaultVal>false</defaultVal>
```

^b73

### Block 74

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIEN" type="div3"/>
  </listRef>
```

^b74

