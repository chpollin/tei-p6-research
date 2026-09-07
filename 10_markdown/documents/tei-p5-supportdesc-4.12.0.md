---
type: representation
source-type: document
source: '[[00_sources/tei-p5-supportdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 supportDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/supportDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# supportDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4558. Git blob: `54f4aa7ed8f83ef3cae7ab3a67da1db19bcbfaa8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="SUPPORTDESC" ident="supportDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">support description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">보충 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción de ayuda</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description du support</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione del supporto</gloss>
  <desc versionDate="2019-01-17" xml:lang="en">groups elements describing the physical support for the written part of a manuscript or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 텍스트 부분에 대한 물리적 서류를 기술하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集描述手稿書寫部分的物質載體元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料のテキスト部分を作る物理的な素材を示す要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe les éléments décrivant le support physique du texte du manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que describen el soporte físico de la parte escrita de un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che descrivono il supporto fisico della parte scritta di un manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <sequence>
        <elementRef key="support" minOccurs="0"/>
        <elementRef key="extent" minOccurs="0"/>
        <elementRef key="foliation" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="collation" minOccurs="0"/>
        <elementRef key="condition" minOccurs="0"/>
      </sequence>
    </alternate>
  </content>
  <attList>
    <attDef ident="material">
      <gloss versionDate="2007-06-12" xml:lang="en">material</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">matériau</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">a short project-defined name for the material composing
      the majority of the support.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">대부분의 서류를 구성하는 재질에 때한 프로젝트에서 정의한 간단한 이름</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">載體主要組成材料的簡短用途定義名稱</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">プロジェクトで定義した、素材を示す短い名前。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">contient un nom abrégé propre au projet désignant
          le matériau qui a principalement servi pour fabriquer le support.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">un nombre breve definido en el ámbito de un proyecto y referente al material que costituye la mayor parte del suporte.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">un nome breve definito nell'ambito di un progetto e riferito al materiale che costituisce la maggior parte del supporto.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="paper"/>
        <valItem ident="parch">
          <gloss versionDate="2007-07-04" xml:lang="en">parchment</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">parchemin</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">pergamena</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">pergamino</gloss>
        </valItem>
        <valItem ident="mixed"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUPPORTDESC-egXML-hj">
      <supportDesc>
        <support> Parchment roll with <material>silk</material> ribbons.
   </support>
      </supportDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">support description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">보충 기술</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">descripción de ayuda</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description du support</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione del supporto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en">groups elements describing the physical support for the written part of a manuscript or other object.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 텍스트 부분에 대한 물리적 서류를 기술하는 요소를 모아 놓는다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集描述手稿書寫部分的物質載體元素。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料のテキスト部分を作る物理的な素材を示す要素をまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe les éléments décrivant le support physique du texte du manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que describen el soporte físico de la parte escrita de un manuscrito.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che descrivono il supporto fisico della parte scritta di un manoscritto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <sequence>
        <elementRef key="support" minOccurs="0"/>
        <elementRef key="extent" minOccurs="0"/>
        <elementRef key="foliation" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="collation" minOccurs="0"/>
        <elementRef key="condition" minOccurs="0"/>
      </sequence>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">material</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">matériau</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">a short project-defined name for the material composing
      the majority of the support.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">대부분의 서류를 구성하는 재질에 때한 프로젝트에서 정의한 간단한 이름</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">載體主要組成材料的簡短用途定義名稱</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">プロジェクトで定義した、素材を示す短い名前。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un nom abrégé propre au projet désignant
          le matériau qui a principalement servi pour fabriquer le support.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">un nombre breve definido en el ámbito de un proyecto y referente al material que costituye la mayor parte del suporte.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">un nome breve definito nell'ambito di un progetto e riferito al materiale che costituisce la maggior parte del supporto.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="paper"/>
        <valItem ident="parch">
          <gloss versionDate="2007-07-04" xml:lang="en">parchment</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">parchemin</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">pergamena</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">pergamino</gloss>
        </valItem>
        <valItem ident="mixed"/>
      </valList>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SUPPORTDESC-egXML-hj">
      <supportDesc>
        <support> Parchment roll with <material>silk</material> ribbons.
   </support>
      </supportDesc>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph1"/>
  </listRef>
```

^b28

