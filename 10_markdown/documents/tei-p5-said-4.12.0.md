---
type: representation
source-type: document
source: '[[00_sources/tei-p5-said-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 said
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/said.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# said

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 13466. Git blob: `3a59fdd71d9308c77fc81a0d6c91010227147b27`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-said" ident="said">
  <gloss versionDate="2007-07-18" xml:lang="en">speech or thought</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">대화 또는 사고</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">parlamento, discurso o pensamiento</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">Parole ou pensée.</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">parlato o pensiero</gloss>
  <desc versionDate="2007-09-30" xml:lang="en">indicates passages thought or spoken aloud, whether explicitly indicated in the source or
    not, whether directly or indirectly reported, whether by real people or fictional characters.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원본에 명시적으로 표시되었든지 않았든지, 직접적으로 또는 간접적으로 보고되었든지 않았든지, 그리고 실제
    인물 또는 가공의 인물에 의해 생성되었는지 간에, 생각 혹은 소리 내어 말한 단락을 표시한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">indica los pasajes pensados o hablados en voz alta, si
    está indicado explícitamente en la fuente o no, si señalado directamente o indirectamente, sean
    de gente real o de personajes ficticios.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">考えたり声に出されたりした一節を示す。元資料中に明示されているかどう
    か、間接的な伝聞かどうか、実在の人物に依るものかどうか、などは問わな い。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">indique que les passages sont pensés ou qu'ils sont
    prononcés à haute voix, que cela soit indiqué explicitement ou non dans la source , que ces
    passages soient directement ou indirectement rapportés par des personnages réels ou fictifs.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">indica brani pensati o pronunciati, siano essi
    esplicitamente indicati nella fonte o meno, in discorso diretto o indiretto e attribuibili a
    persone realmente esistenti o personaggi di fantasia</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.attributable"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <attList>
    <attDef ident="aloud" usage="opt">
      <desc versionDate="2007-07-18" xml:lang="en">may be used to indicate whether the quoted matter is regarded as having been vocalized
        or signed.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">인용부가 발화된 것으로 또는 신호된 것으로 볼 수 있는지를 표시할 때 사용할 수 있다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">puede ser utilizado para indicar si el material
        marcado ha sido verbalizado o firmado.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">引用内容が言語または記号化されているかどうかを示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">peut être utilisé pour indiquer si l'on estime que
        l'objet cité est dit oralement ou par signes.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">può essere utilizzato per indicare se la citazione in
        questione è stata pronunciata o firmata</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-qx" xml:lang="en" source="#COHQQ-eg-28">
          <p>
            Celia thought privately, <said aloud="false">Dorothea quite despises Sir James Chettam; 
            I believe she would not accept him.</said> Celia felt that this was a pity. 
            <!-- ... -->
          </p>
        </egXML>
      </exemplum>
      <remarks ident="said-attr.aloud-remarks" versionDate="2007-07-18" xml:lang="en">
        <p>The value <val>true</val> indicates the encoded passage was expressed outwardly (whether
          spoken, signed, sung, screamed, chanted, etc.); the value <val>false</val> indicates that
          the encoded passage was thought, but not outwardly expressed.</p>
      </remarks>
      <remarks ident="said-attr.aloud-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que le passage encodé a été prononcé de manière
          explicite (qu'il ait été dit, exprimé par geste, chanté, crié, déclamé etc.) ; la valeur
            <val>false</val> indique que le passage encodé a été pensé, mais pas prononcé.</p>
      </remarks>
      <remarks ident="said-attr.aloud-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El valor <val>verdad</val> indica que el pasaje codificado fue expresado exteriormente
          (si fue hablado, cantado, gritado, etc.); el valor <val>falso</val> indica que el pasaje
          codificado era un pensamiento, pero no expresado exteriormente.</p>
      </remarks>
      <remarks ident="said-attr.aloud-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、符号化されている一節が、外見上(発話、記号、 歌、叫び、詠唱など)表現されていることを示す。属性値
          <val>false</val>は、符号化されている一節が、考えられてはいるが、 外見上は表現されていないことを示す。 </p>
      </remarks>
    </attDef>
    <attDef ident="direct" usage="opt">
      <desc versionDate="2007-07-18" xml:lang="en">may be used to indicate whether the quoted matter is regarded as direct or indirect
        speech.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">인용부가 직접 대화로 또는 간접 대화로 간주할 수 있는지를 표시할 때 사용할 수 있다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">puede ser utilizado para indicar si el material
        marcado está considerado como discurso directo o indirecto.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">引用内容が、直接または間接的な話(法)かどうかを示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">peut être utilisé pour indiquer si le sujet cité est
        à considérer comme comme étant du discours direct ou du discours indirect.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">può essere utilizzato per indicare se la citazione in
        questione è considerata come discorso diretto o indiretto</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <defaultVal>true</defaultVal>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-zc" xml:lang="en" source="#SAID-DIRECT-eg-1">
          <!-- in the header -->
          <editorialDecl>
            <quotation marks="none"/>
          </editorialDecl>
          <!-- ... -->
          <p>Tantripp had brought a card, and said that <said direct="false">there was a gentleman waiting in the lobby</said>. 
            The courier had told him that <said direct="false">only Mrs. Casaubon was at home</said>, 
            but he said <said direct="false">he was a relation of Mr. Casaubon's: would she see him?</said> 
               </p>
        </egXML>
      </exemplum>
      <remarks ident="said-attr.direct-remarks" versionDate="2007-07-18" xml:lang="en">
        <p>The value <val>true</val> indicates the speech or thought is represented directly; the
          value <val>false</val> that speech or thought is represented indirectly, e.g. by use of a
          marked verbal aspect.</p>
      </remarks>
      <remarks ident="said-attr.direct-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que la parole ou la pensée est représentée directement
          ; la valeur <val>false</val>,  qu'elle est représentée indirectement , par exemple marquée
          par une forme verbale.</p>
      </remarks>
      <remarks ident="said-attr.direct-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El valor <val>verdad</val> indica que el discurso o el pensamiento está representado
          directamente; el valor <val>falso</val> que el discurso o el pensamiento está representado
          indirectamente, p.ej. por medio de un aspecto verbal marcado.</p>
      </remarks>
      <remarks ident="said-attr.direct-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、話や考えは、直接的に示されていることを示 す。属性値<val>false</val>は、話や考えは、間接的に示されていること
          示す。例えば、動詞アスペクト指標により示されている。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-sw" source="#COHQQ-eg-34">
      <!-- in the header -->
      <editorialDecl>
        <quotation marks="all"/>
      </editorialDecl>
      <!-- ... -->
      <p><said>"Our minstrel here will warm the old man's heart with song, dazzle him with jewels and
          gold"</said>, a troublemaker simpered. <said>"He'll trample on the Duke's camellias, spill
          his wine, and blunt his sword, and say his name begins with X, and in the end the Duke
          will say, <said>'Take Saralinda, with my blessing, O lordly Prince of Rags and Tags, O
            rider of the sun!'</said>"</said></p>
    </egXML>
    <!-- Thurber: The 13 Clocks, near end of chapter I -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-eb" source="#fr-ex-Flaubert_Sal">
      <p>Ils l'entendaient murmurer : <said> Morts ! Tous morts ! Vous ne viendrez plus obéissant
            à ma voix, quand, assise sur le bord du lac, je vous jetais dans la gueule des pépins de
            pastèques ! Le mystère de Tanit roulait au fond de vos yeux, plus limpides que les
            globules des fleuves.</said> Et elle les appelait par leurs noms, qui étaient les noms
          des mois.<said>Siv ! Sivan ! Tammouz, Eloul, Tischri, Schebar ! Ah ! pitié pour moi,
            Déesse ! </said>
        </p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-cy" source="#fr-ex-Balzac_Vie">
      <p><said aloud="true" rend="pre(“) post(”)">On veut donc plaire à sa petite fille ?...
          </said>, dit Caroline en mettant sa tête sur l'épaule d'Adolphe, qui la baise au front en
          pensant : <said aloud="false">Dieu merci, je la tiens! </said>.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-be" source="#biblzh-tw_n20">
      <p><said>一路下去，慢慢我發覺我和王一生之間，既開始有互相的信任和基於經驗的同情，又有各自的疑問。</said>
            他總是問我與他認識之前是怎麼生活的，尤其是父母死後的兩年是怎麼混的。<said>我大略地告訴他，可他又特別在一些細節上詳細地打聽，主要是關於吃。例如講到有一次我一天沒有吃到東西，他就問：<said>
            「一點兒都沒吃到嗎？」</said>
            </said>
         </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-mm">
      <p><said aloud="true" rend="pre(“) post(”)">嗯，</said>他耳邊傳來小小的聲音說： <said aloud="true" rend="pre(“) post(”)">有點難以決定，非常困難。 很有勇氣、頭腦也不錯、有天份。喔！我的天啊！沒錯— 還有熱切證明自我的渴望，這真的很有趣。…
          我應該把你分發到哪呢？</said>
         </p>
      <p>哈利抓緊分類帽的邊緣想著：<said aloud="false" rend="italic">不要是史來哲林，千萬不要</said>。</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-pl" source="#COHQQ-eg-35">
      <p><said aloud="true" rend="pre(“) post(”)">Hmmm</said>, said a small voice in his ear. 
      <said aloud="true" rend="pre(“) post(”)">Difficult. Very difficult. Plenty of courage, I see.
          Not a bad mind either. there's talent, oh my goodness, yes — and a nice thirst to prove
          yourself, now that's interesting. … So where shall I put you?</said></p>
      <p>Harry gripped the edges of the stool and thought, <said aloud="false" rend="italic">Not
          Slytherin, not Slytherin</said>.</p>
    </egXML>
    <!-- Rowling: Harry Potter and the Sorcerer's Stone,
            chapter 7 "The Sorting Hat"; p. 121 of the first
            Scholastic trade paperback edition -->
  </exemplum>
  <listRef>
    <ptr target="#COHQQ"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-18" xml:lang="en">speech or thought</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">대화 또는 사고</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">parlamento, discurso o pensamiento</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">Parole ou pensée.</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">parlato o pensiero</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-30" xml:lang="en">indicates passages thought or spoken aloud, whether explicitly indicated in the source or
    not, whether directly or indirectly reported, whether by real people or fictional characters.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원본에 명시적으로 표시되었든지 않았든지, 직접적으로 또는 간접적으로 보고되었든지 않았든지, 그리고 실제
    인물 또는 가공의 인물에 의해 생성되었는지 간에, 생각 혹은 소리 내어 말한 단락을 표시한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">indica los pasajes pensados o hablados en voz alta, si
    está indicado explícitamente en la fuente o no, si señalado directamente o indirectamente, sean
    de gente real o de personajes ficticios.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">考えたり声に出されたりした一節を示す。元資料中に明示されているかどう
    か、間接的な伝聞かどうか、実在の人物に依るものかどうか、などは問わな い。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">indique que les passages sont pensés ou qu'ils sont
    prononcés à haute voix, que cela soit indiqué explicitement ou non dans la source , que ces
    passages soient directement ou indirectement rapportés par des personnages réels ou fictifs.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica brani pensati o pronunciati, siano essi
    esplicitamente indicati nella fonte o meno, in discorso diretto o indiretto e attribuibili a
    persone realmente esistenti o personaggi di fantasia</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.attributable"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-07-18" xml:lang="en">may be used to indicate whether the quoted matter is regarded as having been vocalized
        or signed.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인용부가 발화된 것으로 또는 신호된 것으로 볼 수 있는지를 표시할 때 사용할 수 있다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">puede ser utilizado para indicar si el material
        marcado ha sido verbalizado o firmado.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">引用内容が言語または記号化されているかどうかを示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">peut être utilisé pour indiquer si l'on estime que
        l'objet cité est dit oralement ou par signes.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">può essere utilizzato per indicare se la citazione in
        questione è stata pronunciata o firmata</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-qx" xml:lang="en" source="#COHQQ-eg-28">
          <p>
            Celia thought privately, <said aloud="false">Dorothea quite despises Sir James Chettam; 
            I believe she would not accept him.</said> Celia felt that this was a pity. 
            <!-- ... -->
          </p>
        </egXML>
      </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="said-attr.aloud-remarks" versionDate="2007-07-18" xml:lang="en">
        <p>The value <val>true</val> indicates the encoded passage was expressed outwardly (whether
          spoken, signed, sung, screamed, chanted, etc.); the value <val>false</val> indicates that
          the encoded passage was thought, but not outwardly expressed.</p>
      </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="said-attr.aloud-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que le passage encodé a été prononcé de manière
          explicite (qu'il ait été dit, exprimé par geste, chanté, crié, déclamé etc.) ; la valeur
            <val>false</val> indique que le passage encodé a été pensé, mais pas prononcé.</p>
      </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="said-attr.aloud-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El valor <val>verdad</val> indica que el pasaje codificado fue expresado exteriormente
          (si fue hablado, cantado, gritado, etc.); el valor <val>falso</val> indica que el pasaje
          codificado era un pensamiento, pero no expresado exteriormente.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="said-attr.aloud-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、符号化されている一節が、外見上(発話、記号、 歌、叫び、詠唱など)表現されていることを示す。属性値
          <val>false</val>は、符号化されている一節が、考えられてはいるが、 外見上は表現されていないことを示す。 </p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-07-18" xml:lang="en">may be used to indicate whether the quoted matter is regarded as direct or indirect
        speech.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인용부가 직접 대화로 또는 간접 대화로 간주할 수 있는지를 표시할 때 사용할 수 있다.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">puede ser utilizado para indicar si el material
        marcado está considerado como discurso directo o indirecto.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">引用内容が、直接または間接的な話(法)かどうかを示す。</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">peut être utilisé pour indiquer si le sujet cité est
        à considérer comme comme étant du discours direct ou du discours indirect.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">può essere utilizzato per indicare se la citazione in
        questione è considerata come discorso diretto o indiretto</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>true</defaultVal>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-zc" xml:lang="en" source="#SAID-DIRECT-eg-1">
          <!-- in the header -->
          <editorialDecl>
            <quotation marks="none"/>
          </editorialDecl>
          <!-- ... -->
          <p>Tantripp had brought a card, and said that <said direct="false">there was a gentleman waiting in the lobby</said>. 
            The courier had told him that <said direct="false">only Mrs. Casaubon was at home</said>, 
            but he said <said direct="false">he was a relation of Mr. Casaubon's: would she see him?</said> 
               </p>
        </egXML>
      </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="said-attr.direct-remarks" versionDate="2007-07-18" xml:lang="en">
        <p>The value <val>true</val> indicates the speech or thought is represented directly; the
          value <val>false</val> that speech or thought is represented indirectly, e.g. by use of a
          marked verbal aspect.</p>
      </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="said-attr.direct-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que la parole ou la pensée est représentée directement
          ; la valeur <val>false</val>,  qu'elle est représentée indirectement , par exemple marquée
          par une forme verbale.</p>
      </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="said-attr.direct-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El valor <val>verdad</val> indica que el discurso o el pensamiento está representado
          directamente; el valor <val>falso</val> que el discurso o el pensamiento está representado
          indirectamente, p.ej. por medio de un aspecto verbal marcado.</p>
      </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="said-attr.direct-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、話や考えは、直接的に示されていることを示 す。属性値<val>false</val>は、話や考えは、間接的に示されていること
          示す。例えば、動詞アスペクト指標により示されている。 </p>
      </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-sw" source="#COHQQ-eg-34">
      <!-- in the header -->
      <editorialDecl>
        <quotation marks="all"/>
      </editorialDecl>
      <!-- ... -->
      <p><said>"Our minstrel here will warm the old man's heart with song, dazzle him with jewels and
          gold"</said>, a troublemaker simpered. <said>"He'll trample on the Duke's camellias, spill
          his wine, and blunt his sword, and say his name begins with X, and in the end the Duke
          will say, <said>'Take Saralinda, with my blessing, O lordly Prince of Rags and Tags, O
            rider of the sun!'</said>"</said></p>
    </egXML>
    <!-- Thurber: The 13 Clocks, near end of chapter I -->
  </exemplum>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-eb" source="#fr-ex-Flaubert_Sal">
      <p>Ils l'entendaient murmurer : <said> Morts ! Tous morts ! Vous ne viendrez plus obéissant
            à ma voix, quand, assise sur le bord du lac, je vous jetais dans la gueule des pépins de
            pastèques ! Le mystère de Tanit roulait au fond de vos yeux, plus limpides que les
            globules des fleuves.</said> Et elle les appelait par leurs noms, qui étaient les noms
          des mois.<said>Siv ! Sivan ! Tammouz, Eloul, Tischri, Schebar ! Ah ! pitié pour moi,
            Déesse ! </said>
        </p>
    </egXML>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-cy" source="#fr-ex-Balzac_Vie">
      <p><said aloud="true" rend="pre(“) post(”)">On veut donc plaire à sa petite fille ?...
          </said>, dit Caroline en mettant sa tête sur l'épaule d'Adolphe, qui la baise au front en
          pensant : <said aloud="false">Dieu merci, je la tiens! </said>.</p>
    </egXML>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-be" source="#biblzh-tw_n20">
      <p><said>一路下去，慢慢我發覺我和王一生之間，既開始有互相的信任和基於經驗的同情，又有各自的疑問。</said>
            他總是問我與他認識之前是怎麼生活的，尤其是父母死後的兩年是怎麼混的。<said>我大略地告訴他，可他又特別在一些細節上詳細地打聽，主要是關於吃。例如講到有一次我一天沒有吃到東西，他就問：<said>
            「一點兒都沒吃到嗎？」</said>
            </said>
         </p>
    </egXML>
  </exemplum>
```

^b42

### Block 43

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-mm">
      <p><said aloud="true" rend="pre(“) post(”)">嗯，</said>他耳邊傳來小小的聲音說： <said aloud="true" rend="pre(“) post(”)">有點難以決定，非常困難。 很有勇氣、頭腦也不錯、有天份。喔！我的天啊！沒錯— 還有熱切證明自我的渴望，這真的很有趣。…
          我應該把你分發到哪呢？</said>
         </p>
      <p>哈利抓緊分類帽的邊緣想著：<said aloud="false" rend="italic">不要是史來哲林，千萬不要</said>。</p>
    </egXML>
  </exemplum>
```

^b43

### Block 44

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-said-egXML-pl" source="#COHQQ-eg-35">
      <p><said aloud="true" rend="pre(“) post(”)">Hmmm</said>, said a small voice in his ear. 
      <said aloud="true" rend="pre(“) post(”)">Difficult. Very difficult. Plenty of courage, I see.
          Not a bad mind either. there's talent, oh my goodness, yes — and a nice thirst to prove
          yourself, now that's interesting. … So where shall I put you?</said></p>
      <p>Harry gripped the edges of the stool and thought, <said aloud="false" rend="italic">Not
          Slytherin, not Slytherin</said>.</p>
    </egXML>
    <!-- Rowling: Harry Potter and the Sorcerer's Stone,
            chapter 7 "The Sorting Hat"; p. 121 of the first
            Scholastic trade paperback edition -->
  </exemplum>
```

^b44

### Block 45

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQQ"/>
  </listRef>
```

^b45

