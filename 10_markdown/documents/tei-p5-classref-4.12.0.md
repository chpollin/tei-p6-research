---
type: representation
source-type: document
source: '[[00_sources/tei-p5-classref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 classRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/classRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# classRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8414. Git blob: `00cb7a4c4918d0ed20f340cda5ec9a95abb02f97`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-classRef" ident="classRef">
  <desc versionDate="2010-07-06" xml:lang="en">points to the specification for an attribute or model class which is to be included in a schema.</desc>
  <desc versionDate="2024-02-28" xml:lang="ja">スキーマに含まれる属性クラスあるいはモデルクラスの仕様を指し示す。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
    <memberOf key="model.oddRef"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="key" usage="req">
      <desc versionDate="2010-07-06" xml:lang="en">the identifier used for the required class within the
        source indicated.</desc>
      <desc versionDate="2024-02-28" xml:lang="ja">指示されたソースの中の要求されたクラスに対して使用される識別子。</desc>
      <datatype><dataRef key="teidata.xmlName"/></datatype>
    </attDef>
    <attDef ident="expand" usage="opt">
      <desc versionDate="2013-11-21" xml:lang="en">indicates how references
      to this class within a content model should be interpreted.</desc>
      <desc versionDate="2024-02-28" xml:lang="ja">内容モデル内でこのクラスへの参照がどのように解釈されるべきなのかを示す。</desc>
      <valList type="closed">
        <valItem ident="alternation">
          <desc versionDate="2013-11-21" xml:lang="en">any one member of the class may appear</desc>
          <desc versionDate="2024-02-24" xml:lang="ja">クラスのいずれかのメンバーが出現し得る。</desc>
        </valItem>
        <valItem ident="sequence">
          <desc versionDate="2013-11-21" xml:lang="en">a single occurrence
          of all members of the class may appear in sequence</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスのすべてのメンバーが順に1回ずつ出現し得る。</desc>
        </valItem>
        <valItem ident="sequenceOptional">
          <desc versionDate="2013-11-21" xml:lang="en">a single occurrence of
          one or more members
          of the class may appear in sequence</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスの1つ以上のメンバーが順に1回ずつ出現し得る。</desc>
        </valItem>
        <valItem ident="sequenceOptionalRepeatable">
          <desc versionDate="2013-11-21" xml:lang="en">one or more
          occurrences of one or more members of the class
          may appear in sequence.</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスの1つまたは複数のメンバーが1回以上、順に出現し得る。</desc>
        </valItem>
        <valItem ident="sequenceRepeatable">
          <desc versionDate="2013-11-21" xml:lang="en">one or more
          occurrences of all members of the class may appear in sequence</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスのすべてのメンバーが1回以上、順に出現し得る。</desc>
        </valItem>
      </valList>
      <remarks ident="classRef-attr.expand-remarks" versionDate="2013-11-20" xml:lang="en">
	<!-- Encoding (and whitespace) updated 2019-07-07 w/ no change to text -->
	<p>If the members of the class are <ident>a</ident>,
	<ident>b</ident> and <ident>c</ident>, then a reference to the
	class within a content model is understood as being a
	reference to <code>a|b|c</code> when <att>expand</att> is
	omitted or has the value <val>alternation</val>; to
	<code>a,b,c</code> when it has the value <val>sequence</val>;
	to <code>(a?,b?,c?)</code> when it has the value
	<val>sequenceOptional</val>; to <code>(a*,b*,c*)</code> when
	it has the value <val>sequenceOptionalRepeatable</val>; or to
	<code>(a+,b+,c+)</code> when it has the value
	<val>sequenceRepeatable</val>.</p>
      </remarks>
      <remarks ident="classRef-attr.expand-remarks" versionDate="2024-02-28" xml:lang="ja"><p>クラスのメンバーが <val>a</val>、<val>b</val>そして<val>c</val>であるとして、
        <att>expand</att>の値が<val>alternation</val>ならば、内容モデル内の該当クラスへの参照は，<val>a|b|c</val>への参照として理解される。
        また、<att>expand</att>の値が<val>sequence</val>ならば、<val>a,b,c</val>への，<val>sequenceOptional</val>ならば<val>(a?,b?,c?)</val>への、
        <val>sequenceOptionalRepeatable</val>ならば<val>(a*,b*,c*)</val>への、そして<val>sequenceRepeatable</val>ならば<val>(a+,b+,c+)</val>への参照としてそれぞれ理解される。</p></remarks>
    </attDef>
    <attList org="choice">
      <attDef ident="include">
        <desc versionDate="2011-09-21" xml:lang="en">supplies a list of class members which are to be included in the schema being defined.</desc>
        <desc versionDate="2024-02-28" xml:lang="ja">定義されているスキーマに含まれるクラスメンバーのリスト。</desc>
        <datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
      </attDef>
      <attDef ident="except">
        <desc versionDate="2011-09-21" xml:lang="en">supplies a list of class members which are to be excluded from the schema being defined.</desc>
        <desc versionDate="2024-02-28" xml:lang="ja">定義されているスキーマから除外するクラスメンバーのリスト。</desc>
        <datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
      </attDef>     
    </attList>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classRef-egXML-uc" source="#UND">
      <schemaSpec ident="myTEIe" start="TEI">
        <moduleRef key="tei"/>
        <moduleRef key="core" include="abbr add core addrLine address author bibl biblScope choice cit corr date del desc divGen editor emph expan foreign gap gloss graphic head hi index item l label lb lg list listBibl mentioned milestone name note num orig p pb ptr pubPlace publisher q ref reg relatedItem resp respStmt rs sic soCalled sp speaker stage teiCorpus term time title unclear"/>
        <moduleRef key="header" include="authority availability catRef category change classCode classDecl creation distributor edition editionStmt editorialDecl encodingDesc extent fileDesc funder idno keywords langUsage language licence notesStmt principal profileDesc projectDesc publicationStmt refsDecl revisionDesc samplingDecl seriesStmt sourceDesc sponsor taxonomy teiHeader textClass titleStmt"/>
        <moduleRef key="textstructure" include="TEI argument back body byline closer dateline div docAuthor docDate docEdition docImprint docTitle epigraph front group opener postscript salute signed text titlePage titlePart trailer"/>
        <classRef key="att.global.facs"/>
      </schemaSpec>
    </egXML>
  </exemplum>
  <remarks ident="classRef-remarks" versionDate="2019-07-07" xml:lang="en">
 <!-- p>If neither <att>include</att> nor <att>except</att> is specified, all class members are included in the schema being defined.</p -->
    <p>Attribute and model classes are identified by the name supplied as value for the
    <att>ident</att> attribute on the <gi>classSpec</gi> element in
    which they are declared. All TEI class names are unique; attribute
    class names conventionally begin with the letters <code>att.</code>.
    </p>
  </remarks>
  <remarks ident="classRef-remarks" versionDate="2024-02-28" xml:lang="ja">
    <p>
      属性クラスとモデルクラスは、それらが宣言された<gi>classSpec</gi>の要素において<att>ident</att>属性の値として指定された名前により、識別される。
      TEI内のすべての名前は一意である。属性クラス名は通常<code>att.</code>という文字ではじまる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TDCLA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2010-07-06" xml:lang="en">points to the specification for an attribute or model class which is to be included in a schema.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">スキーマに含まれる属性クラスあるいはモデルクラスの仕様を指し示す。</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.repeatable"/>
    <memberOf key="model.contentPart"/>
    <memberOf key="model.oddRef"/>
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
<desc versionDate="2010-07-06" xml:lang="en">the identifier used for the required class within the
        source indicated.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">指示されたソースの中の要求されたクラスに対して使用される識別子。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-11-21" xml:lang="en">indicates how references
      to this class within a content model should be interpreted.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">内容モデル内でこのクラスへの参照がどのように解釈されるべきなのかを示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="alternation">
          <desc versionDate="2013-11-21" xml:lang="en">any one member of the class may appear</desc>
          <desc versionDate="2024-02-24" xml:lang="ja">クラスのいずれかのメンバーが出現し得る。</desc>
        </valItem>
        <valItem ident="sequence">
          <desc versionDate="2013-11-21" xml:lang="en">a single occurrence
          of all members of the class may appear in sequence</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスのすべてのメンバーが順に1回ずつ出現し得る。</desc>
        </valItem>
        <valItem ident="sequenceOptional">
          <desc versionDate="2013-11-21" xml:lang="en">a single occurrence of
          one or more members
          of the class may appear in sequence</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスの1つ以上のメンバーが順に1回ずつ出現し得る。</desc>
        </valItem>
        <valItem ident="sequenceOptionalRepeatable">
          <desc versionDate="2013-11-21" xml:lang="en">one or more
          occurrences of one or more members of the class
          may appear in sequence.</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスの1つまたは複数のメンバーが1回以上、順に出現し得る。</desc>
        </valItem>
        <valItem ident="sequenceRepeatable">
          <desc versionDate="2013-11-21" xml:lang="en">one or more
          occurrences of all members of the class may appear in sequence</desc>
          <desc versionDate="2024-02-28" xml:lang="ja">クラスのすべてのメンバーが1回以上、順に出現し得る。</desc>
        </valItem>
      </valList>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="classRef-attr.expand-remarks" versionDate="2013-11-20" xml:lang="en">
	<!-- Encoding (and whitespace) updated 2019-07-07 w/ no change to text -->
	<p>If the members of the class are <ident>a</ident>,
	<ident>b</ident> and <ident>c</ident>, then a reference to the
	class within a content model is understood as being a
	reference to <code>a|b|c</code> when <att>expand</att> is
	omitted or has the value <val>alternation</val>; to
	<code>a,b,c</code> when it has the value <val>sequence</val>;
	to <code>(a?,b?,c?)</code> when it has the value
	<val>sequenceOptional</val>; to <code>(a*,b*,c*)</code> when
	it has the value <val>sequenceOptionalRepeatable</val>; or to
	<code>(a+,b+,c+)</code> when it has the value
	<val>sequenceRepeatable</val>.</p>
      </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="classRef-attr.expand-remarks" versionDate="2024-02-28" xml:lang="ja"><p>クラスのメンバーが <val>a</val>、<val>b</val>そして<val>c</val>であるとして、
        <att>expand</att>の値が<val>alternation</val>ならば、内容モデル内の該当クラスへの参照は，<val>a|b|c</val>への参照として理解される。
        また、<att>expand</att>の値が<val>sequence</val>ならば、<val>a,b,c</val>への，<val>sequenceOptional</val>ならば<val>(a?,b?,c?)</val>への、
        <val>sequenceOptionalRepeatable</val>ならば<val>(a*,b*,c*)</val>への、そして<val>sequenceRepeatable</val>ならば<val>(a+,b+,c+)</val>への参照としてそれぞれ理解される。</p></remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-09-21" xml:lang="en">supplies a list of class members which are to be included in the schema being defined.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">定義されているスキーマに含まれるクラスメンバーのリスト。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2011-09-21" xml:lang="en">supplies a list of class members which are to be excluded from the schema being defined.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">定義されているスキーマから除外するクラスメンバーのリスト。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classRef-egXML-uc" source="#UND">
      <schemaSpec ident="myTEIe" start="TEI">
        <moduleRef key="tei"/>
        <moduleRef key="core" include="abbr add core addrLine address author bibl biblScope choice cit corr date del desc divGen editor emph expan foreign gap gloss graphic head hi index item l label lb lg list listBibl mentioned milestone name note num orig p pb ptr pubPlace publisher q ref reg relatedItem resp respStmt rs sic soCalled sp speaker stage teiCorpus term time title unclear"/>
        <moduleRef key="header" include="authority availability catRef category change classCode classDecl creation distributor edition editionStmt editorialDecl encodingDesc extent fileDesc funder idno keywords langUsage language licence notesStmt principal profileDesc projectDesc publicationStmt refsDecl revisionDesc samplingDecl seriesStmt sourceDesc sponsor taxonomy teiHeader textClass titleStmt"/>
        <moduleRef key="textstructure" include="TEI argument back body byline closer dateline div docAuthor docDate docEdition docImprint docTitle epigraph front group opener postscript salute signed text titlePage titlePart trailer"/>
        <classRef key="att.global.facs"/>
      </schemaSpec>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="classRef-remarks" versionDate="2019-07-07" xml:lang="en">
 <!-- p>If neither <att>include</att> nor <att>except</att> is specified, all class members are included in the schema being defined.</p -->
    <p>Attribute and model classes are identified by the name supplied as value for the
    <att>ident</att> attribute on the <gi>classSpec</gi> element in
    which they are declared. All TEI class names are unique; attribute
    class names conventionally begin with the letters <code>att.</code>.
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="classRef-remarks" versionDate="2024-02-28" xml:lang="ja">
    <p>
      属性クラスとモデルクラスは、それらが宣言された<gi>classSpec</gi>の要素において<att>ident</att>属性の値として指定された名前により、識別される。
      TEI内のすべての名前は一意である。属性クラス名は通常<code>att.</code>という文字ではじまる。
    </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDCLA"/>
  </listRef>
```

^b22

