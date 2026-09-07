---
type: representation
source-type: document
source: '[[00_sources/tei-p5-citestructure-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 citeStructure
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/citeStructure.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# citeStructure

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4361. Git blob: `eb8f259fd27b4b628018ee04947bd07c1ef04c40`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-citeStructure" ident="citeStructure">
  <gloss versionDate="2020-02-03" xml:lang="en">citation structure</gloss>
  <desc versionDate="2020-02-03" xml:lang="en">declares a structure and method for citing the current document.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citeStructurePart"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="citeData" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="citeStructure" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <attList>
    <attDef ident="delim" usage="opt">
      <gloss versionDate="2020-02-03" xml:lang="en">delimiter</gloss>
      <desc versionDate="2020-02-03" xml:lang="en">supplies a delimiting string preceding the structural component.</desc>
      <datatype>
        <dataRef name="string" restriction=".+"/>
      </datatype>
      <remarks ident="citeStructure-attr.delim-remarks" versionDate="2020-03-24" xml:lang="en">
        <p><att>delim</att> must contain at least one character.</p>
      </remarks>
    </attDef>
    <attDef ident="match" usage="req">
      <gloss versionDate="2020-02-03" xml:lang="en">match</gloss>
      <desc versionDate="2020-02-03" xml:lang="en">supplies an XPath selection pattern using the
        syntax defined in <ptr target="#XSLT3"/> which identifies a set of nodes which are 
        citable structural components. The expression may be absolute (beginning with <code>/</code>) or relative. 
        <att>match</att> on a <gi>citeStructure</gi> without a <gi>citeStructure</gi> parent must be an absolute XPath. If it is
        relative, its context is set by the <att>match</att> of the parent <gi>citeStructure</gi>.</desc>
      <datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
      <constraintSpec ident="citestructure-outer-match" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:citeStructure[not(parent::tei:citeStructure)]">
            <sch:assert test="starts-with(@match,'/')">An XPath in @match on the outer &lt;<sch:name/>> must start with '/'.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <constraintSpec ident="citestructure-inner-match" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:citeStructure[parent::tei:citeStructure]">
            <sch:assert test="not(starts-with(@match,'/'))">An XPath in @match must not start with '/' except on the outer &lt;<sch:name/>>.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </attDef>
    <attDef ident="unit" usage="opt">
      <gloss versionDate="2020-02-03" xml:lang="en">unit</gloss>
      <desc versionDate="2020-02-03" xml:lang="en">describes the structural unit indicated by the <gi>citeStructure</gi>.</desc>
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
        <valItem ident="book"/>
        <valItem ident="chapter"/>
        <valItem ident="entry"/>
        <valItem ident="poem"/>
        <valItem ident="letter"/>
        <valItem ident="line"/>
        <valItem ident="section"/>
        <valItem ident="verse"/>
        <valItem ident="volume"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citeStructure-egXML-ch" source="#UND">
      <citeStructure unit="book" match="//body/div" use="@n">
        <citeStructure unit="chapter" match="div" use="position()" delim=" ">
          <citeStructure unit="verse" match="div" use="position()" delim=":"/>
        </citeStructure>
      </citeStructure>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CORS6"/>
    <ptr target="#SACRCS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-02-03" xml:lang="en">citation structure</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-02-03" xml:lang="en">declares a structure and method for citing the current document.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.citeStructurePart"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="citeData" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="citeStructure" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2020-02-03" xml:lang="en">delimiter</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2020-02-03" xml:lang="en">supplies a delimiting string preceding the structural component.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef name="string" restriction=".+"/>
      </datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="citeStructure-attr.delim-remarks" versionDate="2020-03-24" xml:lang="en">
        <p><att>delim</att> must contain at least one character.</p>
      </remarks>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2020-02-03" xml:lang="en">match</gloss>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2020-02-03" xml:lang="en">supplies an XPath selection pattern using the
        syntax defined in <ptr target="#XSLT3"/> which identifies a set of nodes which are 
        citable structural components. The expression may be absolute (beginning with <code>/</code>) or relative. 
        <att>match</att> on a <gi>citeStructure</gi> without a <gi>citeStructure</gi> parent must be an absolute XPath. If it is
        relative, its context is set by the <att>match</att> of the parent <gi>citeStructure</gi>.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[2]/constraintSpec[1]`.

```xml
<constraintSpec ident="citestructure-outer-match" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:citeStructure[not(parent::tei:citeStructure)]">
            <sch:assert test="starts-with(@match,'/')">An XPath in @match on the outer &lt;<sch:name/>> must start with '/'.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[2]/constraintSpec[2]`.

```xml
<constraintSpec ident="citestructure-inner-match" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:citeStructure[parent::tei:citeStructure]">
            <sch:assert test="not(starts-with(@match,'/'))">An XPath in @match must not start with '/' except on the outer &lt;<sch:name/>>.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2020-02-03" xml:lang="en">unit</gloss>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2020-02-03" xml:lang="en">describes the structural unit indicated by the <gi>citeStructure</gi>.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[3]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="book"/>
        <valItem ident="chapter"/>
        <valItem ident="entry"/>
        <valItem ident="poem"/>
        <valItem ident="letter"/>
        <valItem ident="line"/>
        <valItem ident="section"/>
        <valItem ident="verse"/>
        <valItem ident="volume"/>
      </valList>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-citeStructure-egXML-ch" source="#UND">
      <citeStructure unit="book" match="//body/div" use="@n">
        <citeStructure unit="chapter" match="div" use="position()" delim=" ">
          <citeStructure unit="verse" match="div" use="position()" delim=":"/>
        </citeStructure>
      </citeStructure>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS6"/>
    <ptr target="#SACRCS"/>
  </listRef>
```

^b19

