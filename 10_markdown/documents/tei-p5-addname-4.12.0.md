---
type: representation
source-type: document
source: '[[00_sources/tei-p5-addname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 addName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/addName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# addName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3689. Git blob: `f8096828eeff42e2a68fe24b77e2388aa92dc1a0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-addName" ident="addName">
  <gloss versionDate="2005-01-14" xml:lang="en">additional name</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">부가명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">附加名稱</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">nom additionnel</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nombre adicional</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nome aggiuntivo</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">追加的名称</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an additional name component, such as a nickname, epithet, or alias, or any other descriptive phrase used within a personal
    name.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">별명, 통명, 가명, 또는 개인 이름 내에서 사용되는 다른 기술적 구와 같이 부가적 이름 성분을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">附加的名稱，例如綽號、稱號、或別名，或是在人名中出現的其他描述性措辭。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">付加的な名前要素を示す。例えば、愛称、渾名、別名などの個人名。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient une composante de nom additionnelle, comme un surnom, une épithète, un alias ou toute autre
    expression descriptive utilisée dans un nom de personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un componente añadido al nombre, como un sobrenombre, un epíteto, alias u otras eventuales
    expresiones utilizadas al interno de un nombre propio de persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una componente aggiuntiva del nome, come un soprannome, un epiteto, o eventuali altre
    espressioni utilizzate all'interno di un nome proprio di persona</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addName-egXML-zm" source="#NONE">
      <persName>
        <forename>Frederick</forename>
        <addName type="epithet">the Great</addName>
        <roleName>Emperor of Prussia</roleName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addName-egXML-dt" source="#NONE">
      <persName><forename>Catherine</forename><genName>II</genName>, <addName type="epithet"> la
          Grande</addName>, <roleName>impératrice de Russie</roleName></persName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW" source="#NONE">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addName-egXML-di" source="#NONE">
      <persName>
        <forename>政</forename>
        <surname>嬴</surname>
        <addName type="epithet">趙政</addName>
        <roleName>秦始皇</roleName>
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
<gloss versionDate="2005-01-14" xml:lang="en">additional name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">부가명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">附加名稱</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">nom additionnel</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nombre adicional</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nome aggiuntivo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">追加的名称</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an additional name component, such as a nickname, epithet, or alias, or any other descriptive phrase used within a personal
    name.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">별명, 통명, 가명, 또는 개인 이름 내에서 사용되는 다른 기술적 구와 같이 부가적 이름 성분을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">附加的名稱，例如綽號、稱號、或別名，或是在人名中出現的其他描述性措辭。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">付加的な名前要素を示す。例えば、愛称、渾名、別名などの個人名。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient une composante de nom additionnelle, comme un surnom, une épithète, un alias ou toute autre
    expression descriptive utilisée dans un nom de personne.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un componente añadido al nombre, como un sobrenombre, un epíteto, alias u otras eventuales
    expresiones utilizadas al interno de un nombre propio de persona.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una componente aggiuntiva del nome, come un soprannome, un epiteto, o eventuali altre
    espressioni utilizzate all'interno di un nome proprio di persona</desc>
```

^b14

### Block 15

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

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addName-egXML-zm" source="#NONE">
      <persName>
        <forename>Frederick</forename>
        <addName type="epithet">the Great</addName>
        <roleName>Emperor of Prussia</roleName>
      </persName>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addName-egXML-dt" source="#NONE">
      <persName><forename>Catherine</forename><genName>II</genName>, <addName type="epithet"> la
          Grande</addName>, <roleName>impératrice de Russie</roleName></persName>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW" source="#NONE">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addName-egXML-di" source="#NONE">
      <persName>
        <forename>政</forename>
        <surname>嬴</surname>
        <addName type="epithet">趙政</addName>
        <roleName>秦始皇</roleName>
      </persName>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPER"/>
  </listRef>
```

^b20

