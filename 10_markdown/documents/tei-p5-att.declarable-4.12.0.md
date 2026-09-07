---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.declarable-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.declarable
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.declarable.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.declarable

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8967. Git blob: `84dd11ef9b37b4c04148c57babc9440099720106`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tei" xml:id="DECLABL" type="atts" ident="att.declarable">
  <desc versionDate="2013-02-02" xml:lang="en">provides attributes for those elements in the TEI header which
  may be independently selected by means of  the special purpose <att>decls</att> attribute.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">특별한 목적의 <att>decls</att> 속성을 통해서 독립적으로 선택될 수 있는 TEI 헤더의 요소에 대한 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，用於TEI標頭內可單獨以特殊目的的屬性<att>decls</att>選出的元素。</desc>
  <desc versionDate="2019-05-20" xml:lang="ja">特別な目的の<att>decls</att>属性を用いて独自に選択できるTEIヘッダー内の要素の属性を提供する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour ces éléments de
      l'en-tête TEI qui peuvent être choisis indépendamment au moyen de l'attribut
      <att>decls</att>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para los elementos contenidos en el encabezado que pueden ser seleccionados autónomamente mediante el atributo <att>decls</att> adecuado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">individua attributi per gli elementi contenuti nell'intestazione che possono essere selezionati autonomamente grazie all'apposito attributo <att>decls</att></desc>
  <!-- BEGIN patch for #2750: -->
  <!--
      This entire block (a single <constraintSpec> element) commented
      out 2025-08-26 in response to issue #2750. Whether it will be
      deleted, modified and returned to action, or put back on the
      front lines unmodified will be decided in the future. For now it
      is being removed because it flags constructs as erroneous that
      Council feels a reasonable user would expect to be valid.
  -->
  <!-- <constraintSpec ident="att-declarable" scheme="schematron" xml:lang="en"> -->
  <!--   <constraint> -->
  <!--     <sch:pattern id="declarable" abstract="true"> -->
  <!--       <!-\- parameter 'tde' is for "this declarable element (type)" -\-> -->
  <!--       <sch:rule context="$tde[ ancestor::tei:teiHeader -->
  <!--                                and -->
  <!--                                following-sibling::$tde -->
  <!--                                and -->
  <!--                                not( preceding-sibling::$tde ) ]"> -->
  <!--         <sch:report test="../child::$tde[ not( @xml:id ) ]"> -->
  <!--           When there is more than one <sch:name/>, each must have an @xml:id -->
  <!--         </sch:report> -->
  <!--         <sch:assert test="count( ../child::$tde[ normalize-space( @default ) = ('1','true') ] ) eq 1"> -->
  <!--           When there is more than one <sch:name/>, one and only one must have a @default of 'true'. -->
  <!--         </sch:assert> -->
  <!--       </sch:rule> -->
  <!--     </sch:pattern> -->
  <!--   </constraint> -->
  <!-- </constraintSpec> -->
  <!-- END patch for #2750 -->
  <attList>
    <attDef ident="default" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">indicates whether or not this element is selected by default when
its parent is selected.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">그 부모가 선택될 때 기본값으로 이 요소가 선택되었는지를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">當父元素被選擇時，指出此元素是否會被選擇。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">親要素が選択された場合に、当該要素がデフォルトとして選択されるか
      どうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si oui ou non cet élément est affecté par
          défaut quand son élément parent a été sélectionné.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el elemento es seleccionado automáticamente o no  cuando es seleccionado el padre</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se l'elemento è selezionato automaticamente quando è selezionato il genitore.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
      <defaultVal>false</defaultVal>
      <valList type="closed">
        <valItem ident="true">
          <desc versionDate="2007-06-27" xml:lang="en">This element is selected if its parent is selected</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">그 부모가 선택된다면 이 요소가 선택된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">若父元素被選擇，則此元素會被選擇。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Este elemento se selecciona si sus padres son seleccionados</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">親要素が選択された場合、当該要素が選択される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément est choisi si son parent
est choisi</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è selezionato se è selezionato il genitore.</desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2007-06-27" xml:lang="en">This element can only be selected explicitly, unless it is the
only one of its kind, in which case it is selected if its parent is selected.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이런 유형 중 유일한 경우가 아니라면, 이 요소는 명시적으로만 선택될 수 있다. 유일한 경우에는, 그 부모가 선택된다면 이 요소가 선택된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素僅能被明確選擇，若此元素為其類別中之唯一，則父元素被選擇時，此元素會被選擇。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Este elemento sólo se puede seleccionar explícitamente, a menos que sea el único de su clase, en este caso se selecciona si su padre es seleccionado.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素は、明示的にのみ選択される。または、親要素が選択され、
          これが唯一の選択肢であるときのみに、これは選択される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément ne peut être sélectionné
