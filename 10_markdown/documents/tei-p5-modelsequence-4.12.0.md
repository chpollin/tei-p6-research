---
type: representation
source-type: document
source: '[[00_sources/tei-p5-modelsequence-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 modelSequence
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/modelSequence.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# modelSequence

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3820. Git blob: `d5d361d2c2a4e6fa087453af83d2c52acb694448`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="modelSequence" xml:id="gi-modelSequence" module="tagdocs">
  <desc versionDate="2017-02-07" xml:lang="en">any sequence of model or <gi>modelSequence</gi> elements which is to be processed as a single set of actions.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identEquiv"/>
        <classRef key="model.descLike"/>
      </alternate>
      <elementRef key="model" minOccurs="2" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="no_outputs_nor_predicates_4_my_kids" xml:lang="en">
    <constraint>
      <sch:rule context="tei:modelSequence">
        <sch:report test="tei:model[@output]" role="warning">The &lt;model&gt; children
        of a &lt;modelSequence&gt; element inherit the @output attribute of the
        parent &lt;modelSequence&gt;, and thus should not have their own.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="predicate" usage="opt">
      <desc versionDate="2015-05-15" xml:lang="en">the condition under which this model applies given as an XPath Predicate Expression.</desc>
      <datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
    </attDef>
    <attDef ident="useSourceRendition" usage="opt">
      <desc versionDate="2015-05-15" xml:lang="en">whether to obey any rendition attribute that is present.</desc>
      <datatype>
        <dataRef key="teidata.truthValue"/>
      </datatype>
    </attDef>
    <attDef ident="output" usage="opt">
      <desc versionDate="2015-05-15" xml:lang="en">the intended output method.</desc>
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="semi">
        <valItem ident="web">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a web format</desc>
        </valItem>
        <valItem ident="print">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a print format</desc>
        </valItem>
        <valItem ident="plaintext">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a plain text format</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-modelSequence-egXML-oj" source="#UND">
      <modelGrp output="print">
        <modelSequence>
          <model behaviour="inline">
            <param name="content" value="@n"/>
          </model>
          <model behaviour="footnote">
            <param name="place" value="'foot'"/>
          </model>
        </modelSequence>
      </modelGrp>
    </egXML>
  </exemplum>
  <remarks ident="modelSequence-remarks" versionDate="2016-11-21" xml:lang="en">
    <p>All of the <gi>model</gi> elements inside a <gi>modelSequence</gi> 
      element must be processed. The operations indicated by each <gi>model</gi> 
      child cannot be dependent on any other operation in the sequence. The results 
      must be rendered in the order given by the list of <gi>model</gi>s in the 
      <gi>modelSequence</gi>.</p>
  </remarks>
  <listRef>
    <ptr target="#TDPMMS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">any sequence of model or <gi>modelSequence</gi> elements which is to be processed as a single set of actions.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identEquiv"/>
        <classRef key="model.descLike"/>
      </alternate>
      <elementRef key="model" minOccurs="2" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="no_outputs_nor_predicates_4_my_kids" xml:lang="en">
    <constraint>
      <sch:rule context="tei:modelSequence">
        <sch:report test="tei:model[@output]" role="warning">The &lt;model&gt; children
        of a &lt;modelSequence&gt; element inherit the @output attribute of the
        parent &lt;modelSequence&gt;, and thus should not have their own.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2015-05-15" xml:lang="en">the condition under which this model applies given as an XPath Predicate Expression.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.xpath"/>
      </datatype>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2015-05-15" xml:lang="en">whether to obey any rendition attribute that is present.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.truthValue"/>
      </datatype>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2015-05-15" xml:lang="en">the intended output method.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[3]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="web">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a web format</desc>
        </valItem>
        <valItem ident="print">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a print format</desc>
        </valItem>
        <valItem ident="plaintext">
          <desc versionDate="2015-05-15" xml:lang="en">the output is intended for presentation in a plain text format</desc>
        </valItem>
      </valList>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-modelSequence-egXML-oj" source="#UND">
      <modelGrp output="print">
        <modelSequence>
          <model behaviour="inline">
            <param name="content" value="@n"/>
          </model>
          <model behaviour="footnote">
            <param name="place" value="'foot'"/>
          </model>
        </modelSequence>
      </modelGrp>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="modelSequence-remarks" versionDate="2016-11-21" xml:lang="en">
    <p>All of the <gi>model</gi> elements inside a <gi>modelSequence</gi> 
      element must be processed. The operations indicated by each <gi>model</gi> 
      child cannot be dependent on any other operation in the sequence. The results 
      must be rendered in the order given by the list of <gi>model</gi>s in the 
      <gi>modelSequence</gi>.</p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDPMMS"/>
  </listRef>
```

^b14

