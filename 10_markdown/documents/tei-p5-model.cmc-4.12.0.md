---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.cmc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.cmc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.cmc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.cmc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1054. Git blob: `9665a19d2fc734f3e17fbabb02b1cbee3b6f3911`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
Copyright TEI Consortium.
Dual-licensed under CC-by and BSD2 licences
See the file COPYING.txt for details.
-->
<?xml-model href="http://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" ident="model.cmc" type="model" module="tei">
    <desc versionDate="2021-09-07" xml:lang="en">includes the CMC-specific element <gi>post</gi> and
        makes it available on the divPart level. This allows for
        using (and combining) occurrences of <gi>post</gi>,
        <gi>u</gi>, <gi>incident</gi>, and <gi>kinesic</gi> in one
        and the same <gi>div</gi> in order to be able to represent
        the combined use of written and spoken posts, utterances,
        and nonverbal acts on the GUI of multimodal CMC
        environments.</desc>
    <classes>
        
        <memberOf key="model.common"/>
    </classes>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-09-07" xml:lang="en">includes the CMC-specific element <gi>post</gi> and
        makes it available on the divPart level. This allows for
        using (and combining) occurrences of <gi>post</gi>,
        <gi>u</gi>, <gi>incident</gi>, and <gi>kinesic</gi> in one
        and the same <gi>div</gi> in order to be able to represent
        the combined use of written and spoken posts, utterances,
        and nonverbal acts on the GUI of multimodal CMC
        environments.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
        
        <memberOf key="model.common"/>
    </classes>
```

^b2

