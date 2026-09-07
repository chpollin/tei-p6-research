---
type: representation
source-type: document
source: '[[00_sources/tei-p5-trait-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 trait
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/trait.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# trait

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5333. Git blob: `4719f3af204c0325f256c692e04e8027356ab830`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-trait" ident="trait">
  <gloss versionDate="2009-03-19" xml:lang="en">trait</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">trait distinctif</gloss>
  <desc versionDate="2011-12-01" xml:lang="en">contains a description of some status or quality attributed to a person, place, or organization typically, but not necessarily, independent of the volition or action of the holder and usually not at some specific time or for a specific date range.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient la description d'une caractéristique culturelle et en principe permanente, attribuée à une personne ou à un lieu.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사람 또는 장소에 관한, 문화적으로 결정된 특성 기술을 포함한다.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物や場所の文化的な特性を示す。</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de una característica personal o cultural determinada atribuida a una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la descrizione di una caratteristica personale o legata alla cultura di appartenenza di una determinata persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <elementRef key="trait" minOccurs="1" maxOccurs="unbounded"/>
        <sequence>
          <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
          <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.noteLike"/>
            <classRef key="model.biblLike"/>
          </alternate>
        </sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.labelLike"/>
          <classRef key="model.noteLike"/>
          <classRef key="model.biblLike"/>
        </alternate>
      </alternate>
    </sequence>
  </content>
  <!--    <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-bp">
            <trait cert="high" type="social" from="1987-01-01" to="1997-12-31">
                <label>citizenship</label>
                <desc>Between 1987 and 1997 held status of naturalized UK citizen</desc>
            </trait>
        </egXML>
    </exemplum>
    <exemplum xml:lang="zh-TW">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-sd">
            <trait cert="high" type="social" from="1987-01-01" to="1997-12-31">
                <label>公民權</label>
                <desc>在1987到1997年是英國的自然公民</desc>
            </trait>
        </egXML>
    </exemplum>-->
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-ao">
      <trait type="physical">
        <label>眼珠顏色</label>
        <desc>藍色</desc>
      </trait>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-ap">
      <trait type="physical">
        <label>Couleur des yeux</label>
        <desc>bleu</desc>
      </trait>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-aq">
      <trait type="physical">
        <label>Eye colour</label>
        <desc>Blue</desc>
      </trait>
    </egXML>
  </exemplum>
  <remarks ident="trait-remarks" versionDate="2011-12-01" xml:lang="en">
    <p>Where there is confusion between <gi>trait</gi> and <gi>state</gi> the more general purpose
      element <gi>state</gi> should be used even for unchanging characteristics. If you wish to
      distinguish between characteristics that are generally perceived to be time-bound states and
      those assumed to be fixed traits, then <gi>trait</gi> is available for the more static of
      these. The <gi>state</gi> element encodes characteristics which are sometimes assumed to
      change, often at specific times or over a date range, whereas the <gi>trait</gi> elements are
      used to record characteristics, such as eye-colour, which are less subject to change. Traits are typically, but not necessarily, 
      independent of the volition or action of the holder.</p>
  </remarks>
  <listRef>
    <ptr target="#NDPERSbp"/>
    <ptr target="#NDPERSEpc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="en">trait</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="fr">trait distinctif</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-12-01" xml:lang="en">contains a description of some status or quality attributed to a person, place, or organization typically, but not necessarily, independent of the volition or action of the holder and usually not at some specific time or for a specific date range.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient la description d'une caractéristique culturelle et en principe permanente, attribuée à une personne ou à un lieu.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사람 또는 장소에 관한, 문화적으로 결정된 특성 기술을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物や場所の文化的な特性を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de una característica personal o cultural determinada atribuida a una persona.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la descrizione di una caratteristica personale o legata alla cultura di appartenenza di una determinata persona.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <elementRef key="trait" minOccurs="1" maxOccurs="unbounded"/>
        <sequence>
          <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
          <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.noteLike"/>
            <classRef key="model.biblLike"/>
          </alternate>
        </sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.labelLike"/>
          <classRef key="model.noteLike"/>
          <classRef key="model.biblLike"/>
        </alternate>
      </alternate>
    </sequence>
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-ao">
      <trait type="physical">
        <label>眼珠顏色</label>
        <desc>藍色</desc>
      </trait>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-ap">
      <trait type="physical">
        <label>Couleur des yeux</label>
        <desc>bleu</desc>
      </trait>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trait-egXML-aq">
      <trait type="physical">
        <label>Eye colour</label>
        <desc>Blue</desc>
      </trait>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="trait-remarks" versionDate="2011-12-01" xml:lang="en">
    <p>Where there is confusion between <gi>trait</gi> and <gi>state</gi> the more general purpose
      element <gi>state</gi> should be used even for unchanging characteristics. If you wish to
      distinguish between characteristics that are generally perceived to be time-bound states and
      those assumed to be fixed traits, then <gi>trait</gi> is available for the more static of
      these. The <gi>state</gi> element encodes characteristics which are sometimes assumed to
      change, often at specific times or over a date range, whereas the <gi>trait</gi> elements are
      used to record characteristics, such as eye-colour, which are less subject to change. Traits are typically, but not necessarily, 
      independent of the volition or action of the holder.</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSbp"/>
    <ptr target="#NDPERSEpc"/>
  </listRef>
```

^b15

