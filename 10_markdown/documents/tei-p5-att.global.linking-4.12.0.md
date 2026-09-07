---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.global.linking-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.global.linking
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.global.linking.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.global.linking

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 19848. Git blob: `91dc83b4b10af17162293452811226a616ba5663`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" predeclare="true" module="linking" xml:id="CLLINK" type="atts" ident="att.global.linking">
  <desc versionDate="2016-02-16" xml:lang="en">provides a set of attributes for hypertextual linking.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하이퍼텍스트와 다른 연결에 대한 속성의 집합을 정의한다. 이것은 연결에 대한 부가적 태그 집합이 선택될 때 모든 요소에 가능해야 한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一組用於超文字連結及其他連結的屬性，當連結的附加標籤組被選擇時，這些屬性可用於所有元素。</desc>
  <desc versionDate="2019-07-21" xml:lang="ja">ハイパーテキストリンクの属性セットを提供する。</desc>
  <desc versionDate="2016-02-16" xml:lang="fr">fournit un ensemble d'attributs pour décrire les liens hypertextuels.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define un conjunto de atributos para hipertexto u otro vínculo habilitado para todos los elementos cuando se selecciona la etiqueta adicional para los enlaces.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi per ipertesto o altro legame abilitati per tutti gli elementi quando è selezionato il sottoinsieme di marcatori per i collegamenti.</desc>
  <desc versionDate="2025-02-06" xml:lang="de">stellt Attribute für hypertextuelle Verlinkungen bereit.</desc>
  <attList>
    <attDef ident="corresp" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">corresponds</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">일치</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">correspondencia</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">correspond</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">corrispondente</gloss>
      <gloss versionDate="2019-07-21" xml:lang="ja">対応</gloss>
      <gloss versionDate="2025-02-06" xml:lang="de">korrespondiert</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">points to elements that correspond to the current element in some way.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">어떤 식으로든 현 요소와 일치하는 요소를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素在某方面符合現有元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素と対応する要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers des éléments qui ont une correspondance avec l'élément en question.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala los elementos que presentan una correspondencia con el elemento corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta a elementi che hanno una qualche corrispondenza con l'elemento corrente.</desc>
      <desc versionDate="2025-02-06" xml:lang="de">zeigt auf Elemente, die dem aktuellen Element in gewisser Weise entsprechen.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum versionDate="2017-05-11" xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CLLINK-egXML-vp" xml:lang="en">
          <group>
            <text xml:id="t1-g1-t1" xml:lang="mi">
              <body xml:id="t1-g1-t1-body1">
                <div type="chapter">
                  <head>He Whakamaramatanga mo te Ture Hoko, Riihi hoki, i nga Whenua Maori, 1876.</head>
                  <p>…</p>
                </div>
              </body>
            </text>
            <text xml:id="t1-g1-t2" xml:lang="en">
              <body xml:id="t1-g1-t2-body1" corresp="#t1-g1-t1-body1">
                <div type="chapter">
                  <head>An Act to regulate the Sale, Letting, and Disposal of Native Lands, 1876.</head>
                  <p>…</p>
                </div>
              </body>
            </text>
          </group>
        </egXML>
        <p>In this example a <gi>group</gi> contains two <gi>text</gi>s, each containing the same document in a different language. The correspondence is indicated using <att>corresp</att>. The language is indicated using <att>xml:lang</att>, whose value is inherited; both the tag with the <att>corresp</att> and the tag pointed to by the <att>corresp</att> inherit the value from their immediate parent.  </p>
      </exemplum>
      
      <exemplum versionDate="2017-05-25" xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CLLINK-egXML-zo" xml:lang="en">
          
        <!-- In a placeography called "places.xml" -->
        <place xml:id="LOND1" corresp="people.xml#LOND2 people.xml#GENI1">
          <placeName>London</placeName>
          <desc>The city of London...</desc>
        </place>
        
        <!-- In a literary personography called "people.xml" -->
        <person xml:id="LOND2" corresp="places.xml#LOND1 #GENI1">
          <persName type="lit">London</persName>
          <note>
            <p>Allegorical character representing the city of <placeName ref="places.xml#LOND1">London</placeName>.</p>
          </note>
        </person>
        <person xml:id="GENI1" corresp="places.xml#LOND1 #LOND2">
          <persName type="lit">London’s Genius</persName>
          <note>
            <p>Personification of London’s genius. Appears as an 
              allegorical character in mayoral shows.
            </p>
          </note>
        </person>
      </egXML>
        <p>In this example, a <gi>place</gi> element containing information about the city of 
           London is linked with two <gi>person</gi> elements in a literary personography. 
           This correspondence represents a slightly looser relationship than the one in the 
           preceding example; there is no sense in which an allegorical character could be 
           substituted for the physical city, or vice versa, but there is obviously a correspondence 
           between them.</p>
      </exemplum>
      
    </attDef>
    <attDef ident="synch" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">synchronous</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">동시발생</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">sincrónico</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">synchrone</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">sincrono</gloss>
      <gloss versionDate="2019-07-21" xml:lang="ja">連動</gloss>
      <gloss versionDate="2025-02-06" xml:lang="de">synchron</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">points to elements that are synchronous with the current element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 요소와 동시 발생하는 요소를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素和現有元素同時出現。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素と連動する要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers des éléments qui sont synchrones avec l'élément en question.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala los elementos que son sincrónicos con el elemento corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta a elementi sincroni rispetto all'elemento corrente.</desc>
      <desc versionDate="2025-02-06" xml:lang="de">zeigt auf Elemente, die synchron mit dem aktuellen Element sind.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="sameAs" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">points to an element that is the same as the current element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 요소와 동일한 요소를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素和現有元素相同。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素と同一の要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers un élément identique à l'élément en question.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala el elementos que se corresponde exactamente con el elemento corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta a un elemento che corrisponde esattamente all'elemento corrente.</desc>
      <desc versionDate="2025-02-06" xml:lang="de">zeigt auf ein Element, das mit dem aktuellen Element identisch ist.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="copyOf" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">points to an element of which the current element is a copy.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 요소가 그 복사인 요소를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">現有元素為所連結元素的複製本。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素のコピー要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers un élément dont l'élément en question est une copie.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala un elemento del que el elemento corriente es una copia.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta a un elemento di cui l'elemento corrente è una copia.</desc>
      <desc versionDate="2025-02-06" xml:lang="de">zeigt auf ein Element, von dem das aktuelle Element eine Kopie ist.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.global.linking-attr.copyOf-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>Any content of the current element should be ignored. Its
        true content is that of the element being pointed at.</p>
      </remarks>
      <remarks ident="att.global.linking-attr.copyOf-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Tout contenu appartenant à l'élément en cours doit être ignoré. Le vrai
                        contenu est celui de l'élément cible du pointeur.</p>
      </remarks>
      <remarks ident="att.global.linking-attr.copyOf-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該要素の内容は無視されるべき。本当の内容は、参照先の要素の内
        容になる。
        </p>
      </remarks>
    </attDef>
    <attDef ident="next" usage="opt">
      <gloss versionDate="2025-02-06" xml:lang="en">next</gloss>
      <gloss versionDate="2025-02-06" xml:lang="fr">suivant</gloss>
      <gloss versionDate="2025-02-06" xml:lang="de">nachfolgend</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">points to the next element of a virtual aggregate of which the current element is part.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 요소가 그 부분인 가상 집합의 다음 요소를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到現有元素所屬虛擬集合中的下一個元素。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">indica el elemento siguiente de un agregado virtual del cual elemento actual es una parte.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素も所属する仮想集合における次の要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers l'élément suivant d'un ensemble virtuel dont l'élément en question est une partie.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta all'elemento seguente all'interno di un aggregazione virtuale di cui l'elemento corrente fa parte.</desc>
      <desc versionDate="2025-02-06" xml:lang="de">zeigt auf das nächste Element innerhalb einer gedachten Gruppe, von der das betreffende Element ein Teil ist.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.global.linking-attr.next-remarks" versionDate="2017-05-02" xml:lang="en"><p>It is recommended that the element indicated be of the same type as the element bearing this attribute.</p></remarks>
      <remarks ident="att.global.linking-attr.next-remarks" versionDate="2019-09-16" xml:lang="ja">
        <p>指定された要素も、この属性を持つ要素と同じ型であることが推奨される。</p>
      </remarks>
    </attDef>
    <attDef ident="prev" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">previous</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">이전</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">anterior</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">précédent</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">precedente</gloss>
      <gloss versionDate="2019-07-21" xml:lang="ja">前の</gloss>
      <gloss versionDate="2025-02-06" xml:lang="de">vorhergehend</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">points to the previous element of a virtual aggregate of which the current element is part.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 요소가 그 부분인 가상 집합의 이전 요소를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到現有元素所屬虛擬集合中的上一個元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素も所属する仮想集合における前の要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers l'élément précédent d'un ensemble virtuel auquel appartient l'élément en question.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala al elemento precedente de una adición virtual, de la cual el elemento corriente forma parte.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta all'elemento precedente all'interno di un aggregazione virtuale di cui l'elemento corrente fa parte.</desc>
      <desc versionDate="2025-02-06" xml:lang="de">zeigt auf das vorherige Element innerhalb einer gedachten Gruppe, von der das betreffende Element ein Teil ist.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.global.linking-attr.prev-remarks" versionDate="2017-05-02" xml:lang="en"><p>It is recommended that the element indicated be of the same type as the element bearing this attribute.</p></remarks>
      <remarks ident="att.global.linking-attr.prev-remarks" versionDate="2019-09-16" xml:lang="ja">
        <p>指定された要素も、この属性を持つ要素と同じ型であることが推奨される。</p>
      </remarks>
    </attDef>
    <attDef ident="exclude" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">points to elements that are in exclusive alternation with the current element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 요소와 배타적 교체인 요소를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素是現有元素的專有替換元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素の代替要素を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers des éléments qui sont une alternative exclusive à l'élément en question.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala los elementos que estan en relación de alternancia exclusiva con el elemento corriente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta a elementi in relazione di alternanza esclusiva con l'elemento corrente.</desc>
      <desc versionDate="2025-02-06" xml:lang="de">zeigt auf Elemente, die eine exklusive Alternative zu dem aktuellen Element darstellen.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="select" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">selects one or more alternants; if one alternant is
      selected, the ambiguity or uncertainty is marked as resolved. If
      more than one alternant is selected, the degree of ambiguity or
      uncertainty is marked as reduced by the number of alternants not
      selected.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">하나 이상의 교체형을 선택한다; 만약 하나의 교체형이 선택되면 중의성 또는 불활실성이 해결된 것으로 표시된다. 만약 둘 이상의 교체형이 선택되면, 중의성 또는 불확실성의 정도가, 선택되지 않은 교체형의 수로 감소된 것으로 표시된다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">選擇一個或多個替換；若選擇一個替換，則疑惑或不明確被標記為已解決。若選擇的替換多於一個，則疑惑或不明確的程度因為未選擇的替換而被標記為減低。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">ひとつ以上の選択肢を選ぶ。ひとつの選択肢が選ばれる場合、その曖昧 度や不確実度が示される。複数の選択肢が選ばれる場合、選ばれなかっ た選択肢の数から還元される、曖昧度や不確実度が示される。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">sélectionne une ou plusieurs valeurs alternatives ; si une seule valeur est sélectionnée, l'ambiguïté ou l'incertitude est marquée comme résolue. Si plus d'une valeur alternative est sélectionnée, le degré d'ambiguïté ou d'incertitude est marqué comme réduit par le nombre de valeurs alternatives non sélectionnées.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">selecciona una o más alternativas; si se selecciona una de las alternativas, la ambigüidad o la incerteza se indica como resuelta; si se selecciona más de una alternativa, el grado de ambigüidad o incerteza se indica como reducido del número de las alternativas no seleccionadas.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">seleziona una o più alternative; se viene selezionata una delle alternative, l'ambiguità o incertezza è indicata come risolta; se viene selezionata più di un'alternativa, il grado di ambiguità o incertezza è indicato come ridotto dal numero delle alternative non selezionate.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.global.linking-attr.select-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>This attribute should be placed on an element which is
        superordinate to all of the alternants from which the
        selection is being made.</p>
      </remarks>
      <remarks ident="att.global.linking-attr.select-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut doit être placé dans un élément hiérarchiquement supérieur à
                        tous les éléments possibles parmi lesquelles la sélection est faite.</p>
      </remarks>
      <remarks ident="att.global.linking-attr.select-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該属性は、選択対象となる全ての要素の上位に位置する要素に付与
        されるべきである。
        </p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#SA"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-02-16" xml:lang="en">provides a set of attributes for hypertextual linking.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하이퍼텍스트와 다른 연결에 대한 속성의 집합을 정의한다. 이것은 연결에 대한 부가적 태그 집합이 선택될 때 모든 요소에 가능해야 한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一組用於超文字連結及其他連結的屬性，當連結的附加標籤組被選擇時，這些屬性可用於所有元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2019-07-21" xml:lang="ja">ハイパーテキストリンクの属性セットを提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2016-02-16" xml:lang="fr">fournit un ensemble d'attributs pour décrire les liens hypertextuels.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define un conjunto de atributos para hipertexto u otro vínculo habilitado para todos los elementos cuando se selecciona la etiqueta adicional para los enlaces.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi per ipertesto o altro legame abilitati per tutti gli elementi quando è selezionato il sottoinsieme di marcatori per i collegamenti.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">stellt Attribute für hypertextuelle Verlinkungen bereit.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">corresponds</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">일치</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">correspondencia</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">correspond</gloss>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">corrispondente</gloss>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2019-07-21" xml:lang="ja">対応</gloss>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[7]`.

