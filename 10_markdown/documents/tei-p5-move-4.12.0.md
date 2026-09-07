---
type: representation
source-type: document
source: '[[00_sources/tei-p5-move-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 move
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/move.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# move

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12027. Git blob: `0ecf1677d9dce32a61d0c69b6f7ec7ab1ab9f2e1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-move" ident="move">
  <gloss versionDate="2007-07-04" xml:lang="en">movement</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">이동</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">動作</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">movimiento</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">mouvement</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">movimento</gloss>
  <desc versionDate="2017-11-17" xml:lang="en">marks the actual movement of one or more characters.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">무대에서 하나 이상의 등장 인물들의 실제적 입장과 퇴장을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記舞台上人物的實際進場或退場。</desc>
  <desc versionDate="2017-11-17" xml:lang="es">marca la entrada o salida real de uno o más personajes.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">舞台上で、ひとり以上の登場人物の出やはけを示す。</desc>
  <desc versionDate="2017-11-17" xml:lang="fr">signale l'entrée ou la sortie d'un ou de plusieurs
    personnages.</desc>
  <desc versionDate="2017-11-17" xml:lang="it">segnala l'entrata o uscita di uno o più
    personaggi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">characterizes the movement, for example as an entrance or exit.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 입장 또는 퇴장과 같은, 이동의 특성을 기술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明舞台動作，例如進場或退場。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">caracteriza el movimiento, por ejemplo de una entrada
        o de una salida.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該動きの分類を示す。例えば、出、はけ、など。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">caractérise un mouvement , par exemple une entrée ou
        une sortie.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il tipo di movimento, ad esempio come entrata
        o uscita.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="entrance">
          <desc versionDate="2007-06-27" xml:lang="en">character is entering the stage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">등장인물이 무대에 등장하고 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">角色進場</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el personaje se incorpora a la escena.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">登場人物が舞台に出る。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le personnage entre en scène.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il personaggio entra in scena.</desc>
        </valItem>
        <valItem ident="exit">
          <desc versionDate="2007-06-27" xml:lang="en">character is exiting the stage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">등장인물이 무대에서 퇴장하고 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">角色退場</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el personaje sale de la escena.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">登場人物が舞台からはける。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le personnage sort de scène.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il personaggio lascia la scena.</desc>
        </valItem>
        <valItem ident="onStage">
          <desc versionDate="2007-07-04" xml:lang="en">character moves on stage</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">등장인물이 무대에서 이동한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el personaje se mueve en la escena</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">登場人物が舞台上で移動する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le personnage se déplace sur scène.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il personaggio si muove sulla scena.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="where" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the direction of a stage movement.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">무대 이동의 방향을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明舞台動作的方向。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">especifica la dirección de un movimiento en el
        escenario.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">舞台上の動きの方向を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique la direction d'un mouvement sur scène.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica la direzione di un movimento in scena.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.authority"/></datatype>
      <valList type="open">
        <valItem ident="L">
          <gloss versionDate="2007-07-04" xml:lang="en">left</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">왼쪽</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">izquierdo</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">à gauche</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sinistra</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">stage left</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">무대 왼쪽</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台左側</desc>
          <desc versionDate="2008-04-06" xml:lang="es">izquierda del escenario</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">上手。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">côté cour (à gauche).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lato sinistro della scena.</desc>
        </valItem>
        <valItem ident="R">
          <gloss versionDate="2007-07-04" xml:lang="en">right</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">오른쪽</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">derecha</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">à droite.</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">destra</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">stage right</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">무대 오른쪽</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台右側</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la derecha del escenario</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">下手。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">côté jardin (à droite).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lato destro della scena.</desc>
        </valItem>
        <valItem ident="C">
          <gloss versionDate="2007-07-04" xml:lang="en">center</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">중앙</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">centro</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">au centre</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">centro</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">centre stage</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">무대 중앙</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台中央</desc>
          <desc versionDate="2008-04-06" xml:lang="es">centro del escenario</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">舞台中央。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">milieu de scène</desc>
          <desc versionDate="2007-01-21" xml:lang="it">centro della scena.</desc>
        </valItem>
      </valList>
      <remarks ident="move-attr.where-remarks" versionDate="2020-02-12" xml:lang="en">
        <p>Full blocking information will normally require combinations of values, (for example
            <q>UL</q> for <q>upper stage left</q>) and may also require more detailed encoding of
          speed, direction etc. Full documentation of any coding system used should be provided in
          the header. URIs may be used as values.</p>
      </remarks>
      <remarks ident="move-attr.where-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Donner une information complète de mise en place requiert normalement une combinaison de
          valeurs (par ex. : <q>FG</q> pour <q>au fond à gauche de la scène</q>) et peut aussi
          nécessiter d'encoder de façon plus précise la vitesse, la direction, etc. La documentation
          complète de toute règle de codage doit être fournie dans l'en-tête TEI.</p>
      </remarks>
      <remarks ident="move-attr.where-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 演出情報をもっと記述するには、これらの値の組み合わせ(例えば、 上手上段を示す<q>UL</q>)や、早さや方向など、より詳細な符号化が必
          要となるだろう。符号化システムに関する詳細な記録は、ヘダー内で示 されるべきである。 </p>
      </remarks>
    </attDef>
   
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-move-egXML-vi">
      <performance xml:id="perf1">
        <p>First performance</p>
        <castList>
          <castItem>
            <role xml:id="bellaf">Bellafront</role>
          </castItem>
          <!-- ... -->
        </castList>
      </performance>
      <!-- ... -->
      <stage type="entrance"><move who="#bellaf" type="enter" where="L" perf="#perf1"/> Enter
        Bellafront mad.</stage>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-move-egXML-vd" source="#fr-ex-Shakes-Richard-III">
      <performance xml:id="fr_perf1">
        <p>Première apparition</p>
        <castList>
          <castItem>
            <role xml:id="fr_clar">Clarence</role>
          </castItem>
        </castList>
      </performance>
      <stage type="entrance"><move who="#fr_clar" type="enter" perf="#perf1"/>(Entre Clarence,
          entouré de gardes).</stage>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-move-egXML-jc">
      <performance xml:id="zh-tw_perf1">
        <p>第一場戲</p>
        <castList>
          <castItem>
            <role xml:id="zh-tw_bellaf">楊四郎</role>
          </castItem>
          <!-- 其他角色 -->
        </castList>
      </performance>
      <!-- ... -->
      <stage type="entrance"><move who="#zh-tw_bellaf" type="enter" where="L" perf="#perf1"/>
        進場：楊四郎，鬱悶思鄉。</stage>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DRSTA" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">movement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">이동</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">動作</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">movimiento</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">mouvement</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">movimento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-11-17" xml:lang="en">marks the actual movement of one or more characters.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">무대에서 하나 이상의 등장 인물들의 실제적 입장과 퇴장을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記舞台上人物的實際進場或退場。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2017-11-17" xml:lang="es">marca la entrada o salida real de uno o más personajes.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">舞台上で、ひとり以上の登場人物の出やはけを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-11-17" xml:lang="fr">signale l'entrée ou la sortie d'un ou de plusieurs
    personnages.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2017-11-17" xml:lang="it">segnala l'entrata o uscita di uno o più
    personaggi.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">characterizes the movement, for example as an entrance or exit.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어 입장 또는 퇴장과 같은, 이동의 특성을 기술한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明舞台動作，例如進場或退場。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">caracteriza el movimiento, por ejemplo de una entrada
        o de una salida.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該動きの分類を示す。例えば、出、はけ、など。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">caractérise un mouvement , par exemple une entrée ou
        une sortie.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il tipo di movimento, ad esempio come entrata
        o uscita.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="entrance">
          <desc versionDate="2007-06-27" xml:lang="en">character is entering the stage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">등장인물이 무대에 등장하고 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">角色進場</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el personaje se incorpora a la escena.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">登場人物が舞台に出る。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le personnage entre en scène.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il personaggio entra in scena.</desc>
        </valItem>
        <valItem ident="exit">
          <desc versionDate="2007-06-27" xml:lang="en">character is exiting the stage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">등장인물이 무대에서 퇴장하고 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">角色退場</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el personaje sale de la escena.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">登場人物が舞台からはける。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le personnage sort de scène.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il personaggio lascia la scena.</desc>
        </valItem>
        <valItem ident="onStage">
          <desc versionDate="2007-07-04" xml:lang="en">character moves on stage</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">등장인물이 무대에서 이동한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el personaje se mueve en la escena</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">登場人物が舞台上で移動する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le personnage se déplace sur scène.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il personaggio si muove sulla scena.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the direction of a stage movement.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">무대 이동의 방향을 명시한다.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明舞台動作的方向。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">especifica la dirección de un movimiento en el
        escenario.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">舞台上の動きの方向を示す。</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la direction d'un mouvement sur scène.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica la direzione di un movimento in scena.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.authority"/></datatype>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="L">
          <gloss versionDate="2007-07-04" xml:lang="en">left</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">왼쪽</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">izquierdo</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">à gauche</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sinistra</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">stage left</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">무대 왼쪽</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台左側</desc>
          <desc versionDate="2008-04-06" xml:lang="es">izquierda del escenario</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">上手。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">côté cour (à gauche).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lato sinistro della scena.</desc>
        </valItem>
        <valItem ident="R">
          <gloss versionDate="2007-07-04" xml:lang="en">right</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">오른쪽</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">derecha</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">à droite.</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">destra</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">stage right</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">무대 오른쪽</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台右側</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la derecha del escenario</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">下手。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">côté jardin (à droite).</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lato destro della scena.</desc>
        </valItem>
        <valItem ident="C">
          <gloss versionDate="2007-07-04" xml:lang="en">center</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">중앙</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">centro</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">au centre</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">centro</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">centre stage</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">무대 중앙</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">舞台中央</desc>
          <desc versionDate="2008-04-06" xml:lang="es">centro del escenario</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">舞台中央。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">milieu de scène</desc>
          <desc versionDate="2007-01-21" xml:lang="it">centro della scena.</desc>
        </valItem>
      </valList>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="move-attr.where-remarks" versionDate="2020-02-12" xml:lang="en">
        <p>Full blocking information will normally require combinations of values, (for example
            <q>UL</q> for <q>upper stage left</q>) and may also require more detailed encoding of
          speed, direction etc. Full documentation of any coding system used should be provided in
          the header. URIs may be used as values.</p>
      </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="move-attr.where-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Donner une information complète de mise en place requiert normalement une combinaison de
          valeurs (par ex. : <q>FG</q> pour <q>au fond à gauche de la scène</q>) et peut aussi
          nécessiter d'encoder de façon plus précise la vitesse, la direction, etc. La documentation
          complète de toute règle de codage doit être fournie dans l'en-tête TEI.</p>
      </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="move-attr.where-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 演出情報をもっと記述するには、これらの値の組み合わせ(例えば、 上手上段を示す<q>UL</q>)や、早さや方向など、より詳細な符号化が必
          要となるだろう。符号化システムに関する詳細な記録は、ヘダー内で示 されるべきである。 </p>
      </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-move-egXML-vi">
      <performance xml:id="perf1">
        <p>First performance</p>
        <castList>
          <castItem>
            <role xml:id="bellaf">Bellafront</role>
          </castItem>
          <!-- ... -->
        </castList>
      </performance>
      <!-- ... -->
      <stage type="entrance"><move who="#bellaf" type="enter" where="L" perf="#perf1"/> Enter
        Bellafront mad.</stage>
    </egXML>
  </exemplum>
```

^b37

### Block 38

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-move-egXML-vd" source="#fr-ex-Shakes-Richard-III">
      <performance xml:id="fr_perf1">
        <p>Première apparition</p>
        <castList>
          <castItem>
            <role xml:id="fr_clar">Clarence</role>
          </castItem>
        </castList>
      </performance>
      <stage type="entrance"><move who="#fr_clar" type="enter" perf="#perf1"/>(Entre Clarence,
          entouré de gardes).</stage>
    </egXML>
  </exemplum>
```

^b38

### Block 39

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-move-egXML-jc">
      <performance xml:id="zh-tw_perf1">
        <p>第一場戲</p>
        <castList>
          <castItem>
            <role xml:id="zh-tw_bellaf">楊四郎</role>
          </castItem>
          <!-- 其他角色 -->
        </castList>
      </performance>
      <!-- ... -->
      <stage type="entrance"><move who="#zh-tw_bellaf" type="enter" where="L" perf="#perf1"/>
        進場：楊四郎，鬱悶思鄉。</stage>
    </egXML>
  </exemplum>
```

^b39

### Block 40

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRSTA" type="div3"/>
  </listRef>
```

^b40

