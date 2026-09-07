---
type: representation
source-type: document
source: '[[00_sources/tei-p5-macro.specialpara.cmc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 macro.specialPara.cmc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/macro.specialPara.cmc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# macro.specialPara.cmc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1432. Git blob: `25436043f22f71e9f06df632b385f6c08f62d5da`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
Copyright TEI Consortium.
Dual-licensed under CC-by and BSD2 licences
See the file COPYING.txt for details.
-->
<?xml-model href="http://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<macroSpec xmlns="http://www.tei-c.org/ns/1.0" ident="macro.specialPara.cmc" mode="add" module="cmc">
    <gloss versionDate="2021-03-04" xml:lang="en">'special'
        paragraph content with added CMC element(s)</gloss>
    <desc versionDate="2021-03-04" xml:lang="en">defines the
        content model of the <gi>quote</gi> element, whose content
        is just like others (such as notes or list items) which
        either contain a series of component-level elements or else
        have the same structure as a paragraph, containing a series
        of phrase-level and inter-level elements, but also contains
        element(s) for transcription of CMC.</desc>
    <content>
        <alternate minOccurs="0" maxOccurs="unbounded">
            <textNode/>
            <classRef key="model.gLike"/>
            <classRef key="model.phrase"/>
            <classRef key="model.inter"/>
            <classRef key="model.divPart"/>
            <classRef key="model.global"/>
            <classRef key="model.cmc"/>
        </alternate>    
    </content>
</macroSpec>
```

## Source blocks

### Block 1

XML location: `/macroSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2021-03-04" xml:lang="en">'special'
        paragraph content with added CMC element(s)</gloss>
```

^b1

### Block 2

XML location: `/macroSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-03-04" xml:lang="en">defines the
        content model of the <gi>quote</gi> element, whose content
        is just like others (such as notes or list items) which
        either contain a series of component-level elements or else
        have the same structure as a paragraph, containing a series
        of phrase-level and inter-level elements, but also contains
        element(s) for transcription of CMC.</desc>
```

^b2

### Block 3

XML location: `/macroSpec[1]/content[1]`.

```xml
<content>
        <alternate minOccurs="0" maxOccurs="unbounded">
            <textNode/>
            <classRef key="model.gLike"/>
            <classRef key="model.phrase"/>
            <classRef key="model.inter"/>
            <classRef key="model.divPart"/>
            <classRef key="model.global"/>
            <classRef key="model.cmc"/>
        </alternate>    
    </content>
```

^b3

