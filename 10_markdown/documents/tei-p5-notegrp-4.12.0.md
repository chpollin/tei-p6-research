---
type: representation
source-type: document
source: '[[00_sources/tei-p5-notegrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 noteGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/noteGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# noteGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2840. Git blob: `b5a615a2b25d14442642415a7616beecdfa0d711`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-noteGrp" ident="noteGrp">
  <gloss versionDate="2022-06-09" xml:lang="en">note group</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a group of notes.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.anchoring"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.correspActionPart"/>
    <memberOf key="model.correspContextPart"/>
    <memberOf key="model.correspDescPart"/>
    <memberOf key="model.noteLike"/>
  </classes>
  <content>
    <sequence>
        <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="note"/>
          <elementRef key="noteGrp"/>
        </alternate>
    </sequence>
  </content>
  <exemplum versionDate="2021-01-28" xml:lang="en">
    <p>In the following example, there are two notes in different
    languages, each specifying the content of the annotation relating
    to the same fragment of text:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-noteGrp-egXML-pl" source="#SERAFIN2">
      <p>(...) tamen reuerendos dominos archiepiscopum et canonicos Leopolienses
        necnon episcopum in duplicibus Quatuortemporibus
        <noteGrp>
          <note xml:lang="en">Quatuor Tempora, so called dry fast days (Wednesday, Friday, and Saturday)
            falling on each of the quarters of the year. In the first quarter they were called Cinerum
            (following Ash Wednesday), second Spiritus (following Pentecost), third Crucis
            (after the Exaltation of the Holy Cross, September 14th), and Luciae
            in the fourth (after the feast of St. Lucia, December 13th).
          </note>
          <note xml:lang="pl">Quatuor Tempora, tzw. Suche dni postne (środa, piątek i sobota)
            przypadające cztery razy w roku. W pierwszym kwartale zwały się Cinerum
            (po Popielcu), w drugim Spiritus (po Zielonych Świętach), w trzecim Crucis
            (po święcie Podwyższenia Krzyża 14 września), w czwartym Luciae
            (po dniu św. Łucji 13 grudnia).
          </note>
        </noteGrp>
        totaliter expediui.
      </p>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CONONOGR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2022-06-09" xml:lang="en">note group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a group of notes.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.anchoring"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.correspActionPart"/>
    <memberOf key="model.correspContextPart"/>
    <memberOf key="model.correspDescPart"/>
    <memberOf key="model.noteLike"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
        <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="note"/>
          <elementRef key="noteGrp"/>
        </alternate>
    </sequence>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2021-01-28" xml:lang="en">
    <p>In the following example, there are two notes in different
    languages, each specifying the content of the annotation relating
    to the same fragment of text:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-noteGrp-egXML-pl" source="#SERAFIN2">
      <p>(...) tamen reuerendos dominos archiepiscopum et canonicos Leopolienses
        necnon episcopum in duplicibus Quatuortemporibus
        <noteGrp>
          <note xml:lang="en">Quatuor Tempora, so called dry fast days (Wednesday, Friday, and Saturday)
            falling on each of the quarters of the year. In the first quarter they were called Cinerum
            (following Ash Wednesday), second Spiritus (following Pentecost), third Crucis
            (after the Exaltation of the Holy Cross, September 14th), and Luciae
            in the fourth (after the feast of St. Lucia, December 13th).
          </note>
          <note xml:lang="pl">Quatuor Tempora, tzw. Suche dni postne (środa, piątek i sobota)
            przypadające cztery razy w roku. W pierwszym kwartale zwały się Cinerum
            (po Popielcu), w drugim Spiritus (po Zielonych Świętach), w trzecim Crucis
            (po święcie Podwyższenia Krzyża 14 września), w czwartym Luciae
            (po dniu św. Łucji 13 grudnia).
          </note>
        </noteGrp>
        totaliter expediui.
      </p>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONONOGR"/>
  </listRef>
```

^b6

