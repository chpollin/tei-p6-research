---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listbibl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listBibl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listBibl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listBibl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5850. Git blob: `5ef98df932ed38c8b092920787770c7f93077e94`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-listBibl" ident="listBibl">
  <gloss versionDate="2005-01-14" xml:lang="en">citation list</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">인용 목록</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">書目列表</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">liste de références bibliographiques</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">lista de cita</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">lista di citazioni</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Liste bibliografischer Angaben</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a list of bibliographic citations of any kind.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">여러 종류의 서지 인용 목록을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何種類的書目資料列表。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">書誌項目引用のリストを示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une liste de références bibliographiques de toute nature.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una lista de citas bibliográficas de cualquier tipo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una lista di citazioni bibliografiche di qualsiasi natura.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält eine Liste von bibliografischen Angaben jeglicher Art.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblLike"/>
    <!-- model.listLike is incompatible with membership in model.biblLike since both are referenced from macro.inter -->
    <memberOf key="model.frontPart"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.milestoneLike" minOccurs="1" maxOccurs="1"/>
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.biblLike" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.milestoneLike" minOccurs="1" maxOccurs="1"/>
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <constraintSpec ident="listBibl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listBibl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listBibl-egXML-eb">
      <listBibl>
        <head>Works consulted</head>
        <bibl>Blain, Clements and Grundy: Feminist Companion to
                    Literature in English (Yale, 1990)
                </bibl>
        <biblStruct>
          <analytic>
            <title>The Interesting story of the Children in the Wood</title>
          </analytic>
          <monogr>
            <title>The Penny Histories</title>
            <author>Victor E Neuberg</author>
            <imprint>
              <publisher>OUP</publisher>
              <date>1968</date>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listBibl-egXML-sp">
      <listBibl>
        <head>Liste des ouvrages cités</head>
        <bibl>Les Petits Romantiques </bibl>
        <biblStruct>
          <analytic>
            <title>La poésie en prose</title>
          </analytic>
          <monogr>
            <title>Aloysius Bertrand, "inventeur" du poème en prose</title>
            <author>Bert Guégand</author>
            <imprint>
              <publisher>PUN</publisher>
              <date>2000</date>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listBibl-egXML-gw" source="#biblzh-tw_n13">
      <listBibl>
        <head>參考書籍</head>
        <bibl>潘定衡、楊朝文: 蚩尤的傳說 (貴陽：貴州民族出版社，1989 ) </bibl>
        <biblStruct>
          <analytic>
            <title>中國古史的傳說時代 </title>
          </analytic>
          <monogr>
            <title>苗族蚩尤神话，與逐鹿之戰。</title>
            <author>吳曉東</author>
            <imprint>
              <publisher>北京：民族文學研究 </publisher>
              <date> 1998 </date>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
    </egXML>
  </exemplum>
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
<gloss versionDate="2005-01-14" xml:lang="en">citation list</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">인용 목록</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">書目列表</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">liste de références bibliographiques</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">lista de cita</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">lista di citazioni</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Liste bibliografischer Angaben</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a list of bibliographic citations of any kind.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">여러 종류의 서지 인용 목록을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何種類的書目資料列表。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">書誌項目引用のリストを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une liste de références bibliographiques de toute nature.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lista de citas bibliográficas de cualquier tipo.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lista di citazioni bibliografiche di qualsiasi natura.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält eine Liste von bibliografischen Angaben jeglicher Art.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblLike"/>
    <!-- model.listLike is incompatible with membership in model.biblLike since both are referenced from macro.inter -->
    <memberOf key="model.frontPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.milestoneLike" minOccurs="1" maxOccurs="1"/>
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.biblLike" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.milestoneLike" minOccurs="1" maxOccurs="1"/>
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="listBibl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listBibl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listBibl-egXML-eb">
      <listBibl>
        <head>Works consulted</head>
        <bibl>Blain, Clements and Grundy: Feminist Companion to
                    Literature in English (Yale, 1990)
                </bibl>
        <biblStruct>
          <analytic>
            <title>The Interesting story of the Children in the Wood</title>
          </analytic>
          <monogr>
            <title>The Penny Histories</title>
            <author>Victor E Neuberg</author>
            <imprint>
              <publisher>OUP</publisher>
              <date>1968</date>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listBibl-egXML-sp">
      <listBibl>
        <head>Liste des ouvrages cités</head>
        <bibl>Les Petits Romantiques </bibl>
        <biblStruct>
          <analytic>
            <title>La poésie en prose</title>
          </analytic>
          <monogr>
            <title>Aloysius Bertrand, "inventeur" du poème en prose</title>
            <author>Bert Guégand</author>
            <imprint>
              <publisher>PUN</publisher>
              <date>2000</date>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listBibl-egXML-gw" source="#biblzh-tw_n13">
      <listBibl>
        <head>參考書籍</head>
        <bibl>潘定衡、楊朝文: 蚩尤的傳說 (貴陽：貴州民族出版社，1989 ) </bibl>
        <biblStruct>
          <analytic>
            <title>中國古史的傳說時代 </title>
          </analytic>
          <monogr>
            <title>苗族蚩尤神话，與逐鹿之戰。</title>
            <author>吳曉東</author>
            <imprint>
              <publisher>北京：民族文學研究 </publisher>
              <date> 1998 </date>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBITY"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b22

