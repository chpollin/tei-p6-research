---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.temporal.working-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.temporal.working
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.temporal.working.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.temporal.working

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1636. Git blob: `0af191c9f7e6063bd240e1a36ef02aff013a8dba`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.temporal.working">
  <desc versionDate="2020-11-19" xml:lang="en">defines the range of
    values, conforming to the W3C <ref target="#XSD2">XML Schema Part 2:
  Datatypes Second Edition</ref> specification, expressing a date or
  a date and a time within the working life of the document.</desc>
  <content>
    <alternate>
      <dataRef name="date" restriction="(19[789][0-9]|[2-9][0-9]{3}).*"/>
      <dataRef name="dateTime" restriction="(19[789][0-9]|[2-9][0-9]{3}).*"/>
      <!--
	  Note: the idea behind the regular expression used above is
	  to constrain only the first 4 characters of the value, i.e.
	  the year; let the standard named datatype constrain the
	  rest.
      -->
    </alternate>
  </content>
  <remarks ident="teidata.temporal.working-remarks" versionDate="2020-11-19" xml:lang="en">
    <p>If it is likely that the value used is to be compared with
    another, then a time zone indicator should always be included, and
    only the dateTime representation should be used.</p>
    <p>The earliest time expressable with this datatype is 01 January
    1970 (the Unix Epoch), which could be written as either 1970-01-01
    or 1970-01-01T00:00:00Z.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-11-19" xml:lang="en">defines the range of
    values, conforming to the W3C <ref target="#XSD2">XML Schema Part 2:
  Datatypes Second Edition</ref> specification, expressing a date or
  a date and a time within the working life of the document.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <dataRef name="date" restriction="(19[789][0-9]|[2-9][0-9]{3}).*"/>
      <dataRef name="dateTime" restriction="(19[789][0-9]|[2-9][0-9]{3}).*"/>
      <!--
	  Note: the idea behind the regular expression used above is
	  to constrain only the first 4 characters of the value, i.e.
	  the year; let the standard named datatype constrain the
	  rest.
      -->
    </alternate>
  </content>
```

^b2

### Block 3

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.temporal.working-remarks" versionDate="2020-11-19" xml:lang="en">
    <p>If it is likely that the value used is to be compared with
    another, then a time zone indicator should always be included, and
    only the dateTime representation should be used.</p>
    <p>The earliest time expressable with this datatype is 01 January
    1970 (the Unix Epoch), which could be written as either 1970-01-01
    or 1970-01-01T00:00:00Z.</p>
  </remarks>
```

^b3

