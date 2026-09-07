---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.deprecated-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.deprecated
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.deprecated.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.deprecated

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5803. Git blob: `2a2946c916cad339e7620b449dee318d884a9a68`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" type="atts" ident="att.deprecated" predeclare="true">
  <desc versionDate="2013-05-16" xml:lang="en">provides attributes indicating how a deprecated feature will be treated in future releases.</desc>
  <desc versionDate="2019-04-08" xml:lang="ja">非推奨の機能を将来のリリースでどのように扱うかを示す属性を提供する。</desc>
  <attList>
    <attDef ident="validUntil" usage="opt">
      <desc versionDate="2013-05-16" xml:lang="en">provides a date before which the construct being defined will not be removed.</desc>
      <desc versionDate="2019-04-08" xml:lang="ja">定義されている構文が削除される前の日付を提供する。</desc>
      <datatype minOccurs="1" maxOccurs="1">
        <!--
            WARNING: In the 'valid' target of the build process the
            validity of @validUntil is tested against xsd:date not by
            using the schema generated from this definition, but
            rather by an ad-hoc test in an XSLT program, namely
            P5/Utilities/extractegXML.xsl. Thus if we ever change the
            datatype here, we may well need to change it there as
            well. —Syd, 2022-02-02
        -->
        <dataRef name="date"/>
      </datatype>
      <constraintSpec scheme="schematron" ident="deprecation-two-month-warning" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@validUntil]">
            <sch:let name="advance_warning_period" value="current-date() + xs:dayTimeDuration('P60D')"/>
            <sch:let name="me_phrase" value="if (@ident) then concat('The ', @ident ) else concat('This ', local-name(.), ' of ', ancestor::tei:*[@ident][1]/@ident )"/>
            <sch:assert test="@validUntil cast as xs:date ge current-date()">
              <sch:value-of select="concat( $me_phrase, ' construct is outdated (as of ', @validUntil, '); ODD processors may ignore it, and its use is no longer supported.' )"/>
            </sch:assert>
            <sch:assert role="warning" test="@validUntil cast as xs:date ge $advance_warning_period">
              <sch:value-of select="concat( $me_phrase, ' construct becomes outdated on ', @validUntil, '.')"/>
            </sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <constraintSpec scheme="schematron" ident="deprecation-should-be-explained" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@validUntil][ not( self::tei:valDesc | self::tei:valList | self::tei:defaultVal | self::tei:remarks )]">
            <sch:assert test="child::tei:desc[ @type eq 'deprecationInfo']">
              A deprecated construct should include, whenever possible, an explanation, but this <sch:value-of select="name(.)"/> does not have a child &lt;desc type="deprecationInfo"&gt;.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <remarks ident="att.deprecated-attr.validUntil-remarks" versionDate="2013-05-16" xml:lang="en">
        <p>The value of this attribute should represent a date (in
        standard <code>yyyy-mm-dd</code> format) which is later than
        the date on which the attribute is added to an ODD.
        Technically, this attribute asserts only the intent to leave a
        construct in future releases of the markup language being
        defined up to at least the specified date, and makes no
        assertion about what happens past that date. In practice, the
        expectation is that the construct will be removed from future
        releases of the markup language being defined sometime shortly
        after the <att>validUntil</att> date.</p>
        <p>An ODD processor will typically not process a specification
        element which has a <att>validUntil</att> date that is in the
        past. An ODD processor will typically warn users about
        constructs which have a <att>validUntil</att> date that is in
        the future. E.g., the documentation for such a construct might
        include the phrase <mentioned>warning: deprecated</mentioned>
        in red.</p>
      </remarks>      
      <remarks ident="att.deprecated-attr.validUntil-remarks" versionDate="2019-04-08" xml:lang="ja">
        <p>この属性の値は、（<code>yyyy-mm-dd</code>の形式で）日付を表し、属性がODDに追加された日付より後である必要がある。技術的には、この属性は、指定された日付まで定義されているマークアップ言語の将来のリリースで構造を残す意図のみを表明し、その日付以降に何が起こるかについて主張しない。実際には、<att>validUntil</att>日付の直後に定義されるマークアップ言語の将来のリリースからコンストラクトが削除されることが期待されます。</p>
        <p>ODDプロセッサは、通常、<att>validUntil</att>日付が過去のものである仕様要素を処理しない。ODDプロセッサは、通常、<att>validUntil</att>の日付を持つコンストラクトについてユーザに警告する。例えば、そのような構造のドキュメントには、<mentioned>warning：deprecated</mentioned>というフレーズが赤で表示される。</p>
      </remarks>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-05-16" xml:lang="en">provides attributes indicating how a deprecated feature will be treated in future releases.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-04-08" xml:lang="ja">非推奨の機能を将来のリリースでどのように扱うかを示す属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-05-16" xml:lang="en">provides a date before which the construct being defined will not be removed.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2019-04-08" xml:lang="ja">定義されている構文が削除される前の日付を提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="1">
        <!--
            WARNING: In the 'valid' target of the build process the
            validity of @validUntil is tested against xsd:date not by
            using the schema generated from this definition, but
            rather by an ad-hoc test in an XSLT program, namely
            P5/Utilities/extractegXML.xsl. Thus if we ever change the
            datatype here, we may well need to change it there as
            well. —Syd, 2022-02-02
        -->
        <dataRef name="date"/>
      </datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="deprecation-two-month-warning" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@validUntil]">
            <sch:let name="advance_warning_period" value="current-date() + xs:dayTimeDuration('P60D')"/>
            <sch:let name="me_phrase" value="if (@ident) then concat('The ', @ident ) else concat('This ', local-name(.), ' of ', ancestor::tei:*[@ident][1]/@ident )"/>
            <sch:assert test="@validUntil cast as xs:date ge current-date()">
              <sch:value-of select="concat( $me_phrase, ' construct is outdated (as of ', @validUntil, '); ODD processors may ignore it, and its use is no longer supported.' )"/>
            </sch:assert>
            <sch:assert role="warning" test="@validUntil cast as xs:date ge $advance_warning_period">
              <sch:value-of select="concat( $me_phrase, ' construct becomes outdated on ', @validUntil, '.')"/>
            </sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/constraintSpec[2]`.

```xml
<constraintSpec scheme="schematron" ident="deprecation-should-be-explained" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@validUntil][ not( self::tei:valDesc | self::tei:valList | self::tei:defaultVal | self::tei:remarks )]">
            <sch:assert test="child::tei:desc[ @type eq 'deprecationInfo']">
              A deprecated construct should include, whenever possible, an explanation, but this <sch:value-of select="name(.)"/> does not have a child &lt;desc type="deprecationInfo"&gt;.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.deprecated-attr.validUntil-remarks" versionDate="2013-05-16" xml:lang="en">
        <p>The value of this attribute should represent a date (in
        standard <code>yyyy-mm-dd</code> format) which is later than
        the date on which the attribute is added to an ODD.
        Technically, this attribute asserts only the intent to leave a
        construct in future releases of the markup language being
        defined up to at least the specified date, and makes no
        assertion about what happens past that date. In practice, the
        expectation is that the construct will be removed from future
        releases of the markup language being defined sometime shortly
        after the <att>validUntil</att> date.</p>
        <p>An ODD processor will typically not process a specification
        element which has a <att>validUntil</att> date that is in the
        past. An ODD processor will typically warn users about
        constructs which have a <att>validUntil</att> date that is in
        the future. E.g., the documentation for such a construct might
        include the phrase <mentioned>warning: deprecated</mentioned>
        in red.</p>
      </remarks>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.deprecated-attr.validUntil-remarks" versionDate="2019-04-08" xml:lang="ja">
        <p>この属性の値は、（<code>yyyy-mm-dd</code>の形式で）日付を表し、属性がODDに追加された日付より後である必要がある。技術的には、この属性は、指定された日付まで定義されているマークアップ言語の将来のリリースで構造を残す意図のみを表明し、その日付以降に何が起こるかについて主張しない。実際には、<att>validUntil</att>日付の直後に定義されるマークアップ言語の将来のリリースからコンストラクトが削除されることが期待されます。</p>
        <p>ODDプロセッサは、通常、<att>validUntil</att>日付が過去のものである仕様要素を処理しない。ODDプロセッサは、通常、<att>validUntil</att>の日付を持つコンストラクトについてユーザに警告する。例えば、そのような構造のドキュメントには、<mentioned>warning：deprecated</mentioned>というフレーズが赤で表示される。</p>
      </remarks>
```

^b9

