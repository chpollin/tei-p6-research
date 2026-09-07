---
type: representation
source-type: document
source: '[[00_sources/tei-p5-equipment-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 equipment
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/equipment.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# equipment

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4479. Git blob: `d8280d975ac850eb55ba252f4507c948d14bf358`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="spoken" xml:id="gi-equipment" ident="equipment">
  <gloss versionDate="2009-04-17" xml:lang="en">equipment</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">matériel</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides technical details of the equipment and media used for
an audio or video recording used as the source for a spoken text.</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">fournit des détails techniques sur les appareils et les supports servant à l’enregistrement audio ou vidéo utilisé comme source de la parole transcrite.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트의 원본으로 사용된 오디오 또는 비디오 녹음에 동원된 장비 및 매체에 대한 기술적인 상세 항목을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供錄製設備及媒介的技術性細節，該設備及媒介用於口說文本來源之影像或聲音錄製。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話テキストを録音・録画する際に使用された機器や媒体の技術的詳細を示
  す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">gibt die technischen
  Details zu Geräteausstattung und Medien an, welche für die Ton- oder
  Videoaufnahme als Quelle des gesprochenen Textes benutzt wurden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona detalles técnicos sobre el equipo y los medios empleados para la grabación de un audio o video usados como fuente de un texto hablado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce dettagli tecnici sull'attrezzatura per una registrazione audio o video utilizzata quale fonte di un testo orale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.recordingPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>    
  </content>
  <constraintSpec ident="equipment-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:equipment"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-gt">
      <equipment>
        <p>"Hi-8" 8 mm NTSC camcorder with integral directional
  microphone and windshield and stereo digital sound
  recording channel.
  </p>
      </equipment>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-ih">
      <equipment>
        <p>Enregistreur numérique avec connexion USB et 512 Mo de mémoire intégrée</p>
      </equipment>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-pq">
      <equipment>
        <p>enregistreur numérique 16 pistes</p>
      </equipment>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-os" source="#fr-ex-la-bas-si-jy-suis">
      <broadcast>
        <p>
          <!-- ... -->
        </p>
      </broadcast>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-qr">
      <equipment>
        <p>內建麥克風、立體聲音響以及數位錄音聲道的"Hi-8" 的8釐米NTSC攝錄像機。</p>
      </equipment>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-gi">
      <equipment>
        <p>8-track analogue transfer mixed down to 19 cm/sec audio
 tape for cassette mastering</p>
      </equipment>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD32"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="en">equipment</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">matériel</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides technical details of the equipment and media used for
an audio or video recording used as the source for a spoken text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">fournit des détails techniques sur les appareils et les supports servant à l’enregistrement audio ou vidéo utilisé comme source de la parole transcrite.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트의 원본으로 사용된 오디오 또는 비디오 녹음에 동원된 장비 및 매체에 대한 기술적인 상세 항목을 제공한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供錄製設備及媒介的技術性細節，該設備及媒介用於口說文本來源之影像或聲音錄製。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話テキストを録音・録画する際に使用された機器や媒体の技術的詳細を示
  す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt die technischen
  Details zu Geräteausstattung und Medien an, welche für die Ton- oder
  Videoaufnahme als Quelle des gesprochenen Textes benutzt wurden.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona detalles técnicos sobre el equipo y los medios empleados para la grabación de un audio o video usados como fuente de un texto hablado.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce dettagli tecnici sull'attrezzatura per una registrazione audio o video utilizzata quale fonte di un testo orale.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.recordingPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>    
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="equipment-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:equipment"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-gt">
      <equipment>
        <p>"Hi-8" 8 mm NTSC camcorder with integral directional
  microphone and windshield and stereo digital sound
  recording channel.
  </p>
      </equipment>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-ih">
      <equipment>
        <p>Enregistreur numérique avec connexion USB et 512 Mo de mémoire intégrée</p>
      </equipment>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-pq">
      <equipment>
        <p>enregistreur numérique 16 pistes</p>
      </equipment>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-os" source="#fr-ex-la-bas-si-jy-suis">
      <broadcast>
        <p>
          <!-- ... -->
        </p>
      </broadcast>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-qr">
      <equipment>
        <p>內建麥克風、立體聲音響以及數位錄音聲道的"Hi-8" 的8釐米NTSC攝錄像機。</p>
      </equipment>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-equipment-egXML-gi">
      <equipment>
        <p>8-track analogue transfer mixed down to 19 cm/sec audio
 tape for cassette mastering</p>
      </equipment>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD32"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b20

