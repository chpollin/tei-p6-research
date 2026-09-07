---
type: representation
source-type: document
source: '[[00_sources/tei-p5-postcode-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 postCode
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/postCode.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# postCode

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4585. Git blob: `eac082a7cf6716034b077e82d9dfb5a1781e6ec4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-postCode" ident="postCode">
  <gloss versionDate="2007-07-04" xml:lang="en">postal code</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">우편 번호</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">郵遞區號</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">code postal</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">Código postal</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">Codice di Avviamento Postale</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Postleitzahl</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a numerical or alphanumeric code used as part of a postal address to simplify
        sorting or delivery of mail.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">우편의 분류 및 배달을 용이하도록 우편 주소의 일부로 사용되는 숫자 또는 문자와 숫자가 혼용된
        기호.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個數字或字母加數字的區域代碼，屬於郵寄地址的一部分，用以簡化郵件的分類及寄送工作。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">郵便の配達や区分けを簡単にするための、郵便の宛名情報の部分となる数値 または文字を含む。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un code numérique ou alphanumérique qui fait
        partie de l'adresse postale et sert à simplifier le tri ou la distribution du courrier.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">Contiene un código numérico o alfabético usado como
        parte de la dirección postal para simplificar la clasificación o entrega de correo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il codice alfanumerico utilizzato
        nell'indirizzo postale per semplificare l'ordine e la distribuzione della posta.</desc>
  <desc versionDate="2024-04-11" xml:lang="de">enthält einen numerischen oder alphanumerischen Schlüssel,
        der als Teil einer Postadresse zur Vereinfachung der Sortierung oder Zustellung von Postsendungen verwendet wird.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.addrPart"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-uo">
      <postCode>HR1 3LR</postCode>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-oc">
      <postCode>84000</postCode>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-pb">
      <postCode>60142-7</postCode>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-cx">
      <postCode>310</postCode>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-wh" source="#biblzh-tw_n18">
      <postCode>310-51</postCode>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-wo">
      <postCode>60142-7</postCode>
    </egXML>
  </exemplum>
  <remarks ident="postCode-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The position and nature of postal codes is highly country-specific; the conventions
            appropriate to the country concerned should be used.</p>
  </remarks>
  <remarks ident="postCode-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La disposition et la nature des codes postaux est spécifique à chaque pays ; on utilise les
      conventions qui leur sont propres .</p>
  </remarks>
  <remarks ident="postCode-remarks" versionDate="2008-04-05" xml:lang="ja">
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
<gloss versionDate="2007-07-04" xml:lang="en">postal code</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">우편 번호</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">郵遞區號</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">code postal</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">Código postal</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">Codice di Avviamento Postale</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Postleitzahl</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a numerical or alphanumeric code used as part of a postal address to simplify
        sorting or delivery of mail.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">우편의 분류 및 배달을 용이하도록 우편 주소의 일부로 사용되는 숫자 또는 문자와 숫자가 혼용된
        기호.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個數字或字母加數字的區域代碼，屬於郵寄地址的一部分，用以簡化郵件的分類及寄送工作。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">郵便の配達や区分けを簡単にするための、郵便の宛名情報の部分となる数値 または文字を含む。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient un code numérique ou alphanumérique qui fait
        partie de l'adresse postale et sert à simplifier le tri ou la distribution du courrier.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">Contiene un código numérico o alfabético usado como
        parte de la dirección postal para simplificar la clasificación o entrega de correo.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il codice alfanumerico utilizzato
        nell'indirizzo postale per semplificare l'ordine e la distribuzione della posta.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2024-04-11" xml:lang="de">enthält einen numerischen oder alphanumerischen Schlüssel,
        der als Teil einer Postadresse zur Vereinfachung der Sortierung oder Zustellung von Postsendungen verwendet wird.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-uo">
      <postCode>HR1 3LR</postCode>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-oc">
      <postCode>84000</postCode>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-pb">
      <postCode>60142-7</postCode>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-cx">
      <postCode>310</postCode>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-wh" source="#biblzh-tw_n18">
      <postCode>310-51</postCode>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postCode-egXML-wo">
      <postCode>60142-7</postCode>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="postCode-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The position and nature of postal codes is highly country-specific; the conventions
            appropriate to the country concerned should be used.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="postCode-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La disposition et la nature des codes postaux est spécifique à chaque pays ; on utilise les
      conventions qui leur sont propres .</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="postCode-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 郵便番号の位置づけや性質は、国家に強く依存する。国の事情にあった方 式が採用されるべきである。 </p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONAAD"/>
  </listRef>
```

^b27

