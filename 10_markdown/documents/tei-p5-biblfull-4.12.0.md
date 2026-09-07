---
type: representation
source-type: document
source: '[[00_sources/tei-p5-biblfull-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 biblFull
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/biblFull.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# biblFull

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6276. Git blob: `29beee5bffa2ce3a3b8e7055c13469721025c3e0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-biblFull" ident="biblFull">
  <gloss versionDate="2007-07-04" xml:lang="en">fully-structured bibliographic citation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">완전히 구조화된 서지 인용 정보</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">citación bibliográfica estructurada completa</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">référence bibliographique totalement structurée</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">citazione bibliografica strutturata</gloss>
  <gloss versionDate="2023-09-21" xml:lang="ja">完全に構造化された典拠情報</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a fully-structured bibliographic citation, in which all components of the TEI file
    description are present.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">완전히 구조화된 서지 정보를 포함하며, 그 안에 TEI 파일 기술의 모든 성분이 제시된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含結構完整的書目資料，其中呈現出TEI檔案描述內的所有元件。</desc>
  <desc versionDate="2023-09-21" xml:lang="ja">完全に構造化された典拠情報を示す。TEIのファイル記述のための全要素が利用できる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une référence bibliographique totalement
    structurée : tous les composants de la description du fichier TEI  y sont présents.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una cita bibliográfica completamente
    estructurada, en la cual están presentes todos los componentes de la descripción del archivo
    TEI.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una citazione bibliografica interamente
    strutturata nella quale sono presenti tutti i componenti di descrizione di un file TEI.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.docStatus"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.biblLike"/>
  </classes>
  <content>
    <alternate>
      <sequence>
        <sequence>
          <elementRef key="titleStmt"/>
          <elementRef key="editionStmt" minOccurs="0"/>
          <elementRef key="extent" minOccurs="0"/>
          <elementRef key="publicationStmt"/>
          <elementRef key="seriesStmt" minOccurs="0" maxOccurs="unbounded"/>
          <elementRef key="notesStmt" minOccurs="0"/>
        </sequence>
        <elementRef key="sourceDesc" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <sequence>
        <elementRef key="fileDesc"/>
        <elementRef key="profileDesc"/>
      </sequence>
    </alternate>
  </content>
  <constraintSpec ident="biblFull-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:biblFull"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblFull-egXML-ov">
      <biblFull>
        <titleStmt>
          <title>The Feminist Companion to Literature in English: women writers from the middle ages
            to the present</title>
          <author>Blain, Virginia</author>
          <author>Clements, Patricia</author>
          <author>Grundy, Isobel</author>
        </titleStmt>
        <editionStmt>
          <edition>UK edition</edition>
        </editionStmt>
        <extent>1231 pp</extent>
        <publicationStmt>
          <publisher>Yale University Press</publisher>
          <pubPlace>New Haven and London</pubPlace>
          <date>1990</date>
        </publicationStmt>
        <sourceDesc>
          <p>No source: this is an original work</p>
        </sourceDesc>
      </biblFull>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblFull-egXML-gz" source="#fr-ex-Hydraul">
      <biblFull>
        <titleStmt>
          <title>Hydraulique fluviale. Tome 16, Écoulement et phénomènes de transport dans les
              canaux à géométrie simple </title>
          <editor> Mustafa Siddik Altinakar</editor>
          <editor> René Walther</editor>
        </titleStmt>
        <editionStmt>
          <edition>2e édition corrigée</edition>
        </editionStmt>
        <extent>627 p.</extent>
        <publicationStmt>
          <publisher>Presses polytechniques et universitaires romandes</publisher>
          <pubPlace>Lausanne</pubPlace>
          <date>2008</date>
        </publicationStmt>
        <sourceDesc>
          <p>Pas de source : il s'agit d'un document original</p>
        </sourceDesc>
      </biblFull>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblFull-egXML-wg">
      <biblFull>
        <titleStmt>
          <title>勘誤表：審視後的生命</title>
          <author>喬治．史坦納。</author>
        </titleStmt>
        <editionStmt>
          <edition>台灣地區繁中版本</edition>
        </editionStmt>
        <extent>208面</extent>
        <publicationStmt>
          <publisher>行人出版社</publisher>
          <pubPlace>台北</pubPlace>
          <date>2007</date>
        </publicationStmt>
        <sourceDesc>
          <p>譯自 Errata: An Examined Life (1997)</p>
        </sourceDesc>
      </biblFull>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COBITY"/>
    <ptr target="#HD2"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">fully-structured bibliographic citation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">완전히 구조화된 서지 인용 정보</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">citación bibliográfica estructurada completa</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">référence bibliographique totalement structurée</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">citazione bibliografica strutturata</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-09-21" xml:lang="ja">完全に構造化された典拠情報</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a fully-structured bibliographic citation, in which all components of the TEI file
    description are present.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">완전히 구조화된 서지 정보를 포함하며, 그 안에 TEI 파일 기술의 모든 성분이 제시된다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含結構完整的書目資料，其中呈現出TEI檔案描述內的所有元件。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-09-21" xml:lang="ja">完全に構造化された典拠情報を示す。TEIのファイル記述のための全要素が利用できる。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une référence bibliographique totalement
    structurée : tous les composants de la description du fichier TEI  y sont présents.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una cita bibliográfica completamente
    estructurada, en la cual están presentes todos los componentes de la descripción del archivo
    TEI.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una citazione bibliografica interamente
    strutturata nella quale sono presenti tutti i componenti di descrizione di un file TEI.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.docStatus"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.biblLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <sequence>
        <sequence>
          <elementRef key="titleStmt"/>
          <elementRef key="editionStmt" minOccurs="0"/>
          <elementRef key="extent" minOccurs="0"/>
          <elementRef key="publicationStmt"/>
          <elementRef key="seriesStmt" minOccurs="0" maxOccurs="unbounded"/>
          <elementRef key="notesStmt" minOccurs="0"/>
        </sequence>
        <elementRef key="sourceDesc" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <sequence>
        <elementRef key="fileDesc"/>
        <elementRef key="profileDesc"/>
      </sequence>
    </alternate>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="biblFull-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:biblFull"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblFull-egXML-ov">
      <biblFull>
        <titleStmt>
          <title>The Feminist Companion to Literature in English: women writers from the middle ages
            to the present</title>
          <author>Blain, Virginia</author>
          <author>Clements, Patricia</author>
          <author>Grundy, Isobel</author>
        </titleStmt>
        <editionStmt>
          <edition>UK edition</edition>
        </editionStmt>
        <extent>1231 pp</extent>
        <publicationStmt>
          <publisher>Yale University Press</publisher>
          <pubPlace>New Haven and London</pubPlace>
          <date>1990</date>
        </publicationStmt>
        <sourceDesc>
          <p>No source: this is an original work</p>
        </sourceDesc>
      </biblFull>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblFull-egXML-gz" source="#fr-ex-Hydraul">
      <biblFull>
        <titleStmt>
          <title>Hydraulique fluviale. Tome 16, Écoulement et phénomènes de transport dans les
              canaux à géométrie simple </title>
          <editor> Mustafa Siddik Altinakar</editor>
          <editor> René Walther</editor>
        </titleStmt>
        <editionStmt>
          <edition>2e édition corrigée</edition>
        </editionStmt>
        <extent>627 p.</extent>
        <publicationStmt>
          <publisher>Presses polytechniques et universitaires romandes</publisher>
          <pubPlace>Lausanne</pubPlace>
          <date>2008</date>
        </publicationStmt>
        <sourceDesc>
          <p>Pas de source : il s'agit d'un document original</p>
        </sourceDesc>
      </biblFull>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblFull-egXML-wg">
      <biblFull>
        <titleStmt>
          <title>勘誤表：審視後的生命</title>
          <author>喬治．史坦納。</author>
        </titleStmt>
        <editionStmt>
          <edition>台灣地區繁中版本</edition>
        </editionStmt>
        <extent>208面</extent>
        <publicationStmt>
          <publisher>行人出版社</publisher>
          <pubPlace>台北</pubPlace>
          <date>2007</date>
        </publicationStmt>
        <sourceDesc>
          <p>譯自 Errata: An Examined Life (1997)</p>
        </sourceDesc>
      </biblFull>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBITY"/>
    <ptr target="#HD2"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b21

