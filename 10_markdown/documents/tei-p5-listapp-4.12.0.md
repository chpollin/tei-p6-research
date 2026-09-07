---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listapp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listApp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listApp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listApp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4564. Git blob: `c344fe0c60e910c34e27fa018d17c84deb19b69c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. --><!-- MDH 2012-07-14. --><!-- Only one useful example so far. The call is out for more, but no response as yet. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="textcrit" xml:id="gi-listApp" ident="listApp">
  <gloss versionDate="2012-08-14" xml:lang="en">list of apparatus entries</gloss>
  <gloss versionDate="2012-07-14" xml:lang="fr">liste d'entrées dans un apparat critique</gloss>
  <gloss versionDate="2021-02-02" xml:lang="it">lista delle voci di un apparato critico</gloss>
  <desc versionDate="2012-07-15" xml:lang="en">contains a list of apparatus entries.</desc>
  <desc versionDate="2012-07-14" xml:lang="fr">contient une liste d'entrées dans un apparat critique.</desc>
  <desc versionDate="2021-02-02" xml:lang="it">contiene una lista delle voci di un apparato critico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="app"/>
        <elementRef key="listApp"/>
      </alternate>
    </sequence>
  </content>
  <constraintSpec ident="listApp-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listApp"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en" versionDate="2012-08-06">
    <p>In the following example from the exegetical Yasna, the base text is encoded in the <gi>body</gi> of 
    the document, and two separate <gi>listApp</gi> elements are used in the <gi>back</gi>, containing 
    variant readings written in different scripts.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listApp-egXML-te">
      <body>
        <div>
          <lg type="stanza" xml:id="Y-36.01" xml:lang="pal-Avst" rend="italic">
            <l xml:id="Y-36.01_L-1">
              <w xml:id="Y-36.01_L1_W-01">ahiiā</w>
              <w xml:id="Y-36.01_L1_W-02">ϑβā</w>
              <w xml:id="Y-36.01_L1_W-03">āϑrō</w>
              <w xml:id="Y-36.01_L1_W-04">vərəzə̄nā</w>
              <w xml:id="Y-36.01_L1_W-05">paouruiiē</w>
              <w xml:id="Y-36.01_L1_W-06">pairijasāmaiδē</w>
              <w xml:id="Y-36.01_L1_W-07">mazdā</w>
              <w xml:id="Y-36.01_L1_W-08">ahurā</w>
            </l>
            <!-- ... -->
          </lg>
        </div>
      </body>
      <!-- ... -->
      <back>
        <div>
          <listApp xml:id="CA_Y-36" xml:lang="pal-Avst">
            <head>Variants from witnesses in Avestan script</head>
            <app from="#Y-36.01_L1_W-01">
              <rdg wit="#Pt4 #F2 #J2 #M1">ahiiā</rdg>
            </app>
            <app from="#Y-36.01_L1_W-02">
              <rdg wit="#Pt4 #F2 #J2 #M1">ϑβā</rdg>
            </app>
            <app from="#Y-36.01_L1_W-03">
              <rdg wit="#Pt4 #J2 #M1">āϑrō</rdg>
              <rdg wit="#F2">āϑrōi</rdg>
            </app>
            <!-- ... -->
          </listApp>
          <listApp xml:id="CA_PY-36" xml:lang="pal-Phlv">
            <head>Variants from witnesses written in Pahlavi script</head>
            <app from="#PY-36.01_L1_W-01">
              <rdg wit="#Pt4 #F2 #J2 #M1">ʾytwnˈ</rdg>
            </app>
            <app from="#PY-36.01_L1_W-02">
              <rdg wit="#Pt4 #F2 #J2 #M1">ʾwˈ</rdg>
            </app>
            <app from="#PY-36.01_L1_W-03">
              <rdg wit="#Pt4 #F2 #J2 #M1">ḤNʾ</rdg>
            </app>
            <!-- ... -->
          </listApp>
        </div>
      </back>
    </egXML>
  </exemplum>
  <remarks ident="listApp-remarks" versionDate="2012-08-06" xml:lang="en">
    <p><gi>listApp</gi> elements would normally be located in the <gi>back</gi> part of a document,
    but they may appear elsewhere.</p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLK"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2012-08-14" xml:lang="en">list of apparatus entries</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2012-07-14" xml:lang="fr">liste d'entrées dans un apparat critique</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2021-02-02" xml:lang="it">lista delle voci di un apparato critico</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-07-15" xml:lang="en">contains a list of apparatus entries.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2012-07-14" xml:lang="fr">contient une liste d'entrées dans un apparat critique.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2021-02-02" xml:lang="it">contiene una lista delle voci di un apparato critico.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
  </classes>
```

