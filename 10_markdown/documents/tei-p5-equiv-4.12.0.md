---
type: representation
source-type: document
source: '[[00_sources/tei-p5-equiv-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 equiv
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/equiv.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# equiv

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9557. Git blob: `7a45466a5d3462e0218abb1a6b1a043e51132e79`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xml:id="gi-equiv" module="tagdocs" ident="equiv">
  <gloss versionDate="2007-07-04" xml:lang="en">equivalent</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">동치</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">equivalente</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">équivalent</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">equivalente</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies a component which is considered equivalent to the parent element, either by
    co-reference, or by external link.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">부모 요소와 동치로 고려되는 성분을 공지시 또는 외부 연결을 통해 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">具體指出一個與父元素同等的名稱，無論是藉由交互參照或是外部連結。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">親要素と同等とされる構成要素を、相互参照または外部リンクで示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">précise un composant considéré comme un équivalent de
    l'élément parent, soit par une référence commune, soit par un lien externe.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica un componente que se considera equivalente al
    elemento padre, o por co-referencias o por algún enlace externo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica un componente considerato equivalente ad un
    elemento genitore sia per co-referenza che tramite link esterno.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.internetMedia"/>
    <memberOf key="att.predicate"/>
    <memberOf key="model.identEquiv"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="name" usage="opt">
      <desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), naming the underlying concept of which the parent is a representation.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">부모가 표상하는 기저 개념에 대한 이름을 부여한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明父元素所標記的基本概念。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">親要素の意義を表す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">nomme le concept sous-jacent dont le parent est une
        représentation.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el concepto subyacente cuyo padre es una
        representación.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica un concetto sottostante di cui il genitore
        è una rappesentazione</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef ident="uri" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">uniform resource identifier</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">표준 자원 확인소(URL)</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">identificador de recurso uniforme</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">Identifiant de ressource uniforme.</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">URI (identificatore universale di risorse)</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">references the underlying concept of which the parent is a representation by means of
        some external identifier.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">부모가 외부 확인소를 통해서 표상하는 기저 개념을 지시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">以外部識別符來說明父元素所標記的基本概念</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">外部識別子によって親要素の意義を表す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">référence le concept sous-jacent dont le parent est
        une représentation au moyen d'un identifiant externe quelconque.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">referencia el concepto subyacente del cual padre es
        una representación mediante algún identificador externo</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il concetto sottostante di cui il genitore è
        una rappesentazione attraverso un identificatore esterno</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="filter" usage="opt">
      <desc versionDate="2005-05-22" xml:lang="en">references an external script which contains a method to transform instances of this
        element to canonical TEI.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 요소의 실례를 표준 TEI로 변환하는 방법을 포함하는 외부 스크립트를 참조한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">參照能把該元素實例轉變成標準TEI的外部程式</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素を標準的XMLデータに変形する外部スクリプトへの参照を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">référence un script externe qui contient une méthode
        pour transformer les instances de cet élément en TEI canonique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">referencia un guión externo que contiene un método
        para transformar ejemplos de este elemento a TEI canónico.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica uno script esterno contenente un metodo per
        trasformare le occorrenze dell'elemento in TEI canonico</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <p>The following example declares that the <gi scheme="imaginary">bo</gi> element is
      conceptually equivalent to the markup construct <tag>hi rend='bold'</tag>, and that an
      external definition of this concept is available from the URI indicated</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equiv-egXML-vq">
      <elementSpec ident="hi" mode="change">
        <equiv name="BOLD"/>
        <desc>bold typography</desc>
        <attList>
          <attDef ident="rend" mode="change">
            <valList>
              <valItem ident="bold"/>
            </valList>
          </attDef>
        </attList>
      </elementSpec>
      <elementSpec ident="bo" mode="add">
        <equiv name="BOLD" uri="http://www.example.com/typesetting/bold"/>
      </elementSpec>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">L'exemple suivant déclare que l'élément <gi scheme="imaginary">bo</gi> est conceptuellement
        équivalent au marqueur construit <tag>hi rend='bold'</tag>, et qu'une définition externe de
        ce concept est disponible à l'URI indiqué.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equiv-egXML-hu">
      <elementSpec ident="hi" mode="change">
        <equiv name="BOLD"/>
        <desc>caractères gras</desc>
        <attList>
          <attDef ident="rend" mode="change">
            <valList>
              <valItem ident="bold"/>
            </valList>
          </attDef>
        </attList>
      </elementSpec>
      <elementSpec ident="bo" mode="add">
        <equiv name="BOLD" uri="http://www.example.com/typesetting/bold"/>
      </elementSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equiv-egXML-ao">
      <elementSpec ident="hi" mode="change">
        <equiv name="BOLD"/>
        <desc>粗體印刷</desc>
        <attList>
          <attDef ident="rend" mode="change">
            <valList>
              <valItem ident="bold"/>
            </valList>
          </attDef>
        </attList>
      </elementSpec>
      <elementSpec ident="bo" mode="add">
        <equiv name="BOLD" uri="http://www.example.com/typesetting/bold"/>
      </elementSpec>
    </egXML>
  </exemplum>
  <remarks ident="equiv-remarks" versionDate="2007-06-14" xml:lang="en">
    <p>The <att>mimeType</att> attribute should be used to supply the MIME media type of the filter
      script specified by the <att>filter</att> attribute.</p>
  </remarks>
  <remarks ident="equiv-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>mimeType</att> doit être utilisé pour fournir le type de media MIME du script
      de filtre spécifié par l'attribut <att>filter</att>.</p>
  </remarks>
  <remarks ident="equiv-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>mimeType</att>は、属性<att>filter</att>で示されたスクリプ トファイルのMIMEタイプを示すために使われるべきである。 </p>
  </remarks>
  <listRef>
    <ptr target="#COHTG"/>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">equivalent</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">동치</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">equivalente</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">équivalent</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">equivalente</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies a component which is considered equivalent to the parent element, either by
    co-reference, or by external link.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부모 요소와 동치로 고려되는 성분을 공지시 또는 외부 연결을 통해 명시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">具體指出一個與父元素同等的名稱，無論是藉由交互參照或是外部連結。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">親要素と同等とされる構成要素を、相互参照または外部リンクで示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise un composant considéré comme un équivalent de
    l'élément parent, soit par une référence commune, soit par un lien externe.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica un componente que se considera equivalente al
    elemento padre, o por co-referencias o por algún enlace externo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica un componente considerato equivalente ad un
    elemento genitore sia per co-referenza che tramite link esterno.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.internetMedia"/>
    <memberOf key="att.predicate"/>
    <memberOf key="model.identEquiv"/>
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

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), naming the underlying concept of which the parent is a representation.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부모가 표상하는 기저 개념에 대한 이름을 부여한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明父元素所標記的基本概念。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">親要素の意義を表す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">nomme le concept sous-jacent dont le parent est une
        représentation.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el concepto subyacente cuyo padre es una
        representación.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica un concetto sottostante di cui il genitore
        è una rappesentazione</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">uniform resource identifier</gloss>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">표준 자원 확인소(URL)</gloss>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">identificador de recurso uniforme</gloss>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">Identifiant de ressource uniforme.</gloss>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">URI (identificatore universale di risorse)</gloss>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">references the underlying concept of which the parent is a representation by means of
        some external identifier.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부모가 외부 확인소를 통해서 표상하는 기저 개념을 지시한다.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">以外部識別符來說明父元素所標記的基本概念</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">外部識別子によって親要素の意義を表す。</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">référence le concept sous-jacent dont le parent est
        une représentation au moyen d'un identifiant externe quelconque.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">referencia el concepto subyacente del cual padre es
        una representación mediante algún identificador externo</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il concetto sottostante di cui il genitore è
        una rappesentazione attraverso un identificatore esterno</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-05-22" xml:lang="en">references an external script which contains a method to transform instances of this
        element to canonical TEI.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 요소의 실례를 표준 TEI로 변환하는 방법을 포함하는 외부 스크립트를 참조한다.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">參照能把該元素實例轉變成標準TEI的外部程式</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素を標準的XMLデータに変形する外部スクリプトへの参照を示す。</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">référence un script externe qui contient une méthode
        pour transformer les instances de cet élément en TEI canonique.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">referencia un guión externo que contiene un método
        para transformar ejemplos de este elemento a TEI canónico.</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica uno script esterno contenente un metodo per
        trasformare le occorrenze dell'elemento in TEI canonico</desc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b44

