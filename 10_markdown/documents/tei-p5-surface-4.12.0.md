---
type: representation
source-type: document
source: '[[00_sources/tei-p5-surface-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 surface
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/surface.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# surface

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7102. Git blob: `dbfde7f74d21d94e01e4ddbfb9272ad9ef5ae060`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="surface" xml:id="gi-surface" module="transcr">
  <desc versionDate="2011-11-20" xml:lang="en">defines a written surface as a two-dimensional or three-dimensional 
coordinate space, optionally grouping one or more graphic representations of
that space, zones of interest within that space, and, when using an embedded transcription approach, transcriptions of the writing within them.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">직사각형의 좌표 공간과 그 내부에서 기록 표면부를 정의한다. 수의적으로 그 공간의 하나 이상의 그림 표상과 관심 있는 직사각형 공간을 모아놓는다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">define una superficie escrita en coordinadas rectangulares, agrupando opcionalmente una o más representaciones gráficas de ese espacio, y las zonas rectangulares de interés dentro de él.</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">矩形の座標により、書記の表面を定義する。選択的に、空間や矩形範囲中のひ
とつ以上の図表表現をまとめる。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">définit une surface écrite comme un rectangle décrit par ses coordonnées spatiales, en regroupant éventuellement une ou plusieurs représentations
graphiques de cet espace et des zones rectangulaires intéressantes à l'intérieur de
celui-ci.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">definisce una superficie scritta in termini di uno spazio rettangolare di coordinate, eventualmente che raggruppi una o più rappresentazioni grafiche di tale spazio, e delle zone rettangolari di interesse all'interno di questo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.coordinated"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <!-- added by gen -->
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.labelLike"/>
          <classRef key="model.graphicLike"/>
        </alternate>
      
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <alternate>
            <elementRef key="zone"/>
            <elementRef key="line"/>
            <elementRef key="path"/>
            <elementRef key="surface"/>
            <elementRef key="surfaceGrp"/>
          </alternate>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <attList>
    <attDef ident="attachment">
      <desc versionDate="2011-11-15" xml:lang="en">describes the method by which this surface is or was
         connected to the main surface.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="glued">
          <desc versionDate="2011-11-15" xml:lang="en">glued in place</desc>
        </valItem>
        <valItem ident="pinned">
          <desc versionDate="2011-11-15" xml:lang="en">pinned or stapled in place</desc>
        </valItem>
        <valItem ident="sewn">
          <desc versionDate="2011-11-15" xml:lang="en">sewn in place</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="flipping">
      <desc versionDate="2011-11-11" xml:lang="en">indicates whether the
      surface is attached and folded in such a way as to provide two
      writing surfaces.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surface-egXML-wq" source="#UND">
      <facsimile>
        <surface ulx="0" uly="0" lrx="200" lry="300">
          <graphic url="Bovelles-49r.png"/>
        </surface>
      </facsimile>
    </egXML>
  </exemplum>
  <remarks ident="surface-remarks" versionDate="2011-11-20" xml:lang="en">
    <p>The <gi>surface</gi> element represents any two-dimensional or three-dimensional space on
some physical surface forming part of the source material, such as a piece of
paper, a face of a monument, a billboard, a scroll, a leaf etc.</p>
    <p>The coordinate space defined by this element may be thought of
    as a grid <att>lrx</att> - <att>ulx</att> units wide and
    <att>uly</att> - <att>lry</att> units high. </p>
    <p>The  <gi>surface</gi> element may contain graphic representations
or transcriptions of written zones, or both. The coordinate values used by every
    <gi>zone</gi> element contained by this element are to be
    understood with reference to the same grid. <!-- If the <att>points</att> attribute is used to indicate the
exact perimeter of the surface being documented, the points defined
are also understood with reference to this same coordinate system.--> </p>
    <p>Where it is useful or meaningful to do so, any grouping of multiple
<gi>surface</gi> elements may be indicated using the
<gi>surfaceGrp</gi> element.</p>
  </remarks>
  <remarks ident="surface-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>L'élément <gi>surface</gi> représente un secteur rectangulaire d’une surface physique faisant partie du matériau source. Ce peut être une feuille du papier, la façade d'un monument, un panneau publicitaire, un rouleau de papyrus ou en fait toute surface à deux dimensions.</p>
    <p>L'espace de coordonnées défini par cet élément peut être considéré comme une grille d'unités horizontales<att>lrx</att> - <att>ulx</att> et verticales <att>uly</att> - <att>lry</att>. Cette grille se superpose à la totalité de toute image directement contenue par l'élément <gi>surface</gi>. Les coordonnées employées par chaque élément <gi>zone</gi>contenu par cette surface doivent être interprétées en référence à la même grille.</p>
  </remarks>
  <remarks ident="surface-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
当該要素<gi>surface</gi>は、素材表面にある矩形範囲を示す。
例えば、紙、碑、掲示板、パピルスの巻子など、2次元の面を持つもの。
</p>
    <p>
