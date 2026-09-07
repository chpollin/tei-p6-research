---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.typed-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.typed
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.typed.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.typed

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7452. Git blob: `73f39bde141f71d2319fecc3a521fc245dd9c0ab`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tei" xml:id="TYPED" type="atts" ident="att.typed" predeclare="true">
  <desc versionDate="2007-10-02" xml:lang="en">provides attributes that can be used to classify or subclassify elements in any way.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">요소의 분류 또는 하위분류에서 사용될 수 있는 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供可依任何方法將元素分類或次要分類的一般屬性。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素を分類するための属性を示す。</desc>
  <desc versionDate="2009-05-29" xml:lang="fr">fournit des attributs qui peuvent être utilisés pour classer ou interclasser des éléments de n'importe quelle façon.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos genéricos utilizables para cualquier clasificación o subclasificación de elementos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi generici utilizzabili per qualsiasi classificazione e sottoclassificazione di elementi.</desc>
  <constraintSpec scheme="schematron" ident="subtypeTyped" xml:lang="en">
    <constraint>
      <sch:rule context="tei:*[@subtype]">
        <sch:assert test="@type">
          The &lt;<sch:name/>&gt; element should not be categorized in detail with @subtype unless also categorized in general with @type.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="type" usage="opt">
      <!-- Any time changes are made to this @type attribute, you should change the definitions in att.entryLike 
           and att.textCritical if needed for consistency.
       -->
      <desc versionDate="2005-10-10" xml:lang="en">characterizes the element in some sense, using any convenient classification scheme or typology.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">다양한 분류 스키마 또는 유형을 사용해서 요소의 특성을 기술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類標準或類型來描述該元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素の分類を示す。</desc>
      <desc versionDate="2009-05-29" xml:lang="fr">caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">caracteriza el elemento utilizando una clasificación o tipología funcional.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">caratterizza l'elemento utilizzando una classificazione o tipologia funzionale.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TYPED-egXML-vd" source="#NZETC01" xml:lang="en">
          <div type="verse">
            <head>Night in Tarras</head>
            <lg type="stanza">
              <l>At evening tramping on the hot white road</l>
              <l>…</l>
            </lg>
            <lg type="stanza">
              <l>A wind sprang up from nowhere as the sky</l>
              <l>…</l>
            </lg>
          </div>
        </egXML>
      </exemplum>
      <remarks ident="att.typed-attr.type-remarks" versionDate="2012-04-21" xml:lang="en">
        <p>The <att>type</att> attribute is present on a number of
        elements, not all of which are members of <ident type="class">att.typed</ident>, usually because these elements
        restrict the possible values for the attribute in a specific way.</p>
      </remarks>
    </attDef>
    <attDef ident="subtype" usage="opt">
      <gloss versionDate="2009-05-29" xml:lang="en">subtype</gloss>
      <gloss versionDate="2009-05-29" xml:lang="fr">sous-type</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">provides a sub-categorization of the element, if needed.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">필요하다면 요소의 하위범주를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">若有需要，提供該元素的次要分類</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">必要であれば、当該要素の下位分類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit une sous-catégorisation de l'élément, si c'est nécessaire.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona, si es necesario, una subcategorización del elemento.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">stabilisce, se necessario, una sottocategorizzazione dell'elemento.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="att.typed-attr.subtype-remarks" versionDate="2013-01-13" xml:lang="en">
        <p>The <att>subtype</att> attribute may be used to provide any
sub-classification for the element additional to that provided by its
<att>type</att> attribute.</p>
      </remarks>
      <remarks ident="att.typed-attr.subtype-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'attribut <att>subtype</att> peut être employé pour fournir une
                        sous-classification pour cet élément, en plus de celle fournie par son
                        propre attribut <att>type</att>.</p>
      </remarks>
      <remarks ident="att.typed-attr.subtype-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El atributo <att>subtype</att> (subtipo) se puede utilizar para proporcionar cualquier subclasificación para el elemento, adicional a ésa proporcionada por su
