---
type: representation
source-type: document
source: '[[00_sources/tei-p5-catchwords-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 catchwords
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/catchwords.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# catchwords

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3511. Git blob: `68fe4d81707805cb0f3549806044fcc6b74a58e3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="CATCHWORDS" ident="catchwords">
  <gloss versionDate="2007-06-12" xml:lang="en">catchwords</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">réclames</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="catchwords.desc">describes the system used to ensure correct ordering of the quires or similar making up a codex, incunable, or other object typically by means of annotations at the foot of the page.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일반적으로 페이지의 밑에 표시되며, 제본되지 않은 원고 또는 고판본의 정확한 순서를 보장하는 체계를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述一疊書頁裝訂成手抄本或書冊時，確保書頁順序無誤的方法，通常是利用頁腳的註記。</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">古い冊子本や刊本にみられる、折丁の正しい順序を確認するためのシステムについて記述する。一般には、ページの脚に注記される。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit le système utilisé pour s'assurer que les cahiers formant un manuscrit ou un incunable sont dans le bon ordre, typiquement au moyen d'annotations en bas de page.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe el sistema utilizado para garantizar la ordenación correcta de los cuadernos que constituyen un códex o un incunable, obtenido normalmente por medio de anotaciones a pie de página.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive il sistema utilizzato per garantire l'ordinamento corretto dei quaderni che costituiscono un codice o incunabolo, ottenuto solitamente tramite annotazioni a piè di pagina.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <constraintSpec ident="catchword_in_msDesc" scheme="schematron" xml:lang="en">
    <!-- 
         The <egXML> referred to in the constraint below is, of
         course, in the teix: namespace, not the tei: namespace.
         However, at the point in the processing pipeline when we want
         to test this the content of <egXML>s have been extracted and
         put in the TEI namespace for testing.
         At least, that's what I think is going on. —Syd, 2018-10-01
    -->
    <constraint>
      <sch:rule context="tei:catchwords">
        <sch:assert test="ancestor::tei:msDesc or ancestor::tei:egXML">The &lt;<sch:name/>> element should not be used outside of &lt;msDesc>.</sch:assert>
      </sch:rule>
    </constraint> 
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CATCHWORDS-egXML-be">
      <catchwords>Vertical catchwords in the hand of the scribe placed along 
the inner bounding line, reading from top to bottom.</catchwords>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msmisc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">catchwords</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">réclames</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="catchwords.desc">describes the system used to ensure correct ordering of the quires or similar making up a codex, incunable, or other object typically by means of annotations at the foot of the page.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일반적으로 페이지의 밑에 표시되며, 제본되지 않은 원고 또는 고판본의 정확한 순서를 보장하는 체계를 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述一疊書頁裝訂成手抄本或書冊時，確保書頁順序無誤的方法，通常是利用頁腳的註記。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">古い冊子本や刊本にみられる、折丁の正しい順序を確認するためのシステムについて記述する。一般には、ページの脚に注記される。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit le système utilisé pour s'assurer que les cahiers formant un manuscrit ou un incunable sont dans le bon ordre, typiquement au moyen d'annotations en bas de page.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe el sistema utilizado para garantizar la ordenación correcta de los cuadernos que constituyen un códex o un incunable, obtenido normalmente por medio de anotaciones a pie de página.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il sistema utilizzato per garantire l'ordinamento corretto dei quaderni che costituiscono un codice o incunabolo, ottenuto solitamente tramite annotazioni a piè di pagina.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="catchword_in_msDesc" scheme="schematron" xml:lang="en">
    <!-- 
         The <egXML> referred to in the constraint below is, of
         course, in the teix: namespace, not the tei: namespace.
         However, at the point in the processing pipeline when we want
         to test this the content of <egXML>s have been extracted and
         put in the TEI namespace for testing.
         At least, that's what I think is going on. —Syd, 2018-10-01
    -->
    <constraint>
      <sch:rule context="tei:catchwords">
        <sch:assert test="ancestor::tei:msDesc or ancestor::tei:egXML">The &lt;<sch:name/>> element should not be used outside of &lt;msDesc>.</sch:assert>
      </sch:rule>
    </constraint> 
  </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CATCHWORDS-egXML-be">
      <catchwords>Vertical catchwords in the hand of the scribe placed along 
the inner bounding line, reading from top to bottom.</catchwords>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msmisc"/>
  </listRef>
```

^b14

