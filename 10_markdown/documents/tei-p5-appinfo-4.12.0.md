---
type: representation
source-type: document
source: '[[00_sources/tei-p5-appinfo-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 appInfo
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/appInfo.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# appInfo

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2396. Git blob: `2e9c650d640aa0fac8f7fd0622039774f293a40f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="appInfo" xml:id="gi-appInfo" module="header">
  <gloss versionDate="2007-07-31" xml:lang="en">application information</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">애플리케이션 정보</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">información de la aplicación</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">informations d'application</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">informazioni su applicazione</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">アプリケーション情報</gloss>
  <desc versionDate="2007-07-31" xml:lang="en">records information about an application which has
  edited the TEI file.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">TEI 파일을 편집한 애플리케이션에 관한 정보를 기록한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">recoge información sobre la aplicación que ha editado el fichero de TEI.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">TEIファイルを編集したソフトウェアに関する情報を示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">enregistre des informations sur l'application qui a
été utilisée pour traiter le fichier TEI.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">registra informazioni relative a un'applicazione che ha modificato il contenuto del file TEI.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    
      <classRef key="model.applicationLike" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-appInfo-egXML-hm" source="#NONE">
      <appInfo>
        <application version="1.24" ident="Xaira">
          <label>XAIRA Indexer</label>
          <ptr target="#P1"/>
        </application>
      </appInfo>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HDAPP"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-31" xml:lang="en">application information</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">애플리케이션 정보</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">información de la aplicación</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">informations d'application</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">informazioni su applicazione</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">アプリケーション情報</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-07-31" xml:lang="en">records information about an application which has
  edited the TEI file.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">TEI 파일을 편집한 애플리케이션에 관한 정보를 기록한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">recoge información sobre la aplicación que ha editado el fichero de TEI.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">TEIファイルを編集したソフトウェアに関する情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">enregistre des informations sur l'application qui a
été utilisée pour traiter le fichier TEI.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">registra informazioni relative a un'applicazione che ha modificato il contenuto del file TEI.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <classRef key="model.applicationLike" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-appInfo-egXML-hm" source="#NONE">
      <appInfo>
        <application version="1.24" ident="Xaira">
          <label>XAIRA Indexer</label>
          <ptr target="#P1"/>
        </application>
      </appInfo>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDAPP"/>
  </listRef>
```

^b16

