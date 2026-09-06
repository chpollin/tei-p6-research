---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.global.source-4.12.0.xml]]'
converter: tools.ingest_git_blobs v2; complete XML plus XML itertext English reading
  blocks with whitespace normalized and identified locators
channel: collection
metadata:
  title: TEI P5 4.12.0 att.global.source specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.global.source.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# att.global.source

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.
A locator names an element that carries an `ident` attribute by that ident, so the
reading block of an attribute definition states which attribute it describes.

Source byte length: 6791. Git blob: `99eff95e2ef18a407b64fb7f59932bc23334e664`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" predeclare="true" xml:id="GBLSRC" module="tei" type="atts" ident="att.global.source">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes used by elements to point to an external source.</desc>
  <desc versionDate="2019-09-18" xml:lang="ja">外部ソースを参照する要素によって用いられる属性を示す。</desc>
  <desc versionDate="2025-02-06" xml:lang="de">stellt Attribute bereit, anhand derer die Elemente auf eine externe Quelle verweisen.</desc>
  <attList>
    <attDef ident="source" usage="opt">
      <desc versionDate="2010-05-09" xml:lang="en">specifies the source from which some aspect of this element is drawn.</desc>
      <desc versionDate="2019-09-18" xml:lang="ja">この要素の何らかの側面を示すソースを指定する。</desc>
      <desc versionDate="2025-02-06" xml:lang="de">gibt die Quelle an, aus der ein Bestandteil dieses Elements stammt.</desc>
      <datatype maxOccurs="unbounded">
        <dataRef key="teidata.pointer"/>
      </datatype>
      <constraintSpec scheme="schematron" ident="only_1_ODD_source" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@source]">
            <sch:let name="srcs" value="tokenize( normalize-space(@source),' ')"/>
            <sch:report test="(   self::tei:classRef                                 | self::tei:dataRef                                 | self::tei:elementRef                                 | self::tei:macroRef                                 | self::tei:moduleRef                                 | self::tei:schemaSpec )                                   and                                   $srcs[2]">
              When used on a schema description element (like
              &lt;<sch:value-of select="name(.)"/>&gt;), the @source attribute
              should have only 1 value. (This one has <sch:value-of select="count($srcs)"/>.)
            </sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <remarks ident="att.global.source-attr.source-remarks" versionDate="2017-06-06" xml:lang="en">
        <p>The <att>source</att> attribute points to an external
        source. When used on an element describing a schema component
        (<gi>classRef</gi>, <gi>dataRef</gi>, <gi>elementRef</gi>,
        <gi>macroRef</gi>, <gi>moduleRef</gi>, or
        <!-- these elements were the members of tei:3.0.0_att.readFrom -->
        <gi>schemaSpec</gi>), it identifies the source from which
        declarations for the components should be obtained.</p>
        <p>On other elements it provides a pointer to the
        bibliographical source from which a quotation or citation is
        drawn.</p>
        <p>In either case, the location may be provided using any form
        of URI, for example an absolute URI, a relative URI, a private
        scheme URI of the form <code>tei:x.y.z</code>, where
        <code>x.y.z</code> indicates the version number, e.g.
        <code>tei:4.3.2</code> for TEI P5 release 4.3.2 or (as a
        special case) <code>tei:current</code> for whatever is the
        latest release, or a private scheme URI that is expanded to an
        absolute URI as documented in a <gi>prefixDef</gi>.</p>
        <p>When used on elements describing schema components,
        <att>source</att> should have only one value; when used on
        other elements multiple values are permitted.</p>
      </remarks>
        <remarks ident="att.global.source-attr.source-remarks" versionDate="2022-05-09" xml:lang="ja">
        <p><att>source</att> 属性は外部ソースを指し示す。<gi>schemaSpec</gi> 
          や <gi>moduleRef</gi> といったスキーマの構成要素を記述する要素で用いられた場合は、
          その定義しようとしているオブジェクトの構成要素の宣言が得られるソースを特定する。
          その他の要素では、引用の出典となる書誌ソースへのポインタを提供する。いずれの場合も、
          場所は何らかの URI、例えば絶対 URI や相対 URI、<gi>prefixDef</gi> 
          に定められた方法で絶対 URI に展開できる私用形式の URI で与えることができる。
          複数の場所が指定された場合、デフォルトでは要求されたソースがそれらのリソースの組み合わせによって得られるものと想定される。</p>
        </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GBLSRC-egXML-tz" source="#SOURCE-eg-01">
      <p><!-- ... --> As Willard McCarty (<bibl xml:id="mcc_2012">2012, p.2</bibl>) tells us, <quote source="#mcc_2012">‘Collaboration’ is a problematic and should be a contested
          term.</quote>
        <!-- ... -->
      </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GBLSRC-egXML-te">
      <p>
        <!-- ... -->
        <quote source="#chicago_15_ed">Grammatical theories are in flux, and the more we learn, the
          less we seem to know.</quote>
        <!-- ... -->
      </p>
      <!-- ... -->
      <bibl xml:id="chicago_15_ed"><title level="m">The Chicago Manual of Style</title>,
          <edition>15th edition</edition>. <pubPlace>Chicago</pubPlace>: <publisher>University of
          Chicago Press</publisher> (<date>2003</date>), <biblScope unit="page">p.147</biblScope>.
      </bibl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GBLSRC-egXML-fx" source="#UND">
      <elementRef key="p" source="tei:2.0.1"/>
    </egXML>
    <p>Include in the schema an element named <gi>p</gi> available from the TEI P5 2.0.1
      release.</p>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GBLSRC-egXML-rt" source="#UND">
      <schemaSpec ident="myODD" source="mycompiledODD.xml">
        <!-- further declarations specifying the components required -->
      </schemaSpec>
    </egXML>
    <p>Create a schema using components taken from the file <ident>mycompiledODD.xml</ident>.</p>
  </exemplum>
  <listRef>
    <ptr target="#STGAso"/>
    <ptr target="#COHQQ"/>
    <ptr target="#TSBAWR"/>
  </listRef>
