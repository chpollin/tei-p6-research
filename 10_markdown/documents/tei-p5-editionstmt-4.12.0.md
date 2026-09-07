---
type: representation
source-type: document
source: '[[00_sources/tei-p5-editionstmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 editionStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/editionStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# editionStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4310. Git blob: `16db311fa7c2c52e42d1199e3cb631736259517c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-editionStmt" ident="editionStmt">
  <gloss versionDate="2005-01-14" xml:lang="en">edition statement</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">mention d'édition</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">편집 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">版本陳述</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Angaben zur Ausgabe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de la edición</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sull'edizione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups information relating to one edition of a text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">regroupe les informations relatives à l’édition d’un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 한 판에 관련된 정보를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文件某一版本的相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">版に関する情報をまとめる。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">umfasst Angaben, die sich auf eine spezifische Ausgabe eines Textes beziehen.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa la información relativa a la edición de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni riguardo una edizione di un testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        <elementRef key="edition"/>
        
          <classRef key="model.respLike" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-ne">
      <editionStmt>
        <edition n="S2">Students' edition</edition>
        <respStmt>
          <resp>Adapted by </resp>
          <name>Elizabeth Kirk</name>
        </respStmt>
      </editionStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-yu">
      <editionStmt>
        <edition>Deuxième édition</edition>
        <respStmt>
          <resp>réalisée par</resp>
          <name>L. F.</name>
        </respStmt>
      </editionStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-ep">
      <editionStmt>
        <p>Première édition électronique, Nancy, <date> 2002</date>, réalisée dans le cadre de la
            base <ref target="http://www.frantext.fr/">FRANTEXT</ref> .</p>
      </editionStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-wy">
      <editionStmt>
        <edition n="S2">學生版</edition>
        <respStmt>
          <resp>改編自</resp>
          <name>伊莉莎白．科克</name>
        </respStmt>
      </editionStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-nv">
      <editionStmt>
        <p>初版<date>1991年，上學期</date>
            </p>
      </editionStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-to">
      <editionStmt>
        <p>First edition, <date>Michaelmas Term, 1991.</date>
            </p>
      </editionStmt>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD22"/>
    <ptr target="#HD2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">edition statement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">mention d'édition</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">편집 진술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">版本陳述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angaben zur Ausgabe</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de la edición</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sull'edizione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups information relating to one edition of a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">regroupe les informations relatives à l’édition d’un texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 한 판에 관련된 정보를 모아 놓는다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文件某一版本的相關資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">版に関する情報をまとめる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">umfasst Angaben, die sich auf eine spezifische Ausgabe eines Textes beziehen.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa la información relativa a la edición de un texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni riguardo una edizione di un testo.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        <elementRef key="edition"/>
        
          <classRef key="model.respLike" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-ne">
      <editionStmt>
        <edition n="S2">Students' edition</edition>
        <respStmt>
          <resp>Adapted by </resp>
          <name>Elizabeth Kirk</name>
        </respStmt>
      </editionStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-yu">
      <editionStmt>
        <edition>Deuxième édition</edition>
        <respStmt>
          <resp>réalisée par</resp>
          <name>L. F.</name>
        </respStmt>
      </editionStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-ep">
      <editionStmt>
        <p>Première édition électronique, Nancy, <date> 2002</date>, réalisée dans le cadre de la
            base <ref target="http://www.frantext.fr/">FRANTEXT</ref> .</p>
      </editionStmt>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-wy">
      <editionStmt>
        <edition n="S2">學生版</edition>
        <respStmt>
          <resp>改編自</resp>
          <name>伊莉莎白．科克</name>
        </respStmt>
      </editionStmt>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-nv">
      <editionStmt>
        <p>初版<date>1991年，上學期</date>
            </p>
      </editionStmt>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editionStmt-egXML-to">
      <editionStmt>
        <p>First edition, <date>Michaelmas Term, 1991.</date>
            </p>
      </editionStmt>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD22"/>
    <ptr target="#HD2"/>
  </listRef>
```

^b24

