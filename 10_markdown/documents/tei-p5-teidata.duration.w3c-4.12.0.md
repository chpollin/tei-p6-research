---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.duration.w3c-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.duration.w3c
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.duration.w3c.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.duration.w3c

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5869. Git blob: `5a6ecf984f7ad88033fd2f2c783e50182cda81f7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="data-duration.w3c" ident="teidata.duration.w3c">
  <desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values available for representation of a duration in time using W3C datatypes.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">W3C 데이터 유형을 사용해서 시간 지속을 나타내는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">以W3C datatypes標準格式來定義表示一段持續性時間的屬性值範圍</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">W3Cのデータ型を使用して表現できる時間幅を値域とする属性値を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant une durée temporaraire utilisant les types de données W3C</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos disponibles para la representación de un periodo de tiempo usando tipos de datos W3C</desc>
  <content>
      <dataRef name="duration"/>
   </content>
  <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-mq">
         <time dur="PT45M">forty-five minutes</time>
      </egXML>
  </exemplum>
  <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-ct">
         <date dur="P1DT12H">a day and a half</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-lp">
         <date dur="P7D">a week</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-oz">
         <time dur="PT45M">quarante-cinq minutes</time>
      </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-oo">
         <date dur="P1DT12H">une journée et demie</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-bg">
         <date dur="P7D">une semaine</date>
      </egXML>
  </exemplum>
  <exemplum xml:lang="und">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-gn">
         <time dur="PT0.02S">20 ms</time>
      </egXML>
  </exemplum>
  <remarks ident="teidata.duration.w3c-remarks" versionDate="2007-04-20" xml:lang="en">
      <p>A duration is expressed as a sequence of number-letter pairs,
    preceded by the letter P; the letter gives the unit and may be Y
    (year), M (month), D (day), H (hour), M (minute), or S (second),
    in that order. The numbers are all unsigned integers, except for
    the <code>S</code> number, which may have a decimal component
    (using <code>.</code> as the decimal point). If any number is
    <mentioned>0</mentioned>, then that number-letter pair may be
    omitted. If any of the H (hour), M (minute), or S (second)
    number-letter pairs are present, then the separator <code>T</code>
    must precede the first <soCalled>time</soCalled> number-letter
    pair.</p>
      <p>For complete details, see the <ref target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#duration">W3C
    specification</ref>.</p>
  </remarks>
  <remarks ident="teidata.duration.w3c-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p>
    時間幅は、先頭文字Pに続いて、数値-文字のペア列で示される。
    文字は単位を示している。Y(年)、M(月)、D(日)、H(時間)、M(分)、S(秒)
    の順番になる。数値は符号のない整数である。但し、<code>S</code>の場
    合、最後に10進数の表記記号(小数点を示す<code>.</code>)をとることが
    ある。数値が<mentioned>0</mentioned>の場合、数値-文字のペアは省略
    されることがある。H(時間)、M(分)、S(秒)が数値-文字のペアを作る場合、
    区切子<code>T</code>を先頭にして<soCalled>時間</soCalled>を示す
    数値-文字のペアを示す必要がある。
    </p>
      <p>
    詳細については、
    <ref target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#duration">
    W3C specification</ref>を参照のこと。
    </p>
  </remarks>
  <remarks ident="teidata.duration.w3c-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Une durée est exprimée par une suite de paires alphanumériques, précédée par la lettre P ; la lettre donne l'unité et peut être Y
      (année), M (mois), D (jour), H (heure), M (minute), ou S (seconde),
      dans cet ordre. Les nombres sont des entiers non signés à l'exception du dernier, qui peut comporter une décimale (en utilisant soit 
      <code>.</code> soit <code>,</code> pour la virgule ; la dernière possibilité est préférable). Si un nombre est <mentioned>0</mentioned>, alors
      la paire alphanumérique peut être omise. Si les paires alphanumériques H (heure), M
      (minute), ou S (seconde) sont présentes, alors le séparateur
      <code>T</code> doit précéder la première paire alphanumérique
      <soCalled>time</soCalled>.</p>
      <p>Pour des détails complets, voir <ref target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#duration">W3C
      specification</ref>.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values available for representation of a duration in time using W3C datatypes.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">W3C 데이터 유형을 사용해서 시간 지속을 나타내는 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">以W3C datatypes標準格式來定義表示一段持續性時間的屬性值範圍</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">W3Cのデータ型を使用して表現できる時間幅を値域とする属性値を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant une durée temporaraire utilisant les types de données W3C</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos disponibles para la representación de un periodo de tiempo usando tipos de datos W3C</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef name="duration"/>
   </content>
```

