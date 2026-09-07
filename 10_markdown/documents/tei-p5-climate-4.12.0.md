---
type: representation
source-type: document
source: '[[00_sources/tei-p5-climate-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 climate
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/climate.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# climate

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3608. Git blob: `e2ca4c3d4d7559b59cb12e68a384f3ddb7ada67f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="climate" xml:id="gi-climate" module="namesdates">
  <gloss versionDate="2008-12-09" xml:lang="en">climate</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">climat</gloss>
  <desc versionDate="2007-06-14" xml:lang="en">contains information about the physical climate of a place.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">장소의 기후에 관한 정보를 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene información sobre el clima físico de un lugar.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ある場所の天候に関する情報を示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient des informations sur le climat physique d'un lieu.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene informazioni relative al clima fisico di un luogo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
      </alternate>
      <elementRef key="climate" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-climate-egXML-bn">
      <place xml:id="ROMA">
        <placeName>Rome</placeName>
        <!-- ... -->
        <climate>
          <ab>
            <table>
              <head>24-hr Average Temperature</head>
              <row>
                <cell/>
                <cell role="label">Jan</cell>
                <cell role="label">Jun</cell>
                <cell role="label">Dec</cell>
              </row>
              <row>
                <cell role="label">°C</cell>
                <cell role="data">7.1</cell>
                <cell role="data">21.7</cell>
                <cell role="data">8.3</cell>
              </row>
              <row>
                <cell role="label">°F</cell>
                <cell role="data">44.8</cell>
                <cell role="data">71.1</cell>
                <cell role="data">46.9</cell>
              </row>
            </table>
          </ab>
          <note>Taken from <bibl><abbr>GHCN 2 Beta</abbr>: The Global Historical Climatology Network,
                            version 2 beta, 1904 months between 1811 and 1980. <ptr target="http://www.worldclimate.com/cgi-bin/data.pl?ref=N41E012+1202+0004058G2"/></bibl>
                    </note>
        </climate>
      </place>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDGEOGste"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">climate</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">climat</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-06-14" xml:lang="en">contains information about the physical climate of a place.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">장소의 기후에 관한 정보를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene información sobre el clima físico de un lugar.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ある場所の天候に関する情報を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient des informations sur le climat physique d'un lieu.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene informazioni relative al clima fisico di un luogo.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
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
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
      </alternate>
      <elementRef key="climate" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-climate-egXML-bn">
      <place xml:id="ROMA">
        <placeName>Rome</placeName>
        <!-- ... -->
        <climate>
          <ab>
            <table>
              <head>24-hr Average Temperature</head>
              <row>
                <cell/>
                <cell role="label">Jan</cell>
                <cell role="label">Jun</cell>
                <cell role="label">Dec</cell>
              </row>
              <row>
                <cell role="label">°C</cell>
                <cell role="data">7.1</cell>
                <cell role="data">21.7</cell>
                <cell role="data">8.3</cell>
              </row>
              <row>
                <cell role="label">°F</cell>
                <cell role="data">44.8</cell>
                <cell role="data">71.1</cell>
                <cell role="data">46.9</cell>
              </row>
            </table>
          </ab>
          <note>Taken from <bibl><abbr>GHCN 2 Beta</abbr>: The Global Historical Climatology Network,
                            version 2 beta, 1904 months between 1811 and 1980. <ptr target="http://www.worldclimate.com/cgi-bin/data.pl?ref=N41E012+1202+0004058G2"/></bibl>
                    </note>
        </climate>
      </place>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDGEOGste"/>
  </listRef>
```

^b12

