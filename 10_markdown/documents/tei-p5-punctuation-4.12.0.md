---
type: representation
source-type: document
source: '[[00_sources/tei-p5-punctuation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 punctuation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/punctuation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# punctuation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4150. Git blob: `b81bc47aca48d2f489e3b8a2a989fb8ef8b24c69`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-punctuation" ident="punctuation">
  <desc versionDate="2013-06-20" xml:lang="en">specifies editorial practice adopted with respect to punctuation marks in the original.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>    
    <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="punctuation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:punctuation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="marks" usage="opt">
      <desc versionDate="2013-06-20" xml:lang="en">indicates whether or not punctation marks have been retained as content within the text.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="none">
          <desc versionDate="2013-06-20" xml:lang="en">no punctuation marks have been retained</desc>
        </valItem>
        <valItem ident="some">
          <desc versionDate="2013-06-20" xml:lang="en">some punctuation marks have been retained</desc>
        </valItem>
        <valItem ident="all">
          <desc versionDate="2013-06-20" xml:lang="en">all punctuation marks have been retained</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="placement" usage="opt">
      <desc versionDate="2018-01-16" xml:lang="en"> indicates the positioning of punctuation marks that are associated with marked up text as being encoded within the element surrounding the text or immediately before or after it.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="internal">
          <desc versionDate="2018-01-16" xml:lang="en">punctuation marks found at the start or end of a marked up text component are included within its surrounding element;</desc>
        </valItem>
        <valItem ident="external">
          <desc versionDate="2018-01-16" xml:lang="en">punctuation marks found at the start or end of a marked up text component appear immediately before or after the surrounding element</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-punctuation-egXML-fl">
      <punctuation marks="all" placement="internal">
        <p>All punctuation marks in the source text have been retained and represented using the
          appropriate Unicode code point. In cases where a punctuation mark and nearby markup convey
          the same information (for example, a sentence ends with a question mark and is also tagged
          as <gi>s</gi>) the punctuation mark is captured as content within the element.</p>
      </punctuation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>External placement of punctuation:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-punctuation-egXML-qm" source="#MLK01">
      <p>I would agree with Saint Augustine that “<quote>An unjust law is no law at all</quote>.”</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>Internal placement of punctuation:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-punctuation-egXML-xn" source="#MLK01">
      <p>I would agree with Saint Augustine that <quote>“An unjust law is no law at all.”</quote></p>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD53"/>
    <ptr target="#COPU"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-06-20" xml:lang="en">specifies editorial practice adopted with respect to punctuation marks in the original.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>    
    <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="punctuation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:punctuation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-06-20" xml:lang="en">indicates whether or not punctation marks have been retained as content within the text.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="none">
          <desc versionDate="2013-06-20" xml:lang="en">no punctuation marks have been retained</desc>
        </valItem>
        <valItem ident="some">
          <desc versionDate="2013-06-20" xml:lang="en">some punctuation marks have been retained</desc>
        </valItem>
        <valItem ident="all">
          <desc versionDate="2013-06-20" xml:lang="en">all punctuation marks have been retained</desc>
        </valItem>
      </valList>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2018-01-16" xml:lang="en"> indicates the positioning of punctuation marks that are associated with marked up text as being encoded within the element surrounding the text or immediately before or after it.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="internal">
          <desc versionDate="2018-01-16" xml:lang="en">punctuation marks found at the start or end of a marked up text component are included within its surrounding element;</desc>
        </valItem>
        <valItem ident="external">
          <desc versionDate="2018-01-16" xml:lang="en">punctuation marks found at the start or end of a marked up text component appear immediately before or after the surrounding element</desc>
        </valItem>
      </valList>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-punctuation-egXML-fl">
      <punctuation marks="all" placement="internal">
        <p>All punctuation marks in the source text have been retained and represented using the
          appropriate Unicode code point. In cases where a punctuation mark and nearby markup convey
          the same information (for example, a sentence ends with a question mark and is also tagged
          as <gi>s</gi>) the punctuation mark is captured as content within the element.</p>
      </punctuation>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <p>External placement of punctuation:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-punctuation-egXML-qm" source="#MLK01">
      <p>I would agree with Saint Augustine that “<quote>An unjust law is no law at all</quote>.”</p>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <p>Internal placement of punctuation:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-punctuation-egXML-xn" source="#MLK01">
      <p>I would agree with Saint Augustine that <quote>“An unjust law is no law at all.”</quote></p>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#COPU"/>
  </listRef>
```

^b14

