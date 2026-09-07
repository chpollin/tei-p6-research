---
type: representation
source-type: document
source: '[[00_sources/tei-p5-death-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 death
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/death.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# death

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4227. Git blob: `313d6490732e257874ab56838a22909b5df39268`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-death" ident="death">
  <gloss versionDate="2008-12-09" xml:lang="en">death</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">décès</gloss>
  <desc versionDate="2005-12-13" xml:lang="en">contains information about a person's death, such as its date and place.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">날짜, 장소와 같이 개인의 죽음과 관련된 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的死亡資訊，例如日期及地點等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物の死亡に関する情報を示す。例えば、日付や場所など。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient des informations sur le décès d'une personne, comme la date et le lieu.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas a la defunción de una persona, del tipo lugar y fecha.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al luogo e alla data di morte di una persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.locatable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.personPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
	<valItem ident="proclaimed"/>
	<valItem ident="assumed"/>
	<valItem ident="verified"/>
	<valItem ident="clinical"/>
	<valItem ident="brain"/>
	<valItem ident="natural"/>
	<valItem ident="unnatural"/>
	<valItem ident="fragmentation"/>
	<valItem ident="dissolution"/>
      </valList>
      <remarks ident="death-attr.type-remarks" versionDate="2017-06-23" xml:lang="en">
	<p>This attribute is not intended to express the cause of death.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-ez" source="#UND">
      <death when="1902-10-01"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-kb" source="#UND">
      <death when="1902-10-01"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-cg" source="#fr-ex-Ernaux-perdre">
      <death when="1953-04-07">Ma mère est morte le 7 avril.</death>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-pj">
      <death when="1960-12-10">在<name type="place">北大教堂</name>附近死於腦性麻痺</death>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-cj">
      <death when="1960-12-10">Passed away near <name type="place">Aix-la-Chapelle</name>, after suffering from cerebral palsy. </death>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-wh">
      <death when="2024-08-16" where="gn:US-NM-039-5467024"/>
    </egXML>
    <p>In this example, the value of <att>where</att> demonstrates the use of private URI scheme and custom prefix (<val>gn:</val>), which would typically be defined by a <gi>prefixDef</gi> in the document's <gi>teiHeader</gi>.</p>
  </exemplum>
  <listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">death</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">décès</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-12-13" xml:lang="en">contains information about a person's death, such as its date and place.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">날짜, 장소와 같이 개인의 죽음과 관련된 정보를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的死亡資訊，例如日期及地點等。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物の死亡に関する情報を示す。例えば、日付や場所など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient des informations sur le décès d'une personne, comme la date et le lieu.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas a la defunción de una persona, del tipo lugar y fecha.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al luogo e alla data di morte di una persona.</desc>
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
    <memberOf key="att.locatable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.personPart"/>
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

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
	<valItem ident="proclaimed"/>
	<valItem ident="assumed"/>
	<valItem ident="verified"/>
	<valItem ident="clinical"/>
	<valItem ident="brain"/>
	<valItem ident="natural"/>
	<valItem ident="unnatural"/>
	<valItem ident="fragmentation"/>
	<valItem ident="dissolution"/>
      </valList>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="death-attr.type-remarks" versionDate="2017-06-23" xml:lang="en">
	<p>This attribute is not intended to express the cause of death.</p>
      </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-ez" source="#UND">
      <death when="1902-10-01"/>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-kb" source="#UND">
      <death when="1902-10-01"/>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-cg" source="#fr-ex-Ernaux-perdre">
      <death when="1953-04-07">Ma mère est morte le 7 avril.</death>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-pj">
      <death when="1960-12-10">在<name type="place">北大教堂</name>附近死於腦性麻痺</death>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-cj">
      <death when="1960-12-10">Passed away near <name type="place">Aix-la-Chapelle</name>, after suffering from cerebral palsy. </death>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-death-egXML-wh">
      <death when="2024-08-16" where="gn:US-NM-039-5467024"/>
    </egXML>
    <p>In this example, the value of <att>where</att> demonstrates the use of private URI scheme and custom prefix (<val>gn:</val>), which would typically be defined by a <gi>prefixDef</gi> in the document's <gi>teiHeader</gi>.</p>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b21

