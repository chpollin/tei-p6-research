---
type: representation
source-type: document
source: '[[00_sources/tei-p5-funder-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 funder
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/funder.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# funder

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5229. Git blob: `e4af657def039f41e866ab5031a9fc1a3c849f16`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-funder" ident="funder">
  <gloss versionDate="2007-07-04" xml:lang="en">funding body</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">financeur</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">재정 지원 조직체</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">資助者</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Geldgeber</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">responsable de la financiación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">finanziatore</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies the name of an individual, institution, or organization responsible for the funding of a project or text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">désigne le nom d’une personne ou d’un organisme responsable du financement d’un projet ou d’un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">프로젝트 또는 텍스트의 재정 지원 책임을 지는 개인, 기관, 조직의 이름을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明負責資助一項計畫或文件製作的個人、機構或組織名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストやプロジェクトの資金提供に責任を持つ個人、団体、組織の名前を 示す。</desc>
  <desc versionDate="2016-11-17" xml:lang="de">gibt den Namen einer Einzelperson, Institution oder Organisation an, die für die Finanzierung eines Projekts oder Textes verantwortlich ist.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del individuo, la institución o la organización responsable de la financiación de un proyecto o de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica il nome di un individuo, istituzione o organizzazione responsabile del finanziamento di un progetto o testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.respLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-funder-egXML-ch">
      <funder>The National Endowment for the Humanities, an independent federal agency</funder>
      <funder>Directorate General XIII of the Commission of the European Communities</funder>
      <funder>The Andrew W. Mellon Foundation</funder>
      <funder>The Social Sciences and Humanities Research Council of Canada</funder>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-funder-egXML-dr">
      <funder>Ministère de l'Enseignement supérieur et de la Recherche</funder>
      <funder>Conseil général de Meurthe-et-Moselle </funder>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-funder-egXML-zp">
      <funder>行政院國家科學委員會</funder>
      <funder>國家圖書館</funder>
      <funder>國立故宮博物院</funder>
      <funder>國立自然科學博物館</funder>
    </egXML>
  </exemplum>
  <remarks ident="funder-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Funders provide financial support for a project; they are distinct from
      <term>sponsors</term> (see element <gi>sponsor</gi>), who provide intellectual support and authority.</p>
  </remarks>
  <remarks ident="funder-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les financeurs apportent un soutien financier au projet ; ils se distinguent des
        <term>commanditaires</term>, qui apportent une caution , une autorité intellectuelle.</p>
  </remarks>
  <remarks ident="funder-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los proveedores de fondos proporcionan la ayuda financiera para un proyecto; son distintos de
      los <term>patrocinadores</term>, que proporciona la ayuda y la autoridad intelectual.</p>
  </remarks>
  <remarks ident="funder-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の資金提供者とは、プロジェクトへの資金を支援するものである。 知的支援や責任を持つ人物示す要素<term>sponsors</term>は異なる。 </p>
  </remarks>
  <remarks ident="funder-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>
          Die Geldgeber finanzieren das Projekt. Sie sind zu unterscheiden von den <term>Förderern</term> (siehe <gi>sponsor</gi>-Element), die das Projekt intellektuell und mit fachlicher Autorität unterstützen.      
      </p>
  </remarks>
  <listRef>
    <ptr target="#HD21"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">funding body</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">financeur</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">재정 지원 조직체</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">資助者</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Geldgeber</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">responsable de la financiación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">finanziatore</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the name of an individual, institution, or organization responsible for the funding of a project or text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">désigne le nom d’une personne ou d’un organisme responsable du financement d’un projet ou d’un texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">프로젝트 또는 텍스트의 재정 지원 책임을 지는 개인, 기관, 조직의 이름을 명시한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明負責資助一項計畫或文件製作的個人、機構或組織名稱。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストやプロジェクトの資金提供に責任を持つ個人、団体、組織の名前を 示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">gibt den Namen einer Einzelperson, Institution oder Organisation an, die für die Finanzierung eines Projekts oder Textes verantwortlich ist.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del individuo, la institución o la organización responsable de la financiación de un proyecto o de un texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il nome di un individuo, istituzione o organizzazione responsabile del finanziamento di un progetto o testo.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.respLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-funder-egXML-ch">
      <funder>The National Endowment for the Humanities, an independent federal agency</funder>
      <funder>Directorate General XIII of the Commission of the European Communities</funder>
      <funder>The Andrew W. Mellon Foundation</funder>
      <funder>The Social Sciences and Humanities Research Council of Canada</funder>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-funder-egXML-dr">
      <funder>Ministère de l'Enseignement supérieur et de la Recherche</funder>
      <funder>Conseil général de Meurthe-et-Moselle </funder>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-funder-egXML-zp">
      <funder>行政院國家科學委員會</funder>
      <funder>國家圖書館</funder>
      <funder>國立故宮博物院</funder>
      <funder>國立自然科學博物館</funder>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="funder-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Funders provide financial support for a project; they are distinct from
      <term>sponsors</term> (see element <gi>sponsor</gi>), who provide intellectual support and authority.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="funder-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les financeurs apportent un soutien financier au projet ; ils se distinguent des
        <term>commanditaires</term>, qui apportent une caution , une autorité intellectuelle.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="funder-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los proveedores de fondos proporcionan la ayuda financiera para un proyecto; son distintos de
      los <term>patrocinadores</term>, que proporciona la ayuda y la autoridad intelectual.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="funder-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の資金提供者とは、プロジェクトへの資金を支援するものである。 知的支援や責任を持つ人物示す要素<term>sponsors</term>は異なる。 </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="funder-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>
          Die Geldgeber finanzieren das Projekt. Sie sind zu unterscheiden von den <term>Förderern</term> (siehe <gi>sponsor</gi>-Element), die das Projekt intellektuell und mit fachlicher Autorität unterstützen.      
      </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD21"/>
  </listRef>
```

^b26

