---
type: representation
source-type: document
source: '[[00_sources/tei-p5-precision-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 precision
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/precision.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# precision

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2857. Git blob: `56b96e647875ae77c2775318c5ca865e5d6d20f2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="certainty" xml:id="gi-precision" ident="precision">
  <desc versionDate="2009-06-05" xml:lang="en">indicates the numerical accuracy or precision  associated with some aspect of the text markup.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.ranging"/>
    <memberOf key="att.scoping"/>
    <memberOf key="model.certLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="precision">
      <desc versionDate="2011-04-13" xml:lang="en">characterizes the precision of the element or attribute pointed 
        to by the <gi>precision</gi> element.</desc>
      <datatype><dataRef key="teidata.certainty"/></datatype>
    </attDef>
    <attDef ident="stdDeviation" usage="opt">
      <desc versionDate="2009-06-05" xml:lang="en">supplies a standard deviation associated with the value in
      question.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-precision-egXML-cw">
      <date xml:id="date001" notBefore="0014" notAfter="0064">Within about 50
        years of the death of Augustus</date>
      <precision target="#date001" match="@notBefore" precision="high"/>
      <precision target="#date001" match="@notAfter" precision="low"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-precision-egXML-pl">
      <date notBefore="1632" notAfter="1642">Not more than ten years before the start of the Civil War
            <precision match="@notBefore" precision="low"/>
            <precision match="@notAfter" precision="high"/>
         </date>
    </egXML>
  </exemplum>
  <!--<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples">
         <state from="1382" to="1477">
            <p>Catholicos-Patriarch of the Church of the East.</p> 
            <precision match="@from" atLeast="1382" atMost="1430"/>
            <precision match="@to" atLeast="1444"  atMost="1477"/>
         </state>
      </egXML>
   </exemplum>-->
  <listRef>
    <ptr target="#CEPREC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2009-06-05" xml:lang="en">indicates the numerical accuracy or precision  associated with some aspect of the text markup.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.ranging"/>
    <memberOf key="att.scoping"/>
    <memberOf key="model.certLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-04-13" xml:lang="en">characterizes the precision of the element or attribute pointed 
        to by the <gi>precision</gi> element.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.certainty"/></datatype>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2009-06-05" xml:lang="en">supplies a standard deviation associated with the value in
      question.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-precision-egXML-cw">
      <date xml:id="date001" notBefore="0014" notAfter="0064">Within about 50
        years of the death of Augustus</date>
      <precision target="#date001" match="@notBefore" precision="high"/>
      <precision target="#date001" match="@notAfter" precision="low"/>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-precision-egXML-pl">
      <date notBefore="1632" notAfter="1642">Not more than ten years before the start of the Civil War
            <precision match="@notBefore" precision="low"/>
            <precision match="@notAfter" precision="high"/>
         </date>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CEPREC"/>
  </listRef>
```

^b10

