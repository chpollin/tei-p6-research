---
type: representation
source-type: document
source: '[[00_sources/tei-p5-origplace-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 origPlace
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/origPlace.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# origPlace

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3315. Git blob: `691e8dac005b33387d0593dab7bf692ff8550fb9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="ORIGPLACE" ident="origPlace">
  <gloss versionDate="2007-07-04" xml:lang="en">origin place</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">생산 장소</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">lugar de origen</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">lieu de création</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">luogo di origine</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="origplace.desc">contains any form of place name, used to identify the place of origin for a manuscript, manuscript part, or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 일부를 생산한 장소를 식별하는 장소 이름 형식을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何格式的地名，用以確認手稿或手稿部分的來源地點。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料が生まれた場所を特定するための場所を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un nom de lieu, dans une forme libre, utilisé pour désigner l'endroit où a été produit un manuscrit ou une partie d'un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de nombre de lugar utilizado para indicar el lugar de origen de un manuscrito o de una de sus partes.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi nome di luogo utilizzato per indicare il luogo di origine di un manoscritto o di una sua parte.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGPLACE-egXML-ig">
      <origPlace>Birmingham</origPlace>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGPLACE-egXML-lh">
      <origPlace>Birmingham</origPlace>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGPLACE-egXML-hq">
      <origPlace>伯明罕</origPlace>
    </egXML>
  </exemplum>
  <remarks ident="origPlace-remarks" versionDate="2008-09-08" xml:lang="en">
    <p>The <att>type</att> attribute may be used to distinguish
different kinds of <soCalled>origin</soCalled>, for example original
place of publication, as opposed to original place of
printing.</p>
  </remarks>
  <listRef>
    <ptr target="#msdates"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">origin place</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">생산 장소</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">lugar de origen</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">lieu de création</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">luogo di origine</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="origplace.desc">contains any form of place name, used to identify the place of origin for a manuscript, manuscript part, or other object.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 일부를 생산한 장소를 식별하는 장소 이름 형식을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何格式的地名，用以確認手稿或手稿部分的來源地點。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料が生まれた場所を特定するための場所を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un nom de lieu, dans une forme libre, utilisé pour désigner l'endroit où a été produit un manuscrit ou une partie d'un manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de nombre de lugar utilizado para indicar el lugar de origen de un manuscrito o de una de sus partes.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi nome di luogo utilizzato per indicare il luogo di origine di un manoscritto o di una sua parte.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGPLACE-egXML-ig">
      <origPlace>Birmingham</origPlace>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGPLACE-egXML-lh">
      <origPlace>Birmingham</origPlace>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGPLACE-egXML-hq">
      <origPlace>伯明罕</origPlace>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="origPlace-remarks" versionDate="2008-09-08" xml:lang="en">
    <p>The <att>type</att> attribute may be used to distinguish
different kinds of <soCalled>origin</soCalled>, for example original
place of publication, as opposed to original place of
printing.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msdates"/>
  </listRef>
```

^b20