### Block 45

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>The following example declares that the <gi scheme="imaginary">bo</gi> element is
      conceptually equivalent to the markup construct <tag>hi rend='bold'</tag>, and that an
      external definition of this concept is available from the URI indicated</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equiv-egXML-vq">
      <elementSpec ident="hi" mode="change">
        <equiv name="BOLD"/>
        <desc>bold typography</desc>
        <attList>
          <attDef ident="rend" mode="change">
            <valList>
              <valItem ident="bold"/>
            </valList>
          </attDef>
        </attList>
      </elementSpec>
      <elementSpec ident="bo" mode="add">
        <equiv name="BOLD" uri="http://www.example.com/typesetting/bold"/>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b45

### Block 46

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">L'exemple suivant déclare que l'élément <gi scheme="imaginary">bo</gi> est conceptuellement
        équivalent au marqueur construit <tag>hi rend='bold'</tag>, et qu'une définition externe de
        ce concept est disponible à l'URI indiqué.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equiv-egXML-hu">
      <elementSpec ident="hi" mode="change">
        <equiv name="BOLD"/>
        <desc>caractères gras</desc>
        <attList>
          <attDef ident="rend" mode="change">
            <valList>
              <valItem ident="bold"/>
            </valList>
          </attDef>
        </attList>
      </elementSpec>
      <elementSpec ident="bo" mode="add">
        <equiv name="BOLD" uri="http://www.example.com/typesetting/bold"/>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b46

### Block 47

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equiv-egXML-ao">
      <elementSpec ident="hi" mode="change">
        <equiv name="BOLD"/>
        <desc>粗體印刷</desc>
        <attList>
          <attDef ident="rend" mode="change">
            <valList>
              <valItem ident="bold"/>
            </valList>
          </attDef>
        </attList>
      </elementSpec>
      <elementSpec ident="bo" mode="add">
        <equiv name="BOLD" uri="http://www.example.com/typesetting/bold"/>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b47

### Block 48

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="equiv-remarks" versionDate="2007-06-14" xml:lang="en">
    <p>The <att>mimeType</att> attribute should be used to supply the MIME media type of the filter
      script specified by the <att>filter</att> attribute.</p>
  </remarks>
```

^b48

### Block 49

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="equiv-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>mimeType</att> doit être utilisé pour fournir le type de media MIME du script
      de filtre spécifié par l'attribut <att>filter</att>.</p>
  </remarks>
```

^b49

### Block 50

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="equiv-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>mimeType</att>は、属性<att>filter</att>で示されたスクリプ トファイルのMIMEタイプを示すために使われるべきである。 </p>
  </remarks>
```

^b50

### Block 51

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHTG"/>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
```

^b51