```xml
<gloss versionDate="2025-02-06" xml:lang="de">korrespondiert</gloss>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to elements that correspond to the current element in some way.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 식으로든 현 요소와 일치하는 요소를 가리킨다.</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素在某方面符合現有元素。</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素と対応する要素を示す。</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers des éléments qui ont une correspondance avec l'élément en question.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala los elementos que presentan una correspondencia con el elemento corriente.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta a elementi che hanno una qualche corrispondenza con l'elemento corrente.</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">zeigt auf Elemente, die dem aktuellen Element in gewisser Weise entsprechen.</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum versionDate="2017-05-11" xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CLLINK-egXML-vp" xml:lang="en">
          <group>
            <text xml:id="t1-g1-t1" xml:lang="mi">
              <body xml:id="t1-g1-t1-body1">
                <div type="chapter">
                  <head>He Whakamaramatanga mo te Ture Hoko, Riihi hoki, i nga Whenua Maori, 1876.</head>
                  <p>…</p>
                </div>
              </body>
            </text>
            <text xml:id="t1-g1-t2" xml:lang="en">
              <body xml:id="t1-g1-t2-body1" corresp="#t1-g1-t1-body1">
                <div type="chapter">
                  <head>An Act to regulate the Sale, Letting, and Disposal of Native Lands, 1876.</head>
                  <p>…</p>
                </div>
              </body>
            </text>
          </group>
        </egXML>
        <p>In this example a <gi>group</gi> contains two <gi>text</gi>s, each containing the same document in a different language. The correspondence is indicated using <att>corresp</att>. The language is indicated using <att>xml:lang</att>, whose value is inherited; both the tag with the <att>corresp</att> and the tag pointed to by the <att>corresp</att> inherit the value from their immediate parent.  </p>
      </exemplum>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-05-25" xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CLLINK-egXML-zo" xml:lang="en">
          
        <!-- In a placeography called "places.xml" -->
        <place xml:id="LOND1" corresp="people.xml#LOND2 people.xml#GENI1">
          <placeName>London</placeName>
          <desc>The city of London...</desc>
        </place>
        
        <!-- In a literary personography called "people.xml" -->
        <person xml:id="LOND2" corresp="places.xml#LOND1 #GENI1">
          <persName type="lit">London</persName>
          <note>
            <p>Allegorical character representing the city of <placeName ref="places.xml#LOND1">London</placeName>.</p>
          </note>
        </person>
        <person xml:id="GENI1" corresp="places.xml#LOND1 #LOND2">
          <persName type="lit">London’s Genius</persName>
          <note>
            <p>Personification of London’s genius. Appears as an 
              allegorical character in mayoral shows.
            </p>
          </note>
        </person>
      </egXML>
        <p>In this example, a <gi>place</gi> element containing information about the city of 
           London is linked with two <gi>person</gi> elements in a literary personography. 
           This correspondence represents a slightly looser relationship than the one in the 
           preceding example; there is no sense in which an allegorical character could be 
           substituted for the physical city, or vice versa, but there is obviously a correspondence 
           between them.</p>
      </exemplum>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">synchronous</gloss>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">동시발생</gloss>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">sincrónico</gloss>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">synchrone</gloss>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">sincrono</gloss>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[6]`.

