---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.duration.iso-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.duration.iso
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.duration.iso.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.duration.iso

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6086. Git blob: `704d7aa8e77863785435d810f3569596661f0812`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="data-duration.iso" ident="teidata.duration.iso">
  <desc versionDate="2007-04-09" xml:lang="en">defines the range of attribute values available for representation of a duration in time
    using ISO 8601 standard formats.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">ISO 8601 표준 형식을 사용하여 시간의 지속을 나타내는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">以ISO 8601標準格式定義表示一段持續性時間的屬性值範圍</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ISO 8601にある標準形式を使い、時間幅を表現する当該属性値の範囲を定義 する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme de valeurs d'attributs exprimant une durée temporaraire utilisant le norme ISO 8601.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos posibles para
    representar la duración en el tiempo usando formatos estàndards ISO 8601.</desc>
  <content>
      <dataRef name="token" restriction="[0-9.,DHMPRSTWYZ/:+\-]+"/>
   </content>
  <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-rh">
         <time dur-iso="PT0,75H">three-quarters of an hour</time>
      </egXML>
  </exemplum>
  <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-fc">
         <date dur-iso="P1,5D">a day and a half</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-es">
         <date dur-iso="P14D">a fortnight</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-eh">
         <time dur-iso="PT0,75H">trois quarts d'une heure</time>
      </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-ty">
         <date dur-iso="P1,5D">une journee et demie</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-jv">
         <date dur-iso="P14D">une quinzaine</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="und">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-ww">
         <time dur-iso="PT0.02S">20 ms</time>
      </egXML>
  </exemplum>
  <remarks ident="teidata.duration.iso-remarks" versionDate="2007-04-20" xml:lang="en">
      <p>A duration is expressed as a sequence of number-letter pairs, preceded by the letter P; the
      letter gives the unit and may be Y (year), M (month), D (day), H (hour), M (minute), or S
      (second), in that order. The numbers are all unsigned integers, except for the last, which may
      have a decimal component (using either <code>.</code> or <code>,</code> as the decimal point;
      the latter is preferred). If any number is <mentioned>0</mentioned>, then that number-letter
      pair may be omitted. If any of the H (hour), M (minute), or S (second) number-letter pairs are
      present, then the separator <code>T</code> must precede the first <soCalled>time</soCalled>
      number-letter pair.</p>
      <p>For complete details, see ISO 8601 <title>Data elements and interchange formats — Information
        interchange — Representation of dates and times</title>.</p>
  </remarks>
  <remarks ident="teidata.duration.iso-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 時間幅は、先頭文字Pに続いて、数値-文字のペア列で示される。 文字は単位を示している。Y(年)、M(月)、D(日)、H(時間)、M(分)、S(秒)
      の順番になる。数値は符号のない整数である。但し、最後に10進数の 表記記号(小数点を示す<code>.</code>または<code>,</code>。後者が望
        ましい)をとることはある。数値が<mentioned>0</mentioned>の場合、 数値-文字のペアは省略されることがある。 H(時間)、M(分)、
      S(秒)が数値-文字のペアを作る場合、区切子 <code>T</code>を先頭にして<soCalled>時間</soCalled>を示す数値-文字 のペアを示す必要がある。 </p>
      <p> 詳細については、ISO 8601<title>Data elements and interchange formats - Information interchange -
        Representation of dates and times</title>を参照のこと。 </p>
  </remarks>
  <remarks ident="teidata.duration.iso-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Une durée est exprimée par une suite de paires alphanumériques, précédée par la lettre P ;
      la lettre donne l'unité et peut être Y (année), M (mois), D (jour), H (heure), M (minute), ou
      S (seconde), dans cet ordre. Les nombres sont des entiers sans
      signe,  à l'exception du dernier,
      qui peut comporter une décimale (en utilisant soit <code>.</code> soit <code>,</code> pour la
      virgule ; la dernière possibilité est préférable). Si un nombre est <mentioned>0</mentioned>,
      alors la paire alphanumérique peut être omise. Si les paires alphanumériques H (heure), M
      (minute), ou S (seconde) sont présentes, alors le séparateur <code>T</code> doit précéder la
      première paire alphanumérique <soCalled>time</soCalled>.</p>
      <p>Pour des détails complets, voir ISO 8601 <title>Data elements and interchange formats —
        Information interchange — Representation of dates and times</title>.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-09" xml:lang="en">defines the range of attribute values available for representation of a duration in time
    using ISO 8601 standard formats.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">ISO 8601 표준 형식을 사용하여 시간의 지속을 나타내는 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">以ISO 8601標準格式定義表示一段持續性時間的屬性值範圍</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ISO 8601にある標準形式を使い、時間幅を表現する当該属性値の範囲を定義 する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme de valeurs d'attributs exprimant une durée temporaraire utilisant le norme ISO 8601.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos posibles para
    representar la duración en el tiempo usando formatos estàndards ISO 8601.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="token" restriction="[0-9.,DHMPRSTWYZ/:+\-]+"/>
   </content>
