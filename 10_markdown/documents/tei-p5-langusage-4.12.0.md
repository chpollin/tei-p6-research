---
type: representation
source-type: document
source: '[[00_sources/tei-p5-langusage-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 langUsage
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/langUsage.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# langUsage

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4141. Git blob: `87e7cbba456bf1c88630b8d62d1864abb9d4ea75`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-langUsage" ident="langUsage">
  <gloss versionDate="2005-01-14" xml:lang="en">language usage</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">langue utilisée</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">언어 사용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">語言使用</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Sprachgebrauch</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">lengua empleada</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">lingua utilizzata</gloss>
  <desc versionDate="2008-01-28" xml:lang="en">describes the languages, sublanguages, registers, dialects, etc. represented within a text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit les langues, variétés de langues, registres, dialectes, etc. présents à l’intérieur d’un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 내에 나타나는 언어, 특수 언어, 레지스터, 방언 등을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述文件中使用的語言、次要語言、語域、方言等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト中にある言語、特殊言語、社会的方言、方言などを示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">beschreibt Sprachen, Subsprachen, Register, Dialekte usw., die innerhalb eines Textes vorkommen.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe las lenguas, jergas, registros, dialectos, etc. presentes en el texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive le lingue, i linguaggi secondari, i registri, i dialetti ecc. rappresentati all'interno di un testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="language" minOccurs="1" maxOccurs="unbounded"/>        
    </alternate>
  </content>
  <constraintSpec ident="langUsage-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:langUsage"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langUsage-egXML-ev">
      <langUsage>
        <language ident="fr-CA" usage="60">Québecois</language>
        <language ident="en-CA" usage="20">Canadian business English</language>
        <language ident="en-GB" usage="20">British English</language>
      </langUsage>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langUsage-egXML-en">
      <langUsage>
        <language ident="fr-CA" usage="60">Québecois</language>
        <language ident="en-CA" usage="20">Anglais canadien des affaires</language>
        <language ident="en-GB" usage="20">Anglais de Grande-Bretagne</language>
      </langUsage>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langUsage-egXML-xz">
      <langUsage>
        <language ident="fr-CA" usage="60">加拿大魁北克省法語</language>
        <language ident="en-CA" usage="20">加拿大商用英語</language>
        <language ident="en-GB" usage="20">英式英語</language>
      </langUsage>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD41"/>
    <ptr target="#HD4"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">language usage</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">langue utilisée</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">언어 사용</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">語言使用</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Sprachgebrauch</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">lengua empleada</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">lingua utilizzata</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-01-28" xml:lang="en">describes the languages, sublanguages, registers, dialects, etc. represented within a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit les langues, variétés de langues, registres, dialectes, etc. présents à l’intérieur d’un texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 내에 나타나는 언어, 특수 언어, 레지스터, 방언 등을 기술한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述文件中使用的語言、次要語言、語域、方言等。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト中にある言語、特殊言語、社会的方言、方言などを示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">beschreibt Sprachen, Subsprachen, Register, Dialekte usw., die innerhalb eines Textes vorkommen.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe las lenguas, jergas, registros, dialectos, etc. presentes en el texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive le lingue, i linguaggi secondari, i registri, i dialetti ecc. rappresentati all'interno di un testo.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="language" minOccurs="1" maxOccurs="unbounded"/>        
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="langUsage-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:langUsage"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langUsage-egXML-ev">
      <langUsage>
        <language ident="fr-CA" usage="60">Québecois</language>
        <language ident="en-CA" usage="20">Canadian business English</language>
        <language ident="en-GB" usage="20">British English</language>
      </langUsage>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langUsage-egXML-en">
      <langUsage>
        <language ident="fr-CA" usage="60">Québecois</language>
        <language ident="en-CA" usage="20">Anglais canadien des affaires</language>
        <language ident="en-GB" usage="20">Anglais de Grande-Bretagne</language>
      </langUsage>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langUsage-egXML-xz">
      <langUsage>
        <language ident="fr-CA" usage="60">加拿大魁北克省法語</language>
        <language ident="en-CA" usage="20">加拿大商用英語</language>
        <language ident="en-GB" usage="20">英式英語</language>
      </langUsage>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD41"/>
    <ptr target="#HD4"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b22

