---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.handfeatures-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.handFeatures
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.handFeatures.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.handFeatures

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7988. Git blob: `11f23efa42fe1356459e4c339e00a9e70c801115`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" ident="att.handFeatures">
  <desc versionDate="2007-09-27" xml:lang="en">provides attributes describing aspects of the hand in which a manuscript is written.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고가 쓰여진 필적의 측면을 기술하는 속성을 제공한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">proporciona atributos que describen los aspectos de la mano que ha escrito un manuscrito.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の筆致に関する情報を表す情報を示す。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">fournit des attributs décrivant les caractéristiques de la main par laquelle un manuscrit est écrit.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">indica degli attributi che descrivono aspetti delle mano utilizzata per la scrittura del manoscritto.</desc>
  <classes>
    <memberOf key="att.scope"/>
  </classes>
  <attList>
    <attDef ident="scribe">
      <desc versionDate="2010-09-28" xml:lang="en">gives a name or other identifier for the scribe believed to be responsible for this hand.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 필적에 대한 책임이 있다고 간주되는 필기사에 대한 표준명 또는 다른 확인소를 제시한다.</desc>
      <desc versionDate="2019-09-16" xml:lang="ja">当該筆致に対応すると考えられる筆写者の名前またはその他の識別子を示す。</desc>
      <desc versionDate="2009-05-27" xml:lang="fr">donne un nom normalisé ou un autre identifiant pour le scribe reconnu comme responsable de cette main.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un nome o altro identificatore standard al trascrittore che si ritiene corrisponda alla mano in questione.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">asigna un nombre u otro identificador estándard para el transcriptor que se identifica con la mano en cuestión.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
      <!-- valDesc xml:lang="fr">Un nom quelconque.</valDesc -->
    </attDef>
    <attDef ident="scribeRef">
      <desc versionDate="2010-09-28" xml:lang="en">points to a full description of the scribe concerned, typically supplied by a <gi>person</gi> element elsewhere in the description.</desc>
      <desc versionDate="2019-09-16" xml:lang="ja">問題の筆写者についての詳細な記述へポイントする。典型的には記述のどこかで<gi>person</gi>要素によって補われる。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="script">
      <desc versionDate="2008-02-01" xml:lang="en">characterizes the particular script or writing style used by this hand, for example <mentioned>secretary</mentioned>, <mentioned>copperplate</mentioned>, <mentioned>Chancery</mentioned>, <mentioned>Italian</mentioned>, etc.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"><mentioned>secretary</mentioned>, <mentioned>copperplate</mentioned>, <mentioned>Chancery</mentioned>, <mentioned>Italian</mentioned> 등과 같이 이 필적으로 사용된 특별한 필사본 또는 글쓰기 스타일의 특성을 기술한다.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該筆致で使用されている特定の筆体や書記スタイルの特徴を示す。例 えば、<mentioned>secretary(書記官スタイル)</mentioned>、 <mentioned>copperplate(銅板スタイル)</mentioned>、 <mentioned>Chancery(公文書スタイル)</mentioned>、 <mentioned>Italian(イタリアスタイル)</mentioned>など。</desc>
      <desc versionDate="2009-05-27" xml:lang="fr">caractérise la calligraphie ou le style d'écriture particuliers utilisés par cette main, par exemple <mentioned>écriture anglaise</mentioned>, <mentioned>de chancellerie</mentioned>, <mentioned>italienne</mentioned>, etc.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">caratterizza un determinato stile di scrittura utilizzato dalla mano in questione, per esempio <mentioned>segretario</mentioned>, <mentioned>incisione su rame</mentioned>, <mentioned>Chancery</mentioned>, <mentioned>italiano</mentioned>, ecc.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">caracteriza un determinado estilo de escritura utilizado por la mano en cuestión, p.ej. <mentioned>secretario</mentioned>, <mentioned>grabado sobre cobre</mentioned>, <mentioned>cancelleresco</mentioned>, <mentioned>italiano</mentioned>, etc.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef ident="scriptRef">
      <desc versionDate="2010-09-28" xml:lang="en">points to a full description of the script or writing style used by this hand, typically supplied by a <gi>scriptNote</gi> element elsewhere in the description.</desc>
      <desc versionDate="2019-09-16" xml:lang="ja">問題の筆体や書記スタイルについての詳細な記述へポイントする。典型的には記述のどこかで<gi>scriptNote</gi>要素によって補われる。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="medium">
      <desc versionDate="2007-09-27" xml:lang="en">describes the tint or type of ink, e.g. <mentioned>brown</mentioned>, or other writing medium, e.g. <mentioned>pencil</mentioned>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"><mentioned>brown</mentioned>와 같이 잉크의 색 또는 유형, 또는 <mentioned>pencil</mentioned>와 같이 글쓰기 방식 기술한다.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">インクの種類や色合い、例えば、<mentioned>茶色</mentioned> や、筆記具の種類、例えば、<mentioned>鉛筆</mentioned>など。</desc>
      <desc versionDate="2009-05-29" xml:lang="fr">décrit la teinte ou le type d'encre, par exemple <mentioned>brune</mentioned>, ou un autre outil d'écriture, par exemple un <mentioned>crayon</mentioned>.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">descrive la tinta o il tipo di inchiostro, per esempio <mentioned>marrone</mentioned>, o altri strumenti di scrittura, per esempio <mentioned>matita</mentioned></desc>
      <desc versionDate="2007-05-04" xml:lang="es">describe la tinta o el tipo de tinta, p.ej. <mentioned>marrón</mentioned>, u otros instrumentos de escritura, p.ej. <mentioned>lápiz</mentioned>.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
  </attList>
  <remarks ident="att.handFeatures-remarks" versionDate="2026-01-03" xml:lang="en">
    <p>These guidelines provide no semantic basis or suggested
    precedence when both <att>script</att> and <att>scriptRef</att> or
    when both <att>scribe</att> and <att>scribeRef</att> are
    provided. For this reason simultaneous use of either pair of
    attributes is not recommended for interchange unless documentation
    explaining the use is provided, probably in an ODD
    customization.</p>
  </remarks>
  <remarks ident="att.handFeatures-remarks" versionDate="2019-09-16" xml:lang="ja">
    <p>通常は <att>script</att> または <att>scriptRef</att> そして同様に、 <att>scribe</att> あるいは <att>scribeRef</att> が用いられるだろう。</p>
  </remarks>
  <listRef>
    <ptr target="#PHDH"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-27" xml:lang="en">provides attributes describing aspects of the hand in which a manuscript is written.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고가 쓰여진 필적의 측면을 기술하는 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona atributos que describen los aspectos de la mano que ha escrito un manuscrito.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の筆致に関する情報を表す情報を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">fournit des attributs décrivant les caractéristiques de la main par laquelle un manuscrit est écrit.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica degli attributi che descrivono aspetti delle mano utilizzata per la scrittura del manoscritto.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.scope"/>
  </classes>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2010-09-28" xml:lang="en">gives a name or other identifier for the scribe believed to be responsible for this hand.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 필적에 대한 책임이 있다고 간주되는 필기사에 대한 표준명 또는 다른 확인소를 제시한다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2019-09-16" xml:lang="ja">当該筆致に対応すると考えられる筆写者の名前またはその他の識別子を示す。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">donne un nom normalisé ou un autre identifiant pour le scribe reconnu comme responsable de cette main.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un nome o altro identificatore standard al trascrittore che si ritiene corrisponda alla mano in questione.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">asigna un nombre u otro identificador estándard para el transcriptor que se identifica con la mano en cuestión.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2010-09-28" xml:lang="en">points to a full description of the scribe concerned, typically supplied by a <gi>person</gi> element elsewhere in the description.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2019-09-16" xml:lang="ja">問題の筆写者についての詳細な記述へポイントする。典型的には記述のどこかで<gi>person</gi>要素によって補われる。</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2008-02-01" xml:lang="en">characterizes the particular script or writing style used by this hand, for example <mentioned>secretary</mentioned>, <mentioned>copperplate</mentioned>, <mentioned>Chancery</mentioned>, <mentioned>Italian</mentioned>, etc.</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><mentioned>secretary</mentioned>, <mentioned>copperplate</mentioned>, <mentioned>Chancery</mentioned>, <mentioned>Italian</mentioned> 등과 같이 이 필적으로 사용된 특별한 필사본 또는 글쓰기 스타일의 특성을 기술한다.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該筆致で使用されている特定の筆体や書記スタイルの特徴を示す。例 えば、<mentioned>secretary(書記官スタイル)</mentioned>、 <mentioned>copperplate(銅板スタイル)</mentioned>、 <mentioned>Chancery(公文書スタイル)</mentioned>、 <mentioned>Italian(イタリアスタイル)</mentioned>など。</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">caractérise la calligraphie ou le style d'écriture particuliers utilisés par cette main, par exemple <mentioned>écriture anglaise</mentioned>, <mentioned>de chancellerie</mentioned>, <mentioned>italienne</mentioned>, etc.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">caratterizza un determinato stile di scrittura utilizzato dalla mano in questione, per esempio <mentioned>segretario</mentioned>, <mentioned>incisione su rame</mentioned>, <mentioned>Chancery</mentioned>, <mentioned>italiano</mentioned>, ecc.</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">caracteriza un determinado estilo de escritura utilizado por la mano en cuestión, p.ej. <mentioned>secretario</mentioned>, <mentioned>grabado sobre cobre</mentioned>, <mentioned>cancelleresco</mentioned>, <mentioned>italiano</mentioned>, etc.</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.name"/></datatype>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2010-09-28" xml:lang="en">points to a full description of the script or writing style used by this hand, typically supplied by a <gi>scriptNote</gi> element elsewhere in the description.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2019-09-16" xml:lang="ja">問題の筆体や書記スタイルについての詳細な記述へポイントする。典型的には記述のどこかで<gi>scriptNote</gi>要素によって補われる。</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2007-09-27" xml:lang="en">describes the tint or type of ink, e.g. <mentioned>brown</mentioned>, or other writing medium, e.g. <mentioned>pencil</mentioned>.</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><mentioned>brown</mentioned>와 같이 잉크의 색 또는 유형, 또는 <mentioned>pencil</mentioned>와 같이 글쓰기 방식 기술한다.</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">インクの種類や色合い、例えば、<mentioned>茶色</mentioned> や、筆記具の種類、例えば、<mentioned>鉛筆</mentioned>など。</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2009-05-29" xml:lang="fr">décrit la teinte ou le type d'encre, par exemple <mentioned>brune</mentioned>, ou un autre outil d'écriture, par exemple un <mentioned>crayon</mentioned>.</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive la tinta o il tipo di inchiostro, per esempio <mentioned>marrone</mentioned>, o altri strumenti di scrittura, per esempio <mentioned>matita</mentioned></desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la tinta o el tipo de tinta, p.ej. <mentioned>marrón</mentioned>, u otros instrumentos de escritura, p.ej. <mentioned>lápiz</mentioned>.</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
```

^b34

### Block 35

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.handFeatures-remarks" versionDate="2026-01-03" xml:lang="en">
    <p>These guidelines provide no semantic basis or suggested
    precedence when both <att>script</att> and <att>scriptRef</att> or
    when both <att>scribe</att> and <att>scribeRef</att> are
    provided. For this reason simultaneous use of either pair of
    attributes is not recommended for interchange unless documentation
    explaining the use is provided, probably in an ODD
    customization.</p>
  </remarks>
```

^b35

### Block 36

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.handFeatures-remarks" versionDate="2019-09-16" xml:lang="ja">
    <p>通常は <att>script</att> または <att>scriptRef</att> そして同様に、 <att>scribe</att> あるいは <att>scribeRef</att> が用いられるだろう。</p>
  </remarks>
```

^b36

### Block 37

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDH"/>
  </listRef>
```

^b37