qu'explicitement, à moins qu'il ne soit le seul de ce type, auquel cas
il est sélectionné si son parent a été choisi</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento deve essere esplicitamente selezionato, a meno che non sia l'unico del suo genere, nel qual caso è selezionato se è selezionato il genitore.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <remarks ident="att.declarable-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>The rules governing the association of declarable elements with
    individual parts of a TEI text are fully defined in chapter <ptr target="#CCAS"/>. Only one element of a particular type may have a
    <att>default</att> attribute with a value of <val>true</val>.</p>
  </remarks>
  <remarks ident="att.declarable-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les règles régissant l'association d'éléments déclarables avec des parties
                individuelles d'un texte TEI sont entièrement définies
                au chap1itre <ptr target="#CCAS"/>. Un seul élément
                d'un type particulier peut avoir un attribut <att>default</att> avec une valeur
                    <val>true</val>.</p>
  </remarks>
  <remarks ident="att.declarable-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Las reglas que gobiernan la asociación de los elementos declarables con las partes individuales de un texto de TEI se definen completamente en el capítulo <ptr target="#CCAS"/>. Solamente un elemento de un tipo determinado puede tener algún atributo de <att>default</att> con un valor de <val>verdad</val>.</p>
  </remarks>
  <remarks ident="att.declarable-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    このような選択可能要素の関連性を決める規則は、
    <ptr target="#CCAS"/>において詳しく規定されている。
    属性値<val>true</val>をとるのは、ひとつの要素だけである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#CCAS"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-02-02" xml:lang="en">provides attributes for those elements in the TEI header which
  may be independently selected by means of  the special purpose <att>decls</att> attribute.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">특별한 목적의 <att>decls</att> 속성을 통해서 독립적으로 선택될 수 있는 TEI 헤더의 요소에 대한 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，用於TEI標頭內可單獨以特殊目的的屬性<att>decls</att>選出的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2019-05-20" xml:lang="ja">特別な目的の<att>decls</att>属性を用いて独自に選択できるTEIヘッダー内の要素の属性を提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour ces éléments de
      l'en-tête TEI qui peuvent être choisis indépendamment au moyen de l'attribut
      <att>decls</att>.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para los elementos contenidos en el encabezado que pueden ser seleccionados autónomamente mediante el atributo <att>decls</att> adecuado.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">individua attributi per gli elementi contenuti nell'intestazione che possono essere selezionati autonomamente grazie all'apposito attributo <att>decls</att></desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates whether or not this element is selected by default when
its parent is selected.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그 부모가 선택될 때 기본값으로 이 요소가 선택되었는지를 표시한다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">當父元素被選擇時，指出此元素是否會被選擇。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">親要素が選択された場合に、当該要素がデフォルトとして選択されるか
      どうかを示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si oui ou non cet élément est affecté par
          défaut quand son élément parent a été sélectionné.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el elemento es seleccionado automáticamente o no  cuando es seleccionado el padre</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se l'elemento è selezionato automaticamente quando è selezionato il genitore.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>false</defaultVal>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="true">
          <desc versionDate="2007-06-27" xml:lang="en">This element is selected if its parent is selected</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">그 부모가 선택된다면 이 요소가 선택된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">若父元素被選擇，則此元素會被選擇。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Este elemento se selecciona si sus padres son seleccionados</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">親要素が選択された場合、当該要素が選択される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément est choisi si son parent
est choisi</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è selezionato se è selezionato il genitore.</desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2007-06-27" xml:lang="en">This element can only be selected explicitly, unless it is the
only one of its kind, in which case it is selected if its parent is selected.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이런 유형 중 유일한 경우가 아니라면, 이 요소는 명시적으로만 선택될 수 있다. 유일한 경우에는, 그 부모가 선택된다면 이 요소가 선택된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素僅能被明確選擇，若此元素為其類別中之唯一，則父元素被選擇時，此元素會被選擇。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Este elemento sólo se puede seleccionar explícitamente, a menos que sea el único de su clase, en este caso se selecciona si su padre es seleccionado.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素は、明示的にのみ選択される。または、親要素が選択され、
          これが唯一の選択肢であるときのみに、これは選択される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément ne peut être sélectionné
qu'explicitement, à moins qu'il ne soit le seul de ce type, auquel cas
il est sélectionné si son parent a été choisi</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento deve essere esplicitamente selezionato, a meno che non sia l'unico del suo genere, nel qual caso è selezionato se è selezionato il genitore.</desc>
        </valItem>
      </valList>
```

^b17

### Block 18

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.declarable-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>The rules governing the association of declarable elements with
    individual parts of a TEI text are fully defined in chapter <ptr target="#CCAS"/>. Only one element of a particular type may have a
    <att>default</att> attribute with a value of <val>true</val>.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.declarable-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les règles régissant l'association d'éléments déclarables avec des parties
                individuelles d'un texte TEI sont entièrement définies
                au chap1itre <ptr target="#CCAS"/>. Un seul élément
                d'un type particulier peut avoir un attribut <att>default</att> avec une valeur
                    <val>true</val>.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.declarable-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Las reglas que gobiernan la asociación de los elementos declarables con las partes individuales de un texto de TEI se definen completamente en el capítulo <ptr target="#CCAS"/>. Solamente un elemento de un tipo determinado puede tener algún atributo de <att>default</att> con un valor de <val>verdad</val>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="att.declarable-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    このような選択可能要素の関連性を決める規則は、
    <ptr target="#CCAS"/>において詳しく規定されている。
    属性値<val>true</val>をとるのは、ひとつの要素だけである。
    </p>
  </remarks>
```

^b21

### Block 22

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAS"/>
  </listRef>
```

^b22

