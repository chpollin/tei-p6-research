---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.namespaceorname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.namespaceOrName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.namespaceOrName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.namespaceOrName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1720. Git blob: `81d8585cbb847439ea5bae61ac06cfb63d8beb18`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.namespaceOrName">
  <desc versionDate="2017-05-23" xml:lang="en">defines attribute values which contain either an absolute namespace URI or a qualified XML name.</desc>
  <content>
    <!--
     What we'd like to say:
    <alternate>
      <!- - no slashes before the required first colon, thus to exclude relative URIs - ->
      <dataRef key="teidata.namespace" restriction="[^/]+:.*"/>
      <!- - require a colon[1] - ->
      <dataRef key="teidata.name" restriction=".+:.+"/>
    </alternate>
     but cannot, because @restriction on <dataRef> is not implemented yet -->
    <alternate>
      <dataRef name="anyURI">
        <!-- no slashes before the required first colon, thus to exclude relative URIs -->
        <dataFacet name="pattern" value="[^/\s]+:\S*"/>
      </dataRef>
      <dataRef name="Name">
        <!-- require a colon[1] -->
        <dataFacet name="pattern" value=".+:.+"/>
      </dataRef>
    </alternate>
  </content>
  <!-- [1] Cannot use <dateRef name="QName"> for two reasons: first,  -->
  <!-- for reasons I don't entirely understand, 'duck' is valid as a  -->
  <!-- QName. (I suspect because it inherits a namespace.) Second, it -->
  <!-- would require that the prefix 'mid' in 'mid:night' be in scope -->
  <!-- wherever this was used. -->
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-05-23" xml:lang="en">defines attribute values which contain either an absolute namespace URI or a qualified XML name.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <!--
     What we'd like to say:
    <alternate>
      <!- - no slashes before the required first colon, thus to exclude relative URIs - ->
      <dataRef key="teidata.namespace" restriction="[^/]+:.*"/>
      <!- - require a colon[1] - ->
      <dataRef key="teidata.name" restriction=".+:.+"/>
    </alternate>
     but cannot, because @restriction on <dataRef> is not implemented yet -->
    <alternate>
      <dataRef name="anyURI">
        <!-- no slashes before the required first colon, thus to exclude relative URIs -->
        <dataFacet name="pattern" value="[^/\s]+:\S*"/>
      </dataRef>
      <dataRef name="Name">
        <!-- require a colon[1] -->
        <dataFacet name="pattern" value=".+:.+"/>
      </dataRef>
    </alternate>
  </content>
```

^b2