```xml
<gloss versionDate="2019-07-21" xml:lang="ja">連動</gloss>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[7]`.

```xml
<gloss versionDate="2025-02-06" xml:lang="de">synchron</gloss>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to elements that are synchronous with the current element.</desc>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 요소와 동시 발생하는 요소를 가리킨다.</desc>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素和現有元素同時出現。</desc>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素と連動する要素を示す。</desc>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers des éléments qui sont synchrones avec l'élément en question.</desc>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala los elementos que son sincrónicos con el elemento corriente.</desc>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta a elementi sincroni rispetto all'elemento corrente.</desc>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">zeigt auf Elemente, die synchron mit dem aktuellen Element sind.</desc>
```

^b41

### Block 42

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b42

### Block 43

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to an element that is the same as the current element.</desc>
```

^b43

### Block 44

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 요소와 동일한 요소를 가리킨다.</desc>
```

^b44

### Block 45

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素和現有元素相同。</desc>
```

^b45

### Block 46

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素と同一の要素を示す。</desc>
```

^b46

### Block 47

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers un élément identique à l'élément en question.</desc>
```

^b47

### Block 48

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala el elementos que se corresponde exactamente con el elemento corriente.</desc>
```

^b48

### Block 49

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta a un elemento che corrisponde esattamente all'elemento corrente.</desc>
```

^b49

### Block 50

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">zeigt auf ein Element, das mit dem aktuellen Element identisch ist.</desc>
```

