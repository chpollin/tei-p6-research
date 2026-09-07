---
type: representation
source-type: document
source: '[[00_sources/tei-p5-joingrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 joinGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/joinGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# joinGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4581. Git blob: `fc391271bd349c1712791eedf7cd8f96ef4b68bc`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="linking" xml:id="gi-joinGrp" ident="joinGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">join group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">결합군</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">連結群組</gloss>
  <gloss versionDate="2009-10-06" xml:lang="fr">groupe de jointures</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de enlace</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di collegamento</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">groups a collection of <gi>join</gi> elements and possibly pointers.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">결합 요소 및 가능한 포인터의 집합군</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一群連結元素與可能指標。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素joinやポインタをまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe une collection d'éléments <gi>join</gi> ainsi que, éventuellement, des pointeurs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa un conjunto de elementos de enlace a eventuales señalizadores.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa un insieme di elementi di collegamento ed eventuali puntatori.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.pointing.group"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="equiv"/>
        <elementRef key="gloss"/>
        <classRef key="model.descLike"/>
      </alternate>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="join"/>
        <elementRef key="ptr"/>
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="result" usage="opt">
      <desc versionDate="2013-12-21" xml:lang="en">supplies the default value for the <att>result</att> on each <gi>join</gi> included within the group.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 집합에 모아진 결합 결과를 기술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">描述此集合中匯集的連結結果。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素でまとめられた要素joinを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">décrit le résultat produit par le rassemblement dans cette collection des éléments <gi>join</gi>.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">describe el resultado de los enlaces agrupados en tal conjunto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">descrive il risultato dei collegamenti raggruppati in tale insieme.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-joinGrp-egXML-my" source="#UND">
      <joinGrp domains="#zuitxt1 #zuitxt2 #zuitxt3" result="q">
        <join target="#zuiq1 #zuiq2 #zuiq6"/>
        <join target="#zuiq3 #zuiq4 #zuiq5"/>
      </joinGrp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-joinGrp-egXML-kl" source="#UND">
      <joinGrp domains="#zuitxt1 #zuitxt2 #zuitxt3" result="q">
        <join target="#fr_zuiq1 #fr_zuiq2 #fr_zuiq6"/>
        <join target="#fr_zuiq3 #fr_zuiq4 #fr_zuiq5"/>
      </joinGrp>
    </egXML>
  </exemplum>
  <remarks ident="joinGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Any number of <gi>join</gi> or <gi>ptr</gi> elements.</p>
  </remarks>
  <remarks ident="joinGrp-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p rend="dataDesc">Un nombre quelconque d'éléments <gi>join</gi> ou <gi>ptr</gi>.</p>
  </remarks>
  <remarks ident="joinGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 任意数の要素<gi>join</gi>または要素<gi>ptr</gi>。 </p>
  </remarks>
  <listRef>
    <ptr target="#SAAG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">join group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">결합군</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">連結群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-10-06" xml:lang="fr">groupe de jointures</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de enlace</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di collegamento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">groups a collection of <gi>join</gi> elements and possibly pointers.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">결합 요소 및 가능한 포인터의 집합군</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一群連結元素與可能指標。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素joinやポインタをまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe une collection d'éléments <gi>join</gi> ainsi que, éventuellement, des pointeurs.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa un conjunto de elementos de enlace a eventuales señalizadores.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa un insieme di elementi di collegamento ed eventuali puntatori.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.pointing.group"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="equiv"/>
        <elementRef key="gloss"/>
        <classRef key="model.descLike"/>
      </alternate>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="join"/>
        <elementRef key="ptr"/>
      </alternate>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">supplies the default value for the <att>result</att> on each <gi>join</gi> included within the group.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 집합에 모아진 결합 결과를 기술한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述此集合中匯集的連結結果。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素でまとめられた要素joinを示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit le résultat produit par le rassemblement dans cette collection des éléments <gi>join</gi>.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe el resultado de los enlaces agrupados en tal conjunto.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il risultato dei collegamenti raggruppati in tale insieme.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-joinGrp-egXML-my" source="#UND">
      <joinGrp domains="#zuitxt1 #zuitxt2 #zuitxt3" result="q">
        <join target="#zuiq1 #zuiq2 #zuiq6"/>
        <join target="#zuiq3 #zuiq4 #zuiq5"/>
      </joinGrp>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-joinGrp-egXML-kl" source="#UND">
      <joinGrp domains="#zuitxt1 #zuitxt2 #zuitxt3" result="q">
        <join target="#fr_zuiq1 #fr_zuiq2 #fr_zuiq6"/>
        <join target="#fr_zuiq3 #fr_zuiq4 #fr_zuiq5"/>
      </joinGrp>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="joinGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Any number of <gi>join</gi> or <gi>ptr</gi> elements.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="joinGrp-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p rend="dataDesc">Un nombre quelconque d'éléments <gi>join</gi> ou <gi>ptr</gi>.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="joinGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 任意数の要素<gi>join</gi>または要素<gi>ptr</gi>。 </p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SAAG"/>
  </listRef>
```

^b29

