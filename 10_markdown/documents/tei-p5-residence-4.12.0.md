---
type: representation
source-type: document
source: '[[00_sources/tei-p5-residence-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 residence
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/residence.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# residence

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4433. Git blob: `2ffd2d4f2aefed65c5a1f250bef6f809d7969e14`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-residence" ident="residence">
  <gloss versionDate="2007-01-21" xml:lang="en">residence</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">거주</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">住所</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">résidence</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">residencia</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">residenza</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes a person's present or past places of residence.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 현재 또는 과거의 거주지를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述個人過去或現在的住所。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物の、現在または過去の住居を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">décrit les lieux de résidence présents ou passés d'une personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe el lugar de residencia presente o pasado de una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive il luogo di residenza presente o passato di una persona.</desc>
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
        <valItem ident="primary"/>
        <valItem ident="secondary"/>
        <valItem ident="temporary"/>
        <valItem ident="permanent"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-gd">
      <residence>Childhood in East Africa and long term resident of Glasgow, Scotland.</residence>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-uh">
      <residence>Enfance passée en Afrique orientale, résidant longtemps à Glasgow en
        Ecosse.</residence>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-nl">
      <residence notAfter="1997">Mbeni estate, Dzukumura region, Matabele land</residence>
      <residence notBefore="1903" notAfter="1996">
        <placeName>
          <settlement>Glasgow</settlement>
          <region>Ecosse</region>
        </placeName>
      </residence>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-ky">
      <residence>童年生活於中亞，長期居留在中國青島。</residence>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-iv">
      <residence notAfter="1997">台北東區帝寶大廈</residence>
      <residence notBefore="1903" notAfter="1996">
        <placeName>
          <settlement>沙鹿</settlement>
          <region>台中</region>
        </placeName>
      </residence>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-lx">
      <residence notAfter="1997">Mbeni estate, Dzukumura region, Matabele land</residence>
      <residence notBefore="1903" notAfter="1996">
        <placeName>
          <settlement>Glasgow</settlement>
          <region>Scotland</region>
        </placeName>
      </residence>
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
<gloss versionDate="2007-01-21" xml:lang="en">residence</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">거주</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">住所</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">résidence</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">residencia</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">residenza</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes a person's present or past places of residence.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 현재 또는 과거의 거주지를 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述個人過去或現在的住所。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物の、現在または過去の住居を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">décrit les lieux de résidence présents ou passés d'une personne.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe el lugar de residencia presente o pasado de una persona.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il luogo di residenza presente o passato di una persona.</desc>
```

^b13

### Block 14

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

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="primary"/>
        <valItem ident="secondary"/>
        <valItem ident="temporary"/>
        <valItem ident="permanent"/>
      </valList>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-gd">
      <residence>Childhood in East Africa and long term resident of Glasgow, Scotland.</residence>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-uh">
      <residence>Enfance passée en Afrique orientale, résidant longtemps à Glasgow en
        Ecosse.</residence>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-nl">
      <residence notAfter="1997">Mbeni estate, Dzukumura region, Matabele land</residence>
      <residence notBefore="1903" notAfter="1996">
        <placeName>
          <settlement>Glasgow</settlement>
          <region>Ecosse</region>
        </placeName>
      </residence>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-ky">
      <residence>童年生活於中亞，長期居留在中國青島。</residence>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-iv">
      <residence notAfter="1997">台北東區帝寶大廈</residence>
      <residence notBefore="1903" notAfter="1996">
        <placeName>
          <settlement>沙鹿</settlement>
          <region>台中</region>
        </placeName>
      </residence>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-residence-egXML-lx">
      <residence notAfter="1997">Mbeni estate, Dzukumura region, Matabele land</residence>
      <residence notBefore="1903" notAfter="1996">
        <placeName>
          <settlement>Glasgow</settlement>
          <region>Scotland</region>
        </placeName>
      </residence>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b24