^b50

### Block 51

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b51

### Block 52

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to an element of which the current element is a copy.</desc>
```

^b52

### Block 53

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 요소가 그 복사인 요소를 가리킨다.</desc>
```

^b53

### Block 54

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">現有元素為所連結元素的複製本。</desc>
```

^b54

### Block 55

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素のコピー要素を示す。</desc>
```

^b55

### Block 56

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers un élément dont l'élément en question est une copie.</desc>
```

^b56

### Block 57

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala un elemento del que el elemento corriente es una copia.</desc>
```

^b57

### Block 58

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta a un elemento di cui l'elemento corrente è una copia.</desc>
```

^b58

### Block 59

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">zeigt auf ein Element, von dem das aktuelle Element eine Kopie ist.</desc>
```

^b59

### Block 60

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b60

### Block 61

XML location: `/classSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="att.global.linking-attr.copyOf-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>Any content of the current element should be ignored. Its
        true content is that of the element being pointed at.</p>
      </remarks>
```

^b61

### Block 62

XML location: `/classSpec[1]/attList[1]/attDef[4]/remarks[2]`.

```xml
<remarks ident="att.global.linking-attr.copyOf-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Tout contenu appartenant à l'élément en cours doit être ignoré. Le vrai
                        contenu est celui de l'élément cible du pointeur.</p>
      </remarks>
```

