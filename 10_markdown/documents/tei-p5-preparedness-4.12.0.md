---
type: representation
source-type: document
source: '[[00_sources/tei-p5-preparedness-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 preparedness
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/preparedness.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# preparedness

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6295. Git blob: `5de21612c3938c81aba95daffdc9db90f8837b7f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="corpus" xml:id="gi-preparedness" ident="preparedness">
  <gloss versionDate="2007-06-12" xml:lang="en">preparedness</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">degré de préparation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the extent to which a text may be regarded as
prepared or spontaneous.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 준비된 것 또는 자발적인 것으로 간주될 수 있는지의 범위를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述文本可能被視為經過準備或自然呈現的程度。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストが準備されたものか、即興的なものかの程度を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit le degré de préparation ou de spontanéité d'un texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe la posibilidad de considerar un texto como preparado o espontáneo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive quanto un testo possa essere considerato preparato o spontaneo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.textDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">a keyword characterizing the type of preparedness.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">준비성의 유형의 특성을 기술하는 키워드</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明準備程度的類型。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">即興度の種類を示すキーワード。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">un mot clé caractérisant le type de préparation</desc>
      <desc versionDate="2007-05-04" xml:lang="es">una palabra clave que caracteriza el tipo de preparación.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">una parola chiava che caratterizza il grado di spontaneità.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="none">
          <desc versionDate="2007-06-27" xml:lang="en">spontaneous or unprepared</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">자발적 또는 준비되지 않은</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">自然呈現或未經準備</desc>
          <desc versionDate="2008-04-06" xml:lang="es">espontáneo o sin preparación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">即興または準備されていない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">spontané ou non préparé.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">spontaneo o non preparato.</desc>
        </valItem>
        <valItem ident="scripted">
          <desc versionDate="2007-06-27" xml:lang="en">follows a script</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">스크립트를 따른다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">依照稿子</desc>
          <desc versionDate="2008-04-06" xml:lang="es">sigue un guión</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">台本に従う。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">suit un script.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">segue un copione.</desc>
        </valItem>
        <valItem ident="formulaic">
          <desc versionDate="2007-06-27" xml:lang="en">follows a predefined set of conventions</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">미리 규정된 관례를 따른다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">依照一套事先定義的常規</desc>
          <desc versionDate="2008-04-06" xml:lang="es">sigue un conjunto predefinido de convenciones</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">事前の打ち合わせに従う。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">suit un ensemble de conventions
prédéfini.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">segue una serie di convenzioni predefinite.</desc>
        </valItem>
        <valItem ident="revised">
          <desc versionDate="2007-06-27" xml:lang="en">polished or revised before presentation</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">제시되기 전 다듬거나 수정된</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本呈現前事先經過潤飾或修訂</desc>
          <desc versionDate="2008-04-06" xml:lang="es">revisado antes de la presentación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">事前の準備が練り直しまたは修正されている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">affiné ou révisé avant la
présentation.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">materiale pulito o revisionato prima della presentazione.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-preparedness-egXML-wm" source="#UND">
      <preparedness type="none"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-preparedness-egXML-no" source="#UND">
      <preparedness type="none"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-preparedness-egXML-am" source="#UND">
      <preparedness type="無"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">preparedness</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">degré de préparation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the extent to which a text may be regarded as
prepared or spontaneous.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트가 준비된 것 또는 자발적인 것으로 간주될 수 있는지의 범위를 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述文本可能被視為經過準備或自然呈現的程度。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストが準備されたものか、即興的なものかの程度を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit le degré de préparation ou de spontanéité d'un texte.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la posibilidad de considerar un texto como preparado o espontáneo.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive quanto un testo possa essere considerato preparato o spontaneo.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.textDescPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">a keyword characterizing the type of preparedness.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">준비성의 유형의 특성을 기술하는 키워드</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明準備程度的類型。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">即興度の種類を示すキーワード。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">un mot clé caractérisant le type de préparation</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">una palabra clave que caracteriza el tipo de preparación.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">una parola chiava che caratterizza il grado di spontaneità.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="none">
          <desc versionDate="2007-06-27" xml:lang="en">spontaneous or unprepared</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">자발적 또는 준비되지 않은</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">自然呈現或未經準備</desc>
          <desc versionDate="2008-04-06" xml:lang="es">espontáneo o sin preparación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">即興または準備されていない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">spontané ou non préparé.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">spontaneo o non preparato.</desc>
        </valItem>
        <valItem ident="scripted">
          <desc versionDate="2007-06-27" xml:lang="en">follows a script</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">스크립트를 따른다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">依照稿子</desc>
          <desc versionDate="2008-04-06" xml:lang="es">sigue un guión</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">台本に従う。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">suit un script.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">segue un copione.</desc>
        </valItem>
        <valItem ident="formulaic">
          <desc versionDate="2007-06-27" xml:lang="en">follows a predefined set of conventions</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">미리 규정된 관례를 따른다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">依照一套事先定義的常規</desc>
          <desc versionDate="2008-04-06" xml:lang="es">sigue un conjunto predefinido de convenciones</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">事前の打ち合わせに従う。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">suit un ensemble de conventions
prédéfini.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">segue una serie di convenzioni predefinite.</desc>
        </valItem>
        <valItem ident="revised">
          <desc versionDate="2007-06-27" xml:lang="en">polished or revised before presentation</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">제시되기 전 다듬거나 수정된</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本呈現前事先經過潤飾或修訂</desc>
          <desc versionDate="2008-04-06" xml:lang="es">revisado antes de la presentación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">事前の準備が練り直しまたは修正されている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">affiné ou révisé avant la
présentation.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">materiale pulito o revisionato prima della presentazione.</desc>
        </valItem>
      </valList>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-preparedness-egXML-wm" source="#UND">
      <preparedness type="none"/>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-preparedness-egXML-no" source="#UND">
      <preparedness type="none"/>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-preparedness-egXML-am" source="#UND">
      <preparedness type="無"/>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
```

^b24

