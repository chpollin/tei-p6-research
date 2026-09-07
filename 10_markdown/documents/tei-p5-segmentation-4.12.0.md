---
type: representation
source-type: document
source: '[[00_sources/tei-p5-segmentation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 segmentation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/segmentation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# segmentation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3410. Git blob: `4f5c70fd3ec8005d5d0683897506eed2bbdc3fc5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-segmentation" ident="segmentation">
  <gloss versionDate="2007-06-12" xml:lang="en">segmentation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">segmentation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the principles according to which the text has been segmented, for example into
    sentences, tone-units, graphemic strata, etc.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit les principes selon lesquels le texte a été
    segmenté, par exemple en phrases, en intonèmes (unités tonales), en strates graphématiques
    (niveaux superposés de signes graphiques), etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 문장, 음성 단위, 문자적 층위로 텍스트가 분절되는 원리를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述文件分割的原理方法，例如分割成句子、音調單位、字形層次等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該テキストを分割した基準を示す。例えば、文、音単位、書記層など。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">gibt an, nach welchen Prinzipien ein Text segmentiert
    wurde, zum Beispiel in Sätze, Tonsequenzen, graphemische Einheiten, usw.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe los principios aplicados en la fragmentación del
    texto, p.ej. en las oraciones, sintagmas, morfemas, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive il modo in cui è stato segmentato il testo, ad
    esempio in frasi, unità toniche, strati grafemici, ecc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="segmentation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:segmentation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-segmentation-egXML-ij">
      <segmentation>
        <p><gi>s</gi> elements mark orthographic sentences and are numbered sequentially within
          their parent <gi>div</gi> element </p>
      </segmentation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-segmentation-egXML-wg">
      <p><gi>seg</gi> elements are used to mark functional constituents of various types within each
          <gi>s</gi>; the typology used is defined by a <gi>taxonomy</gi> element in the corpus
        header <gi>classDecl</gi>
         </p>
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
<gloss versionDate="2007-06-12" xml:lang="en">segmentation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">segmentation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the principles according to which the text has been segmented, for example into
    sentences, tone-units, graphemic strata, etc.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit les principes selon lesquels le texte a été
    segmenté, par exemple en phrases, en intonèmes (unités tonales), en strates graphématiques
    (niveaux superposés de signes graphiques), etc.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어 문장, 음성 단위, 문자적 층위로 텍스트가 분절되는 원리를 기술한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述文件分割的原理方法，例如分割成句子、音調單位、字形層次等。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストを分割した基準を示す。例えば、文、音単位、書記層など。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, nach welchen Prinzipien ein Text segmentiert
    wurde, zum Beispiel in Sätze, Tonsequenzen, graphemische Einheiten, usw.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe los principios aplicados en la fragmentación del
    texto, p.ej. en las oraciones, sintagmas, morfemas, etc.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il modo in cui è stato segmentato il testo, ad
    esempio in frasi, unità toniche, strati grafemici, ecc.</desc>
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
<constraintSpec ident="segmentation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:segmentation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-segmentation-egXML-ij">
      <segmentation>
        <p><gi>s</gi> elements mark orthographic sentences and are numbered sequentially within
          their parent <gi>div</gi> element </p>
      </segmentation>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-segmentation-egXML-wg">
      <p><gi>seg</gi> elements are used to mark functional constituents of various types within each
          <gi>s</gi>; the typology used is defined by a <gi>taxonomy</gi> element in the corpus
        header <gi>classDecl</gi>
         </p>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b16

