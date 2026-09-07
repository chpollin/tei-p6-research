---
type: representation
source-type: document
source: '[[00_sources/tei-p5-dataref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 dataRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/dataRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# dataRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6146. Git blob: `d4d450ac95568afacd8b70b39de7d4045c860094`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-dataRef" ident="dataRef">
  <desc versionDate="2010-05-14" xml:lang="en">identifies the datatype of an attribute value, either by referencing an item in an externally defined datatype library, or by
    pointing to a TEI-defined data specification</desc>
  <desc versionDate="2024-09-02" xml:lang="ja">外部で定義されたデータ型ライブラリ内の項目を参照するか、もしくはTEIにより定義されたデータ仕様を指し示すことで、属性値のデータ型を識別する</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.contentPart"/>
    <memberOf key="model.oddRef"/>
  </classes>
  <content>
    <elementRef minOccurs="0" maxOccurs="unbounded" key="dataFacet"/>
  </content>
  <constraintSpec ident="restrictDataFacet" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:dataRef[tei:dataFacet]">
        <sch:assert test="@name" role="nonfatal">Data facets can only be specified for references to datatypes specified by
          XML Schema Part 2: Datatypes Second Edition — that is, for there to be a &lt;dataFacet> child there must be a @name attribute.</sch:assert>
        <sch:report test="@restriction" role="nonfatal">Data facets and restrictions cannot both be expressed on the same data reference — that is, the @restriction attribute cannot be used when a &lt;dataFacet> child element is present.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="restrictAttResctrictionName" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:dataRef[@restriction]">
        <sch:assert test="@name" role="nonfatal">Restrictions can only be specified for references to datatypes specified by
          XML Schema Part 2: Datatypes Second Edition — that is, for there to be a @restriction attribute there must be a @name attribute, too.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attList org="choice">
      <attDef ident="key" usage="req">
        <desc versionDate="2010-05-14" xml:lang="en">the identifier used for this datatype specification</desc>
        <desc versionDate="2024-09-02" xml:lang="ja">このデータ型仕様に使われる識別子</desc>
        <datatype><dataRef key="teidata.xmlName"/></datatype>
      </attDef>
      <attDef ident="name" usage="req">
        <desc versionDate="2010-05-14" xml:lang="en">the name of a datatype in the list provided by 
        <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref></desc>
        <desc versionDate="2024-09-02" xml:lang="ja"><ref target="#XSD2">XML Schemas: Part 2: Datatypes</ref>で提供されているリスト内のデータ型の名前</desc>
        <datatype><dataRef key="teidata.xmlName"/></datatype>
      </attDef>
      <attDef ident="ref" usage="req">
        <desc versionDate="2010-05-14" xml:lang="en">a pointer to a datatype defined in some datatype library</desc>
        <desc versionDate="2024-09-02" xml:lang="ja">あるデータ型ライブラリ内で定義されたデータ型へのポインタ</desc>
        <datatype><dataRef key="teidata.pointer"/></datatype>
      </attDef>
    </attList>
    <attDef ident="restriction">
      <desc versionDate="2012-12-04" xml:lang="en">supplies a string representing a regular expression providing additional constraints 
      on the strings used to represent values of this datatype</desc>
      <desc versionDate="2024-09-02" xml:lang="ja">このデータ型の値を表すために使用される文字列に追加の制約を加える正規表現を表す文字列を提供する</desc>
     <datatype><dataRef key="teidata.pattern"/></datatype>
   </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataRef-egXML-ts" source="#UND">
      <schemaSpec ident="myTEI" source="http://www.tei-c.org/Vault/P5/current/xml/tei/odd/p5subset.xml">
        <!-- ... -->
        <dataRef key="teidata.enumerated"/>
        <!-- ... -->
      </schemaSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataRef-egXML-zp" source="#UND">
      <schemaSpec ident="myTEI" source="http://www.tei-c.org/Vault/P5/current/xml/tei/odd/p5subset.xml">
        <!-- ... -->
        <dataRef name="float"/>
        <!-- ... -->
      </schemaSpec>
    </egXML></exemplum>
    <exemplum xml:lang="und">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataRef-egXML-rg">
        <dataSpec ident="data.integerExample">
          <desc>datatype used for attributes taking an integer value between 0 and 99</desc>     
     <content>   <dataRef name="nonNegativeInteger" restriction="[0-9][0-9]?"/>
    </content>    </dataSpec>
      </egXML>
    </exemplum>
    
  <remarks ident="dataRef-remarks" versionDate="2010-05-14" xml:lang="en">
    <p>Only one of the attributes <att>key</att>, <att>name</att>, and <att>ref</att> may be used on any given instance of <gi>dataRef</gi>.</p>
    <p>Neither a <att>restriction</att> attribute nor a <gi>dataFacet</gi> child element may be used unless the <gi>dataRef</gi> refers to a datatype from the specification <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref> with a <att>name</att> attribute.</p>
  </remarks>
  <remarks ident="dataRef-remarks" versionDate="2024-09-02" xml:lang="ja"><p> <att>key</att>、<att>name</att>、<att>ref</att>の内どれか一つの属性のみを使用することができる</p></remarks>
  <listRef>
    <ptr target="#TD-datatypes"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2010-05-14" xml:lang="en">identifies the datatype of an attribute value, either by referencing an item in an externally defined datatype library, or by
    pointing to a TEI-defined data specification</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">外部で定義されたデータ型ライブラリ内の項目を参照するか、もしくはTEIにより定義されたデータ仕様を指し示すことで、属性値のデータ型を識別する</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.contentPart"/>
    <memberOf key="model.oddRef"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <elementRef minOccurs="0" maxOccurs="unbounded" key="dataFacet"/>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="restrictDataFacet" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:dataRef[tei:dataFacet]">
        <sch:assert test="@name" role="nonfatal">Data facets can only be specified for references to datatypes specified by
          XML Schema Part 2: Datatypes Second Edition — that is, for there to be a &lt;dataFacet> child there must be a @name attribute.</sch:assert>
        <sch:report test="@restriction" role="nonfatal">Data facets and restrictions cannot both be expressed on the same data reference — that is, the @restriction attribute cannot be used when a &lt;dataFacet> child element is present.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b5

