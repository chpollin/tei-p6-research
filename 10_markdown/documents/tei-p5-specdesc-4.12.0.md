---
type: representation
source-type: document
source: '[[00_sources/tei-p5-specdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 specDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/specDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# specDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11120. Git blob: `0536ae01cfcc21214e6bdfe21bd02ed30be8b410`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="SPECDESC" ident="specDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">specification description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">명시 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">元素或元素集描述</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">specification description</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción de elemento o clase.</gloss>
  <gloss versionDate="2021-02-09" xml:lang="it">descrizione di elemento, macro o classe</gloss>
  <desc versionDate="2021-01-23" xml:lang="en">indicates that a description of the specified element, class, or macro should be included at this
    point within a document.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">명시된 요소 또는 부류에 대한 기술이 문서 내 이 지점에 포함되었음을 나타낸다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出指定元素或元素集的描述應在此包括在文件中。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">特定された要素またはクラスの解説は、文書中のこの場所にあるべきである ことを示す。</desc>
  <desc versionDate="2021-01-23" xml:lang="fr">indique qu'une description de l'élément particulier, de
    la classe particulière ou de la macro doit être incluse à ce point dans un document.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el punto del documento en el que debe inserirse la
    descripción de un elemento dado o de una clase dada.</desc>
  <desc versionDate="2021-01-29" xml:lang="it">indica il punto del documento nel quale deve essere
    inserita la descrizione di un dato elemento, una data macro o di una data classe</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.specDescLike"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="key" usage="req">
      <gloss versionDate="2005-01-14" xml:lang="en">identifier</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">확인소</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW">識別符碼</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">identifiant</gloss>
      <gloss versionDate="2007-05-04" xml:lang="es">identificador</gloss>
      <gloss versionDate="2007-01-21" xml:lang="it">identificatore</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">supplies the
      identifier of the documentary element or class for which a
      description is to be obtained.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">기술이 얻어진 문서 요소 또는 부류에 대한 확인소를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件元素或元素集的識別符碼。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">解説が表される、記録用の要素またはクラスの識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant de l'élément ou de la classe
        documentaire pour lequels la description est à faire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">adscribe un identificador al elemento o a la clase
        que se está describiendo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento o alla classe
        per i quali deve essere fornita una descrizione</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-tk" source="#UND">
          <specDesc key="emph"/>
        </egXML>
      </exemplum>
      <exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-ur" source="#UND">
          <specDesc key="emph"/>
        </egXML>
      </exemplum>
      <remarks ident="specDesc-attr.key-remarks" versionDate="2021-01-28" xml:lang="en"><p>The value should match the <att>ident</att> of a documentary element (that is, a member of att.identified).</p></remarks>
      <remarks ident="specDesc-attr.key-remarks" versionDate="2021-01-29" xml:lang="it"><p>Il valore dovrebbe essere lo stesso dell'<att>ident</att> di un elemento di documentazione (vale a dire, il membro di att.identified).</p></remarks>
    </attDef>
    <attDef ident="atts" usage="rec">
      <gloss versionDate="2005-01-14" xml:lang="en">attributes</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">속성</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">attributs</gloss>
      <gloss versionDate="2007-05-04" xml:lang="es">atributo</gloss>
      <gloss versionDate="2007-01-21" xml:lang="it">attributi</gloss>
      <desc versionDate="2005-08-06" xml:lang="en">supplies attribute names for which descriptions should additionally be obtained.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">기술이 부가적으로 얻어진 속성명을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供其屬性描述應另外包含的屬性名稱。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">解説が付加的に表される属性名を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne les noms des attributs dont il faut une
        description supplémentaire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona nombres de atributo pera los que se debe
        proporcionar una descripción.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica dei nomi di attributi per i quali devono
        essere fornite delle descrizioni</desc>
      <datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.name"/></datatype>
      <exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-cz" source="#UND">
          <specDesc key="foreign" atts="usage xml:lang"/>
        </egXML>
      </exemplum>
      <exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-ju" source="#UND">
          <specDesc key="foreign" atts="usage xml:lang"/>
        </egXML>
      </exemplum>
      <remarks ident="specDesc-attr.atts-remarks" versionDate="2013-12-06" xml:lang="en">
        <p>The attribute names listed may include both attributes inherited from a class and those
          defined explicitly for the associated element. <!-- If the <att>atts</att> attribute is not
          supplied, then descriptions for all non-inherited attributes are listed, along with
          references to any classes. If an empty string is supplied as the value for the
          <att>atts</att> attribute, then no description should be displayed.--></p>
      </remarks>
      <remarks ident="specDesc-attr.atts-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Les noms d'attribut listés peuvent inclure à la fois des attributs hérités d'une classe
          et ceux qui sont définis explicitement pour l'élément associé. <!-- Si l'attribut <att>atts</att> n'est
          pas fourni, il faut lister et décrire tous les attributs non hérités, avec référence aux
          classes éventuelles. Si une chaîne vide est indiquée comme valeur pour l'attribut
            <att>atts</att>, on ne devrait pas afficher de description.--></p>
      </remarks>
      <remarks ident="specDesc-attr.atts-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> リスト中の属性名には、クラスから継承した属性や、また関連する要 素で明示的に定義されている属性を含むかもしれない。
          属性<att>atts</att>がない場合、継承されない属性がリスト化され、 各クラスへの参照が示される。属性<att>atts</att>の値に空文字が
          付与されている場合、解説は表示されないべきである。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-fc" source="#UND">
      <specDesc key="orth"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-eh" source="#UND">
      <specDesc key="orth"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-my" source="#UND">
      <specDesc key="emph"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-ga" source="#UND">
      <specDesc key="foreign" atts="usage xml:lang"/>
    </egXML>
  </exemplum>
  <remarks ident="specDesc-remarks" versionDate="2005-08-06" xml:lang="en">
    <p>The description is usually displayed as a label and an item. <!--, with any list of values defined
      for the attribute as an embedded glossary list, No selection among the values is possible. -->The
      list of attributes may include some which are inherited by virtue of an element's class
      membership; descriptions for such attributes may also be retrieved using another
      <gi>specDesc</gi>, this time pointing at the relevant class.</p>
  </remarks>
  <remarks ident="specDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La description est habituellement affichée sous la forme d'une étiquette et d'un contenu. <!--,
      avec toutes les listes de valeurs définies pour l'attribut, comme une liste de glossaire imbriquée.
     Aucune sélection parmi ces valeurs n'est possible. --> La liste d'attributs peut inclure des
      attributs hérités en vertu de leur appartenance à une classe d'éléments ; les descriptions de
      ces attributs peuvent également être récupérées en utilisant un autre élément
      <gi>specDesc</gi> qui pointe cette fois vers la classe pertinente.</p>
  </remarks>
  <remarks ident="specDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該解説は、一般には、属性として定義される値のリストとして、ラベル と各項目で示される。その値から更に選択することはできない。属性
      のリストには、要素クラスから継承したものもある。このような属性の解 説は、他の要素<gi>specDesc</gi>を使い示されるかもしれない。この場
      合、関連するクラスを指示することになる。 </p>
  </remarks>
  <listRef>
    <ptr target="#TDphraseEA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">specification description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">명시 기술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">元素或元素集描述</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">specification description</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción de elemento o clase.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2021-02-09" xml:lang="it">descrizione di elemento, macro o classe</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-01-23" xml:lang="en">indicates that a description of the specified element, class, or macro should be included at this
    point within a document.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">명시된 요소 또는 부류에 대한 기술이 문서 내 이 지점에 포함되었음을 나타낸다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出指定元素或元素集的描述應在此包括在文件中。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">特定された要素またはクラスの解説は、文書中のこの場所にあるべきである ことを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2021-01-23" xml:lang="fr">indique qu'une description de l'élément particulier, de
    la classe particulière ou de la macro doit être incluse à ce point dans un document.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el punto del documento en el que debe inserirse la
    descripción de un elemento dado o de una clase dada.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2021-01-29" xml:lang="it">indica il punto del documento nel quale deve essere
    inserita la descrizione di un dato elemento, una data macro o di una data classe</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.specDescLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">identifier</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">확인소</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">識別符碼</gloss>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">identifiant</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">identificador</gloss>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">identificatore</gloss>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies the
      identifier of the documentary element or class for which a
      description is to be obtained.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기술이 얻어진 문서 요소 또는 부류에 대한 확인소를 제시한다.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件元素或元素集的識別符碼。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">解説が表される、記録用の要素またはクラスの識別子を示す。</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant de l'élément ou de la classe
        documentaire pour lequels la description est à faire.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">adscribe un identificador al elemento o a la clase
        que se está describiendo.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore all'elemento o alla classe
        per i quali deve essere fornita una descrizione</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-tk" source="#UND">
          <specDesc key="emph"/>
        </egXML>
      </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-ur" source="#UND">
          <specDesc key="emph"/>
        </egXML>
      </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="specDesc-attr.key-remarks" versionDate="2021-01-28" xml:lang="en"><p>The value should match the <att>ident</att> of a documentary element (that is, a member of att.identified).</p></remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="specDesc-attr.key-remarks" versionDate="2021-01-29" xml:lang="it"><p>Il valore dovrebbe essere lo stesso dell'<att>ident</att> di un elemento di documentazione (vale a dire, il membro di att.identified).</p></remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">attributes</gloss>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">속성</gloss>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性</gloss>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">attributs</gloss>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">atributo</gloss>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">attributi</gloss>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-08-06" xml:lang="en">supplies attribute names for which descriptions should additionally be obtained.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기술이 부가적으로 얻어진 속성명을 제시한다.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供其屬性描述應另外包含的屬性名稱。</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">解説が付加的に表される属性名を示す。</desc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne les noms des attributs dont il faut une
        description supplémentaire.</desc>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona nombres de atributo pera los que se debe
        proporcionar una descripción.</desc>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica dei nomi di attributi per i quali devono
        essere fornite delle descrizioni</desc>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.name"/></datatype>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[2]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-cz" source="#UND">
          <specDesc key="foreign" atts="usage xml:lang"/>
        </egXML>
      </exemplum>
