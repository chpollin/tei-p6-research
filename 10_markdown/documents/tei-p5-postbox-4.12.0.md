---
type: representation
source-type: document
source: '[[00_sources/tei-p5-postbox-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 postBox
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/postBox.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# postBox

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4095. Git blob: `af607d9020e1d42e08e97831153a9b0efd57c1b5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-postBox" ident="postBox">
  <gloss versionDate="2007-07-04" xml:lang="en">postal box or post office box</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">우편함 또는 사서함</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">郵政信箱</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">boîte postale</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">buzón</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">Casella postale</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Postfach</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a number or other identifier for some postal delivery point other than a street
    address.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">주소 이외의 우편 배달 지점을 위한 숫자 또는 다른 확인소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個數字或其他識別名稱，標示街道地址之外的郵件寄送點。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">郵便配達で識別子となる、通り名以外の、数値などを示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un numéro ou un autre identifiant d'un lieu de
    distribution du courrier autre qu'un nom de rue.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un número u otro identificador para algún punto
    de entrega postal distinto a una dirección postal.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il numero o altro identificatore per un luogo di
    consegna della posta diverso da un indirizzo postale.</desc>
  <desc versionDate="2024-04-11" xml:lang="de">enthält eine Nummer oder eine andere Kennung für eine Postanschrift,
    bei der es sich nicht um eine Straßenadresse handelt.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.addrPart"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-wa">
      <postBox>P.O. Box 280</postBox>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-ky">
      <postBox>B.P. 4232 </postBox>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-dn">
      <postBox>BP 3317</postBox>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-dv">
      <postBox>廣州郵局第280號信箱</postBox>
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-pr">
      <postBox>Postbus 532</postBox>
    </egXML>
  </exemplum>
  <remarks ident="postBox-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The position and nature of postal codes is highly country-specific; the conventions
      appropriate to the country concerned should be used.</p>
  </remarks>
  <remarks ident="postBox-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La disposition et la nature des codes postaux est spécifique à chaque pays ; on utilise les
      conventions qui leur sont propres .</p>
  </remarks>
  <remarks ident="postBox-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 郵便番号の位置づけや性質は、国家に強く依存する。国の事情にあった方 式が採用されるべきである。 </p>
  </remarks>
  <listRef>
    <ptr target="#CONAAD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">postal box or post office box</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">우편함 또는 사서함</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">郵政信箱</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">boîte postale</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">buzón</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">Casella postale</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Postfach</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a number or other identifier for some postal delivery point other than a street
    address.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">주소 이외의 우편 배달 지점을 위한 숫자 또는 다른 확인소를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個數字或其他識別名稱，標示街道地址之外的郵件寄送點。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">郵便配達で識別子となる、通り名以外の、数値などを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient un numéro ou un autre identifiant d'un lieu de
    distribution du courrier autre qu'un nom de rue.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un número u otro identificador para algún punto
    de entrega postal distinto a una dirección postal.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il numero o altro identificatore per un luogo di
    consegna della posta diverso da un indirizzo postale.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2024-04-11" xml:lang="de">enthält eine Nummer oder eine andere Kennung für eine Postanschrift,
    bei der es sich nicht um eine Straßenadresse handelt.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.addrPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-wa">
      <postBox>P.O. Box 280</postBox>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-ky">
      <postBox>B.P. 4232 </postBox>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-dn">
      <postBox>BP 3317</postBox>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-dv">
      <postBox>廣州郵局第280號信箱</postBox>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postBox-egXML-pr">
      <postBox>Postbus 532</postBox>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="postBox-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The position and nature of postal codes is highly country-specific; the conventions
      appropriate to the country concerned should be used.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="postBox-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La disposition et la nature des codes postaux est spécifique à chaque pays ; on utilise les
      conventions qui leur sont propres .</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="postBox-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 郵便番号の位置づけや性質は、国家に強く依存する。国の事情にあった方 式が採用されるべきである。 </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONAAD"/>
  </listRef>
```

^b26

