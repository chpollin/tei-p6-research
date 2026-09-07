---
type: representation
source-type: document
source: '[[00_sources/tei-p5-char-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 char
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/char.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# char

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3067. Git blob: `13053743ab1be1abd9e914b0bd9272b41afb2ac5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="char" module="gaiji" xml:id="CHAR">
  <gloss versionDate="2005-01-14" xml:lang="en">character</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문자</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文字</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">caractère</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">carácter</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">carattere</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">文字</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides descriptive information about a character<!-- which is not
otherwise available in the document character set-->.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문자에 관한 기술 정보를 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個文字的描述性資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">文字に関する情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des informations descriptives sur un caractère.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona información descriptiva sobre un carácter.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni descrittive su di un carattere.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
    <elementRef key="unicodeProp"/>
    <elementRef key="unihanProp"/>
    <elementRef key="localProp"/>
    <elementRef key="mapping"/>
    <elementRef key="figure"/>
    <classRef key="model.graphicLike"/>
    <classRef key="model.noteLike"/>
    <classRef key="model.descLike"/>
  </alternate>
  </content>
  <exemplum versionDate="2019-07-01" xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CHAR-egXML-su">
      <char xml:id="circledU4EBA">
        <localProp name="Name" value="CIRCLED IDEOGRAPH 4EBA"/>
        <localProp name="daikanwa" value="36"/>
        <unicodeProp name="Decomposition_Mapping" value="circle"/>
        <mapping type="standard">人</mapping>
      </char>
    </egXML>
  </exemplum>
  <exemplum versionDate="2019-07-01" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CHAR-egXML-qs">
      <char xml:id="fr_circledU4EBA">
        <localProp name="nom" value="IDEOGRAMME ENCADRE 4EBA"/>
        <localProp name="daikanwa" value="36"/>
        <unicodeProp name="Decomposition_Mapping" value="circle"/>
        <mapping type="standard">人</mapping>
      </char>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#D25-20"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">character</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문자</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文字</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">caractère</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">carácter</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">carattere</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">文字</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides descriptive information about a character<!-- which is not
otherwise available in the document character set-->.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문자에 관한 기술 정보를 제공한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個文字的描述性資訊。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">文字に関する情報を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des informations descriptives sur un caractère.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona información descriptiva sobre un carácter.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni descrittive su di un carattere.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
    <elementRef key="unicodeProp"/>
    <elementRef key="unihanProp"/>
    <elementRef key="localProp"/>
    <elementRef key="mapping"/>
    <elementRef key="figure"/>
    <classRef key="model.graphicLike"/>
    <classRef key="model.noteLike"/>
    <classRef key="model.descLike"/>
  </alternate>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2019-07-01" xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CHAR-egXML-su">
      <char xml:id="circledU4EBA">
        <localProp name="Name" value="CIRCLED IDEOGRAPH 4EBA"/>
        <localProp name="daikanwa" value="36"/>
        <unicodeProp name="Decomposition_Mapping" value="circle"/>
        <mapping type="standard">人</mapping>
      </char>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2019-07-01" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CHAR-egXML-qs">
      <char xml:id="fr_circledU4EBA">
        <localProp name="nom" value="IDEOGRAMME ENCADRE 4EBA"/>
        <localProp name="daikanwa" value="36"/>
        <unicodeProp name="Decomposition_Mapping" value="circle"/>
        <mapping type="standard">人</mapping>
      </char>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#D25-20"/>
  </listRef>
```

^b19

