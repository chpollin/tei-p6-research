---
type: representation
source-type: document
source: '[[00_sources/tei-p5-pc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 pc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/pc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# pc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4949. Git blob: `517f06762e13b223aaeac96750c8f23f43c16292`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. --><!--
  attribute force { data.word }?,
  attribute unit { data.word }?,
  attribute direction { "before" | "after" | "unknown" | "inapplicable" }?,
-->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="gi-pc" ident="pc">
  <gloss versionDate="2009-06-10" xml:lang="en">punctuation character</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Interpunktionszeichen</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">contains a character or string of characters regarded as constituting a single punctuation mark.</desc>
  <desc xml:lang="fr" versionDate="2007-06-12">contient un caractère ou une chaîne de caractères  considérés comme un signe de ponctuation unique.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält ein Zeichen oder eine Zeichenkette, die ein einzelnes Interpunktionszeichen repräsentiert.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.linguistic"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <elementRef key="c"/>
      <classRef key="model.pPart.edit"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="force" usage="opt">
      <desc versionDate="2009-06-18" xml:lang="en">indicates the extent to which this punctuation mark
      conventionally separates words or phrases.</desc>
      <desc versionDate="2017-06-19" xml:lang="de">gibt an, in welchem Maß das betreffende Interpunktionszeichen Wörter oder Phrasen gewöhnlich
        voneinander trennt.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="strong">
          <desc versionDate="2009-06-18" xml:lang="en">the punctuation mark is a word separator</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Interpunktionszeichen ist ein Wortbegrenzungszeichen.</desc>
        </valItem>
        <valItem ident="weak">
          <desc versionDate="2009-06-18" xml:lang="en">the punctuation mark is not a word separator</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Interpunktionszeichen ist kein Wortbegrenzungszeichen.</desc>
        </valItem>
        <valItem ident="inter">
          <desc versionDate="2009-06-18" xml:lang="en">the punctuation mark may or may not be a word separator</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Interpunktionszeichen kann oder kann nicht als Wortbegrenzungszeichen fungieren.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="unit" usage="opt">
      <desc versionDate="2009-06-18" xml:lang="en">provides a name for the kind of unit delimited by  this punctuation mark.</desc>
      <desc versionDate="2017-06-19" xml:lang="de">gibt die Art der Einheit an, die durch das Interpunktionszeichen begrenzt wird.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
    <attDef ident="pre" usage="opt">
      <desc versionDate="2009-06-18" xml:lang="en">indicates whether this punctuation mark precedes or
      follows the unit it delimits.</desc>
      <desc versionDate="2017-06-19" xml:lang="de">gibt an, ob das Interpunktionszeichen der Einheit, die es begrenzt, vorangeht oder folgt.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pc-egXML-rb">
      <phr>
        <w>do</w>
        <w>you</w>
        <w>understand</w>
        <pc type="interrogative">?</pc>
      </phr>
    </egXML>
  </exemplum>
  <!-- better examples needed -->
  <exemplum xml:lang="en">
    <p>Example encoding of the German sentence <mentioned>Wir fahren in den Urlaub.</mentioned>, encoded with attributes from 
      <ident type="class">att.linguistic</ident> discussed in section <ptr target="#AILALW"/>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pc-egXML-kx">
      <s>
        <w pos="PPER" msd="1.Pl.*.Nom">Wir</w>
        <w pos="VVFIN" msd="1.Pl.Pres.Ind">fahren</w>
        <w pos="APPR" msd="--">in</w>
        <w pos="ART" msd="Def.Masc.Akk.Sg.">den</w>
        <w pos="NN" msd="Masc.Akk.Sg.">Urlaub</w>
        <pc pos="$." msd="--" join="left">.</pc>
      </s>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#AIPC"/>
    <ptr target="#AILALW"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-06-10" xml:lang="en">punctuation character</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Interpunktionszeichen</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains a character or string of characters regarded as constituting a single punctuation mark.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc xml:lang="fr" versionDate="2007-06-12">contient un caractère ou une chaîne de caractères  considérés comme un signe de ponctuation unique.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält ein Zeichen oder eine Zeichenkette, die ein einzelnes Interpunktionszeichen repräsentiert.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.linguistic"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
  </classes>
```

^b6

### Block 7

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <elementRef key="c"/>
      <classRef key="model.pPart.edit"/>
    </alternate>
  </content>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2009-06-18" xml:lang="en">indicates the extent to which this punctuation mark
      conventionally separates words or phrases.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">gibt an, in welchem Maß das betreffende Interpunktionszeichen Wörter oder Phrasen gewöhnlich
        voneinander trennt.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="strong">
          <desc versionDate="2009-06-18" xml:lang="en">the punctuation mark is a word separator</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Interpunktionszeichen ist ein Wortbegrenzungszeichen.</desc>
        </valItem>
        <valItem ident="weak">
          <desc versionDate="2009-06-18" xml:lang="en">the punctuation mark is not a word separator</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Interpunktionszeichen ist kein Wortbegrenzungszeichen.</desc>
        </valItem>
        <valItem ident="inter">
          <desc versionDate="2009-06-18" xml:lang="en">the punctuation mark may or may not be a word separator</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Interpunktionszeichen kann oder kann nicht als Wortbegrenzungszeichen fungieren.</desc>
        </valItem>
      </valList>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2009-06-18" xml:lang="en">provides a name for the kind of unit delimited by  this punctuation mark.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">gibt die Art der Einheit an, die durch das Interpunktionszeichen begrenzt wird.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2009-06-18" xml:lang="en">indicates whether this punctuation mark precedes or
      follows the unit it delimits.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">gibt an, ob das Interpunktionszeichen der Einheit, die es begrenzt, vorangeht oder folgt.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pc-egXML-rb">
      <phr>
        <w>do</w>
        <w>you</w>
        <w>understand</w>
        <pc type="interrogative">?</pc>
      </phr>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <p>Example encoding of the German sentence <mentioned>Wir fahren in den Urlaub.</mentioned>, encoded with attributes from 
      <ident type="class">att.linguistic</ident> discussed in section <ptr target="#AILALW"/>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pc-egXML-kx">
      <s>
        <w pos="PPER" msd="1.Pl.*.Nom">Wir</w>
        <w pos="VVFIN" msd="1.Pl.Pres.Ind">fahren</w>
        <w pos="APPR" msd="--">in</w>
        <w pos="ART" msd="Def.Masc.Akk.Sg.">den</w>
        <w pos="NN" msd="Masc.Akk.Sg.">Urlaub</w>
        <pc pos="$." msd="--" join="left">.</pc>
      </s>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AIPC"/>
    <ptr target="#AILALW"/>
  </listRef>
```

^b20

