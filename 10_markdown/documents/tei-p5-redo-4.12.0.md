---
type: representation
source-type: document
source: '[[00_sources/tei-p5-redo-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 redo
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/redo.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# redo

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2225. Git blob: `cdd6db916b50c61ce086e5ba649173f8ed215266`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="redo" xml:id="gi-redo" module="transcr">
  <desc versionDate="2013-04-16" xml:lang="en">indicates one or more cancelled interventions in a
		  document which have subsequently been
		  marked as reaffirmed or repeated.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="target">
      <desc versionDate="2013-04-16" xml:lang="en">points to one or more elements representing the
	 interventions which are being reasserted.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-redo-egXML-cs">
      <line><redo hand="#g_t" target="#redo-1" cause="fix"/><mod xml:id="redo-1" rend="strikethrough" spanTo="#anchor-1" hand="#g_bl"/>Ihr hagren, triſten, krummgezog<mod rend="strikethrough">nen</mod>ener Nacken</line>
      <line>Wenn ihr nur piepſet iſt die Welt ſchon matt.<anchor xml:id="anchor-1"/>
         </line>
    </egXML>
    <p>This encoding represents the following sequence of events:
<list><item>"Ihr hagren, triſten, krummgezog nenener Nacken/ Wenn ihr
nur piepſet iſt die Welt ſchon matt." is written </item><item>the redundant letters "nen" in "nenener" are deleted</item><item>the whole passage is deleted by hand <code>g_bl</code> using strikethrough</item><item>the deletion is reasserted by another hand (identified here as <code>g_t</code>)</item></list>
      </p>
  </exemplum>
  <listRef>
    <ptr target="#undo"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en">indicates one or more cancelled interventions in a
		  document which have subsequently been
		  marked as reaffirmed or repeated.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en">points to one or more elements representing the
	 interventions which are being reasserted.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-redo-egXML-cs">
      <line><redo hand="#g_t" target="#redo-1" cause="fix"/><mod xml:id="redo-1" rend="strikethrough" spanTo="#anchor-1" hand="#g_bl"/>Ihr hagren, triſten, krummgezog<mod rend="strikethrough">nen</mod>ener Nacken</line>
      <line>Wenn ihr nur piepſet iſt die Welt ſchon matt.<anchor xml:id="anchor-1"/>
         </line>
    </egXML>
    <p>This encoding represents the following sequence of events:
<list><item>"Ihr hagren, triſten, krummgezog nenener Nacken/ Wenn ihr
nur piepſet iſt die Welt ſchon matt." is written </item><item>the redundant letters "nen" in "nenener" are deleted</item><item>the whole passage is deleted by hand <code>g_bl</code> using strikethrough</item><item>the deletion is reasserted by another hand (identified here as <code>g_t</code>)</item></list>
      </p>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#undo"/>
  </listRef>
```

^b7

