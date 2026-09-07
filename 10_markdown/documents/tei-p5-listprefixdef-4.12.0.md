---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listprefixdef-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listPrefixDef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listPrefixDef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listPrefixDef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2472. Git blob: `88f1bf081fbd3bae6f8137d575b1130545b63285`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-listPrefixDef" ident="listPrefixDef">
  <gloss versionDate="2012-11-22" xml:lang="en">list of prefix definitions</gloss>
  <desc versionDate="2012-11-23" xml:lang="en">contains a list of definitions of prefixing schemes used in <ident type="datatype">teidata.pointer</ident> values, showing how abbreviated URIs using each scheme may be expanded into full URIs.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="prefixDef"/>
          <elementRef key="listPrefixDef"/>
        </alternate>
    </sequence>
   </content>
  <exemplum versionDate="2012-11-22" xml:lang="en">
    <p>In this example, two private URI scheme prefixes are defined and patterns are provided 
    for dereferencing them. Each prefix is also supplied with a human-readable explanation in a
    <gi>p</gi> element.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listPrefixDef-egXML-dd">
      <listPrefixDef>
        <prefixDef ident="psn" matchPattern="([A-Z]+)" replacementPattern="personography.xml#$1">
          <p>
            Private URIs using the <code>psn</code> 
            prefix are pointers to <gi>person</gi> 
            elements in the personography.xml file. 
            For example, <code>psn:MDH</code> 
            dereferences to <code>personography.xml#MDH</code>.
          </p>
        </prefixDef>
        <prefixDef ident="bibl" matchPattern="([a-z]+[a-z0-9]*)" replacementPattern="http://www.example.com/getBibl.xql?id=$1">
          <p>
            Private URIs using the <code>bibl</code> prefix can be 
            expanded to form URIs which retrieve the relevant 
            bibliographical reference from www.example.com.
          </p>
        </prefixDef>
      </listPrefixDef>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#SAPU"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2012-11-22" xml:lang="en">list of prefix definitions</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-11-23" xml:lang="en">contains a list of definitions of prefixing schemes used in <ident type="datatype">teidata.pointer</ident> values, showing how abbreviated URIs using each scheme may be expanded into full URIs.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="prefixDef"/>
          <elementRef key="listPrefixDef"/>
        </alternate>
    </sequence>
   </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2012-11-22" xml:lang="en">
    <p>In this example, two private URI scheme prefixes are defined and patterns are provided 
    for dereferencing them. Each prefix is also supplied with a human-readable explanation in a
    <gi>p</gi> element.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listPrefixDef-egXML-dd">
      <listPrefixDef>
        <prefixDef ident="psn" matchPattern="([A-Z]+)" replacementPattern="personography.xml#$1">
          <p>
            Private URIs using the <code>psn</code> 
            prefix are pointers to <gi>person</gi> 
            elements in the personography.xml file. 
            For example, <code>psn:MDH</code> 
            dereferences to <code>personography.xml#MDH</code>.
          </p>
        </prefixDef>
        <prefixDef ident="bibl" matchPattern="([a-z]+[a-z0-9]*)" replacementPattern="http://www.example.com/getBibl.xql?id=$1">
          <p>
            Private URIs using the <code>bibl</code> prefix can be 
            expanded to form URIs which retrieve the relevant 
            bibliographical reference from www.example.com.
          </p>
        </prefixDef>
      </listPrefixDef>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SAPU"/>
  </listRef>
```

^b6

