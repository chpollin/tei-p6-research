---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.resource-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.resource
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.resource.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.resource

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1543. Git blob: `4eae6d19b3d6e33a330deadd77d6401fa9ddac44`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="model" ident="model.resource" predeclare="true">
  <desc versionDate="2016-02-19" xml:lang="en">groups separate elements
    which constitute the content of a digital resource, as opposed to its
    metadata.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">TEI 문서를 구성하는 헤더 및 텍스트와 함께 나타날 수 있는 비테스트적 요소를 모아 놓는다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">agrupa los elementos no-textuales que pueden aparecer junto al encabezado y un texto para constituir un documento de TEI.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ヘダーやTEI文書を構成するテキストと共に出現する、非テキスト要素をま
  とめる。</desc>
  <desc versionDate="2009-10-06" xml:lang="fr">regroupe des éléments non-textuels qui, avec un
en-tête et un texte, constitue un document TEI.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi non testuali che possono costituire un documento TEI insieme a un'intestazione e a un testo.</desc>
  <listRef>
    <ptr target="#STEC"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-02-19" xml:lang="en">groups separate elements
    which constitute the content of a digital resource, as opposed to its
    metadata.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">TEI 문서를 구성하는 헤더 및 텍스트와 함께 나타날 수 있는 비테스트적 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">agrupa los elementos no-textuales que pueden aparecer junto al encabezado y un texto para constituir un documento de TEI.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ヘダーやTEI文書を構成するテキストと共に出現する、非テキスト要素をま
  とめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-10-06" xml:lang="fr">regroupe des éléments non-textuels qui, avec un
en-tête et un texte, constitue un document TEI.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi non testuali che possono costituire un documento TEI insieme a un'intestazione e a un testo.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
  </listRef>
```

^b7

