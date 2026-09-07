---
type: representation
source-type: document
source: '[[00_sources/tei-p5-nationality-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 nationality
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/nationality.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# nationality

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3107. Git blob: `964baca2e2196c97d7e9092b605868f500b1184a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-nationality" ident="nationality">
  <gloss versionDate="2009-03-19" xml:lang="en">nationality</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">nationalité</gloss>
  <desc versionDate="2005-12-14" xml:lang="en">contains an informal description of a person's present or past nationality or citizenship.</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient une description non formalisée de la nationalité ou citoyenneté présente ou passée d'une personne.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 현재 또는 과거의 국적 또는 시민권에 대한 비공식적 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一非正式的敘述，表示個人現在或過去擁有的國籍或公民身分。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物の国籍や市民権の形式的でない解説を示す。</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal de la nacionalidad o ciudadanía presente o pasada de una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale della nazionalità o cittadinanza presente o passata di una persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
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
	<valItem ident="birth"/>
	<valItem ident="naturalised"/>
	<valItem ident="self-assigned"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nationality-egXML-zf">
      <nationality key="US" notBefore="1966"> Obtained US Citizenship in 1966</nationality>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nationality-egXML-io">
      <nationality key="US" notBefore="1966"> Citoyenneté américaine obtenue en 1966</nationality>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nationality-egXML-mf">
      <nationality key="US" notBefore="1966">1966年得到美國公民身份</nationality>
    </egXML>
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
<gloss versionDate="2009-03-19" xml:lang="en">nationality</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="fr">nationalité</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-12-14" xml:lang="en">contains an informal description of a person's present or past nationality or citizenship.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient une description non formalisée de la nationalité ou citoyenneté présente ou passée d'une personne.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 현재 또는 과거의 국적 또는 시민권에 대한 비공식적 기술을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一非正式的敘述，表示個人現在或過去擁有的國籍或公民身分。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物の国籍や市民権の形式的でない解説を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal de la nacionalidad o ciudadanía presente o pasada de una persona.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale della nazionalità o cittadinanza presente o passata di una persona.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
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
	<valItem ident="birth"/>
	<valItem ident="naturalised"/>
	<valItem ident="self-assigned"/>
      </valList>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nationality-egXML-zf">
      <nationality key="US" notBefore="1966"> Obtained US Citizenship in 1966</nationality>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nationality-egXML-io">
      <nationality key="US" notBefore="1966"> Citoyenneté américaine obtenue en 1966</nationality>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nationality-egXML-mf">
      <nationality key="US" notBefore="1966">1966年得到美國公民身份</nationality>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b17

