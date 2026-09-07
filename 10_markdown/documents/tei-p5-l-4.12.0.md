---
type: representation
source-type: document
source: '[[00_sources/tei-p5-l-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 l
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/l.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# l

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3580. Git blob: `2ad5c6c17a5dc8be9ac1e1b3cb18ce903ddba736`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-l" ident="l">
  <gloss versionDate="2005-01-14" xml:lang="en">verse line</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">운문 시행</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">詩行</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">vers</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">verso</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">verso</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Vers(zeile)</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a single, possibly incomplete, line of verse.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">미완성일 수도 있지만 운문의 하나의 시행을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含詩文的一行，也許是不完整的詩行。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">韻文中の1行を示す。行として完全でない場合もある。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un seul vers, éventuellement incomplet.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un único verso, posiblemente incompleto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un singolo verso, anche incompleto.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält eine einzelne, möglicherweise unvollständige, Verszeile.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.enjamb"/>
    <memberOf key="att.fragmentable"/>
    <memberOf key="att.metrical"/>
    <memberOf key="model.lLike"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.inter"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
  <constraintSpec ident="abstractModel-structure-l-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:l">
        <sch:report test="ancestor::tei:l[not(.//tei:note//tei:l[. = current()])]">Abstract model violation: Metrical lines (&lt;l> elements) may not contain &lt;l> or &lt;lg> elements.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-l-egXML-lc" source="#l-td-eg-1">
      <l met="x/x/x/x/x/" real="/xx/x/x/x/">Shall I compare thee to a summer's day?</l>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-l-egXML-wx" xml:lang="fr">
      <l>Que toujours, dans vos vers, le sens coupant les mots</l>
      <l>Suspende l'hémistiche, en marque le repos.</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-l-egXML-lu" source="#UND">
      <l met="平平仄仄平" part="Y"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COVE"/>
    <ptr target="#CODV"/>
    <ptr target="#DRPAL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">verse line</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">운문 시행</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">詩行</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">vers</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">verso</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">verso</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Vers(zeile)</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a single, possibly incomplete, line of verse.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">미완성일 수도 있지만 운문의 하나의 시행을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含詩文的一行，也許是不完整的詩行。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">韻文中の1行を示す。行として完全でない場合もある。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient un seul vers, éventuellement incomplet.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un único verso, posiblemente incompleto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un singolo verso, anche incompleto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält eine einzelne, möglicherweise unvollständige, Verszeile.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.enjamb"/>
    <memberOf key="att.fragmentable"/>
    <memberOf key="att.metrical"/>
    <memberOf key="model.lLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.inter"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="abstractModel-structure-l-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:l">
        <sch:report test="ancestor::tei:l[not(.//tei:note//tei:l[. = current()])]">Abstract model violation: Metrical lines (&lt;l> elements) may not contain &lt;l> or &lt;lg> elements.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-l-egXML-lc" source="#l-td-eg-1">
      <l met="x/x/x/x/x/" real="/xx/x/x/x/">Shall I compare thee to a summer's day?</l>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-l-egXML-wx" xml:lang="fr">
      <l>Que toujours, dans vos vers, le sens coupant les mots</l>
      <l>Suspende l'hémistiche, en marque le repos.</l>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-l-egXML-lu" source="#UND">
      <l met="平平仄仄平" part="Y"/>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COVE"/>
    <ptr target="#CODV"/>
    <ptr target="#DRPAL"/>
  </listRef>
```

^b22

