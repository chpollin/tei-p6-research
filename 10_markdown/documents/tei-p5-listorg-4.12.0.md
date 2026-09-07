---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listorg-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listOrg
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listOrg.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listOrg

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5268. Git blob: `f91ed3e1ce4ff4f235534d55635abceb36a77abd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-listOrg" ident="listOrg">
  <gloss versionDate="2007-07-04" xml:lang="en">list of organizations</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">조직 목록</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">lista de organizaciones</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">liste d'organisations</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">elenco delle organizzazioni</gloss>
  <desc versionDate="2008-04-29" xml:lang="en">contains a list of elements, each of which provides information about an identifiable
        organization.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">식별 가능한 조직에 관한 정보를 제공하며, 각각에 대한 기술 목록을 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una lista de descripciones, que proporciona a
        la información sobre una organización identificable.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">特定可能な団体に関する情報を示す解説のリストを示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient une liste d'éléments, chacun d'eux fournissant
        des informations sur une organisation identifiable.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una lista di descrizioni, ognuna delle quali
        fornisce informazioni relative a una determinata organizzazione</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
    <memberOf key="model.orgPart"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="org" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listOrg" minOccurs="1" maxOccurs="1"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <constraintSpec ident="listOrg-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listOrg"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listOrg-egXML-xb" source="#ND-eg-99">
      <listOrg>
        <head>Libyans</head>
        <org>
          <orgName>Adyrmachidae</orgName>
          <desc>These people have, in most points, the same customs as the Egyptians, but
                        use the costume of the Libyans. Their women wear on each leg a ring made of
                        bronze [...]</desc>
        </org>
        <org>
          <orgName>Nasamonians</orgName>
          <desc>In summer they leave their flocks and herds upon the sea-shore, and go up
                        the country to a place called Augila, where they gather the dates from the
                        palms [...]</desc>
        </org>
        <org>
          <orgName>Garamantians</orgName>
          <desc>[...] avoid all society or intercourse with their fellow-men, have no
                        weapon of war, and do not know how to defend themselves. [...]</desc>
          <!-- ... -->
        </org>
      </listOrg>
    </egXML>
  </exemplum>
  <!-- adapted from Herodotus - edition available at
        http://www.fordham.edu/halsall/ancient/herod-libya1.html -->
  <remarks ident="listOrg-remarks" versionDate="2007-09-13" xml:lang="en">
    <p rend="dataDesc">The type attribute may be used to distinguish lists of organizations of a
            particular type if convenient.</p>
  </remarks>
  <remarks ident="listOrg-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc">L'attribut type peut être utilisé pour établir des listes par type
            d'organisation si cela présente un intérêt.</p>
  </remarks>
  <remarks ident="listOrg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 属性typeは、特別な種類の組織を区別するために使われるかもしれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#NDORG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">list of organizations</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조직 목록</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">lista de organizaciones</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">liste d'organisations</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">elenco delle organizzazioni</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-04-29" xml:lang="en">contains a list of elements, each of which provides information about an identifiable
        organization.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">식별 가능한 조직에 관한 정보를 제공하며, 각각에 대한 기술 목록을 포함한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una lista de descripciones, que proporciona a
        la información sobre una organización identificable.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">特定可能な団体に関する情報を示す解説のリストを示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient une liste d'éléments, chacun d'eux fournissant
        des informations sur une organisation identifiable.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una lista di descrizioni, ognuna delle quali
        fornisce informazioni relative a una determinata organizzazione</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
    <memberOf key="model.orgPart"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="org" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listOrg" minOccurs="1" maxOccurs="1"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="listOrg-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listOrg"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listOrg-egXML-xb" source="#ND-eg-99">
      <listOrg>
        <head>Libyans</head>
        <org>
          <orgName>Adyrmachidae</orgName>
          <desc>These people have, in most points, the same customs as the Egyptians, but
                        use the costume of the Libyans. Their women wear on each leg a ring made of
                        bronze [...]</desc>
        </org>
        <org>
          <orgName>Nasamonians</orgName>
          <desc>In summer they leave their flocks and herds upon the sea-shore, and go up
                        the country to a place called Augila, where they gather the dates from the
                        palms [...]</desc>
        </org>
        <org>
          <orgName>Garamantians</orgName>
          <desc>[...] avoid all society or intercourse with their fellow-men, have no
                        weapon of war, and do not know how to defend themselves. [...]</desc>
          <!-- ... -->
        </org>
      </listOrg>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listOrg-remarks" versionDate="2007-09-13" xml:lang="en">
    <p rend="dataDesc">The type attribute may be used to distinguish lists of organizations of a
            particular type if convenient.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="listOrg-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc">L'attribut type peut être utilisé pour établir des listes par type
            d'organisation si cela présente un intérêt.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="listOrg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 属性typeは、特別な種類の組織を区別するために使われるかもしれない。 </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDORG"/>
  </listRef>
```

^b19

