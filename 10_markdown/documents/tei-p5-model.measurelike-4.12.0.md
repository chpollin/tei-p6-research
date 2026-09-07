---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.measurelike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.measureLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.measureLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.measureLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1860. Git blob: `df88899e104c664eb76b53644694f640d34b3a21`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="model" ident="model.measureLike">
  <desc versionDate="2007-10-18" xml:lang="en">groups elements which denote a number, a quantity, a measurement, or similar piece of text
    that conveys some numerical meaning.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">숫자, 양, 측정값 등 수치적 의미를 드러내는 텍스트 부분을 가리키는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素代表一個數字、數量、度量，或類似的文字，傳達某些數值上的意義</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">数値、量、計測値など、数値的意味を示すテキストを示す要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui indiquent un nombre, une
    quantité, une mesure ou un extrait d'un texte qui porte une signification numérique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que contienen un número, una cantidad,
    una medida, o un fragmento de texto similar que refleja algún significado numérico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi riferiti a numeri, quantità,
    misurazioni o altra porzione di testo che veicola un significato di tipo numerico</desc>
  <classes>
    
    <memberOf key="model.pPart.data"/>
  </classes>
  <listRef>
    <ptr target="#CONANU"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">groups elements which denote a number, a quantity, a measurement, or similar piece of text
    that conveys some numerical meaning.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">숫자, 양, 측정값 등 수치적 의미를 드러내는 텍스트 부분을 가리키는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集的元素代表一個數字、數量、度量，或類似的文字，傳達某些數值上的意義</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">数値、量、計測値など、数値的意味を示すテキストを示す要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui indiquent un nombre, une
    quantité, une mesure ou un extrait d'un texte qui porte une signification numérique.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que contienen un número, una cantidad,
    una medida, o un fragmento de texto similar que refleja algún significado numérico.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi riferiti a numeri, quantità,
    misurazioni o altra porzione di testo che veicola un significato di tipo numerico</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.pPart.data"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONANU"/>
  </listRef>
```

^b9

