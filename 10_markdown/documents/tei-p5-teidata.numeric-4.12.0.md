---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.numeric-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.numeric
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.numeric.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.numeric

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4683. Git blob: `d71d22b372709eaca85a28da942f0859526126ad`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.numeric">
  <desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values used for numeric values.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수치에 사용되는 속성 값의 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義用於數值的屬性值範圍</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">数値をとる属性値の範囲を定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs utilisées pour
    des valeurs numériques.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos para valores
    numéricos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per
    valori numerici</desc>
  <content>
      <alternate>
         <dataRef name="double"/>
         <dataRef name="token" restriction="(\-?[\d]+/\-?[\d]+)"/>
         <dataRef name="decimal"/>
      </alternate>
   </content>
  <remarks ident="teidata.numeric-remarks" versionDate="2009-06-01" xml:lang="en">
      <p>Any numeric value, represented as a decimal number, in floating point format, or as a ratio.</p>
      <p>To represent a floating point number, expressed in scientific notation, <soCalled>E
      notation</soCalled>, a variant of <soCalled>exponential notation</soCalled>, may be used. In
      this format, the value is expressed as two numbers separated by the letter E. The first
      number, the significand (sometimes called the mantissa) is given in decimal format, while the
      second is an integer. The value is obtained by multiplying the mantissa by 10 the number of
      times indicated by the integer. Thus the value represented in decimal notation as 1000.0 might
      be represented in scientific notation as 10E3.</p>
      <p>A value expressed as a ratio is represented by two integer values separated by a solidus (/)
      character. Thus, the value represented in decimal notation as 0.5 might be represented as a
      ratio by the string 1/2.</p>
  </remarks>
  <remarks ident="teidata.numeric-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>浮動小数点形式の10進小数、あるいは比の形式で表現されるなんらかの数値。浮動小数点数を表現するには、<soCalled>指数表記</soCalled>の一種である科学的表記、通称<soCalled>E記法</soCalled>が使用できる。この形式では、値はEの文字で区切られた二つの数字で表現する。一つ目の数字である仮数は小数で、二つ目の数字は整数で表される。値は、仮数を〔二つ目の〕整数の示す回数だけ10倍することで得られる。したがって、10進小数で1000.0と表記されている値は、科学的表記では10E3となる。</p><p>比の値は、二つの整数を「/」で区切って表す。したがって、10進小数で0.5と表される値は、比としては1/2という文字列で表現できる。 </p>
  </remarks>
  <remarks ident="teidata.numeric-remarks" versionDate="2009-10-06" xml:lang="fr">
      <p> Toute valeur numérique, représentée en nombre décimal, notée en virgule flottante ou
      en fraction.</p>
      <p>Pour représenter un nombre en virgule flottante, exprimé en notation scientifique,
        <soCalled>E notation</soCalled>, une variante de la <soCalled>notation
      exponentielle</soCalled> peut être utilisée. Dans ce format, la valeur est exprimée par deux
      nombres séparés par la lettre E. Le premier facteur, le significande (parfois appelé mantisse)
      est donné sous forme décimale, tandis que le second est un entier. La valeur est obtenue en
      multipliant la mantisse par 10 fois le nombre indiqué par l'entier. Ainsi la valeur
      représentée en notation décimale 1000.0 pourrait être représentée en notation
      scientifique 10E3.</p>
      <p>Une valeur exprimée en fraction est représentée par deux nombres entiers séparés par une
      barre oblique (/). Ainsi, la valeur représentée en notation décimale 0.5 pourrait être
      représentée en fraction par la chaîne de caractères 1/2.</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values used for numeric values.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수치에 사용되는 속성 값의 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義用於數值的屬性值範圍</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">数値をとる属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attributs utilisées pour
    des valeurs numériques.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos para valores
    numéricos.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per
    valori numerici</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <alternate>
         <dataRef name="double"/>
         <dataRef name="token" restriction="(\-?[\d]+/\-?[\d]+)"/>
         <dataRef name="decimal"/>
      </alternate>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.numeric-remarks" versionDate="2009-06-01" xml:lang="en">
      <p>Any numeric value, represented as a decimal number, in floating point format, or as a ratio.</p>
      <p>To represent a floating point number, expressed in scientific notation, <soCalled>E
      notation</soCalled>, a variant of <soCalled>exponential notation</soCalled>, may be used. In
      this format, the value is expressed as two numbers separated by the letter E. The first
      number, the significand (sometimes called the mantissa) is given in decimal format, while the
      second is an integer. The value is obtained by multiplying the mantissa by 10 the number of
      times indicated by the integer. Thus the value represented in decimal notation as 1000.0 might
      be represented in scientific notation as 10E3.</p>
      <p>A value expressed as a ratio is represented by two integer values separated by a solidus (/)
      character. Thus, the value represented in decimal notation as 0.5 might be represented as a
      ratio by the string 1/2.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.numeric-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>浮動小数点形式の10進小数、あるいは比の形式で表現されるなんらかの数値。浮動小数点数を表現するには、<soCalled>指数表記</soCalled>の一種である科学的表記、通称<soCalled>E記法</soCalled>が使用できる。この形式では、値はEの文字で区切られた二つの数字で表現する。一つ目の数字である仮数は小数で、二つ目の数字は整数で表される。値は、仮数を〔二つ目の〕整数の示す回数だけ10倍することで得られる。したがって、10進小数で1000.0と表記されている値は、科学的表記では10E3となる。</p><p>比の値は、二つの整数を「/」で区切って表す。したがって、10進小数で0.5と表される値は、比としては1/2という文字列で表現できる。 </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.numeric-remarks" versionDate="2009-10-06" xml:lang="fr">
      <p> Toute valeur numérique, représentée en nombre décimal, notée en virgule flottante ou
      en fraction.</p>
      <p>Pour représenter un nombre en virgule flottante, exprimé en notation scientifique,
        <soCalled>E notation</soCalled>, une variante de la <soCalled>notation
      exponentielle</soCalled> peut être utilisée. Dans ce format, la valeur est exprimée par deux
      nombres séparés par la lettre E. Le premier facteur, le significande (parfois appelé mantisse)
      est donné sous forme décimale, tandis que le second est un entier. La valeur est obtenue en
      multipliant la mantisse par 10 fois le nombre indiqué par l'entier. Ainsi la valeur
      représentée en notation décimale 1000.0 pourrait être représentée en notation
      scientifique 10E3.</p>
      <p>Une valeur exprimée en fraction est représentée par deux nombres entiers séparés par une
      barre oblique (/). Ainsi, la valeur représentée en notation décimale 0.5 pourrait être
      représentée en fraction par la chaîne de caractères 1/2.</p>
  </remarks>
```

^b11

