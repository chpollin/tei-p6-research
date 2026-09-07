---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.pointing.group-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.pointing.group
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.pointing.group.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.pointing.group

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9105. Git blob: `660c7a6d520bd20c0005f64aeb78f134c5f106bd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" ident="att.pointing.group">
  <desc versionDate="2016-02-15" xml:lang="en">provides a set of attributes common to all elements which
  enclose groups of pointer elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">포인터 요소군을 포함하는 모든 요소에 공통적인 속성 집합을 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一組屬性，通用於所有包含指標元素群組的元素。</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">ポインター要素をグループ化する、すべての要素に共通の属性セットを提供する。</desc>
  <desc versionDate="2016-02-15" xml:lang="fr">fournit un ensemble d'attributs communs à tous les éléments qui contiennent des groupes d'éléments pointeurs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define un conjunto de atributos comunes a todos los elementos que incluyen grupos de indicadores.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi comuni a tutti gli elementi che includono gruppi di puntatori.</desc>
  <classes>
    
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
  </classes>
  <attList>
    <attDef ident="domains" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">optionally specifies the identifiers of the elements
      within which all elements indicated by the contents of this
      element lie.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 요소 내용에 의해 지시된 모든 요소에 대한 확인소를 수의적으로 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明元素的識別符碼 (但非必備) ，此元素內容所指明的元素皆包含於這些元素當中。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素の中にある全要素を対象とした識別子を選択的に指定する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie, facultativement, les identifiants des éléments englobant tous les éléments indiqués par le contenu de cet élément.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">establece facultativamente los identificadores de elementos al interno de los cuales se encuentran todos los elementos indicados de los contenidos del elemento en cuestión.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">stabilisce facoltativamente gli identificatori di elementi all'interno dei quali si trovano tutti gli elementi indicati dai contenuti dell'elemento in questione.</desc>
      <datatype minOccurs="2" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.pointing.group-attr.domains-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>If this attribute is supplied every element specified as a
	target must be contained within the element or elements
	named by it. An application may choose whether or not to
	report failures to satisfy this constraint as errors, but may
	not access an element of the right identifier but in the wrong
	context. If this attribute is not supplied, then target
	elements may appear anywhere within the target document.</p>
      </remarks>
      <remarks ident="att.pointing.group-attr.domains-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si cet attribut est utilisé, tout élément spécifié comme étant une cible doit
                        être contenu dans l'élément ou les éléments qu'il nomme. Une application
                        peut choisir de faire apparaître en erreur, ou non, les entorses à cette
                        contrainte mais ne peut pas accéder à un élément qui aurait le bon
                        identifiant mais se trouverait dans le mauvais contexte. Si cet attribut
                        n'est pas utilisé, les éléments cibles peuvent apparaître n'importe où dans
                        le document cible.</p>
      </remarks>
      <remarks ident="att.pointing.group-attr.domains-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
          当該属性が付与されている場合、参照先の要素は全て、当該要素または参照先の要素中になければならない。ソフトウェアは、この制約に違反した場合にエラーを返すかどうかを選択できるかもしれないが、識別子は正しくとも間違った文脈にある要素にはアクセスできないかもしれない。当該属性が付与されていない場合、参照先の要素は、参照された文書中のどこにあってもよい。
	</p>
      </remarks>
    </attDef>
    <attDef ident="targFunc" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">target function</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">대상 기능</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">función meta</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">fonction cible</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">funzione obiettivo</gloss>
      <gloss versionDate="2024-08-08" xml:lang="ja">ターゲットの機能</gloss>
      <desc versionDate="2011-07-25" xml:lang="en">describes the function of each of the values of the
      <att>target</att> attribute of the enclosed <gi>link</gi>,
      <gi>join</gi>, or <gi>alt</gi> tags.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"><gi>link</gi>, <gi>join</gi> 또는 <gi>alt</gi> 태그의  속성 값 각각에 대한 기능을 기술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">描述每個元素標籤<gi>link</gi>、<gi>join</gi>、或<gi>alt</gi>當中的屬性<att>target</att>的屬性值功能。</desc>
      <desc versionDate="2024-08-08" xml:lang="ja">この属性を有する要素がグループ化する<gi>link</gi>や<gi>join</gi>、<gi>alt</gi>自体がもっている<att>target</att>属性のそれぞれの値の機能を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">décrit la fonction de chacune des valeurs de
          l'attribut <att>target</att> pour les balises incluses <gi>link</gi>, <gi>join</gi>, ou
          <gi>alt</gi>.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">describe la función de cada uno de los valores del atributo <att>target</att> (metas) de los marcadores correspondientes <gi>link</gi>, <gi>join</gi>, o <gi>alt</gi>.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">descrive la funzione di ognuno dei valori dell'attributo <att>target</att> dei marcatori corrispondenti <gi>link</gi>,
      <gi>join</gi>, o <gi>alt</gi></desc>
      <datatype minOccurs="2" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
      <remarks ident="att.pointing.group-attr.targFunc-remarks" versionDate="2011-07-25" xml:lang="en">
        <p>The number of separate values must match the number of
        values in the <att>target</att> attribute in the enclosed
        <gi>link</gi>, <gi>join</gi>, or <gi>alt</gi> tags (an
        intermediate <gi>ptr</gi> element may be needed to accomplish
        this). It should also match the number of values in the
        <att>domains</att> attribute, of the current element, if one
        has been specified.</p>
      </remarks>
      <remarks ident="att.pointing.group-attr.targFunc-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Le nombre de valeurs distinctes doit correspondre au nombre de valeurs dans
                        l'attribut <att>target</att> des balises incluses <gi>link</gi>,
                        <gi>join</gi> ou <gi>alt</gi> (un élément intermédiaire <gi>ptr</gi> peut
                        être nécessaire dans ce cas). Il devrait également correspondre au nombre de
                        valeurs se trouvant dans l'attribut <att>domains</att> de l'élément en
                        question, si un tel attribut a été spécifié.</p>
      </remarks>
      <remarks ident="att.pointing.group-attr.targFunc-remarks" versionDate="2023-09-27" xml:lang="ja">
        <p>
          この値で指定される値の数は、<gi>link</gi>, <gi>join</gi>, あるいは<gi>alt</gi>に含まれる<att>target</att>属性における値の数と一致しなければならない（仲立ちをする<gi>ptr</gi>要素がこのために必要かもしれない）。もし同じ要素に<att>domains</att>属性が付与されているならば、その値の数とも一致させるべきである。
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
<desc versionDate="2016-02-15" xml:lang="en">provides a set of attributes common to all elements which
  enclose groups of pointer elements.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">포인터 요소군을 포함하는 모든 요소에 공통적인 속성 집합을 정의한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一組屬性，通用於所有包含指標元素群組的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">ポインター要素をグループ化する、すべての要素に共通の属性セットを提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2016-02-15" xml:lang="fr">fournit un ensemble d'attributs communs à tous les éléments qui contiennent des groupes d'éléments pointeurs.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define un conjunto de atributos comunes a todos los elementos que incluyen grupos de indicadores.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi comuni a tutti gli elementi che includono gruppi di puntatori.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">optionally specifies the identifiers of the elements
      within which all elements indicated by the contents of this
      element lie.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 요소 내용에 의해 지시된 모든 요소에 대한 확인소를 수의적으로 명시한다.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明元素的識別符碼 (但非必備) ，此元素內容所指明的元素皆包含於這些元素當中。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素の中にある全要素を対象とした識別子を選択的に指定する。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie, facultativement, les identifiants des éléments englobant tous les éléments indiqués par le contenu de cet élément.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">establece facultativamente los identificadores de elementos al interno de los cuales se encuentran todos los elementos indicados de los contenidos del elemento en cuestión.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">stabilisce facoltativamente gli identificatori di elementi all'interno dei quali si trovano tutti gli elementi indicati dai contenuti dell'elemento in questione.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="2" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.pointing.group-attr.domains-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>If this attribute is supplied every element specified as a
	target must be contained within the element or elements
	named by it. An application may choose whether or not to
	report failures to satisfy this constraint as errors, but may
	not access an element of the right identifier but in the wrong
	context. If this attribute is not supplied, then target
	elements may appear anywhere within the target document.</p>
      </remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.pointing.group-attr.domains-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si cet attribut est utilisé, tout élément spécifié comme étant une cible doit
                        être contenu dans l'élément ou les éléments qu'il nomme. Une application
                        peut choisir de faire apparaître en erreur, ou non, les entorses à cette
                        contrainte mais ne peut pas accéder à un élément qui aurait le bon
                        identifiant mais se trouverait dans le mauvais contexte. Si cet attribut
                        n'est pas utilisé, les éléments cibles peuvent apparaître n'importe où dans
                        le document cible.</p>
      </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.pointing.group-attr.domains-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
          当該属性が付与されている場合、参照先の要素は全て、当該要素または参照先の要素中になければならない。ソフトウェアは、この制約に違反した場合にエラーを返すかどうかを選択できるかもしれないが、識別子は正しくとも間違った文脈にある要素にはアクセスできないかもしれない。当該属性が付与されていない場合、参照先の要素は、参照された文書中のどこにあってもよい。
	</p>
      </remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">target function</gloss>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">대상 기능</gloss>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">función meta</gloss>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">fonction cible</gloss>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">funzione obiettivo</gloss>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[6]`.