当該要素で定義される座標空間は、幅が属性<att>lrx</att> - <att>ulx</att>、高さが属
性<att>uly</att> - <att>lry</att>によるグリッド単位で示される。このグリッドは、要
素<gi>surface</gi>を含む画面全体に重ね合わされる。この表面に含まれてい
る要素<gi>zone</gi>で使われる座標値は、同じグリッドに対する参照と解釈
される。
</p>
  </remarks>
  <listRef>
    <ptr target="#PHFAX"/>
    <ptr target="#PHZLAB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-20" xml:lang="en">defines a written surface as a two-dimensional or three-dimensional 
coordinate space, optionally grouping one or more graphic representations of
that space, zones of interest within that space, and, when using an embedded transcription approach, transcriptions of the writing within them.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">직사각형의 좌표 공간과 그 내부에서 기록 표면부를 정의한다. 수의적으로 그 공간의 하나 이상의 그림 표상과 관심 있는 직사각형 공간을 모아놓는다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">define una superficie escrita en coordinadas rectangulares, agrupando opcionalmente una o más representaciones gráficas de ese espacio, y las zonas rectangulares de interés dentro de él.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">矩形の座標により、書記の表面を定義する。選択的に、空間や矩形範囲中のひ
とつ以上の図表表現をまとめる。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">définit une surface écrite comme un rectangle décrit par ses coordonnées spatiales, en regroupant éventuellement une ou plusieurs représentations
graphiques de cet espace et des zones rectangulaires intéressantes à l'intérieur de
celui-ci.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">definisce una superficie scritta in termini di uno spazio rettangolare di coordinate, eventualmente che raggruppi una o più rappresentazioni grafiche di tale spazio, e delle zone rettangolari di interesse all'interno di questo.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.coordinated"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <!-- added by gen -->
  </classes>
```

^b7

### Block 8

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.labelLike"/>
          <classRef key="model.graphicLike"/>
        </alternate>
      
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <alternate>
            <elementRef key="zone"/>
            <elementRef key="line"/>
            <elementRef key="path"/>
            <elementRef key="surface"/>
            <elementRef key="surfaceGrp"/>
          </alternate>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-11-15" xml:lang="en">describes the method by which this surface is or was
         connected to the main surface.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="glued">
          <desc versionDate="2011-11-15" xml:lang="en">glued in place</desc>
        </valItem>
        <valItem ident="pinned">
          <desc versionDate="2011-11-15" xml:lang="en">pinned or stapled in place</desc>
        </valItem>
        <valItem ident="sewn">
          <desc versionDate="2011-11-15" xml:lang="en">sewn in place</desc>
        </valItem>
      </valList>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2011-11-11" xml:lang="en">indicates whether the
      surface is attached and folded in such a way as to provide two
      writing surfaces.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surface-egXML-wq" source="#UND">
      <facsimile>
        <surface ulx="0" uly="0" lrx="200" lry="300">
          <graphic url="Bovelles-49r.png"/>
        </surface>
      </facsimile>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="surface-remarks" versionDate="2011-11-20" xml:lang="en">
    <p>The <gi>surface</gi> element represents any two-dimensional or three-dimensional space on
some physical surface forming part of the source material, such as a piece of
paper, a face of a monument, a billboard, a scroll, a leaf etc.</p>
    <p>The coordinate space defined by this element may be thought of
    as a grid <att>lrx</att> - <att>ulx</att> units wide and
    <att>uly</att> - <att>lry</att> units high. </p>
    <p>The  <gi>surface</gi> element may contain graphic representations
or transcriptions of written zones, or both. The coordinate values used by every
    <gi>zone</gi> element contained by this element are to be
    understood with reference to the same grid. <!-- If the <att>points</att> attribute is used to indicate the
exact perimeter of the surface being documented, the points defined
are also understood with reference to this same coordinate system.--> </p>
    <p>Where it is useful or meaningful to do so, any grouping of multiple
<gi>surface</gi> elements may be indicated using the
<gi>surfaceGrp</gi> element.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="surface-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>L'élément <gi>surface</gi> représente un secteur rectangulaire d’une surface physique faisant partie du matériau source. Ce peut être une feuille du papier, la façade d'un monument, un panneau publicitaire, un rouleau de papyrus ou en fait toute surface à deux dimensions.</p>
    <p>L'espace de coordonnées défini par cet élément peut être considéré comme une grille d'unités horizontales<att>lrx</att> - <att>ulx</att> et verticales <att>uly</att> - <att>lry</att>. Cette grille se superpose à la totalité de toute image directement contenue par l'élément <gi>surface</gi>. Les coordonnées employées par chaque élément <gi>zone</gi>contenu par cette surface doivent être interprétées en référence à la même grille.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="surface-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
当該要素<gi>surface</gi>は、素材表面にある矩形範囲を示す。
例えば、紙、碑、掲示板、パピルスの巻子など、2次元の面を持つもの。
</p>
    <p>
当該要素で定義される座標空間は、幅が属性<att>lrx</att> - <att>ulx</att>、高さが属
性<att>uly</att> - <att>lry</att>によるグリッド単位で示される。このグリッドは、要
素<gi>surface</gi>を含む画面全体に重ね合わされる。この表面に含まれてい
る要素<gi>zone</gi>で使われる座標値は、同じグリッドに対する参照と解釈
される。
</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHFAX"/>
    <ptr target="#PHZLAB"/>
  </listRef>
```

^b18

