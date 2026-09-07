---
type: representation
source-type: document
source: '[[00_sources/tei-p5-actor-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 actor
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/actor.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# actor

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4948. Git blob: `8d28cbc2e3a0723ff7ccd26129f40eec7a968491`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-actor" ident="actor">
  <desc versionDate="2012-12-27" xml:lang="en">contains the name of an actor appearing within a cast list.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">배역 목록에 나타나는 배우의 이름</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">角色名單中的演員姓名。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">Nombre de un actor que aparece dentro de la lista del reparto.</desc>
  <desc versionDate="2018-12-18" xml:lang="ja">登場人物リスト中の役者名を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">nom d'un acteur apparaissant dans une distribution.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">nome di un attore che appare nella lista dei personaggi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.castItemPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="sex" usage="opt">
      <desc versionDate="2023-03-11" xml:lang="en">specifies the sex of the actor.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.sex"/></datatype>
      <remarks ident="actor-attr.sex-remarks" versionDate="2023-03-11" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or may refer to an external standard.</p>
      </remarks>
    </attDef>
    <attDef ident="gender" usage="opt">
      <desc versionDate="2023-03-11" xml:lang="en">specifies the gender of the actor.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
      <remarks ident="actor-attr.gender-remarks" versionDate="2023-03-11" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-actor-egXML-ay" source="#DRCAST-eg-21">
      <castItem>
        <role>Mathias</role>
        <roleDesc>the Burgomaster</roleDesc>
        <actor ref="https://en.wikipedia.org/wiki/Henry_Irving">Mr. Henry Irving</actor>
      </castItem>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-actor-egXML-ig" source="#UND">
      <castItem>
	<role>Mrs Saunders</role>
	<roleDesc>la logeuse</roleDesc>
	<actor>Sylvia Marriott</actor>
      </castItem>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-actor-egXML-kj" source="#biblzh-tw_n29">
      <castItem>
        <role>梁山伯</role>
        <roleDesc>窮書生</roleDesc>
        <actor>凌波</actor>
      </castItem>
    </egXML>
  </exemplum>
  <remarks ident="actor-remarks" versionDate="2006-06-11" xml:lang="en">
    <p>This element should be used only to mark the name of the actor as
    given in the source. Chapter <ptr target="#ND"/> discusses ways of
    marking the components of names, and also of associating names with
    biographical information about a person. </p>
  </remarks>
  <remarks ident="actor-remarks" versionDate="2018-09-08" xml:lang="es"><p>Este elemento debe ser usado solo para marcar el nombre del actor tal como aparece en la fuente. El capítulo <ptr target="#ND"/> comenta/discute formas de marcar los componentes de los nombres,  asi como también asociar nombre con información biográfica sobre una persona</p></remarks>
  <remarks ident="actor-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément ne devrait être utilisé que pour encoder le nom de l'acteur tel qu'il est donné
                dans la source. Le chapitre <ptr target="#ND"/>
                traite des différentes manières d'encoder les composants des noms, et aussi celui d'associer des
                noms à des informations biographiques concernant une personne.</p>
  </remarks>
  <remarks ident="actor-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、元資料にある役者名を示すために使用されるべきである。
    <ptr target="#ND"/>では、名前の構成要素や、当該人物に関する情報に
    関連する名前をタグ付けする方法が解説されている。
 </p>
  </remarks>
  <listRef>
    <ptr target="#DRCAST" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains the name of an actor appearing within a cast list.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">배역 목록에 나타나는 배우의 이름</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">角色名單中的演員姓名。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">Nombre de un actor que aparece dentro de la lista del reparto.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2018-12-18" xml:lang="ja">登場人物リスト中の役者名を示す。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">nom d'un acteur apparaissant dans une distribution.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">nome di un attore che appare nella lista dei personaggi.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.castItemPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2023-03-11" xml:lang="en">specifies the sex of the actor.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.sex"/></datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="actor-attr.sex-remarks" versionDate="2023-03-11" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or may refer to an external standard.</p>
      </remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2023-03-11" xml:lang="en">specifies the gender of the actor.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="actor-attr.gender-remarks" versionDate="2023-03-11" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-actor-egXML-ay" source="#DRCAST-eg-21">
      <castItem>
        <role>Mathias</role>
        <roleDesc>the Burgomaster</roleDesc>
        <actor ref="https://en.wikipedia.org/wiki/Henry_Irving">Mr. Henry Irving</actor>
      </castItem>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-actor-egXML-ig" source="#UND">
      <castItem>
	<role>Mrs Saunders</role>
	<roleDesc>la logeuse</roleDesc>
	<actor>Sylvia Marriott</actor>
      </castItem>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-actor-egXML-kj" source="#biblzh-tw_n29">
      <castItem>
        <role>梁山伯</role>
        <roleDesc>窮書生</roleDesc>
        <actor>凌波</actor>
      </castItem>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="actor-remarks" versionDate="2006-06-11" xml:lang="en">
    <p>This element should be used only to mark the name of the actor as
    given in the source. Chapter <ptr target="#ND"/> discusses ways of
    marking the components of names, and also of associating names with
    biographical information about a person. </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="actor-remarks" versionDate="2018-09-08" xml:lang="es"><p>Este elemento debe ser usado solo para marcar el nombre del actor tal como aparece en la fuente. El capítulo <ptr target="#ND"/> comenta/discute formas de marcar los componentes de los nombres,  asi como también asociar nombre con información biográfica sobre una persona</p></remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="actor-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément ne devrait être utilisé que pour encoder le nom de l'acteur tel qu'il est donné
                dans la source. Le chapitre <ptr target="#ND"/>
                traite des différentes manières d'encoder les composants des noms, et aussi celui d'associer des
                noms à des informations biographiques concernant une personne.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="actor-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、元資料にある役者名を示すために使用されるべきである。
    <ptr target="#ND"/>では、名前の構成要素や、当該人物に関する情報に
    関連する名前をタグ付けする方法が解説されている。
 </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRCAST" type="div3"/>
  </listRef>
```

^b23

