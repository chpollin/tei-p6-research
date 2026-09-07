---
type: representation
source-type: document
source: '[[00_sources/tei-p5-retrace-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 retrace
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/retrace.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# retrace

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1829. Git blob: `224264bf93ce3255cf5d633a5928419b1ed58310`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="retrace" xml:id="gi-retrace" module="transcr">
  <desc versionDate="2013-04-16" xml:lang="en">contains a sequence of writing which has been retraced, for
      example by over-inking, to clarify or fix it.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="no">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-retrace-egXML-ve">
      <line>... Sku<retrace cause="unclear">l</retrace>dren </line>
    </egXML>
  </exemplum>
  <remarks ident="retrace-remarks" versionDate="2013-04-16" xml:lang="en">
    <p>Multiple retraces are indicated by nesting one
      <gi>retrace</gi> within another. In principle, a retrace
      differs from a substitution in that second and subsequent
      rewrites do not materially alter the content of an
      element. Where minor changes have been made during the retracing action
      however these may be marked up using <gi>del</gi>, <gi>add</gi>,
      etc. with an appropriate value for the <att>change</att>
      attribute.</p>
    <!-- need an example for the latter case -->
  </remarks>
  <listRef>
    <ptr target="#PH-fix"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en">contains a sequence of writing which has been retraced, for
      example by over-inking, to clarify or fix it.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="no">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-retrace-egXML-ve">
      <line>... Sku<retrace cause="unclear">l</retrace>dren </line>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="retrace-remarks" versionDate="2013-04-16" xml:lang="en">
    <p>Multiple retraces are indicated by nesting one
      <gi>retrace</gi> within another. In principle, a retrace
      differs from a substitution in that second and subsequent
      rewrites do not materially alter the content of an
      element. Where minor changes have been made during the retracing action
      however these may be marked up using <gi>del</gi>, <gi>add</gi>,
      etc. with an appropriate value for the <att>change</att>
      attribute.</p>
    <!-- need an example for the latter case -->
  </remarks>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PH-fix"/>
  </listRef>
```

^b6

