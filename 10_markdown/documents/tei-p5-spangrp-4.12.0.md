---
type: representation
source-type: document
source: '[[00_sources/tei-p5-spangrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 spanGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/spanGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# spanGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2844. Git blob: `d34894cfa65a8c6322a07b91862944f1e7a2fe0c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:xi="http://www.w3.org/2001/XInclude" module="analysis" xml:id="gi-spanGrp" ident="spanGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">span group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">범위 집단</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文字段群組</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">groupement de fragments de texte</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de periodo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di porzioni</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">collects together span tags.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">범위 태그를 모아놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文字段標籤。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素<gi>span</gi>をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments <gi>span</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">Agrupa las etiquetas del periodo</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa i marcatori di porzione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.interpLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>   
    <sequence>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="span" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-spanGrp-egXML-vs" source="#CONAAB-eg-150">
      <u xml:id="UU1">Can I have ten oranges and a kilo of bananas please?</u>
      <u xml:id="UU2">Yes, anything else?</u>
      <u xml:id="UU3">No thanks.</u>
      <u xml:id="UU4">That'll be dollar forty.</u>
      <u xml:id="UU5">Two dollars</u>
      <u xml:id="UU6">Sixty, eighty, two dollars. 
   <anchor xml:id="UU6e"/>Thank you.<anchor xml:id="UU6f"/>
         </u>
      <spanGrp type="transactions">
        <span from="#UU1">sale request</span>
        <span from="#UU2" to="#UU3">sale compliance</span>
        <span from="#UU4">sale</span>
        <span from="#UU5" to="#UU6">purchase</span>
        <span from="#UU6e" to="#UU6f">purchase closure</span>
      </spanGrp>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#AISP"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">span group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">범위 집단</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文字段群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">groupement de fragments de texte</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de periodo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di porzioni</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">collects together span tags.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">범위 태그를 모아놓는다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文字段標籤。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素<gi>span</gi>をまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments <gi>span</gi>.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">Agrupa las etiquetas del periodo</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa i marcatori di porzione.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.interpLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>   
    <sequence>
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="span" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-spanGrp-egXML-vs" source="#CONAAB-eg-150">
      <u xml:id="UU1">Can I have ten oranges and a kilo of bananas please?</u>
      <u xml:id="UU2">Yes, anything else?</u>
      <u xml:id="UU3">No thanks.</u>
      <u xml:id="UU4">That'll be dollar forty.</u>
      <u xml:id="UU5">Two dollars</u>
      <u xml:id="UU6">Sixty, eighty, two dollars. 
   <anchor xml:id="UU6e"/>Thank you.<anchor xml:id="UU6f"/>
         </u>
      <spanGrp type="transactions">
        <span from="#UU1">sale request</span>
        <span from="#UU2" to="#UU3">sale compliance</span>
        <span from="#UU4">sale</span>
        <span from="#UU5" to="#UU6">purchase</span>
        <span from="#UU6e" to="#UU6f">purchase closure</span>
      </spanGrp>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AISP"/>
  </listRef>
```

^b17