</classSpec>
```

## English reading blocks

### Reading 1

XML location: `/classSpec[@ident='att.global.source']/desc[1]`.

provides attributes used by elements to point to an external source. ^r1

### Reading 2

XML location: `/classSpec[@ident='att.global.source']/attList[1]/attDef[@ident='source']/desc[1]`.

specifies the source from which some aspect of this element is drawn. ^r2

### Reading 3

XML location: `/classSpec[@ident='att.global.source']/attList[1]/attDef[@ident='source']/remarks[@ident='att.global.source-attr.source-remarks']/p[1]`.

The source attribute points to an external source. When used on an element describing a schema component (classRef, dataRef, elementRef, macroRef, moduleRef, or schemaSpec), it identifies the source from which declarations for the components should be obtained. ^r3

### Reading 4

XML location: `/classSpec[@ident='att.global.source']/attList[1]/attDef[@ident='source']/remarks[@ident='att.global.source-attr.source-remarks']/p[2]`.

On other elements it provides a pointer to the bibliographical source from which a quotation or citation is drawn. ^r4

### Reading 5

XML location: `/classSpec[@ident='att.global.source']/attList[1]/attDef[@ident='source']/remarks[@ident='att.global.source-attr.source-remarks']/p[3]`.

In either case, the location may be provided using any form of URI, for example an absolute URI, a relative URI, a private scheme URI of the form tei:x.y.z, where x.y.z indicates the version number, e.g. tei:4.3.2 for TEI P5 release 4.3.2 or (as a special case) tei:current for whatever is the latest release, or a private scheme URI that is expanded to an absolute URI as documented in a prefixDef. ^r5

### Reading 6

XML location: `/classSpec[@ident='att.global.source']/attList[1]/attDef[@ident='source']/remarks[@ident='att.global.source-attr.source-remarks']/p[4]`.

When used on elements describing schema components, source should have only one value; when used on other elements multiple values are permitted. ^r6

