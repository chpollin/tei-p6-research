---
type: representation
source-type: document
source: '[[00_sources/tei-p5-floruit-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 floruit
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/floruit.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# floruit

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2294. Git blob: `5f67dc74aa60415c289671f3152e56caf7df363f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-floruit" ident="floruit">
  <gloss versionDate="2008-12-09" xml:lang="en">floruit</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">période d'activité</gloss>
  <desc versionDate="2006-06-21" xml:lang="en">contains information about a person's period of activity.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 활동 기간에 대한 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人活動時期的相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物が活躍した時期に関する情報を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient des informations sur la période d'activité d'une personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene información relativa al periodo de actividad de una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al periodod di attività di una persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floruit-egXML-yi" source="#UND">
      <floruit notBefore="1066" notAfter="1100"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floruit-egXML-jx">
      <person>
        <persName>François Villon</persName>
        <floruit notBefore="1457" notAfter="1463"/>
      </person>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">floruit</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">période d'activité</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-06-21" xml:lang="en">contains information about a person's period of activity.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 활동 기간에 대한 정보를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人活動時期的相關資訊。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物が活躍した時期に関する情報を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient des informations sur la période d'activité d'une personne.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene información relativa al periodo de actividad de una persona.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al periodod di attività di una persona.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.persStateLike"/>
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
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floruit-egXML-yi" source="#UND">
      <floruit notBefore="1066" notAfter="1100"/>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floruit-egXML-jx">
      <person>
        <persName>François Villon</persName>
        <floruit notBefore="1457" notAfter="1463"/>
      </person>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
```

^b14

