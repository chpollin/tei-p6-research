---
type: representation
source-type: document
source: '[[00_sources/tei-p5-modulespec-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 moduleSpec
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/moduleSpec.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# moduleSpec

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3224. Git blob: `401bb18eb1f412cf9358f747fd3c49a0b907d5fc`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="MODULESPEC" ident="moduleSpec">
  <gloss versionDate="2007-07-04" xml:lang="en">module specification</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">모듈 명시</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">especificación de módulo</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">spécification de module</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">specifica del modulo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">documents the structure, content, and purpose of a single
module, i.e. a named and externally visible group of declarations.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 모듈에 대한 구조, 내용 및 목적을 기록한다. 즉, 선언의 이름과 외부적으로 가시적인 그룹</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">記錄單一模組的結構、內容、以及用途，例如：一個已命名且外部明確的宣告組。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">いちモジュールの構造、内容、目的を記録する。例えば、外部から名前で参
  照可能な宣言集合などである。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">documente la structure, le contenu et les
                        fonctions d'un module, i.e. d'un groupe de déclarations nommé et 
                        visible extérieurement.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">documenta la estructura, el contenido y la finalidad de un único módulo, es decir, un grupo de declaraciones específicamente indicado y visible externamente.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">documenta struttura, contenuto e scopo di un unico modulo, cioè un gruppo di dichiarazioni specificamente indicato ed esternamente visibile.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <sequence>      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.identEquiv"/>
          <elementRef key="idno"/>
          <classRef key="model.descLike"/>
        </alternate>
        <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="remarks" minOccurs="0"/>
        <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULESPEC-egXML-mo">
      <moduleSpec ident="namesdates">
        <idno type="FPI">Names and Dates</idno>
        <desc>Additional elements for names and dates</desc>
      </moduleSpec>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDmodules"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">module specification</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">모듈 명시</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">especificación de módulo</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">spécification de module</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">specifica del modulo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">documents the structure, content, and purpose of a single
module, i.e. a named and externally visible group of declarations.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 모듈에 대한 구조, 내용 및 목적을 기록한다. 즉, 선언의 이름과 외부적으로 가시적인 그룹</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">記錄單一模組的結構、內容、以及用途，例如：一個已命名且外部明確的宣告組。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">いちモジュールの構造、内容、目的を記録する。例えば、外部から名前で参
  照可能な宣言集合などである。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">documente la structure, le contenu et les
                        fonctions d'un module, i.e. d'un groupe de déclarations nommé et 
                        visible extérieurement.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">documenta la estructura, el contenido y la finalidad de un único módulo, es decir, un grupo de declaraciones específicamente indicado y visible externamente.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">documenta struttura, contenuto e scopo di un unico modulo, cioè un gruppo di dichiarazioni specificamente indicato ed esternamente visibile.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.oddDecl"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.identEquiv"/>
          <elementRef key="idno"/>
          <classRef key="model.descLike"/>
        </alternate>
        <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="remarks" minOccurs="0"/>
        <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULESPEC-egXML-mo">
      <moduleSpec ident="namesdates">
        <idno type="FPI">Names and Dates</idno>
        <desc>Additional elements for names and dates</desc>
      </moduleSpec>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDmodules"/>
  </listRef>
```

^b16

