---
type: representation
source-type: document
source: '[[00_sources/tei-p5-when-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 when
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/when.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# when

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12252. Git blob: `90dffb0b0691264bced794db03ed4101b7281938`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="linking" xml:id="gi-when" ident="when">
  <desc versionDate="2005-01-14" xml:lang="en">indicates a point in time either relative to other elements in the same timeline tag, or absolutely.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">동일 시간선상의 태그에서 다른 요소들에 대한 상대적 또는 절대적인 시간 지점을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出一個時間點，相對或絕對於同一時間進程標籤裡的其他元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">同じ要素<gi>timeline</gi>中にある他の要素に対応する時点、または絶対 的な時点を示す。</desc>
  <desc versionDate="2009-10-06" xml:lang="fr">indique un point dans le temps, soit relatif à d'autres éléments de l'élément <gi>timeline</gi> dans lequel il est contenu, soit dans l'absolu.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona una indicación temporal en términos relativos respecto a otros elementos determinados sobre la misma escala temporal, o en términos absolutos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce un'indicazione temporale in termini relativi, rispetto ad altri elementi determinati sulla stessa scala temporale, o in termini assoluti.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="absolute" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">supplies an absolute value for the time.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시간에 대한 절대값을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個絕對時間值。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該時点の、絶対時間を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">contient une valeur temporelle absolue.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un valor temporal absoluto</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica un valore temporale assoluto.</desc>
      <datatype><dataRef key="teidata.temporal.w3c"/></datatype>
      <remarks ident="when-attr.absolute-remarks" versionDate="2009-07-13" xml:lang="en">
        <p>This attribute should always be specified on a <gi>when</gi> element which serves as the target for the <att>origin</att> attribute of a <gi>timeline</gi>. </p>
      </remarks>
      <remarks ident="when-attr.absolute-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>Cet attribut est obligatoire pour l'élément <gi>when</gi> qui est désigné comme cible par l'attribut <att>origin</att> de l'élément <tag>timeline</tag>. </p>
      </remarks>
      <remarks ident="when-attr.absolute-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 要素<gi>timeline</gi>にある属性<att>origin</att>の値で指定され た要素で必要となる。 </p>
      </remarks>
    </attDef>
    <attDef ident="unit" usage="opt">
      <desc versionDate="2007-12-16" xml:lang="en">specifies the unit of time in which the <att>interval</att> value is expressed, if this is not inherited from the parent <gi>timeline</gi>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">상위 <gi>timeline</gi>으로부터 상속받지 않았다면, <att>interval</att> 값이 표현된 시간 단위를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">若未由父元素<gi>timeLine</gi>得到時間單位資訊，則在此指明屬性<att>interval</att>所使用的時間單位。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">親要素<gi>timeLine</gi>から継承されない場合、属性 <att>interval</att>で示される時間の単位を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie l'unité de temps dans laquelle la valeur de l'attribut <att>interval</att> est exprimée, si elle n'est pas héritée de l'élément parent <gi>timeLine</gi>.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la unidad temporal en la que se expresa el valor <att>interval</att>, si este valor no es heredado del padre <gi>timeline</gi>.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica l'unità temporale nel quale è espresso l'attributo <att>interval</att>, se questo non è ereditato dal genitore <gi>timeline</gi></desc>
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
      <desc versionDate="2013-11-19" xml:lang="en">specifies a time
      interval either as a number or as one of the keywords defined
      by the datatype <ident type="datatype">teidata.interval</ident>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시구간의 수치 부분을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明時間區段中的數值部份</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">時間幅を数値で示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie la partie numérique d'un intervalle de temps.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica los componentes numéricos de un intervalo temporal.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la componente numerica di un intervallo temporale.</desc>
      <datatype><dataRef key="teidata.interval"/></datatype>
    </attDef>
    <attDef ident="since" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">identifies the reference point for determining the time of the current <gi>when</gi> element, which is obtained by adding the interval to the time of the reference point.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현재의 <gi>when</gi> 요소의 시간을 결정하기 위한 참조 지점을 식별하며, 이것은 참조 지점의 시간에 구간을 합하여 구해진다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出一個參照點，用以確定現有元素<gi>when</gi>的時間，可於參照點的時間內加入區段而取得。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素<gi>when</gi>の時間となる参照時点を示す。参照時点に時間 幅を足すことで得られる。</desc>
      <desc versionDate="2009-10-06" xml:lang="fr">identifie le point de référence pour déterminer la date ou l'heure de l'élément courant <gi>when</gi> : cette date ou cette heure s'obtiennent en ajoutant la valeur de l'intervalle à la date du point de référence.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica el punto de referencia para la determinación del valor temporal del elemento <gi>when</gi> (cuando) en cuestión, obtenido añadiendo el intervalo al punto de referencia temporal.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica il punto di riferimento per la determinazione del valore temporale dell'elemento <gi>when</gi> corrente, ottenuto aggiungendo l'intervallo al punto di riferimento temporale.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="when-attr.since-remarks" versionDate="2013-11-19" xml:lang="en">
        <p>This attribute should point to another <gi>when</gi>
	element in the same <gi>timeline</gi>. If no value is
	supplied, and the <att>absolute</att> attribute is also unspecified, then the reference point is understood to be the origin of the enclosing <gi>timeline</gi> tag.</p>
      </remarks>
      <remarks ident="when-attr.since-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>Si cet attribut est omis, et qu'il n'y a pas d'attribut <att>absolute</att>, le point de référence retenu est alors l'attribut <att>origin</att>de l'élément englobant <gi>timeline</gi>.</p>
      </remarks>
      <remarks ident="when-attr.since-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性が省略され、かつ属性<att>absolute</att>が指定されてい ない場合、参照時点は、要素<gi>timeline</gi>の始点と解釈される。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-when-egXML-yh" source="#UND">
      <when xml:id="TW3" interval="20" since="#w2"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-when-egXML-li" source="#UND">
      <when xml:id="fr_TW3" interval="20" since="#fr_w2"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-when-egXML-rs" source="#UND">
      <when xml:id="zh-tw_TW3" interval="20" since="#zh-tw_w2"/>
    </egXML>
  </exemplum>
  <remarks ident="when-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>On this element, the global <att>xml:id</att> attribute must be supplied to specify an identifier for this point in time. The value used may be chosen freely provided that it is unique within the document and is a syntactically valid name. There is no requirement for values containing numbers to be in sequence.</p>
  </remarks>
  <remarks ident="when-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>L'élément <gi>when</gi> doit avoir un attribut global <att>xml:id</att> pour identifier ce point dans le temps. La valeur utilisée peut être choisie librement, pourvu qu'elle soit unique dans le document et que le nom soit syntaxiquement valide. Les valeurs contenant des nombres ne doivent pas nécessairement former une séquence.</p>
  </remarks>
  <remarks ident="when-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素には、時点の識別子となるグローバル属性<att>xml:id</att>は 必ず付与される。この値は、当該文書中でユニークであり、統語上妥当で ある名前であれば、自由に選んでよい。一連の数字を含むといった制約は ない。 </p>
  </remarks>
  <listRef>
    <ptr target="#SASYMP" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates a point in time either relative to other elements in the same timeline tag, or absolutely.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">동일 시간선상의 태그에서 다른 요소들에 대한 상대적 또는 절대적인 시간 지점을 표시한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出一個時間點，相對或絕對於同一時間進程標籤裡的其他元素。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">同じ要素<gi>timeline</gi>中にある他の要素に対応する時点、または絶対 的な時点を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-10-06" xml:lang="fr">indique un point dans le temps, soit relatif à d'autres éléments de l'élément <gi>timeline</gi> dans lequel il est contenu, soit dans l'absolu.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una indicación temporal en términos relativos respecto a otros elementos determinados sobre la misma escala temporal, o en términos absolutos.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un'indicazione temporale in termini relativi, rispetto ad altri elementi determinati sulla stessa scala temporale, o in termini assoluti.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies an absolute value for the time.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시간에 대한 절대값을 제시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個絕對時間值。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該時点の、絶対時間を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une valeur temporelle absolue.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un valor temporal absoluto</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica un valore temporale assoluto.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.temporal.w3c"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="when-attr.absolute-remarks" versionDate="2009-07-13" xml:lang="en">
        <p>This attribute should always be specified on a <gi>when</gi> element which serves as the target for the <att>origin</att> attribute of a <gi>timeline</gi>. </p>
      </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="when-attr.absolute-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>Cet attribut est obligatoire pour l'élément <gi>when</gi> qui est désigné comme cible par l'attribut <att>origin</att> de l'élément <tag>timeline</tag>. </p>
      </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="when-attr.absolute-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 要素<gi>timeline</gi>にある属性<att>origin</att>の値で指定され た要素で必要となる。 </p>
      </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-12-16" xml:lang="en">specifies the unit of time in which the <att>interval</att> value is expressed, if this is not inherited from the parent <gi>timeline</gi>.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">상위 <gi>timeline</gi>으로부터 상속받지 않았다면, <att>interval</att> 값이 표현된 시간 단위를 명시한다.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">若未由父元素<gi>timeLine</gi>得到時間單位資訊，則在此指明屬性<att>interval</att>所使用的時間單位。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">親要素<gi>timeLine</gi>から継承されない場合、属性 <att>interval</att>で示される時間の単位を示す。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie l'unité de temps dans laquelle la valeur de l'attribut <att>interval</att> est exprimée, si elle n'est pas héritée de l'élément parent <gi>timeLine</gi>.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la unidad temporal en la que se expresa el valor <att>interval</att>, si este valor no es heredado del padre <gi>timeline</gi>.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica l'unità temporale nel quale è espresso l'attributo <att>interval</att>, se questo non è ereditato dal genitore <gi>timeline</gi></desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b28

