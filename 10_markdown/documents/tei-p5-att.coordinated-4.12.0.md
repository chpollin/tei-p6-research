---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.coordinated-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.coordinated
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.coordinated.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.coordinated

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6402. Git blob: `d8e44cbb5f8bc77c0b514602489058504b11467f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="transcr" type="atts" ident="att.coordinated">
  <desc versionDate="2016-02-16" xml:lang="en">provides attributes that can be used to position their parent 
    element within a two and three dimensional coordinate system.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">이차원 좌표 체계 내에서 위치될 수 있는 요소</desc>
  <desc versionDate="2008-04-06" xml:lang="es">los elementos se pueden colocar dentro de un sistema de coordenadas bidimensional.</desc>
  <desc versionDate="2019-01-23" xml:lang="ja">2次元座標システムによる、親要素の場所を示す属性。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">attributs utilisables pour les éléments pouvant être positionnés dans un système de coordonnées à deux dimensions.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">elementi posizionabili all'interno di un sistema di coordinate bidimensionale.</desc>
  <attList>
    <attDef ident="start">
      <desc versionDate="2009-10-01" xml:lang="en">indicates the element within a transcription of the text
containing at least the start of the writing represented by this zone
or surface.</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">désigne l'élément qui, dans la transcription du texte, contient au moins le début de la section de texte représentée dans la zone ou surface.</desc>
      <desc versionDate="2019-01-23" xml:lang="ja">このzoneまたはsurface要素で示される記述の少なくとも開始点を含むようなテクストの翻刻内の要素を示す。</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="ulx">
      <desc versionDate="2007-09-22" xml:lang="en">gives the x coordinate value for the upper left corner of a
rectangular space.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 좌측 상단에 대한 x 좌표 값을 제시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada X para el ángulo superior izquierdo de un espacio rectangular.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">矩形における左上点のX軸の値を示す。</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">donne la valeur x de l'abscisse du
        coin supérieur gauche d'un rectangle.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">assegna il valore x all'angolo superiore sinistro di uno spazio rettangolare.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="uly">
      <desc versionDate="2007-09-22" xml:lang="en">gives the y coordinate value for the upper left corner of a
rectangular space.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 좌측 상단에 대한 y 좌표 값을 제시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada Y para el ángulo superior izquierdo de un espacio rectangular.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">矩形における左上点のY軸の値を示す。</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">donne la valeur y de l'ordonnée du coin supérieur gauche d'un rectangle.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">assegna il valore y all'angolo superiore sinistro di uno spazio rettangolare.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="lrx">
      <desc versionDate="2007-09-22" xml:lang="en">gives the x coordinate value for the lower right corner of a
rectangular space.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 오른쪽 하단에 대한 x 좌표 값을 제시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada X para el ángulo inferior derecho de un espacio rectangular</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">矩形における右下点のX軸の値を示す。</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">donne la valeur x de l'abscisse du coin inférieur droit d'un rectangle.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">assegna il valore x all'angolo inferiore destro di uno spazio rettangolare.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="lry">
      <desc versionDate="2007-09-22" xml:lang="en">gives the y coordinate value for the lower right corner of a
rectangular space.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 오른쪽 하단에 대한 y 좌표 값을 제시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada Y para el ángulo inferior izquierdo de un espacio rectangular</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">矩形における右下点のY軸の値を示す。</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">donne la valeur y de l'ordonnée du coin inférieur droit d'un rectangle.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">assegna il valore y all'angolo inferiore destro di uno spazio rettangolare.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="points">
      <desc versionDate="2011-12-17" xml:lang="en">identifies a two or three dimensional area by means of a series of pairs of numbers, each of which gives the x,y, or z coordinates of a point on a line enclosing the area.</desc>
      <desc versionDate="2019-01-23" xml:lang="ja">当該の領域を取り囲む線上の点のXとY軸を与える一連の数値の組を持つ他の属性によって指定されたバウンディングボックス内の2次元の領域を特定する。</desc>
      <datatype minOccurs="3" maxOccurs="unbounded"><dataRef key="teidata.point"/></datatype>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-02-16" xml:lang="en">provides attributes that can be used to position their parent 
    element within a two and three dimensional coordinate system.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이차원 좌표 체계 내에서 위치될 수 있는 요소</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">los elementos se pueden colocar dentro de un sistema de coordenadas bidimensional.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2019-01-23" xml:lang="ja">2次元座標システムによる、親要素の場所を示す属性。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">attributs utilisables pour les éléments pouvant être positionnés dans un système de coordonnées à deux dimensions.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">elementi posizionabili all'interno di un sistema di coordinate bidimensionale.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2009-10-01" xml:lang="en">indicates the element within a transcription of the text
containing at least the start of the writing represented by this zone
or surface.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">désigne l'élément qui, dans la transcription du texte, contient au moins le début de la section de texte représentée dans la zone ou surface.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2019-01-23" xml:lang="ja">このzoneまたはsurface要素で示される記述の少なくとも開始点を含むようなテクストの翻刻内の要素を示す。</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-09-22" xml:lang="en">gives the x coordinate value for the upper left corner of a
rectangular space.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 좌측 상단에 대한 x 좌표 값을 제시한다.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada X para el ángulo superior izquierdo de un espacio rectangular.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">矩形における左上点のX軸の値を示す。</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">donne la valeur x de l'abscisse du
        coin supérieur gauche d'un rectangle.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna il valore x all'angolo superiore sinistro di uno spazio rettangolare.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2007-09-22" xml:lang="en">gives the y coordinate value for the upper left corner of a
rectangular space.</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 좌측 상단에 대한 y 좌표 값을 제시한다.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada Y para el ángulo superior izquierdo de un espacio rectangular.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">矩形における左上点のY軸の値を示す。</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">donne la valeur y de l'ordonnée du coin supérieur gauche d'un rectangle.</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna il valore y all'angolo superiore sinistro di uno spazio rettangolare.</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2007-09-22" xml:lang="en">gives the x coordinate value for the lower right corner of a
rectangular space.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 오른쪽 하단에 대한 x 좌표 값을 제시한다.</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada X para el ángulo inferior derecho de un espacio rectangular</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">矩形における右下点のX軸の値を示す。</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">donne la valeur x de l'abscisse du coin inférieur droit d'un rectangle.</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna il valore x all'angolo inferiore destro di uno spazio rettangolare.</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2007-09-22" xml:lang="en">gives the y coordinate value for the lower right corner of a
rectangular space.</desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">직사각형 공간의 오른쪽 하단에 대한 y 좌표 값을 제시한다.</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona el valor de la coordinada Y para el ángulo inferior izquierdo de un espacio rectangular</desc>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">矩形における右下点のY軸の値を示す。</desc>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">donne la valeur y de l'ordonnée du coin inférieur droit d'un rectangle.</desc>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna il valore y all'angolo inferiore destro di uno spazio rettangolare.</desc>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[1]`.

```xml
<desc versionDate="2011-12-17" xml:lang="en">identifies a two or three dimensional area by means of a series of pairs of numbers, each of which gives the x,y, or z coordinates of a point on a line enclosing the area.</desc>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[6]/desc[2]`.

```xml
<desc versionDate="2019-01-23" xml:lang="ja">当該の領域を取り囲む線上の点のXとY軸を与える一連の数値の組を持つ他の属性によって指定されたバウンディングボックス内の2次元の領域を特定する。</desc>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[6]/datatype[1]`.

```xml
<datatype minOccurs="3" maxOccurs="unbounded"><dataRef key="teidata.point"/></datatype>
```

^b41

