---
type: representation
source-type: document
source: '[[00_sources/tei-p5-datafacet-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 dataFacet
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/dataFacet.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# dataFacet

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3697. Git blob: `7225887b9c4c401af601a5e5ba5f16b591f277e0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-dataFacet" ident="dataFacet">
  <desc versionDate="2016-11-21" xml:lang="en">restricts the value of the strings used to represent values of a datatype, 
    according to <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>.</desc>
  <desc versionDate="2024-09-02" xml:lang="ja"><ref target="#XSD2">XML Schemas: Part 2: Datatypes</ref>に従って、データ型の値を表すために使用される文字列の値を制限する。</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content><empty/></content>
  <attList>
      <attDef ident="name" usage="req">
        <desc versionDate="2016-11-21" xml:lang="en">the name of the facet.</desc>
        <desc versionDate="2024-09-02" xml:lang="ja">ファセットの名前</desc>
        <datatype><dataRef key="teidata.word"/></datatype>
        <valList type="closed">
          <valItem ident="length"/>
          <valItem ident="minLength"/>
          <valItem ident="maxLength"/>
          <valItem ident="pattern"/>
          <valItem ident="enumeration"/>
          <valItem ident="whiteSpace"/>
          <valItem ident="maxInclusive"/>
          <valItem ident="minInclusive"/>
          <valItem ident="maxExclusive"/>
          <valItem ident="minExclusive"/>
          <valItem ident="totalDigits"/>
          <valItem ident="fractionDigits"/> 
        </valList>
      </attDef>
      <attDef ident="value" usage="req">
        <desc versionDate="2016-11-21" xml:lang="en">the facet value.</desc>
        <desc versionDate="2024-09-02" xml:lang="ja">ファセット値</desc>
        <datatype><dataRef name="string"/></datatype>
      </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataFacet-egXML-fb" source="#UND">
      <datatype>
        <dataRef name="decimal">
          <dataFacet name="maxInclusive" value="360.0"/>
          <dataFacet name="minInclusive" value="-360.0"/>
        </dataRef>
      </datatype>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataFacet-egXML-oc">
      <dataSpec ident="data.integerExample">
        <desc>datatype used for attributes taking an integer value between 0 and 99</desc>     
        <content>   
          <dataRef name="nonNegativeInteger">
            <dataFacet name="maxInclusive" value="99"/>
            <dataFacet name="minInclusive" value="0"/>
          </dataRef>
        </content>    
      </dataSpec>
    </egXML>
  </exemplum>
  <remarks ident="dataFacet-remarks" versionDate="2016-11-21" xml:lang="en">
    <p>This element is only allowed when the parent <gi>dataRef</gi> refers with
        <att>name</att> to a datatype from the specification <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>. 
    </p>
  </remarks>
  <remarks ident="dataFacet-remarks" versionDate="2024-09-02" xml:lang="ja"><p>この要素は、親<gi>dataRef</gi>が<att>name</att>によって、<ref target="#XSD2">XML Schemas: Part 2: Datatypes</ref>の仕様書からデータ型を参照する場合にのみ許される。</p></remarks>
  <listRef>
    <ptr target="#TD-datatypes"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-11-21" xml:lang="en">restricts the value of the strings used to represent values of a datatype, 
    according to <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja"><ref target="#XSD2">XML Schemas: Part 2: Datatypes</ref>に従って、データ型の値を表すために使用される文字列の値を制限する。</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2016-11-21" xml:lang="en">the name of the facet.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">ファセットの名前</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
          <valItem ident="length"/>
          <valItem ident="minLength"/>
          <valItem ident="maxLength"/>
          <valItem ident="pattern"/>
          <valItem ident="enumeration"/>
          <valItem ident="whiteSpace"/>
          <valItem ident="maxInclusive"/>
          <valItem ident="minInclusive"/>
          <valItem ident="maxExclusive"/>
          <valItem ident="minExclusive"/>
          <valItem ident="totalDigits"/>
          <valItem ident="fractionDigits"/> 
        </valList>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2016-11-21" xml:lang="en">the facet value.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">ファセット値</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef name="string"/></datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataFacet-egXML-fb" source="#UND">
      <datatype>
        <dataRef name="decimal">
          <dataFacet name="maxInclusive" value="360.0"/>
          <dataFacet name="minInclusive" value="-360.0"/>
        </dataRef>
      </datatype>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataFacet-egXML-oc">
      <dataSpec ident="data.integerExample">
        <desc>datatype used for attributes taking an integer value between 0 and 99</desc>     
        <content>   
          <dataRef name="nonNegativeInteger">
            <dataFacet name="maxInclusive" value="99"/>
            <dataFacet name="minInclusive" value="0"/>
          </dataRef>
        </content>    
      </dataSpec>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="dataFacet-remarks" versionDate="2016-11-21" xml:lang="en">
    <p>This element is only allowed when the parent <gi>dataRef</gi> refers with
        <att>name</att> to a datatype from the specification <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>. 
    </p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="dataFacet-remarks" versionDate="2024-09-02" xml:lang="ja"><p>この要素は、親<gi>dataRef</gi>が<att>name</att>によって、<ref target="#XSD2">XML Schemas: Part 2: Datatypes</ref>の仕様書からデータ型を参照する場合にのみ許される。</p></remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD-datatypes"/>
  </listRef>
```

^b16