^b62

### Block 63

XML location: `/classSpec[1]/attList[1]/attDef[4]/remarks[3]`.

```xml
<remarks ident="att.global.linking-attr.copyOf-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該要素の内容は無視されるべき。本当の内容は、参照先の要素の内
        容になる。
        </p>
      </remarks>
```

^b63

### Block 64

XML location: `/classSpec[1]/attList[1]/attDef[5]/gloss[1]`.

```xml
<gloss versionDate="2025-02-06" xml:lang="en">next</gloss>
```

^b64

### Block 65

XML location: `/classSpec[1]/attList[1]/attDef[5]/gloss[2]`.

```xml
<gloss versionDate="2025-02-06" xml:lang="fr">suivant</gloss>
```

^b65

### Block 66

XML location: `/classSpec[1]/attList[1]/attDef[5]/gloss[3]`.

```xml
<gloss versionDate="2025-02-06" xml:lang="de">nachfolgend</gloss>
```

^b66

### Block 67

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to the next element of a virtual aggregate of which the current element is part.</desc>
```

^b67

### Block 68

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 요소가 그 부분인 가상 집합의 다음 요소를 가리킨다.</desc>
```

^b68

### Block 69

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到現有元素所屬虛擬集合中的下一個元素。</desc>
```

^b69

### Block 70

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">indica el elemento siguiente de un agregado virtual del cual elemento actual es una parte.</desc>
```

