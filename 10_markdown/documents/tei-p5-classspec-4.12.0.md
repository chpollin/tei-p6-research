---
type: representation
source-type: document
source: '[[00_sources/tei-p5-classspec-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 classSpec
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/classSpec.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# classSpec

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 15966. Git blob: `8fead3350c14581f2edadea8e362d0e7538a2298`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-classSpec" ident="classSpec">
  <gloss versionDate="2007-07-04" xml:lang="en">class specification</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">부류 명시</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">especificación de la clase</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">spécification de classe</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">indicazione di classe</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">クラス仕様</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains reference information for a TEI element class; 
that is a group of 
  elements which appear together in  content models, or 
  which share some common attribute, or both.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">TEI 요소 부류에 대한 참조 정보를 포함한다; 이것은 내용 모델에서 함께 나타나거나, 공통 속성을 공유하거나, 이 둘을 포괄하는 요소들의 그룹이다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個TEI元素集的參照資訊；元素集是一群在內容模組中同時出現、或共用某些屬性、或兩者皆包括的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">TEI要素クラスにおける参照情報を示す。内容モデルに出現する要素のまと
  まり、共通する属性のまとまり、またはその両方。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations de référence pour une
			classe d'éléments  TEI, c'est-à-dire un groupe d'éléments qui figurent ensemble
			dans des modèles de contenu ou qui partagent un attribut commun, ou qui ont l'un et l'autre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas a una clase de elementos TEI, es decir, a un grupo de elementos que aparecen juntos en modelos de contenido, o que tienen algunos atributos en común, o ambas cosas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative a una classe di elementi TEI, cioè un gruppo di elementi che compaiono insieme in modelli di contenuto, oppure che hanno alcuni attributi in comune, o entrambe le cose.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.identSynonyms"/>
          <classRef key="model.descLike"/>
        </alternate>
        <elementRef key="classes" minOccurs="0"/>
        <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="attList" minOccurs="0"/>
        <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="req">
      <desc versionDate="2005-10-05" xml:lang="en">indicates whether this is a model class or an attribute class</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">모델 부류 또는 속성 부류 여부를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出這是結構元素集或是屬性元素集。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該クラスがモデルクラスか属性クラスかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si c'est une classe de modèles ou une classe d'attributs.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si se trata de una clase de modelos o de atributos.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se si tratta di una classe di modelli o di attributi.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="model">
          <gloss versionDate="2007-07-04" xml:lang="en">content model</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">내용 모델</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">modelo de contenido</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">modèle de contenu</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">modello di contenuto</gloss>
          <gloss versionDate="2024-02-28" xml:lang="ja">内容モデル</gloss>
          <desc versionDate="2007-04-15" xml:lang="en">members of this class appear in the same  content models</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 부류의 원소는 동일 내용 모델에서 나타난다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素出現在相同的內容模組中</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">内容モデルクラス。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de cette classe
							figurent dans les mêmes modèles de contenu</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de esta clase aparecen en los mismos modelos de contenido.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri di questa classe compaiono negli stessi modelli di contenuto.</desc>
        </valItem>
        <valItem ident="atts">
          <gloss versionDate="2007-07-04" xml:lang="en">attributes</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">속성</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">atributos</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">attributs</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributi</gloss>
          <gloss versionDate="2024-02-28" xml:lang="ja">属性の集合</gloss>
          <desc versionDate="2007-04-15" xml:lang="en">members of this class share common attributes</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 부류의 원소는 공통 속성을 공유한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素有共用的屬性</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性クラス。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de cette classe
							partagent des attributs communs</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de esta clase tienen algunos atributos comunes.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri di questa classe hanno alcuni attributi in comune.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="generate" usage="opt">
      <desc versionDate="2007-10-23" xml:lang="en">indicates which alternation and sequence instantiations
	of a model class may be referenced. By default, all variations
	are permitted.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">모델 부류의 교체 및 일련의 인스턴스 생성이 참조될 수 있음을 나타낸다. 기본적으로 모든 변이형이 허용된다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明應該建立結構元素集的哪些替換及順序作業實例。在預設的情形下，會提供所有的變數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">モデルクラスのインスタンスとしてある選択肢を示す。デフォルトでは、
      あらゆるものが可能である。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne les règles régissant  dans une
					instance TEI  l'ordre et l'alternance des éléments définis par la classe. Par
					défaut, toutes les variations sont données.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica que alternancia y que tipos de secuencia se establecen para una clase de modelos; por defecto se indican todas las variaciones.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica quale alternanza e quali tipi di sequenza stabilire per una classe di modelli; di norma sono indicate tutte le variazioni.</desc>
      <datatype maxOccurs="5"><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="alternation">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class are alternatives</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소들은 선택가능 항목이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素是替換元素</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、選択的である。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe
							constituent des alternatives</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de las clase estan en relación de alternancia.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe sono in relatione di alternanza.</desc>
        </valItem>
        <valItem ident="sequence">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class are to be provided in sequence</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소는 차례대로 제시된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素會依序呈現</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストとしてある。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe doivent
							tous être donnés dans l'ordre indiqué</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de las clase se indican en secuencia.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe devono essere indicati in sequenza.</desc>
        </valItem>
        <valItem ident="sequenceOptional">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class may be provided, in sequence,
	    but are optional</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소는 차례대로 제시될 수 있지만 수의적이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素可依序呈現，但非必須</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストから選択される。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe peuvent
							être donnés, dans l'ordre indiqué, mais sont facultatifs</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de la clase pueden proporcionarse en modo de secuencia pero son opcionales.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe possono essere indicati in sequenza ma sono facoltativi.</desc>
        </valItem>
        <valItem ident="sequenceOptionalRepeatable">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class may be provided one or more
	    times, in sequence, but are optional.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소들은 한 번 이상 그리고 차례대로 제시될 수 있지만 수의적이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素可一次或多次依序呈現，但非必須</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストから1つ以上が選択される。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe peuvent
							être donnés une ou plusieurs fois, dans l'ordre indiqué, mais sont
							facultatifs</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de la clase pueden indicarse una o más ocasiones en secuencia, pero son opcionales.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe possono essere indicati una o più volte in sequenza ma sono facoltativi.</desc>
        </valItem>
        <valItem ident="sequenceRepeatable">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class may be provided one or more times, in sequence</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소들은 차례대로 한 번 이상 제시될 수 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素可一次或多次依序呈現</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストから1つ以上が選択される。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe doivent
							être donnés au moins une fois, dans l'ordre indiqué.</desc>
          <desc versionDate="2007-05-04" xml:lang="es">miembros de la clase pueden ser indicados una o más veces en secuencia.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe possono essere indicati una o più volte in sequenza.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classSpec-egXML-kg">
      <classSpec module="tei" type="model" ident="model.segLike">
        <desc>groups elements used for arbitrary segmentation.</desc>
        <classes>
          <memberOf key="model.phrase"/>
        </classes>
        <remarks>
          <p>The principles on which segmentation is carried out, and
