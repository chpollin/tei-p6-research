---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.phrase.xml-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.phrase.xml
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.phrase.xml.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.phrase.xml

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1806. Git blob: `2ce6ff8d3525bc5ffb74bdec9dca91829a217613`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="model" ident="model.phrase.xml">
  <desc versionDate="2007-10-03" xml:lang="en">groups phrase-level elements used to encode XML constructs such as element names, attribute
    names, and attribute values.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">요소명, 속성명, 그리고 속성값과 같이 XML 구성물을 부호화하는 구-층위 요소를 모아 놓는다.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">XML要素を符号化する、句レベルの要素をまとめる。例えば、要素名、属性 名、属性値など。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">regroupe des éléments de niveau expression utilisés pour
    encoder des constructions XML telles que des noms d'éléments, des noms d'attributs ou des
    valeurs d'attributs.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi a livello di sintagma utilizzati per
    codificare costrutti XML quali nomi di elementi e nomi e valori di attributi</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos usados para codificar construcciones en
    XML en el nivel sintagmático, p.ej. nombre de elemento, nombres de atributo, y valores de
    atributo.</desc>
  <classes>
    <memberOf key="model.limitedPhrase"/>
    
    <memberOf key="model.phrase"/>
  </classes>
  <listRef>
    <ptr target="#TD"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups phrase-level elements used to encode XML constructs such as element names, attribute
    names, and attribute values.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소명, 속성명, 그리고 속성값과 같이 XML 구성물을 부호화하는 구-층위 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">XML要素を符号化する、句レベルの要素をまとめる。例えば、要素名、属性 名、属性値など。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">regroupe des éléments de niveau expression utilisés pour
    encoder des constructions XML telles que des noms d'éléments, des noms d'attributs ou des
    valeurs d'attributs.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">raggruppa elementi a livello di sintagma utilizzati per
    codificare costrutti XML quali nomi di elementi e nomi e valori di attributi</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos usados para codificar construcciones en
    XML en el nivel sintagmático, p.ej. nombre de elemento, nombres de atributo, y valores de
    atributo.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="model.limitedPhrase"/>
    
    <memberOf key="model.phrase"/>
  </classes>
```

^b7

### Block 8

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD"/>
  </listRef>
```

^b8

