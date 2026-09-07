---
type: representation
source-type: document
source: '[[00_sources/tei-p5-metamark-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 metamark
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/metamark.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# metamark

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2790. Git blob: `ef5b77acd2380e8a131c271b2ce8ab57666cfadd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="metamark" xml:id="gi-metamark" module="transcr">
  <desc versionDate="2013-04-16" xml:lang="en">contains or describes any kind of graphic or written signal
   within a document the function of which is to determine how it
   should be read rather than forming part of the actual content of
   the document.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.spanning"/>
    <memberOf key="model.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <attList>
    <attDef ident="function">
      <desc versionDate="2013-04-16" xml:lang="en">describes the function (for example  status, insertion,
	 deletion, transposition) of the metamark.</desc>
      <datatype minOccurs="1"><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="target">
      <desc versionDate="2013-04-16" xml:lang="en">identifies one or more elements to which the metamark applies.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="no">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metamark-egXML-zn">
      <line><seg xml:id="tp-ib01">bör</seg><metamark rend="underline" function="transposition" target="#tp-ib01" place="above">2.</metamark>
   og <seg xml:id="tp-ib02">hör</seg>
            <metamark rend="underline" function="transposition" target="#tp-ib02" place="above">1.</metamark>
         </line>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metamark-egXML-pz">
      <surface>
 <metamark function="used" rend="line" target="#X2"/>
 <zone xml:id="zone-X2">
  <line>I am that halfgrown <add>angry</add> boy, fallen asleep</line>
  <line>The tears of foolish passion yet undried</line>
  <line>upon my cheeks.</line>
<!-- ... -->
  <line>I pass through <add>the</add> travels and <del>fortunes</del> of
  <retrace>thirty</retrace>
  </line>
  <line>years and become old,</line>
  <line>Each in its due order comes and goes,</line>
  <line>And thus a message for me comes.</line>
  <line>The</line>
 </zone>
 <metamark function="used" target="#zone-X2">Entered - Yes</metamark>
</surface>
    </egXML>
  </exemplum>	
  <listRef>
    <ptr target="#PH-meta"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en">contains or describes any kind of graphic or written signal
   within a document the function of which is to determine how it
   should be read rather than forming part of the actual content of
   the document.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.spanning"/>
    <memberOf key="model.global"/>
    </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en">describes the function (for example  status, insertion,
	 deletion, transposition) of the metamark.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1"><dataRef key="teidata.word"/></datatype>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-04-16" xml:lang="en">identifies one or more elements to which the metamark applies.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="no">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metamark-egXML-zn">
      <line><seg xml:id="tp-ib01">bör</seg><metamark rend="underline" function="transposition" target="#tp-ib01" place="above">2.</metamark>
   og <seg xml:id="tp-ib02">hör</seg>
            <metamark rend="underline" function="transposition" target="#tp-ib02" place="above">1.</metamark>
         </line>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metamark-egXML-pz">
      <surface>
 <metamark function="used" rend="line" target="#X2"/>
 <zone xml:id="zone-X2">
  <line>I am that halfgrown <add>angry</add> boy, fallen asleep</line>
  <line>The tears of foolish passion yet undried</line>
  <line>upon my cheeks.</line>
<!-- ... -->
  <line>I pass through <add>the</add> travels and <del>fortunes</del> of
  <retrace>thirty</retrace>
  </line>
  <line>years and become old,</line>
  <line>Each in its due order comes and goes,</line>
  <line>And thus a message for me comes.</line>
  <line>The</line>
 </zone>
 <metamark function="used" target="#zone-X2">Entered - Yes</metamark>
</surface>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PH-meta"/>
  </listRef>
```

^b10