any special codes or attribute values used, should be defined explicitly
in the <gi>segmentation</gi> element of the <gi>encodingDesc</gi> within
the associated TEI header.</p>
        </remarks>
      </classSpec>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classSpec-egXML-mp">
      <classSpec module="tei" type="model" ident="model.segLike">
        <desc>regroupe des éléments utilisés pour des segmentations arbitraires.</desc>
        <classes>
          <memberOf key="model.phrase"/>
        </classes>
        <remarks>
          <p>Les principes selon lesquels la segmentation est effectuée, et tous les codes
              spéciaux ou toutes les valeurs d'attribut utilisées, devraient être définis
              explicitement dans l'élément<gi>segmentation</gi> de l'élément<gi>encodingDesc</gi>
              dans l'en-tête TEI associé.</p>
        </remarks>
      </classSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classSpec-egXML-nw">
      <classSpec module="tei" type="model" ident="model.segLike">
        <desc>匯集用於隨機分割的元素</desc>
        <classes>
          <memberOf key="model.phrase"/>
        </classes>
        <remarks>
          <p>The principles on which segmentation is carried out, and any special codes or attribute
            values used, should be defined explicitly in the <gi>segmentation</gi> element of the
            <gi>encodingDesc</gi> within the associated TEI header.</p>
        </remarks>
      </classSpec>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDcrystals"/>
    <ptr target="#TDCLA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">class specification</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">부류 명시</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">especificación de la clase</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">spécification de classe</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">indicazione di classe</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">クラス仕様</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains reference information for a TEI element class; 
