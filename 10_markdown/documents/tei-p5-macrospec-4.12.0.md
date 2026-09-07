---
type: representation
source-type: document
source: '[[00_sources/tei-p5-macrospec-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 macroSpec
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/macroSpec.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# macroSpec

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3013. Git blob: `db3796e2ada9709f3e9b981581ce46f95b103ef7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-macroSpec" ident="macroSpec">
  <gloss versionDate="2007-07-04" xml:lang="en">macro specification</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">매크로 명시</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">macroespecificación</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">spécification de macro.</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">indicazione di macro</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">documents the function and implementation of a pattern.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">유형의 기능 및 구현을 기록한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">記錄模式的功能與實行。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">パタンの機能や実装を解説する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">documente la fonction et l'implémentation d'un modèle.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">documenta la función y la aplicación de un pattern (patrón).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">documenta la funzione e l'applicazione di un pattern.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identSynonyms"/>
        <classRef key="model.descLike"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="1">
        <elementRef key="content"/>
        <elementRef key="valList"/>
      </alternate>
      <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-macroSpec-egXML-hw" source="#UND">
      <macroSpec module="tei" ident="macro.phraseSeq">
        <content>
          <alternate minOccurs="0" maxOccurs="unbounded">
              <textNode/>
              <classRef key="model.gLike"/>
              <classRef key="model.phrase"/>
              <classRef key="model.global"/>
          </alternate>
        </content>
      </macroSpec>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDcrystals"/>
    <ptr target="#TDENT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">macro specification</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">매크로 명시</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">macroespecificación</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">spécification de macro.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">indicazione di macro</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">documents the function and implementation of a pattern.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">유형의 기능 및 구현을 기록한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">記錄模式的功能與實行。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">パタンの機能や実装を解説する。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">documente la fonction et l'implémentation d'un modèle.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">documenta la función y la aplicación de un pattern (patrón).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">documenta la funzione e l'applicazione di un pattern.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="model.oddDecl"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identSynonyms"/>
        <classRef key="model.descLike"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="1">
        <elementRef key="content"/>
        <elementRef key="valList"/>
      </alternate>
      <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-macroSpec-egXML-hw" source="#UND">
      <macroSpec module="tei" ident="macro.phraseSeq">
        <content>
          <alternate minOccurs="0" maxOccurs="unbounded">
              <textNode/>
              <classRef key="model.gLike"/>
              <classRef key="model.phrase"/>
              <classRef key="model.global"/>
          </alternate>
        </content>
      </macroSpec>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDcrystals"/>
    <ptr target="#TDENT"/>
  </listRef>
```

^b17

