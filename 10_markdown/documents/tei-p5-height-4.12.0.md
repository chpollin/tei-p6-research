---
type: representation
source-type: document
source: '[[00_sources/tei-p5-height-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 height
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/height.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# height

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2133. Git blob: `3f5c9588492b38ea3577e77e41f295aab6cc3f1f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="HEIGHT" ident="height">
  <gloss versionDate="2007-06-12" xml:lang="en">height</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">hauteur</gloss>
  <desc versionDate="2019-05-08" xml:lang="en" xml:id="height.desc">contains a measurement measured along the axis at a right angle to the bottom of the object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">책의 높이 치수를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">沿著與書脊平行的軸線所量出的測量值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">背に沿って計測された大きさを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une dimension prise sur l'axe parallèle au
      dos du manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">refiere la medida tomada del largo del eje paralelo del dorso.***</desc>
  <desc versionDate="2007-01-21" xml:lang="it">si riferisce a una misurazione presa lungo l'asse parallelo al dorso.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="model.dimLike"/>
    <memberOf key="model.measureLike"/>
  </classes>
  <content>
    <macroRef key="macro.xtext"/>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HEIGHT-egXML-uu" source="#UND">
      <height unit="in" quantity="7"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HEIGHT-egXML-bk" source="#UND">
      <height unit="in" quantity="7"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msdim"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">height</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">hauteur</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-05-08" xml:lang="en" xml:id="height.desc">contains a measurement measured along the axis at a right angle to the bottom of the object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">책의 높이 치수를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">沿著與書脊平行的軸線所量出的測量值。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">背に沿って計測された大きさを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une dimension prise sur l'axe parallèle au
      dos du manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">refiere la medida tomada del largo del eje paralelo del dorso.***</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">si riferisce a una misurazione presa lungo l'asse parallelo al dorso.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="model.dimLike"/>
    <memberOf key="model.measureLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.xtext"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HEIGHT-egXML-uu" source="#UND">
      <height unit="in" quantity="7"/>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HEIGHT-egXML-bk" source="#UND">
      <height unit="in" quantity="7"/>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msdim"/>
  </listRef>
```

^b14

