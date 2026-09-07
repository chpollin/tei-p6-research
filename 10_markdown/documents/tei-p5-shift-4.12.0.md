---
type: representation
source-type: document
source: '[[00_sources/tei-p5-shift-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 shift
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/shift.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# shift

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10823. Git blob: `5967a76d829d5d88bf0e392a519e91e205d9bc56`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="spoken" xml:id="gi-shift" ident="shift">
  <gloss versionDate="2009-04-17" xml:lang="en">shift</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">changement</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks the point at which some paralinguistic feature of a series of
utterances by any one speaker changes.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">한 화자의 일련의 발화의 준언어적 특성이 변화는 시점을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">所標記的位置表示任一說話者在一連串說話中，某些附屬語言特性的改變。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話者による一連の発話(パラ言語)素性が変化する場所を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique le point où une caractéristique
    paralinguistique change dans la série d'énonciations d'un même locuteur.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">señala el punto en que un fenómeno paralingüístico de una serie de enunciados producidos por uno de los hablantes cambia estado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segnala il punto in cui un fenomeno paralinguistico di una serie di enunciati prodotti da uno dei parlanti cambia stato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.global.spoken"/>
  </classes>
  <content><empty/></content>
  <constraintSpec ident="shiftNew" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:shift">
        <sch:assert test="@new" role="warning">              
          The @new attribute should always be supplied; use the special value
          "normal" to indicate that the feature concerned ceases to be
          remarkable at this point.
        </sch:assert>
      </sch:rule>       
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="feature" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">a paralinguistic feature.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">준언어적 자질</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">附屬語言特性</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">発話(パラ言語)素性。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">caractéristique paralinguistique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">enunciado paralingüístico</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fenomeno paralinguistico.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="tempo">
          <desc versionDate="2007-06-27" xml:lang="en">speed of utterance.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">발화 속도</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">說話速度</desc>
          <desc versionDate="2008-04-06" xml:lang="es">velocidad de elocución.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">発話の速さ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">vitesse d'énonciation</desc>
          <desc versionDate="2007-01-21" xml:lang="it">velocità di elocuzione.</desc>
        </valItem>
        <valItem ident="loud">
          <desc versionDate="2007-06-27" xml:lang="en">loudness.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">소리 크기</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">音量</desc>
          <desc versionDate="2008-04-06" xml:lang="es">intensidad.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">大きさ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">volume</desc>
          <desc versionDate="2007-01-21" xml:lang="it">volume.</desc>
        </valItem>
        <valItem ident="pitch">
          <desc versionDate="2007-06-27" xml:lang="en">pitch range.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">음 높이 범위</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">音調範圍</desc>
          <desc versionDate="2008-04-06" xml:lang="es">entonación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">音の高さ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">hauteur de ton</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tono.</desc>
        </valItem>
        <valItem ident="tension">
          <desc versionDate="2007-06-27" xml:lang="en">tension or stress pattern.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">긴장 또는 강세 유형</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">張力或強調模式</desc>
          <desc versionDate="2008-04-06" xml:lang="es">tensión o estrés.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">声の張りやアクセントパタン。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">intensité ou accentuation</desc>
          <desc versionDate="2007-01-21" xml:lang="it">accento.</desc>
        </valItem>
        <valItem ident="rhythm">
          <desc versionDate="2007-06-27" xml:lang="en">rhythmic qualities.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">억양 특성</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">節奏品質</desc>
          <desc versionDate="2008-04-06" xml:lang="es">calidades rítmicas.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">リズム性。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">qualité du rythme</desc>
          <desc versionDate="2007-01-21" xml:lang="it">ritmo.</desc>
        </valItem>
        <valItem ident="voice">
          <desc versionDate="2007-06-27" xml:lang="en">voice quality.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">목소리 특성</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">聲音品質</desc>
          <desc versionDate="2008-04-06" xml:lang="es">calidad de voz.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">声質。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">qualité de voix</desc>
          <desc versionDate="2007-01-21" xml:lang="it">qualità della voce.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="new" usage="rec">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the new state of the paralinguistic feature specified.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">명시된 준언어적 자질의 새로운 상태를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明改變後的附屬語言特性狀況。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">発話(パラ言語)素性の、新しい状態を示す。</desc>
      <desc versionDate="2009-04-17" xml:lang="fr">précise le nouvel état de la caractéristique paralinguistique en question.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el nuevo estado del fenómeno paralingüístico especificado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il nuovo stato del fenomeno paralinguistico specificato.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    <defaultVal>normal</defaultVal>
      <remarks ident="shift-attr.new-remarks" versionDate="2014-08-04" xml:lang="en">
        <p>Some possible values for this attribute are provided in section <ptr target="#TSSAPA"/>. The special value <val>normal</val> should be used to
         indicate that the feature concerned ceases to be remarkable at this point. In earlier versions of these Guidelines, a null value for this attribute was understood to have the same effect: this practice is now deprecated and will be removed at a future release. 
   </p>
      </remarks>
      <remarks ident="shift-attr.new-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si aucune valeur n'est spécifiée, on suppose que le trait concerné cesse
          d'être remarquable. La valeur <q>normal</q> a le même effet.</p>
      </remarks>
      <remarks ident="shift-attr.new-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性値がなければ、当該素性は目立つものではないことを示す。属性
        値<q>normal</q>も同じ意味になる。
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-shift-egXML-wi">
      <u who="#LB"><shift feature="loud" new="f"/>Elizabeth</u>
      <u who="#EB">Yes</u>
      <u who="#LB"><shift feature="loud" new="normal"/>Come and try this 
        <pause/><shift feature="loud" new="ff"/>come on</u>
      <!-- ... -->
      <listPerson type="speakers">
        <person xml:id="LB"/>
        <person xml:id="EB"/>
      </listPerson>
    </egXML>
    <p>The word <q>Elizabeth</q> is spoken loudly, the words <q>Yes</q> and
