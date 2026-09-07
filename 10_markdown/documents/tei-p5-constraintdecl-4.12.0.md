---
type: representation
source-type: document
source: '[[00_sources/tei-p5-constraintdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 constraintDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/constraintDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# constraintDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5059. Git blob: `2386ad549c76a83c78791aca0df651a0115504cd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-constraintDecl" ident="constraintDecl">
  <gloss versionDate="2023-03-09" xml:lang="en">constraint declaration</gloss>
  <desc versionDate="2023-03-09" xml:lang="en">contains declarations pertaining to formal constraints expressed elsewhere in <gi>constraintSpec</gi> elements</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
    <!-- <constraintDecl> is part of content of <schemaSpec> directly, not via a class -->
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identEquiv"/>
        <classRef key="model.descLike"/>
      </alternate>
      <anyElement minOccurs="0" maxOccurs="unbounded"/>             <!-- typically <sch:ns> elements -->
    </sequence>
  </content>
  <!-- NOTE: Also see constraint "context-required" in file constraintSpec.xml,
       which may be fired on a <constraintDecl> as well. -->
  <constraintSpec scheme="schematron" ident="one-constraintDecl-per-scheme" xml:lang="en">
    <!-- Note: the “not a descendant of <egXML>” predicate on the
         XPath defining $schemes is required for the P5 build process,
         not for normal users. (In P5 build validity of <egXML>s are
         tested by changing their namespace to TEI, so the tei: prefix
         is not sufficient.) —Syd, 2024-09-19 -->
    <constraint>
      <sch:rule context="/*[ count( //tei:constraintDecl ) gt 1 ]">
        <sch:let name="schemes" value="//tei:constraintDecl[ not(ancestor::*[local-name(.) eq 'egXML'] ) ]/@scheme"/>
        <sch:let name="disctinct_schemes" value="distinct-values( $schemes )"/>
        <sch:assert test="count( $schemes ) eq count( $disctinct_schemes )">
          Each &lt;constraintDecl&gt; element should have a @scheme attribute that is distinct from that of all the other &lt;constraintDecl&gt;s.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="scheme" usage="req">
      <desc versionDate="2023-03-09" xml:lang="en">supplies the name of the language to which the declarations herein apply</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="schematron">
          <gloss versionDate="2016-09-27" xml:lang="en">ISO Schematron</gloss>
        </valItem>
      </valList>
      <remarks ident="constraintDecl-attr.scheme-remarks" versionDate="2023-03-09" xml:lang="en">
        <p>The declarations contained in a particular
        <gi>constraintDecl</gi> (including <att>queryBinding</att>, if
        present) apply to the <gi>constraintSpec</gi> elements whose
        <att>scheme</att> matches the <att>scheme</att> of the
        <gi>constraintDecl</gi>.</p>
      </remarks>
    </attDef>
    <attDef ident="queryBinding" usage="rec">
      <gloss xml:lang="en" versionDate="2023-03-09">query language binding</gloss>
      <desc xml:lang="en" versionDate="2023-03-09">specifies the query
      language binding for rule-based schema expressions in
      <gi>constraintSpec</gi> elements that have a matching
      <att>scheme</att> attribute</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="exslt"/>
        <valItem ident="stx"/>
        <valItem ident="xslt"/>
        <valItem ident="xslt2"/>
        <valItem ident="xslt3"/>
        <valItem ident="xpath"/>
        <valItem ident="xpath2"/>
        <valItem ident="xpath3"/>
        <valItem ident="xpath31"/>
        <valItem ident="xquery"/>
        <valItem ident="xquery3"/>
        <valItem ident="xquery31"/>
      </valList>
      <remarks ident="constraintDecl-attr.queryBinding-remarks" versionDate="2023-03-09" xml:lang="en">
        <p>The suggested values above are the values reserved by the
        Schematron specification. Only <val>exslt</val>,
        <val>stx</val>, <val>xslt</val>, <val>xslt2</val>,
        <val>xslt3</val>, <val>xpath2</val>, and <val>xpath3</val> are
        defined by the specification. Most processors only support one
        or more of <val>xslt</val>, <val>xslt2</val>, and
        <val>xslt3</val>.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples">
      <constraintDecl scheme="schematron" queryBinding="xslt3">
        <sch:ns prefix="wwp" uri="http://www.wwp.northeastern.edu/ns/textbase"/>
      </constraintDecl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDTAGCONS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2023-03-09" xml:lang="en">constraint declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2023-03-09" xml:lang="en">contains declarations pertaining to formal constraints expressed elsewhere in <gi>constraintSpec</gi> elements</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
    <!-- <constraintDecl> is part of content of <schemaSpec> directly, not via a class -->
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identEquiv"/>
        <classRef key="model.descLike"/>
      </alternate>
      <anyElement minOccurs="0" maxOccurs="unbounded"/>             <!-- typically <sch:ns> elements -->
    </sequence>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="one-constraintDecl-per-scheme" xml:lang="en">
    <!-- Note: the “not a descendant of <egXML>” predicate on the
         XPath defining $schemes is required for the P5 build process,
         not for normal users. (In P5 build validity of <egXML>s are
         tested by changing their namespace to TEI, so the tei: prefix
         is not sufficient.) —Syd, 2024-09-19 -->
    <constraint>
      <sch:rule context="/*[ count( //tei:constraintDecl ) gt 1 ]">
        <sch:let name="schemes" value="//tei:constraintDecl[ not(ancestor::*[local-name(.) eq 'egXML'] ) ]/@scheme"/>
        <sch:let name="disctinct_schemes" value="distinct-values( $schemes )"/>
        <sch:assert test="count( $schemes ) eq count( $disctinct_schemes )">
          Each &lt;constraintDecl&gt; element should have a @scheme attribute that is distinct from that of all the other &lt;constraintDecl&gt;s.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2023-03-09" xml:lang="en">supplies the name of the language to which the declarations herein apply</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="schematron">
          <gloss versionDate="2016-09-27" xml:lang="en">ISO Schematron</gloss>
        </valItem>
      </valList>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="constraintDecl-attr.scheme-remarks" versionDate="2023-03-09" xml:lang="en">
        <p>The declarations contained in a particular
        <gi>constraintDecl</gi> (including <att>queryBinding</att>, if
        present) apply to the <gi>constraintSpec</gi> elements whose
        <att>scheme</att> matches the <att>scheme</att> of the
        <gi>constraintDecl</gi>.</p>
      </remarks>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss xml:lang="en" versionDate="2023-03-09">query language binding</gloss>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc xml:lang="en" versionDate="2023-03-09">specifies the query
      language binding for rule-based schema expressions in
      <gi>constraintSpec</gi> elements that have a matching
      <att>scheme</att> attribute</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="exslt"/>
        <valItem ident="stx"/>
        <valItem ident="xslt"/>
        <valItem ident="xslt2"/>
        <valItem ident="xslt3"/>
        <valItem ident="xpath"/>
        <valItem ident="xpath2"/>
        <valItem ident="xpath3"/>
        <valItem ident="xpath31"/>
        <valItem ident="xquery"/>
        <valItem ident="xquery3"/>
        <valItem ident="xquery31"/>
      </valList>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="constraintDecl-attr.queryBinding-remarks" versionDate="2023-03-09" xml:lang="en">
        <p>The suggested values above are the values reserved by the
        Schematron specification. Only <val>exslt</val>,
        <val>stx</val>, <val>xslt</val>, <val>xslt2</val>,
        <val>xslt3</val>, <val>xpath2</val>, and <val>xpath3</val> are
        defined by the specification. Most processors only support one
        or more of <val>xslt</val>, <val>xslt2</val>, and
        <val>xslt3</val>.</p>
      </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples">
      <constraintDecl scheme="schematron" queryBinding="xslt3">
        <sch:ns prefix="wwp" uri="http://www.wwp.northeastern.edu/ns/textbase"/>
      </constraintDecl>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAGCONS"/>
  </listRef>
```

^b16

