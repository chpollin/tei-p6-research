---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.gaijiprop-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.gaijiProp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.gaijiProp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.gaijiProp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5523. Git blob: `a79e8bcb48d9912364feb93f729045854b6518db`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" ident="att.gaijiProp" module="gaiji" type="atts" xml:id="class-attr-gaijiProp">
  <desc versionDate="2020-01-28" xml:lang="en">provides attributes for defining the properties of non-standard characters or glyphs.</desc>
  <desc versionDate="2025-02-06" xml:lang="de">stellt Attribute zur Definition der Eigenschaften von nicht standardisierten Zeichen und Glyphen bereit.</desc>
  <desc versionDate="2020-02-05" xml:lang="it">fornisce attributi per definire le proprietà di caratteri o glifi non standard.</desc>
  <classes>    
    <memberOf key="att.datable"/>
  </classes>
  <attList org="group">
    <attDef ident="name" usage="req">
      <desc versionDate="2020-01-28" xml:lang="en">provides the name of the character or glyph
        property being defined.</desc>
      <datatype maxOccurs="1">
        <dataRef key="teidata.xmlName"/>
      </datatype>
    </attDef>
    <attDef ident="value" usage="req">
      <desc versionDate="2020-01-28" xml:lang="en">provides the value of the character or
        glyph property being defined.</desc>
      <datatype>
        <dataRef key="teidata.text"/>
      </datatype>
    </attDef>
    <attDef ident="version" usage="opt">
      <desc versionDate="2020-01-28" xml:lang="en">specifies the version number of the Unicode Standard in which this property name is defined.</desc>
      <desc versionDate="2019-07-11" xml:lang="de">gibt die Versionsnummer eines externen Standards an, in dem dieser Eigenschaftsname definiert ist.</desc>
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="semi">
        <valItem ident="1.0.1"/>
        <valItem ident="1.1"/>
        <valItem ident="2.0"/>
        <valItem ident="2.1"/>
        <valItem ident="3.0"/>
        <valItem ident="3.1"/>
        <valItem ident="3.2"/>
        <valItem ident="4.0"/>
        <valItem ident="4.1"/>
        <valItem ident="5.0"/>
        <valItem ident="5.1"/>
        <valItem ident="5.2"/>
        <valItem ident="6.0"/>
        <valItem ident="6.1"/>
        <valItem ident="6.2"/>
        <valItem ident="6.3"/>
        <valItem ident="7.0"/>
        <valItem ident="8.0"/>
        <valItem ident="9.0"/>
        <valItem ident="10.0"/>
        <valItem ident="11.0"/>
        <valItem ident="12.0"/>
        <valItem ident="12.1"/>
        <valItem ident="13.0"/>
        <valItem ident="14.0"/>
        <valItem ident="15.0"/>
        <valItem ident="unassigned"/>
      </valList>
    </attDef>
    <attDef ident="scheme" usage="opt">
      <desc versionDate="2023-08-12" xml:lang="en">supplies the name of the character set system from which this property is drawn.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>Unicode</defaultVal>
      <valList type="open">
        <valItem ident="Unicode">
          <gloss xml:lang="en" versionDate="2023-08-12">Unicode</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">ISO 10646</desc>
        </valItem>
        <valItem ident="Bridwell">
          <gloss xml:lang="en" versionDate="2023-08-12">E. Nelson Bridwell</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Original character set developed by E. Nelson Bridwell as described by Al Turniansky, in use from the 1950s to 1985.</desc>
        </valItem>
        <valItem ident="Brewer">
          <gloss xml:lang="en" versionDate="2023-08-12">Georg Brewer</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Developed by Georg Brewer, with a look similar to the Byrne glyphs. Like the Byrne set, this is not a true character set, but rather a set of alternate glyphs.</desc>
        </valItem>
        <valItem ident="Doyle">
          <gloss xml:lang="en" versionDate="2023-08-12">Darren Doyle</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Glyph set (in some cases associated with multiple characters) developed by Darren Doyle as part of a comprehensive version of the language created in part for an invented language classs at UT Austin in 2006.</desc>
        </valItem>
        <valItem ident="Schreyer">
          <gloss xml:lang="en" versionDate="2023-08-12">Christine Schreyer</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Character set (without actual codepoints) of 153 characters developed, along with pronunciation rules, roughly 300 words, and a grammar, developed by Christine Schreyer developed in 2012 for Warner Brothers.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum versionDate="2019-07-01" xml:lang="en">
    <p>In this example a definition for the Unicode property <name>Decomposition Mapping</name>
    is provided.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-gaijiProp-egXML-ii" source="#UND">
      <unicodeProp name="Decomposition_Mapping" value="circle"/>
    </egXML>
  </exemplum>
  <remarks ident="att.gaijiProp-remarks" versionDate="2019-06-29" xml:lang="en">
    <p>All name-only attributes need an xs:boolean attribute value inside <att>value</att>.</p>
  </remarks>
  <listRef>
    <ptr target="#WD"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-01-28" xml:lang="en">provides attributes for defining the properties of non-standard characters or glyphs.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2025-02-06" xml:lang="de">stellt Attribute zur Definition der Eigenschaften von nicht standardisierten Zeichen und Glyphen bereit.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2020-02-05" xml:lang="it">fornisce attributi per definire le proprietà di caratteri o glifi non standard.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>    
    <memberOf key="att.datable"/>
  </classes>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2020-01-28" xml:lang="en">provides the name of the character or glyph
        property being defined.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="1">
        <dataRef key="teidata.xmlName"/>
      </datatype>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2020-01-28" xml:lang="en">provides the value of the character or
        glyph property being defined.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.text"/>
      </datatype>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2020-01-28" xml:lang="en">specifies the version number of the Unicode Standard in which this property name is defined.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2019-07-11" xml:lang="de">gibt die Versionsnummer eines externen Standards an, in dem dieser Eigenschaftsname definiert ist.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[3]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="1.0.1"/>
        <valItem ident="1.1"/>
        <valItem ident="2.0"/>
        <valItem ident="2.1"/>
        <valItem ident="3.0"/>
        <valItem ident="3.1"/>
        <valItem ident="3.2"/>
        <valItem ident="4.0"/>
        <valItem ident="4.1"/>
        <valItem ident="5.0"/>
        <valItem ident="5.1"/>
        <valItem ident="5.2"/>
        <valItem ident="6.0"/>
        <valItem ident="6.1"/>
        <valItem ident="6.2"/>
        <valItem ident="6.3"/>
        <valItem ident="7.0"/>
        <valItem ident="8.0"/>
        <valItem ident="9.0"/>
        <valItem ident="10.0"/>
        <valItem ident="11.0"/>
        <valItem ident="12.0"/>
        <valItem ident="12.1"/>
        <valItem ident="13.0"/>
        <valItem ident="14.0"/>
        <valItem ident="15.0"/>
        <valItem ident="unassigned"/>
      </valList>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2023-08-12" xml:lang="en">supplies the name of the character set system from which this property is drawn.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[4]/defaultVal[1]`.

