---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.predicate-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.predicate
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.predicate.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.predicate

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2386. Git blob: `3808bca682635b55a61d12269c60f11fff52d619`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" type="atts" xml:id="class-attr-predicate" ident="att.predicate">
  <desc versionDate="2021-02-10" xml:lang="en">provides attributes for filtering by an XPath predicate expression.</desc>
  <attList>
    <attDef ident="predicate" usage="opt">
      <desc versionDate="2021-02-10" xml:lang="en">the condition under which the element bearing this attribute applies, given as an XPath predicate expression.</desc>
      <datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
      <remarks ident="att.predicate-attr.predicate-remarks" versionDate="2021-02-12" xml:lang="en">
        <p>The XPath predicate expression given as the value of the <att>predicate</att> 
        attribute has to be provided <emph>without</emph> wrapping square brackets.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-predicate-egXML-ar" source="#NONE">
      <model predicate="parent::person" behaviour="inline">
        <desc versionDate="2015-08-21" xml:lang="en">If it is a child of a person element, treat as inline</desc>
      </model>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>The following example declares that the <gi>name</gi> element can be mapped to, or is equivalent to, the external 
    concepts of <q>PERSON</q> and <q>PLACE</q> depending on the <q>XPath</q> expression given in <att>predicate</att></p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-predicate-egXML-zy" source="#NONE">
      <elementSpec ident="name" mode="change">
        <equiv name="PERSON" predicate="@type eq 'person'" uri="http://www.example.com/entities/person"/>
        <equiv name="PLACE" predicate="@type eq 'place'" uri="http://www.example.com/entities/place"/>
      </elementSpec>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDcrystalsCE"/>
    <ptr target="#TDPMPM"/>
    <ptr target="#TDPMIP"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-02-10" xml:lang="en">provides attributes for filtering by an XPath predicate expression.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2021-02-10" xml:lang="en">the condition under which the element bearing this attribute applies, given as an XPath predicate expression.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.predicate-attr.predicate-remarks" versionDate="2021-02-12" xml:lang="en">
        <p>The XPath predicate expression given as the value of the <att>predicate</att> 
        attribute has to be provided <emph>without</emph> wrapping square brackets.</p>
      </remarks>
```

^b4

### Block 5

XML location: `/classSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-predicate-egXML-ar" source="#NONE">
      <model predicate="parent::person" behaviour="inline">
        <desc versionDate="2015-08-21" xml:lang="en">If it is a child of a person element, treat as inline</desc>
      </model>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/classSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <p>The following example declares that the <gi>name</gi> element can be mapped to, or is equivalent to, the external 
    concepts of <q>PERSON</q> and <q>PLACE</q> depending on the <q>XPath</q> expression given in <att>predicate</att></p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-predicate-egXML-zy" source="#NONE">
      <elementSpec ident="name" mode="change">
        <equiv name="PERSON" predicate="@type eq 'person'" uri="http://www.example.com/entities/person"/>
        <equiv name="PLACE" predicate="@type eq 'place'" uri="http://www.example.com/entities/place"/>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDcrystalsCE"/>
    <ptr target="#TDPMPM"/>
    <ptr target="#TDPMIP"/>
  </listRef>
```

^b7