that is a group of 
  elements which appear together in  content models, or 
  which share some common attribute, or both.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">TEI 요소 부류에 대한 참조 정보를 포함한다; 이것은 내용 모델에서 함께 나타나거나, 공통 속성을 공유하거나, 이 둘을 포괄하는 요소들의 그룹이다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個TEI元素集的參照資訊；元素集是一群在內容模組中同時出現、或共用某些屬性、或兩者皆包括的元素。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">TEI要素クラスにおける参照情報を示す。内容モデルに出現する要素のまと
  まり、共通する属性のまとまり、またはその両方。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations de référence pour une
			classe d'éléments  TEI, c'est-à-dire un groupe d'éléments qui figurent ensemble
			dans des modèles de contenu ou qui partagent un attribut commun, ou qui ont l'un et l'autre.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas a una clase de elementos TEI, es decir, a un grupo de elementos que aparecen juntos en modelos de contenido, o que tienen algunos atributos en común, o ambas cosas.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative a una classe di elementi TEI, cioè un gruppo di elementi che compaiono insieme in modelli di contenuto, oppure che hanno alcuni attributi in comune, o entrambe le cose.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.oddDecl"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.identSynonyms"/>
          <classRef key="model.descLike"/>
        </alternate>
        <elementRef key="classes" minOccurs="0"/>
        <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="attList" minOccurs="0"/>
        <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-05" xml:lang="en">indicates whether this is a model class or an attribute class</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">모델 부류 또는 속성 부류 여부를 나타낸다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出這是結構元素集或是屬性元素集。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該クラスがモデルクラスか属性クラスかを示す。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si c'est une classe de modèles ou une classe d'attributs.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si se trata de una clase de modelos o de atributos.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se si tratta di una classe di modelli o di attributi.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="model">
          <gloss versionDate="2007-07-04" xml:lang="en">content model</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">내용 모델</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">modelo de contenido</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">modèle de contenu</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">modello di contenuto</gloss>
          <gloss versionDate="2024-02-28" xml:lang="ja">内容モデル</gloss>
          <desc versionDate="2007-04-15" xml:lang="en">members of this class appear in the same  content models</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 부류의 원소는 동일 내용 모델에서 나타난다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素出現在相同的內容模組中</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">内容モデルクラス。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de cette classe
							figurent dans les mêmes modèles de contenu</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de esta clase aparecen en los mismos modelos de contenido.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri di questa classe compaiono negli stessi modelli di contenuto.</desc>
        </valItem>
        <valItem ident="atts">
          <gloss versionDate="2007-07-04" xml:lang="en">attributes</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">속성</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">atributos</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">attributs</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributi</gloss>
          <gloss versionDate="2024-02-28" xml:lang="ja">属性の集合</gloss>
          <desc versionDate="2007-04-15" xml:lang="en">members of this class share common attributes</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 부류의 원소는 공통 속성을 공유한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素有共用的屬性</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性クラス。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de cette classe
							partagent des attributs communs</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de esta clase tienen algunos atributos comunes.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri di questa classe hanno alcuni attributi in comune.</desc>
        </valItem>
      </valList>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-10-23" xml:lang="en">indicates which alternation and sequence instantiations
	of a model class may be referenced. By default, all variations
	are permitted.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">모델 부류의 교체 및 일련의 인스턴스 생성이 참조될 수 있음을 나타낸다. 기본적으로 모든 변이형이 허용된다.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明應該建立結構元素集的哪些替換及順序作業實例。在預設的情形下，會提供所有的變數。</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">モデルクラスのインスタンスとしてある選択肢を示す。デフォルトでは、
      あらゆるものが可能である。</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne les règles régissant  dans une
					instance TEI  l'ordre et l'alternance des éléments définis par la classe. Par
					défaut, toutes les variations sont données.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica que alternancia y que tipos de secuencia se establecen para una clase de modelos; por defecto se indican todas las variaciones.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica quale alternanza e quali tipi di sequenza stabilire per una classe di modelli; di norma sono indicate tutte le variazioni.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="5"><dataRef key="teidata.enumerated"/></datatype>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="alternation">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class are alternatives</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소들은 선택가능 항목이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素是替換元素</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、選択的である。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe
							constituent des alternatives</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de las clase estan en relación de alternancia.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe sono in relatione di alternanza.</desc>
        </valItem>
        <valItem ident="sequence">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class are to be provided in sequence</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소는 차례대로 제시된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素會依序呈現</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストとしてある。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe doivent
							tous être donnés dans l'ordre indiqué</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de las clase se indican en secuencia.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe devono essere indicati in sequenza.</desc>
        </valItem>
        <valItem ident="sequenceOptional">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class may be provided, in sequence,
	    but are optional</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소는 차례대로 제시될 수 있지만 수의적이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素可依序呈現，但非必須</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストから選択される。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe peuvent
							être donnés, dans l'ordre indiqué, mais sont facultatifs</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de la clase pueden proporcionarse en modo de secuencia pero son opcionales.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe possono essere indicati in sequenza ma sono facoltativi.</desc>
        </valItem>
        <valItem ident="sequenceOptionalRepeatable">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class may be provided one or more
	    times, in sequence, but are optional.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소들은 한 번 이상 그리고 차례대로 제시될 수 있지만 수의적이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素可一次或多次依序呈現，但非必須</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストから1つ以上が選択される。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe peuvent
							être donnés une ou plusieurs fois, dans l'ordre indiqué, mais sont
							facultatifs</desc>
          <desc versionDate="2007-05-04" xml:lang="es">los miembros de la clase pueden indicarse una o más ocasiones en secuencia, pero son opcionales.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe possono essere indicati una o più volte in sequenza ma sono facoltativi.</desc>
        </valItem>
        <valItem ident="sequenceRepeatable">
          <desc versionDate="2007-04-15" xml:lang="en">members of the class may be provided one or more times, in sequence</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">부류의 원소들은 차례대로 한 번 이상 제시될 수 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集的元素可一次或多次依序呈現</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該クラスの構成要素は、リストから1つ以上が選択される。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">les membres de la classe doivent
							être donnés au moins une fois, dans l'ordre indiqué.</desc>
          <desc versionDate="2007-05-04" xml:lang="es">miembros de la clase pueden ser indicados una o más veces en secuencia.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i membri della classe possono essere indicati una o più volte in sequenza.</desc>
        </valItem>
      </valList>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classSpec-egXML-kg">
      <classSpec module="tei" type="model" ident="model.segLike">
        <desc>groups elements used for arbitrary segmentation.</desc>
        <classes>
          <memberOf key="model.phrase"/>
        </classes>
        <remarks>
          <p>The principles on which segmentation is carried out, and