<q>Come and try this</q> with normal volume, and the words <q>come on</q>
very loudly.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-shift-egXML-zp" source="#fr-ex-Lichtig">
      <u who="#fr_FL"><shift feature="voice" new="f"/>Non ! ... Ne bougez pas. N'allumez pas ! </u>
      <u who="#fr_KL">Florence ?</u>
      <u who="#fr_FL"><shift feature="loud" new="normal"/>Oui, ... n'allumez pas surtout ! <pause/><shift feature="voice" new="ff"/>Ma lettre, ... ça vous ennuie de me la restituer ?</u>
      <listPerson type="speakers">
        <person xml:id="fr_FL"/>
        <person xml:id="fr_KL"/>
      </listPerson>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-shift-egXML-xs">
      <u who="#zh-tw_LB"><shift feature="loud" new="f"/>伊莉莎白</u>
      <u who="#zh-tw_EB">是的</u>
      <u who="#zh-tw_LB"><shift feature="loud" new="normal"/>來把這穿上<pause/>
            <shift feature="loud" new="ff"/>好嘛</u>
      <!-- ... -->
      <listPerson type="speakers">
        <person xml:id="zh-tw_LB"/>
        <person xml:id="zh-tw_EB"/>
      </listPerson>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TSSASH"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="en">shift</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">changement</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks the point at which some paralinguistic feature of a series of
