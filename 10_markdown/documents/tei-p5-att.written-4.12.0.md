---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.written-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.written
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.written.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.written

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2239. Git blob: `3a6f0503e42730b534be6c4172eb9f36e489a9d8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" 
 type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.written">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate the hand in which
    the content of an element was written in the source being transcribed.</desc>
  <desc versionDate="2024-08-16" xml:lang="de">stellt Attribute bereit, um anzuzeigen, von welcher
    Hand der Inhalt eines Elements in der transkribierten Quelle stammt.</desc>
  <classes/>
  <attList>
    <attDef ident="hand" usage="opt">
      <desc versionDate="2018-06-15" xml:lang="en">points to a <gi>handNote</gi> element describing the hand considered responsible for the
        content of the element concerned.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">간섭을 만든 당사자의 필적을 나타낸다.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該調整を行った主体の筆致を特定する。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">signale la main de celui qui est intervenue.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il responsabile dell'aggiunta o della cancellazione.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el responsable de la adición o de la omisión.</desc>
      <datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
      <!--      <valDesc>must refer to a <gi>handNote</gi> element, typically
        declared in the document header (see section <ptr target="#PHDH"/>).</valDesc>
        <valDesc versionDate="2009-05-28" xml:lang="fr">doit faire référence à un élément <gi>handNote</gi>, en général déclaré dans l'en-tête TEI (voir la section <ptr target="#PHDH"/>).</valDesc>-->
      <!-- shdnt there be a constraintspec for this? LB 2013-12-09 -->
    </attDef>
  </attList>
  <listRef>
    <ptr target="#STECAT"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate the hand in which
    the content of an element was written in the source being transcribed.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-08-16" xml:lang="de">stellt Attribute bereit, um anzuzeigen, von welcher
    Hand der Inhalt eines Elements in der transkribierten Quelle stammt.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes/>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2018-06-15" xml:lang="en">points to a <gi>handNote</gi> element describing the hand considered responsible for the
        content of the element concerned.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">간섭을 만든 당사자의 필적을 나타낸다.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該調整を行った主体の筆致を特定する。</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">signale la main de celui qui est intervenue.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il responsabile dell'aggiunta o della cancellazione.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el responsable de la adición o de la omisión.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.pointer"/>
      </datatype>
```

^b10

### Block 11

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STECAT"/>
  </listRef>
```

^b11

