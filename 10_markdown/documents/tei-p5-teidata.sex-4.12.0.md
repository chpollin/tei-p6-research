---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.sex-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.sex
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.sex.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.sex

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2200. Git blob: `6a3519a897a1e6572f19b140176cc0e72583926c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.sex">
  <desc versionDate="2022-05-10" xml:lang="en">defines the range of attribute values used to identify
    the sex of an organism.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">인간 또는 동물의 성을 식별하는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍用以識別人類或動物的性別</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">なんらかの生命体の性別を示す属性値の範囲を定義する。</desc>
  <desc versionDate="2022-05-10" xml:lang="fr">définit la gamme des valeurs d'attributs employés
    pour identifier le sexe d’un organisme.</desc>
  <desc versionDate="2022-05-10" xml:lang="es">define la gama de valores de atributos usados para
    identificar el sexo de un organismo.</desc>
  <desc versionDate="2022-05-10" xml:lang="it">definisce una gamma di valori di attributi usati per
    identificare il sesso di un organismo.</desc>
  <content>
    <dataRef key="teidata.enumerated"/>
  </content>
  <remarks ident="teidata.sex-remarks" versionDate="2022-08-27" xml:lang="en">
    <p>Values for attributes using this datatype may be defined locally by a project, or they may refer to an external standard.</p>
  </remarks>
  <remarks ident="teidata.sex-remarks" versionDate="2022-05-03" xml:lang="fr">
    <p>Les valeurs de cet attribut peuvent être définies localement par un projet ou peuvent faire
      référence à un standard externe.</p>
  </remarks>
  <remarks ident="teidata.sex-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>このデータ型を用いる属性の値は、プロジェクトごとに内部的に定めたり、外部の標準を参照したりしてよい。</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2022-05-10" xml:lang="en">defines the range of attribute values used to identify
    the sex of an organism.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인간 또는 동물의 성을 식별하는 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍用以識別人類或動物的性別</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">なんらかの生命体の性別を示す属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2022-05-10" xml:lang="fr">définit la gamme des valeurs d'attributs employés
    pour identifier le sexe d’un organisme.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-05-10" xml:lang="es">define la gama de valores de atributos usados para
    identificar el sexo de un organismo.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2022-05-10" xml:lang="it">definisce una gamma di valori di attributi usati per
    identificare il sesso di un organismo.</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <dataRef key="teidata.enumerated"/>
  </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.sex-remarks" versionDate="2022-08-27" xml:lang="en">
    <p>Values for attributes using this datatype may be defined locally by a project, or they may refer to an external standard.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.sex-remarks" versionDate="2022-05-03" xml:lang="fr">
    <p>Les valeurs de cet attribut peuvent être définies localement par un projet ou peuvent faire
      référence à un standard externe.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.sex-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>このデータ型を用いる属性の値は、プロジェクトごとに内部的に定めたり、外部の標準を参照したりしてよい。</p>
  </remarks>
```

^b11

