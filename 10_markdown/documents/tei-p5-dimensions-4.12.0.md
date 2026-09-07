---
type: representation
source-type: document
source: '[[00_sources/tei-p5-dimensions-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 dimensions
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/dimensions.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# dimensions

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 15976. Git blob: `ddbae34763cebc2fdadba3355cc22ae68c17276a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="DIMENSIONS" ident="dimensions">
  <gloss versionDate="2009-04-17" xml:lang="en">dimensions</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">dimensions</gloss>
  <desc versionDate="2007-08-02" xml:lang="en" xml:id="dimensions.desc">contains a dimensional specification.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 차원의 명세를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">尺寸的詳細說明。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">大きさ・程度を示す。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">contient une spécification des dimensions.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de especificación referente a las dimensiones.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una qualsiasi indicazione relativa alle dimensioni.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="dim"/>
      <classRef key="model.dimLike"/>
    </alternate>
  </content>
  <constraintSpec scheme="schematron" ident="duplicateDim" xml:lang="en">
    <!-- It would be simpler to use just
         "( count(tei:width), count(tei:height), count(tei:depth) ) > 1",
         but then we would not be able to tell the user which element
         had too many occurrences. -->
    <constraint>
      <sch:rule context="tei:dimensions">
        <sch:report test="count(tei:width) gt 1">
          The element &lt;<sch:name/>&gt; may appear once only.
        </sch:report>
        <sch:report test="count(tei:height) gt 1">
          The element &lt;<sch:name/>&gt; may appear once only.
        </sch:report>
        <sch:report test="count(tei:depth) gt 1">
          The element &lt;<sch:name/>&gt; may appear once only.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="type" mode="change">
      <desc versionDate="2005-01-14" xml:lang="en">indicates which aspect of the object is being measured.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">대상의 어떤 측면이 측정되고 있는지를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出物件被測量的部分。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該計測対象を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">indique quel aspect de l'objet est mesuré.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica que aspecto del objeto se mide.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica quale aspetto dell'oggetto viene misurato.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="leaves">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to one or more leaves (e.g. a single leaf, a gathering, or a separately bound part)</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">하나 이상의 종이의 장과 관련된 차원(예, 한 장, 접지 모음, 또는 각각 분리되어 엮여진 부분)</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">一張或多張頁面的尺寸大小 (例如單一頁面、聚集頁面、或分開裝訂的部份)</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se relacionan con una o más hojas (p.ej. una sola hoja, un conjunto, o un intervalo)</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">葉の状態を示す。例えば、一葉、葉の丁合(折丁)、独立した一枚を まとめたもの、など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent une ou plusieurs feuilles (par exemple une feuille unique, un ensemble de feuilles ou une partie reliée séparément).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono a uno o più fogli (per esempio un foglio, una raccolta, o una parte rilegata separatamente).</desc>
        </valItem>
        <valItem ident="ruled">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the area of a leaf which has been ruled in preparation for writing.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">글쓰기를 준비하기 위해 줄 그은 종이 부분과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面上劃好線以備書寫的範圍大小。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren al área de una hoja que se ha preparado para la escritura.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">書記の準備として罫が引かれている領域を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la zone de la réglure d'une feuille.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla porzione di un foglio sulla quale sono state disegnate delle righe al fine di scriverci.</desc>
        </valItem>
        <valItem ident="pricked">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the area of a leaf which has been pricked out in preparation for ruling (used where this differs significantly from the ruled area, or where the ruling is not measurable).</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">(줄 그은 영역과 다르거나 영역 구분이 측정되지 않은 곳에서 사용되는) 줄을 긋기 위한 준비 과정에서 구멍 뚫은 영역과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面上刺好記號以備劃線的範圍大小 (用在和畫線範圍不同的位置，或是畫線無法測量的位置) 。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren al área de una hoja que ha sido agujereada en la preparación para la escritura (utilizado donde esto difiere significativamente del área lineada, o donde la lineación no es mensurable).</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">罫を引く準備として開けられた穴がある領域を示す。これは、罫付 き領域とも、罫が読み取れない領域とも異なる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la zone d'une feuille qui a été piquée pour préparer la réglure (à utiliser lorsqu'elle diffère significativement de la zone réglée ou lorsque la réglure n'est pas mesurable).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla porzione di un foglio sulla quale è stata indicata la posizione dei fori da praticare al fine di imprimervi delle righe (si usa quando la porzione da rigare è molto diversa da quella già rigata o quando la rigatura non è misurabile).</desc>
        </valItem>
        <valItem ident="written">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the area of a leaf which has been written, with the height measured from the top of the minims on the top line of writing, to the bottom of the minims on the bottom line of writing.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">글의 첫 번째 줄 상단부터 마지막 줄 하단까지 측정된 높이를 통해 한 장의 글 쓴 영역과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面上已書寫文字的範圍大小，高度由最頂行文字的頂端測量至最底行文字的底端。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refiere al área de una hoja que ha sido escrita, con la altura medida desde la línea superior de escritura a la parte inferior de la última línea de la escritura.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">書記領域を示す。先頭文字行から最終文字行までの高さ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la zone écrite de la feuille, dont la hauteur est mesurée depuis le haut des blancs sur la ligne d'écriture supérieure jusqu'au dernier des blancs sur la dernière ligne écrite.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono ad un'area del foglio su cui è stato scritto e la cui altezza è misurata dalla cima degli uncini sulla prima riga scritta fino al fondo degli uncini sull'ultima riga scritta.</desc>
        </valItem>
        <valItem ident="miniatures">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the miniatures within the manuscript</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">원고의 축소형과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">手稿中圖畫的尺寸大小</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones relativas a las miniaturas del manuscrito</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の彩飾図の大きさを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent les miniatures contenues dans le manuscrit.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alle miniature contenute nel manoscritto.</desc>
        </valItem>
        <valItem ident="binding">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the binding in which the codex or manuscript is contained</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">미제본 원고 또는 원고를 포함하는 제본과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">手抄本或手稿裝訂的尺寸大小</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren a la encuadernación que contiene el códice o el manuscrito</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">冊子や写本全体の大きさを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la reliure qui contient le codex ou le manuscrit.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla rilegatura nella quale è contenuto il codice o manoscritto.</desc>
        </valItem>
        <valItem ident="box">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the box or other container in which  the manuscript is stored.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">원고가 보관된 박스 또는 용기와 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">手稿所儲存的箱子或其他容器的尺寸大小</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren a la caja o a cualquier otro contenedor en qué se conserva el manuscrito.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該写本を入れるケースの大きさを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la boîte ou autre conteneur dans lequel le manuscrit est conservé.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla scatola o ad altro contenitore nel quale è custodito il manoscritto.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-ru">
      <dimensions type="leaves">
        <height scope="range">157-160</height>
        <width>105</width>
      </dimensions>
      <dimensions type="ruled">
        <height scope="most">90</height>
        <width scope="most">48</width>
      </dimensions>
      <dimensions unit="in">
        <height>12</height>
        <width>10</width>
      </dimensions>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-jd" source="#fr-ex-BnF-Reliures">
      <dimensions type="binding">
        <height unit="mm">328 (336)</height>
        <width unit="mm">203</width>
        <depth unit="mm">74</depth>
      </dimensions>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Quand de simples quantités numériques sont impliquées, elles peuvent être exprimées par
        l'attribut <att>quantity</att> sur chaque ou sur tous les éléments enfants, comme dans
        l'exemple suivant : </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-jj" source="#fr-ex-BnF-Reliures">
      <dimensions type="binding">
        <height unit="mm">170</height>
        <width unit="mm">98</width>
        <depth unit="mm">15</depth>
      </dimensions>
      <dimensions type="binding">
        <height unit="mm">168</height>
        <width unit="mm">106</width>
        <depth unit="mm">22</depth>
      </dimensions>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>This element may be used to record the dimensions of any
text-bearing object, not necessarily a codex. For example:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-wz">
      <dimensions type="panels">
        <height scope="all">7004</height>
        <width scope="all">1803</width>
        <dim type="relief" unit="mm">345</dim>
      </dimensions>
    </egXML>
    <p>This might be used to show that the inscribed panels on some (imaginary)
monument are all the same size (7004 by 1803 cm) and stand out from
the rest of the monument by 345 mm.
</p>
  </exemplum>
  <exemplum xml:lang="en">
    <p>When simple numeric quantities are involved, they may be
    expressed on the <att>quantity</att> attribute of any or all of
    the child elements, as in the following example:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-kk">
      <dimensions type="leaves">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </dimensions>
      <dimensions type="ruled">
        <height unit="cm" scope="most" quantity="90"/>
        <width unit="cm" scope="most" quantity="48"/>
      </dimensions>
      <dimensions unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
      </dimensions>
    </egXML>
  </exemplum>
  <remarks ident="dimensions-remarks" versionDate="2012-03-14" xml:lang="en">
    <p>Contains no more than one of each of the specialized elements
    used to express a three-dimensional object's height, width, and
    depth, combined with any number of other kinds of dimensional
    specification.</p>
  </remarks>
  <remarks ident="dimensions-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Contient la mesure de la hauteur, de la largeur et de la profondeur d'un objet à 1,
                2 ou 3 dimensions.</p>
  </remarks>
  <remarks ident="dimensions-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    対象物の高さ、幅、奥行きの大きさを示す。
    </p>
  </remarks>
  <listRef>
    <ptr target="#msdim"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="en">dimensions</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">dimensions</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-08-02" xml:lang="en" xml:id="dimensions.desc">contains a dimensional specification.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 차원의 명세를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">尺寸的詳細說明。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">大きさ・程度を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">contient une spécification des dimensions.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de especificación referente a las dimensiones.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una qualsiasi indicazione relativa alle dimensioni.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="dim"/>
      <classRef key="model.dimLike"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="duplicateDim" xml:lang="en">
    <!-- It would be simpler to use just
         "( count(tei:width), count(tei:height), count(tei:depth) ) > 1",
         but then we would not be able to tell the user which element
         had too many occurrences. -->
    <constraint>
      <sch:rule context="tei:dimensions">
        <sch:report test="count(tei:width) gt 1">
          The element &lt;<sch:name/>&gt; may appear once only.
        </sch:report>
        <sch:report test="count(tei:height) gt 1">
          The element &lt;<sch:name/>&gt; may appear once only.
        </sch:report>
        <sch:report test="count(tei:depth) gt 1">
          The element &lt;<sch:name/>&gt; may appear once only.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates which aspect of the object is being measured.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">대상의 어떤 측면이 측정되고 있는지를 나타낸다.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出物件被測量的部分。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該計測対象を示す。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">indique quel aspect de l'objet est mesuré.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica que aspecto del objeto se mide.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica quale aspetto dell'oggetto viene misurato.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="leaves">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to one or more leaves (e.g. a single leaf, a gathering, or a separately bound part)</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">하나 이상의 종이의 장과 관련된 차원(예, 한 장, 접지 모음, 또는 각각 분리되어 엮여진 부분)</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">一張或多張頁面的尺寸大小 (例如單一頁面、聚集頁面、或分開裝訂的部份)</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se relacionan con una o más hojas (p.ej. una sola hoja, un conjunto, o un intervalo)</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">葉の状態を示す。例えば、一葉、葉の丁合(折丁)、独立した一枚を まとめたもの、など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent une ou plusieurs feuilles (par exemple une feuille unique, un ensemble de feuilles ou une partie reliée séparément).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono a uno o più fogli (per esempio un foglio, una raccolta, o una parte rilegata separatamente).</desc>
        </valItem>
        <valItem ident="ruled">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the area of a leaf which has been ruled in preparation for writing.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">글쓰기를 준비하기 위해 줄 그은 종이 부분과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面上劃好線以備書寫的範圍大小。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren al área de una hoja que se ha preparado para la escritura.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">書記の準備として罫が引かれている領域を示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la zone de la réglure d'une feuille.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla porzione di un foglio sulla quale sono state disegnate delle righe al fine di scriverci.</desc>
        </valItem>
        <valItem ident="pricked">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the area of a leaf which has been pricked out in preparation for ruling (used where this differs significantly from the ruled area, or where the ruling is not measurable).</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">(줄 그은 영역과 다르거나 영역 구분이 측정되지 않은 곳에서 사용되는) 줄을 긋기 위한 준비 과정에서 구멍 뚫은 영역과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面上刺好記號以備劃線的範圍大小 (用在和畫線範圍不同的位置，或是畫線無法測量的位置) 。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren al área de una hoja que ha sido agujereada en la preparación para la escritura (utilizado donde esto difiere significativamente del área lineada, o donde la lineación no es mensurable).</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">罫を引く準備として開けられた穴がある領域を示す。これは、罫付 き領域とも、罫が読み取れない領域とも異なる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la zone d'une feuille qui a été piquée pour préparer la réglure (à utiliser lorsqu'elle diffère significativement de la zone réglée ou lorsque la réglure n'est pas mesurable).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla porzione di un foglio sulla quale è stata indicata la posizione dei fori da praticare al fine di imprimervi delle righe (si usa quando la porzione da rigare è molto diversa da quella già rigata o quando la rigatura non è misurabile).</desc>
        </valItem>
        <valItem ident="written">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the area of a leaf which has been written, with the height measured from the top of the minims on the top line of writing, to the bottom of the minims on the bottom line of writing.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">글의 첫 번째 줄 상단부터 마지막 줄 하단까지 측정된 높이를 통해 한 장의 글 쓴 영역과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面上已書寫文字的範圍大小，高度由最頂行文字的頂端測量至最底行文字的底端。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refiere al área de una hoja que ha sido escrita, con la altura medida desde la línea superior de escritura a la parte inferior de la última línea de la escritura.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">書記領域を示す。先頭文字行から最終文字行までの高さ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la zone écrite de la feuille, dont la hauteur est mesurée depuis le haut des blancs sur la ligne d'écriture supérieure jusqu'au dernier des blancs sur la dernière ligne écrite.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono ad un'area del foglio su cui è stato scritto e la cui altezza è misurata dalla cima degli uncini sulla prima riga scritta fino al fondo degli uncini sull'ultima riga scritta.</desc>
        </valItem>
        <valItem ident="miniatures">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the miniatures within the manuscript</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">원고의 축소형과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">手稿中圖畫的尺寸大小</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones relativas a las miniaturas del manuscrito</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の彩飾図の大きさを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent les miniatures contenues dans le manuscrit.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alle miniature contenute nel manoscritto.</desc>
        </valItem>
        <valItem ident="binding">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the binding in which the codex or manuscript is contained</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">미제본 원고 또는 원고를 포함하는 제본과 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">手抄本或手稿裝訂的尺寸大小</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren a la encuadernación que contiene el códice o el manuscrito</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">冊子や写本全体の大きさを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la reliure qui contient le codex ou le manuscrit.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla rilegatura nella quale è contenuto il codice o manoscritto.</desc>
        </valItem>
        <valItem ident="box">
          <desc versionDate="2007-06-27" xml:lang="en">dimensions relate to the box or other container in which  the manuscript is stored.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">원고가 보관된 박스 또는 용기와 관련된 차원</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">手稿所儲存的箱子或其他容器的尺寸大小</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las dimensiones se refieren a la caja o a cualquier otro contenedor en qué se conserva el manuscrito.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該写本を入れるケースの大きさを示す。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les dimensions concernent la boîte ou autre conteneur dans lequel le manuscrit est conservé.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le dimensioni si riferiscono alla scatola o ad altro contenitore nel quale è custodito il manoscritto.</desc>
        </valItem>
      </valList>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-ru">
      <dimensions type="leaves">
        <height scope="range">157-160</height>
        <width>105</width>
      </dimensions>
      <dimensions type="ruled">
        <height scope="most">90</height>
        <width scope="most">48</width>
      </dimensions>
      <dimensions unit="in">
        <height>12</height>
        <width>10</width>
      </dimensions>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-jd" source="#fr-ex-BnF-Reliures">
      <dimensions type="binding">
        <height unit="mm">328 (336)</height>
        <width unit="mm">203</width>
        <depth unit="mm">74</depth>
      </dimensions>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Quand de simples quantités numériques sont impliquées, elles peuvent être exprimées par
        l'attribut <att>quantity</att> sur chaque ou sur tous les éléments enfants, comme dans
        l'exemple suivant : </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-jj" source="#fr-ex-BnF-Reliures">
      <dimensions type="binding">
        <height unit="mm">170</height>
        <width unit="mm">98</width>
        <depth unit="mm">15</depth>
      </dimensions>
      <dimensions type="binding">
        <height unit="mm">168</height>
        <width unit="mm">106</width>
        <depth unit="mm">22</depth>
      </dimensions>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <p>This element may be used to record the dimensions of any
text-bearing object, not necessarily a codex. For example:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-wz">
      <dimensions type="panels">
        <height scope="all">7004</height>
        <width scope="all">1803</width>
        <dim type="relief" unit="mm">345</dim>
      </dimensions>
    </egXML>
    <p>This might be used to show that the inscribed panels on some (imaginary)
monument are all the same size (7004 by 1803 cm) and stand out from
the rest of the monument by 345 mm.
</p>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <p>When simple numeric quantities are involved, they may be
    expressed on the <att>quantity</att> attribute of any or all of
    the child elements, as in the following example:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DIMENSIONS-egXML-kk">
      <dimensions type="leaves">
        <height scope="range">157-160</height>
        <width quantity="105"/>
      </dimensions>
      <dimensions type="ruled">
        <height unit="cm" scope="most" quantity="90"/>
        <width unit="cm" scope="most" quantity="48"/>
      </dimensions>
      <dimensions unit="in">
        <height quantity="12"/>
        <width quantity="10"/>
      </dimensions>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="dimensions-remarks" versionDate="2012-03-14" xml:lang="en">
    <p>Contains no more than one of each of the specialized elements
    used to express a three-dimensional object's height, width, and
    depth, combined with any number of other kinds of dimensional
    specification.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="dimensions-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Contient la mesure de la hauteur, de la largeur et de la profondeur d'un objet à 1,
                2 ou 3 dimensions.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="dimensions-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    対象物の高さ、幅、奥行きの大きさを示す。
    </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msdim"/>
  </listRef>
```

^b30

