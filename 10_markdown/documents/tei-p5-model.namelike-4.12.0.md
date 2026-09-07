---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.namelike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.nameLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.nameLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.nameLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2684. Git blob: `b1a913c4d69e9b103619d14bcf17b280e624741a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="NAMING" type="model" ident="model.nameLike">
  <desc versionDate="2007-10-18" xml:lang="en">groups elements which name or refer to a person, place, or organization.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">인물, 장소, 또는 조직의 이름 또는 지시를 나타내는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的空白元素可出現於TEI文件內的任何位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物、場所、団体に名前を付与する、または参照する要素をまとめる。</desc>
  <desc versionDate="2009-05-27" xml:lang="fr">regroupe des éléments qui nomment  une
    personne, un lieu ou une organisation, ou qui y font référence à.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que nombran o indican a una persona,
    un lugar (construido por el hombre o geográfico), o una organización.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che nominano o indicano una
    persona, un luogo (costruito dall'uomo o geografico), o un'organizzazione</desc>
  <classes>
    
    <memberOf key="model.addrPart"/>
    <memberOf key="model.correspActionPart"/>
    <memberOf key="model.pPart.data"/>
  </classes>
  <remarks ident="model.nameLike-remarks" versionDate="2005-11-26" xml:lang="en">
    <p>A superset of the naming elements that may appear in datelines, addresses, statements of
      responsibility, etc.</p>
  </remarks>
  <remarks ident="model.nameLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un ensemble de niveau supérieur regroupant les éléments d'appellation qui peuvent apparaître
      dans les dates, les adresses, les mentions de responsabilité, etc.</p>
  </remarks>
  <remarks ident="model.nameLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Un superconjunto de elementos de nombramiento que pueden aparecer en las líneas de fecha, de
      dirección, de declaración de esponsabilidad,l etc.</p>
  </remarks>
  <remarks ident="model.nameLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 日付欄、住所情報、責任表示等に現れる、名前を示す要素の親集合。 </p>
  </remarks>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">groups elements which name or refer to a person, place, or organization.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인물, 장소, 또는 조직의 이름 또는 지시를 나타내는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的空白元素可出現於TEI文件內的任何位置。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物、場所、団体に名前を付与する、または参照する要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">regroupe des éléments qui nomment  une
    personne, un lieu ou une organisation, ou qui y font référence à.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa los elementos que nombran o indican a una persona,
    un lugar (construido por el hombre o geográfico), o una organización.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che nominano o indicano una
    persona, un luogo (costruito dall'uomo o geografico), o un'organizzazione</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.addrPart"/>
    <memberOf key="model.correspActionPart"/>
    <memberOf key="model.pPart.data"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.nameLike-remarks" versionDate="2005-11-26" xml:lang="en">
    <p>A superset of the naming elements that may appear in datelines, addresses, statements of
      responsibility, etc.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.nameLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un ensemble de niveau supérieur regroupant les éléments d'appellation qui peuvent apparaître
      dans les dates, les adresses, les mentions de responsabilité, etc.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.nameLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Un superconjunto de elementos de nombramiento que pueden aparecer en las líneas de fecha, de
      dirección, de declaración de esponsabilidad,l etc.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.nameLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 日付欄、住所情報、責任表示等に現れる、名前を示す要素の親集合。 </p>
  </remarks>
```

^b12

