---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.identified-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.identified
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.identified.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.identified

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6605. Git blob: `17c48fae8a7a6e99b1021b95cd2e89988b0f499d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" type="atts" ident="att.identified">
  <desc versionDate="2021-08-22" xml:lang="en">provides identifying attributes for elements which can be subsequently referenced by means of a <att>key</att> attribute.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><att>key</att> 속성에 의해 참조될 수 있는 요소의 속성을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">可利用屬性 <att>key</att>來參照的元素</desc>
  <desc versionDate="2022-05-09" xml:lang="ja">後で<att>key</att>属性によって参照されうる要素を指定する属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit les attributs pour des éléments référençables au moyen d'un attribut <att>key</att>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">elementos a los que se puede hacer referencia a través del atributo <att>key</att>.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">elementi ai quali si può fare riferimento tramite l'attributo <att>key</att></desc>
  <classes>
    <memberOf key="att.combinable"/>
  </classes>
  <constraintSpec ident="spec-in-module" scheme="schematron" xml:lang="en">
    <!--
      The @context below is somewhat complicated, because we do not
      want to test @module attributes that occur in a circumstance
      where the module it refers to is almost certainly defined
      elsewhere, so would not be in this file, anyway. So we test that
      the @module is either
      1) in a file that has at least a <schemaSpec>, if not a <TEI>
         (or <teiCorpus); and
      2) in a file that has at least one <moduleSpec> or <moduleRef>,
         because if there are no <moduleSpec>s nor <moduleRef>s, there
         cannot be one that is refered to by this @module attribute.
      The result of (1) is that we ignore the various sub-files that
      make up P5 (and other similar cases); the result of (2) is that
      we ignore most customization files. The good news is that
      ignoring these cases avoids a lot of false positives; the bad
      news is that quite a few cases of @module will go unchecked by
      this useful test.
    -->
    <constraint>
      <sch:rule context="( tei:elementSpec[@module] | tei:classSpec[@module] | tei:macroSpec[@module] )[                            ( ancestor::tei:schemaSpec | ancestor::tei:TEI | ancestor::tei:teiCorpus )                            and                            ( //tei:moduleSpec | //tei:moduleRef )                            ]">
        <sch:assert test="( //tei:moduleSpec/@ident | //tei:moduleRef/@key ) = @module">
          Specification <sch:value-of select="@ident"/>: the value of the module attribute
          ("<sch:value-of select="@module"/>") should correspond to an existing module, via
          a moduleSpec or moduleRef.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="ident" usage="req">
      <desc versionDate="2012-12-27" xml:lang="en">supplies the identifier by which this element may be referenced.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 요소가 참조된 확인소를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供被參照的元素的識別符號。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素を参照する識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant qui référence cet élément.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador utilizado para indicar un elemento.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica l'identificatore utilizzato per indicare l'elemento.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef ident="predeclare" usage="opt">
      <desc versionDate="2012-12-27" xml:lang="en">says whether this object should be predeclared in the
      <ident type="module">tei</ident> infrastructure module.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"><ident type="module">tei</ident> 하부구조 모듈에서 이 대상이 미리 선언되어야 하는지를 설명한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該元素集是否為全域元素集，並必須在核心中宣告。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該オブジェクトが、<ident type="module">TEI</ident>基盤モジュー ルで事前に宣言されるべきかどうかを示す。</desc>
      <desc versionDate="2009-05-27" xml:lang="fr">précise si cet objet nécessite une prédéfinition dans le module d'infrastructure <ident type="module">tei</ident>.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">declara si la clase debe ser considerada global y por tanto definida en el módulo core</desc>
      <desc versionDate="2007-01-21" xml:lang="it">dichiara se la classe debba essere considerata globale e quindi definita nel modulo core.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
      <defaultVal>false</defaultVal>
    </attDef>
    <attDef ident="module" usage="opt">
      <desc versionDate="2012-12-27" xml:lang="en">supplies a name for the module in which this object is to be declared.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 대상이 정의되어야 하는 모듈명을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供定義該元素的模組名稱。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該オブジェクトが定義されているモジュール名を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit le nom du module dans lequel doit être défini cet objet.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del módulo en que el objeto debe ser definido.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il nome del modulo nel quale l'oggetto deve essere definito.</desc>
      <datatype><dataRef key="teidata.xmlName"/></datatype>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides identifying attributes for elements which can be subsequently referenced by means of a <att>key</att> attribute.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><att>key</att> 속성에 의해 참조될 수 있는 요소의 속성을 제시한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">可利用屬性 <att>key</att>來參照的元素</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">後で<att>key</att>属性によって参照されうる要素を指定する属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit les attributs pour des éléments référençables au moyen d'un attribut <att>key</att>.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">elementos a los que se puede hacer referencia a través del atributo <att>key</att>.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">elementi ai quali si può fare riferimento tramite l'attributo <att>key</att></desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.combinable"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="spec-in-module" scheme="schematron" xml:lang="en">
    <!--
      The @context below is somewhat complicated, because we do not
      want to test @module attributes that occur in a circumstance
      where the module it refers to is almost certainly defined
      elsewhere, so would not be in this file, anyway. So we test that
      the @module is either
      1) in a file that has at least a <schemaSpec>, if not a <TEI>
         (or <teiCorpus); and
      2) in a file that has at least one <moduleSpec> or <moduleRef>,
         because if there are no <moduleSpec>s nor <moduleRef>s, there
         cannot be one that is refered to by this @module attribute.
      The result of (1) is that we ignore the various sub-files that
      make up P5 (and other similar cases); the result of (2) is that
      we ignore most customization files. The good news is that
      ignoring these cases avoids a lot of false positives; the bad
      news is that quite a few cases of @module will go unchecked by
      this useful test.
    -->
    <constraint>
      <sch:rule context="( tei:elementSpec[@module] | tei:classSpec[@module] | tei:macroSpec[@module] )[                            ( ancestor::tei:schemaSpec | ancestor::tei:TEI | ancestor::tei:teiCorpus )                            and                            ( //tei:moduleSpec | //tei:moduleRef )                            ]">
        <sch:assert test="( //tei:moduleSpec/@ident | //tei:moduleRef/@key ) = @module">
          Specification <sch:value-of select="@ident"/>: the value of the module attribute
          ("<sch:value-of select="@module"/>") should correspond to an existing module, via
          a moduleSpec or moduleRef.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">supplies the identifier by which this element may be referenced.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 요소가 참조된 확인소를 제공한다.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供被參照的元素的識別符號。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素を参照する識別子を示す。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant qui référence cet élément.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el identificador utilizado para indicar un elemento.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica l'identificatore utilizzato per indicare l'elemento.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">says whether this object should be predeclared in the
      <ident type="module">tei</ident> infrastructure module.</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><ident type="module">tei</ident> 하부구조 모듈에서 이 대상이 미리 선언되어야 하는지를 설명한다.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該元素集是否為全域元素集，並必須在核心中宣告。</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該オブジェクトが、<ident type="module">TEI</ident>基盤モジュー ルで事前に宣言されるべきかどうかを示す。</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">précise si cet objet nécessite une prédéfinition dans le module d'infrastructure <ident type="module">tei</ident>.</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">declara si la clase debe ser considerada global y por tanto definida en el módulo core</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">dichiara se la classe debba essere considerata globale e quindi definita nel modulo core.</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>false</defaultVal>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">supplies a name for the module in which this object is to be declared.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 대상이 정의되어야 하는 모듈명을 제시한다.</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供定義該元素的模組名稱。</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該オブジェクトが定義されているモジュール名を示す。</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit le nom du module dans lequel doit être défini cet objet.</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del módulo en que el objeto debe ser definido.</desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il nome del modulo nel quale l'oggetto deve essere definito.</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b34

