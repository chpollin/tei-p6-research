---
type: representation
source-type: document
source: '[[00_sources/tei-p5-secfol-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 secFol
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/secFol.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# secFol

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3861. Git blob: `0a8cdb27943d0c089ba9401f6374d50fd2503940`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="SECFOL" ident="secFol">
  <gloss versionDate="2007-12-20" xml:lang="en">second folio</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">두 번째 장</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">segundo folio</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">deuxième folio</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">secondo foglio</gloss>
  <desc versionDate="2012-12-27" xml:lang="en" xml:id="secfol.desc">marks the word or words taken from a fixed point in a codex (typically the beginning of the second leaf) in order to provide a unique identifier for it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">고유한 확인소를 제공하기 위해 미제본 원고의 고정 위치(일반적으로 두 번째 장의 시작)에서 얻어진 단어 또는 단어군</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">從手抄本中固定位置所拿開的一個或多個字 (通常在第二張書頁的開頭) ，目的是提供一個專有的識別符號。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ユニークな識別子を示すために、冊子中の特定点にある単語を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">le mot ou les mots repris d'un point précisément connu d'un codex (comme le début du second feuillet) pour identifier celui-ci de façon univoque.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">la palabra o palabras extraídas de un punto preciso de un códex (normalmente el inicio del segundo folio) con el fin de identificar lo mismo en modo unívoco.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">la parola o le parole estratte da un punto preciso di un codice (di solito l'inizio del secondo foglio) al fine di identificare lo stesso in modo univoco.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <constraintSpec ident="secFol_in_msDesc" scheme="schematron" xml:lang="en">
    <!-- 
         The <egXML> referred to in the constraint below is, of
         course, in the teix: namespace, not the tei: namespace.
         However, at the point in the processing pipeline when we want
         to test this the content of <egXML>s have been extracted and
         put in the TEI namespace for testing.
         At least, that's what I think is going on. —Syd, 2018-10-01
      -->
    <constraint>
      <sch:rule context="tei:secFol">
        <sch:assert test="ancestor::tei:msDesc or ancestor::tei:egXML">The &lt;<sch:name/>> element should not be used outside of &lt;msDesc>.</sch:assert>
      </sch:rule>
    </constraint> 
  </constraintSpec>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SECFOL-egXML-bj">
      <secFol>(con-)versio morum</secFol>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SECFOL-egXML-dr">
      <secFol>(con-)versio morum</secFol>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SECFOL-egXML-us">
      <secFol>当臥遊適</secFol>
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
<gloss versionDate="2007-12-20" xml:lang="en">second folio</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">두 번째 장</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">segundo folio</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">deuxième folio</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">secondo foglio</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en" xml:id="secfol.desc">marks the word or words taken from a fixed point in a codex (typically the beginning of the second leaf) in order to provide a unique identifier for it.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">고유한 확인소를 제공하기 위해 미제본 원고의 고정 위치(일반적으로 두 번째 장의 시작)에서 얻어진 단어 또는 단어군</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">從手抄本中固定位置所拿開的一個或多個字 (通常在第二張書頁的開頭) ，目的是提供一個專有的識別符號。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ユニークな識別子を示すために、冊子中の特定点にある単語を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">le mot ou les mots repris d'un point précisément connu d'un codex (comme le début du second feuillet) pour identifier celui-ci de façon univoque.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">la palabra o palabras extraídas de un punto preciso de un códex (normalmente el inicio del segundo folio) con el fin de identificar lo mismo en modo unívoco.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">la parola o le parole estratte da un punto preciso di un codice (di solito l'inizio del secondo foglio) al fine di identificare lo stesso in modo univoco.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="secFol_in_msDesc" scheme="schematron" xml:lang="en">
    <!-- 
         The <egXML> referred to in the constraint below is, of
         course, in the teix: namespace, not the tei: namespace.
         However, at the point in the processing pipeline when we want
         to test this the content of <egXML>s have been extracted and
         put in the TEI namespace for testing.
         At least, that's what I think is going on. —Syd, 2018-10-01
      -->
    <constraint>
      <sch:rule context="tei:secFol">
        <sch:assert test="ancestor::tei:msDesc or ancestor::tei:egXML">The &lt;<sch:name/>> element should not be used outside of &lt;msDesc>.</sch:assert>
      </sch:rule>
    </constraint> 
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SECFOL-egXML-bj">
      <secFol>(con-)versio morum</secFol>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SECFOL-egXML-dr">
      <secFol>(con-)versio morum</secFol>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SECFOL-egXML-us">
      <secFol>当臥遊適</secFol>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msmisc"/>
  </listRef>
```

^b20

