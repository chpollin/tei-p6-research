---
type: representation
source-type: document
source: '[[00_sources/tei-p5-annotation-4.12.0.xml]]'
converter: tools.ingest_text_identity v1; complete XML plus XML itertext English reading
  blocks with whitespace normalized
channel: collection
metadata:
  title: TEI P5 4.12.0 annotation specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/annotation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-05'
updated: '2026-09-05'
---

# annotation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.

Source byte length: 6577. Git blob: `9c98ca8590036df7de925753c7d65fb028c41d1b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="linking" xml:id="gi-annotation" ident="annotation">
  <desc versionDate="2020-07-31" xml:lang="en">represents an annotation following the <ref target="#WADM">Web Annotation Data Model</ref>.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.pointing"/>
    <memberOf key="model.annotationLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="respStmt" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="revisionDesc" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="licence" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.annotationPart.body" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <attList>
    <attDef ident="motivation" usage="opt">
      <datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="closed">
        <valItem ident="assessing">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to assess the target resource in
            some way, rather than simply make a comment about it</desc>
        </valItem>
        <valItem ident="bookmarking">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to create a bookmark to the target
            or part thereof</desc>
        </valItem>
        <valItem ident="classifying">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to classify the target in some
            way</desc>
        </valItem>
        <valItem ident="commenting">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to comment about the target</desc>
        </valItem>
        <valItem ident="describing">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to describe the target, rather than
            (for example) comment on it</desc>
        </valItem>
        <valItem ident="editing">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to request an edit or a change to
            the target resource</desc>
        </valItem>
        <valItem ident="highlighting">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to highlight the target resource or
            a segment thereof</desc>
        </valItem>
        <valItem ident="identifying">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to assign an identity to the
            target</desc>
        </valItem>
        <valItem ident="linking">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to link to a resource related to
            the target</desc>
        </valItem>
        <valItem ident="moderating">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to assign some value or quality to
            the target</desc>
        </valItem>
        <valItem ident="questioning">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to ask a question about the
            target</desc>
        </valItem>
        <valItem ident="replying">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to reply to a previous statement,
            either an annotation or another resource</desc>
        </valItem>
        <valItem ident="tagging">
          <desc versionDate="2020-08-10" xml:lang="en">intent is to associate a tag with the
            target</desc>
        </valItem>
      </valList>
      <remarks ident="annotation-attr.motivation-remarks" versionDate="2020-08-10" xml:lang="en">
        <p>For further detailed explanation of the suggested values, see the <ref target="#WAV">Web
            Annotation Vocabulary</ref> (WAV). The motivations described here map to URIs defined by
          the WAV and when exported to RDF or JSON-LD must have the URI
            <code>http://www.w3.org/ns/oa#</code> prepended.</p>
        <p>As an <ref target="#RDFPrimer">RDF</ref> vocabulary, WADM permits the definition of new
          motivations (see Appendix C of the WAV). In TEI, new motivations may be defined in a
          custom ODD (see section <ref target="#MDMDAL">23.3.1.3</ref>). New motivations must also
          map to URIs defined by an RDF ontology extending the WAV.</p>
      </remarks>
    </attDef>
    <attDef ident="target" mode="change" usage="req"/>
    <attDef ident="xml:id" mode="change" usage="req"/>
  </attList>
  <exemplum versionDate="2020-07-31" xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-annotation-egXML-mw">
      <annotation xml:id="ann1" motivation="linking" target="#Gallia">
        <!-- See https://www.w3.org/TR/annotation-model/#lifecycle-information and 
             https://www.w3.org/TR/annotation-model/#agents -->
        <respStmt xml:id="fred">
          <resp>creator</resp>
          <persName>Fred Editor</persName>
        </respStmt>
        <revisionDesc>
          <change status="created" when="2020-05-21T13:59:00Z" who="#fred"/>
          <change status="modified" when="2020-05-21T19:48:00Z" who="#fred"/>
        </revisionDesc>
        <!-- See https://www.w3.org/TR/annotation-model/#rights-information -->
        <licence target="http://creativecommons.org/licenses/by/3.0/"/>
        <!-- Multiple bodies -->
        <!-- Pointers to sections of text in the same document -->
        <ptr target="#string-range(c1p1s1,0,6)"/>
        <ptr target="#string-range(c1p1s6,19,7)"/>
      </annotation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2020-07-31" xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-annotation-egXML-ep">
      <annotation xml:id="TheCorrectTitle" motivation="commenting" target="#line1">
        <note>The correct title of this specification, and the correct full name of XML, is
          "Extensible Markup Language". "eXtensible Markup Language" is just a spelling error.
          However, the abbreviation "XML" is not only correct but, appearing as it does in the title
          of the specification, an official name of the Extensible Markup Language. </note>
      </annotation>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#SASOstdf"/>
  </listRef>
</elementSpec>
```

## English reading blocks

### Reading 1

XML location: `/elementSpec[1]/desc[1]`.

represents an annotation following the Web Annotation Data Model. ^r1

### Reading 2

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[1]/desc[1]`.

intent is to assess the target resource in some way, rather than simply make a comment about it ^r2

### Reading 3

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[2]/desc[1]`.

intent is to create a bookmark to the target or part thereof ^r3

### Reading 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[3]/desc[1]`.

intent is to classify the target in some way ^r4

### Reading 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[4]/desc[1]`.

intent is to comment about the target ^r5

### Reading 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[5]/desc[1]`.

intent is to describe the target, rather than (for example) comment on it ^r6

### Reading 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[6]/desc[1]`.

intent is to request an edit or a change to the target resource ^r7

### Reading 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[7]/desc[1]`.

intent is to highlight the target resource or a segment thereof ^r8

### Reading 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[8]/desc[1]`.

intent is to assign an identity to the target ^r9

### Reading 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[9]/desc[1]`.

intent is to link to a resource related to the target ^r10

### Reading 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[10]/desc[1]`.

intent is to assign some value or quality to the target ^r11

### Reading 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[11]/desc[1]`.

intent is to ask a question about the target ^r12

### Reading 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[12]/desc[1]`.

intent is to reply to a previous statement, either an annotation or another resource ^r13

### Reading 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]/valItem[13]/desc[1]`.

intent is to associate a tag with the target ^r14

### Reading 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]/p[1]`.

For further detailed explanation of the suggested values, see the Web Annotation Vocabulary (WAV). The motivations described here map to URIs defined by the WAV and when exported to RDF or JSON-LD must have the URI http://www.w3.org/ns/oa# prepended. ^r15

### Reading 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]/p[2]`.

As an RDF vocabulary, WADM permits the definition of new motivations (see Appendix C of the WAV). In TEI, new motivations may be defined in a custom ODD (see section 23.3.1.3). New motivations must also map to URIs defined by an RDF ontology extending the WAV. ^r16

