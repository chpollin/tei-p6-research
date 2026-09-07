---
type: representation
source-type: document
source: '[[00_sources/tei-p5-unitdef-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 unitDef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/unitDef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# unitDef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1981. Git blob: `2f7dfb8a62c386724f3cc975c3b6eb5ffb91067c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-unitDef" ident="unitDef">
  <gloss versionDate="2018-07-18" xml:lang="en">unit definition</gloss>
  <desc versionDate="2018-07-18" xml:lang="en">contains descriptive information related to a specific unit of measurement.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
     <alternate minOccurs="1" maxOccurs="unbounded">
       <classRef key="model.labelLike" minOccurs="1"/>
       <classRef key="model.placeNamePart" minOccurs="0"/>
       <elementRef key="conversion" minOccurs="0"/>
       <elementRef key="unit" minOccurs="0"/>     
     </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unitDef-egXML-wv" source="#NONE">
      <unitDecl>
      <unitDef xml:id="pechys" type="length">
        <label>πῆχυς</label>
        <placeName ref="#athens"/>
        <conversion fromUnit="#daktylos" toUnit="#pechys" formula="$fromUnit div 24"/>
        <desc>Equivalent to a cubit or 24 daktyloi.</desc>
      </unitDef>
      <unitDef xml:id="daktylos" type="length">
        <label>δάκτυλος</label>
        <placeName ref="#athens"/>
        <desc>A basic unit of length equivalent to one finger (or the size of a thumb) in ancient Greece.</desc>
      </unitDef>
     </unitDecl>
    </egXML>
  </exemplum> 
  <listRef>
    <ptr target="#HDUDECL" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2018-07-18" xml:lang="en">unit definition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-07-18" xml:lang="en">contains descriptive information related to a specific unit of measurement.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
     <alternate minOccurs="1" maxOccurs="unbounded">
       <classRef key="model.labelLike" minOccurs="1"/>
       <classRef key="model.placeNamePart" minOccurs="0"/>
       <elementRef key="conversion" minOccurs="0"/>
       <elementRef key="unit" minOccurs="0"/>     
     </alternate>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unitDef-egXML-wv" source="#NONE">
      <unitDecl>
      <unitDef xml:id="pechys" type="length">
        <label>πῆχυς</label>
        <placeName ref="#athens"/>
        <conversion fromUnit="#daktylos" toUnit="#pechys" formula="$fromUnit div 24"/>
        <desc>Equivalent to a cubit or 24 daktyloi.</desc>
      </unitDef>
      <unitDef xml:id="daktylos" type="length">
        <label>δάκτυλος</label>
        <placeName ref="#athens"/>
        <desc>A basic unit of length equivalent to one finger (or the size of a thumb) in ancient Greece.</desc>
      </unitDef>
     </unitDecl>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDUDECL" type="div3"/>
  </listRef>
```

^b6

