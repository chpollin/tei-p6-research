---
type: representation
source-type: document
source: '[[00_sources/tei-p5-application-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 application
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/application.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# application

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5595. Git blob: `9ccd52aa40bdaefcdce5b375e483b39fe505e94f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="application" xml:id="gi-application" module="header">
  <desc versionDate="2007-07-31" xml:lang="en">provides information about an application which has acted upon the document.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문서에 사용한 애플리케이션에 관한 정보를 제시한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">proporciona información sobre la aplicación que ha actuado sobre el documento.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該文書に作用するソフトウェアに関する情報を示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">fournit des informations sur une application qui a été utilisée pour le traitement du document.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">registra informazioni relative a un'applicazione che ha agito sul documento.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.applicationLike"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.ptrLike" minOccurs="0" maxOccurs="unbounded"/>
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>        
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="ident" usage="req">
      <desc versionDate="2013-04-12" xml:lang="en">supplies an identifier for the application, independent of its version number or display name.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">버전 또는 표시명과 상관없이 애플리케이션의 확인소를 제공한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona un identificador para la aplicación, independientemente de su número de versión o el nombre de la visualización.</desc>
      <desc versionDate="2018-12-28" xml:lang="ja">当該ソフトウェアの識別子を示す。これは、版番号や表示名とは異なる。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">fournit un identifiant pour l'application, indépendamment de son numéro de version ou du nom affiché.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica un identificatore per l'applicazione, indipendentemente dal numero di versione o dal nome visualizzato.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef ident="version" usage="req">
      <desc versionDate="2013-04-12" xml:lang="en">supplies a version number for the application, independent of its identifier or display name.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">확인소 또는 표시명과 상관없이 애플리케이션의 버전을 제공한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">Suministra un número de versión para la aplicación, independientemente de su identificador o el nombre de la visualización.</desc>
      <desc versionDate="2018-12-28" xml:lang="ja">当該ソフトウェアの版番号を示す。識別子や表示名とは異なる。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">fournit un numéro de version pour l'application, indépendamment de son identifiant ou du nom affiché.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica un numero di versione per l'applicazione, indipendentemente dall'identificatore o dal nome visualizzato.</desc>
      <datatype><dataRef key="teidata.versionNumber"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-application-egXML-ii" source="#NONE">
      <appInfo>
        <application version="1.5" ident="ImageMarkupTool1" notAfter="2006-06-01">
          <label>Image Markup Tool</label>
          <ptr target="#P1"/>
          <ptr target="#P2"/>
        </application>
      </appInfo>
    </egXML>
    <p>This example shows an <gi>appInfo</gi> element documenting the
    fact that version 1.5 of the Image Markup Tool application has an
    interest in two parts of a document which was last saved on 06
    June 2006. The parts concerned are accessible at the URLs given as
    the <att>target</att> attributes of the two <gi>ptr</gi>
    elements.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-application-egXML-ox" source="#NONE">
      <appInfo>
        <application version="1.24" ident="Xaira">
          <label>XAIRA Indexer</label>
          <ptr target="#fr_HD"/>
        </application>
      </appInfo>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-application-egXML-xs" source="#NONE">
      <appInfo>
        <application version="1.5" ident="ImageMarkupTool1" notAfter="2006-06-01">
          <label>影像標記工具</label>
          <ptr target="#P1"/>
          <ptr target="#P2"/>
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

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-07-31" xml:lang="en">provides information about an application which has acted upon the document.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문서에 사용한 애플리케이션에 관한 정보를 제시한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona información sobre la aplicación que ha actuado sobre el documento.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該文書に作用するソフトウェアに関する情報を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">fournit des informations sur une application qui a été utilisée pour le traitement du document.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">registra informazioni relative a un'applicazione che ha agito sul documento.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.applicationLike"/>
  </classes>
```

^b7

### Block 8

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.labelLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.ptrLike" minOccurs="0" maxOccurs="unbounded"/>
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>        
      </alternate>
    </sequence>
  </content>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-04-12" xml:lang="en">supplies an identifier for the application, independent of its version number or display name.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">버전 또는 표시명과 상관없이 애플리케이션의 확인소를 제공한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona un identificador para la aplicación, independientemente de su número de versión o el nombre de la visualización.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">当該ソフトウェアの識別子を示す。これは、版番号や表示名とは異なる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">fournit un identifiant pour l'application, indépendamment de son numéro de version ou du nom affiché.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica un identificatore per l'applicazione, indipendentemente dal numero di versione o dal nome visualizzato.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-04-12" xml:lang="en">supplies a version number for the application, independent of its identifier or display name.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">확인소 또는 표시명과 상관없이 애플리케이션의 버전을 제공한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">Suministra un número de versión para la aplicación, independientemente de su identificador o el nombre de la visualización.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">当該ソフトウェアの版番号を示す。識別子や表示名とは異なる。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">fournit un numéro de version pour l'application, indépendamment de son identifiant ou du nom affiché.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica un numero di versione per l'applicazione, indipendentemente dall'identificatore o dal nome visualizzato.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.versionNumber"/></datatype>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-application-egXML-ii" source="#NONE">
      <appInfo>
        <application version="1.5" ident="ImageMarkupTool1" notAfter="2006-06-01">
          <label>Image Markup Tool</label>
          <ptr target="#P1"/>
          <ptr target="#P2"/>
        </application>
      </appInfo>
    </egXML>
    <p>This example shows an <gi>appInfo</gi> element documenting the
    fact that version 1.5 of the Image Markup Tool application has an
    interest in two parts of a document which was last saved on 06
    June 2006. The parts concerned are accessible at the URLs given as
    the <att>target</att> attributes of the two <gi>ptr</gi>
    elements.</p>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-application-egXML-ox" source="#NONE">
      <appInfo>
        <application version="1.24" ident="Xaira">
          <label>XAIRA Indexer</label>
          <ptr target="#fr_HD"/>
        </application>
      </appInfo>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-application-egXML-xs" source="#NONE">
      <appInfo>
        <application version="1.5" ident="ImageMarkupTool1" notAfter="2006-06-01">
          <label>影像標記工具</label>
          <ptr target="#P1"/>
          <ptr target="#P2"/>
        </application>
      </appInfo>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDAPP"/>
  </listRef>
```

^b26

