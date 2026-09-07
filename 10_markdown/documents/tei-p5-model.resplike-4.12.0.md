---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.resplike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.respLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.respLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.respLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1810. Git blob: `27431c8300a8182a2864eb5775fc8188b54b7b8a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="RESPLIKE" type="model" ident="model.respLike">
  <desc versionDate="2008-10-12" xml:lang="en">groups elements which are used to indicate intellectual or other significant responsibility,
    for example within a bibliographic element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 서지 요소 내에서 지적 책임을 나타내는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集指出智慧責任的元素，例如在書目元素內。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">知的責任を示す要素をまとめる。例えば、書誌情報要素内にあるもの。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments qui sont utilisés pour indiquer une
    responsabilité intellectuelle ou une autre responsabilité significative, par exemple dans un
    élément bibliographique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">aggrupa elementos utilizados para indicar responsabilidad
    intelectual, p.ej. dentro de un elemento bibliográfico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi utilizzati per indicare responsabilità
    intellettuale, per esempio all'interno di un elemento bibliografico</desc>
  <classes>
    
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msItemPart"/>
  </classes>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-10-12" xml:lang="en">groups elements which are used to indicate intellectual or other significant responsibility,
    for example within a bibliographic element.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어 서지 요소 내에서 지적 책임을 나타내는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集指出智慧責任的元素，例如在書目元素內。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">知的責任を示す要素をまとめる。例えば、書誌情報要素内にあるもの。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments qui sont utilisés pour indiquer une
    responsabilité intellectuelle ou une autre responsabilité significative, par exemple dans un
    élément bibliographique.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">aggrupa elementos utilizados para indicar responsabilidad
    intelectual, p.ej. dentro de un elemento bibliográfico.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi utilizzati per indicare responsabilità
    intellettuale, per esempio all'interno di un elemento bibliografico</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msItemPart"/>
  </classes>
```

^b8

