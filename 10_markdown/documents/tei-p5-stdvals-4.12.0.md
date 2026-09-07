---
type: representation
source-type: document
source: '[[00_sources/tei-p5-stdvals-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 stdVals
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/stdVals.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# stdVals

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3449. Git blob: `e207255449d0a73e9abc8177eedfbb92cfd7ff5f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-stdVals" ident="stdVals">
  <gloss versionDate="2007-07-04" xml:lang="en">standard values</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">valeurs normalisées</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">표준 값</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">標準值</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Standardwerte</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">valores estándard</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">valori standard</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies the format used when standardized date or number values are supplied.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">précise le format utilisé pour exprimer une date ou une
    valeur numérique de manière normalisée .</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준화된 날짜 또는 숫자 값이 제시될 때 사용되는 형식을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">明確說明文本中標準化日期或數值所使用的格式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">標準的な日付や数値を示す形式を特定する。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">beschreibt das Format, das für Standard-Datumsangaben
    oder Zahlenwerte genutzt wird.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el formato usado cuando aparecen fechas
    estandarizadas o valores numéricos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica il formato usato quando vengono fornite date e
    altri valori numerici standardizzati.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="stdVals-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:stdVals"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stdVals-egXML-ri">
      <stdVals>
        <p>All integer numbers are left-filled with zeroes to 8 digits.</p>
      </stdVals>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stdVals-egXML-ve">
      <stdVals>
        <p>Les nombres entiers sont précédés de 0 à 8 chiffres.</p>
      </stdVals>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stdVals-egXML-tt">
      <stdVals>
        <p>所有數字四捨五入至小數點第二位</p>
      </stdVals>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">standard values</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">valeurs normalisées</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">표준 값</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">標準值</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Standardwerte</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">valores estándard</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">valori standard</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the format used when standardized date or number values are supplied.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">précise le format utilisé pour exprimer une date ou une
    valeur numérique de manière normalisée .</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준화된 날짜 또는 숫자 값이 제시될 때 사용되는 형식을 명시한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">明確說明文本中標準化日期或數值所使用的格式。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">標準的な日付や数値を示す形式を特定する。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">beschreibt das Format, das für Standard-Datumsangaben
    oder Zahlenwerte genutzt wird.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el formato usado cuando aparecen fechas
    estandarizadas o valores numéricos.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il formato usato quando vengono fornite date e
    altri valori numerici standardizzati.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="stdVals-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:stdVals"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stdVals-egXML-ri">
      <stdVals>
        <p>All integer numbers are left-filled with zeroes to 8 digits.</p>
      </stdVals>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stdVals-egXML-ve">
      <stdVals>
        <p>Les nombres entiers sont précédés de 0 à 8 chiffres.</p>
      </stdVals>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stdVals-egXML-tt">
      <stdVals>
        <p>所有數字四捨五入至小數點第二位</p>
      </stdVals>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b22

