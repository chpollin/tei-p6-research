---
type: representation
source-type: document
source: '[[00_sources/tei-p5-provenance-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 provenance
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/provenance.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# provenance

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3445. Git blob: `75a5e61b7c142031109a7451f6243282b1082fa7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="PROVENANCE" ident="provenance">
  <gloss versionDate="2007-06-12" xml:lang="en">provenance</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">provenance</gloss>
  <gloss versionDate="2023-08-08" xml:lang="de">Provenienz</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="prov.desc">contains any descriptive or other information concerning a single identifiable episode during the history of a manuscript, manuscript part, or other object after its creation but before its acquisition.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">생성된 후부터 획득되기 전까지 원고 또는 원고 일부의 이력에 대해 확인가능한 에피소드에 관련한 기술적 또는 기타 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何描述性或其他資訊，關於手稿或手稿部分的歷史中單一可確認的事件，發生在手稿產生之後、取得之前。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料を入手するまでの歴史に関する、特定可能なエピソードに関する 情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur un épisode précis de l'histoire du manuscrit ou de la partie du manuscrit, après sa création et avant son acquisition.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene descripciones o informaciones relativas a un único episodio identificable en la historia de un manuscrito o de una de sus partes que sea posterior al momento de su creación pero anterior al momento de su adquisición.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative a un unico episodio rintracciabile nella storia di un manoscritto o di una sua parte che sia posteriore alla sua creazione ma anteriore rispetto alla sua acquisizione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PROVENANCE-egXML-hg">
      <provenance>Listed as the property of Lawrence Sterne in 1788.</provenance>
      <provenance>Sold at Sothebys in 1899.</provenance>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PROVENANCE-egXML-tq">
      <provenance>Listed as the property of Lawrence Sterne in 1788.</provenance>
      <provenance>Sold at Sothebys in 1899.</provenance>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PROVENANCE-egXML-fj">
      <provenance>1020年列為范寬的財產。</provenance>
      <provenance>1024年於洛陽賣出。</provenance>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mshy"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">provenance</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">provenance</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2023-08-08" xml:lang="de">Provenienz</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="prov.desc">contains any descriptive or other information concerning a single identifiable episode during the history of a manuscript, manuscript part, or other object after its creation but before its acquisition.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">생성된 후부터 획득되기 전까지 원고 또는 원고 일부의 이력에 대해 확인가능한 에피소드에 관련한 기술적 또는 기타 정보를 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何描述性或其他資訊，關於手稿或手稿部分的歷史中單一可確認的事件，發生在手稿產生之後、取得之前。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料を入手するまでの歴史に関する、特定可能なエピソードに関する 情報を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur un épisode précis de l'histoire du manuscrit ou de la partie du manuscrit, après sa création et avant son acquisition.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene descripciones o informaciones relativas a un único episodio identificable en la historia de un manuscrito o de una de sus partes que sea posterior al momento de su creación pero anterior al momento de su adquisición.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative a un unico episodio rintracciabile nella storia di un manoscritto o di una sua parte che sia posteriore alla sua creazione ma anteriore rispetto alla sua acquisizione.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PROVENANCE-egXML-hg">
      <provenance>Listed as the property of Lawrence Sterne in 1788.</provenance>
      <provenance>Sold at Sothebys in 1899.</provenance>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PROVENANCE-egXML-tq">
      <provenance>Listed as the property of Lawrence Sterne in 1788.</provenance>
      <provenance>Sold at Sothebys in 1899.</provenance>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PROVENANCE-egXML-fj">
      <provenance>1020年列為范寬的財產。</provenance>
      <provenance>1024年於洛陽賣出。</provenance>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mshy"/>
  </listRef>
```

^b16

