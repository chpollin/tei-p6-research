---
type: representation
source-type: document
source: '[[00_sources/tei-p5-unit-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 unit
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/unit.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# unit

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3398. Git blob: `6ce7696bb8424b3d89f0d83e2e51a1008e9a75bc`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-unit" ident="unit">
  <desc versionDate="2018-07-17" xml:lang="en">contains a symbol, a word or a phrase referring to a unit of measurement in any kind of formal or informal system.</desc>
  <desc versionDate="2018-07-17" xml:lang="de">enthält ein Symbol, ein Wort oder eine Phrase, die sich auf eine Maßeinheit in einem formellen oder informellen System bezieht.</desc>
  <desc versionDate="2023-07-29" xml:lang="ja">公式・非公式に関わらず、単位を表す記号や単語、語句を含む。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.measurement"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
  </classes>
  <content>
     <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum versionDate="2019-07-10" xml:lang="en">
    <p>Here is an example of a <gi>unit</gi> element holding a <att>unitRef</att> attribute that points to a definition of the unit in the TEI header.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-te">
      <measure><num>3</num> <unit unitRef="#ell">ells</unit></measure>

    <!-- In the TEI Header: -->
      
      <encodingDesc>
        <unitDecl>
          <unitDef xml:id="ell">
            <label>ell</label>
            <placeName ref="#iceland"/>
            <desc>A unit of measure for cloth, roughly equivalent to 18 inches, or from an adult male’s elbow to the tip of the middle finger.</desc>
          </unitDef>
        </unitDecl>
      </encodingDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-gc">
      <measure>
        <num>2</num>
        <unit>kg</unit></measure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-fh">
      <measure type="value"><num>3</num><unit type="time" unit="min">minute</unit></measure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-sd">
      <measure type="list"><num>1</num>, <num>2</num>, <num>5</num>, <num>7</num>
        <unit type="length" unit="mm">millimètres</unit></measure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-so">
      <measure type="interval"><num atLeast="1.2">1.2</num> to <num atMost="5.6">5.6</num>
        <unit type="velocity" unit="km/h">km/h</unit></measure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-xi">
      <p>Light travels at <num value="3E10">3×10^10</num>
        <unit type="rate" unit="cm/s">
          <unit type="space">cm</unit> per <unit type="time">second</unit>
        </unit>.</p>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CONANU" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-07-17" xml:lang="en">contains a symbol, a word or a phrase referring to a unit of measurement in any kind of formal or informal system.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2018-07-17" xml:lang="de">enthält ein Symbol, ein Wort oder eine Phrase, die sich auf eine Maßeinheit in einem formellen oder informellen System bezieht.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2023-07-29" xml:lang="ja">公式・非公式に関わらず、単位を表す記号や単語、語句を含む。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.measurement"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
  </classes>
```

^b4

### Block 5

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
     <macroRef key="macro.phraseSeq"/>
  </content>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2019-07-10" xml:lang="en">
    <p>Here is an example of a <gi>unit</gi> element holding a <att>unitRef</att> attribute that points to a definition of the unit in the TEI header.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-te">
      <measure><num>3</num> <unit unitRef="#ell">ells</unit></measure>

    <!-- In the TEI Header: -->
      
      <encodingDesc>
        <unitDecl>
          <unitDef xml:id="ell">
            <label>ell</label>
            <placeName ref="#iceland"/>
            <desc>A unit of measure for cloth, roughly equivalent to 18 inches, or from an adult male’s elbow to the tip of the middle finger.</desc>
          </unitDef>
        </unitDecl>
      </encodingDesc>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-gc">
      <measure>
        <num>2</num>
        <unit>kg</unit></measure>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-fh">
      <measure type="value"><num>3</num><unit type="time" unit="min">minute</unit></measure>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-sd">
      <measure type="list"><num>1</num>, <num>2</num>, <num>5</num>, <num>7</num>
        <unit type="length" unit="mm">millimètres</unit></measure>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-so">
      <measure type="interval"><num atLeast="1.2">1.2</num> to <num atMost="5.6">5.6</num>
        <unit type="velocity" unit="km/h">km/h</unit></measure>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-unit-egXML-xi">
      <p>Light travels at <num value="3E10">3×10^10</num>
        <unit type="rate" unit="cm/s">
          <unit type="space">cm</unit> per <unit type="time">second</unit>
        </unit>.</p>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONANU" type="div3"/>
  </listRef>
```

^b12