### Block 6

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="restrictAttResctrictionName" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:dataRef[@restriction]">
        <sch:assert test="@name" role="nonfatal">Restrictions can only be specified for references to datatypes specified by
          XML Schema Part 2: Datatypes Second Edition — that is, for there to be a @restriction attribute there must be a @name attribute, too.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2010-05-14" xml:lang="en">the identifier used for this datatype specification</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">このデータ型仕様に使われる識別子</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2010-05-14" xml:lang="en">the name of a datatype in the list provided by 
        <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref></desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja"><ref target="#XSD2">XML Schemas: Part 2: Datatypes</ref>で提供されているリスト内のデータ型の名前</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2010-05-14" xml:lang="en">a pointer to a datatype defined in some datatype library</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">あるデータ型ライブラリ内で定義されたデータ型へのポインタ</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-12-04" xml:lang="en">supplies a string representing a regular expression providing additional constraints 
      on the strings used to represent values of this datatype</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">このデータ型の値を表すために使用される文字列に追加の制約を加える正規表現を表す文字列を提供する</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pattern"/></datatype>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataRef-egXML-ts" source="#UND">
      <schemaSpec ident="myTEI" source="http://www.tei-c.org/Vault/P5/current/xml/tei/odd/p5subset.xml">
        <!-- ... -->
        <dataRef key="teidata.enumerated"/>
        <!-- ... -->
      </schemaSpec>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataRef-egXML-zp" source="#UND">
      <schemaSpec ident="myTEI" source="http://www.tei-c.org/Vault/P5/current/xml/tei/odd/p5subset.xml">
        <!-- ... -->
        <dataRef name="float"/>
        <!-- ... -->
      </schemaSpec>
    </egXML></exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="und">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dataRef-egXML-rg">
        <dataSpec ident="data.integerExample">
          <desc>datatype used for attributes taking an integer value between 0 and 99</desc>     
     <content>   <dataRef name="nonNegativeInteger" restriction="[0-9][0-9]?"/>
    </content>    </dataSpec>
      </egXML>
    </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="dataRef-remarks" versionDate="2010-05-14" xml:lang="en">
    <p>Only one of the attributes <att>key</att>, <att>name</att>, and <att>ref</att> may be used on any given instance of <gi>dataRef</gi>.</p>
    <p>Neither a <att>restriction</att> attribute nor a <gi>dataFacet</gi> child element may be used unless the <gi>dataRef</gi> refers to a datatype from the specification <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref> with a <att>name</att> attribute.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="dataRef-remarks" versionDate="2024-09-02" xml:lang="ja"><p> <att>key</att>、<att>name</att>、<att>ref</att>の内どれか一つの属性のみを使用することができる</p></remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD-datatypes"/>
  </listRef>
```

^b24

