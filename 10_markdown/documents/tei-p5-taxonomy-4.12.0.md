---
type: representation
source-type: document
source: '[[00_sources/tei-p5-taxonomy-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 taxonomy
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/taxonomy.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# taxonomy

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9827. Git blob: `ca125d20715711f63cf4152fd3b12f28702843a1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-taxonomy" ident="taxonomy">
  <gloss versionDate="2009-05-04" xml:lang="en">taxonomy</gloss>
  <gloss versionDate="2009-05-04" xml:lang="fr">taxinomie</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Taxonomie</gloss>
  <desc versionDate="2011-11-02" xml:lang="en">defines a typology either implicitly, by means of a bibliographic
  citation, or explicitly by a structured taxonomy.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">définit une typologie 
  soit implicitement au moyen d’une référence bibliographique, soit explicitement au moyen d’une
  taxinomie structurée.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">서지 정보 인용으로 비명시적으로 또는 구조화된 분류법으로 명시적으로 텍스트를 분류하는 유형을 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義文件分類的類型學，可以是潛在地以書目資料的方式，或是明確地以結構分類法的方式來分類。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストの分類法を、書誌情報を参照したり、または構造化された分類法を 示すことで、定義する。</desc>
  <desc versionDate="2016-11-17" xml:lang="de">definiert eine Typologie entweder implizit durch einen bibliografischen Verweis oder explizit durch eine strukturierte Taxonomie.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una tipología o
  implícitamente, mediante una cita bibliográfica, o explícitamente, mediante una taxonomía
  estructurada.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce una tipologia o
  in modo implicito, usando una citazione bibliograficha, o in modo esplicito attraverso una
  tassonomia strutturata.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
  <content>
    <alternate>
      <!-- We'd like the following clause to be a simple one: -->
      <!-- ( a*, b+ ) | ( a+, b* ) -->
      <!-- where: -->
      <!--   'a' = (descLike|equiv|gloss), and -->
      <!--   'b' = (category|taxonomy) -->
      <!-- but that is non-deterministic or ambigious. Thus we -->
      <!-- rewrite it as the mildly more confusing -->
      <!-- ( b+ | ( a+, b* ) ) -->
      <alternate>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="category"/>
          <elementRef key="taxonomy"/>
        </alternate>
        <sequence>
          <alternate minOccurs="1" maxOccurs="unbounded">
            <classRef key="model.descLike" minOccurs="1" maxOccurs="1"/>
            <elementRef key="equiv" minOccurs="1" maxOccurs="1"/>
            <elementRef key="gloss" minOccurs="1" maxOccurs="1"/>
          </alternate>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="category"/>
            <elementRef key="taxonomy"/>
          </alternate>
        </sequence>
      </alternate>
      <sequence>
        <classRef key="model.biblLike"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="category"/>
          <elementRef key="taxonomy"/>
        </alternate>
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-ra">
      <taxonomy xml:id="tax.b">
        <bibl>Brown Corpus</bibl>
        <category xml:id="tax.b.a">
          <catDesc>Press Reportage</catDesc>
          <category xml:id="tax.b.a1">
            <catDesc>Daily</catDesc>
          </category>
          <category xml:id="tax.b.a2">
            <catDesc>Sunday</catDesc>
          </category>
          <category xml:id="tax.b.a3">
            <catDesc>National</catDesc>
          </category>
          <category xml:id="tax.b.a4">
            <catDesc>Provincial</catDesc>
          </category>
          <category xml:id="tax.b.a5">
            <catDesc>Political</catDesc>
          </category>
          <category xml:id="tax.b.a6">
            <catDesc>Sports</catDesc>
          </category>
        </category>
        <category xml:id="tax.b.d">
          <catDesc>Religion</catDesc>
          <category xml:id="tax.b.d1">
            <catDesc>Books</catDesc>
          </category>
          <category xml:id="tax.b.d2">
            <catDesc>Periodicals and tracts</catDesc>
          </category>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-zq">
      <taxonomy xml:id="fr_tax.a">
        <category xml:id="fr_tax.a.a">
          <catDesc>littérature</catDesc>
        </category>
        <category xml:id="fr_tax.a.a.1">
          <catDesc>Drame bourgeois</catDesc>
        </category>
        <category xml:id="fr_tax.a.a.1.α">
          <catDesc>Comédie larmoyante</catDesc>
        </category>
        <category xml:id="fr_tax.a.b">
          <catDesc>Correspondance</catDesc>
        </category>
        <category xml:id="fr_tax.a.b.1.a">
          <catDesc>Dernières lettres</catDesc>
        </category>
        <category xml:id="fr_tax.a.c.">
          <catDesc>Littérature européenne -- 16e siècle</catDesc>
        </category>
        <category xml:id="fr_tax.a.c.1">
          <catDesc>Satire de la Renaissance </catDesc>
        </category>
        <category xml:id="fr_tax.a.d">
          <catDesc>Récits de voyage</catDesc>
        </category>
        <category xml:id="fr_tax.a.d.1">
          <catDesc>Récits de la mer </catDesc>
        </category>
      </taxonomy>
      <bibl>indexation selon le système d'indexation RAMEAU, géré par la Bibliothèque nationale de
      France</bibl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-ft">
      <taxonomy xml:id="zh-tw_tax.b">
        <bibl>布朗集</bibl>
        <category xml:id="zh-tw_tax.b.a">
          <catDesc>媒體採訪報導</catDesc>
          <category xml:id="zh-tw_tax.b.a1">
            <catDesc>日報</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a2">
            <catDesc>週日</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a3">
            <catDesc>全國性</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a4">
            <catDesc>地方性</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a5">
            <catDesc>政治</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a6">
            <catDesc>體育</catDesc>
          </category>
        </category>
        <category xml:id="zh-tw_tax.b.d">
          <catDesc>宗教</catDesc>
          <category xml:id="zh-tw_tax.b.d1">
            <catDesc>藝文</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.d2">
            <catDesc>期刊與短文</catDesc>
          </category>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-em">
      <taxonomy>
        <category xml:id="literature">
          <catDesc>Literature</catDesc>
          <category xml:id="poetry">
            <catDesc>Poetry</catDesc>
            <category xml:id="sonnet">
              <catDesc>Sonnet</catDesc>
              <category xml:id="shakesSonnet">
                <catDesc>Shakespearean Sonnet</catDesc>
              </category>
              <category xml:id="petraSonnet">
                <catDesc>Petrarchan Sonnet</catDesc>
              </category>
            </category>
            <category xml:id="haiku">
              <catDesc>Haiku</catDesc>
            </category>
          </category>
          <category xml:id="drama">
            <catDesc>Drama</catDesc>
          </category>
        </category>
        <category xml:id="meter">
          <catDesc>Metrical Categories</catDesc>
          <category xml:id="feet">
            <catDesc>Metrical Feet</catDesc>
            <category xml:id="iambic">
              <catDesc>Iambic</catDesc>
            </category>
            <category xml:id="trochaic">
              <catDesc>trochaic</catDesc>
            </category>
          </category>
          <category xml:id="feetNumber">
            <catDesc>Number of feet</catDesc>
            <category xml:id="pentameter">
              <catDesc>&gt;Pentameter</catDesc>
            </category>
            <category xml:id="tetrameter">
              <catDesc>&gt;Tetrameter</catDesc>
            </category>
          </category>
        </category>
      </taxonomy>
      <!-- elsewhere in document -->
      <lg ana="#shakesSonnet #iambic #pentameter">
        <l>Shall I compare thee to a summer's day</l>
        <!-- ... -->
      </lg>
    </egXML>
  </exemplum>
  <remarks ident="taxonomy-remarks" versionDate="2015-10-31" xml:lang="en">
    <p>Nested taxonomies are common in many fields, so the
    <gi>taxonomy</gi> element can be nested.</p>
  </remarks>
  <remarks ident="taxonomy-remarks" versionDate="2016-11-17" xml:lang="de">
    <p>
      Da in vielen Bereichen verschachtelte Taxonomien gängig sind, kann das <gi>taxonomy</gi>-Element verschachtelt werden.
    </p>
  </remarks>
  <listRef>
    <ptr target="#HD55"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-05-04" xml:lang="en">taxonomy</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-05-04" xml:lang="fr">taxinomie</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Taxonomie</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-02" xml:lang="en">defines a typology either implicitly, by means of a bibliographic
  citation, or explicitly by a structured taxonomy.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">définit une typologie 
  soit implicitement au moyen d’une référence bibliographique, soit explicitement au moyen d’une
  taxinomie structurée.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">서지 정보 인용으로 비명시적으로 또는 구조화된 분류법으로 명시적으로 텍스트를 분류하는 유형을 정의한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義文件分類的類型學，可以是潛在地以書目資料的方式，或是明確地以結構分類法的方式來分類。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストの分類法を、書誌情報を参照したり、または構造化された分類法を 示すことで、定義する。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">definiert eine Typologie entweder implizit durch einen bibliografischen Verweis oder explizit durch eine strukturierte Taxonomie.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una tipología o
  implícitamente, mediante una cita bibliográfica, o explícitamente, mediante una taxonomía
  estructurada.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce una tipologia o
  in modo implicito, usando una citazione bibliograficha, o in modo esplicito attraverso una
  tassonomia strutturata.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <!-- We'd like the following clause to be a simple one: -->
      <!-- ( a*, b+ ) | ( a+, b* ) -->
      <!-- where: -->
      <!--   'a' = (descLike|equiv|gloss), and -->
      <!--   'b' = (category|taxonomy) -->
      <!-- but that is non-deterministic or ambigious. Thus we -->
      <!-- rewrite it as the mildly more confusing -->
      <!-- ( b+ | ( a+, b* ) ) -->
      <alternate>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="category"/>
          <elementRef key="taxonomy"/>
        </alternate>
        <sequence>
          <alternate minOccurs="1" maxOccurs="unbounded">
            <classRef key="model.descLike" minOccurs="1" maxOccurs="1"/>
            <elementRef key="equiv" minOccurs="1" maxOccurs="1"/>
            <elementRef key="gloss" minOccurs="1" maxOccurs="1"/>
          </alternate>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="category"/>
            <elementRef key="taxonomy"/>
          </alternate>
        </sequence>
      </alternate>
      <sequence>
        <classRef key="model.biblLike"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="category"/>
          <elementRef key="taxonomy"/>
        </alternate>
      </sequence>
    </alternate>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-ra">
      <taxonomy xml:id="tax.b">
        <bibl>Brown Corpus</bibl>
        <category xml:id="tax.b.a">
          <catDesc>Press Reportage</catDesc>
          <category xml:id="tax.b.a1">
            <catDesc>Daily</catDesc>
          </category>
          <category xml:id="tax.b.a2">
            <catDesc>Sunday</catDesc>
          </category>
          <category xml:id="tax.b.a3">
            <catDesc>National</catDesc>
          </category>
          <category xml:id="tax.b.a4">
            <catDesc>Provincial</catDesc>
          </category>
          <category xml:id="tax.b.a5">
            <catDesc>Political</catDesc>
          </category>
          <category xml:id="tax.b.a6">
            <catDesc>Sports</catDesc>
          </category>
        </category>
        <category xml:id="tax.b.d">
          <catDesc>Religion</catDesc>
          <category xml:id="tax.b.d1">
            <catDesc>Books</catDesc>
          </category>
          <category xml:id="tax.b.d2">
            <catDesc>Periodicals and tracts</catDesc>
          </category>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-zq">
      <taxonomy xml:id="fr_tax.a">
        <category xml:id="fr_tax.a.a">
          <catDesc>littérature</catDesc>
        </category>
        <category xml:id="fr_tax.a.a.1">
          <catDesc>Drame bourgeois</catDesc>
        </category>
        <category xml:id="fr_tax.a.a.1.α">
          <catDesc>Comédie larmoyante</catDesc>
        </category>
        <category xml:id="fr_tax.a.b">
          <catDesc>Correspondance</catDesc>
        </category>
        <category xml:id="fr_tax.a.b.1.a">
          <catDesc>Dernières lettres</catDesc>
        </category>
        <category xml:id="fr_tax.a.c.">
          <catDesc>Littérature européenne -- 16e siècle</catDesc>
        </category>
        <category xml:id="fr_tax.a.c.1">
          <catDesc>Satire de la Renaissance </catDesc>
        </category>
        <category xml:id="fr_tax.a.d">
          <catDesc>Récits de voyage</catDesc>
        </category>
        <category xml:id="fr_tax.a.d.1">
          <catDesc>Récits de la mer </catDesc>
        </category>
      </taxonomy>
      <bibl>indexation selon le système d'indexation RAMEAU, géré par la Bibliothèque nationale de
      France</bibl>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-ft">
      <taxonomy xml:id="zh-tw_tax.b">
        <bibl>布朗集</bibl>
        <category xml:id="zh-tw_tax.b.a">
          <catDesc>媒體採訪報導</catDesc>
          <category xml:id="zh-tw_tax.b.a1">
            <catDesc>日報</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a2">
            <catDesc>週日</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a3">
            <catDesc>全國性</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a4">
            <catDesc>地方性</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a5">
            <catDesc>政治</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.a6">
            <catDesc>體育</catDesc>
          </category>
        </category>
        <category xml:id="zh-tw_tax.b.d">
          <catDesc>宗教</catDesc>
          <category xml:id="zh-tw_tax.b.d1">
            <catDesc>藝文</catDesc>
          </category>
          <category xml:id="zh-tw_tax.b.d2">
            <catDesc>期刊與短文</catDesc>
          </category>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-taxonomy-egXML-em">
      <taxonomy>
        <category xml:id="literature">
          <catDesc>Literature</catDesc>
          <category xml:id="poetry">
            <catDesc>Poetry</catDesc>
            <category xml:id="sonnet">
              <catDesc>Sonnet</catDesc>
              <category xml:id="shakesSonnet">
                <catDesc>Shakespearean Sonnet</catDesc>
              </category>
              <category xml:id="petraSonnet">
                <catDesc>Petrarchan Sonnet</catDesc>
              </category>
            </category>
            <category xml:id="haiku">
              <catDesc>Haiku</catDesc>
            </category>
          </category>
          <category xml:id="drama">
            <catDesc>Drama</catDesc>
          </category>
        </category>
        <category xml:id="meter">
          <catDesc>Metrical Categories</catDesc>
          <category xml:id="feet">
            <catDesc>Metrical Feet</catDesc>
            <category xml:id="iambic">
              <catDesc>Iambic</catDesc>
            </category>
            <category xml:id="trochaic">
              <catDesc>trochaic</catDesc>
            </category>
          </category>
          <category xml:id="feetNumber">
            <catDesc>Number of feet</catDesc>
            <category xml:id="pentameter">
              <catDesc>&gt;Pentameter</catDesc>
            </category>
            <category xml:id="tetrameter">
              <catDesc>&gt;Tetrameter</catDesc>
            </category>
          </category>
        </category>
      </taxonomy>
      <!-- elsewhere in document -->
      <lg ana="#shakesSonnet #iambic #pentameter">
        <l>Shall I compare thee to a summer's day</l>
        <!-- ... -->
      </lg>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="taxonomy-remarks" versionDate="2015-10-31" xml:lang="en">
    <p>Nested taxonomies are common in many fields, so the
    <gi>taxonomy</gi> element can be nested.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="taxonomy-remarks" versionDate="2016-11-17" xml:lang="de">
    <p>
      Da in vielen Bereichen verschachtelte Taxonomien gängig sind, kann das <gi>taxonomy</gi>-Element verschachtelt werden.
    </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD55"/>
  </listRef>
```

^b20

