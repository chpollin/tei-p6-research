---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.word-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.word
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.word.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.word

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2476. Git blob: `ac234d68256ee2fb9b5a37dbdd3656cc1c93f033`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.word">
  <desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values expressed as a single
  word or token.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">단일 단어 또는 토큰으로 표현된 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍表示一個單字或代號</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">いち単語またはトークンをとる属性値の範囲を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant un seul mot ou signe.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una gama de valores de atributos expresados como una única palabra o señal.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi espressi come singola parola o singolo token.</desc>
  <content>
      <dataRef name="token" restriction="[^\p{C}\p{Z}]+"/>
   </content>
  <remarks ident="teidata.word-remarks" versionDate="2005-10-18" xml:lang="en">
      <p>Attributes using this datatype must contain a single
    <soCalled>word</soCalled> which contains only letters, digits,
    punctuation characters, or symbols: thus it cannot include
    whitespace.</p>
  </remarks>
  <remarks ident="teidata.word-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p>
    当該データ型を使用する属性値は、ひとつの<soCalled>単語</soCalled>
    になる。単語とは、文字、数字、句読点などの記号から構成されている。
    空白文字は含むことができない。
    </p>
  </remarks>
  <remarks ident="teidata.word-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Les attributs employant ce type de données doivent contenir un 
      <soCalled>mot</soCalled> simple  ne contenant que des lettres, des chiffres, 
      des signes de ponctuation, ou des symboles : ils ne peuvent donc pas inclure 
      d’espace.
    </p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-22" xml:lang="en">defines the range of attribute values expressed as a single
  word or token.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">단일 단어 또는 토큰으로 표현된 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍表示一個單字或代號</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">いち単語またはトークンをとる属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant un seul mot ou signe.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una gama de valores de atributos expresados como una única palabra o señal.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi espressi come singola parola o singolo token.</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="token" restriction="[^\p{C}\p{Z}]+"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.word-remarks" versionDate="2005-10-18" xml:lang="en">
      <p>Attributes using this datatype must contain a single
    <soCalled>word</soCalled> which contains only letters, digits,
    punctuation characters, or symbols: thus it cannot include
    whitespace.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.word-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p>
    当該データ型を使用する属性値は、ひとつの<soCalled>単語</soCalled>
    になる。単語とは、文字、数字、句読点などの記号から構成されている。
    空白文字は含むことができない。
    </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.word-remarks" versionDate="2007-06-12" xml:lang="fr">
      <p>Les attributs employant ce type de données doivent contenir un 
      <soCalled>mot</soCalled> simple  ne contenant que des lettres, des chiffres, 
      des signes de ponctuation, ou des symboles : ils ne peuvent donc pas inclure 
      d’espace.
    </p>
  </remarks>
```

^b11

