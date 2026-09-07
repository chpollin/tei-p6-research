---
type: representation
source-type: document
source: '[[00_sources/tei-p5-u-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 u
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/u.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# u

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10554. Git blob: `40bb1a7ff566f2c594baf7d79b86f4806dad29f6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" xml:id="gi-u" ident="u">
  <gloss versionDate="2005-01-14" xml:lang="en">utterance</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">발화</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">話語</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">énonciation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">enunciado</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">enunciato</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">contains a stretch of speech usually preceded and followed by silence or by a change of speaker.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일반적으로 침묵 또는 화자 바뀜에 의해 구분되는, 말의 연속체.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">一段言詞，通常在說話前後是一段沉默、或是另一個人的說話。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">一般に沈黙または話者交替が前後する、発話の時間。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">partie de discours généralement précédée et suivie d'un silence ou d'un changement de locuteur.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">fragmento de texto hablado precedido y seguido normalmente de un silencio o de un cambio de hablante</desc>
  <desc versionDate="2007-01-21" xml:lang="it">porzione di parlato solitamente preceduta e seguita da un silenzio o da un cambio di parlante.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.timed"/>
    <memberOf key="model.divPart.spoken"/>
    <memberOf key="model.standOffPart"/>   
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="trans" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">transition</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">전이</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">transición</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">transizione</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates the nature of the transition between this utterance and the previous one.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">발화 사이의 전이적 특성을 나타낸다.</desc>
      <desc versionDate="2008-10-02" xml:lang="fr">transition</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出此段話語和前段話語之間轉變過程的特性。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">前の発話から当該発話への遷移(交替)の性質を示す。</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la naturaleza de la transición entre un enunciado y el precedente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la natura del passaggio tra questo enunciato e il precedente.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>smooth</defaultVal>
      <valList type="closed">
        <valItem ident="smooth">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins without unusual pause or rapidity.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">발화가 일상적 휴지 또는 신속함 없이 시작된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語的開頭並無異常停頓或異常迅速。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza sin la pausa inicial o con una rapidez inusual.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、変な間や急ぐことなく、始まる。</desc>
          <desc versionDate="2009-04-17" xml:lang="fr">cette intervention commence avec une pause dont la durée n'est pas inhabituelle</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia senza pause o accelerazioni insolite.</desc>
        </valItem>
        <valItem ident="latching">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins with a markedly shorter pause than normal.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">발화가 평소보다 두드러지게 짧은 휴지와 더불어 시작한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語開頭的停頓明顯比平常要短。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza con una pausa marcada más corta de lo normal.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、普通より短い間に続けて、始まる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette intervention commence par une pause manifestement plus courte que la normale</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia con una pausa nettamente più breve del normale.</desc>
        </valItem>
        <valItem ident="overlap">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins before the previous one has finished.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이전 발화가 끝나기 전에 발화가 시작한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語在前一段還未結束前就開始。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza antes de que la anterior haya acabado.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、以前の発話が終わる前に、始まる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette intervention commence avant que la précédente ne soit finie</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia prima che sia terminato quello precedente.</desc>
        </valItem>
        <valItem ident="pause">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins after a noticeable pause.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">현저한 휴지 이후에 발화가 시작한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語在一段明顯的停頓之後開始。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza después de una pausa notable.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、目立った間に続けて、始まる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette intervention commence après une
pause considérable</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia con una pausa notevolmente lunga.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-u-egXML-rz">
      <u who="#spkr1">if did you set</u>
      <u trans="latching" who="#spkr2">well Joe and I set it between us</u>
      <list type="speakers">
        <item xml:id="spkr1"/>
        <item xml:id="spkr2"/>
      </list>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-u-egXML-uq">
      <u who="#fr_spkr1">si tu te déplaçais</u>
      <u trans="latching" who="#fr_spkr2">Joe et moi l'aurions mis entre nous</u>
      <list type="speakers">
        <item xml:id="fr_spkr1"/>
        <item xml:id="fr_spkr2"/>
      </list>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-u-egXML-jy">
      <u who="#zh-tw_spkr1">假如你真的決定</u>
      <u trans="latching" who="#zh-tw_spkr2">...我和小文會在我們之間做個決定</u>
      <list type="speakers">
        <item xml:id="zh-tw_spkr1"/>
        <item xml:id="zh-tw_spkr2"/>
      </list>
    </egXML>
  </exemplum>
  <remarks ident="u-remarks" versionDate="2007-06-27" xml:lang="en">
    <p rend="dataDesc">Prose and a mixture of speech
elements</p>
    <p>Although individual transcriptions may consistently use
<gi>u</gi> elements for turns or other units, and although in most
cases a <gi>u</gi> will be delimited by pause or change of speaker,
<gi>u</gi> is not required to represent a turn or any communicative
event, nor to be bounded by pauses or change of speaker.  At a minimum,
a <gi>u</gi> is some phonetic production by a given speaker.</p>
  </remarks>
  <remarks ident="u-remarks" versionDate="2009-04-17" xml:lang="fr">
    <p rend="dataDesc">Prose et combinaison d'éléments pour la transcription de l'oral</p>
    <p>Bien que certaines transcriptions emploient systématiquement des éléments <gi>u</gi>
                dans le cas de tours de parole ou pour d'autres unités linguistiques, et bien que dans la
                plupart des cas un élément <gi>u</gi> soit délimité par une pause ou par un
                changement de locuteur, l’élément <gi>u</gi> ne représente pas obligatoirement un tour de parole ou tout autre événement de communication, et n'est pas nécessairement
                limité par des pauses ou par un changement de locuteur. A minima,
                l’élément<gi>u</gi> peut être un phonème émis par un locuteur donné.</p>
  </remarks>
  <remarks ident="u-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    散文と発話要素の混在。
    </p>
    <p>
    個々の発話遷移(交替)は、ターンを示す要素<gi>u</gi>や他の要素により
    示され、多くの場合、要素<gi>u</gi>はその前後を間や発話交替で区切ら
    れている。しかし、要素<gi>u</gi>は、ターンや伝達に関する事象を示す
    ために必須のものではない。また、その前後に間や発話交替があることも
    必須ではない。最低限、要素<gi>u</gi>は、話者が示す音声である。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TSBAUT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">utterance</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">발화</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">話語</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">énonciation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">enunciado</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">enunciato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains a stretch of speech usually preceded and followed by silence or by a change of speaker.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일반적으로 침묵 또는 화자 바뀜에 의해 구분되는, 말의 연속체.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">一段言詞，通常在說話前後是一段沉默、或是另一個人的說話。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">一般に沈黙または話者交替が前後する、発話の時間。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">partie de discours généralement précédée et suivie d'un silence ou d'un changement de locuteur.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">fragmento de texto hablado precedido y seguido normalmente de un silencio o de un cambio de hablante</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">porzione di parlato solitamente preceduta e seguita da un silenzio o da un cambio di parlante.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.timed"/>
    <memberOf key="model.divPart.spoken"/>
    <memberOf key="model.standOffPart"/>   
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">transition</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">전이</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">transición</gloss>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">transizione</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the nature of the transition between this utterance and the previous one.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">발화 사이의 전이적 특성을 나타낸다.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-10-02" xml:lang="fr">transition</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出此段話語和前段話語之間轉變過程的特性。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">前の発話から当該発話への遷移(交替)の性質を示す。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la naturaleza de la transición entre un enunciado y el precedente.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la natura del passaggio tra questo enunciato e il precedente.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>smooth</defaultVal>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="smooth">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins without unusual pause or rapidity.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">발화가 일상적 휴지 또는 신속함 없이 시작된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語的開頭並無異常停頓或異常迅速。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza sin la pausa inicial o con una rapidez inusual.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、変な間や急ぐことなく、始まる。</desc>
          <desc versionDate="2009-04-17" xml:lang="fr">cette intervention commence avec une pause dont la durée n'est pas inhabituelle</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia senza pause o accelerazioni insolite.</desc>
        </valItem>
        <valItem ident="latching">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins with a markedly shorter pause than normal.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">발화가 평소보다 두드러지게 짧은 휴지와 더불어 시작한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語開頭的停頓明顯比平常要短。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza con una pausa marcada más corta de lo normal.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、普通より短い間に続けて、始まる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette intervention commence par une pause manifestement plus courte que la normale</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia con una pausa nettamente più breve del normale.</desc>
        </valItem>
        <valItem ident="overlap">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins before the previous one has finished.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이전 발화가 끝나기 전에 발화가 시작한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語在前一段還未結束前就開始。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza antes de que la anterior haya acabado.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、以前の発話が終わる前に、始まる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette intervention commence avant que la précédente ne soit finie</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia prima che sia terminato quello precedente.</desc>
        </valItem>
        <valItem ident="pause">
          <desc versionDate="2007-06-27" xml:lang="en">this utterance begins after a noticeable pause.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">현저한 휴지 이후에 발화가 시작한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此段話語在一段明顯的停頓之後開始。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta elocución comienza después de una pausa notable.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該発話は、目立った間に続けて、始まる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette intervention commence après une
pause considérable</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'enunciato comincia con una pausa notevolmente lunga.</desc>
        </valItem>
      </valList>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-u-egXML-rz">
      <u who="#spkr1">if did you set</u>
      <u trans="latching" who="#spkr2">well Joe and I set it between us</u>
      <list type="speakers">
        <item xml:id="spkr1"/>
        <item xml:id="spkr2"/>
      </list>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-u-egXML-uq">
      <u who="#fr_spkr1">si tu te déplaçais</u>
      <u trans="latching" who="#fr_spkr2">Joe et moi l'aurions mis entre nous</u>
      <list type="speakers">
        <item xml:id="fr_spkr1"/>
        <item xml:id="fr_spkr2"/>
      </list>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-u-egXML-jy">
      <u who="#zh-tw_spkr1">假如你真的決定</u>
      <u trans="latching" who="#zh-tw_spkr2">...我和小文會在我們之間做個決定</u>
      <list type="speakers">
        <item xml:id="zh-tw_spkr1"/>
        <item xml:id="zh-tw_spkr2"/>
      </list>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="u-remarks" versionDate="2007-06-27" xml:lang="en">
    <p rend="dataDesc">Prose and a mixture of speech
elements</p>
    <p>Although individual transcriptions may consistently use
<gi>u</gi> elements for turns or other units, and although in most
cases a <gi>u</gi> will be delimited by pause or change of speaker,
<gi>u</gi> is not required to represent a turn or any communicative
event, nor to be bounded by pauses or change of speaker.  At a minimum,
a <gi>u</gi> is some phonetic production by a given speaker.</p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="u-remarks" versionDate="2009-04-17" xml:lang="fr">
    <p rend="dataDesc">Prose et combinaison d'éléments pour la transcription de l'oral</p>
    <p>Bien que certaines transcriptions emploient systématiquement des éléments <gi>u</gi>
                dans le cas de tours de parole ou pour d'autres unités linguistiques, et bien que dans la
                plupart des cas un élément <gi>u</gi> soit délimité par une pause ou par un
                changement de locuteur, l’élément <gi>u</gi> ne représente pas obligatoirement un tour de parole ou tout autre événement de communication, et n'est pas nécessairement
                limité par des pauses ou par un changement de locuteur. A minima,
                l’élément<gi>u</gi> peut être un phonème émis par un locuteur donné.</p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="u-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    散文と発話要素の混在。
    </p>
    <p>
    個々の発話遷移(交替)は、ターンを示す要素<gi>u</gi>や他の要素により
    示され、多くの場合、要素<gi>u</gi>はその前後を間や発話交替で区切ら
    れている。しかし、要素<gi>u</gi>は、ターンや伝達に関する事象を示す
    ために必須のものではない。また、その前後に間や発話交替があることも
    必須ではない。最低限、要素<gi>u</gi>は、話者が示す音声である。
    </p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSBAUT"/>
  </listRef>
```

^b36

