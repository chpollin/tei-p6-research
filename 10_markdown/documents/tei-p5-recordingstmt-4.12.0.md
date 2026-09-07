---
type: representation
source-type: document
source: '[[00_sources/tei-p5-recordingstmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 recordingStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/recordingStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# recordingStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3504. Git blob: `95a42e50edc697bb51fb131c39710867a3820677`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" xml:id="gi-recordingStmt" ident="recordingStmt">
  <gloss versionDate="2005-01-14" xml:lang="en">recording statement</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">déclaration d'enregistrements</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">녹음 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">影音陳述</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Erklärung zur Aufnahme</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de grabación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulla registrazione</gloss>
  <desc versionDate="2007-04-27" xml:lang="en">describes a set of recordings used as the basis for transcription of a
spoken text.</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">décrit un ensemble d’enregistrements utilisés pour la transcription de la parole.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 전사의 기반으로 사용된 녹음 집합을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">當所轉錄的口說文本來源為影音檔案時，在此描述影音錄製的相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話テキストの転記の元になる録音、録画されたものを示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">beschreibt eine Sammlung von
  Aufnahmen, die als Basis für die Transkription eines gesprochenen Texts
  verwendet wurde.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe la serie de grabaciones utilizadas como la base de transcripción de un texto hablado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive l'insieme delle registrazioni usate nella trascrizione di un testo orale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.sourceDescPart"/>
  </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      
        <elementRef key="recording" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recordingStmt-egXML-ko">
      <recordingStmt>
        <recording type="audio" dur="P30M">
          <respStmt>
            <resp>Location recording by</resp>
            <name>Sound Services Ltd.</name>
          </respStmt>
          <equipment>
            <p>Multiple close microphones mixed down to stereo Digital
     Audio Tape, standard play, 44.1 KHz sampling frequency</p>
          </equipment>
          <date>12 Jan 1987</date>
        </recording>
      </recordingStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recordingStmt-egXML-yb">
      <recordingStmt>
        <p>Three
distinct recordings made by hidden microphone in early February
2001.</p>
      </recordingStmt>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD32"/>
    <ptr target="#HD3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">recording statement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">déclaration d'enregistrements</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">녹음 진술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">影音陳述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Erklärung zur Aufnahme</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de grabación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulla registrazione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-27" xml:lang="en">describes a set of recordings used as the basis for transcription of a
spoken text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">décrit un ensemble d’enregistrements utilisés pour la transcription de la parole.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 전사의 기반으로 사용된 녹음 집합을 기술한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">當所轉錄的口說文本來源為影音檔案時，在此描述影音錄製的相關資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話テキストの転記の元になる録音、録画されたものを示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">beschreibt eine Sammlung von
  Aufnahmen, die als Basis für die Transkription eines gesprochenen Texts
  verwendet wurde.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la serie de grabaciones utilizadas como la base de transcripción de un texto hablado.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive l'insieme delle registrazioni usate nella trascrizione di un testo orale.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.sourceDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      
        <elementRef key="recording" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recordingStmt-egXML-ko">
      <recordingStmt>
        <recording type="audio" dur="P30M">
          <respStmt>
            <resp>Location recording by</resp>
            <name>Sound Services Ltd.</name>
          </respStmt>
          <equipment>
            <p>Multiple close microphones mixed down to stereo Digital
     Audio Tape, standard play, 44.1 KHz sampling frequency</p>
          </equipment>
          <date>12 Jan 1987</date>
        </recording>
      </recordingStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recordingStmt-egXML-yb">
      <recordingStmt>
        <p>Three
distinct recordings made by hidden microphone in early February
2001.</p>
      </recordingStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD32"/>
    <ptr target="#HD3"/>
  </listRef>
```

^b20

