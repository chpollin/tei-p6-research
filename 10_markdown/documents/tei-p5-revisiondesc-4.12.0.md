---
type: representation
source-type: document
source: '[[00_sources/tei-p5-revisiondesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 revisionDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/revisionDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# revisionDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4784. Git blob: `1179819ccf811d203ac790305f82286d1a772590`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-revisionDesc" ident="revisionDesc">
  <gloss versionDate="2005-01-14" xml:lang="en">revision description</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">descriptif des révisions</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">수정 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">修訂描述</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Beschreibung der Dateihistorie</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción de la revisión</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descirzione della revisione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">summarizes the revision history for a file.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">fournit un résumé de l’historique des révisions d’un fichier.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 파일에 대한 수정 이력을 요약한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">概述檔案的修訂歷史。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ファイルの改訂履歴を示す。</desc>
  <desc versionDate="2016-11-25" xml:lang="de">dokumentiert die Änderungen, die an der Datei vorgenommen wurden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">resume el historial de la revisión de un archivo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">sintetizza la storia delle revisioni di un file.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.docStatus"/>
  </classes>
  <content>
    <alternate>
      <elementRef key="list" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="listChange" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="change" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-revisionDesc-egXML-yt">
      <revisionDesc status="embargoed">
        <change when="1991-11-11" who="#LB"> deleted chapter 10 </change>
      </revisionDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-revisionDesc-egXML-qn">
      <revisionDesc>
        <list>
          <item><date when="2003-04-12">12 avril 03</date>Dernière révision par F. B.</item>
          <item><date when="2003-03-01">1 mars 03</date> F.B a fait le nouveau fichier.</item>
        </list>
      </revisionDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-revisionDesc-egXML-io">
      <revisionDesc status="embargoed">
        <change when="1991-11-11"> 王大明刪除第十章</change>
      </revisionDesc>
    </egXML>
  </exemplum>
  <remarks ident="revisionDesc-remarks" versionDate="2016-11-04" xml:lang="en">
    <p>If present on this element, the <att>status</att> attribute
    should indicate the current status of the document. The same
    attribute may appear on any <gi>change</gi> to record the status
    at the time of that change. Conventionally <gi>change</gi> elements should
    be given in reverse date order, with the most recent change at the
    start of the list.</p>
  </remarks>
  <remarks ident="revisionDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les changements les plus récents apparaissent en début de liste</p>
  </remarks>
  <remarks ident="revisionDesc-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Registran los cambios más recientes en el top de la lista.</p>
  </remarks>
  <remarks ident="revisionDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 直近の変更をリストの先頭に記録する。 </p>
  </remarks>
  <remarks ident="revisionDesc-remarks" versionDate="2016-11-25" xml:lang="de">
      <p>Wenn an diesem Element gesetzt, sollte das <att>status</att>-Attribut den aktuellen 
          Status des Dokuments widerspiegeln. An jedem <gi>change</gi>-Kindelement gibt das selbe 
          Attribut den jeweiligen Status zum Zeitpunkt der Änderung an. Die <gi>change</gi>-Elemente 
          werden der Konvention nach so angeordnet, dass die letzte Änderung am Anfang steht und die erste zum Schluss. </p>
  </remarks>
  <listRef>
    <ptr target="#HD6"/>
    <ptr target="#HD11"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">revision description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">descriptif des révisions</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">수정 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">修訂描述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Beschreibung der Dateihistorie</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción de la revisión</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descirzione della revisione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">summarizes the revision history for a file.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">fournit un résumé de l’historique des révisions d’un fichier.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 파일에 대한 수정 이력을 요약한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">概述檔案的修訂歷史。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ファイルの改訂履歴を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">dokumentiert die Änderungen, die an der Datei vorgenommen wurden.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">resume el historial de la revisión de un archivo.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">sintetizza la storia delle revisioni di un file.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.docStatus"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <elementRef key="list" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="listChange" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="change" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-revisionDesc-egXML-yt">
      <revisionDesc status="embargoed">
        <change when="1991-11-11" who="#LB"> deleted chapter 10 </change>
      </revisionDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-revisionDesc-egXML-qn">
      <revisionDesc>
        <list>
          <item><date when="2003-04-12">12 avril 03</date>Dernière révision par F. B.</item>
          <item><date when="2003-03-01">1 mars 03</date> F.B a fait le nouveau fichier.</item>
        </list>
      </revisionDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-revisionDesc-egXML-io">
      <revisionDesc status="embargoed">
        <change when="1991-11-11"> 王大明刪除第十章</change>
      </revisionDesc>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="revisionDesc-remarks" versionDate="2016-11-04" xml:lang="en">
    <p>If present on this element, the <att>status</att> attribute
    should indicate the current status of the document. The same
    attribute may appear on any <gi>change</gi> to record the status
    at the time of that change. Conventionally <gi>change</gi> elements should
    be given in reverse date order, with the most recent change at the
    start of the list.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="revisionDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les changements les plus récents apparaissent en début de liste</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="revisionDesc-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Registran los cambios más recientes en el top de la lista.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="revisionDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 直近の変更をリストの先頭に記録する。 </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="revisionDesc-remarks" versionDate="2016-11-25" xml:lang="de">
      <p>Wenn an diesem Element gesetzt, sollte das <att>status</att>-Attribut den aktuellen 
          Status des Dokuments widerspiegeln. An jedem <gi>change</gi>-Kindelement gibt das selbe 
          Attribut den jeweiligen Status zum Zeitpunkt der Änderung an. Die <gi>change</gi>-Elemente 
          werden der Konvention nach so angeordnet, dass die letzte Änderung am Anfang steht und die erste zum Schluss. </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD6"/>
    <ptr target="#HD11"/>
  </listRef>
```

^b26

