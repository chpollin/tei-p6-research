---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.pattern-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.pattern
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.pattern.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.pattern

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4790. Git blob: `58b715f7da86808e52e762ee150414bfd4655416`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.pattern">
  <!-- <gloss 
          versionDate="2007-07-02"
          xml:lang="en">regular expression pattern</gloss>
  <gloss 
          versionDate="2007-12-20"
          xml:lang="ko">정규표현 유형</gloss>-->
  <desc versionDate="2007-10-18" xml:lang="en">defines attribute values which
    are expressed as a regular expression.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">정규표현으로 표시된 속성 값을 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以固定方法表示</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">正規表現を属性値として定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs
    d'attributs exprimant une expression régulière.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una gama de valores de
    atributos expresados como una expresión regular.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce una gamma di valori di
    attributi rappresentati come espressione regolare</desc>
  <content>
    <dataRef name="token"/>
  </content>
  <remarks ident="teidata.pattern-remarks" versionDate="2013-03-18" xml:lang="en">
    <p>
      <cit rend="display">
        <quote>A regular expression, often called a <term>pattern</term>, is an
          expression that describes a set of strings. They are usually used to
          give a concise description of a set, without having to list all
          elements. For example, the set containing the three strings
            <mentioned>Handel</mentioned>, <mentioned>Händel</mentioned>, and
            <mentioned>Haendel</mentioned> can be described by the pattern
            <code>H(ä|ae?)ndel</code> (or alternatively, it is said that the
          pattern <code>H(ä|ae?)ndel</code>
          <term>matches</term> each of the three strings)</quote>
        <ref target="http://en.wikipedia.org/wiki/Regular_expression#Basic_concepts">Wikipedia </ref>
      </cit>
    </p>
    <p>This TEI datatype is mapped to the XSD token datatype, and may therefore
      contain any string of characters. However, it is recommended that the
      value used conform to the particular flavour of regular expression syntax
      supported by XSD Schema. </p>
    <!-- http://www.regular-expressions.info/xml.html -->
  </remarks>
  <remarks ident="teidata.pattern-remarks" xml:lang="ja" versionDate="2024-08-08">
    <p>
      <cit rend="display"><quote>正規表現は、よく<term>パタン/パターン</term>ともいわれるもので、文字列の集合を記述するための表現方法である。一般には、簡潔な表現で、 すべての要素を列挙することなく集合を表現するために使用される。例えば、三つの文字列<mentioned>Handel</mentioned>、<mentioned>Händel</mentioned>、<mentioned>Haendel</mentioned>〔訳注：これらはすべて「ヘンデル」の異表記〕を、一つのパタン<code>H(ä|ae?)ndel</code>で記述することができる（あるいは、<code>H(ä|ae?)ndel</code>は、三つの文字列のいずれにも<term>マッチする</term>といわれる）。</quote><ref target="http://en.wikipedia.org/wiki/Regular_expression#Basic_concepts">wikipedia</ref></cit>
    </p>
  </remarks>
  <remarks ident="teidata.pattern-remarks" versionDate="2009-05-25" xml:lang="fr">
    <p>
      <cit>
        <quote>Une expression régulière, souvent appelée <term>modèle</term>,
          est une expression qui décrit un jeu de chaînes de caractères. Elles
          sont généralement utilisées pour donner une brève description d'un
          jeu, sans avoir à en lister tous les éléments. Par exemple, le jeu
          contenant les trois chaînes de caractères
            <mentioned>Handel</mentioned>, <mentioned>Händel</mentioned>, et
            <mentioned>Haendel</mentioned> peut être décrit comme le modèle
            <code>H(ä|ae?)ndel</code> (ou on peut dire que
            <code>H(ä|ae?)ndel</code>
          <term>équivaut à</term> chacune des trois chaînes)</quote>
        <ref target="http://fr.wikipedia.org/wiki/Expression_rationnelle">wikipedia</ref>
        <ref target="http://en.wikipedia.org/wiki/Regular_expression#Basic_concepts">wikipedia</ref>
      </cit>
    </p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines attribute values which
    are expressed as a regular expression.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">정규표현으로 표시된 속성 값을 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍以固定方法表示</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">正規表現を属性値として定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs
    d'attributs exprimant une expression régulière.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una gama de valores de
    atributos expresados como una expresión regular.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce una gamma di valori di
    attributi rappresentati come espressione regolare</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <dataRef name="token"/>
  </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.pattern-remarks" versionDate="2013-03-18" xml:lang="en">
    <p>
      <cit rend="display">
        <quote>A regular expression, often called a <term>pattern</term>, is an
          expression that describes a set of strings. They are usually used to
          give a concise description of a set, without having to list all
          elements. For example, the set containing the three strings
            <mentioned>Handel</mentioned>, <mentioned>Händel</mentioned>, and
            <mentioned>Haendel</mentioned> can be described by the pattern
            <code>H(ä|ae?)ndel</code> (or alternatively, it is said that the
          pattern <code>H(ä|ae?)ndel</code>
          <term>matches</term> each of the three strings)</quote>
        <ref target="http://en.wikipedia.org/wiki/Regular_expression#Basic_concepts">Wikipedia </ref>
      </cit>
    </p>
    <p>This TEI datatype is mapped to the XSD token datatype, and may therefore
      contain any string of characters. However, it is recommended that the
      value used conform to the particular flavour of regular expression syntax
      supported by XSD Schema. </p>
    <!-- http://www.regular-expressions.info/xml.html -->
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.pattern-remarks" xml:lang="ja" versionDate="2024-08-08">
    <p>
      <cit rend="display"><quote>正規表現は、よく<term>パタン/パターン</term>ともいわれるもので、文字列の集合を記述するための表現方法である。一般には、簡潔な表現で、 すべての要素を列挙することなく集合を表現するために使用される。例えば、三つの文字列<mentioned>Handel</mentioned>、<mentioned>Händel</mentioned>、<mentioned>Haendel</mentioned>〔訳注：これらはすべて「ヘンデル」の異表記〕を、一つのパタン<code>H(ä|ae?)ndel</code>で記述することができる（あるいは、<code>H(ä|ae?)ndel</code>は、三つの文字列のいずれにも<term>マッチする</term>といわれる）。</quote><ref target="http://en.wikipedia.org/wiki/Regular_expression#Basic_concepts">wikipedia</ref></cit>
    </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.pattern-remarks" versionDate="2009-05-25" xml:lang="fr">
    <p>
      <cit>
        <quote>Une expression régulière, souvent appelée <term>modèle</term>,
          est une expression qui décrit un jeu de chaînes de caractères. Elles
          sont généralement utilisées pour donner une brève description d'un
          jeu, sans avoir à en lister tous les éléments. Par exemple, le jeu
          contenant les trois chaînes de caractères
            <mentioned>Handel</mentioned>, <mentioned>Händel</mentioned>, et
            <mentioned>Haendel</mentioned> peut être décrit comme le modèle
            <code>H(ä|ae?)ndel</code> (ou on peut dire que
            <code>H(ä|ae?)ndel</code>
          <term>équivaut à</term> chacune des trois chaînes)</quote>
        <ref target="http://fr.wikipedia.org/wiki/Expression_rationnelle">wikipedia</ref>
        <ref target="http://en.wikipedia.org/wiki/Regular_expression#Basic_concepts">wikipedia</ref>
      </cit>
    </p>
  </remarks>
```

^b11

