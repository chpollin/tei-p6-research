---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.repeatable-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.repeatable
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.repeatable.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.repeatable

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5491. Git blob: `b0a880f646f393e27319c2242931288b8ee15f2c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="att.repeatable" type="atts" module="tagdocs">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes for the elements which define
  component parts of a content model.</desc>
  <desc versionDate="2023-09-27" xml:lang="ja">内容モデルの構成部分を定義するエレメントのための属性を提供する。</desc>
  <!-- we know that @minOccurs is castable as an integer, and we know that -->
  <!-- @maxOccurs is either "unbounded" or castable as an integer, because -->
  <!-- they have passed standard grammar-based validation. -->
  <constraintSpec ident="MINandMAXoccurs" scheme="schematron" xml:lang="en">
    <!-- <desc>The value of <att>minOccurs</att> should always be less than or
         equal to that of <att>maxOccurs</att>. Since the default value of
         <att>maxOccurs</att> is 1, when <att>maxOccurs</att> is not specified
         <att>minOccurs</att> must always be less than or equal to 1.</desc> -->
    <constraint>
      <sch:rule context="tei:*[ @minOccurs and @maxOccurs ]">
        <sch:let name="min" value="@minOccurs cast as xs:integer"/>
        <sch:let name="max" value="if ( normalize-space( @maxOccurs ) eq 'unbounded') then -1 else @maxOccurs cast as xs:integer"/>
        <sch:assert test="$max eq -1 or $max ge $min">@maxOccurs should be greater than or equal to @minOccurs.</sch:assert>
      </sch:rule>
      <sch:rule context="tei:*[ @minOccurs and not( @maxOccurs ) ]">
        <sch:assert test="@minOccurs cast as xs:integer lt 2">When @maxOccurs is not specified, @minOccurs must be 0 or 1.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="minOccurs">
      <gloss versionDate="2013-11-21" xml:lang="en">minimum number of occurrences</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">빈도의 최소 수</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW">出現次數最小值</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">nombre minimum d'occurrences</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">numero minimo di occorrenze</gloss>
      <gloss versionDate="2007-05-04" xml:lang="es">número mínimo de apariciones</gloss>
      <gloss versionDate="2023-09-27" xml:lang="ja">最小出現数</gloss>
      <desc versionDate="2013-11-21" xml:lang="en">indicates the smallest number of times this component may occur.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">この部品が出現し得る最小回数を示す。</desc>
      <datatype>
        <dataRef key="teidata.count"/>
      </datatype>
      <defaultVal>1</defaultVal>
    </attDef>
    <attDef ident="maxOccurs">
      <gloss versionDate="2007-12-20" xml:lang="en">maximum number of occurrences</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">빈도의 최대 수</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW">出現次數最大值</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">nombre maximum d'occurrences.</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">numero minimo di occorrenze</gloss>
      <gloss versionDate="2007-05-04" xml:lang="es">número máximo de apariciones.</gloss>
      <gloss versionDate="2023-09-27" xml:lang="ja">最大出現数</gloss>
      <desc versionDate="2013-11-21" xml:lang="en">indicates the largest number of times this component may occur.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">概算推量のための最大推定値を与える。</desc>
      <datatype>
        <dataRef key="teidata.unboundedCount"/>
      </datatype>
      <defaultVal>1</defaultVal>
    </attDef>
  </attList>
  <remarks ident="att.repeatable-remarks" versionDate="2016-12-08" xml:lang="en">
    <p>The value of <att>minOccurs</att> must always be less than or equal to that of
    <att>maxOccurs</att>. Since the default value of <att>maxOccurs</att> is 1, when
    <att>maxOccurs</att> is not specified <att>minOccurs</att> must always be less than or equal
    to 1. The default value of <att>minOccurs</att> is also 1, and therefore, when
    <att>minOccurs</att> is not specified the value of <att>maxOccurs</att> must 
    always be greater than or equal to 1. An ODD processor should raise an error if either of
    these conditions is not met.</p>
  </remarks>
  <remarks ident="att.repeatable-remarks" versionDate="2023-09-27" xml:lang="ja"><p>
  <att>minOccurs</att>の値は常に<att>maxOccurs</att>の値以下でなければならない。<att>maxOccurs</att>のデフォルト値が1なので、<att>maxOccurs</att>が指定されない時には、<att>minOccurs</att>は1以下でなければならない。
    <att>minOccurs</att>のデフォルト値も1なので、<att>minOccurs</att>が指定されない時には、<att>maxOccurs</att>は常に1以上でなければならない。これらの条件のいずれかが満たされなければ、ODDプロセッサはエラーとなるだろう。</p>
  </remarks>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes for the elements which define
  component parts of a content model.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">内容モデルの構成部分を定義するエレメントのための属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="MINandMAXoccurs" scheme="schematron" xml:lang="en">
    <!-- <desc>The value of <att>minOccurs</att> should always be less than or
         equal to that of <att>maxOccurs</att>. Since the default value of
         <att>maxOccurs</att> is 1, when <att>maxOccurs</att> is not specified
         <att>minOccurs</att> must always be less than or equal to 1.</desc> -->
    <constraint>
      <sch:rule context="tei:*[ @minOccurs and @maxOccurs ]">
        <sch:let name="min" value="@minOccurs cast as xs:integer"/>
        <sch:let name="max" value="if ( normalize-space( @maxOccurs ) eq 'unbounded') then -1 else @maxOccurs cast as xs:integer"/>
        <sch:assert test="$max eq -1 or $max ge $min">@maxOccurs should be greater than or equal to @minOccurs.</sch:assert>
      </sch:rule>
      <sch:rule context="tei:*[ @minOccurs and not( @maxOccurs ) ]">
        <sch:assert test="@minOccurs cast as xs:integer lt 2">When @maxOccurs is not specified, @minOccurs must be 0 or 1.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2013-11-21" xml:lang="en">minimum number of occurrences</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">빈도의 최소 수</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">出現次數最小值</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">nombre minimum d'occurrences</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">numero minimo di occorrenze</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">número mínimo de apariciones</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[7]`.

