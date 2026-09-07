---
type: representation
source-type: document
source: '[[00_sources/tei-p5-org-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 org
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/org.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# org

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5174. Git blob: `fe97b92af3f2991df88acb525566c43a62a4ab88`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-org" ident="org">
  <gloss versionDate="2007-07-04" xml:lang="en">organization</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">organisation</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
  <desc versionDate="2007-06-14" xml:lang="en">provides information
  about an identifiable organization such as a business, a tribe, or
  any other grouping of people.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">업무, 종족, 또는 사람들의 다른 종류의 그룹과 같은 식별 가능한 조직에 대한 정보를 제공한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">proporciona a la
  información sobre una organización identificable tal como un
  negocio, una tribu, o cualquier otro grupo de personas.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">特定可能な団体の情報を示す。例えば、会社、集団など、人の集まり。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">fournit des
  informations sur une organisation identifiable, telle qu'une
  entreprise, une tribu ou tout autre groupement de personnes.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">fornisce informazioni
  relative a un'organizzazione identificate come società, tribù, o
  qualsiasi altro raggruppamento di persone</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.personLike"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.labelLike"/>
          <classRef key="model.nameLike"/>
          <classRef key="model.placeLike"/>
          <classRef key="model.orgPart"/>
          <classRef key="model.milestoneLike"/>
        </alternate>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="linkGrp"/>
        <elementRef key="link"/>
      </alternate>
      <classRef key="model.personLike" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <attList>
    <attDef ident="role" usage="opt">
      <desc versionDate="2007-06-14" xml:lang="en">specifies a primary
      role or classification for the organization.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">조직에 대한 주요 역할 또는 분류를 명시한다.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該組織の、第一位の役割または分類を示す。</desc>
      <desc versionDate="2008-12-09" xml:lang="fr">spécifie le rôle
      principal ou la catégorie d'une organisation.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">establece el rol o
      la clasificación primaria de una persona.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">stabilisce il ruolo
      o la classificazione primaria di una persona</desc>
      <datatype maxOccurs="unbounded">
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <remarks ident="org-attr.role-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
        project, using arbitrary keywords such as <val>artist</val>,
        <val>employer</val>, <val>familyGroup</val>, or
        <val>politicalParty</val>, each of which should be associated
        with a definition. Such local definitions will typically be
        provided by a <gi>desc</gi> for each <gi>valItem</gi> element
        in the schema specification of the project's
        customization.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-org-egXML-qi">
      <org xml:id="JAMs">
        <orgName>Justified Ancients of Mummu</orgName>
        <desc>An underground anarchist collective spearheaded by
        <persName>Hagbard Celine</persName>, who fight the Illuminati
        from a golden submarine, the <name>Leif Ericson</name></desc>
        <bibl>
          <author>Robert Shea</author>
          <author>Robert Anton Wilson</author>
          <title>The Illuminatus! Trilogy</title>
        </bibl>
      </org>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#ND-org"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">organization</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">organisation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-06-14" xml:lang="en">provides information
  about an identifiable organization such as a business, a tribe, or
  any other grouping of people.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">업무, 종족, 또는 사람들의 다른 종류의 그룹과 같은 식별 가능한 조직에 대한 정보를 제공한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona a la
  información sobre una organización identificable tal como un
  negocio, una tribu, o cualquier otro grupo de personas.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">特定可能な団体の情報を示す。例えば、会社、集団など、人の集まり。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">fournit des
  informations sur une organisation identifiable, telle qu'une
  entreprise, une tribu ou tout autre groupement de personnes.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">fornisce informazioni
  relative a un'organizzazione identificate come società, tribù, o
  qualsiasi altro raggruppamento di persone</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.personLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.labelLike"/>
          <classRef key="model.nameLike"/>
          <classRef key="model.placeLike"/>
          <classRef key="model.orgPart"/>
          <classRef key="model.milestoneLike"/>
        </alternate>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="linkGrp"/>
        <elementRef key="link"/>
      </alternate>
      <classRef key="model.personLike" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-06-14" xml:lang="en">specifies a primary
      role or classification for the organization.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">조직에 대한 주요 역할 또는 분류를 명시한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該組織の、第一位の役割または分類を示す。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">spécifie le rôle
      principal ou la catégorie d'une organisation.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">establece el rol o
      la clasificación primaria de una persona.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">stabilisce il ruolo
      o la classificazione primaria di una persona</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded">
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="org-attr.role-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
        project, using arbitrary keywords such as <val>artist</val>,
        <val>employer</val>, <val>familyGroup</val>, or
        <val>politicalParty</val>, each of which should be associated
        with a definition. Such local definitions will typically be
        provided by a <gi>desc</gi> for each <gi>valItem</gi> element
        in the schema specification of the project's
        customization.</p>
      </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-org-egXML-qi">
      <org xml:id="JAMs">
        <orgName>Justified Ancients of Mummu</orgName>
        <desc>An underground anarchist collective spearheaded by
        <persName>Hagbard Celine</persName>, who fight the Illuminati
        from a golden submarine, the <name>Leif Ericson</name></desc>
        <bibl>
          <author>Robert Shea</author>
          <author>Robert Anton Wilson</author>
          <title>The Illuminatus! Trilogy</title>
        </bibl>
      </org>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#ND-org"/>
  </listRef>
```

^b23

