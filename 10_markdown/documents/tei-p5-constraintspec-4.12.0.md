---
type: representation
source-type: document
source: '[[00_sources/tei-p5-constraintspec-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 constraintSpec
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/constraintSpec.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# constraintSpec

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11921. Git blob: `15ca20f85ab888e65246c473a17abc42e0761a4e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-constraintSpec" ident="constraintSpec">
  <gloss versionDate="2009-06-10" xml:lang="en">constraint on schema</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">スキーマの制約</gloss>
  <desc versionDate="2017-06-24" xml:lang="en">contains a formal constraint, typically expressed in a rule-based schema language, to which a construct must conform in order to be considered valid</desc>
  <desc versionDate="2024-02-28" xml:lang="ja">〔データの〕構造が妥当であるために満たしていなければならない形式的な制約。 通常は規則ベースのスキーマ言語で表現される。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identSynonyms"/>
        <classRef key="model.descLike"/>
      </alternate>
      <elementRef key="constraint" minOccurs="0" maxOccurs="1"/>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="empty-based-on-mode" xml:lang="en">
    <!-- 
         This constraint specification is much like the
         "child-constraint-based-on-mode" for <elementSpec>, which
         does something something similar (in that it is based on
         @mode), but not quite the same.
    -->
    <constraint>
      <sch:rule context="tei:constraintSpec[ @mode eq 'delete']">
        <sch:report test="child::*">This &lt;constraintSpec> element has a @mode of "delete" even though it has child elements. Change the @mode to "add", "change", or "replace", or remove the child elements.</sch:report>
      </sch:rule>
      <sch:rule context="tei:constraintSpec[ @mode eq 'change']">
        <sch:assert test="child::*">This &lt;constraintSpec> element has a @mode of "change", but does not have any child elements. Specify child elements, or change the @mode to "delete".</sch:assert>
      </sch:rule>
      <sch:rule context="tei:constraintSpec[ @mode = ('add','replace') ]">
        <sch:assert test="child::tei:constraint">This &lt;constraintSpec> element has a @mode of "<sch:value-of select="@mode"/>", but does not have a child 'constraint' element. Use a child 'constraint' element or change the @mode to "delete" or "change".</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="sch_no_more" scheme="schematron" xml:lang="en">
    <desc versionDate="2018-07-06" xml:lang="en">Relationship between scheme attribute and contents: Schematron 1.x</desc>
    <constraint>
      <sch:rule context="tei:constraintSpec">
        <sch:report test="tei:constraint/sch1x:* and @scheme = ('isoschematron','schematron')">Rules
        in the Schematron 1.* language must be inside a &lt;constraintSpec&gt;
        with a value other than "schematron" or "isoschematron" on the
        @scheme attribute.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="isosch" scheme="schematron" xml:lang="en">
    <desc versionDate="2018-07-06" xml:lang="en">Relationship between scheme attribute and contents: ISO Schematron</desc>
    <constraint>
      <sch:rule context="tei:constraintSpec[ @mode = ('add','replace') or not( @mode ) ]">
        <sch:report test="tei:constraint/sch:* and not( @scheme eq 'schematron')">Rules
          in the ISO Schematron language must be inside a &lt;constraintSpec&gt;
          with the value "schematron" on the @scheme attribute.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="context-required" scheme="schematron" xml:lang="en">
    <!-- Note: This constraint also fires on some cases of <constraintDecl>. -->
    <!-- It would be somewhat easier and clearer to use
         "tei:constraintSpec[ @scheme eq 'schematron']//( sch:assert | sch:report )"
         as the context, and then test for "ancestor::sch:rule/@context".
         But if we did that, then a user who had multiple
         <sch:assert>s and <sch:report>s in a single contextless
         constraint would get multiple messages. This way she only
         gets one message. -->
    <constraint>
      <sch:rule context="(tei:constraintSpec|tei:constraintDecl)[ @scheme eq 'schematron'][ .//sch:assert | .//sch:report ]">
        <sch:let name="assertsHaveContext" value="for $a in .//sch:assert return exists( $a/ancestor::sch:rule/@context )"/>
        <sch:let name="reportsHaveContext" value="for $r in .//sch:report return exists( $r/ancestor::sch:rule/@context )"/>
        <sch:report test="( $assertsHaveContext, $reportsHaveContext ) = false()">An &lt;sch:assert> or &lt;sch:report>
          element must be a descendant of an &lt;sch:rule> that has a @context; one or more inside this
          &lt;<sch:value-of select="local-name(.)"/>> are not.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="unique-constraintSpec-ident" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:constraintSpec[ @mode eq 'add' or not( @mode ) ]">
        <sch:let name="myIdent" value="normalize-space(@ident)"/>
        <sch:report test="preceding::tei:constraintSpec[ normalize-space(@ident) eq $myIdent ]">
        The @ident of &lt;constraintSpec> should be unique; this one (<sch:value-of select="$myIdent"/>) is the same as that of a previous &lt;constraintSpec>.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="scheme" usage="opt">
      <!-- Note:
           Per "usage_based_on_mode", below,
           * usage=req iff mode=add or mode=replace (or @mode not specified)
           * usage=opt iff mode=change or mode=delete
           Not sure, maybe @scheme should not be allowed when mode=change
           or mode=delete. Hmmm ...
      -->
      <desc versionDate="2009-06-10" xml:lang="en">supplies the name of the language in which the constraints are defined</desc>
      <desc versionDate="2024-02-28" xml:lang="ja">制約を定義する言語名を示す。</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <constraintSpec scheme="schematron" ident="usage_based_on_mode" xml:lang="en">
        <constraint>
          <sch:rule context="tei:constraintSpec[ @mode = ('add','replace')  or  not( @mode ) ]">
            <sch:assert test="@scheme">
            The @scheme attribute of &lt;constraintSpec&gt; is required when the @mode is
            <sch:value-of select="if (@mode) then concat('&#34;',@mode,'&#34;') else 'not specified'"/>
            (here on "<sch:value-of select="@ident"/>").</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <valList type="semi">
        <valItem ident="schematron">
          <gloss versionDate="2016-09-27" xml:lang="en">ISO Schematron</gloss>
          <gloss versionDate="2024-02-28" xml:lang="ja">ISO スキマトロン</gloss>
        </valItem>
      </valList>
      <remarks ident="constraintSpec-attr.scheme-remarks" versionDate="2023-08-06" xml:lang="en">
        <p>These Guidelines no longer recommend, and the current TEI
        stylesheets no longer support, the use of Schematron 1.x
        within <gi>constraintSpec</gi>. Thus the value
        <val>schematron</val> is used to indicate that ISO Schematron
        is used within the <gi>constraintSpec</gi>.</p>
        <p>The <att>scheme</att> attribute is required when the value
        of <att>mode</att> is <val>add</val> or
        <val>replace</val>. The <att>scheme</att> attribute is
        permitted when the value of <att>mode</att> is
        <val>delete</val>, but these Guidelines make no reccomendation
        for what a processor should do if its value does not match
        that of the <gi>constraintSpec</gi> being deleted.</p>
      </remarks>
      <remarks ident="constraintSpec-attr.scheme-remarks" versionDate="2024-02-28" xml:lang="ja">
        <p><gi>constraintSpec</gi>でのSchematron 1.xの利用は、このガイドラインでは推奨せず最近のTEIスタイルシートでもサポートしない。
        それ故、<val>schematron</val>の値はISO Schematronが<gi>constraintSpec</gi>で用いられることを示すのに使う。</p>
      </remarks>
    </attDef>
    <attDef ident="type" mode="replace">
      <desc versionDate="2018-09-17" xml:lang="en">characterizes the
      <gi>constraintSpec</gi> element in some sense; used to indicate
      when a <gi>constraintSpec</gi> warns about a deprecated
      construct.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="deprecationWarning">
          <desc versionDate="2018-09-17" xml:lang="en">Indicates that
          this constraint specification warns that some other
          construct in the schema is deprecated.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <p>This constraint uses Schematron to enforce the presence of the
    <att>spanTo</att> attribute (which comes from an attribute class)
    on the <gi>addSpan</gi> element: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraintSpec-egXML-kl">
      <constraintSpec ident="demo-c1" scheme="schematron">
        <desc>Enforce the presence of the <att>spanTo</att> attribute</desc>
        <constraint>
          <sch:rule context="tei:addSpan">
            <sch:assert test="@spanTo">The @spanTo attribute of &lt;<sch:name/>> is required.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraintSpec-egXML-ho">
      <constraintSpec ident="demo-c2" scheme="schematron">
        <desc>Implement an accessibility rule which says that pictures
        should have textual explanations</desc>
        <constraint>
          <sch:rule context="tei:figure">
            <sch:report test="not( tei:figDesc | tei:head )">You should
            provide information in a figure from which
            we can construct an @alt attribute in HTML.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>This constraint uses SPITBOL (a language which is not
    expressed in XML) to check whether the title and author are identical: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraintSpec-egXML-qp">
      <constraintSpec ident="author_ne_title" scheme="SPITBOL">
        <constraint> 
(output = leq(title,author)  "title and author cannot be the same")
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
  <remarks ident="constraintSpec-remarks" versionDate="2022-04-09" xml:lang="en">
    <p>A child <gi>constraint</gi> is required when the
    <att>mode</att> attribute has the value <val>replace</val> or
    <val>add</val> (or is not specified, as <val>add</val> is the
    default). No child elements are permitted when the <att>mode</att>
    attribute has the value <val>delete</val>. At least one child
    element is required when the <att>mode</att> attribute has the
    value <val>change</val>.</p>
  </remarks>
  <listRef>
    <ptr target="#TDTAG"/>
  </listRef>
</elementSpec>

```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-06-10" xml:lang="en">constraint on schema</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">スキーマの制約</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-06-24" xml:lang="en">contains a formal constraint, typically expressed in a rule-based schema language, to which a construct must conform in order to be considered valid</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">〔データの〕構造が妥当であるために満たしていなければならない形式的な制約。 通常は規則ベースのスキーマ言語で表現される。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.typed"/>
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
      <elementRef key="constraint" minOccurs="0" maxOccurs="1"/>
    </sequence>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="empty-based-on-mode" xml:lang="en">
    <!-- 
         This constraint specification is much like the
         "child-constraint-based-on-mode" for <elementSpec>, which
         does something something similar (in that it is based on
         @mode), but not quite the same.
    -->
    <constraint>
      <sch:rule context="tei:constraintSpec[ @mode eq 'delete']">
        <sch:report test="child::*">This &lt;constraintSpec> element has a @mode of "delete" even though it has child elements. Change the @mode to "add", "change", or "replace", or remove the child elements.</sch:report>
      </sch:rule>
      <sch:rule context="tei:constraintSpec[ @mode eq 'change']">
        <sch:assert test="child::*">This &lt;constraintSpec> element has a @mode of "change", but does not have any child elements. Specify child elements, or change the @mode to "delete".</sch:assert>
      </sch:rule>
      <sch:rule context="tei:constraintSpec[ @mode = ('add','replace') ]">
        <sch:assert test="child::tei:constraint">This &lt;constraintSpec> element has a @mode of "<sch:value-of select="@mode"/>", but does not have a child 'constraint' element. Use a child 'constraint' element or change the @mode to "delete" or "change".</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b7