^b7

### Block 8

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="app"/>
        <elementRef key="listApp"/>
      </alternate>
    </sequence>
  </content>
```

^b8

### Block 9

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="listApp-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listApp"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en" versionDate="2012-08-06">
    <p>In the following example from the exegetical Yasna, the base text is encoded in the <gi>body</gi> of 
    the document, and two separate <gi>listApp</gi> elements are used in the <gi>back</gi>, containing 
    variant readings written in different scripts.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listApp-egXML-te">
      <body>
        <div>
          <lg type="stanza" xml:id="Y-36.01" xml:lang="pal-Avst" rend="italic">
            <l xml:id="Y-36.01_L-1">
              <w xml:id="Y-36.01_L1_W-01">ahiiā</w>
              <w xml:id="Y-36.01_L1_W-02">ϑβā</w>
              <w xml:id="Y-36.01_L1_W-03">āϑrō</w>
              <w xml:id="Y-36.01_L1_W-04">vərəzə̄nā</w>
              <w xml:id="Y-36.01_L1_W-05">paouruiiē</w>
              <w xml:id="Y-36.01_L1_W-06">pairijasāmaiδē</w>
              <w xml:id="Y-36.01_L1_W-07">mazdā</w>
              <w xml:id="Y-36.01_L1_W-08">ahurā</w>
            </l>
            <!-- ... -->
          </lg>
        </div>
      </body>
      <!-- ... -->
      <back>
        <div>
          <listApp xml:id="CA_Y-36" xml:lang="pal-Avst">
            <head>Variants from witnesses in Avestan script</head>
            <app from="#Y-36.01_L1_W-01">
              <rdg wit="#Pt4 #F2 #J2 #M1">ahiiā</rdg>
            </app>
            <app from="#Y-36.01_L1_W-02">
              <rdg wit="#Pt4 #F2 #J2 #M1">ϑβā</rdg>
            </app>
            <app from="#Y-36.01_L1_W-03">
              <rdg wit="#Pt4 #J2 #M1">āϑrō</rdg>
              <rdg wit="#F2">āϑrōi</rdg>
            </app>
            <!-- ... -->
          </listApp>
          <listApp xml:id="CA_PY-36" xml:lang="pal-Phlv">
            <head>Variants from witnesses written in Pahlavi script</head>
            <app from="#PY-36.01_L1_W-01">
              <rdg wit="#Pt4 #F2 #J2 #M1">ʾytwnˈ</rdg>
            </app>
            <app from="#PY-36.01_L1_W-02">
              <rdg wit="#Pt4 #F2 #J2 #M1">ʾwˈ</rdg>
            </app>
            <app from="#PY-36.01_L1_W-03">
              <rdg wit="#Pt4 #F2 #J2 #M1">ḤNʾ</rdg>
            </app>
            <!-- ... -->
          </listApp>
        </div>
      </back>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listApp-remarks" versionDate="2012-08-06" xml:lang="en">
    <p><gi>listApp</gi> elements would normally be located in the <gi>back</gi> part of a document,
    but they may appear elsewhere.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLK"/>
  </listRef>
```

^b12

