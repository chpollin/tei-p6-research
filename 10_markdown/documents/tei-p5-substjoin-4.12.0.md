---
type: representation
source-type: document
source: '[[00_sources/tei-p5-substjoin-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 substJoin
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/substJoin.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# substJoin

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1566. Git blob: `08a28557aef3e45914597dcc6e31586371033d43`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-substJoin" ident="substJoin">
  <gloss versionDate="2011-11-08" xml:lang="en">substitution join</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">jointure de substitution</gloss>
  <desc versionDate="2020-08-16" xml:lang="en">identifies a series of  possibly fragmented additions, deletions, or other revisions on a manuscript that combine to make up a single intervention in the text.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-substJoin-egXML-pt">
      While <del xml:id="r112">pondering</del> thus <add xml:id="r113">she mus'd</add>, her pinions fann'd<substJoin target="#r112 #r113"/>
      </egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHSU"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2011-11-08" xml:lang="en">substitution join</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">jointure de substitution</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-08-16" xml:lang="en">identifies a series of  possibly fragmented additions, deletions, or other revisions on a manuscript that combine to make up a single intervention in the text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b4

### Block 5

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-substJoin-egXML-pt">
      While <del xml:id="r112">pondering</del> thus <add xml:id="r113">she mus'd</add>, her pinions fann'd<substJoin target="#r112 #r113"/>
      </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHSU"/>
  </listRef>
```

^b7

