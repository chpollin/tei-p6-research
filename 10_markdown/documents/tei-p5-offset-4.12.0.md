---
type: representation
source-type: document
source: '[[00_sources/tei-p5-offset-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 offset
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/offset.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# offset

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2885. Git blob: `0cdbd6856159415e896789d5492e430d44f7cbc0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-offset" ident="offset">
  <gloss versionDate="2008-12-09" xml:lang="en">offset</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">distance relative</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">marks that part of a relative temporal or spatial expression which indicates the direction of the offset between the two place names, dates, or times involved in the expression.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표현에 포함된 두 장소명, 날짜, 또는 시간 사이의 차이 방향을 표시하는 상대적 시간 또는 공간 표현의 부분</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在時間或空間差距的表示中，該部分指出兩個地名、日期、或時間之間差距的方向性。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該表現に含まれている2つの場所名、日付、時間のオフセットの方向を示 す、相対的な時空表現の部分を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">la partie d'une expression temporelle ou spatiale qui indique la distance et/ou la direction entre les deux lieux, dates ou heures sur lesquels porte l'expression.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">la parte de una expresión temporal o espacial relativa que indica la dirección del desfase entre dos nombres de lugar, fecha u horario al interno de la expresión.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">la parte di un'espressione temporale o spaziale relativa che indica la direzione dello sfasamento tra due nomi di luogo, date o orari all'interno dell'espressione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.offsetLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-offset-egXML-so">
      <placeName key="NRPA1">
        <offset>50 metres below the summit of</offset>
        <geogName>
          <geogFeat>Mount</geogFeat>
          <name>Sinai</name>
        </geogName>
      </placeName>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">offset</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">distance relative</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">marks that part of a relative temporal or spatial expression which indicates the direction of the offset between the two place names, dates, or times involved in the expression.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표현에 포함된 두 장소명, 날짜, 또는 시간 사이의 차이 방향을 표시하는 상대적 시간 또는 공간 표현의 부분</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在時間或空間差距的表示中，該部分指出兩個地名、日期、或時間之間差距的方向性。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該表現に含まれている2つの場所名、日付、時間のオフセットの方向を示 す、相対的な時空表現の部分を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">la partie d'une expression temporelle ou spatiale qui indique la distance et/ou la direction entre les deux lieux, dates ou heures sur lesquels porte l'expression.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">la parte de una expresión temporal o espacial relativa que indica la dirección del desfase entre dos nombres de lugar, fecha u horario al interno de la expresión.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">la parte di un'espressione temporale o spaziale relativa che indica la direzione dello sfasamento tra due nomi di luogo, date o orari all'interno dell'espressione.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.offsetLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-offset-egXML-so">
      <placeName key="NRPA1">
        <offset>50 metres below the summit of</offset>
        <geogName>
          <geogFeat>Mount</geogFeat>
          <name>Sinai</name>
        </geogName>
      </placeName>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
```

^b13