^b7

### Block 8

XML location: `/dataSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-mq">
         <time dur="PT45M">forty-five minutes</time>
      </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/dataSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-ct">
         <date dur="P1DT12H">a day and a half</date>
      </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/dataSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-lp">
         <date dur="P7D">a week</date>
      </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/dataSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-oz">
         <time dur="PT45M">quarante-cinq minutes</time>
      </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/dataSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-oo">
         <date dur="P1DT12H">une journée et demie</date>
      </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/dataSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="fr">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-bg">
         <date dur="P7D">une semaine</date>
      </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/dataSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="und">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="data-duration.w3c-egXML-gn">
         <time dur="PT0.02S">20 ms</time>
      </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.duration.w3c-remarks" versionDate="2007-04-20" xml:lang="en">
      <p>A duration is expressed as a sequence of number-letter pairs,
    preceded by the letter P; the letter gives the unit and may be Y
    (year), M (month), D (day), H (hour), M (minute), or S (second),
    in that order. The numbers are all unsigned integers, except for
    the <code>S</code> number, which may have a decimal component
    (using <code>.</code> as the decimal point). If any number is
    <mentioned>0</mentioned>, then that number-letter pair may be
    omitted. If any of the H (hour), M (minute), or S (second)
    number-letter pairs are present, then the separator <code>T</code>
    must precede the first <soCalled>time</soCalled> number-letter
    pair.</p>
      <p>For complete details, see the <ref target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#duration">W3C
    specification</ref>.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.duration.w3c-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p>
    時間幅は、先頭文字Pに続いて、数値-文字のペア列で示される。
    文字は単位を示している。Y(年)、M(月)、D(日)、H(時間)、M(分)、S(秒)
    の順番になる。数値は符号のない整数である。但し、<code>S</code>の場
    合、最後に10進数の表記記号(小数点を示す<code>.</code>)をとることが
    ある。数値が<mentioned>0</mentioned>の場合、数値-文字のペアは省略
    されることがある。H(時間)、M(分)、S(秒)が数値-文字のペアを作る場合、
    区切子<code>T</code>を先頭にして<soCalled>時間</soCalled>を示す
    数値-文字のペアを示す必要がある。
    </p>
      <p>
    詳細については、
    <ref target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#duration">
    W3C specification</ref>を参照のこと。
    </p>
  </remarks>
```

^b16

### Block 17

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.duration.w3c-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>Une durée est exprimée par une suite de paires alphanumériques, précédée par la lettre P ; la lettre donne l'unité et peut être Y
      (année), M (mois), D (jour), H (heure), M (minute), ou S (seconde),
      dans cet ordre. Les nombres sont des entiers non signés à l'exception du dernier, qui peut comporter une décimale (en utilisant soit 
      <code>.</code> soit <code>,</code> pour la virgule ; la dernière possibilité est préférable). Si un nombre est <mentioned>0</mentioned>, alors
      la paire alphanumérique peut être omise. Si les paires alphanumériques H (heure), M
      (minute), ou S (seconde) sont présentes, alors le séparateur
      <code>T</code> doit précéder la première paire alphanumérique
      <soCalled>time</soCalled>.</p>
      <p>Pour des détails complets, voir <ref target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#duration">W3C
      specification</ref>.</p>
  </remarks>
```

^b17

