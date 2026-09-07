---
type: representation
source-type: document
source: '[[00_sources/tei-p5-encodingdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 encodingDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/encodingDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# encodingDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3409. Git blob: `9f0c41133a9eacd76ce52f9520464890bd57422f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-encodingDesc" ident="encodingDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">encoding description</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">description de l'encodage</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">부호화 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">編碼描述</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Beschreibung der Kodierung</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">Descripción de la codificación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione della codifica</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">documents the relationship between an electronic text and the
source or sources from which it was derived.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">documente la relation d'un texte électronique avec sa ou ses sources.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자 텍스트와 그것의 원전 텍스트 혹은 텍스트들 사이의 관련성을 기록한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">記錄電子文件和其ㄧ個或多個文件來源之間的關係。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">電子テキストとその元資料との関係を示す。</desc>
  <desc versionDate="2016-11-17" xml:lang="de">dokumentiert das Verhältnis zwischen dem elektronischen Text und seiner Quelle oder den Quellen, von denen er sich ableitet.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">documenta la relación entre un texto electrónico y la fuente o fuentes de las que este deriva.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">documenta la relazione fra un documento elettronico e la o le fonti da cui è derivato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.teiHeaderPart"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.encodingDescPart"/>
      <classRef key="model.pLike"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-encodingDesc-egXML-vi">
      <encodingDesc>
        <p>Basic encoding, capturing lexical information only. All
        hyphenation, punctuation, and variant spellings normalized. No
        formatting or layout information preserved.</p>
      </encodingDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-encodingDesc-egXML-rs">
      <encodingDesc>
        <projectDesc>
          <p>Corpus de textes sélectionnés pour la formation MISAT,
          Frejus, juillet 2010.</p>
        </projectDesc>
        <samplingDecl>
          <p>Corpus d'échantillons de 2000 mots pris au début de
          chaque texte.</p>
        </samplingDecl>
      </encodingDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD5"/>
    <ptr target="#HD11"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">encoding description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">description de l'encodage</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">부호화 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">編碼描述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Beschreibung der Kodierung</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">Descripción de la codificación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione della codifica</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">documents the relationship between an electronic text and the
source or sources from which it was derived.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">documente la relation d'un texte électronique avec sa ou ses sources.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자 텍스트와 그것의 원전 텍스트 혹은 텍스트들 사이의 관련성을 기록한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">記錄電子文件和其ㄧ個或多個文件來源之間的關係。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">電子テキストとその元資料との関係を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">dokumentiert das Verhältnis zwischen dem elektronischen Text und seiner Quelle oder den Quellen, von denen er sich ableitet.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">documenta la relación entre un texto electrónico y la fuente o fuentes de las que este deriva.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">documenta la relazione fra un documento elettronico e la o le fonti da cui è derivato.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.teiHeaderPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.encodingDescPart"/>
      <classRef key="model.pLike"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-encodingDesc-egXML-vi">
      <encodingDesc>
        <p>Basic encoding, capturing lexical information only. All
        hyphenation, punctuation, and variant spellings normalized. No
        formatting or layout information preserved.</p>
      </encodingDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-encodingDesc-egXML-rs">
      <encodingDesc>
        <projectDesc>
          <p>Corpus de textes sélectionnés pour la formation MISAT,
          Frejus, juillet 2010.</p>
        </projectDesc>
        <samplingDecl>
          <p>Corpus d'échantillons de 2000 mots pris au début de
          chaque texte.</p>
        </samplingDecl>
      </encodingDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD5"/>
    <ptr target="#HD11"/>
  </listRef>
```

^b20