```

^b48

### Block 49

XML location: `/elementSpec[1]/attList[1]/attDef[2]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-ju" source="#UND">
          <specDesc key="foreign" atts="usage xml:lang"/>
        </egXML>
      </exemplum>
```

^b49

### Block 50

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="specDesc-attr.atts-remarks" versionDate="2013-12-06" xml:lang="en">
        <p>The attribute names listed may include both attributes inherited from a class and those
          defined explicitly for the associated element. <!-- If the <att>atts</att> attribute is not
          supplied, then descriptions for all non-inherited attributes are listed, along with
          references to any classes. If an empty string is supplied as the value for the
          <att>atts</att> attribute, then no description should be displayed.--></p>
      </remarks>
```

^b50

### Block 51

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="specDesc-attr.atts-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Les noms d'attribut listés peuvent inclure à la fois des attributs hérités d'une classe
          et ceux qui sont définis explicitement pour l'élément associé. <!-- Si l'attribut <att>atts</att> n'est
          pas fourni, il faut lister et décrire tous les attributs non hérités, avec référence aux
          classes éventuelles. Si une chaîne vide est indiquée comme valeur pour l'attribut
            <att>atts</att>, on ne devrait pas afficher de description.--></p>
      </remarks>
```

^b51

### Block 52

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="specDesc-attr.atts-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> リスト中の属性名には、クラスから継承した属性や、また関連する要 素で明示的に定義されている属性を含むかもしれない。
          属性<att>atts</att>がない場合、継承されない属性がリスト化され、 各クラスへの参照が示される。属性<att>atts</att>の値に空文字が
          付与されている場合、解説は表示されないべきである。 </p>
      </remarks>
```

