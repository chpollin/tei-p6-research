---
type: representation
source-type: document
source: '[[00_sources/tei-p5-paramspec-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 paramSpec
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/paramSpec.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# paramSpec

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2189. Git blob: `ae0d0b9723869957211a96ba825103c4944ae5e9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="paramSpec" xml:id="gi-paramSpec" module="tagdocs">
  <desc versionDate="2015-05-15" xml:lang="en">supplies specification for one parameter of a model
    behaviour.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.identEquiv"/>
      <classRef key="model.descLike"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-paramSpec-egXML-xg">
      <valItem ident="link">
        <desc>create a hyperlink</desc>
        <paramList>
          <paramSpec ident="content">
            <desc>supplies the location of some content describing the link</desc>
          </paramSpec>
          <paramSpec ident="link">
            <desc>supplies the location of the intended URL</desc>
          </paramSpec>
        </paramList>
      </valItem>
    </egXML>
  </exemplum>
  <remarks ident="paramSpec-remarks" versionDate="2016-02-29" xml:lang="en">
    <p>Where a model behaviour uses more than one parameter, individual <gi>paramSpec</gi> elements
      should be grouped together using a <gi>paramList</gi> element, as above. Parameter
      specifications are provided within the <gi>valItem</gi> used to define a particular behaviour,
      which forms part of the specification of a <gi>model</gi> element's <att>behaviour</att>
      attribute. In the example above, the behaviour <ident>link</ident> has two parameters:
        <val>content</val> and <val>link</val>.</p>
    <p>Using a <gi>desc</gi> element within a <gi>paramSpec</gi> is optional but recommended
      practice.</p>
  </remarks>
  <listRef>
    <ptr target="#TDPMDEF"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2015-05-15" xml:lang="en">supplies specification for one parameter of a model
    behaviour.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.identEquiv"/>
      <classRef key="model.descLike"/>
    </alternate>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-paramSpec-egXML-xg">
      <valItem ident="link">
        <desc>create a hyperlink</desc>
        <paramList>
          <paramSpec ident="content">
            <desc>supplies the location of some content describing the link</desc>
          </paramSpec>
          <paramSpec ident="link">
            <desc>supplies the location of the intended URL</desc>
          </paramSpec>
        </paramList>
      </valItem>
    </egXML>
  </exemplum>
```

^b4

### Block 5

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="paramSpec-remarks" versionDate="2016-02-29" xml:lang="en">
    <p>Where a model behaviour uses more than one parameter, individual <gi>paramSpec</gi> elements
      should be grouped together using a <gi>paramList</gi> element, as above. Parameter
      specifications are provided within the <gi>valItem</gi> used to define a particular behaviour,
      which forms part of the specification of a <gi>model</gi> element's <att>behaviour</att>
      attribute. In the example above, the behaviour <ident>link</ident> has two parameters:
        <val>content</val> and <val>link</val>.</p>
    <p>Using a <gi>desc</gi> element within a <gi>paramSpec</gi> is optional but recommended
      practice.</p>
  </remarks>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDPMDEF"/>
  </listRef>
```

^b6