utterances by any one speaker changes.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">한 화자의 일련의 발화의 준언어적 특성이 변화는 시점을 표시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所標記的位置表示任一說話者在一連串說話中，某些附屬語言特性的改變。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話者による一連の発話(パラ言語)素性が変化する場所を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le point où une caractéristique
    paralinguistique change dans la série d'énonciations d'un même locuteur.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala el punto en que un fenómeno paralingüístico de una serie de enunciados producidos por uno de los hablantes cambia estado.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segnala il punto in cui un fenomeno paralinguistico di una serie di enunciati prodotti da uno dei parlanti cambia stato.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.global.spoken"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="shiftNew" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:shift">
        <sch:assert test="@new" role="warning">              
          The @new attribute should always be supplied; use the special value
          "normal" to indicate that the feature concerned ceases to be
          remarkable at this point.
        </sch:assert>
      </sch:rule>       
    </constraint>
  </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">a paralinguistic feature.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">준언어적 자질</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">附屬語言特性</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話(パラ言語)素性。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">caractéristique paralinguistique.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">enunciado paralingüístico</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fenomeno paralinguistico.</desc>
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
<valList type="semi">
        <valItem ident="tempo">
          <desc versionDate="2007-06-27" xml:lang="en">speed of utterance.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">발화 속도</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">說話速度</desc>
          <desc versionDate="2008-04-06" xml:lang="es">velocidad de elocución.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">発話の速さ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">vitesse d'énonciation</desc>
          <desc versionDate="2007-01-21" xml:lang="it">velocità di elocuzione.</desc>
        </valItem>
        <valItem ident="loud">
          <desc versionDate="2007-06-27" xml:lang="en">loudness.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">소리 크기</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">音量</desc>
          <desc versionDate="2008-04-06" xml:lang="es">intensidad.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">大きさ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">volume</desc>
          <desc versionDate="2007-01-21" xml:lang="it">volume.</desc>
        </valItem>
        <valItem ident="pitch">
          <desc versionDate="2007-06-27" xml:lang="en">pitch range.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">음 높이 범위</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">音調範圍</desc>
          <desc versionDate="2008-04-06" xml:lang="es">entonación</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">音の高さ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">hauteur de ton</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tono.</desc>
        </valItem>
        <valItem ident="tension">
          <desc versionDate="2007-06-27" xml:lang="en">tension or stress pattern.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">긴장 또는 강세 유형</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">張力或強調模式</desc>
          <desc versionDate="2008-04-06" xml:lang="es">tensión o estrés.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">声の張りやアクセントパタン。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">intensité ou accentuation</desc>
          <desc versionDate="2007-01-21" xml:lang="it">accento.</desc>
        </valItem>
        <valItem ident="rhythm">
          <desc versionDate="2007-06-27" xml:lang="en">rhythmic qualities.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">억양 특성</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">節奏品質</desc>
          <desc versionDate="2008-04-06" xml:lang="es">calidades rítmicas.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">リズム性。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">qualité du rythme</desc>
          <desc versionDate="2007-01-21" xml:lang="it">ritmo.</desc>
        </valItem>
        <valItem ident="voice">
          <desc versionDate="2007-06-27" xml:lang="en">voice quality.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">목소리 특성</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">聲音品質</desc>
          <desc versionDate="2008-04-06" xml:lang="es">calidad de voz.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">声質。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">qualité de voix</desc>
          <desc versionDate="2007-01-21" xml:lang="it">qualità della voce.</desc>
        </valItem>
      </valList>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the new state of the paralinguistic feature specified.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">명시된 준언어적 자질의 새로운 상태를 명시한다.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明改變後的附屬語言特性狀況。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話(パラ言語)素性の、新しい状態を示す。</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">précise le nouvel état de la caractéristique paralinguistique en question.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el nuevo estado del fenómeno paralingüístico especificado.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il nuovo stato del fenomeno paralinguistico specificato.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>normal</defaultVal>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="shift-attr.new-remarks" versionDate="2014-08-04" xml:lang="en">
        <p>Some possible values for this attribute are provided in section <ptr target="#TSSAPA"/>. The special value <val>normal</val> should be used to
         indicate that the feature concerned ceases to be remarkable at this point. In earlier versions of these Guidelines, a null value for this attribute was understood to have the same effect: this practice is now deprecated and will be removed at a future release. 
   </p>
      </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="shift-attr.new-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si aucune valeur n'est spécifiée, on suppose que le trait concerné cesse
          d'être remarquable. La valeur <q>normal</q> a le même effet.</p>
      </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="shift-attr.new-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性値がなければ、当該素性は目立つものではないことを示す。属性
        値<q>normal</q>も同じ意味になる。
        </p>
      </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-shift-egXML-wi">
      <u who="#LB"><shift feature="loud" new="f"/>Elizabeth</u>
      <u who="#EB">Yes</u>
      <u who="#LB"><shift feature="loud" new="normal"/>Come and try this 
        <pause/><shift feature="loud" new="ff"/>come on</u>
      <!-- ... -->
      <listPerson type="speakers">
        <person xml:id="LB"/>
        <person xml:id="EB"/>
      </listPerson>
    </egXML>
    <p>The word <q>Elizabeth</q> is spoken loudly, the words <q>Yes</q> and
<q>Come and try this</q> with normal volume, and the words <q>come on</q>
very loudly.</p>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-shift-egXML-zp" source="#fr-ex-Lichtig">
      <u who="#fr_FL"><shift feature="voice" new="f"/>Non ! ... Ne bougez pas. N'allumez pas ! </u>
      <u who="#fr_KL">Florence ?</u>
      <u who="#fr_FL"><shift feature="loud" new="normal"/>Oui, ... n'allumez pas surtout ! <pause/><shift feature="voice" new="ff"/>Ma lettre, ... ça vous ennuie de me la restituer ?</u>
      <listPerson type="speakers">
        <person xml:id="fr_FL"/>
        <person xml:id="fr_KL"/>
      </listPerson>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-shift-egXML-xs">
      <u who="#zh-tw_LB"><shift feature="loud" new="f"/>伊莉莎白</u>
      <u who="#zh-tw_EB">是的</u>
      <u who="#zh-tw_LB"><shift feature="loud" new="normal"/>來把這穿上<pause/>
            <shift feature="loud" new="ff"/>好嘛</u>
      <!-- ... -->
      <listPerson type="speakers">
        <person xml:id="zh-tw_LB"/>
        <person xml:id="zh-tw_EB"/>
      </listPerson>
    </egXML>
  </exemplum>
```

^b36

### Block 37

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSSASH"/>
  </listRef>
```

^b37

