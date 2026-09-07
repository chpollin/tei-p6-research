---
type: representation
source-type: document
source: '[[00_sources/tei-p5-camera-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 camera
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/camera.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# camera

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2964. Git blob: `783b3e6cd2093f441ac0a66bcba9e98056ffd1a4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-camera" ident="camera">
  <gloss versionDate="2007-06-12" xml:lang="en">camera</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">angle de prise de vue</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes a particular camera angle or viewpoint in a screen play.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">시나리오에서 특정 카메라 각도 또는 관점을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述電影視劇本中攝影機的某特定視角或觀看角度。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">describe un ángulo de cámara o un punto de vista determinado en un escenario.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">撮影時の、カメラアングルや視点を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit un angle de prise de vue ou un plan dans un
      scénario.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive un particolare angolatura o punto di vista in una sceneggiatura.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-camera-egXML-ep" source="#FieldScreen">
      <view>George glances at the window—and freezes.
<camera type="cut">New angle—shock cut</camera>
Out the window the body of a dead man suddenly slams into frame
</view>
    </egXML><!-- quoted in Syd Field Definitive Guide to Screen writing --></exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-camera-egXML-xn" source="#fr-ex-Zazie">
      <view><camera type="plan">Plan américain (très légère plongée)</camera> de la plate-forme
          bondée. <camera type="mouvement">Pano</camera> sur Klein qui se glisse dans le couloir
          intérieur du véhicule, jusqu'à une jeune femme qui se tient debout. </view>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-camera-egXML-ec">
      <view>喬治望向窗戶，凍住。 <camera type="cut">新角度—shock
        cut（凝住）</camera> 窗外一具屍體突然砰向畫面</view>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DRTEC" type="div3"/>
    <ptr target="#DROTH"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">camera</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">angle de prise de vue</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes a particular camera angle or viewpoint in a screen play.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시나리오에서 특정 카메라 각도 또는 관점을 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述電影視劇本中攝影機的某特定視角或觀看角度。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">describe un ángulo de cámara o un punto de vista determinado en un escenario.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">撮影時の、カメラアングルや視点を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit un angle de prise de vue ou un plan dans un
      scénario.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive un particolare angolatura o punto di vista in una sceneggiatura.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-camera-egXML-ep" source="#FieldScreen">
      <view>George glances at the window—and freezes.
<camera type="cut">New angle—shock cut</camera>
Out the window the body of a dead man suddenly slams into frame
</view>
    </egXML><!-- quoted in Syd Field Definitive Guide to Screen writing --></exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-camera-egXML-xn" source="#fr-ex-Zazie">
      <view><camera type="plan">Plan américain (très légère plongée)</camera> de la plate-forme
          bondée. <camera type="mouvement">Pano</camera> sur Klein qui se glisse dans le couloir
          intérieur du véhicule, jusqu'à une jeune femme qui se tient debout. </view>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-camera-egXML-ec">
      <view>喬治望向窗戶，凍住。 <camera type="cut">新角度—shock
        cut（凝住）</camera> 窗外一具屍體突然砰向畫面</view>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRTEC" type="div3"/>
    <ptr target="#DROTH"/>
  </listRef>
```

^b15

