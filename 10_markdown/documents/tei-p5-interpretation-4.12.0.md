---
type: representation
source-type: document
source: '[[00_sources/tei-p5-interpretation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 interpretation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/interpretation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# interpretation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3546. Git blob: `1a8487979ad0acadc75034e91b68878e15b771e9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-interpretation" ident="interpretation">
  <gloss versionDate="2007-06-12" xml:lang="en">interpretation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">Interprétation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the scope of any analytic or interpretive information added to the text in
    addition to the transcription.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit le champ d’application de toute information
    analytique ou interprétative ajoutée à la transcription du texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전사본에 덧붙여 텍스트에 부착된 분석적 또는 해석적 정보의 범위를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出除了轉錄之外，文件中加入哪些分析性或詮釋性的資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">転記されたテキストに付加された、分析または解釈情報の範囲を示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">beschreibt den Umfang von Analyse oder Interpretation,
    die zusätzlich zur Transkription dem Text hinzugefügt wurde.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe la finalidad de cualquier información analítica
    o descriptiva añadida al texto en la transcripción.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive l'estensione di qualsiasi informazione analitica
    o interpretativa inserita nel testo, in aggiunta alla trascrizione</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="interpretation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:interpretation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpretation-egXML-be">
      <interpretation>
        <p>The part of speech analysis applied throughout section 4 was added by hand and has not
          been checked</p>
      </interpretation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpretation-egXML-um">
      <interpretation>
        <p>La partie concernant l'analyse de discours qui a été appliquée partout dans la section
            4 a été ajoutée à la main et n'a pas été vérifiée.</p>
      </interpretation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpretation-egXML-dr">
      <interpretation>
        <p>第四節部份言說分析是手寫加上去的，尚未檢查。</p>
      </interpretation>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD53"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">interpretation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">Interprétation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the scope of any analytic or interpretive information added to the text in
    addition to the transcription.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit le champ d’application de toute information
    analytique ou interprétative ajoutée à la transcription du texte.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전사본에 덧붙여 텍스트에 부착된 분석적 또는 해석적 정보의 범위를 기술한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出除了轉錄之外，文件中加入哪些分析性或詮釋性的資訊。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">転記されたテキストに付加された、分析または解釈情報の範囲を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">beschreibt den Umfang von Analyse oder Interpretation,
    die zusätzlich zur Transkription dem Text hinzugefügt wurde.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la finalidad de cualquier información analítica
    o descriptiva añadida al texto en la transcripción.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive l'estensione di qualsiasi informazione analitica
    o interpretativa inserita nel testo, in aggiunta alla trascrizione</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="interpretation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:interpretation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpretation-egXML-be">
      <interpretation>
        <p>The part of speech analysis applied throughout section 4 was added by hand and has not
          been checked</p>
      </interpretation>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpretation-egXML-um">
      <interpretation>
        <p>La partie concernant l'analyse de discours qui a été appliquée partout dans la section
            4 a été ajoutée à la main et n'a pas été vérifiée.</p>
      </interpretation>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-interpretation-egXML-dr">
      <interpretation>
        <p>第四節部份言說分析是手寫加上去的，尚未檢查。</p>
      </interpretation>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
  </listRef>
```

^b17