```xml
<defaultVal>Unicode</defaultVal>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[4]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="Unicode">
          <gloss xml:lang="en" versionDate="2023-08-12">Unicode</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">ISO 10646</desc>
        </valItem>
        <valItem ident="Bridwell">
          <gloss xml:lang="en" versionDate="2023-08-12">E. Nelson Bridwell</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Original character set developed by E. Nelson Bridwell as described by Al Turniansky, in use from the 1950s to 1985.</desc>
        </valItem>
        <valItem ident="Brewer">
          <gloss xml:lang="en" versionDate="2023-08-12">Georg Brewer</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Developed by Georg Brewer, with a look similar to the Byrne glyphs. Like the Byrne set, this is not a true character set, but rather a set of alternate glyphs.</desc>
        </valItem>
        <valItem ident="Doyle">
          <gloss xml:lang="en" versionDate="2023-08-12">Darren Doyle</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Glyph set (in some cases associated with multiple characters) developed by Darren Doyle as part of a comprehensive version of the language created in part for an invented language classs at UT Austin in 2006.</desc>
        </valItem>
        <valItem ident="Schreyer">
          <gloss xml:lang="en" versionDate="2023-08-12">Christine Schreyer</gloss>
          <desc xml:lang="en" versionDate="2023-08-12">Character set (without actual codepoints) of 153 characters developed, along with pronunciation rules, roughly 300 words, and a grammar, developed by Christine Schreyer developed in 2012 for Warner Brothers.</desc>
        </valItem>
      </valList>
```

^b16

### Block 17

XML location: `/classSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2019-07-01" xml:lang="en">
    <p>In this example a definition for the Unicode property <name>Decomposition Mapping</name>
    is provided.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-gaijiProp-egXML-ii" source="#UND">
      <unicodeProp name="Decomposition_Mapping" value="circle"/>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.gaijiProp-remarks" versionDate="2019-06-29" xml:lang="en">
    <p>All name-only attributes need an xs:boolean attribute value inside <att>value</att>.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#WD"/>
  </listRef>
```

^b19

