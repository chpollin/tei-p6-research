---
type: representation
source-type: document
source: '[[00_sources/tei-p5-prefixdef-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 prefixDef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/prefixDef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# prefixDef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2924. Git blob: `a2f83843df05b65f393bb780a3b14e39823cb503`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-prefixDef" ident="prefixDef">
  <gloss versionDate="2012-11-22" xml:lang="en">prefix definition</gloss>
  <desc versionDate="2012-12-26" xml:lang="en">defines a prefixing scheme used in <ident type="datatype">teidata.pointer</ident> values,
  showing how abbreviated URIs using the scheme may be expanded into full URIs.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.patternReplacement"/>
  </classes>
  <content>
      <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
  <attList>
    <attDef ident="ident" usage="req">
      <desc versionDate="2012-11-22" xml:lang="en">supplies a name which functions as the prefix for an abbreviated
          pointing scheme such as a private URI scheme. The prefix constitutes the 
        text preceding the first colon.</desc>
	<datatype>
	  <dataRef key="teidata.prefix"/>
	</datatype>
	<remarks ident="prefixDef-attr.ident-remarks" versionDate="2017-05-25" xml:lang="en">
	  <p>The value is limited to <ident type="datatype">teidata.prefix</ident> so that it may be
	  mapped directly to a URI prefix.</p>
	</remarks>
    </attDef>
  </attList>
  <exemplum versionDate="2012-11-22" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prefixDef-egXML-fm">
      <prefixDef ident="ref" matchPattern="([a-z]+)" replacementPattern="../../references/references.xml#$1">
        <p>
          In the context of this project, private URIs with 
          the prefix "ref" point to <gi>div</gi> elements in 
          the project's global references.xml file.
        </p>
      </prefixDef>
    </egXML>
  </exemplum>
  <remarks ident="prefixDef-remarks" versionDate="2026-04-16" xml:lang="en">
    <p>Note that we used the term <q>prefix</q> in a general sense; in the context 
      of a <ident type="datatype">teidata.pointer</ident> attribute, the prefix 
      functions as a private URI scheme name as defined in 
      <ref target="https://datatracker.ietf.org/doc/html/rfc7595">RFC 7595</ref>.
    </p>
    <p>The abbreviated pointer may be dereferenced to produce either
    an absolute or a relative URI reference. In the latter case it is
    combined with the value of <att>xml:base</att> in force at the
    place where the pointing attribute occurs to form an absolute URI
    in the usual manner as prescribed by <ref target="https://www.w3.org/TR/xmlbase/">XML Base</ref>.</p>
  </remarks>
  <listRef>
    <ptr target="#SAPU"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2012-11-22" xml:lang="en">prefix definition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-26" xml:lang="en">defines a prefixing scheme used in <ident type="datatype">teidata.pointer</ident> values,
  showing how abbreviated URIs using the scheme may be expanded into full URIs.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.patternReplacement"/>
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

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-11-22" xml:lang="en">supplies a name which functions as the prefix for an abbreviated
          pointing scheme such as a private URI scheme. The prefix constitutes the 
        text preceding the first colon.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
	  <dataRef key="teidata.prefix"/>
	</datatype>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="prefixDef-attr.ident-remarks" versionDate="2017-05-25" xml:lang="en">
	  <p>The value is limited to <ident type="datatype">teidata.prefix</ident> so that it may be
	  mapped directly to a URI prefix.</p>
	</remarks>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2012-11-22" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prefixDef-egXML-fm">
      <prefixDef ident="ref" matchPattern="([a-z]+)" replacementPattern="../../references/references.xml#$1">
        <p>
          In the context of this project, private URIs with 
          the prefix "ref" point to <gi>div</gi> elements in 
          the project's global references.xml file.
        </p>
      </prefixDef>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="prefixDef-remarks" versionDate="2026-04-16" xml:lang="en">
    <p>Note that we used the term <q>prefix</q> in a general sense; in the context 
      of a <ident type="datatype">teidata.pointer</ident> attribute, the prefix 
      functions as a private URI scheme name as defined in 
      <ref target="https://datatracker.ietf.org/doc/html/rfc7595">RFC 7595</ref>.
    </p>
    <p>The abbreviated pointer may be dereferenced to produce either
    an absolute or a relative URI reference. In the latter case it is
    combined with the value of <att>xml:base</att> in force at the
    place where the pointing attribute occurs to form an absolute URI
    in the usual manner as prescribed by <ref target="https://www.w3.org/TR/xmlbase/">XML Base</ref>.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SAPU"/>
  </listRef>
```

^b10

