---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.global.facs-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.global.facs
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.global.facs.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.global.facs

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3239. Git blob: `070cc3fb028c2c708f64f8adb07bb2405f97ef67`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" predeclare="true" module="transcr" type="atts" ident="att.global.facs">
  <desc versionDate="2021-05-09" xml:lang="en">provides attributes used to express correspondence between an element and all or part of a facsimile image or surface.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><gi>facsimile</gi> 요소 내에서 이미지 또는 표면부와 관련될 수 있는 요소</desc>
  <desc versionDate="2008-04-06" xml:lang="es">los elementos que se pueden asociar a una imagen o a una
    superficie dentro de un <gi>facsímil</gi>.</desc>
  <desc versionDate="2019-07-21" xml:lang="ja">転写されたテキストを含む要素と、そのテキストを表す画像の全部または一部との間の対応を表すために使用される属性を提供する。</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">attributs utilisables pour les éléments correspondant à tout ou partie d'une image, parce qu'ils contiennent une représentation alternative de cette image, généralement mais
    pas nécessairement, une transcription.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">elementi che possono essere associati a un'immagine o una
    superficie all'interno dell'elemento facsimile</desc>
  <attList>
    <attDef ident="facs" usage="opt">
      <gloss versionDate="2007-08-26" xml:lang="en">facsimile</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">모사</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">facsímil</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">fac-similé</gloss>
      <gloss versionDate="2019-07-21" xml:lang="ja">ファクシミリ</gloss>
      <desc versionDate="2021-05-09" xml:lang="en">points to one or more images, portions of an image, or surfaces which correspond to the current element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이미지 또는 이 요소와 일치하는 <gi>facsimile</gi> 요소의 부분을 직접 가리킨다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">indica directamente a la imagen, o a la parte de un
          <gi>facsímil</gi> que se corresponde con este elemento.</desc>
      <desc versionDate="2008-04-06" xml:lang="ja">当該要素に対応する要素<gi>facsimile</gi>にある画像やその部分への 参照。</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">pointe directement vers une image ou vers une partie
        d'une image correspondant au contenu de l'élément.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica direttamente un'immagine o una parte di un
        elemento facsimile corrispondente a tale elemento</desc>
      <datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#PHFAX"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-05-09" xml:lang="en">provides attributes used to express correspondence between an element and all or part of a facsimile image or surface.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><gi>facsimile</gi> 요소 내에서 이미지 또는 표면부와 관련될 수 있는 요소</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">los elementos que se pueden asociar a una imagen o a una
    superficie dentro de un <gi>facsímil</gi>.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2019-07-21" xml:lang="ja">転写されたテキストを含む要素と、そのテキストを表す画像の全部または一部との間の対応を表すために使用される属性を提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">attributs utilisables pour les éléments correspondant à tout ou partie d'une image, parce qu'ils contiennent une représentation alternative de cette image, généralement mais
    pas nécessairement, une transcription.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">elementi che possono essere associati a un'immagine o una
    superficie all'interno dell'elemento facsimile</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-08-26" xml:lang="en">facsimile</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">모사</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">facsímil</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">fac-similé</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2019-07-21" xml:lang="ja">ファクシミリ</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2021-05-09" xml:lang="en">points to one or more images, portions of an image, or surfaces which correspond to the current element.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이미지 또는 이 요소와 일치하는 <gi>facsimile</gi> 요소의 부분을 직접 가리킨다.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">indica directamente a la imagen, o a la parte de un
          <gi>facsímil</gi> que se corresponde con este elemento.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">当該要素に対応する要素<gi>facsimile</gi>にある画像やその部分への 参照。</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">pointe directement vers une image ou vers une partie
        d'une image correspondant au contenu de l'élément.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica direttamente un'immagine o una parte di un
        elemento facsimile corrispondente a tale elemento</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b18

### Block 19

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHFAX"/>
  </listRef>
```

^b19