```

^b7

### Block 8

XML location: `/dataSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-rh">
         <time dur-iso="PT0,75H">three-quarters of an hour</time>
      </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/dataSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-fc">
         <date dur-iso="P1,5D">a day and a half</date>
      </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/dataSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-es">
         <date dur-iso="P14D">a fortnight</date>
      </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/dataSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-eh">
         <time dur-iso="PT0,75H">trois quarts d'une heure</time>
      </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/dataSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-ty">
         <date dur-iso="P1,5D">une journee et demie</date>
      </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/dataSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-jv">
         <date dur-iso="P14D">une quinzaine</date>
      </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/dataSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="und">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.iso-egXML-ww">
         <time dur-iso="PT0.02S">20 ms</time>
      </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.duration.iso-remarks" versionDate="2007-04-20" xml:lang="en">
      <p>A duration is expressed as a sequence of number-letter pairs, preceded by the letter P; the
      letter gives the unit and may be Y (year), M (month), D (day), H (hour), M (minute), or S
      (second), in that order. The numbers are all unsigned integers, except for the last, which may
      have a decimal component (using either <code>.</code> or <code>,</code> as the decimal point;
      the latter is preferred). If any number is <mentioned>0</mentioned>, then that number-letter
      pair may be omitted. If any of the H (hour), M (minute), or S (second) number-letter pairs are
      present, then the separator <code>T</code> must precede the first <soCalled>time</soCalled>
      number-letter pair.</p>
      <p>For complete details, see ISO 8601 <title>Data elements and interchange formats — Information
        interchange — Representation of dates and times</title>.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.duration.iso-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 時間幅は、先頭文字Pに続いて、数値-文字のペア列で示される。 文字は単位を示している。Y(年)、M(月)、D(日)、H(時間)、M(分)、S(秒)
      の順番になる。数値は符号のない整数である。但し、最後に10進数の 表記記号(小数点を示す<code>.</code>または<code>,</code>。後者が望
        ましい)をとることはある。数値が<mentioned>0</mentioned>の場合、 数値-文字のペアは省略されることがある。 H(時間)、M(分)、
      S(秒)が数値-文字のペアを作る場合、区切子 <code>T</code>を先頭にして<soCalled>時間</soCalled>を示す数値-文字 のペアを示す必要がある。 </p>
      <p> 詳細については、ISO 8601<title>Data elements and interchange formats - Information interchange -
        Representation of dates and times</title>を参照のこと。 </p>
  </remarks>
```

^b16

### Block 17

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.duration.iso-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Une durée est exprimée par une suite de paires alphanumériques, précédée par la lettre P ;
      la lettre donne l'unité et peut être Y (année), M (mois), D (jour), H (heure), M (minute), ou
      S (seconde), dans cet ordre. Les nombres sont des entiers sans
      signe,  à l'exception du dernier,
      qui peut comporter une décimale (en utilisant soit <code>.</code> soit <code>,</code> pour la
      virgule ; la dernière possibilité est préférable). Si un nombre est <mentioned>0</mentioned>,
      alors la paire alphanumérique peut être omise. Si les paires alphanumériques H (heure), M
      (minute), ou S (seconde) sont présentes, alors le séparateur <code>T</code> doit précéder la
      première paire alphanumérique <soCalled>time</soCalled>.</p>
      <p>Pour des détails complets, voir ISO 8601 <title>Data elements and interchange formats —
        Information interchange — Representation of dates and times</title>.</p>
  </remarks>
```

^b17

