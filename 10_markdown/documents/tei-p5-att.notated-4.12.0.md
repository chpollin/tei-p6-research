---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.notated-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.notated
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.notated.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.notated

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1895. Git blob: `5f3a285f736c0259c9447de86dfa6d35159e21e1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" 
  type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.notated">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate any specialised notation used for element content.</desc>
  <desc versionDate="2023-08-24" xml:lang="ja">要素の内容を対象とした特別な表記法を示す属性を提供する。</desc>
  <attList>
    <attDef ident="notation" usage="opt">
      <desc versionDate="2012-03-26" xml:lang="en">names the notation used for the content of the element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">요소 내용으로 사용되어 앞서 정의된 표기법 이름을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供先前已定義過、適用於該元素內容的記號名稱。</desc>
      <desc versionDate="2023-08-24" xml:lang="ja">当該要素の内容に用いられた表記法の名前を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise le nom d'une notation définie précédemment,
        utilisée dans le contenu de l'élément.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el nombre de una anotación definida
        previamente y usada para el contenido de un elemento.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome di un'annotazione definita
        precedentemente utilizzata come contenuto dell'elemento.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate any specialised notation used for element content.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-08-24" xml:lang="ja">要素の内容を対象とした特別な表記法を示す属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-03-26" xml:lang="en">names the notation used for the content of the element.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소 내용으로 사용되어 앞서 정의된 표기법 이름을 제시한다.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供先前已定義過、適用於該元素內容的記號名稱。</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2023-08-24" xml:lang="ja">当該要素の内容に用いられた表記法の名前を示す。</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise le nom d'une notation définie précédemment,
        utilisée dans le contenu de l'élément.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el nombre de una anotación definida
        previamente y usada para el contenido de un elemento.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome di un'annotazione definita
        precedentemente utilizzata come contenuto dell'elemento.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b10

