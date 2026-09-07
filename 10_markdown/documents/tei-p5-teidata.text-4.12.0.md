---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.text-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.text
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.text.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.text

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1660. Git blob: `e0432a4e38998266a9e1415764be9c23454940c1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.text">
  <desc versionDate="2012-06-17" xml:lang="en">defines the range of attribute values used to express some
  kind of identifying string as a single sequence
  of Unicode characters possibly including whitespace.</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs 
      exprimant une chaine de caracteres Unicode, y compris des
  espaces blancs.</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">空白文字を含みうるUnicode文字の単一の列として表現される何らかの識別のための文字列を示す属性値の範囲を定義する。</desc>
  <content>
      <dataRef name="string"/>
   </content>
  <remarks ident="teidata.text-remarks" versionDate="2012-06-17" xml:lang="en">
      <p>Attributes using this datatype must contain a single
    <soCalled>token</soCalled> in which whitespace and other
    punctuation characters are permitted. </p>
  </remarks>
  <remarks ident="teidata.text-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>このデータ型を用いる属性は、単一の<soCalled>トークン</soCalled>（空白文字や句読点を入れてもよい）を含まなければならない。</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-06-17" xml:lang="en">defines the range of attribute values used to express some
  kind of identifying string as a single sequence
  of Unicode characters possibly including whitespace.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs 
      exprimant une chaine de caracteres Unicode, y compris des
  espaces blancs.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">空白文字を含みうるUnicode文字の単一の列として表現される何らかの識別のための文字列を示す属性値の範囲を定義する。</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="string"/>
   </content>
```

^b4

### Block 5

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.text-remarks" versionDate="2012-06-17" xml:lang="en">
      <p>Attributes using this datatype must contain a single
    <soCalled>token</soCalled> in which whitespace and other
    punctuation characters are permitted. </p>
  </remarks>
```

^b5

### Block 6

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.text-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>このデータ型を用いる属性は、単一の<soCalled>トークン</soCalled>（空白文字や句読点を入れてもよい）を含まなければならない。</p>
  </remarks>
```

^b6

