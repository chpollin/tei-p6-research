---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.personal-4.12.0.xml]]'
converter: tools.ingest_git_blobs v2; complete XML plus XML itertext English reading
  blocks with whitespace normalized and identified locators
channel: collection
metadata:
  title: TEI P5 4.12.0 att.personal specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.personal.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# att.personal

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.
A locator names an element that carries an `ident` attribute by that ident, so the
reading block of an attribute definition states which attribute it describes.

Source byte length: 8885. Git blob: `da9ebd55d9ee07a9ecc0f5d7c6d066f9981585cd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.personal">
  <gloss versionDate="2012-10-24" xml:lang="en">attributes for components of names usually, but not necessarily, personal names</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">사람 이름의 성분에 대한 속성</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">用於個人名稱元件的屬性</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">attributs des composantes des noms de personnes</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">atributos para los componentes de nombres propios de persona</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">attributi per componenti di nomi propri di persona</gloss>
  <gloss versionDate="2023-08-24" xml:lang="ja">名前を構成するもののための属性。通常は人物名だが、必ずしもそうとは限らない。</gloss>
  <desc versionDate="2012-10-24" xml:lang="en">common attributes for those elements which form part of a name usually, but not necessarily, a personal name.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사람 이름의 부분을 형성하는 요소에 대한 공통 속성</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">構成部分個人名稱的元素所用之通用屬性</desc>
  <desc versionDate="2023-08-24" xml:lang="ja">名前の構成要素となる要素に付与される一般的な属性。通常は人物名だが、必ずしもそうとは限らない。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">attributs communs des éléments qui composent un nom de personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">atributos comunes para los elementos que forman parte de un nombre propio de persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">attributi comuni agli
  elementi che compongono un nome proprio di persona</desc>
  <classes>
    
    <memberOf key="att.naming"/>
  </classes>
  <attList>
    <attDef ident="full" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">indicates whether the name component is given in full, as an
abbreviation or simply as an initial.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">축약 또는 이니셜로 간단하게 이름 성분이 완전히 제시된 것인지의 여부를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出所提供的名稱元件是否完整，為一縮寫或僅為一字首字母。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該名前要素は省略がないか、省略形か、イニシャルのような簡単なも
    のか示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si la composante du nom est donnée en intégralité, sous forme d'abréviation ou simplement d'initiale.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el componente del nombre aparece por completo, como una abreviatura o como una inicial.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se la componente del nome compare per esteso, come abbreviazione o come iniziale.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>yes</defaultVal>
      <valList type="closed">
        <valItem ident="yes">
          <gloss versionDate="2009-05-28" xml:lang="en">yes</gloss>
          <gloss versionDate="2009-05-28" xml:lang="fr">complet</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the name component is spelled out in full.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이름 성분이 완전히 제시된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該名稱元件的拼字完整。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el componente nombre se deletrea por completo.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該名前要素は、省略無く示されている。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">la composante du nom est orthographiée en intégralité.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la componente del nome compare per esteso.</desc>
        </valItem>
        <valItem ident="abb">
          <gloss versionDate="2007-07-04" xml:lang="en">abbreviated</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">축약된</gloss>
          <gloss versionDate="2009-05-28" xml:lang="fr">abrégé</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">abbreviato</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">el componente del nombre aparece como forma abreviada.</gloss>
          <gloss versionDate="2023-08-24" xml:lang="ja">省略された</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the name component is given in an abbreviated form.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이름 성분이 축약형으로 제시된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該名稱元件為縮寫形式。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el componente conocido se da en una forma abreviada.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該名前要素には、省略がある。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la composante du nom est donnée sous forme abrégée.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la componente del nome compare in forma abbreviata.</desc>
        </valItem>
        <valItem ident="init">
          <gloss versionDate="2007-07-04" xml:lang="en">initial letter</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">이니셜 문자</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">initiale</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">lettera iniziale</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">el componente del nombre aparece mediante la inicial.</gloss>
          <gloss versionDate="2023-08-24" xml:lang="ja">イニシャルの</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the name component is indicated only by
one initial.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이름 성분이 하나의 이니셜(첫글자)로 제시되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該名稱元件僅以一字首字母表示。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el componente conocido es indicado solamente por una inicial.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該名前要素は、イニシャルだけで示されている。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">la composante du nom n'est indiquée que par sa lettre initiale.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la componente del nome è indicata da una sola iniziale.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="sort" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">sort</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">ordre</gloss>
      <gloss versionDate="2023-08-24" xml:lang="ja">並び替え</gloss>
      <desc versionDate="2012-10-24" xml:lang="en">specifies the sort order of the name component in relation to others within the name.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사람 이름 내에 다른 것과 관련된 이름 성분의 정렬 순서를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明個人名稱中該名稱元件與其他元件之間的排列順序。</desc>
      <desc versionDate="2023-08-24" xml:lang="ja">名前の並び替えにおいて、その名前要素が他の構成要素との関係で何番目に優先されるかを指定する。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">précise dans quel ordre est placé la composante par rapport aux autres dans le nom d'une personne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la posición del componente al interno del nombre propio de persona en relación con los otros componentes.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica la posizione della componente all'interno del nome proprio di persona in relazione alle altre componenti.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#NDPER"/>
  </listRef>
</classSpec>
```

## English reading blocks

### Reading 1

XML location: `/classSpec[@ident='att.personal']/desc[1]`.

common attributes for those elements which form part of a name usually, but not necessarily, a personal name. ^r1

### Reading 2

XML location: `/classSpec[@ident='att.personal']/attList[1]/attDef[@ident='full']/desc[1]`.

indicates whether the name component is given in full, as an abbreviation or simply as an initial. ^r2

### Reading 3

XML location: `/classSpec[@ident='att.personal']/attList[1]/attDef[@ident='full']/valList[1]/valItem[@ident='yes']/desc[1]`.

the name component is spelled out in full. ^r3

### Reading 4

XML location: `/classSpec[@ident='att.personal']/attList[1]/attDef[@ident='full']/valList[1]/valItem[@ident='abb']/desc[1]`.

the name component is given in an abbreviated form. ^r4

### Reading 5

XML location: `/classSpec[@ident='att.personal']/attList[1]/attDef[@ident='full']/valList[1]/valItem[@ident='init']/desc[1]`.

the name component is indicated only by one initial. ^r5

### Reading 6

XML location: `/classSpec[@ident='att.personal']/attList[1]/attDef[@ident='sort']/desc[1]`.

specifies the sort order of the name component in relation to others within the name. ^r6