### Block 29

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

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2013-11-19" xml:lang="en">specifies a time
      interval either as a number or as one of the keywords defined
      by the datatype <ident type="datatype">teidata.interval</ident>.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시구간의 수치 부분을 명시한다.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明時間區段中的數值部份</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間幅を数値で示す。</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie la partie numérique d'un intervalle de temps.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica los componentes numéricos de un intervalo temporal.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la componente numerica di un intervallo temporale.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.interval"/></datatype>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">identifies the reference point for determining the time of the current <gi>when</gi> element, which is obtained by adding the interval to the time of the reference point.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현재의 <gi>when</gi> 요소의 시간을 결정하기 위한 참조 지점을 식별하며, 이것은 참조 지점의 시간에 구간을 합하여 구해진다.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出一個參照點，用以確定現有元素<gi>when</gi>的時間，可於參照點的時間內加入區段而取得。</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素<gi>when</gi>の時間となる参照時点を示す。参照時点に時間 幅を足すことで得られる。</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2009-10-06" xml:lang="fr">identifie le point de référence pour déterminer la date ou l'heure de l'élément courant <gi>when</gi> : cette date ou cette heure s'obtiennent en ajoutant la valeur de l'intervalle à la date du point de référence.</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica el punto de referencia para la determinación del valor temporal del elemento <gi>when</gi> (cuando) en cuestión, obtenido añadiendo el intervalo al punto de referencia temporal.</desc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica il punto di riferimento per la determinazione del valore temporale dell'elemento <gi>when</gi> corrente, ottenuto aggiungendo l'intervallo al punto di riferimento temporale.</desc>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="when-attr.since-remarks" versionDate="2013-11-19" xml:lang="en">
        <p>This attribute should point to another <gi>when</gi>
	element in the same <gi>timeline</gi>. If no value is
	supplied, and the <att>absolute</att> attribute is also unspecified, then the reference point is understood to be the origin of the enclosing <gi>timeline</gi> tag.</p>
      </remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[2]`.

```xml
<remarks ident="when-attr.since-remarks" versionDate="2009-10-06" xml:lang="fr">
        <p>Si cet attribut est omis, et qu'il n'y a pas d'attribut <att>absolute</att>, le point de référence retenu est alors l'attribut <att>origin</att>de l'élément englobant <gi>timeline</gi>.</p>
      </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[3]`.

```xml
<remarks ident="when-attr.since-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性が省略され、かつ属性<att>absolute</att>が指定されてい ない場合、参照時点は、要素<gi>timeline</gi>の始点と解釈される。 </p>
      </remarks>
