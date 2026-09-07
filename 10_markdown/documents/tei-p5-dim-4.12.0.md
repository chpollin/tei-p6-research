---
type: representation
source-type: document
source: '[[00_sources/tei-p5-dim-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 dim
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/dim.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# dim

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1383. Git blob: `2e4be08626210204054e51ed2def8bef08994317`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="gi-dim" ident="dim">
  <desc versionDate="2009-06-06" xml:lang="en">contains any single measurement forming part of a dimensional
specification of some sort.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
  </classes>
  <content>
    <macroRef key="macro.xtext"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xmlns:rng="http://relaxng.org/ns/structure/1.0" xml:id="gi-dim-egXML-qz" source="#UND">
      <dim type="circumference" extent="4.67 in"/>
    </egXML>
  </exemplum>
  <remarks ident="dim-remarks" versionDate="2009-06-06" xml:lang="en">
    <p>The specific elements <gi>width</gi>, <gi>height</gi>, and
<gi>depth</gi> should be used in preference to this generic element
wherever appropriate.</p>
  </remarks>
  <listRef>
    <ptr target="#msdim"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2009-06-06" xml:lang="en">contains any single measurement forming part of a dimensional
specification of some sort.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.xtext"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xmlns:rng="http://relaxng.org/ns/structure/1.0" xml:id="gi-dim-egXML-qz" source="#UND">
      <dim type="circumference" extent="4.67 in"/>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="dim-remarks" versionDate="2009-06-06" xml:lang="en">
    <p>The specific elements <gi>width</gi>, <gi>height</gi>, and
<gi>depth</gi> should be used in preference to this generic element
wherever appropriate.</p>
  </remarks>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msdim"/>
  </listRef>
```

^b6

