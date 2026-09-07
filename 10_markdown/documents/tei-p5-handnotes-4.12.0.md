---
type: representation
source-type: document
source: '[[00_sources/tei-p5-handnotes-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 handNotes
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/handNotes.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# handNotes

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2223. Git blob: `ebcf6126012c654f2858bd077e4a13e810be55e4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-handNotes" ident="handNotes">
  <desc versionDate="2007-09-27" xml:lang="en">contains one or more <gi>handNote</gi> elements documenting the
different hands identified within the source texts.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원본 텍스트 내에서 식별되는 필적을 기록하는 하나 이상의  <gi>handNote</gi> 요소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一系列<gi>書寫者</gi>元素，列出來源文件中不同的書寫者。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">元資料にある特定可能な筆致を記録する、ひとつ以上の要素
  <gi>handNote</gi>を示す。</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">contient un ou plusieurs éléments <gi>handNote</gi> qui documentent les différentes mains identifiées dans les textes source.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una serie di elementi che elencano le diverse mani della fonte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una serie de elementos que indexa las diversas manos de la fuente.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    
      <elementRef key="handNote" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-handNotes-egXML-or">
      <handNotes>
        <handNote xml:id="H1" script="copperplate" medium="brown-ink">Carefully written with regular descenders</handNote>
        <handNote xml:id="H2" script="print" medium="pencil">Unschooled scrawl</handNote>
      </handNotes>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHDH"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-27" xml:lang="en">contains one or more <gi>handNote</gi> elements documenting the
different hands identified within the source texts.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원본 텍스트 내에서 식별되는 필적을 기록하는 하나 이상의  <gi>handNote</gi> 요소를 포함한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一系列<gi>書寫者</gi>元素，列出來源文件中不同的書寫者。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元資料にある特定可能な筆致を記録する、ひとつ以上の要素
  <gi>handNote</gi>を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">contient un ou plusieurs éléments <gi>handNote</gi> qui documentent les différentes mains identifiées dans les textes source.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una serie di elementi che elencano le diverse mani della fonte.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una serie de elementos que indexa las diversas manos de la fuente.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <elementRef key="handNote" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-handNotes-egXML-or">
      <handNotes>
        <handNote xml:id="H1" script="copperplate" medium="brown-ink">Carefully written with regular descenders</handNote>
        <handNote xml:id="H2" script="print" medium="pencil">Unschooled scrawl</handNote>
      </handNotes>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDH"/>
  </listRef>
```

^b11

