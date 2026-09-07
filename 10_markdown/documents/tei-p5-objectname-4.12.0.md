---
type: representation
source-type: document
source: '[[00_sources/tei-p5-objectname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 objectName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/objectName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# objectName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1928. Git blob: `bfb9ef60bcc0b5a10c64737f677971eb5c854c2a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-objectName" ident="objectName">
  <gloss versionDate="2018-07-15" xml:lang="en">name of an object</gloss>
  <gloss versionDate="2019-01-22" xml:lang="de">Name eines Objekts</gloss>
  <desc versionDate="2018-07-15" xml:lang="en">contains a proper noun or noun phrase used to refer to an object.</desc>
  <desc versionDate="2019-01-22" xml:lang="de">enthält einen Eigennamen in Form eines Nomens oder einer Nominalphrase, der verwendet wird, um auf ein Objekt zu verweisen.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.nameLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-objectName-egXML-lw">
      <p> 
        The <objectName ref="#MinsterLovellJewel">Minster Lovell Jewel</objectName> is probably the most similar to the
        <objectName ref="#AlfredJewel">Alfred Jewel</objectName> and was found in <placeName ref="#MinsterLovell">Minster
          Lovell</placeName> in <placeName ref="#Oxfordshire">Oxfordshire</placeName> and is kept at the <orgName ref="#AshmoleanMuseum">Ashmolean Museum</orgName>. 
      </p>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDOBJN"/>
  </listRef>  
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2018-07-15" xml:lang="en">name of an object</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2019-01-22" xml:lang="de">Name eines Objekts</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-07-15" xml:lang="en">contains a proper noun or noun phrase used to refer to an object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-01-22" xml:lang="de">enthält einen Eigennamen in Form eines Nomens oder einer Nominalphrase, der verwendet wird, um auf ein Objekt zu verweisen.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.nameLike"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-objectName-egXML-lw">
      <p> 
        The <objectName ref="#MinsterLovellJewel">Minster Lovell Jewel</objectName> is probably the most similar to the
        <objectName ref="#AlfredJewel">Alfred Jewel</objectName> and was found in <placeName ref="#MinsterLovell">Minster
          Lovell</placeName> in <placeName ref="#Oxfordshire">Oxfordshire</placeName> and is kept at the <orgName ref="#AshmoleanMuseum">Ashmolean Museum</orgName>. 
      </p>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDOBJN"/>
  </listRef>
```

^b8