^b70

### Block 71

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素も所属する仮想集合における次の要素を示す。</desc>
```

^b71

### Block 72

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers l'élément suivant d'un ensemble virtuel dont l'élément en question est une partie.</desc>
```

^b72

### Block 73

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta all'elemento seguente all'interno di un aggregazione virtuale di cui l'elemento corrente fa parte.</desc>
```

^b73

### Block 74

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">zeigt auf das nächste Element innerhalb einer gedachten Gruppe, von der das betreffende Element ein Teil ist.</desc>
```

^b74

### Block 75

XML location: `/classSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b75

### Block 76

XML location: `/classSpec[1]/attList[1]/attDef[5]/remarks[1]`.

```xml
<remarks ident="att.global.linking-attr.next-remarks" versionDate="2017-05-02" xml:lang="en"><p>It is recommended that the element indicated be of the same type as the element bearing this attribute.</p></remarks>
```

^b76

### Block 77

XML location: `/classSpec[1]/attList[1]/attDef[5]/remarks[2]`.

```xml
<remarks ident="att.global.linking-attr.next-remarks" versionDate="2019-09-16" xml:lang="ja">
        <p>指定された要素も、この属性を持つ要素と同じ型であることが推奨される。</p>
      </remarks>
```

^b77

### Block 78

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">previous</gloss>
```

^b78

### Block 79

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">이전</gloss>
```

^b79

### Block 80

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">anterior</gloss>
```

^b80

### Block 81

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">précédent</gloss>
```

^b81

### Block 82

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">precedente</gloss>
```

^b82

### Block 83

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[6]`.

```xml
<gloss versionDate="2019-07-21" xml:lang="ja">前の</gloss>
```

^b83

### Block 84

XML location: `/classSpec[1]/attList[1]/attDef[6]/gloss[7]`.

```xml
<gloss versionDate="2025-02-06" xml:lang="de">vorhergehend</gloss>
```

^b84

### Block 85

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to the previous element of a virtual aggregate of which the current element is part.</desc>
```

^b85

### Block 86

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 요소가 그 부분인 가상 집합의 이전 요소를 가리킨다.</desc>
```

^b86

### Block 87

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到現有元素所屬虛擬集合中的上一個元素。</desc>
```

^b87

### Block 88

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素も所属する仮想集合における前の要素を示す。</desc>
```

^b88

### Block 89

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers l'élément précédent d'un ensemble virtuel auquel appartient l'élément en question.</desc>
```

^b89

### Block 90

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala al elemento precedente de una adición virtual, de la cual el elemento corriente forma parte.</desc>
```

^b90

### Block 91

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta all'elemento precedente all'interno di un aggregazione virtuale di cui l'elemento corrente fa parte.</desc>
```

^b91

### Block 92

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">zeigt auf das vorherige Element innerhalb einer gedachten Gruppe, von der das betreffende Element ein Teil ist.</desc>
```

^b92

### Block 93

XML location: `/classSpec[1]/attList[1]/attDef[6]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b93

### Block 94

XML location: `/classSpec[1]/attList[1]/attDef[6]/remarks[1]`.

```xml
<remarks ident="att.global.linking-attr.prev-remarks" versionDate="2017-05-02" xml:lang="en"><p>It is recommended that the element indicated be of the same type as the element bearing this attribute.</p></remarks>
```

^b94

### Block 95

XML location: `/classSpec[1]/attList[1]/attDef[6]/remarks[2]`.

```xml
<remarks ident="att.global.linking-attr.prev-remarks" versionDate="2019-09-16" xml:lang="ja">
        <p>指定された要素も、この属性を持つ要素と同じ型であることが推奨される。</p>
      </remarks>
```

^b95

### Block 96

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to elements that are in exclusive alternation with the current element.</desc>
```

^b96

### Block 97

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 요소와 배타적 교체인 요소를 가리킨다.</desc>
```

^b97

### Block 98

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到的元素是現有元素的專有替換元素。</desc>
```

^b98

### Block 99

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素の代替要素を示す。</desc>
```

^b99

### Block 100

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers des éléments qui sont une alternative exclusive à l'élément en question.</desc>
```

^b100

### Block 101

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala los elementos que estan en relación de alternancia exclusiva con el elemento corriente.</desc>
```

