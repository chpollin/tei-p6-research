---
type: representation
source-type: document
source: '[[00_sources/tei-p5-meeting-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 meeting
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/meeting.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# meeting

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4088. Git blob: `5d2fe3c09783fe070bff65207e3a697fc1a06e28`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-meeting" ident="meeting">
  <desc versionDate="2007-10-15" xml:lang="en">contains the formalized descriptive title for a meeting or conference, for use in a bibliographic description for an item derived from such a meeting, or as a heading or preamble to publications emanating from it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">회의에서 배포된 항목 또는 회의에서 산출된 출판물의 표제 및 서문에 대한 서지적 설명으로 사용된 경우 회의 또는 학술회의의 공식적 설명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在書目參照當中，標記該書目項目來源的會議相關描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">会議中の項目を書誌情報で記述する際や、発行物の見出しや序文に現れる、 会合や会議を表す、形式化された記述的タイトルを示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient le titre descriptif formalisé d’une réunion ou d’une conférence, employé dans une description bibliographique pour un article provenant d'une telle réunion, ou comme le titre ou le préambule aux publications qui en émanent.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">en referencias bibliográficas, contiene una descripción del encuentro o conferencia del que deriva el elemento bibliográfico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">nei riferimenti biliografici, contiene una descrizione di un incontro o convegno dal quale deriva l'unità bibliografica.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.respLike"/>
  </classes>
  <content>
    <macroRef key="macro.limitedContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-meeting-egXML-pj">
      <div>
        <meeting>Ninth International Conference on Middle High German Textual Criticism, Aachen,
          June 1998.</meeting>
        <list type="attendance">
          <head>List of Participants</head>
          <item>
            <persName>...</persName>
          </item>
          <item>
            <persName>...</persName>
          </item>
          <!--...-->
        </list>
        <p>...</p>
      </div>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-meeting-egXML-ai">
      <div>
        <meeting>Colloque international : Duras, marges et transgressions, Nancy, 1er et 2 avril
            2005</meeting>
        <list type="attendance">
          <head>liste des participants</head>
          <item>
            <persName>...</persName>
          </item>
          <item>
            <persName>...</persName>
          </item>
        </list>
        <p>...</p>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-meeting-egXML-lz">
      <div>
        <meeting>2007第三屆亞太藝術教育國際研討會</meeting>
        <list type="參與者">
          <head>與會者名單</head>
          <item>
            <persName>馬桂順 </persName>
          </item>
          <item>
            <persName>仲瀨律久</persName>
          </item>
          <!--...-->
        </list>
        <p>...</p>
      </div>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COBICOR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-15" xml:lang="en">contains the formalized descriptive title for a meeting or conference, for use in a bibliographic description for an item derived from such a meeting, or as a heading or preamble to publications emanating from it.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">회의에서 배포된 항목 또는 회의에서 산출된 출판물의 표제 및 서문에 대한 서지적 설명으로 사용된 경우 회의 또는 학술회의의 공식적 설명을 포함한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在書目參照當中，標記該書目項目來源的會議相關描述。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">会議中の項目を書誌情報で記述する際や、発行物の見出しや序文に現れる、 会合や会議を表す、形式化された記述的タイトルを示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient le titre descriptif formalisé d’une réunion ou d’une conférence, employé dans une description bibliographique pour un article provenant d'une telle réunion, ou comme le titre ou le préambule aux publications qui en émanent.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">en referencias bibliográficas, contiene una descripción del encuentro o conferencia del que deriva el elemento bibliográfico.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">nei riferimenti biliografici, contiene una descrizione di un incontro o convegno dal quale deriva l'unità bibliografica.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.respLike"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.limitedContent"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-meeting-egXML-pj">
      <div>
        <meeting>Ninth International Conference on Middle High German Textual Criticism, Aachen,
          June 1998.</meeting>
        <list type="attendance">
          <head>List of Participants</head>
          <item>
            <persName>...</persName>
          </item>
          <item>
            <persName>...</persName>
          </item>
          <!--...-->
        </list>
        <p>...</p>
      </div>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-meeting-egXML-ai">
      <div>
        <meeting>Colloque international : Duras, marges et transgressions, Nancy, 1er et 2 avril
            2005</meeting>
        <list type="attendance">
          <head>liste des participants</head>
          <item>
            <persName>...</persName>
          </item>
          <item>
            <persName>...</persName>
          </item>
        </list>
        <p>...</p>
      </div>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-meeting-egXML-lz">
      <div>
        <meeting>2007第三屆亞太藝術教育國際研討會</meeting>
        <list type="參與者">
          <head>與會者名單</head>
          <item>
            <persName>馬桂順 </persName>
          </item>
          <item>
            <persName>仲瀨律久</persName>
          </item>
          <!--...-->
        </list>
        <p>...</p>
      </div>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOR"/>
  </listRef>
```

^b13