```xml
<gloss versionDate="2024-08-08" xml:lang="ja">ターゲットの機能</gloss>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2011-07-25" xml:lang="en">describes the function of each of the values of the
      <att>target</att> attribute of the enclosed <gi>link</gi>,
      <gi>join</gi>, or <gi>alt</gi> tags.</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><gi>link</gi>, <gi>join</gi> 또는 <gi>alt</gi> 태그의  속성 값 각각에 대한 기능을 기술한다.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述每個元素標籤<gi>link</gi>、<gi>join</gi>、或<gi>alt</gi>當中的屬性<att>target</att>的屬性值功能。</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">この属性を有する要素がグループ化する<gi>link</gi>や<gi>join</gi>、<gi>alt</gi>自体がもっている<att>target</att>属性のそれぞれの値の機能を示す。</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit la fonction de chacune des valeurs de
          l'attribut <att>target</att> pour les balises incluses <gi>link</gi>, <gi>join</gi>, ou
          <gi>alt</gi>.</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la función de cada uno de los valores del atributo <att>target</att> (metas) de los marcadores correspondientes <gi>link</gi>, <gi>join</gi>, o <gi>alt</gi>.</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive la funzione di ognuno dei valori dell'attributo <att>target</att> dei marcatori corrispondenti <gi>link</gi>,
      <gi>join</gi>, o <gi>alt</gi></desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="2" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.pointing.group-attr.targFunc-remarks" versionDate="2011-07-25" xml:lang="en">
        <p>The number of separate values must match the number of
        values in the <att>target</att> attribute in the enclosed
        <gi>link</gi>, <gi>join</gi>, or <gi>alt</gi> tags (an
        intermediate <gi>ptr</gi> element may be needed to accomplish
        this). It should also match the number of values in the
        <att>domains</att> attribute, of the current element, if one
        has been specified.</p>
      </remarks>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="att.pointing.group-attr.targFunc-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Le nombre de valeurs distinctes doit correspondre au nombre de valeurs dans
                        l'attribut <att>target</att> des balises incluses <gi>link</gi>,
                        <gi>join</gi> ou <gi>alt</gi> (un élément intermédiaire <gi>ptr</gi> peut
                        être nécessaire dans ce cas). Il devrait également correspondre au nombre de
                        valeurs se trouvant dans l'attribut <att>domains</att> de l'élément en
                        question, si un tel attribut a été spécifié.</p>
      </remarks>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="att.pointing.group-attr.targFunc-remarks" versionDate="2023-09-27" xml:lang="ja">
        <p>
          この値で指定される値の数は、<gi>link</gi>, <gi>join</gi>, あるいは<gi>alt</gi>に含まれる<att>target</att>属性における値の数と一致しなければならない（仲立ちをする<gi>ptr</gi>要素がこのために必要かもしれない）。もし同じ要素に<att>domains</att>属性が付与されているならば、その値の数とも一致させるべきである。
    </p>
      </remarks>
```

^b36

### Block 37

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SA"/>
  </listRef>
```

^b37

