---
type: representation
source-type: document
source: '[[00_sources/tei-p5-macro.abcontent-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 macro.abContent
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/macro.abContent.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# macro.abContent

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 872. Git blob: `3e577dabf7bd7e43402d4e051ff090672ba9bd4e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<macroSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="macro.abContent">
  <gloss versionDate="2022-05-21" xml:lang="en">anonymous block content</gloss>
  <desc versionDate="2022-10-14" xml:lang="en">defines the content of anonymous block elements.</desc>
  <content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.paraPart"/>
      <elementRef key="ab"/>
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
<gloss versionDate="2022-05-21" xml:lang="en">anonymous block content</gloss>
```

^b1

### Block 2

XML location: `/macroSpec[1]/desc[1]`.

```xml
<desc versionDate="2022-10-14" xml:lang="en">defines the content of anonymous block elements.</desc>
```

^b2

### Block 3

XML location: `/macroSpec[1]/content[1]`.

```xml
<content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.paraPart"/>
      <elementRef key="ab"/>
    </alternate>
  </content>
```

^b3

### Block 4

XML location: `/macroSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
  </listRef>
```

^b4

