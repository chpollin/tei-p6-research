---
type: representation
source-type: document
source: '[[00_sources/tei-p5-transpose-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 transpose
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/transpose.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# transpose

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1722. Git blob: `ed5849c27c00ddf93dc6dc955880a11784acc037`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="transpose" xml:id="gi-transpose" module="transcr">
  <desc versionDate="2013-04-16" xml:lang="en"> describes a single textual transposition as an ordered list
   of at least two pointers specifying the order in which the elements
   indicated should be re-combined.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <elementRef key="ptr" minOccurs="2" maxOccurs="unbounded"/>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-transpose-egXML-ts" source="#UND">
      <transpose>
        <ptr target="#ib02"/>
        <ptr target="#ib01"/>
      </transpose>
    </egXML>
    <p>The transposition recorded here indicates that the content of the element with
identifier <code>ib02</code> should appear before the content of the
element with identifier <code>ib01</code>.</p>
  </exemplum>
  <remarks ident="transpose-remarks" versionDate="2013-04-16" xml:lang="en">
    <p>Transposition is usually indicated in a document by a
metamark such as a wavy line or numbering. </p>
    <p>The order in which  <gi>ptr</gi> elements appear within a
<gi>transpose</gi> element should correspond with the desired order,
as indicated by the metamark.</p>
  </remarks>
  <listRef>
    <ptr target="#transpo"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en"> describes a single textual transposition as an ordered list
   of at least two pointers specifying the order in which the elements
   indicated should be re-combined.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <elementRef key="ptr" minOccurs="2" maxOccurs="unbounded"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-transpose-egXML-ts" source="#UND">
      <transpose>
        <ptr target="#ib02"/>
        <ptr target="#ib01"/>
      </transpose>
    </egXML>
    <p>The transposition recorded here indicates that the content of the element with
identifier <code>ib02</code> should appear before the content of the
element with identifier <code>ib01</code>.</p>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="transpose-remarks" versionDate="2013-04-16" xml:lang="en">
    <p>Transposition is usually indicated in a document by a
metamark such as a wavy line or numbering. </p>
    <p>The order in which  <gi>ptr</gi> elements appear within a
<gi>transpose</gi> element should correspond with the desired order,
as indicated by the metamark.</p>
  </remarks>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#transpo"/>
  </listRef>
```

^b6

