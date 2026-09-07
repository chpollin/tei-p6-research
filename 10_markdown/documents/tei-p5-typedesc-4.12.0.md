---
type: representation
source-type: document
source: '[[00_sources/tei-p5-typedesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 typeDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/typeDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# typeDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2230. Git blob: `3fa82e1f5d27ddf603703bf9cec9479f1f870b4d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="gi-typeDesc" ident="typeDesc">
  <gloss versionDate="2020-12-20" xml:lang="en">typeface description</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">description des styles de caractère</gloss>
  <desc versionDate="2008-09-02" xml:lang="en">contains a description of the typefaces or other aspects of
  the printing of an incunable or other printed source.</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">contient la description des styles de caractères ou d'autres aspects de l'impression d'un incunable ou d'une autre source imprimée.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="typeNote" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-typeDesc-egXML-vg">
      <typeDesc>
        <p>Uses an unidentified black letter font, probably from the
	15th century</p>
      </typeDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-typeDesc-egXML-ol">
      <typeDesc>
        <summary>Contains a mixture of blackletter and Roman (antiqua) typefaces</summary>
        <typeNote xml:id="Frak1">Blackletter face, showing
	similarities to those produced in Wuerzburg after 1470.</typeNote>
        <typeNote xml:id="Rom1">Roman face of Venetian origins.</typeNote>
      </typeDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msphwr"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">typeface description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">description des styles de caractère</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-09-02" xml:lang="en">contains a description of the typefaces or other aspects of
  the printing of an incunable or other printed source.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">contient la description des styles de caractères ou d'autres aspects de l'impression d'un incunable ou d'une autre source imprimée.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="typeNote" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-typeDesc-egXML-vg">
      <typeDesc>
        <p>Uses an unidentified black letter font, probably from the
	15th century</p>
      </typeDesc>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-typeDesc-egXML-ol">
      <typeDesc>
        <summary>Contains a mixture of blackletter and Roman (antiqua) typefaces</summary>
        <typeNote xml:id="Frak1">Blackletter face, showing
	similarities to those produced in Wuerzburg after 1470.</typeNote>
        <typeNote xml:id="Rom1">Roman face of Venetian origins.</typeNote>
      </typeDesc>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msphwr"/>
  </listRef>
```

^b9

