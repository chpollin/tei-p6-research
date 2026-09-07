---
type: representation
source-type: document
source: '[[00_sources/tei-p5-seal-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 seal
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/seal.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# seal

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4332. Git blob: `e8b6935345cfc87b4b088b877dde298d2930196c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="SEAL" ident="seal">
  <gloss versionDate="2007-06-12" xml:lang="en">seal</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">sceau</gloss>
  <desc versionDate="2018-07-17" xml:lang="en">contains a description of one seal or similar applied to the object described.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고에 적용된 봉인 또는 유사 부착물 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述一個章印或其他附於手稿的類似項目</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料にあるシールや付着物を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description d'un sceau ou d'un objet similaire, attaché au manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de un sello o de un elemento externo aplicado a un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la descrizione di un sigillo o altro oggetto applicato al manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <elementRef key="decoNote"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="contemporary">
      <gloss versionDate="2007-06-12" xml:lang="en">contemporary</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">contemporain</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">specifies whether or not the seal is contemporary with the
      item to which it is affixed</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">봉인이 그것이 첨부된 항목과 동시에 만들어졌는가를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該章印和其附著的項目是否出於同一時期。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該シールが、当該資料と同時代のものかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie si le sceau est ou non contemporain du
          manuscrit auquel il est attaché.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica si el sello es o no contemporáneo al objeto al que se ha aplicado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica se il sigillo è coevo o meno rispetto all'oggetto al quale è applicato.</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEAL-egXML-hj">
      <seal n="2" type="pendant" subtype="cauda_duplex">
        <p>The seal of <name>Jens Olufsen</name> in black wax. 
(<ref>DAS 1061</ref>). Legend: <q>S IOHANNES OLAVI</q>.
Parchment tag on which is written: <q>Woldorp Iohanne G</q>.</p>
      </seal>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEAL-egXML-vf">
      <seal n="2" type="pendant" subtype="cauda_duplex">
        <p>The seal of <name>Jens Olufsen</name> in black wax. (<ref>DAS 1061</ref>). Legend: <q>S
              IOHANNES OLAVI</q>. Parchment tag on which is written: <q>Woldorp Iohanne G</q>.</p>
      </seal>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEAL-egXML-hm">
      <seal>
        <p>清<name>乾隆</name>皇帝的「古稀天子之寶」玉璽，是選用整塊碧玉琢製而成，印面以正方形，雙龍鈕繫黃條，印面琢三行六字篆書，為乾隆年登70歲之印。</p>
      </seal>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msphse"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">seal</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">sceau</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-07-17" xml:lang="en">contains a description of one seal or similar applied to the object described.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고에 적용된 봉인 또는 유사 부착물 기술을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述一個章印或其他附於手稿的類似項目</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料にあるシールや付着物を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description d'un sceau ou d'un objet similaire, attaché au manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de un sello o de un elemento externo aplicado a un manuscrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la descrizione di un sigillo o altro oggetto applicato al manoscritto.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <elementRef key="decoNote"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">contemporary</gloss>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contemporain</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies whether or not the seal is contemporary with the
      item to which it is affixed</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">봉인이 그것이 첨부된 항목과 동시에 만들어졌는가를 명시한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該章印和其附著的項目是否出於同一時期。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該シールが、当該資料と同時代のものかを示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie si le sceau est ou non contemporain du
          manuscrit auquel il est attaché.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica si el sello es o no contemporáneo al objeto al que se ha aplicado.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica se il sigillo è coevo o meno rispetto all'oggetto al quale è applicato.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEAL-egXML-hj">
      <seal n="2" type="pendant" subtype="cauda_duplex">
        <p>The seal of <name>Jens Olufsen</name> in black wax. 
(<ref>DAS 1061</ref>). Legend: <q>S IOHANNES OLAVI</q>.
Parchment tag on which is written: <q>Woldorp Iohanne G</q>.</p>
      </seal>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEAL-egXML-vf">
      <seal n="2" type="pendant" subtype="cauda_duplex">
        <p>The seal of <name>Jens Olufsen</name> in black wax. (<ref>DAS 1061</ref>). Legend: <q>S
              IOHANNES OLAVI</q>. Parchment tag on which is written: <q>Woldorp Iohanne G</q>.</p>
      </seal>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SEAL-egXML-hm">
      <seal>
        <p>清<name>乾隆</name>皇帝的「古稀天子之寶」玉璽，是選用整塊碧玉琢製而成，印面以正方形，雙龍鈕繫黃條，印面琢三行六字篆書，為乾隆年登70歲之印。</p>
      </seal>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msphse"/>
  </listRef>
```

^b25

