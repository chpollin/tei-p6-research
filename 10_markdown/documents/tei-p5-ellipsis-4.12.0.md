---
type: representation
source-type: document
source: '[[00_sources/tei-p5-ellipsis-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 ellipsis
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/ellipsis.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# ellipsis

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4132. Git blob: `4644c8937082b5342360ef5af7a9d2158d0fd4e4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-ellipsis" ident="ellipsis">
  <gloss versionDate="2021-07-07" xml:lang="en">deliberately marked omission</gloss>
  <desc versionDate="2021-07-07" xml:lang="en">indicates a purposeful
  marking in the source document signalling that content has been
  omitted, and may also supply or describe the omitted content.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.timed"/>
    <memberOf key="model.global.edit"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="metamark"/>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="1"/>
      <elementRef key="supplied" minOccurs="0" maxOccurs="1"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ellipsis-egXML-qm" source="#COEDADD-eg-91">
      <lg>
        <l>What projects men make—what queer turns they take,</l>
        <l>Since <emph>steam</emph> has improved our condition;</l>
        <l>They never are still, but must cure or must kill</l>
        <l>With steam physic or steam ammunition.</l>
        <l>But a short time ago, to a quack you would go,</l>
        <l>To steam a fat man to a thinner;</l>
        <l>Now changed from all that, if you wish to get <emph>fat</emph>,</l>
        <l>Come to Barton’s and eat a <emph>steam dinner!</emph></l>
        <l>Oh dear! think of a scheme, odd though it seem—</l>
        <l>I’m sure ’twill succeed if you make it by steam.</l>
      </lg>
      <lg>
        <l>You may sleep, you may dream, you may travel by steam,</l>
        <l>For the outcry is still to go faster;</l>
        <l>And what does it reck, should you e’en break your neck,</l>
        <l>If ’tis <emph>steam</emph> that brings on the disaster?</l>
        <ellipsis resp="#ChambersEdnbrghJrnl1880">
        <metamark function="multilineEllipsis"> * * * * </metamark>
        <desc resp="#teiProjectEditor2021">The printer omits four lines here,  
         skipping the second half of the second octave, before the refrain.</desc>
        </ellipsis>
        <l>Oh dear! think of a scheme, odd though it seem—</l>
        <l>I’m sure ’twill succeed if you make it by steam.</l>
      </lg>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ellipsis-egXML-ge" source="#COEDADD-eg-92">
      <lg>
        <l>You think you’ve lost your love </l>
        <l>Well, I saw her yesterday </l>
        <l>It’s you she's thinking of </l>
        <l>And she told me what to say</l>
      </lg>
      <lg xml:id="chorus">
        <label>[Refrain]</label>
        <l>She says she loves you </l>
        <l>And you know that can’t be bad </l>
        <l>Yes, she loves you </l>
        <l>And you know you should be glad</l>
      </lg>
      <lg>
        <l>She said you hurt her so </l>
        <l>She almost lost her mind </l>
        <l>But now she said she knows </l>
        <l>You’re not the hurting kind</l>
      </lg>
      <ellipsis>
        <metamark>******</metamark>
        <supplied copyOf="#chorus"/>
      </ellipsis>
    </egXML>
  </exemplum>
  <remarks ident="ellipsis-remarks" versionDate="2021-07-07" xml:lang="en">
    <p>Unlike <gi>gap</gi>, which indicates content that the encoder
    cannot or chooses not to represent, <gi>ellipsis</gi> indicates a
    passage explicitly signalled in the source document as absent. The
    <gi>ellipsis</gi> element is not appropriate for every use of
    ellipsis points, such as when they indicate that a speaker is
    pausing.</p>
  </remarks>
  <listRef>
    <ptr target="#COEDADD" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2021-07-07" xml:lang="en">deliberately marked omission</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-07-07" xml:lang="en">indicates a purposeful
  marking in the source document signalling that content has been
  omitted, and may also supply or describe the omitted content.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.timed"/>
    <memberOf key="model.global.edit"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="metamark"/>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="1"/>
      <elementRef key="supplied" minOccurs="0" maxOccurs="1"/>
    </sequence>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ellipsis-egXML-qm" source="#COEDADD-eg-91">
      <lg>
        <l>What projects men make—what queer turns they take,</l>
        <l>Since <emph>steam</emph> has improved our condition;</l>
        <l>They never are still, but must cure or must kill</l>
        <l>With steam physic or steam ammunition.</l>
        <l>But a short time ago, to a quack you would go,</l>
        <l>To steam a fat man to a thinner;</l>
        <l>Now changed from all that, if you wish to get <emph>fat</emph>,</l>
        <l>Come to Barton’s and eat a <emph>steam dinner!</emph></l>
        <l>Oh dear! think of a scheme, odd though it seem—</l>
        <l>I’m sure ’twill succeed if you make it by steam.</l>
      </lg>
      <lg>
        <l>You may sleep, you may dream, you may travel by steam,</l>
        <l>For the outcry is still to go faster;</l>
        <l>And what does it reck, should you e’en break your neck,</l>
        <l>If ’tis <emph>steam</emph> that brings on the disaster?</l>
        <ellipsis resp="#ChambersEdnbrghJrnl1880">
        <metamark function="multilineEllipsis"> * * * * </metamark>
        <desc resp="#teiProjectEditor2021">The printer omits four lines here,  
         skipping the second half of the second octave, before the refrain.</desc>
        </ellipsis>
        <l>Oh dear! think of a scheme, odd though it seem—</l>
        <l>I’m sure ’twill succeed if you make it by steam.</l>
      </lg>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ellipsis-egXML-ge" source="#COEDADD-eg-92">
      <lg>
        <l>You think you’ve lost your love </l>
        <l>Well, I saw her yesterday </l>
        <l>It’s you she's thinking of </l>
        <l>And she told me what to say</l>
      </lg>
      <lg xml:id="chorus">
        <label>[Refrain]</label>
        <l>She says she loves you </l>
        <l>And you know that can’t be bad </l>
        <l>Yes, she loves you </l>
        <l>And you know you should be glad</l>
      </lg>
      <lg>
        <l>She said you hurt her so </l>
        <l>She almost lost her mind </l>
        <l>But now she said she knows </l>
        <l>You’re not the hurting kind</l>
      </lg>
      <ellipsis>
        <metamark>******</metamark>
        <supplied copyOf="#chorus"/>
      </ellipsis>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="ellipsis-remarks" versionDate="2021-07-07" xml:lang="en">
    <p>Unlike <gi>gap</gi>, which indicates content that the encoder
    cannot or chooses not to represent, <gi>ellipsis</gi> indicates a
    passage explicitly signalled in the source document as absent. The
    <gi>ellipsis</gi> element is not appropriate for every use of
    ellipsis points, such as when they indicate that a speaker is
    pausing.</p>
  </remarks>
```

^b7

### Block 8

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COEDADD" type="div3"/>
  </listRef>
```

^b8

