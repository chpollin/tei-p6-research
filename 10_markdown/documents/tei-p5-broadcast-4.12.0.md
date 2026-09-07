---
type: representation
source-type: document
source: '[[00_sources/tei-p5-broadcast-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 broadcast
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/broadcast.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# broadcast

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3488. Git blob: `a4413d45c640addabc07e1aa09b3008c7e0d5563`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="spoken" xml:id="gi-broadcast" ident="broadcast">
  <gloss versionDate="2009-04-17" xml:lang="en">broadcast</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">diffusion</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes a broadcast used as the source of a spoken text.</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">décrit une émission utilisée comme source de la parole transcrite.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트의 원본으로 사용된 방송에 대해 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述口說文本的公開播送影音來源相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話されたテキストの元となる放送を示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">beschreibt eine Sendung,
  die als Quelle eines gesprochenen Textes genutzt wird.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe la emisión usada como fuente de un texto escrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive una messa in onda utilizzata quale fonte di un testo orale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.recordingPart"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.biblLike"/>
      <elementRef key="recording"/>
    </alternate>
  </content>
  <constraintSpec ident="broadcast-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:broadcast"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-broadcast-egXML-fk">
      <broadcast>
        <bibl>
          <author>Radio Trent</author>
          <title>Gone Tomorrow</title>
          <respStmt>
            <resp>Presenter</resp>
            <name>Tim Maby</name>
          </respStmt>
          <respStmt>
            <resp>Producer</resp>
            <name>Mary Kerr</name>
          </respStmt>
          <date when="1989-06-12T12:30:00">12 June 89, 1230 pm</date>
        </bibl>
      </broadcast>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-broadcast-egXML-pe">
      <broadcast>
        <bibl>
          <author>中國廣播公司</author>
          <title>司馬中原說鬼故事</title>
          <respStmt>
            <resp>主持人</resp>
            <name>司馬中原</name>
          </respStmt>
          <respStmt>
            <resp>主持人</resp>
            <name>常勤芬</name>
          </respStmt>
          <date when="1989-06-12T12:30:00">1989年6月12日1230 pm</date>
        </bibl>
      </broadcast>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD32"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="en">broadcast</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">diffusion</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes a broadcast used as the source of a spoken text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">décrit une émission utilisée comme source de la parole transcrite.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트의 원본으로 사용된 방송에 대해 기술한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述口說文本的公開播送影音來源相關資訊。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話されたテキストの元となる放送を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">beschreibt eine Sendung,
  die als Quelle eines gesprochenen Textes genutzt wird.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la emisión usada como fuente de un texto escrito.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive una messa in onda utilizzata quale fonte di un testo orale.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.recordingPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.biblLike"/>
      <elementRef key="recording"/>
    </alternate>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="broadcast-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:broadcast"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-broadcast-egXML-fk">
      <broadcast>
        <bibl>
          <author>Radio Trent</author>
          <title>Gone Tomorrow</title>
          <respStmt>
            <resp>Presenter</resp>
            <name>Tim Maby</name>
          </respStmt>
          <respStmt>
            <resp>Producer</resp>
            <name>Mary Kerr</name>
          </respStmt>
          <date when="1989-06-12T12:30:00">12 June 89, 1230 pm</date>
        </bibl>
      </broadcast>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-broadcast-egXML-pe">
      <broadcast>
        <bibl>
          <author>中國廣播公司</author>
          <title>司馬中原說鬼故事</title>
          <respStmt>
            <resp>主持人</resp>
            <name>司馬中原</name>
          </respStmt>
          <respStmt>
            <resp>主持人</resp>
            <name>常勤芬</name>
          </respStmt>
          <date when="1989-06-12T12:30:00">1989年6月12日1230 pm</date>
        </bibl>
      </broadcast>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD32"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b16

