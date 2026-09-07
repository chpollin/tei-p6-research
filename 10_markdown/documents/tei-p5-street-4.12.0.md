---
type: representation
source-type: document
source: '[[00_sources/tei-p5-street-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 street
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/street.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# street

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4214. Git blob: `531485c5f7abee703e8c126cca4d9c5763e6e399`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-street" ident="street">
  <desc versionDate="2012-12-27" xml:lang="en">contains a full street address including any name or number identifying a
        building as well as the name of the street or route on which it is
        located.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">거리 또는 도로 이름을 비롯하여 건물을 식별할 수 있는 이름 및 번지를 포함하는 전체 주소.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">完整的街道地址，包含任何名稱或數字，用以識別一棟建築物以及所在街道名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">住所情報としての、通りを表す完全情報を示す。建物の名前や番号、通りの
        名前など。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">adresse complète d'une rue comprenant un nom
        ou un numéro identifiant un bâtiment ainsi que le nom de la rue ou du chemin sur laquelle
        il est situé.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">una dirección postal completa, incluyendo cualquier nombre o número identificativo para identificar el edifio, como el nombre de la calle o carretera.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indirizzo postale completo, incluso il nome o il numero che identifica l'edificio, così come il nome della strada dove è situato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.addrPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-nr">
      <street>via della Faggiola, 36</street>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-sy">
      <street>110, rue de Grenelle </street>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-vt">
      <street>36, quai des Orfèvres</street>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-zy">
      <street>天津街25號</street>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-ph">
      <street>皇后大道東123號<name>灣仔大廈</name>
         </street>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-ml">
      <street><name>Duntaggin</name>, 110 Southmoor Road</street>
    </egXML>
  </exemplum>
  <remarks ident="street-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The order and presentation of house names and numbers and
            street names, etc., may vary considerably in different countries.  The
            encoding should reflect the order which is appropriate in the country
            concerned. </p>
  </remarks>
  <remarks ident="street-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'ordre et la présentation des noms et numéros de maisons et des noms de rues, etc.
            L'encodage peut varier considérablement selon les pays ; il devrait reprendre la disposition
            propre au pays concerné. </p>
  </remarks>
  <remarks ident="street-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            家屋の名や番号、通りの名前などの表記順番は、国により異なる。符号化
            する際には、その国の習慣に合った順番にすべきである。
        </p>
  </remarks>
  <listRef>
    <ptr target="#CONAAD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains a full street address including any name or number identifying a
        building as well as the name of the street or route on which it is
        located.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">거리 또는 도로 이름을 비롯하여 건물을 식별할 수 있는 이름 및 번지를 포함하는 전체 주소.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">完整的街道地址，包含任何名稱或數字，用以識別一棟建築物以及所在街道名稱。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">住所情報としての、通りを表す完全情報を示す。建物の名前や番号、通りの
        名前など。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">adresse complète d'une rue comprenant un nom
        ou un numéro identifiant un bâtiment ainsi que le nom de la rue ou du chemin sur laquelle
        il est situé.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">una dirección postal completa, incluyendo cualquier nombre o número identificativo para identificar el edifio, como el nombre de la calle o carretera.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indirizzo postale completo, incluso il nome o il numero che identifica l'edificio, così come il nome della strada dove è situato.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.addrPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-nr">
      <street>via della Faggiola, 36</street>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-sy">
      <street>110, rue de Grenelle </street>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-vt">
      <street>36, quai des Orfèvres</street>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-zy">
      <street>天津街25號</street>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-ph">
      <street>皇后大道東123號<name>灣仔大廈</name>
         </street>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-street-egXML-ml">
      <street><name>Duntaggin</name>, 110 Southmoor Road</street>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="street-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The order and presentation of house names and numbers and
            street names, etc., may vary considerably in different countries.  The
            encoding should reflect the order which is appropriate in the country
            concerned. </p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="street-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'ordre et la présentation des noms et numéros de maisons et des noms de rues, etc.
            L'encodage peut varier considérablement selon les pays ; il devrait reprendre la disposition
            propre au pays concerné. </p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="street-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            家屋の名や番号、通りの名前などの表記順番は、国により異なる。符号化
            する際には、その国の習慣に合った順番にすべきである。
        </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONAAD"/>
  </listRef>
```

^b19

