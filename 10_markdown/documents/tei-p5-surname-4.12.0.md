---
type: representation
source-type: document
source: '[[00_sources/tei-p5-surname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 surname
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/surname.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# surname

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2604. Git blob: `2cd01efcff747693dc26754c3f30a2a722461223`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-surname" ident="surname">
  <gloss versionDate="2009-03-19" xml:lang="en">surname</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">nom de famille</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a family (inherited) name, as opposed to a given, baptismal, or nick name.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient un nom de famille (hérité) par opposition à un nom donné, nom de baptême ou surnom.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">이름, 세례명, 또는 별명에 반대되는 것으로 (물려받은) 성을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個家族姓氏，並非名字、教名、或綽號。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">(継承される)苗字を示す。姓名中の名、洗礼名、愛称、別称とは異なる。</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el apellido o nombre de família (heredado), en oposicion a un nombre asignado, un nombre de
        bautismo o un sobranombre.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un nome di famiglia (ereditato) piuttosto che un nome assegnato, un nome di battesimo o un
        soprannome</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surname-egXML-hf">
      <surname type="combine">St John Stevas</surname>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surname-egXML-gd">
      <surname type="combine">Sidonie Gabrielle Colette</surname>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surname-egXML-ee">
      <surname type="combine">歐陽</surname>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPER"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="en">surname</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="fr">nom de famille</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a family (inherited) name, as opposed to a given, baptismal, or nick name.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient un nom de famille (hérité) par opposition à un nom donné, nom de baptême ou surnom.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이름, 세례명, 또는 별명에 반대되는 것으로 (물려받은) 성을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個家族姓氏，並非名字、教名、或綽號。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">(継承される)苗字を示す。姓名中の名、洗礼名、愛称、別称とは異なる。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el apellido o nombre de família (heredado), en oposicion a un nombre asignado, un nombre de
        bautismo o un sobranombre.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un nome di famiglia (ereditato) piuttosto che un nome assegnato, un nome di battesimo o un
        soprannome</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surname-egXML-hf">
      <surname type="combine">St John Stevas</surname>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surname-egXML-gd">
      <surname type="combine">Sidonie Gabrielle Colette</surname>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surname-egXML-ee">
      <surname type="combine">歐陽</surname>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPER"/>
  </listRef>
```

^b15

