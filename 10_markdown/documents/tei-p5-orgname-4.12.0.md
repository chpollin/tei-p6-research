---
type: representation
source-type: document
source: '[[00_sources/tei-p5-orgname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 orgName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/orgName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# orgName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2881. Git blob: `1477dcad893f3a646fe09ccd87baff4635b96873`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-orgName" ident="orgName">
  <gloss versionDate="2005-01-14" xml:lang="en">organization name</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">조직명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">組織名稱</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">nom d'organisation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nombre de una organización</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nome di organizzazione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an organizational name.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">조직명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個組織名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">組織の名前を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient le nom d'une organisation.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de una organización.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome proprio di un'organizzazione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.nameLike.agent"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orgName-egXML-qv">About a year back, a question of considerable interest was agitated in the <orgName key="PAS1" type="voluntary"><placeName key="PEN">Pennsyla.</placeName> Abolition Society</orgName> [...]</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orgName-egXML-zd">
      <orgName key="ssav" type="regional">Société savoisienne de <placeName key="GRE">Grenoble</placeName>
         </orgName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orgName-egXML-zj"> 大約一年前，在<placeName key="PEN">賓州</placeName>的<orgName key="PAS1" type="voluntary">廢止黑奴協會</orgName>，有一場轟動的激辯。</egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDORG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">organization name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조직명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">組織名稱</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">nom d'organisation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nombre de una organización</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nome di organizzazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an organizational name.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">조직명을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個組織名稱。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">組織の名前を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient le nom d'une organisation.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de una organización.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome proprio di un'organizzazione.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.nameLike.agent"/>
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

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orgName-egXML-qv">About a year back, a question of considerable interest was agitated in the <orgName key="PAS1" type="voluntary"><placeName key="PEN">Pennsyla.</placeName> Abolition Society</orgName> [...]</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orgName-egXML-zd">
      <orgName key="ssav" type="regional">Société savoisienne de <placeName key="GRE">Grenoble</placeName>
         </orgName>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orgName-egXML-zj"> 大約一年前，在<placeName key="PEN">賓州</placeName>的<orgName key="PAS1" type="voluntary">廢止黑奴協會</orgName>，有一場轟動的激辯。</egXML>
  </exemplum>
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

