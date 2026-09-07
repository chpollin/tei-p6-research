---
type: representation
source-type: document
source: '[[00_sources/tei-p5-witdetail-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 witDetail
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/witDetail.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# witDetail

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5947. Git blob: `09898783056f04e5413acebf3410af967fdccfce`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-witDetail" ident="witDetail">
  <gloss versionDate="2007-07-04" xml:lang="en">witness detail</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트 세목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">detalle del testimonio</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">informations détaillées sur le témoin</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">dettagli del testimone</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">gives further information about a particular witness, or
witnesses, to a particular reading.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">특별한 비교 대상 텍스트에 관한 상세한 정보를 특별한 독법에 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">進一步提供一個特殊對應本的特殊版本資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">特定の解釈に関連する、特定の文献について詳細な情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">donne des renseignements supplémentaires sur un
			témoin particulier ou sur des témoins, pour une leçon particulière.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona ulteriores detalles sobre uno o más testimonios relativos a una lectura dada.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce ulteriori dettagli in merito a un testimone o più testimoni relativi a una data lettura.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.global"/>
      <elementRef key="bibl"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="wit" usage="req">
      <gloss versionDate="2007-07-04" xml:lang="en">witnesses</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">testimonios</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">témoins</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">testimoni</gloss>
      <desc versionDate="2013-11-18" xml:lang="en">indicates the sigil
      or sigla identifying the witness or witnesses to which the
detail refers.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">세목이 참조하는 비교 대상 텍스트에 대한 변항 기호 또는 기호일람표를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明細節資訊所指版本的一個或多個印記。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">細目が参照する当該文献の印や文献記号を示す。</desc>
      <desc versionDate="2009-04-17" xml:lang="fr">contient le ou les code(s)				identifiant le ou le(s) témoin(s) auxquels fait référence l'élément
						<gi>witDetail</gi>.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la sigla o siglas relativas a los testimonios a los cuales se refieren los detalles</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la sigla o le sigle relative ai testimoni ai quali si riferiscono i dettagli.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">describes the type of information given about the witness.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트에 관해 제시된 정보의 유형을 기술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">版本的資訊種類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該文献に関する情報の種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">décrit le type de renseignement donné sur
					le témoin.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">describe el tipo de información dada sobre los testimonios.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">descrive il tipo di informazione fornita in merito al testimone.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-witDetail-egXML-fm">
      <app type="substantive">
        <lem xml:id="W026x" wit="#El #HG">Experience</lem>
        <rdg wit="#Ha4">Experiens</rdg>
        <witDetail target="#W026x" resp="#PR" wit="#El" type="presentation">Ornamental capital.</witDetail>
      </app>
    </egXML>
  </exemplum>
  <remarks ident="witDetail-remarks" versionDate="2019-01-17" xml:lang="en">
    <p>The <gi>witDetail</gi> element was formerly permitted anywhere that <gi>note</gi>
    could appear, but since it should only be used in association with <gi>lem</gi> and
    <gi>rdg</gi>, it is recommended that it be placed immediately following the reading that it modifies, 
    in the same <gi>app</gi>. A <gi>witDetail</gi> without a <att>target</att> attribute 
    should be assumed to refer to the closest preceding <gi>lem</gi> or <gi>rdg</gi>.
    </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">witness detail</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트 세목</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">detalle del testimonio</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">informations détaillées sur le témoin</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">dettagli del testimone</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives further information about a particular witness, or
witnesses, to a particular reading.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">특별한 비교 대상 텍스트에 관한 상세한 정보를 특별한 독법에 제공한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">進一步提供一個特殊對應本的特殊版本資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">特定の解釈に関連する、特定の文献について詳細な情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne des renseignements supplémentaires sur un
			témoin particulier ou sur des témoins, pour une leçon particulière.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona ulteriores detalles sobre uno o más testimonios relativos a una lectura dada.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce ulteriori dettagli in merito a un testimone o più testimoni relativi a una data lettura.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <classRef key="model.global"/>
      <elementRef key="bibl"/>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">witnesses</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">testimonios</gloss>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">témoins</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">testimoni</gloss>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-11-18" xml:lang="en">indicates the sigil
      or sigla identifying the witness or witnesses to which the
detail refers.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">세목이 참조하는 비교 대상 텍스트에 대한 변항 기호 또는 기호일람표를 표시한다.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明細節資訊所指版本的一個或多個印記。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">細目が参照する当該文献の印や文献記号を示す。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">contient le ou les code(s)				identifiant le ou le(s) témoin(s) auxquels fait référence l'élément
						<gi>witDetail</gi>.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la sigla o siglas relativas a los testimonios a los cuales se refieren los detalles</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la sigla o le sigle relative ai testimoni ai quali si riferiscono i dettagli.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the type of information given about the witness.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트에 관해 제시된 정보의 유형을 기술한다.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">版本的資訊種類。</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該文献に関する情報の種類を示す。</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit le type de renseignement donné sur
					le témoin.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe el tipo de información dada sobre los testimonios.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il tipo di informazione fornita in merito al testimone.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b36

### Block 37

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-witDetail-egXML-fm">
      <app type="substantive">
        <lem xml:id="W026x" wit="#El #HG">Experience</lem>
        <rdg wit="#Ha4">Experiens</rdg>
        <witDetail target="#W026x" resp="#PR" wit="#El" type="presentation">Ornamental capital.</witDetail>
      </app>
    </egXML>
  </exemplum>
```

^b37

### Block 38

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="witDetail-remarks" versionDate="2019-01-17" xml:lang="en">
    <p>The <gi>witDetail</gi> element was formerly permitted anywhere that <gi>note</gi>
    could appear, but since it should only be used in association with <gi>lem</gi> and
    <gi>rdg</gi>, it is recommended that it be placed immediately following the reading that it modifies, 
    in the same <gi>app</gi>. A <gi>witDetail</gi> without a <att>target</att> attribute 
    should be assumed to refer to the closest preceding <gi>lem</gi> or <gi>rdg</gi>.
    </p>
  </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b39

