---
type: representation
source-type: document
source: '[[00_sources/tei-p5-empty-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 empty
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/empty.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# empty

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1079. Git blob: `c2fd3124adaeea59878994ff8b0b3bb2ce8e6c7a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-empty" ident="empty">
  <desc versionDate="2014-07-01" xml:lang="en">indicates the presence of an empty node within a
    content model.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.contentPart"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-empty-egXML-rz" source="#UND">
      <content>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <empty/>
          <elementRef key="hi"/>
        </alternate>
      </content>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2014-07-01" xml:lang="en">indicates the presence of an empty node within a
    content model.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.contentPart"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-empty-egXML-rz" source="#UND">
      <content>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <empty/>
          <elementRef key="hi"/>
        </alternate>
      </content>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD"/>
  </listRef>
```

^b5

