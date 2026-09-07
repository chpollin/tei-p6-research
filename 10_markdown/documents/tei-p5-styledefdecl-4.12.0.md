---
type: representation
source-type: document
source: '[[00_sources/tei-p5-styledefdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 styleDefDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/styleDefDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# styleDefDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1837. Git blob: `919c69695fdf104b9a98a4d8670d6dd0f86b4ae0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-styleDefDecl" ident="styleDefDecl">
  <gloss versionDate="2012-10-06" xml:lang="en">style definition language declaration</gloss>
  <desc versionDate="2013-04-12" xml:lang="en">specifies the name of the formal language in which style or
  renditional information is supplied elsewhere in the document. The
  specific version of the scheme may also be supplied.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.styleDef"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="styleDefDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:styleDefDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-styleDefDecl-egXML-us">
      <styleDefDecl scheme="css" schemeVersion="2.1"/>
      <!-- ... -->
      <tagsDecl>
        <rendition xml:id="boldface">font-weight: bold;</rendition>
        <rendition xml:id="italicstyle">font-style: italic;</rendition>
      </tagsDecl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD57-1a"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2012-10-06" xml:lang="en">style definition language declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-12" xml:lang="en">specifies the name of the formal language in which style or
  renditional information is supplied elsewhere in the document. The
  specific version of the scheme may also be supplied.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.styleDef"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="styleDefDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:styleDefDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-styleDefDecl-egXML-us">
      <styleDefDecl scheme="css" schemeVersion="2.1"/>
      <!-- ... -->
      <tagsDecl>
        <rendition xml:id="boldface">font-weight: bold;</rendition>
        <rendition xml:id="italicstyle">font-style: italic;</rendition>
      </tagsDecl>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD57-1a"/>
  </listRef>
```

^b7