```

^b48

### Block 49

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-when-egXML-yh" source="#UND">
      <when xml:id="TW3" interval="20" since="#w2"/>
    </egXML>
  </exemplum>
```

^b49

### Block 50

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-when-egXML-li" source="#UND">
      <when xml:id="fr_TW3" interval="20" since="#fr_w2"/>
    </egXML>
  </exemplum>
```

^b50

### Block 51

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-when-egXML-rs" source="#UND">
      <when xml:id="zh-tw_TW3" interval="20" since="#zh-tw_w2"/>
    </egXML>
  </exemplum>
```

^b51

### Block 52

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="when-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>On this element, the global <att>xml:id</att> attribute must be supplied to specify an identifier for this point in time. The value used may be chosen freely provided that it is unique within the document and is a syntactically valid name. There is no requirement for values containing numbers to be in sequence.</p>
  </remarks>
```

^b52

### Block 53

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="when-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>L'élément <gi>when</gi> doit avoir un attribut global <att>xml:id</att> pour identifier ce point dans le temps. La valeur utilisée peut être choisie librement, pourvu qu'elle soit unique dans le document et que le nom soit syntaxiquement valide. Les valeurs contenant des nombres ne doivent pas nécessairement former une séquence.</p>
  </remarks>
```

^b53

### Block 54

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="when-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素には、時点の識別子となるグローバル属性<att>xml:id</att>は 必ず付与される。この値は、当該文書中でユニークであり、統語上妥当で ある名前であれば、自由に選んでよい。一連の数字を含むといった制約は ない。 </p>
  </remarks>
```

^b54

### Block 55

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SASYMP" type="div3"/>
  </listRef>
```

^b55