### Block 8

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="sch_no_more" scheme="schematron" xml:lang="en">
    <desc versionDate="2018-07-06" xml:lang="en">Relationship between scheme attribute and contents: Schematron 1.x</desc>
    <constraint>
      <sch:rule context="tei:constraintSpec">
        <sch:report test="tei:constraint/sch1x:* and @scheme = ('isoschematron','schematron')">Rules
        in the Schematron 1.* language must be inside a &lt;constraintSpec&gt;
        with a value other than "schematron" or "isoschematron" on the
        @scheme attribute.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b8

### Block 9

XML location: `/elementSpec[1]/constraintSpec[3]`.

```xml
<constraintSpec ident="isosch" scheme="schematron" xml:lang="en">
    <desc versionDate="2018-07-06" xml:lang="en">Relationship between scheme attribute and contents: ISO Schematron</desc>
    <constraint>
      <sch:rule context="tei:constraintSpec[ @mode = ('add','replace') or not( @mode ) ]">
        <sch:report test="tei:constraint/sch:* and not( @scheme eq 'schematron')">Rules
          in the ISO Schematron language must be inside a &lt;constraintSpec&gt;
          with the value "schematron" on the @scheme attribute.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b9

### Block 10

XML location: `/elementSpec[1]/constraintSpec[4]`.

```xml
<constraintSpec ident="context-required" scheme="schematron" xml:lang="en">
    <!-- Note: This constraint also fires on some cases of <constraintDecl>. -->
    <!-- It would be somewhat easier and clearer to use
         "tei:constraintSpec[ @scheme eq 'schematron']//( sch:assert | sch:report )"
         as the context, and then test for "ancestor::sch:rule/@context".
         But if we did that, then a user who had multiple
         <sch:assert>s and <sch:report>s in a single contextless
         constraint would get multiple messages. This way she only
         gets one message. -->
    <constraint>
      <sch:rule context="(tei:constraintSpec|tei:constraintDecl)[ @scheme eq 'schematron'][ .//sch:assert | .//sch:report ]">
        <sch:let name="assertsHaveContext" value="for $a in .//sch:assert return exists( $a/ancestor::sch:rule/@context )"/>
        <sch:let name="reportsHaveContext" value="for $r in .//sch:report return exists( $r/ancestor::sch:rule/@context )"/>
        <sch:report test="( $assertsHaveContext, $reportsHaveContext ) = false()">An &lt;sch:assert> or &lt;sch:report>
          element must be a descendant of an &lt;sch:rule> that has a @context; one or more inside this
          &lt;<sch:value-of select="local-name(.)"/>> are not.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b10

