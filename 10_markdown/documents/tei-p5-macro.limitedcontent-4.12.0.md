---
type: representation
source-type: document
source: '[[00_sources/tei-p5-macro.limitedcontent-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 macro.limitedContent
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/macro.limitedContent.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# macro.limitedContent

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2000. Git blob: `01874ed5ff1e1c1361f3bdfa02709aa78f1ed49f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<macroSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="macro.limitedContent">
  <gloss versionDate="2007-04-14" xml:lang="en">paragraph content</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문단 내용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">段落內容</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">contenu du paragraphe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">contenido del párrafo</gloss>
  <desc versionDate="2007-10-18" xml:lang="en">defines the content of prose elements that are not used for transcription of extant materials.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">현존 자료의 전사에 사용되지 않은 산문적 요소 내용을 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義散文元素的內容，該元素未用於轉錄現存資料</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">現存する資料の転記で使われるものではない散文要素の内容を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit le contenu des éléments textuels qui ne sont
      pas utilisés pour la transcription des contenus existants.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define el contenido de elementos de prosa que no se usan para la transcripción de materiales existentes.</desc>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.limitedPhrase"/>
        <classRef key="model.inter"/>
      </alternate>
    
  </content>
  <listRef>
    <ptr target="#STEC"/>
  </listRef>
</macroSpec>
```

## Source blocks

### Block 1

XML location: `/macroSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-04-14" xml:lang="en">paragraph content</gloss>
```

^b1

### Block 2

XML location: `/macroSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문단 내용</gloss>
```

^b2

### Block 3

XML location: `/macroSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">段落內容</gloss>
```

^b3

### Block 4

XML location: `/macroSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contenu du paragraphe</gloss>
```

^b4

### Block 5

XML location: `/macroSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">contenido del párrafo</gloss>
```

^b5

### Block 6

XML location: `/macroSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the content of prose elements that are not used for transcription of extant materials.</desc>
```

^b6

### Block 7

XML location: `/macroSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현존 자료의 전사에 사용되지 않은 산문적 요소 내용을 정의한다.</desc>
```

^b7

### Block 8

XML location: `/macroSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義散文元素的內容，該元素未用於轉錄現存資料</desc>
```

^b8

### Block 9

XML location: `/macroSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">現存する資料の転記で使われるものではない散文要素の内容を定義する。</desc>
```

^b9

### Block 10

XML location: `/macroSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit le contenu des éléments textuels qui ne sont
      pas utilisés pour la transcription des contenus existants.</desc>
```

^b10

### Block 11

XML location: `/macroSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define el contenido de elementos de prosa que no se usan para la transcripción de materiales existentes.</desc>
```

^b11

### Block 12

XML location: `/macroSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.limitedPhrase"/>
        <classRef key="model.inter"/>
      </alternate>
    
  </content>
```

^b12

### Block 13

XML location: `/macroSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STEC"/>
  </listRef>
```

^b13