```xml
<gloss versionDate="2023-09-27" xml:lang="ja">最小出現数</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-11-21" xml:lang="en">indicates the smallest number of times this component may occur.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">この部品が出現し得る最小回数を示す。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.count"/>
      </datatype>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>1</defaultVal>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="en">maximum number of occurrences</gloss>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">빈도의 최대 수</gloss>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">出現次數最大值</gloss>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">nombre maximum d'occurrences.</gloss>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">numero minimo di occorrenze</gloss>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">número máximo de apariciones.</gloss>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[7]`.

```xml
<gloss versionDate="2023-09-27" xml:lang="ja">最大出現数</gloss>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-11-21" xml:lang="en">indicates the largest number of times this component may occur.</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">概算推量のための最大推定値を与える。</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.unboundedCount"/>
      </datatype>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>1</defaultVal>
```

^b25

### Block 26

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.repeatable-remarks" versionDate="2016-12-08" xml:lang="en">
    <p>The value of <att>minOccurs</att> must always be less than or equal to that of
    <att>maxOccurs</att>. Since the default value of <att>maxOccurs</att> is 1, when
    <att>maxOccurs</att> is not specified <att>minOccurs</att> must always be less than or equal
    to 1. The default value of <att>minOccurs</att> is also 1, and therefore, when
    <att>minOccurs</att> is not specified the value of <att>maxOccurs</att> must 
    always be greater than or equal to 1. An ODD processor should raise an error if either of
    these conditions is not met.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.repeatable-remarks" versionDate="2023-09-27" xml:lang="ja"><p>
  <att>minOccurs</att>の値は常に<att>maxOccurs</att>の値以下でなければならない。<att>maxOccurs</att>のデフォルト値が1なので、<att>maxOccurs</att>が指定されない時には、<att>minOccurs</att>は1以下でなければならない。
    <att>minOccurs</att>のデフォルト値も1なので、<att>minOccurs</att>が指定されない時には、<att>maxOccurs</att>は常に1以上でなければならない。これらの条件のいずれかが満たされなければ、ODDプロセッサはエラーとなるだろう。</p>
  </remarks>
```

^b27

