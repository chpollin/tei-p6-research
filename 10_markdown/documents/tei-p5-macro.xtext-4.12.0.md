---
type: representation
source-type: document
source: '[[00_sources/tei-p5-macro.xtext-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 macro.xtext
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/macro.xtext.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# macro.xtext

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1854. Git blob: `75942b4ee66aa7443bcb4c523a8870d39998b188`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<macroSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" ident="macro.xtext">
  <gloss versionDate="2005-10-05" xml:lang="en">extended text</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">확장 텍스트</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">擴充文件</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">texte étendu</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">el texto</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">testo esteso</gloss>
  <desc versionDate="2005-10-05" xml:lang="en">defines a sequence of character data and gaiji elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문자 데이터 및 외부 문자 요소의 연쇄를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一連串文字資料與缺字元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">一連の文字列や外字要素を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit une suite de caractères et d'éléments gaiji.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una secuencia de caracteres y elementos gaiji.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce una sequenza di caratteri ed elementi gaiji.</desc>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
      </alternate>
    
  </content>
</macroSpec>
```

## Source blocks

### Block 1

XML location: `/macroSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-10-05" xml:lang="en">extended text</gloss>
```

^b1

### Block 2

XML location: `/macroSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">확장 텍스트</gloss>
```

^b2

### Block 3

XML location: `/macroSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">擴充文件</gloss>
```

^b3

### Block 4

XML location: `/macroSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">texte étendu</gloss>
```

^b4

### Block 5

XML location: `/macroSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">el texto</gloss>
```

^b5

### Block 6

XML location: `/macroSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">testo esteso</gloss>
```

^b6

### Block 7

XML location: `/macroSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-10-05" xml:lang="en">defines a sequence of character data and gaiji elements.</desc>
```

^b7

### Block 8

XML location: `/macroSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문자 데이터 및 외부 문자 요소의 연쇄를 정의한다.</desc>
```

^b8

### Block 9

XML location: `/macroSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一連串文字資料與缺字元素。</desc>
```

^b9

### Block 10

XML location: `/macroSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">一連の文字列や外字要素を定義する。</desc>
```

^b10

### Block 11

XML location: `/macroSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit une suite de caractères et d'éléments gaiji.</desc>
```

^b11

### Block 12

XML location: `/macroSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una secuencia de caracteres y elementos gaiji.</desc>
```

^b12

### Block 13

XML location: `/macroSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce una sequenza di caratteri ed elementi gaiji.</desc>
```

^b13

### Block 14

XML location: `/macroSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
      </alternate>
    
  </content>
```

^b14

