---
type: representation
source-type: document
source: '[[00_sources/tei-p5-lem-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 lem
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/lem.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# lem

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5229. Git blob: `460a1019eae5c4e168a67da53195c1980e090195`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-lem" ident="lem">
  <gloss versionDate="2005-01-14" xml:lang="en">lemma</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">레마</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">主題</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">lemme</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">lema</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the lemma, or base text, of a textual variation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형의 레마 또는 기본 텍스트를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個原文變異的主題或基礎文件。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">異なるテキストにおける対象語、すなわち基底テキスト(base text)を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le lemme ou le texte de base d'une variante textuelle.</desc>
  <desc versionDate="2022-06-30" xml:lang="es">contiene el lema, o texto base, de una variante textual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il lemma, o testo base, di una variante testuale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.textCritical"/>
    <memberOf key="att.witnessed"/>
  </classes>
  <content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.divLike"/>
      <classRef key="model.divPart"/>
      <elementRef key="titlePage"/>
      <!-- WINITA: begin 454 hack section -->
      <!--
          model.titlepagePart sans <binaryObject> and <graphic>, i.e.
          change to <classRef key="model.titlepagePart" except="binaryObject graphic"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="argument"/>
      <elementRef key="byline"/>
      <elementRef key="docAuthor"/>
      <elementRef key="docDate"/>
      <elementRef key="docEdition"/>
      <elementRef key="docImprint"/>
      <elementRef key="docTitle"/>
      <elementRef key="epigraph"/>
      <elementRef key="imprimatur"/>
      <elementRef key="speaker"/>
      <elementRef key="titlePart"/>
      <!--
          model.frontPart.drama sans <castList>, i.e.
          change to <classRef key="model.frontPart.drama" except="castList"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="epilogue"/>
      <elementRef key="performance"/>
      <elementRef key="prologue"/>
      <elementRef key="set"/>
      <!-- WINITA: end 454 hack section -->
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.inter"/>
      <classRef key="model.global"/>
      <classRef key="model.rdgPart"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lem-egXML-vt">
      <app>
        <lem wit="#El #Hg">Experience</lem>
        <rdg wit="#La" type="substantive">Experiment</rdg>
        <rdg wit="#Ra2" type="substantive">Eryment</rdg>
      </app>
    </egXML>
  </exemplum>
  <remarks ident="lem-remarks" versionDate="2021-08-25" xml:lang="en">
    <p>The term <term>lemma</term> is used in text criticism to describe the reading given in the
      main text, which may be used as a heading in the apparatus itself. This usage connects it to
      mathematics (where a lemma is a proven proposition used as a step in a proof, a "given") and
      natural-language processing (where a lemma is the dictionary headword associated with an
      inflected form in the running text). </p>
  </remarks>
  <remarks ident="lem-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le terme <term>lemma</term> est utilisé dans la critique textuelle pour décrire la
                leçon dans le texte lui-même (par opposition à l'apparat) ; cette acception est
                différente du sens en mathématiques (où un lemme est une étape majeure dans une
                démonstration) et du sens dans le domaine du traitement du langage naturel (où un
                lemme est la forme du dictionnaire associée à une forme fléchie dans le texte
                courant).</p>
  </remarks>
  <remarks ident="lem-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    校勘学において用語「lemma」は、テキスト中の解釈を指すものとして使
    われる(現存資料中の解釈とは異なる)。これは、数学上の意味(証明過程
    中のいち段階)とは異なっている。また、自然言語処理上の意味(本文中の
    屈折形と関連する、辞書中の項目)とも異なる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">lemma</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">레마</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">主題</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">lemme</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">lema</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the lemma, or base text, of a textual variation.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형의 레마 또는 기본 텍스트를 포함한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個原文變異的主題或基礎文件。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">異なるテキストにおける対象語、すなわち基底テキスト(base text)を示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le lemme ou le texte de base d'une variante textuelle.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-06-30" xml:lang="es">contiene el lema, o texto base, de una variante textual.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il lemma, o testo base, di una variante testuale.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.textCritical"/>
    <memberOf key="att.witnessed"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.divLike"/>
      <classRef key="model.divPart"/>
      <elementRef key="titlePage"/>
      <!-- WINITA: begin 454 hack section -->
      <!--
          model.titlepagePart sans <binaryObject> and <graphic>, i.e.
          change to <classRef key="model.titlepagePart" except="binaryObject graphic"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="argument"/>
      <elementRef key="byline"/>
      <elementRef key="docAuthor"/>
      <elementRef key="docDate"/>
      <elementRef key="docEdition"/>
      <elementRef key="docImprint"/>
      <elementRef key="docTitle"/>
      <elementRef key="epigraph"/>
      <elementRef key="imprimatur"/>
      <elementRef key="speaker"/>
      <elementRef key="titlePart"/>
      <!--
          model.frontPart.drama sans <castList>, i.e.
          change to <classRef key="model.frontPart.drama" except="castList"/>
          once https://github.com/TEIC/Stylesheets/issues/454 is fixed:
      -->
      <elementRef key="epilogue"/>
      <elementRef key="performance"/>
      <elementRef key="prologue"/>
      <elementRef key="set"/>
      <!-- WINITA: end 454 hack section -->
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.inter"/>
      <classRef key="model.global"/>
      <classRef key="model.rdgPart"/>
    </alternate>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lem-egXML-vt">
      <app>
        <lem wit="#El #Hg">Experience</lem>
        <rdg wit="#La" type="substantive">Experiment</rdg>
        <rdg wit="#Ra2" type="substantive">Eryment</rdg>
      </app>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="lem-remarks" versionDate="2021-08-25" xml:lang="en">
    <p>The term <term>lemma</term> is used in text criticism to describe the reading given in the
      main text, which may be used as a heading in the apparatus itself. This usage connects it to
      mathematics (where a lemma is a proven proposition used as a step in a proof, a "given") and
      natural-language processing (where a lemma is the dictionary headword associated with an
      inflected form in the running text). </p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="lem-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le terme <term>lemma</term> est utilisé dans la critique textuelle pour décrire la
                leçon dans le texte lui-même (par opposition à l'apparat) ; cette acception est
                différente du sens en mathématiques (où un lemme est une étape majeure dans une
                démonstration) et du sens dans le domaine du traitement du langage naturel (où un
                lemme est la forme du dictionnaire associée à une forme fléchie dans le texte
                courant).</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="lem-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    校勘学において用語「lemma」は、テキスト中の解釈を指すものとして使
    われる(現存資料中の解釈とは異なる)。これは、数学上の意味(証明過程
    中のいち段階)とは異なっている。また、自然言語処理上の意味(本文中の
    屈折形と関連する、辞書中の項目)とも異なる。
    </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b19

