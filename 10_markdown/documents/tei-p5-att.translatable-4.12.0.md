---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.translatable-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.translatable
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.translatable.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.translatable

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3171. Git blob: `7940f69e4c872a6c5da6d930c0db9a5803827341`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" type="atts" ident="att.translatable" predeclare="true">
  <desc versionDate="2006-10-15" xml:lang="en">provides attributes used to  indicate the status of a translatable
portion of an ODD document.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">ODD 문서의 번역 가능 부분의 상태를 나타내는 속성을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供的屬性指出ODD文件中可翻譯部分的狀態。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ODD文書中の翻訳可能部分の状態を表す属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit les attributs utilisés pour indiquer le statut
      d'une partie traduisible d'un document ODD.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos utilizados para indicar el estatus de un fragmento traducibile de un documento aislado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi utilizzati per indicare lo status di una porzione traducibile di un documento isolato.</desc>
  <attList>
    <attDef ident="versionDate" usage="opt">
      <desc versionDate="2012-05-23" xml:lang="en">specifies the date on which the source text was extracted and sent to the translator</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">번역 버전이 도출된 원본의 버전 이름 또는 수를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該翻譯版本來源的版本名稱或版本數</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">翻訳対象となった元資料のバージョンを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie le nom de la version ou le numéro de la
          source dont la version traduite a été tirée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica nombre o número de versión del original del cual deriva la versione traducida</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica nome o numero di versione dell'originale da cui deriva la versione tradotta.</desc>
      <datatype><dataRef key="teidata.temporal.working"/></datatype>
      <remarks ident="att.translatable-attr.versionDate-remarks" versionDate="2012-05-23" xml:lang="en">
        <p>The <att>versionDate</att> attribute can be used to 
        determine whether a translation might
        need to be revisited, by comparing the modification date on the
        containing file with the <att>versionDate</att> value on the translation. If the
        file has changed, changelogs can be checked to see whether the source
        text has been modified since the translation was made.</p>
      </remarks>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-10-15" xml:lang="en">provides attributes used to  indicate the status of a translatable
portion of an ODD document.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">ODD 문서의 번역 가능 부분의 상태를 나타내는 속성을 제시한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供的屬性指出ODD文件中可翻譯部分的狀態。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ODD文書中の翻訳可能部分の状態を表す属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit les attributs utilisés pour indiquer le statut
      d'une partie traduisible d'un document ODD.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos utilizados para indicar el estatus de un fragmento traducibile de un documento aislado.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi utilizzati per indicare lo status di una porzione traducibile di un documento isolato.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-05-23" xml:lang="en">specifies the date on which the source text was extracted and sent to the translator</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">번역 버전이 도출된 원본의 버전 이름 또는 수를 명시한다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該翻譯版本來源的版本名稱或版本數</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">翻訳対象となった元資料のバージョンを示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie le nom de la version ou le numéro de la
          source dont la version traduite a été tirée.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica nombre o número de versión del original del cual deriva la versione traducida</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica nome o numero di versione dell'originale da cui deriva la versione tradotta.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.temporal.working"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.translatable-attr.versionDate-remarks" versionDate="2012-05-23" xml:lang="en">
        <p>The <att>versionDate</att> attribute can be used to 
        determine whether a translation might
        need to be revisited, by comparing the modification date on the
        containing file with the <att>versionDate</att> value on the translation. If the
        file has changed, changelogs can be checked to see whether the source
        text has been modified since the translation was made.</p>
      </remarks>
```

^b16

