---
type: representation
source-type: document
source: '[[00_sources/tei-p5-outputrendition-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 outputRendition
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/outputRendition.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# outputRendition

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3343. Git blob: `38032220edb7d85f7ba6cc426fbc385554ce6b7a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="outputRendition" xml:id="gi-outputRendition" module="tagdocs">
  <desc versionDate="2015-08-21" xml:lang="en">
    describes the rendering or
    appearance intended for all occurrences of an element in a specified
    context for a specified type of output.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <attList>
    <attDef ident="scope">
      <desc versionDate="2016-02-05" xml:lang="en">provides a way of defining
          <soCalled>pseudo-elements</soCalled>, that is, styling rules applicable to specific
        sub-portions of an element.</desc>
      <datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
        <valItem ident="first-line">
          <desc versionDate="2016-02-05" xml:lang="en">styling applies to the first line of the
            target element.</desc>
        </valItem>
        <valItem ident="first-letter">
          <desc versionDate="2016-02-05" xml:lang="en">styling applies to the first character of the
            target element.</desc>
        </valItem>
        <valItem ident="before">
          <desc versionDate="2016-02-05" xml:lang="en">styling should be applied immediately before
            the content of the target element.</desc>
        </valItem>
        <valItem ident="after">
          <desc versionDate="2016-02-05" xml:lang="en">styling should be applied immediately after
            the content of the target element.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-outputRendition-egXML-kp">
      <model predicate="ancestor::p" behaviour="inline">
        <outputRendition>font-style: italic;</outputRendition>
      </model>
      <model behaviour="block">
        <outputRendition>left-margin: 2em;</outputRendition>
      </model>
    </egXML>
  </exemplum>
  <remarks ident="outputRendition-remarks" versionDate="2016-02-05" xml:lang="en">
    <p>This component of an element specification describes the rendering or
      appearance intended for all occurrences of the element in a specified
      context for a specified type of output. The <gi>rendition</gi> element, by
        contrast, describes the actual rendering or appearance of all occurrences
        of the specified element in a source document. The
        <att>useSourceRendition</att> attribute may however be used to indicate
        that formatting information provided by a <gi>rendition</gi> element is to
        be combined with any provided by an <gi>outputRendition</gi> element.</p>
    <p>It is strongly recommended that the W3C Cascading Stylesheet language
      (CSS2 or later) be used to express the required formatting information.</p>
   
  </remarks>
   
  <listRef>
    <ptr target="#TDPMOR"/>
  </listRef>
  
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2015-08-21" xml:lang="en">
    describes the rendering or
    appearance intended for all occurrences of an element in a specified
    context for a specified type of output.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.oddDecl"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2016-02-05" xml:lang="en">provides a way of defining
          <soCalled>pseudo-elements</soCalled>, that is, styling rules applicable to specific
        sub-portions of an element.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="first-line">
          <desc versionDate="2016-02-05" xml:lang="en">styling applies to the first line of the
            target element.</desc>
        </valItem>
        <valItem ident="first-letter">
          <desc versionDate="2016-02-05" xml:lang="en">styling applies to the first character of the
            target element.</desc>
        </valItem>
        <valItem ident="before">
          <desc versionDate="2016-02-05" xml:lang="en">styling should be applied immediately before
            the content of the target element.</desc>
        </valItem>
        <valItem ident="after">
          <desc versionDate="2016-02-05" xml:lang="en">styling should be applied immediately after
            the content of the target element.</desc>
        </valItem>
      </valList>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-outputRendition-egXML-kp">
      <model predicate="ancestor::p" behaviour="inline">
        <outputRendition>font-style: italic;</outputRendition>
      </model>
      <model behaviour="block">
        <outputRendition>left-margin: 2em;</outputRendition>
      </model>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="outputRendition-remarks" versionDate="2016-02-05" xml:lang="en">
    <p>This component of an element specification describes the rendering or
      appearance intended for all occurrences of the element in a specified
      context for a specified type of output. The <gi>rendition</gi> element, by
        contrast, describes the actual rendering or appearance of all occurrences
        of the specified element in a source document. The
        <att>useSourceRendition</att> attribute may however be used to indicate
        that formatting information provided by a <gi>rendition</gi> element is to
        be combined with any provided by an <gi>outputRendition</gi> element.</p>
    <p>It is strongly recommended that the W3C Cascading Stylesheet language
      (CSS2 or later) be used to express the required formatting information.</p>
   
  </remarks>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDPMOR"/>
  </listRef>
```

^b9