### Block 11

XML location: `/elementSpec[1]/constraintSpec[5]`.

```xml
<constraintSpec ident="unique-constraintSpec-ident" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:constraintSpec[ @mode eq 'add' or not( @mode ) ]">
        <sch:let name="myIdent" value="normalize-space(@ident)"/>
        <sch:report test="preceding::tei:constraintSpec[ normalize-space(@ident) eq $myIdent ]">
        The @ident of &lt;constraintSpec> should be unique; this one (<sch:value-of select="$myIdent"/>) is the same as that of a previous &lt;constraintSpec>.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2009-06-10" xml:lang="en">supplies the name of the language in which the constraints are defined</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">制約を定義する言語名を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="usage_based_on_mode" xml:lang="en">
        <constraint>
          <sch:rule context="tei:constraintSpec[ @mode = ('add','replace')  or  not( @mode ) ]">
            <sch:assert test="@scheme">
            The @scheme attribute of &lt;constraintSpec&gt; is required when the @mode is
            <sch:value-of select="if (@mode) then concat('&#34;',@mode,'&#34;') else 'not specified'"/>
            (here on "<sch:value-of select="@ident"/>").</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="schematron">
          <gloss versionDate="2016-09-27" xml:lang="en">ISO Schematron</gloss>
          <gloss versionDate="2024-02-28" xml:lang="ja">ISO スキマトロン</gloss>
        </valItem>
      </valList>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="constraintSpec-attr.scheme-remarks" versionDate="2023-08-06" xml:lang="en">
        <p>These Guidelines no longer recommend, and the current TEI
        stylesheets no longer support, the use of Schematron 1.x
        within <gi>constraintSpec</gi>. Thus the value
        <val>schematron</val> is used to indicate that ISO Schematron
        is used within the <gi>constraintSpec</gi>.</p>
        <p>The <att>scheme</att> attribute is required when the value
        of <att>mode</att> is <val>add</val> or
        <val>replace</val>. The <att>scheme</att> attribute is
        permitted when the value of <att>mode</att> is
        <val>delete</val>, but these Guidelines make no reccomendation
        for what a processor should do if its value does not match
        that of the <gi>constraintSpec</gi> being deleted.</p>
      </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="constraintSpec-attr.scheme-remarks" versionDate="2024-02-28" xml:lang="ja">
        <p><gi>constraintSpec</gi>でのSchematron 1.xの利用は、このガイドラインでは推奨せず最近のTEIスタイルシートでもサポートしない。
        それ故、<val>schematron</val>の値はISO Schematronが<gi>constraintSpec</gi>で用いられることを示すのに使う。</p>
      </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2018-09-17" xml:lang="en">characterizes the
      <gi>constraintSpec</gi> element in some sense; used to indicate
      when a <gi>constraintSpec</gi> warns about a deprecated
      construct.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="deprecationWarning">
          <desc versionDate="2018-09-17" xml:lang="en">Indicates that
          this constraint specification warns that some other
          construct in the schema is deprecated.</desc>
        </valItem>
      </valList>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>This constraint uses Schematron to enforce the presence of the
    <att>spanTo</att> attribute (which comes from an attribute class)
    on the <gi>addSpan</gi> element: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraintSpec-egXML-kl">
      <constraintSpec ident="demo-c1" scheme="schematron">
        <desc>Enforce the presence of the <att>spanTo</att> attribute</desc>
        <constraint>
          <sch:rule context="tei:addSpan">
            <sch:assert test="@spanTo">The @spanTo attribute of &lt;<sch:name/>> is required.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraintSpec-egXML-ho">
      <constraintSpec ident="demo-c2" scheme="schematron">
        <desc>Implement an accessibility rule which says that pictures
        should have textual explanations</desc>
        <constraint>
          <sch:rule context="tei:figure">
            <sch:report test="not( tei:figDesc | tei:head )">You should
            provide information in a figure from which
            we can construct an @alt attribute in HTML.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <p>This constraint uses SPITBOL (a language which is not
    expressed in XML) to check whether the title and author are identical: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraintSpec-egXML-qp">
      <constraintSpec ident="author_ne_title" scheme="SPITBOL">
        <constraint> 
(output = leq(title,author)  "title and author cannot be the same")
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="constraintSpec-remarks" versionDate="2022-04-09" xml:lang="en">
    <p>A child <gi>constraint</gi> is required when the
    <att>mode</att> attribute has the value <val>replace</val> or
    <val>add</val> (or is not specified, as <val>add</val> is the
    default). No child elements are permitted when the <att>mode</att>
    attribute has the value <val>delete</val>. At least one child
    element is required when the <att>mode</att> attribute has the
    value <val>change</val>.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
  </listRef>
```

^b26

