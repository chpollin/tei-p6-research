---
type: representation
source-type: document
source: '[[00_sources/tei-p5-row-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 row
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/row.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# row

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2667. Git blob: `f4d2e2f6ccac286038ad347e955ef181d5ec66ac`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="figures" xml:id="gi-row" ident="row">
  <gloss versionDate="2007-06-12" xml:lang="en">row</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">rangée</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Tabellenzeile</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains one row of a table.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 테이블의 한 행을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含表格中的一列。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">表の1行を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une rangée d'un tableau.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una fila de la tabla.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una riga di una tabella.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält eine Zeile einer Tabelle.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.tableDecoration"/>
  </classes>
  <content>
    
      <!--      <rng:choice> -->
      <elementRef key="cell" minOccurs="1" maxOccurs="unbounded"/>
      <!--        <rng:ref name="table"/>-->
      <!--       </rng:choice>-->
      <!--    <rng:zeroOrMore>
        <rng:ref name="model.global"/>
      </rng:zeroOrMore>-->
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-row-egXML-ob">
      <row role="data">
        <cell role="label">Classics</cell>
        <cell>Idle listless and unimproving</cell>
      </row>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-row-egXML-uf">
      <row role="data">
        <cell role="label">Etudes classiques</cell>
        <cell>Inoccupé indolent et sans amélioration</cell>
      </row>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-row-egXML-iw">
      <row role="data">
        <cell role="label">古文</cell>
        <cell>漫無目的且無精進的</cell>
      </row>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FTTAB1" type="div1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">row</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">rangée</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Tabellenzeile</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains one row of a table.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 테이블의 한 행을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含表格中的一列。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">表の1行を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une rangée d'un tableau.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una fila de la tabla.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una riga di una tabella.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält eine Zeile einer Tabelle.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.tableDecoration"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <!--      <rng:choice> -->
      <elementRef key="cell" minOccurs="1" maxOccurs="unbounded"/>
      <!--        <rng:ref name="table"/>-->
      <!--       </rng:choice>-->
      <!--    <rng:zeroOrMore>
        <rng:ref name="model.global"/>
      </rng:zeroOrMore>-->
    
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-row-egXML-ob">
      <row role="data">
        <cell role="label">Classics</cell>
        <cell>Idle listless and unimproving</cell>
      </row>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-row-egXML-uf">
      <row role="data">
        <cell role="label">Etudes classiques</cell>
        <cell>Inoccupé indolent et sans amélioration</cell>
      </row>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-row-egXML-iw">
      <row role="data">
        <cell role="label">古文</cell>
        <cell>漫無目的且無精進的</cell>
      </row>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FTTAB1" type="div1"/>
  </listRef>
```

^b17

