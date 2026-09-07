---
type: representation
source-type: document
source: '[[00_sources/tei-p5-elementref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 elementRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/elementRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# elementRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2905. Git blob: `3eea7b03a67aeeb9de6a338efc9cf21ba28895f9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-elementRef" ident="elementRef">
  <desc versionDate="2010-05-11" xml:lang="en">points to the specification for some element which is to be included in a schema.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
    <memberOf key="model.oddRef"/>
  </classes>
  <content><empty/></content>
  <constraintSpec ident="only_sensible_attrs" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern>
        <sch:rule context="tei:elementRef[ parent::tei:schemaSpec | parent::tei:specGrp ]">
          <sch:report test="@minOccurs | @maxOccurs" role="error">An element reference is not repeatable when part of a schema specification (and thus this &lt;elementRef> should not have @minOccurs or @maxOccurs).</sch:report>
        </sch:rule>
        <sch:rule context="tei:content//tei:elementRef">
          <sch:report test="@source" role="error">An element reference within a content model must refer to a locally defined element specification (and thus this &lt;elementRef> should not have @source).</sch:report>
        </sch:rule>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="key" usage="req">
      <desc versionDate="2010-05-11" xml:lang="en">the identifier used for the required element within the
        source indicated.</desc>
      <datatype><dataRef key="teidata.xmlName"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementRef-egXML-js" source="#UND">
      <elementRef key="p"/>
    </egXML>
    <p>Include in the schema an element named <gi>p</gi>  available from the
    current default source.</p>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementRef-egXML-vg" source="#UND">
      <elementRef key="p" source="tei:1.2.1"/>
    </egXML>
    <p>Include  in the schema an element named <gi>p</gi> 
    available from the TEI P5 1.2.1 release.</p>
  </exemplum>
  <remarks ident="elementRef-remarks" versionDate="2010-05-14" xml:lang="en">
    <p>Elements are identified by the name supplied as value for the
    <att>ident</att> attribute on the <gi>elementSpec</gi> element in
    which they are declared. TEI element names are unique.
    </p>
  </remarks>
  <listRef>
    <ptr target="#TDmodules"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2010-05-11" xml:lang="en">points to the specification for some element which is to be included in a schema.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
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

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="only_sensible_attrs" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern>
        <sch:rule context="tei:elementRef[ parent::tei:schemaSpec | parent::tei:specGrp ]">
          <sch:report test="@minOccurs | @maxOccurs" role="error">An element reference is not repeatable when part of a schema specification (and thus this &lt;elementRef> should not have @minOccurs or @maxOccurs).</sch:report>
        </sch:rule>
        <sch:rule context="tei:content//tei:elementRef">
          <sch:report test="@source" role="error">An element reference within a content model must refer to a locally defined element specification (and thus this &lt;elementRef> should not have @source).</sch:report>
        </sch:rule>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2010-05-11" xml:lang="en">the identifier used for the required element within the
        source indicated.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementRef-egXML-js" source="#UND">
      <elementRef key="p"/>
    </egXML>
    <p>Include in the schema an element named <gi>p</gi>  available from the
    current default source.</p>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementRef-egXML-vg" source="#UND">
      <elementRef key="p" source="tei:1.2.1"/>
    </egXML>
    <p>Include  in the schema an element named <gi>p</gi> 
    available from the TEI P5 1.2.1 release.</p>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="elementRef-remarks" versionDate="2010-05-14" xml:lang="en">
    <p>Elements are identified by the name supplied as value for the
    <att>ident</att> attribute on the <gi>elementSpec</gi> element in
    which they are declared. TEI element names are unique.
    </p>
  </remarks>
```

^b9

### Block 10

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDmodules"/>
  </listRef>
```

^b10