<att>type</att> (tipo) de atributo.</p>
      </remarks>
      <remarks ident="att.typed-attr.subtype-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性<att>subtype</att>は、属性<att>type</att>に加えて、当該要
    素の下位分類を示すために使われる。
    </p>
      </remarks>
    </attDef>
  </attList>
  <remarks ident="att.typed-remarks" versionDate="2012-04-21" xml:lang="en">
    <p>When appropriate, values from an established typology should be
    used. Alternatively a typology may be defined in the associated
    TEI header. If values are to be taken from a project-specific
    list, this should be defined using the <gi>valList</gi> element in
    the project-specific schema description, as described in <ptr target="#MDMDAL"/> .</p>
  </remarks>
  <listRef>
    <ptr target="#STECAT"/>
    <ptr target="#AILCW"/>
    <ptr target="#CONARS"/>
    <ptr target="#COXR"/>
    <ptr target="#CONAAB"/>
    <ptr target="#COVE"/>
    <ptr target="#DRPAL"/>
    <ptr target="#DSDIV1"/>
    <ptr target="#DSDIV2"/>
    <ptr target="#DSHD"/>
    <ptr target="#DSVIRT"/>
    <ptr target="#NDPERSREL"/>
    <ptr target="#PHCO"/>
    <ptr target="#SAPTL"/>
    <ptr target="#SASE"/>
    <ptr target="#TCAPLK"/>
    <ptr target="#TDTAGCONT"/>
    <ptr target="#TSBA"/>
    <ptr target="#MDMDAL"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-02" xml:lang="en">provides attributes that can be used to classify or subclassify elements in any way.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소의 분류 또는 하위분류에서 사용될 수 있는 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供可依任何方法將元素分類或次要分類的一般屬性。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素を分類するための属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-29" xml:lang="fr">fournit des attributs qui peuvent être utilisés pour classer ou interclasser des éléments de n'importe quelle façon.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos genéricos utilizables para cualquier clasificación o subclasificación de elementos.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi generici utilizzabili per qualsiasi classificazione e sottoclassificazione di elementi.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="subtypeTyped" xml:lang="en">
    <constraint>
      <sch:rule context="tei:*[@subtype]">
        <sch:assert test="@type">
          The &lt;<sch:name/>&gt; element should not be categorized in detail with @subtype unless also categorized in general with @type.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">characterizes the element in some sense, using any convenient classification scheme or typology.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다양한 분류 스키마 또는 유형을 사용해서 요소의 특성을 기술한다.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類標準或類型來描述該元素。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素の分類を示す。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-05-29" xml:lang="fr">caractérise l'élément en utilisant n'importe quel système ou typologie de classification approprié.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">caracteriza el elemento utilizando una clasificación o tipología funcional.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">caratterizza l'elemento utilizzando una classificazione o tipologia funzionale.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TYPED-egXML-vd" source="#NZETC01" xml:lang="en">
          <div type="verse">
            <head>Night in Tarras</head>
            <lg type="stanza">
              <l>At evening tramping on the hot white road</l>
              <l>…</l>
            </lg>
            <lg type="stanza">
              <l>A wind sprang up from nowhere as the sky</l>
              <l>…</l>
            </lg>
          </div>
        </egXML>
      </exemplum>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.typed-attr.type-remarks" versionDate="2012-04-21" xml:lang="en">
        <p>The <att>type</att> attribute is present on a number of
        elements, not all of which are members of <ident type="class">att.typed</ident>, usually because these elements
        restrict the possible values for the attribute in a specific way.</p>
      </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2009-05-29" xml:lang="en">subtype</gloss>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2009-05-29" xml:lang="fr">sous-type</gloss>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">provides a sub-categorization of the element, if needed.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">필요하다면 요소의 하위범주를 제시한다.</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">若有需要，提供該元素的次要分類</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">必要であれば、当該要素の下位分類を示す。</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit une sous-catégorisation de l'élément, si c'est nécessaire.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona, si es necesario, una subcategorización del elemento.</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">stabilisce, se necessario, una sottocategorizzazione dell'elemento.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.typed-attr.subtype-remarks" versionDate="2013-01-13" xml:lang="en">
        <p>The <att>subtype</att> attribute may be used to provide any
sub-classification for the element additional to that provided by its
<att>type</att> attribute.</p>
      </remarks>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="att.typed-attr.subtype-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'attribut <att>subtype</att> peut être employé pour fournir une
                        sous-classification pour cet élément, en plus de celle fournie par son
                        propre attribut <att>type</att>.</p>
      </remarks>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="att.typed-attr.subtype-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El atributo <att>subtype</att> (subtipo) se puede utilizar para proporcionar cualquier subclasificación para el elemento, adicional a ésa proporcionada por su
<att>type</att> (tipo) de atributo.</p>
      </remarks>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="att.typed-attr.subtype-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性<att>subtype</att>は、属性<att>type</att>に加えて、当該要
    素の下位分類を示すために使われる。
    </p>
      </remarks>
```

^b32

### Block 33

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.typed-remarks" versionDate="2012-04-21" xml:lang="en">
    <p>When appropriate, values from an established typology should be
    used. Alternatively a typology may be defined in the associated
    TEI header. If values are to be taken from a project-specific
    list, this should be defined using the <gi>valList</gi> element in
    the project-specific schema description, as described in <ptr target="#MDMDAL"/> .</p>
  </remarks>
```

^b33

### Block 34

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STECAT"/>
    <ptr target="#AILCW"/>
    <ptr target="#CONARS"/>
    <ptr target="#COXR"/>
    <ptr target="#CONAAB"/>
    <ptr target="#COVE"/>
    <ptr target="#DRPAL"/>
    <ptr target="#DSDIV1"/>
    <ptr target="#DSDIV2"/>
    <ptr target="#DSHD"/>
    <ptr target="#DSVIRT"/>
    <ptr target="#NDPERSREL"/>
    <ptr target="#PHCO"/>
    <ptr target="#SAPTL"/>
    <ptr target="#SASE"/>
    <ptr target="#TCAPLK"/>
    <ptr target="#TDTAGCONT"/>
    <ptr target="#TSBA"/>
    <ptr target="#MDMDAL"/>
  </listRef>
```

^b34

