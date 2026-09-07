---
type: representation
source-type: document
source: '[[00_sources/tei-p5-activity-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 activity
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/activity.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# activity

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3770. Git blob: `93bae00a04686c7515d0baa1051b2a6978130641`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="corpus" xml:id="gi-activity" ident="activity">
  <gloss xml:lang="en" versionDate="2009-04-17">activity</gloss>
  <gloss xml:lang="es" versionDate="2022-06-16">actividad</gloss>
  <gloss xml:lang="fr" versionDate="2009-04-17">activité</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Aktivität</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a brief informal description of what a participant in a
language interaction is doing other than speaking, if anything.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">언어 상호작용 참여자의 발화 외의 다른 행위에 대한 간단한 일상적 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含簡短非正式的文字，描述一個對話參與者除了說話以外其他可能的動作。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">言語交流の参加者が行った発話以外の活動を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une description brève et informelle de ce
      que fait, le cas échéant, un participant à une interaction linguistique, en dehors de parler.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una breve descripción informal, si cabe, sobre qué está haciendo, además de hablar, un participante en una interacción lingüística.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una breve descrizione informale di ciò che sta facendo un partecipante ad una interazione linguistica di diverso dal parlare.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.settingPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-activity-egXML-uf" source="#NONE">
      <activity>driving</activity>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-activity-egXML-zw" source="#NONE">
      <activity>Conduite</activity>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-activity-egXML-es" source="#NONE">
      <activity>駕駛</activity>
    </egXML>
  </exemplum>
  <remarks ident="activity-remarks" versionDate="2005-01-14" xml:lang="en" source="#UND">
    <p>For more fine-grained description of participant
activities during a spoken text, the <gi>event</gi> element should
be used.</p>
  </remarks>
  <remarks ident="activity-remarks" versionDate="2022-06-16" xml:lang="es"><p>Para una descripción más detallada de las acciones de los participantes durante los parlamentos, debe utilizarse el elemento  <gi>event</gi></p></remarks>
  <remarks ident="activity-remarks" versionDate="2007-06-12" xml:lang="fr" source="#UND">
    <p>Pour une description plus fine de toute activité survenant lors d'une communication
                orale transcrite, utilisez l'élément <gi>event</gi>. </p>
  </remarks>
  <remarks ident="activity-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    参加者の行動についてより詳細に記述する場合には、要素<gi>event</gi>
    を使用すべきである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#CCAHSE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss xml:lang="en" versionDate="2009-04-17">activity</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss xml:lang="es" versionDate="2022-06-16">actividad</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss xml:lang="fr" versionDate="2009-04-17">activité</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Aktivität</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a brief informal description of what a participant in a
language interaction is doing other than speaking, if anything.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">언어 상호작용 참여자의 발화 외의 다른 행위에 대한 간단한 일상적 기술을 포함한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含簡短非正式的文字，描述一個對話參與者除了說話以外其他可能的動作。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">言語交流の参加者が行った発話以外の活動を示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une description brève et informelle de ce
      que fait, le cas échéant, un participant à une interaction linguistique, en dehors de parler.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una breve descripción informal, si cabe, sobre qué está haciendo, además de hablar, un participante en una interacción lingüística.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una breve descrizione informale di ciò che sta facendo un partecipante ad una interazione linguistica di diverso dal parlare.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.settingPart"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-activity-egXML-uf" source="#NONE">
      <activity>driving</activity>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-activity-egXML-zw" source="#NONE">
      <activity>Conduite</activity>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-activity-egXML-es" source="#NONE">
      <activity>駕駛</activity>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="activity-remarks" versionDate="2005-01-14" xml:lang="en" source="#UND">
    <p>For more fine-grained description of participant
activities during a spoken text, the <gi>event</gi> element should
be used.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="activity-remarks" versionDate="2022-06-16" xml:lang="es"><p>Para una descripción más detallada de las acciones de los participantes durante los parlamentos, debe utilizarse el elemento  <gi>event</gi></p></remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="activity-remarks" versionDate="2007-06-12" xml:lang="fr" source="#UND">
    <p>Pour une description plus fine de toute activité survenant lors d'une communication
                orale transcrite, utilisez l'élément <gi>event</gi>. </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="activity-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    参加者の行動についてより詳細に記述する場合には、要素<gi>event</gi>
    を使用すべきである。
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHSE"/>
  </listRef>
```

^b21

