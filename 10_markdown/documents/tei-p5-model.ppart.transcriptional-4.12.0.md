---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.ppart.transcriptional-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.pPart.transcriptional
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.pPart.transcriptional.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.pPart.transcriptional

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1766. Git blob: `0214d7c9a18553fc1dc2a491f45e91380e23389d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="model" ident="model.pPart.transcriptional">
  <desc versionDate="2007-10-03" xml:lang="en">groups phrase-level elements used for editorial transcription of pre-existing source
    materials.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">앞서 존재하는 원본 자료의 편집상 전사에 사용되는 구-층위 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">僅匯集用於簡單的編輯更正和轉錄、而未能助於編寫的詞組層次元素</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">現存している資料に、編集を加えて転記する際に使う、句レベルの要素をま とめる。</desc>
  <desc versionDate="2009-05-27" xml:lang="fr">regroupe des éléments de niveau expression, utilisés pour
    des transcriptions éditoriales de sources pré-existantes.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi a livello di sintagma utilizzati per
    la trascrizione di fonti preesistenti</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa solo elementos sintagmáticos utilizados para
    simples correcciones y transcripciones editoriales que no parecen ser útiles para la autoría.</desc>
  <classes>    <memberOf key="model.pPart.edit"/>
  </classes>
  <listRef>
    <ptr target="#COED"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups phrase-level elements used for editorial transcription of pre-existing source
    materials.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">앞서 존재하는 원본 자료의 편집상 전사에 사용되는 구-층위 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">僅匯集用於簡單的編輯更正和轉錄、而未能助於編寫的詞組層次元素</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">現存している資料に、編集を加えて転記する際に使う、句レベルの要素をま とめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">regroupe des éléments de niveau expression, utilisés pour
    des transcriptions éditoriales de sources pré-existantes.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi a livello di sintagma utilizzati per
    la trascrizione di fonti preesistenti</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa solo elementos sintagmáticos utilizados para
    simples correcciones y transcripciones editoriales que no parecen ser útiles para la autoría.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>    <memberOf key="model.pPart.edit"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COED"/>
  </listRef>
```

^b9

