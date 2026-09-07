---
type: representation
source-type: document
source: '[[00_sources/tei-p5-macro.specialpara-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 macro.specialPara
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/macro.specialPara.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# macro.specialPara

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3453. Git blob: `931b331a379153893a32fa6b83721164c0324607`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<macroSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="macro.specialPara">
  <gloss versionDate="2005-01-14" xml:lang="en">'special' paragraph content</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">특별 문단 내용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">「特殊」段落內容</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">contenu "spécial" de paragraphe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">contenido de párrafo 'especial'</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">contenuto di paragrafo "speciale"</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">defines the content model of elements such as notes or list items, which either contain a
    series of component-level elements or else have the same structure as a paragraph, containing a
    series of phrase-level and inter-level elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일련의 성분층위 요소를 포함하거나 아니면 문단과 동일 구조를 갖는 주석 또는 목록 항목과 같은 요소의
    내용 모델을 정의하며, 이것은 일련의 구 층위 및 상호층위 요소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義元素的內容模型，如註解或列表項目，這些內容模型包含一系列組合性層次元素，或與一個段落有相同的結構，包含一系列的詞組層次或inter-層次元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">一連の句レベルまたは挿入レベルの要素と共に、一連の構成要素レベルの要
    素、または段落相当の構造を持つ、注釈やリスト項目となる要素の内容モデ ルを定義する。</desc>
  <desc versionDate="2009-07-20" xml:lang="fr">définit le modèle de contenu des éléments tels que des
    notes ou des items de liste, contenant soit une suite d'éléments de niveau composant soit qui
    ont la même structure qu'un paragraphe, contenant une suite d’éléments du niveau de l’expression
    et de niveau intermédiaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define el modelo de contenido de elementos tipo notas o
    entradas de lista que contienen una serie de elementos a nivel de componentes que tienen la
    misma estructura de un párrafo con una serie de elementos a nivel sintagmático y inter-nivel.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce il modello di contenuto di elementi quali note
    o voci di lista che contiene una serie di elementi a livello di componenti aventi la stessa
    struttura di un paragrafo con una serie di elementi a livello sintagmatico e interlivello</desc>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <classRef key="model.divPart"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <listRef>
    <ptr target="#STEC"/>
  </listRef>
</macroSpec>
```

## Source blocks

### Block 1

XML location: `/macroSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">'special' paragraph content</gloss>
```

^b1

### Block 2

XML location: `/macroSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">특별 문단 내용</gloss>
```

^b2

### Block 3

XML location: `/macroSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">「特殊」段落內容</gloss>
```

^b3

### Block 4

XML location: `/macroSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contenu "spécial" de paragraphe</gloss>
```

^b4

### Block 5

XML location: `/macroSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">contenido de párrafo 'especial'</gloss>
```

^b5

### Block 6

XML location: `/macroSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">contenuto di paragrafo "speciale"</gloss>
```

^b6

### Block 7

XML location: `/macroSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">defines the content model of elements such as notes or list items, which either contain a
    series of component-level elements or else have the same structure as a paragraph, containing a
    series of phrase-level and inter-level elements.</desc>
```

^b7

### Block 8

XML location: `/macroSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일련의 성분층위 요소를 포함하거나 아니면 문단과 동일 구조를 갖는 주석 또는 목록 항목과 같은 요소의
    내용 모델을 정의하며, 이것은 일련의 구 층위 및 상호층위 요소를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/macroSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義元素的內容模型，如註解或列表項目，這些內容模型包含一系列組合性層次元素，或與一個段落有相同的結構，包含一系列的詞組層次或inter-層次元素。</desc>
```

^b9

### Block 10

XML location: `/macroSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">一連の句レベルまたは挿入レベルの要素と共に、一連の構成要素レベルの要
    素、または段落相当の構造を持つ、注釈やリスト項目となる要素の内容モデ ルを定義する。</desc>
```

^b10

### Block 11

XML location: `/macroSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-07-20" xml:lang="fr">définit le modèle de contenu des éléments tels que des
    notes ou des items de liste, contenant soit une suite d'éléments de niveau composant soit qui
    ont la même structure qu'un paragraphe, contenant une suite d’éléments du niveau de l’expression
    et de niveau intermédiaire.</desc>
```

^b11

### Block 12

XML location: `/macroSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define el modelo de contenido de elementos tipo notas o
    entradas de lista que contienen una serie de elementos a nivel de componentes que tienen la
    misma estructura de un párrafo con una serie de elementos a nivel sintagmático y inter-nivel.</desc>
```

^b12

### Block 13

XML location: `/macroSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce il modello di contenuto di elementi quali note
    o voci di lista che contiene una serie di elementi a livello di componenti aventi la stessa
    struttura di un paragrafo con una serie di elementi a livello sintagmatico e interlivello</desc>
```

^b13

### Block 14

XML location: `/macroSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <classRef key="model.divPart"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b14

### Block 15

XML location: `/macroSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
  </listRef>
```

^b15

