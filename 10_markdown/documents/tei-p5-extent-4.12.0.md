---
type: representation
source-type: document
source: '[[00_sources/tei-p5-extent-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 extent
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/extent.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# extent

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4482. Git blob: `650d63515c5e588d7117d5abc83ebf6d435ce5ff`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-extent" ident="extent">
  <gloss versionDate="2007-06-12" xml:lang="en">extent</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">étendue</gloss>
  <desc versionDate="2013-01-07" xml:lang="en">describes the approximate size of a text stored on some carrier medium or of some other object, digital  or non-digital, specified in any convenient units.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit la taille approximative d’un texte stocké sur son support, numérique ou non numérique, exprimé dans une unité quelconque appropriée.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전달 매체, 즉, 디지털 또는 비디지털로 저장된 텍스트의, 다양한 단위로 명시되는, 대략적 규모를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述電子文件儲存在某一承載媒介時的約略大小，標以任何適用的單位。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">電子・非電子テキストのおよその大きさを任意の単位で示す。</desc>
  <desc versionDate="2016-11-25" xml:lang="de">beschreibt die ungefähre Größe des elektronischen Textes, die er auf einem Datenträger einnimmt; 
    kann auch für andere digitale oder nicht digitale Objekte verwendet werden; die Angabe erfolgt in entsprechenden Maßeinheiten.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe el tamaño aproximado de un texto almacenado en algún medio, digital o no, especificándolo en alguna unidad funcional.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive la grandezza approssimativa di un documento elettronico così come immagazzinata su supporto, secondo una qualsiasi unità funzionale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-zk">
      <extent>3200 sentences</extent>
      <extent>between 10 and 20 Mb</extent>
      <extent>ten 3.5 inch high density diskettes</extent>
    </egXML>
  </exemplum>
  <exemplum versionDate="2016-11-04" xml:lang="en">
    <p>The  <gi>measure</gi> element may be used to supply normalized
or machine tractable versions of the size or sizes concerned.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-ig">
      <extent>
        <measure unit="MiB" quantity="4.2">About four megabytes</measure>
        <measure unit="pages" quantity="245">245 pages of source
material</measure>
      </extent>
    </egXML>
  </exemplum>

  <exemplum versionDate="2016-11-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-dt">
      <extent>400 Seiten</extent>
      <extent>ungefähr 10MB</extent>
    </egXML>
  </exemplum>
  <exemplum versionDate="2023-02-03" xml:lang="de">
    <p>Das <gi>measure</gi>-Element kann dazu verwendet werden, um normalisierte oder 
      maschinenlesbare Versionen der Größen-Angaben bereitzustellen.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-eo">
      <extent>
        <measure unit="MiB" quantity="4.2">Ungefähr vier Megabyte</measure>
        <measure unit="pages" quantity="245">Textumfang 245 Seiten</measure>
      </extent>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-lh">
      <extent>198 pages</extent>
      <extent>90 195 mots</extent>
      <extent>1 Mo</extent>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-gd">
      <extent>3200個句子</extent>
      <extent>介於10 到20 Mb</extent>
      <extent>10片3.5吋磁碟片</extent>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD23"/>
    <ptr target="#HD2"/>
    <ptr target="#COBICOI"/>
    <ptr target="#msph1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">extent</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">étendue</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-01-07" xml:lang="en">describes the approximate size of a text stored on some carrier medium or of some other object, digital  or non-digital, specified in any convenient units.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit la taille approximative d’un texte stocké sur son support, numérique ou non numérique, exprimé dans une unité quelconque appropriée.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전달 매체, 즉, 디지털 또는 비디지털로 저장된 텍스트의, 다양한 단위로 명시되는, 대략적 규모를 기술한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述電子文件儲存在某一承載媒介時的約略大小，標以任何適用的單位。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">電子・非電子テキストのおよその大きさを任意の単位で示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">beschreibt die ungefähre Größe des elektronischen Textes, die er auf einem Datenträger einnimmt; 
    kann auch für andere digitale oder nicht digitale Objekte verwendet werden; die Angabe erfolgt in entsprechenden Maßeinheiten.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe el tamaño aproximado de un texto almacenado en algún medio, digital o no, especificándolo en alguna unidad funcional.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive la grandezza approssimativa di un documento elettronico così come immagazzinata su supporto, secondo una qualsiasi unità funzionale.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-zk">
      <extent>3200 sentences</extent>
      <extent>between 10 and 20 Mb</extent>
      <extent>ten 3.5 inch high density diskettes</extent>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2016-11-04" xml:lang="en">
    <p>The  <gi>measure</gi> element may be used to supply normalized
or machine tractable versions of the size or sizes concerned.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-ig">
      <extent>
        <measure unit="MiB" quantity="4.2">About four megabytes</measure>
        <measure unit="pages" quantity="245">245 pages of source
material</measure>
      </extent>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2016-11-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-dt">
      <extent>400 Seiten</extent>
      <extent>ungefähr 10MB</extent>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2023-02-03" xml:lang="de">
    <p>Das <gi>measure</gi>-Element kann dazu verwendet werden, um normalisierte oder 
      maschinenlesbare Versionen der Größen-Angaben bereitzustellen.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-eo">
      <extent>
        <measure unit="MiB" quantity="4.2">Ungefähr vier Megabyte</measure>
        <measure unit="pages" quantity="245">Textumfang 245 Seiten</measure>
      </extent>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-lh">
      <extent>198 pages</extent>
      <extent>90 195 mots</extent>
      <extent>1 Mo</extent>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-extent-egXML-gd">
      <extent>3200個句子</extent>
      <extent>介於10 到20 Mb</extent>
      <extent>10片3.5吋磁碟片</extent>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD23"/>
    <ptr target="#HD2"/>
    <ptr target="#COBICOI"/>
    <ptr target="#msph1"/>
  </listRef>
```

^b19