any special codes or attribute values used, should be defined explicitly
in the <gi>segmentation</gi> element of the <gi>encodingDesc</gi> within
the associated TEI header.</p>
        </remarks>
      </classSpec>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classSpec-egXML-mp">
      <classSpec module="tei" type="model" ident="model.segLike">
        <desc>regroupe des éléments utilisés pour des segmentations arbitraires.</desc>
        <classes>
          <memberOf key="model.phrase"/>
        </classes>
        <remarks>
          <p>Les principes selon lesquels la segmentation est effectuée, et tous les codes
              spéciaux ou toutes les valeurs d'attribut utilisées, devraient être définis
              explicitement dans l'élément<gi>segmentation</gi> de l'élément<gi>encodingDesc</gi>
              dans l'en-tête TEI associé.</p>
        </remarks>
      </classSpec>
    </egXML>
  </exemplum>
```

^b36

### Block 37

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classSpec-egXML-nw">
      <classSpec module="tei" type="model" ident="model.segLike">
        <desc>匯集用於隨機分割的元素</desc>
        <classes>
          <memberOf key="model.phrase"/>
        </classes>
        <remarks>
          <p>The principles on which segmentation is carried out, and any special codes or attribute
            values used, should be defined explicitly in the <gi>segmentation</gi> element of the
            <gi>encodingDesc</gi> within the associated TEI header.</p>
        </remarks>
      </classSpec>
    </egXML>
  </exemplum>
```

^b37

### Block 38

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDcrystals"/>
    <ptr target="#TDCLA"/>
  </listRef>
```

^b38

