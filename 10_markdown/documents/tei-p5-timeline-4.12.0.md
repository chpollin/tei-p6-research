---
type: representation
source-type: document
source: '[[00_sources/tei-p5-timeline-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 timeline
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/timeline.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# timeline

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11634. Git blob: `1fd42530dc0e5e60a5472a7d04b06b23fbb8ddd9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="linking" xml:id="gi-timeline" ident="timeline">
  <gloss versionDate="2007-01-21" xml:lang="en">timeline</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">시간선상</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">時間進程</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">frise chronologique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">escala temporal</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">scala temporale</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides a set of ordered points in time which can be linked to elements of a spoken text to create a temporal alignment of that text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">해당 텍스트의 시간 정렬을 생성하기 위해 구어 텍스트의 요소들이 연결될 수 있는 시간의 순서로 정렬된 지점의 집합을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一組整齊的時間順序點，可與口說文本的元素相連結，以建立該文本的時間組序。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">時間的なまとまりを示すために、発話テキストの要素をリンクすることがで きる、時間軸上の順序付き時点の集合を示す。</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">fournit un ensemble de points ordonnés dans le temps qui peuvent être liés à des éléments de la parole transcrite pour créer un alignement temporel de ce texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica una serie de puntos ordenados temporalmente los cuales pueden ser enlazados a los elementos de un texto hablado a fin de obtener un alineamiento temporal del texto mismo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica una serie di punti ordinati temporalmente i quali possono essere collegati agli elementi di un testo parlato al fine di ottenere un allineamento temporale del testo stesso.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    
      <elementRef key="when" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
  <attList>
    <attDef ident="origin" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">designates the origin of the timeline, i.e. the time at which it begins.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시간선상의 시작점을 가리킨다, 즉, 시작 시간</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標出時間進程的開頭，例如開始時間。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">時間軸の起点示す。すなわち、始点の時間。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">désigne le début de la frise chronologique, c'est-à-dire le moment où elle commence.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el origen de la escala temporal, es decir, el momento en que inicia.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'origine della scala temporale, cioè il momento in cui ha inizio.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="timeline-attr.origin-remarks" versionDate="2013-11-21" xml:lang="en">
        <p>If this attribute is not supplied, the implication is that
	the time of origin is not known. If it is supplied, it must
	point either to one of the <gi>when</gi> elements in its
	content, or to another <gi>timeline</gi> element. </p>
      </remarks>
      <remarks ident="timeline-attr.origin-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>Si cet attribut n'est pas fourni, cela implique que le moment où commence la frise n'est pas connu.</p>
      </remarks>
    </attDef>
    <attDef ident="unit" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the unit of time corresponding to the <att>interval</att> value of the timeline or of its constituent points in time.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시간선상의 <att>interval</att> 값에 일치하는 시간 또는 시간 구성성분 지점의 단위를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出符合時間進程屬性<att>interval</att>的屬性值或是符合其接續時間點的時間單位。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">時間軸を構成する属性<att>interval</att>の値に対応する、時間単位 を特定する。</desc>
      <desc versionDate="2009-04-17" xml:lang="fr">spécifie l'unité de temps correspondant à la valeur de l'attribut <att>interval</att> de la frise chronologique ou des points temporels qui la constituent.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la unidad temporal correspondiente al valor del atributo <att>interval</att> (intervalo) de la escala temporal o de sus puntos constitutivos.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica l'unità temporale corrispondente al valore dell'attributo <att>interval</att> della scala temporale o dei suoi punti costitutivi.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="d">
          <gloss versionDate="2005-08-28" xml:lang="en">days</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">jours</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">giorni</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">días</gloss>
        </valItem>
        <valItem ident="h">
          <gloss versionDate="2005-08-28" xml:lang="en">hours</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">heures</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">ore</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">horas</gloss>
        </valItem>
        <valItem ident="min">
          <gloss versionDate="2007-07-04" xml:lang="en">minutes</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">minutos</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">minuti</gloss>
        </valItem>
        <valItem ident="s">
          <gloss versionDate="2005-08-28" xml:lang="en">seconds</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">secondes</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">secondi</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">segundos</gloss>
        </valItem>
        <valItem ident="ms">
          <gloss versionDate="2005-08-28" xml:lang="en">milliseconds</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">millisecondes</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">millesimi di secondo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">milésimas de segundo</gloss>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="interval" usage="opt">
      <desc versionDate="2013-11-20" xml:lang="en">specifies a time
      interval either as a positive integral value or using one of a
      set of predefined codes.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시구간의 수치 비율을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明時間區段中的數值部份</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">間隔を表す数値を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie la partie numérique d'un intervalle de temps.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica los componentes numéricos de un intervalo de tiempo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la componente numerica di un intervallo temporale.</desc>
      <datatype><dataRef key="teidata.interval"/></datatype>
      <remarks ident="timeline-attr.interval-remarks" versionDate="2005-10-12" xml:lang="en">
        <p>The value <val>irregular</val> indicates uncertainty about all the intervals in the timeline; the value <val>regular</val> indicates that all the intervals are evenly spaced, but the size of the intervals is not known; numeric values indicate evenly spaced values of the size specified. If individual points in time in the timeline are given different values for the <att>interval</att> attribute, those values locally override the value given in the timeline.</p>
      </remarks>
      <remarks ident="timeline-attr.interval-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>La valeur <val>irregular</val> indique une incertitude sur tous les intervalles de la frise chronologique ; la valeur <val>regular</val> indique que tous les intervalles sont espacés régulièrement, mais que leur taille est inconnue ; des valeurs numériques indiquent des intervalles régulièrement espacés, de la taille spécifiée. Si on attribue à certains points temporels de la frise chronologique des valeurs différentes pour l'attribut <att>interval</att>, ces valeurs prennent le pas pour ces points sur la valeur donnée dans la frise chronologique.</p>
      </remarks>
      <remarks ident="timeline-attr.interval-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 値<val>irregular</val>は、時間軸上の間隔がはっきりしないことを 示す。値<val>regular</val>は、間隔が均等にとられていることを示 す。但し、その間隔の大きさは不明である。属性値が数値の場合、こ の大きさにより間隔は均等にとられていることを示す。時間軸上にあ る時点の属性<att>interval</att>が、異なる値をとる場合、その値 により、時間軸上にある値を上書きすると解釈される。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-timeline-egXML-br" source="#UND">
      <timeline xml:id="TL01" unit="ms">
        <when xml:id="TL-w0" absolute="11:30:00"/>
        <when xml:id="TL-w1" interval="unknown" since="#TL-w0"/>
        <when xml:id="TL-w2" interval="100" since="#TL-w1"/>
        <when xml:id="TL-w3" interval="200" since="#TL-w2"/>
        <when xml:id="TL-w4" interval="150" since="#TL-w3"/>
        <when xml:id="TL-w5" interval="250" since="#TL-w4"/>
        <when xml:id="TL-w6" interval="100" since="#TL-w5"/>
      </timeline>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-timeline-egXML-ft" source="#UND">
      <timeline xml:id="fr_TL01" origin="#fr_TL-w0" unit="ms">
        <when xml:id="fr_TL-w0" absolute="11:30:00"/>
        <when xml:id="fr_TL-w1" interval="unknown" since="#fr_TL-w0"/>
        <when xml:id="fr_TL-w2" interval="100" since="#fr_TL-w1"/>
        <when xml:id="fr_TL-w3" interval="200" since="#fr_TL-w2"/>
        <when xml:id="fr_TL-w4" interval="150" since="#fr_TL-w3"/>
        <when xml:id="fr_TL-w5" interval="250" since="#fr_TL-w4"/>
        <when xml:id="fr_TL-w6" interval="100" since="#fr_TL-w5"/>
      </timeline>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#SASYMP" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="en">timeline</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">시간선상</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">時間進程</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">frise chronologique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">escala temporal</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">scala temporale</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides a set of ordered points in time which can be linked to elements of a spoken text to create a temporal alignment of that text.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">해당 텍스트의 시간 정렬을 생성하기 위해 구어 텍스트의 요소들이 연결될 수 있는 시간의 순서로 정렬된 지점의 집합을 제시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一組整齊的時間順序點，可與口說文本的元素相連結，以建立該文本的時間組序。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間的なまとまりを示すために、発話テキストの要素をリンクすることがで きる、時間軸上の順序付き時点の集合を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">fournit un ensemble de points ordonnés dans le temps qui peuvent être liés à des éléments de la parole transcrite pour créer un alignement temporel de ce texte.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica una serie de puntos ordenados temporalmente los cuales pueden ser enlazados a los elementos de un texto hablado a fin de obtener un alineamiento temporal del texto mismo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica una serie di punti ordinati temporalmente i quali possono essere collegati agli elementi di un testo parlato al fine di ottenere un allineamento temporale del testo stesso.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <elementRef key="when" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">designates the origin of the timeline, i.e. the time at which it begins.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시간선상의 시작점을 가리킨다, 즉, 시작 시간</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標出時間進程的開頭，例如開始時間。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間軸の起点示す。すなわち、始点の時間。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">désigne le début de la frise chronologique, c'est-à-dire le moment où elle commence.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el origen de la escala temporal, es decir, el momento en que inicia.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'origine della scala temporale, cioè il momento in cui ha inizio.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="timeline-attr.origin-remarks" versionDate="2013-11-21" xml:lang="en">
        <p>If this attribute is not supplied, the implication is that
	the time of origin is not known. If it is supplied, it must
	point either to one of the <gi>when</gi> elements in its
	content, or to another <gi>timeline</gi> element. </p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="timeline-attr.origin-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>Si cet attribut n'est pas fourni, cela implique que le moment où commence la frise n'est pas connu.</p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the unit of time corresponding to the <att>interval</att> value of the timeline or of its constituent points in time.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시간선상의 <att>interval</att> 값에 일치하는 시간 또는 시간 구성성분 지점의 단위를 명시한다.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出符合時間進程屬性<att>interval</att>的屬性值或是符合其接續時間點的時間單位。</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間軸を構成する属性<att>interval</att>の値に対応する、時間単位 を特定する。</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">spécifie l'unité de temps correspondant à la valeur de l'attribut <att>interval</att> de la frise chronologique ou des points temporels qui la constituent.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la unidad temporal correspondiente al valor del atributo <att>interval</att> (intervalo) de la escala temporal o de sus puntos constitutivos.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica l'unità temporale corrispondente al valore dell'attributo <att>interval</att> della scala temporale o dei suoi punti costitutivi.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="d">
          <gloss versionDate="2005-08-28" xml:lang="en">days</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">jours</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">giorni</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">días</gloss>
        </valItem>
        <valItem ident="h">
          <gloss versionDate="2005-08-28" xml:lang="en">hours</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">heures</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">ore</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">horas</gloss>
        </valItem>
        <valItem ident="min">
          <gloss versionDate="2007-07-04" xml:lang="en">minutes</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">minutos</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">minuti</gloss>
        </valItem>
        <valItem ident="s">
          <gloss versionDate="2005-08-28" xml:lang="en">seconds</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">secondes</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">secondi</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">segundos</gloss>
        </valItem>
        <valItem ident="ms">
          <gloss versionDate="2005-08-28" xml:lang="en">milliseconds</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">millisecondes</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">millesimi di secondo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">milésimas de segundo</gloss>
        </valItem>
      </valList>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2013-11-20" xml:lang="en">specifies a time
      interval either as a positive integral value or using one of a
      set of predefined codes.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시구간의 수치 비율을 명시한다.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明時間區段中的數值部份</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">間隔を表す数値を示す。</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie la partie numérique d'un intervalle de temps.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica los componentes numéricos de un intervalo de tiempo.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la componente numerica di un intervallo temporale.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.interval"/></datatype>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="timeline-attr.interval-remarks" versionDate="2005-10-12" xml:lang="en">
        <p>The value <val>irregular</val> indicates uncertainty about all the intervals in the timeline; the value <val>regular</val> indicates that all the intervals are evenly spaced, but the size of the intervals is not known; numeric values indicate evenly spaced values of the size specified. If individual points in time in the timeline are given different values for the <att>interval</att> attribute, those values locally override the value given in the timeline.</p>
      </remarks>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="timeline-attr.interval-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>La valeur <val>irregular</val> indique une incertitude sur tous les intervalles de la frise chronologique ; la valeur <val>regular</val> indique que tous les intervalles sont espacés régulièrement, mais que leur taille est inconnue ; des valeurs numériques indiquent des intervalles régulièrement espacés, de la taille spécifiée. Si on attribue à certains points temporels de la frise chronologique des valeurs différentes pour l'attribut <att>interval</att>, ces valeurs prennent le pas pour ces points sur la valeur donnée dans la frise chronologique.</p>
      </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="timeline-attr.interval-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 値<val>irregular</val>は、時間軸上の間隔がはっきりしないことを 示す。値<val>regular</val>は、間隔が均等にとられていることを示 す。但し、その間隔の大きさは不明である。属性値が数値の場合、こ の大きさにより間隔は均等にとられていることを示す。時間軸上にあ る時点の属性<att>interval</att>が、異なる値をとる場合、その値 により、時間軸上にある値を上書きすると解釈される。 </p>
      </remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-timeline-egXML-br" source="#UND">
      <timeline xml:id="TL01" unit="ms">
        <when xml:id="TL-w0" absolute="11:30:00"/>
        <when xml:id="TL-w1" interval="unknown" since="#TL-w0"/>
        <when xml:id="TL-w2" interval="100" since="#TL-w1"/>
        <when xml:id="TL-w3" interval="200" since="#TL-w2"/>
        <when xml:id="TL-w4" interval="150" since="#TL-w3"/>
        <when xml:id="TL-w5" interval="250" since="#TL-w4"/>
        <when xml:id="TL-w6" interval="100" since="#TL-w5"/>
      </timeline>
    </egXML>
  </exemplum>
```

^b46

### Block 47

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-timeline-egXML-ft" source="#UND">
      <timeline xml:id="fr_TL01" origin="#fr_TL-w0" unit="ms">
        <when xml:id="fr_TL-w0" absolute="11:30:00"/>
        <when xml:id="fr_TL-w1" interval="unknown" since="#fr_TL-w0"/>
        <when xml:id="fr_TL-w2" interval="100" since="#fr_TL-w1"/>
        <when xml:id="fr_TL-w3" interval="200" since="#fr_TL-w2"/>
        <when xml:id="fr_TL-w4" interval="150" since="#fr_TL-w3"/>
        <when xml:id="fr_TL-w5" interval="250" since="#fr_TL-w4"/>
        <when xml:id="fr_TL-w6" interval="100" since="#fr_TL-w5"/>
      </timeline>
    </egXML>
  </exemplum>
```

^b47

### Block 48

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SASYMP" type="div3"/>
  </listRef>
```

^b48