^b101

### Block 102

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta a elementi in relazione di alternanza esclusiva con l'elemento corrente.</desc>
```

^b102

### Block 103

XML location: `/classSpec[1]/attList[1]/attDef[7]/desc[8]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">zeigt auf Elemente, die eine exklusive Alternative zu dem aktuellen Element darstellen.</desc>
```

^b103

### Block 104

XML location: `/classSpec[1]/attList[1]/attDef[7]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b104

### Block 105

XML location: `/classSpec[1]/attList[1]/attDef[8]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">selects one or more alternants; if one alternant is
      selected, the ambiguity or uncertainty is marked as resolved. If
      more than one alternant is selected, the degree of ambiguity or
      uncertainty is marked as reduced by the number of alternants not
      selected.</desc>
```

^b105

### Block 106

XML location: `/classSpec[1]/attList[1]/attDef[8]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나 이상의 교체형을 선택한다; 만약 하나의 교체형이 선택되면 중의성 또는 불활실성이 해결된 것으로 표시된다. 만약 둘 이상의 교체형이 선택되면, 중의성 또는 불확실성의 정도가, 선택되지 않은 교체형의 수로 감소된 것으로 표시된다.</desc>
```

^b106

### Block 107

XML location: `/classSpec[1]/attList[1]/attDef[8]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">選擇一個或多個替換；若選擇一個替換，則疑惑或不明確被標記為已解決。若選擇的替換多於一個，則疑惑或不明確的程度因為未選擇的替換而被標記為減低。</desc>
```

^b107

### Block 108

XML location: `/classSpec[1]/attList[1]/attDef[8]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ひとつ以上の選択肢を選ぶ。ひとつの選択肢が選ばれる場合、その曖昧 度や不確実度が示される。複数の選択肢が選ばれる場合、選ばれなかっ た選択肢の数から還元される、曖昧度や不確実度が示される。</desc>
```

^b108

### Block 109

XML location: `/classSpec[1]/attList[1]/attDef[8]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">sélectionne une ou plusieurs valeurs alternatives ; si une seule valeur est sélectionnée, l'ambiguïté ou l'incertitude est marquée comme résolue. Si plus d'une valeur alternative est sélectionnée, le degré d'ambiguïté ou d'incertitude est marqué comme réduit par le nombre de valeurs alternatives non sélectionnées.</desc>
```

^b109

### Block 110

XML location: `/classSpec[1]/attList[1]/attDef[8]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">selecciona una o más alternativas; si se selecciona una de las alternativas, la ambigüidad o la incerteza se indica como resuelta; si se selecciona más de una alternativa, el grado de ambigüidad o incerteza se indica como reducido del número de las alternativas no seleccionadas.</desc>
```

^b110

### Block 111

XML location: `/classSpec[1]/attList[1]/attDef[8]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">seleziona una o più alternative; se viene selezionata una delle alternative, l'ambiguità o incertezza è indicata come risolta; se viene selezionata più di un'alternativa, il grado di ambiguità o incertezza è indicato come ridotto dal numero delle alternative non selezionate.</desc>
```

^b111

### Block 112

XML location: `/classSpec[1]/attList[1]/attDef[8]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b112

### Block 113

XML location: `/classSpec[1]/attList[1]/attDef[8]/remarks[1]`.

```xml
<remarks ident="att.global.linking-attr.select-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>This attribute should be placed on an element which is
        superordinate to all of the alternants from which the
        selection is being made.</p>
      </remarks>
```

^b113

### Block 114

XML location: `/classSpec[1]/attList[1]/attDef[8]/remarks[2]`.

```xml
<remarks ident="att.global.linking-attr.select-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut doit être placé dans un élément hiérarchiquement supérieur à
                        tous les éléments possibles parmi lesquelles la sélection est faite.</p>
      </remarks>
```

^b114

### Block 115

XML location: `/classSpec[1]/attList[1]/attDef[8]/remarks[3]`.

```xml
<remarks ident="att.global.linking-attr.select-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該属性は、選択対象となる全ての要素の上位に位置する要素に付与
        されるべきである。
        </p>
      </remarks>
```

^b115

### Block 116

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SA"/>
  </listRef>
```

^b116

