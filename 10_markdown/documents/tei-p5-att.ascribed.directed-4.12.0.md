---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.ascribed.directed-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.ascribed.directed
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.ascribed.directed.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.ascribed.directed

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3149. Git blob: `d35d4426892c6a2e8755f30e6f6e8b823f1db810`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-ascribed.directed" ident="att.ascribed.directed">
    <desc versionDate="2018-07-19" xml:lang="en">provides attributes for elements representing speech or action that can be directed at a
        group or individual.</desc>
    <classes>
        
        <memberOf key="att.ascribed"/>
    </classes>
    <attList>
        <attDef ident="toWhom">
            <desc versionDate="2018-07-19" xml:lang="en">indicates the person, or group of people, to whom a speech act or action is directed.</desc>
            
            <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
            <exemplum xml:lang="en">
                <p>In the following example from Mary Pix's The False Friend, speeches (<gi>sp</gi>) in the body of the play 
                    are linked to <gi>castItem</gi> elements in the <gi>castList</gi> using the <att>toWhom</att>
                    attribute, which is used to specify who the speech is directed to. Additionally, the <gi>stage</gi>
                    includes <att>toWhom</att> to indicate the directionality of the action. 
                </p>
                <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ascribed.directed-egXML-rg" xml:lang="en" valid="feasible" source="#toWhom-eg-1">
                    <castItem type="role">
                        <role xml:id="emil">Emilius.</role>
                    </castItem>
                    <castItem type="role">
                        <role xml:id="lov">Lovisa</role>
                    </castItem>
                    <castItem type="role">
                        <role xml:id="serv">A servant</role>
                    </castItem>
                    <!-- ... -->
                    <sp who="#emil" toWhom="#lov">
                        <speaker>Emil.</speaker>
                        <l n="1">My love!</l>
                    </sp>
                    <sp who="#lov" toWhom="#emil">
                        <speaker>Lov.</speaker>
                        <l n="2">I have no Witness of my Noble Birth</l>
                        <stage who="emil" toWhom="#serv">Pointing to her Woman.</stage>
                        <l>But that poor helpless wretch——</l>
                    </sp>
                </egXML>
            </exemplum>
            <remarks ident="att.ascribed.directed-attr.toWhom-remarks" versionDate="2013-11-22" xml:lang="en"><p>To indicate the recipient of written correspondence, use the elements used in section <ptr target="#HD44CD"/>, rather than a <att>toWhom</att> attribute.</p></remarks>
        </attDef>
    </attList>
    <listRef>
        <ptr target="#COHQQ"/>
        <ptr target="#TSBA"/>
    </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-07-19" xml:lang="en">provides attributes for elements representing speech or action that can be directed at a
        group or individual.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
        
        <memberOf key="att.ascribed"/>
    </classes>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2018-07-19" xml:lang="en">indicates the person, or group of people, to whom a speech act or action is directed.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
                <p>In the following example from Mary Pix's The False Friend, speeches (<gi>sp</gi>) in the body of the play 
                    are linked to <gi>castItem</gi> elements in the <gi>castList</gi> using the <att>toWhom</att>
                    attribute, which is used to specify who the speech is directed to. Additionally, the <gi>stage</gi>
                    includes <att>toWhom</att> to indicate the directionality of the action. 
                </p>
                <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ascribed.directed-egXML-rg" xml:lang="en" valid="feasible" source="#toWhom-eg-1">
                    <castItem type="role">
                        <role xml:id="emil">Emilius.</role>
                    </castItem>
                    <castItem type="role">
                        <role xml:id="lov">Lovisa</role>
                    </castItem>
                    <castItem type="role">
                        <role xml:id="serv">A servant</role>
                    </castItem>
                    <!-- ... -->
                    <sp who="#emil" toWhom="#lov">
                        <speaker>Emil.</speaker>
                        <l n="1">My love!</l>
                    </sp>
                    <sp who="#lov" toWhom="#emil">
                        <speaker>Lov.</speaker>
                        <l n="2">I have no Witness of my Noble Birth</l>
                        <stage who="emil" toWhom="#serv">Pointing to her Woman.</stage>
                        <l>But that poor helpless wretch——</l>
                    </sp>
                </egXML>
            </exemplum>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.ascribed.directed-attr.toWhom-remarks" versionDate="2013-11-22" xml:lang="en"><p>To indicate the recipient of written correspondence, use the elements used in section <ptr target="#HD44CD"/>, rather than a <att>toWhom</att> attribute.</p></remarks>
```

^b6

### Block 7

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
        <ptr target="#COHQQ"/>
        <ptr target="#TSBA"/>
    </listRef>
```

^b7

