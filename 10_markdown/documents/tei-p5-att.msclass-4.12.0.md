---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.msclass-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.msClass
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.msClass.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.msClass

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2025. Git blob: `bf5c1048251138908e446262f14c571892198830`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" type="atts" ident="att.msClass">
   <desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate text type or classification.</desc>
   <attList>
      <attDef ident="class">
         <desc versionDate="2013-12-21" xml:lang="en">identifies the text types or classifications applicable to this
            item by pointing to other elements or resources defining the
            classification concerned.</desc>
         <desc versionDate="2007-12-20" xml:lang="ko">이 항목에 적용할 수 있는 텍스트 유형 또는 분류를 식별한다.</desc>
         <desc versionDate="2007-05-02" xml:lang="zh-TW">標明適合的文字類型或分類。</desc>
         <desc versionDate="2022-08-26" xml:lang="ja">関連する分類を定義する他の要素またはリソースを指すことによって、この項目に適用可能なテキストタイプまたは分類を特定する。</desc>
         <desc versionDate="2007-06-12" xml:lang="fr">spécifie la ou les catégories ou classes
            auxquelles l'item appartient.</desc>
         <desc versionDate="2007-05-04" xml:lang="es">identifica la tipología textual u otras clasificaciones aplicables al objeto en cuestión.</desc>
         <desc versionDate="2007-01-21" xml:lang="it">identifica la tipologia testuale o altre classificazioni applicabili all'oggetto in questione.</desc>
         <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      </attDef>
   </attList>
   <listRef>
      <ptr target="#msco"/>
      <ptr target="#mscoit"/>
   </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate text type or classification.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">identifies the text types or classifications applicable to this
            item by pointing to other elements or resources defining the
            classification concerned.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 항목에 적용할 수 있는 텍스트 유형 또는 분류를 식별한다.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明適合的文字類型或分類。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2022-08-26" xml:lang="ja">関連する分類を定義する他の要素またはリソースを指すことによって、この項目に適用可能なテキストタイプまたは分類を特定する。</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie la ou les catégories ou classes
            auxquelles l'item appartient.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica la tipología textual u otras clasificaciones aplicables al objeto en cuestión.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica la tipologia testuale o altre classificazioni applicabili all'oggetto in questione.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b9

### Block 10

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
      <ptr target="#msco"/>
      <ptr target="#mscoit"/>
   </listRef>
```

^b10

