---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sponsor-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sponsor
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sponsor.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sponsor

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4573. Git blob: `e2140391db9de0e1929a40fd6f8e78a54a9d9c93`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-sponsor" ident="sponsor">
  <gloss versionDate="2007-06-12" xml:lang="en">sponsor</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">commanditaire</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Förderer</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies the name of a sponsoring organization or institution.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">indique le nom d’une institution ou d’un organisme partenaires.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">후원 조직 또는 기관의 이름을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明贊助的組織或機構名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">支援を行う組織や団体の名前を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">gibt den Namen einer Organisation oder Institution an, die als Förderer auftritt.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica el nombre de la organización o institución responsable.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica il nome di un'organizzazione o istituzzione finanziatrice.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sponsor-egXML-nr">
      <sponsor>Association for Computers and the Humanities</sponsor>
      <sponsor>Association for Computational Linguistics</sponsor>
      <sponsor ref="http://www.allc.org/">Association for Literary and Linguistic Computing</sponsor>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sponsor-egXML-ga">
      <sponsor>Centre national de la recherche scientifique</sponsor>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sponsor-egXML-vv">
      <sponsor>香港影評人協會</sponsor>
      <sponsor>香港教育專業人員協會</sponsor>
      <sponsor>香港青年協會</sponsor>
    </egXML>
  </exemplum>
  <remarks ident="sponsor-remarks" versionDate="2016-11-17" xml:lang="en">
    <p>Sponsors give their intellectual authority to a project; they are to be distinguished from
        <term>funders</term> (see element <gi>funder</gi>), who provide the funding but do not necessarily take intellectual
      responsibility.</p>
  </remarks>
  <remarks ident="sponsor-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les commanditaires apportent leur caution intellectuelle à un projet ; ils doivent être
      distingués des <term>financeurs</term>, qui  apportent de financement mais n'ont pas
      nécessairement une responsabilité intellectuelle.</p>
  </remarks>
  <remarks ident="sponsor-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los patrocinadores dan su autoridad intelectual a un proyecto; deben ser distinguidos de los
        <term>proveedores de fondos</term>, que proporcionan la financiación pero no asumen
      necesariamente la responsabilidad intelectual.</p>
  </remarks>
  <remarks ident="sponsor-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 支援者は、プロジェクトに知的な責任を持つ。支援者は<term>資金提供者 </term>と区別されるべきである。資金提供者は、資金を提供するが、必 ずしも知的な責任を持つとは限らない。
    </p>
  </remarks>
  <remarks ident="sponsor-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>
          Förderer übernehmen die inhaltliche Verantwortung für ein Projekt. Sie sind zu unterscheiden von 
          <term>Geldgebern</term> (siehe <gi>funder</gi>-Element), die nicht notwendigerweise die inhaltliche Verantwortung oder Betreuung übernehmen.
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
<gloss versionDate="2007-06-12" xml:lang="en">sponsor</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">commanditaire</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Förderer</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the name of a sponsoring organization or institution.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique le nom d’une institution ou d’un organisme partenaires.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">후원 조직 또는 기관의 이름을 명시한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明贊助的組織或機構名稱。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">支援を行う組織や団体の名前を示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">gibt den Namen einer Organisation oder Institution an, die als Förderer auftritt.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el nombre de la organización o institución responsable.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il nome di un'organizzazione o istituzzione finanziatrice.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.respLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sponsor-egXML-nr">
      <sponsor>Association for Computers and the Humanities</sponsor>
      <sponsor>Association for Computational Linguistics</sponsor>
      <sponsor ref="http://www.allc.org/">Association for Literary and Linguistic Computing</sponsor>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sponsor-egXML-ga">
      <sponsor>Centre national de la recherche scientifique</sponsor>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sponsor-egXML-vv">
      <sponsor>香港影評人協會</sponsor>
      <sponsor>香港教育專業人員協會</sponsor>
      <sponsor>香港青年協會</sponsor>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="sponsor-remarks" versionDate="2016-11-17" xml:lang="en">
    <p>Sponsors give their intellectual authority to a project; they are to be distinguished from
        <term>funders</term> (see element <gi>funder</gi>), who provide the funding but do not necessarily take intellectual
      responsibility.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="sponsor-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les commanditaires apportent leur caution intellectuelle à un projet ; ils doivent être
      distingués des <term>financeurs</term>, qui  apportent de financement mais n'ont pas
      nécessairement une responsabilité intellectuelle.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="sponsor-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los patrocinadores dan su autoridad intelectual a un proyecto; deben ser distinguidos de los
        <term>proveedores de fondos</term>, que proporcionan la financiación pero no asumen
      necesariamente la responsabilidad intelectual.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="sponsor-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 支援者は、プロジェクトに知的な責任を持つ。支援者は<term>資金提供者 </term>と区別されるべきである。資金提供者は、資金を提供するが、必 ずしも知的な責任を持つとは限らない。
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="sponsor-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>
          Förderer übernehmen die inhaltliche Verantwortung für ein Projekt. Sie sind zu unterscheiden von 
          <term>Geldgebern</term> (siehe <gi>funder</gi>-Element), die nicht notwendigerweise die inhaltliche Verantwortung oder Betreuung übernehmen.
      </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD21"/>
  </listRef>
```

^b22

