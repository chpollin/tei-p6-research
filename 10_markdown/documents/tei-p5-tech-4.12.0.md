---
type: representation
source-type: document
source: '[[00_sources/tei-p5-tech-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 tech
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/tech.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# tech

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6202. Git blob: `4ae8d9a16c17be70f498e933c4d67e90c39fd252`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-tech" ident="tech">
  <gloss versionDate="2007-07-04" xml:lang="en">technical stage direction</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">전문적 무대 지시</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">技術性舞台指示</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">dirección técnica de escena</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">indication technique de mise en scène</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">Indicazioni i scena tecniche</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes a special-purpose stage direction that is not
meant for the actors.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">배우들에 지시하는 것이 아니라, 특별한 목적의 무대 지시를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述一個具有特殊目的，但並非針對演員的舞台指示。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">describe una indicación de escena particular que no se menciona para los personajes.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">役者以外に向けた、特別なト書きを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indication technique particulière de mise en scène qui n'est pas
      destinée aux acteurs.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive particolari indicazioni di scena non indirizzate agli attori.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">categorizes the technical stage direction.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">전문적 무대 지시를 분류한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">技術性舞台指示類型</desc>
      <desc versionDate="2008-04-06" xml:lang="es">categoriza la dirección técnica de escena</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該ト書きを分類する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">catégorise l'indication technique de mise en
          scène.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica l'indicazione di scena tecnica.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="light">
          <desc versionDate="2007-06-27" xml:lang="en">a lighting cue</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">조명 신호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">燈光提示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una señal de iluminación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">照明への指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">signal lumineux.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un segnale luminoso.</desc>
        </valItem>
        <valItem ident="sound">
          <desc versionDate="2007-06-27" xml:lang="en">a sound cue</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">음향 신호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">音效提示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una señal de sonido</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">音響効果への指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">signal sonore</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un segnale sonoro.</desc>
        </valItem>
        <valItem ident="prop">
          <desc versionDate="2007-06-27" xml:lang="en">a prop cue</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">소품 신호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">道具提示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una señal de apoyo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">小道具への指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indication d'accessoires</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un battuta d'entrata.</desc>
        </valItem>
        <valItem ident="block">
          <desc versionDate="2007-06-27" xml:lang="en">a blocking instruction</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">연출 지시</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台調度指示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una instrucción de bloqueo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">振り付けの指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indication des marques.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un indicazione di arresto.</desc>
        </valItem>
      </valList>
    </attDef>
   
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tech-egXML-kx">
      <tech type="light">Red spot on his face</tech>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tech-egXML-do">
      <tech type="light">lumière rouge sur son visage</tech>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tech-egXML-to">
      <tech type="light">紅光打在他臉上</tech>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DRTEC" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">technical stage direction</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">전문적 무대 지시</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">技術性舞台指示</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">dirección técnica de escena</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">indication technique de mise en scène</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">Indicazioni i scena tecniche</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes a special-purpose stage direction that is not
meant for the actors.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">배우들에 지시하는 것이 아니라, 특별한 목적의 무대 지시를 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述一個具有特殊目的，但並非針對演員的舞台指示。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">describe una indicación de escena particular que no se menciona para los personajes.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">役者以外に向けた、特別なト書きを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indication technique particulière de mise en scène qui n'est pas
      destinée aux acteurs.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive particolari indicazioni di scena non indirizzate agli attori.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">categorizes the technical stage direction.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전문적 무대 지시를 분류한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">技術性舞台指示類型</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">categoriza la dirección técnica de escena</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該ト書きを分類する。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">catégorise l'indication technique de mise en
          scène.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica l'indicazione di scena tecnica.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="light">
          <desc versionDate="2007-06-27" xml:lang="en">a lighting cue</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">조명 신호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">燈光提示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una señal de iluminación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">照明への指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">signal lumineux.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un segnale luminoso.</desc>
        </valItem>
        <valItem ident="sound">
          <desc versionDate="2007-06-27" xml:lang="en">a sound cue</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">음향 신호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">音效提示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una señal de sonido</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">音響効果への指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">signal sonore</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un segnale sonoro.</desc>
        </valItem>
        <valItem ident="prop">
          <desc versionDate="2007-06-27" xml:lang="en">a prop cue</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">소품 신호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">道具提示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una señal de apoyo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">小道具への指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indication d'accessoires</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un battuta d'entrata.</desc>
        </valItem>
        <valItem ident="block">
          <desc versionDate="2007-06-27" xml:lang="en">a blocking instruction</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">연출 지시</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台調度指示</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una instrucción de bloqueo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">振り付けの指示。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indication des marques.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un indicazione di arresto.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tech-egXML-kx">
      <tech type="light">Red spot on his face</tech>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tech-egXML-do">
      <tech type="light">lumière rouge sur son visage</tech>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tech-egXML-to">
      <tech type="light">紅光打在他臉上</tech>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRTEC" type="div3"/>
  </listRef>
```

^b28

