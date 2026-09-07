---
type: representation
source-type: document
source: '[[00_sources/tei-p5-castitem-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 castItem
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/castItem.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# castItem

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6539. Git blob: `d7170b06493870ea8f34f31eea6b07e14fdcc07f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-castItem" ident="castItem">
  <gloss versionDate="2007-07-04" xml:lang="en">cast list item</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">배역 목록 항목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">角色項目</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">elemento del reparto</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">personnage</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">oggetto della lista dei personaggi</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">配役リスト項目</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a single entry within a cast list, describing
either a single role or a list of non-speaking roles.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">배역 목록에서 하나의 배역, 또는 대사가 없는 배역 목록을 기술하는 하나의 항목을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含角色清單中的一個項目，描述單一角色或無台詞角色的列表。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una sola entrada dentro de la lista del reparto, describiendo un solo papel o una lista de papeles sin diálogo.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">配役リスト中の一項目で、ひとつの役、または台詞のない役のリストを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">dans une liste de personnages, entrée décrivant un
      rôle en particulier ou une liste de rôles muets.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una singola voce all'interno della lista dei personaggi, descrive o un ruolo o una lista di ruoli privi di battute.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
 
  </classes>
  <content>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.castItemPart"/>
        <classRef key="model.phrase"/>
        <classRef key="model.global"/>
      </alternate>  
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">characterizes the cast item.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">배역 항목의 특성 기술</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明角色項目的特性。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">caracteriza el elemento del reparto.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該項目の種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">caractérise le personnage.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la voce della lista dei personaggi.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>role</defaultVal>
      <valList type="closed">
        <valItem ident="role">
          <desc versionDate="2007-06-27" xml:lang="en">the item describes a single role.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">항목이 하나의 배역을 기술한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該項目為單一角色</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el elemeto describe un único papel.</desc>
          <desc versionDate="2023-10-02" xml:lang="ja">ひとつの役を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">l'item décrit un simple rôle.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'oggetto descrive un solo ruolo.</desc>
        </valItem>
        <valItem ident="list">
          <desc versionDate="2007-06-27" xml:lang="en">the item describes a list of non-speaking roles.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">항목이 대사 없는 배역 목록을 기술한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該項目為無台詞角色的列表</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el item describe una lista de papeles sin diálogo.</desc>
          <desc versionDate="2023-10-02" xml:lang="ja">台詞がない役のリストを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">l'item décrit une liste de rôles muets</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'oggetto descrive una lista di ruoli privi di battute.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-mt">
      <castItem>
        <role>Player</role>
        <actor>Mr Milward</actor>
      </castItem>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-km" source="#fr-ex-Guerre-Troie">
      <castItem>
        <role>Un marin</role>
        <actor>Henry Courseaux</actor>
      </castItem>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-va">
      <castItem type="list">Agent de police, dessinateur, serrurier, etc.</castItem>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-bh">
      <castItem>
        <role>段小樓</role>
        <actor>張豐毅</actor>
      </castItem>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-xf" source="#biblzh-tw_n30-31">
      <castItem type="list">張國榮、張豐毅、鞏俐…等等</castItem>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-rb">
      <castItem type="list">Constables, Drawer, Turnkey, etc.</castItem>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DRCAST" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">cast list item</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">배역 목록 항목</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">角色項目</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">elemento del reparto</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">personnage</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">oggetto della lista dei personaggi</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">配役リスト項目</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a single entry within a cast list, describing
either a single role or a list of non-speaking roles.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">배역 목록에서 하나의 배역, 또는 대사가 없는 배역 목록을 기술하는 하나의 항목을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含角色清單中的一個項目，描述單一角色或無台詞角色的列表。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una sola entrada dentro de la lista del reparto, describiendo un solo papel o una lista de papeles sin diálogo.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">配役リスト中の一項目で、ひとつの役、または台詞のない役のリストを示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">dans une liste de personnages, entrée décrivant un
      rôle en particulier ou une liste de rôles muets.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una singola voce all'interno della lista dei personaggi, descrive o un ruolo o una lista di ruoli privi di battute.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
 
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.castItemPart"/>
        <classRef key="model.phrase"/>
        <classRef key="model.global"/>
      </alternate>  
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">characterizes the cast item.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">배역 항목의 특성 기술</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明角色項目的特性。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">caracteriza el elemento del reparto.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該項目の種類を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">caractérise le personnage.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la voce della lista dei personaggi.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>role</defaultVal>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="role">
          <desc versionDate="2007-06-27" xml:lang="en">the item describes a single role.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">항목이 하나의 배역을 기술한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該項目為單一角色</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el elemeto describe un único papel.</desc>
          <desc versionDate="2023-10-02" xml:lang="ja">ひとつの役を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">l'item décrit un simple rôle.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'oggetto descrive un solo ruolo.</desc>
        </valItem>
        <valItem ident="list">
          <desc versionDate="2007-06-27" xml:lang="en">the item describes a list of non-speaking roles.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">항목이 대사 없는 배역 목록을 기술한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該項目為無台詞角色的列表</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el item describe una lista de papeles sin diálogo.</desc>
          <desc versionDate="2023-10-02" xml:lang="ja">台詞がない役のリストを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">l'item décrit une liste de rôles muets</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'oggetto descrive una lista di ruoli privi di battute.</desc>
        </valItem>
      </valList>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-mt">
      <castItem>
        <role>Player</role>
        <actor>Mr Milward</actor>
      </castItem>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-km" source="#fr-ex-Guerre-Troie">
      <castItem>
        <role>Un marin</role>
        <actor>Henry Courseaux</actor>
      </castItem>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-va">
      <castItem type="list">Agent de police, dessinateur, serrurier, etc.</castItem>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-bh">
      <castItem>
        <role>段小樓</role>
        <actor>張豐毅</actor>
      </castItem>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-xf" source="#biblzh-tw_n30-31">
      <castItem type="list">張國榮、張豐毅、鞏俐…等等</castItem>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castItem-egXML-rb">
      <castItem type="list">Constables, Drawer, Turnkey, etc.</castItem>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRCAST" type="div3"/>
  </listRef>
```

^b33

