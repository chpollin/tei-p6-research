---
type: representation
source-type: document
source: '[[00_sources/tei-p5-paramlist-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 paramList
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/paramList.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# paramList

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1812. Git blob: `664ee16996bc51bdd16cf1e8feac10d0e478b7a7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="paramList" xml:id="gi-paramList" module="tagdocs">  
  <desc versionDate="2015-05-15" xml:lang="en">list of parameter specifications.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <elementRef minOccurs="0" maxOccurs="unbounded" key="paramSpec"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-paramList-egXML-ow">
	 <valItem ident="alternate">
	   <desc versionDate="2015-08-21" xml:lang="en">create a specialized display of alternating elements for displaying the preferred version and an alternative, both at once or by some method of toggling between the two.</desc>
	   
                    <paramList>
                      <paramSpec ident="default">
                        <desc>preferred content</desc>
                      </paramSpec>
                      <paramSpec ident="alternate">
                        <desc>alternate content</desc>
                      </paramSpec>
                    </paramList>
         	</valItem>
    </egXML>
  </exemplum>
  
  <remarks ident="paramList-remarks" versionDate="2015-08-21" xml:lang="en">
    <p>The <gi>paramList</gi> element provides a a mechanism to document parameter specifications using child <gi>paramSpec</gi> elements.</p>
  </remarks>
  <listRef>
      <ptr target="#TDPMMB"/>
      <ptr target="#TDPMDEF"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2015-05-15" xml:lang="en">list of parameter specifications.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <elementRef minOccurs="0" maxOccurs="unbounded" key="paramSpec"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-paramList-egXML-ow">
	 <valItem ident="alternate">
	   <desc versionDate="2015-08-21" xml:lang="en">create a specialized display of alternating elements for displaying the preferred version and an alternative, both at once or by some method of toggling between the two.</desc>
	   
                    <paramList>
                      <paramSpec ident="default">
                        <desc>preferred content</desc>
                      </paramSpec>
                      <paramSpec ident="alternate">
                        <desc>alternate content</desc>
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
<remarks ident="paramList-remarks" versionDate="2015-08-21" xml:lang="en">
    <p>The <gi>paramList</gi> element provides a a mechanism to document parameter specifications using child <gi>paramSpec</gi> elements.</p>
  </remarks>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
      <ptr target="#TDPMMB"/>
      <ptr target="#TDPMDEF"/>
  </listRef>
```

^b6

