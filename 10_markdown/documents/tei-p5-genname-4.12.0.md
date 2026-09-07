---
type: representation
source-type: document
source: '[[00_sources/tei-p5-genname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 genName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/genName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# genName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4236. Git blob: `294c6ddf72dbb681352815b9e491f823c8445dac`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-genName" ident="genName">
  <gloss versionDate="2007-07-04" xml:lang="en">generational name component</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">세대명 성분</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">componente de nombre generacional</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">qualificatif générationnel de nom</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">componente generazionale del nome</gloss>
  <desc versionDate="2006-01-08" xml:lang="en">contains a name component used to distinguish otherwise similar names on the basis of the relative ages or generations of the persons
        named.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 상대적 나이 또는 세대에 기반하여 유사 이름을 다른 방식으로 구분하는 이름 성분을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">該名稱用來和其他相似名稱做區別，以個人的相對年紀或隸屬世代作依據。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">似た名前を区別する為に、相対的な年齢関係、世代関係などの情報を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient une composante de nom utilisée pour distinguer des noms, par ailleurs similaires, sur la base de
        l'âge ou de la génération des personnes concernées.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un componente del nombre utilizado para distinguir nombre similares entre ellos atendiendo a la
        diferencia de edad o de pertenencia a generaciones distintas que se establece entre las personas nombradas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una componente del nome utilizzata per distinguere nomi simili tra loro sulla base della
        differenza di età o dell'appartenenza a generazioni diverse delle persone nominate</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-gx">
      <persName>
        <forename>Charles</forename>
        <genName>II</genName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-kr">
      <persName>
        <forename>Louis</forename>
        <genName>XIV</genName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-ae">
      <persName>
        <surname>Louis X</surname>
        <genName type="epithet">Le Hutin</genName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-mo">
      <persName>
        <forename>查爾斯</forename>
        <genName>二世</genName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-nk">
      <persName>
        <surname>彼特</surname>
        <genName>小的</genName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-pg">
      <persName>
        <surname>Pitt</surname>
        <genName>the Younger</genName>
      </persName>
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
<gloss versionDate="2007-07-04" xml:lang="en">generational name component</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">세대명 성분</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">componente de nombre generacional</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">qualificatif générationnel de nom</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">componente generazionale del nome</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-08" xml:lang="en">contains a name component used to distinguish otherwise similar names on the basis of the relative ages or generations of the persons
        named.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 상대적 나이 또는 세대에 기반하여 유사 이름을 다른 방식으로 구분하는 이름 성분을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">該名稱用來和其他相似名稱做區別，以個人的相對年紀或隸屬世代作依據。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">似た名前を区別する為に、相対的な年齢関係、世代関係などの情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient une composante de nom utilisée pour distinguer des noms, par ailleurs similaires, sur la base de
        l'âge ou de la génération des personnes concernées.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un componente del nombre utilizado para distinguir nombre similares entre ellos atendiendo a la
        diferencia de edad o de pertenencia a generaciones distintas que se establece entre las personas nombradas.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una componente del nome utilizzata per distinguere nomi simili tra loro sulla base della
        differenza di età o dell'appartenenza a generazioni diverse delle persone nominate</desc>
```

^b13

### Block 14

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

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-gx">
      <persName>
        <forename>Charles</forename>
        <genName>II</genName>
      </persName>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-kr">
      <persName>
        <forename>Louis</forename>
        <genName>XIV</genName>
      </persName>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-ae">
      <persName>
        <surname>Louis X</surname>
        <genName type="epithet">Le Hutin</genName>
      </persName>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-mo">
      <persName>
        <forename>查爾斯</forename>
        <genName>二世</genName>
      </persName>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-nk">
      <persName>
        <surname>彼特</surname>
        <genName>小的</genName>
      </persName>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-genName-egXML-pg">
      <persName>
        <surname>Pitt</surname>
        <genName>the Younger</genName>
      </persName>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPER"/>
  </listRef>
```

^b22