^b52

### Block 53

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-fc" source="#UND">
      <specDesc key="orth"/>
    </egXML>
  </exemplum>
```

^b53

### Block 54

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-eh" source="#UND">
      <specDesc key="orth"/>
    </egXML>
  </exemplum>
```

^b54

### Block 55

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-my" source="#UND">
      <specDesc key="emph"/>
    </egXML>
  </exemplum>
```

^b55

### Block 56

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECDESC-egXML-ga" source="#UND">
      <specDesc key="foreign" atts="usage xml:lang"/>
    </egXML>
  </exemplum>
```

^b56

### Block 57

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="specDesc-remarks" versionDate="2005-08-06" xml:lang="en">
    <p>The description is usually displayed as a label and an item. <!--, with any list of values defined
      for the attribute as an embedded glossary list, No selection among the values is possible. -->The
      list of attributes may include some which are inherited by virtue of an element's class
      membership; descriptions for such attributes may also be retrieved using another
      <gi>specDesc</gi>, this time pointing at the relevant class.</p>
  </remarks>
```

^b57

### Block 58

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="specDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La description est habituellement affichée sous la forme d'une étiquette et d'un contenu. <!--,
      avec toutes les listes de valeurs définies pour l'attribut, comme une liste de glossaire imbriquée.
     Aucune sélection parmi ces valeurs n'est possible. --> La liste d'attributs peut inclure des
      attributs hérités en vertu de leur appartenance à une classe d'éléments ; les descriptions de
      ces attributs peuvent également être récupérées en utilisant un autre élément
      <gi>specDesc</gi> qui pointe cette fois vers la classe pertinente.</p>
  </remarks>
```

^b58

### Block 59

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="specDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該解説は、一般には、属性として定義される値のリストとして、ラベル と各項目で示される。その値から更に選択することはできない。属性
      のリストには、要素クラスから継承したものもある。このような属性の解 説は、他の要素<gi>specDesc</gi>を使い示されるかもしれない。この場
      合、関連するクラスを指示することになる。 </p>
  </remarks>
```

^b59

### Block 60

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDphraseEA"/>
  </listRef>
```

^b60

