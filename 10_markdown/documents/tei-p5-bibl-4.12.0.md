---
type: representation
source-type: document
source: '[[00_sources/tei-p5-bibl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 bibl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/bibl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# bibl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7482. Git blob: `cf97d3899cabf7cf892f99d2a965b5c1bd4b7d45`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-bibl" ident="bibl">
  <gloss versionDate="2005-01-14" xml:lang="en">bibliographic citation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">서지 인용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">書目資料</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">référence bibliographique.</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">cita bibliográfica.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">citazione bibliografica</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">bibliografische Angabe</gloss>
    <gloss versionDate="2023-09-21" xml:lang="ja">典拠情報の明示</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a loosely-structured bibliographic citation of which the sub-components may or may
    not be explicitly tagged.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하위 성분이 명시적으로 구분된 또는 그렇지 않은 덜 구조화된 서지 인용을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含結構零散的書目資料，其中次要元件不一定會明確標記。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">完全な構造を持たない典拠情報の引用を表す。各構成要素はタグ付けされていてもいなくてもよい。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une référence bibliographique faiblement
    structurée dans laquelle les sous-composants peuvent ou non être explicitement balisés.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una cita bibliográfica estructurada libremente,
    los componentes de la cual pueden nohaber sido etiquetados explícitamente.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una citazione bibliografica strutturata
    liberamente i cui componeneti potrebbero o meno essere codificati esplicitamente.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält eine lose strukturierte bibliografische Angabe, in der einzelne Komponenten explizit
    ausgezeichnet sein können.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.docStatus"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblLike"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.highlighted"/>
      <classRef key="model.pPart.data"/>
      <classRef key="model.pPart.edit"/>
      <classRef key="model.segLike"/>
      <classRef key="model.ptrLike"/>
      <classRef key="model.biblPart"/>
      <classRef key="model.global"/>
    </alternate>    
  </content>
  <constraintSpec ident="bibl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:bibl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-sb">
      <bibl>Blain, Clements and Grundy: Feminist Companion to Literature in English (Yale,
      1990)</bibl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-hh">
      <bibl>Mazelier, Roger : Gérard de Nerval et l’Humour divin, Le Mesnil Saint-Denis,
        1995.</bibl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-fi">
      <bibl><title level="a">L'Enracinement</title><author>Simone Weil</author>, <title>Prélude à une déclaration des devoirs envers l'être
            humain </title>. <publisher>Gallimard</publisher><date>1968</date>.</bibl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-nt">
      <bibl>蕭兵，《神話學引論》。台北：文津，2001。</bibl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-lj">
      <bibl><title level="a">我的從影經過</title>。收錄於 <author>王漢倫</author>，<title>中國無聲電影</title>.
          <publisher>北京：中國電影</publisher>
            <date>1996</date>。</bibl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-es">
      <bibl><title level="a">The Interesting story of the Children in the Wood</title>. In
          <author>Victor E Neuberg</author>, <title>The Penny Histories</title>.
          <publisher>OUP</publisher><date>1968</date>. </bibl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-tn">
      <bibl type="article" subtype="book_chapter" xml:id="carlin_2003"><author><name><surname>Carlin</surname>
          (<forename>Claire</forename>)</name></author>,
        <title level="a">The Staging of Impotence : France’s last
          congrès</title> dans
        <bibl type="monogr"><title level="m">Theatrum mundi : studies in honor of Ronald W.
            Tobin</title>, éd.
          <editor><name><forename>Claire</forename><surname>Carlin</surname></name></editor> et
          <editor><name><forename>Kathleen</forename><surname>Wine</surname></name></editor>,
          <pubPlace>Charlottesville, Va.</pubPlace>,
          <publisher>Rookwood Press</publisher>,
          <date when="2003">2003</date>.
        </bibl>
         </bibl>
    </egXML>
  </exemplum>
  <remarks ident="bibl-remarks" versionDate="2017-06-13" xml:lang="en">
    <p rend="dataDesc">Contains <term>phrase-level</term> elements, together with any combination of elements from the
      <ident type="class">model.biblPart</ident> class</p>
  </remarks>
  <remarks ident="bibl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément contient des éléments de type expression, ainsi qu'un jeu
      d'éléments de la classe <ident type="class">model.biblPart</ident>.</p>
  </remarks>
  <remarks ident="bibl-remarks" versionDate="2023-09-21" xml:lang="ja">
    <p rend="dataDesc"><term>フレーズレベル</term>要素と、<ident type="class">model.biblPart</ident>クラスの要素の任意の組み合わせを含む。</p>
  </remarks>
  <remarks ident="bibl-remarks" versionDate="2017-06-13" xml:lang="de">
    <p rend="dataDesc">Enthält <term>Phrasen-Level</term>-Elemente, zusammen mit einer beliebigen Kombination von
      Elementen der <ident type="class">model.biblPart</ident>-Klasse</p>
  </remarks>
  <listRef>
    <ptr target="#COBITY"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">bibliographic citation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">서지 인용</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">書目資料</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">référence bibliographique.</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">cita bibliográfica.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">citazione bibliografica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">bibliografische Angabe</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-09-21" xml:lang="ja">典拠情報の明示</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a loosely-structured bibliographic citation of which the sub-components may or may
    not be explicitly tagged.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하위 성분이 명시적으로 구분된 또는 그렇지 않은 덜 구조화된 서지 인용을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含結構零散的書目資料，其中次要元件不一定會明確標記。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">完全な構造を持たない典拠情報の引用を表す。各構成要素はタグ付けされていてもいなくてもよい。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une référence bibliographique faiblement
    structurée dans laquelle les sous-composants peuvent ou non être explicitement balisés.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una cita bibliográfica estructurada libremente,
    los componentes de la cual pueden nohaber sido etiquetados explícitamente.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una citazione bibliografica strutturata
    liberamente i cui componeneti potrebbero o meno essere codificati esplicitamente.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält eine lose strukturierte bibliografische Angabe, in der einzelne Komponenten explizit
    ausgezeichnet sein können.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.docStatus"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblLike"/>
    <memberOf key="model.biblPart"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.highlighted"/>
      <classRef key="model.pPart.data"/>
      <classRef key="model.pPart.edit"/>
      <classRef key="model.segLike"/>
      <classRef key="model.ptrLike"/>
      <classRef key="model.biblPart"/>
      <classRef key="model.global"/>
    </alternate>    
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="bibl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:bibl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-sb">
      <bibl>Blain, Clements and Grundy: Feminist Companion to Literature in English (Yale,
      1990)</bibl>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-hh">
      <bibl>Mazelier, Roger : Gérard de Nerval et l’Humour divin, Le Mesnil Saint-Denis,
        1995.</bibl>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-fi">
      <bibl><title level="a">L'Enracinement</title><author>Simone Weil</author>, <title>Prélude à une déclaration des devoirs envers l'être
            humain </title>. <publisher>Gallimard</publisher><date>1968</date>.</bibl>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-nt">
      <bibl>蕭兵，《神話學引論》。台北：文津，2001。</bibl>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-lj">
      <bibl><title level="a">我的從影經過</title>。收錄於 <author>王漢倫</author>，<title>中國無聲電影</title>.
          <publisher>北京：中國電影</publisher>
            <date>1996</date>。</bibl>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-es">
      <bibl><title level="a">The Interesting story of the Children in the Wood</title>. In
          <author>Victor E Neuberg</author>, <title>The Penny Histories</title>.
          <publisher>OUP</publisher><date>1968</date>. </bibl>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-bibl-egXML-tn">
      <bibl type="article" subtype="book_chapter" xml:id="carlin_2003"><author><name><surname>Carlin</surname>
          (<forename>Claire</forename>)</name></author>,
        <title level="a">The Staging of Impotence : France’s last
          congrès</title> dans
        <bibl type="monogr"><title level="m">Theatrum mundi : studies in honor of Ronald W.
            Tobin</title>, éd.
          <editor><name><forename>Claire</forename><surname>Carlin</surname></name></editor> et
          <editor><name><forename>Kathleen</forename><surname>Wine</surname></name></editor>,
          <pubPlace>Charlottesville, Va.</pubPlace>,
          <publisher>Rookwood Press</publisher>,
          <date when="2003">2003</date>.
        </bibl>
         </bibl>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="bibl-remarks" versionDate="2017-06-13" xml:lang="en">
    <p rend="dataDesc">Contains <term>phrase-level</term> elements, together with any combination of elements from the
      <ident type="class">model.biblPart</ident> class</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="bibl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément contient des éléments de type expression, ainsi qu'un jeu
      d'éléments de la classe <ident type="class">model.biblPart</ident>.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="bibl-remarks" versionDate="2023-09-21" xml:lang="ja">
    <p rend="dataDesc"><term>フレーズレベル</term>要素と、<ident type="class">model.biblPart</ident>クラスの要素の任意の組み合わせを含む。</p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="bibl-remarks" versionDate="2017-06-13" xml:lang="de">
    <p rend="dataDesc">Enthält <term>Phrasen-Level</term>-Elemente, zusammen mit einer beliebigen Kombination von
      Elementen der <ident type="class">model.biblPart</ident>-Klasse</p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBITY"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b31

