---
type: representation
source-type: document
source: '[[00_sources/tei-p5-macroref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 macroRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/macroRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# macroRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1820. Git blob: `5a74f8b69e0acdf94ea8d7e23b971238747f1fab`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-macroRef" ident="macroRef">
  <desc versionDate="2010-05-14" xml:lang="en">points to the specification for some pattern which is to be included in a schema.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.contentPart"/>
    <memberOf key="model.oddRef"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="key" usage="req">
      <desc versionDate="2010-05-14" xml:lang="en">the identifier used for the required pattern within the
        source indicated.</desc>
      <datatype><dataRef key="teidata.xmlName"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-macroRef-egXML-vu" source="#UND">
      <schemaSpec ident="myTEI" source="http://www.tei-c.org/Vault/P5/current/xml/tei/odd/p5subset.xml">
        <!-- ... -->
        <macroRef key="macro.paraContent"/>
        <!-- ... -->
      </schemaSpec>
    </egXML>
  </exemplum>
  <remarks ident="macroRef-remarks" versionDate="2010-05-14" xml:lang="en">
    <p>Patterns or macros are identified by the name supplied as value for the
    <att>ident</att> attribute on the <gi>macroSpec</gi> element in
    which they are declared. All TEI macro names are unique.
    </p>
  </remarks>
  <listRef>
    <ptr target="#TDENT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2010-05-14" xml:lang="en">points to the specification for some pattern which is to be included in a schema.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.contentPart"/>
    <memberOf key="model.oddRef"/>
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

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2010-05-14" xml:lang="en">the identifier used for the required pattern within the
        source indicated.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-macroRef-egXML-vu" source="#UND">
      <schemaSpec ident="myTEI" source="http://www.tei-c.org/Vault/P5/current/xml/tei/odd/p5subset.xml">
        <!-- ... -->
        <macroRef key="macro.paraContent"/>
        <!-- ... -->
      </schemaSpec>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="macroRef-remarks" versionDate="2010-05-14" xml:lang="en">
    <p>Patterns or macros are identified by the name supplied as value for the
    <att>ident</att> attribute on the <gi>macroSpec</gi> element in
    which they are declared. All TEI macro names are unique.
    </p>
  </remarks>
```

^b7

### Block 8

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDENT"/>
  </listRef>
```

^b8

