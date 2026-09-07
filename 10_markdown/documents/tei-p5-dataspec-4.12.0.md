---
type: representation
source-type: document
source: '[[00_sources/tei-p5-dataspec-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 dataSpec
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/dataSpec.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# dataSpec

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2637. Git blob: `df1c16b82f21fd2e2113b390eef0368bfd30f13b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-dataSpec" ident="dataSpec">
  <gloss versionDate="2007-07-04" xml:lang="en">datatype specification</gloss>
  <gloss versionDate="2024-09-02" xml:lang="ja">データ型の指定</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">documents a datatype.</desc>
  <desc versionDate="2024-09-02" xml:lang="ja">データ型を記述する。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identSynonyms"/>
        <classRef key="model.descLike"/>
      </alternate> 
      <alternate minOccurs="0" maxOccurs="1">
        <elementRef key="content"/> 
        <elementRef key="valList"/> 
      </alternate>
      <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="no_elements_in_data_content" xml:lang="en">
    <constraint>
      <sch:rule role="warn" context="tei:dataSpec/tei:content">
        <sch:report test=".//tei:anyElement | .//tei:classRef | .//tei:elementRef">
          A datatype specification should not refer to an element or a class.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataSpec-egXML-kh">
      <dataSpec ident="teidata.pointer">
        <desc versionDate="2013-01-19" xml:lang="en">defines the range of
        attribute values used to provide a single URI, absolute or relative,
        pointing to some other resource, either within the current document
        or elsewhere.</desc>
        <content>
          <dataRef name="anyURI"/>
        </content>
      </dataSpec>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDcrystals"/>
    <ptr target="#TDENT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">datatype specification</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2024-09-02" xml:lang="ja">データ型の指定</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">documents a datatype.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">データ型を記述する。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="model.oddDecl"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identSynonyms"/>
        <classRef key="model.descLike"/>
      </alternate> 
      <alternate minOccurs="0" maxOccurs="1">
        <elementRef key="content"/> 
        <elementRef key="valList"/> 
      </alternate>
      <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="no_elements_in_data_content" xml:lang="en">
    <constraint>
      <sch:rule role="warn" context="tei:dataSpec/tei:content">
        <sch:report test=".//tei:anyElement | .//tei:classRef | .//tei:elementRef">
          A datatype specification should not refer to an element or a class.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataSpec-egXML-kh">
      <dataSpec ident="teidata.pointer">
        <desc versionDate="2013-01-19" xml:lang="en">defines the range of
        attribute values used to provide a single URI, absolute or relative,
        pointing to some other resource, either within the current document
        or elsewhere.</desc>
        <content>
          <dataRef name="anyURI"/>
        </content>
      </dataSpec>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDcrystals"/>
    <ptr target="#TDENT"/>
  </listRef>
```

^b9

