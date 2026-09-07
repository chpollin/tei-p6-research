---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.prefix-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.prefix
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.prefix.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.prefix

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1222. Git blob: `47e609af6e94611be005c8839efa2cdd7076fae7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl"
            type="application/xml"
	    schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.prefix">
  <desc versionDate="2016-11-28" xml:lang="en">defines a range of values that may function as a URI scheme name.</desc>
  <content>
    <dataRef name="token" restriction="[a-z][a-z0-9\+\.\-]*"/>
  </content>
  <remarks ident="teidata.prefix-remarks" versionDate="2016-11-28" xml:lang="en">
    <p>This datatype is used to constrain a string of characters to
    one that can be used as a URI scheme name according to <ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986</ref>, <ref target="https://tools.ietf.org/html/rfc3986#section-3.1">section
    3.1</ref>. Thus only the 26 lowercase letters a–z, the 10
    digits 0–9, the plus sign, the period, and the hyphen are
    permitted, and the value must start with a letter.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-11-28" xml:lang="en">defines a range of values that may function as a URI scheme name.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <dataRef name="token" restriction="[a-z][a-z0-9\+\.\-]*"/>
  </content>
```

^b2

### Block 3

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.prefix-remarks" versionDate="2016-11-28" xml:lang="en">
    <p>This datatype is used to constrain a string of characters to
    one that can be used as a URI scheme name according to <ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986</ref>, <ref target="https://tools.ietf.org/html/rfc3986#section-3.1">section
    3.1</ref>. Thus only the 26 lowercase letters a–z, the 10
    digits 0–9, the plus sign, the period, and the hyphen are
    permitted, and the value must start with a letter.</p>
  </remarks>
```

^b3

