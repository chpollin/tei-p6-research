---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sound-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sound
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sound.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sound

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7834. Git blob: `fe7ac0e6856af88b581536c3f4cabeab875c1260`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-sound" ident="sound">
  <gloss versionDate="2007-06-12" xml:lang="en">sound</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">son</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes a sound effect or musical sequence specified within a screen play or radio script.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">시나리오 또는 라디오 스크립트에서 지정된 효과음 또는 음악을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述電影或廣播劇本中的音效或配樂。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">describe un efecto sonoro o una secuencia musical
    especificada dentro de una obra teatral o de un programa radiofónico.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">音響効果、すなわち脚本や台本で指定されている一連の音を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit un effet sonore ou un morceau de musique indiqué
    dans un scénario pour le cinéma ou la radio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive un effetto sonoro o una sequenza musicale
    descritti in una sceneggiatura o di un copione radiofonico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">categorizes the sound in some respect, e.g. as music, special effect, etc.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">어떤 측면에서 음향을 분류한다. 예, 음악, 특수 효과음 등.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">將聲音從某方面來分類，例如音樂，特殊音效等。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">categoriza el sonido en algún aspecto, p.ej. como
        música, efecto especial, etc.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該音を分類する。例えば、音楽、特殊効果など。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">caractérise le son, par exemple : musique, effets
        spéciaux, etc.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica il tipo di suono, ad esempio musica,
        effetto speciale, ecc.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
    <attDef ident="discrete" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether the sound overlaps the surrounding speeches or interrupts them.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">음향이 주변 대사와 겹치거나 이를 방해하는지를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該聲音是否和週遭說話聲音重疊或單獨穿插於其間。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">indica si el sonido solapa los discursos circundantes
        o los interrumpe.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該音が周囲の発話にかぶっているか、または会話を遮っているかを示 す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si le son couvre les dialogues ou les
        interrompt.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se il suono si accavalla con le battute o se
        le interrompe</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <remarks ident="sound-attr.discrete-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the sound is heard between the surrounding
          speeches; the value <val>false</val> indicates that the sound overlaps one or more of the
          surrounding speeches.</p>
      </remarks>
      <remarks ident="sound-attr.discrete-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que le son est entendu entre les dialogues ; la valeur
            <val>false</val> indique que le son se superpose à un ou à plusieurs de ces
        dialogues.</p>
      </remarks>
      <remarks ident="sound-attr.discrete-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、当該音が会話の合間に聞こえることを示 す。属性値<val>false</val>は、当該音が、周囲の会話中にも聞こえ ていることを示す。
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sound-egXML-xh" source="#DROTH-eg-57">
      <sp>
        <speaker>Benjy</speaker>
        <p>Now to business.</p>
      </sp>
      <sp>
        <speaker>Ford and Zaphod</speaker>
        <p>To business.</p>
      </sp>
      <sound discrete="true">Glasses clink.</sound>
      <sp>
        <speaker>Benjy</speaker>
        <p>I beg your pardon?</p>
      </sp>
      <sp>
        <speaker>Ford</speaker>
        <p>I'm sorry, I thought you were proposing a toast.</p>
      </sp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sound-egXML-de">
      <view><camera> Plan américain</camera> serré de Zazie, en chemise de nuit, dans les vécés,
          tout carrelés de clair. Au vasistas, passe un rayon de soleil matinal. Zazie réfléchit et
          colle son oreille sur la cloison. La maison est tellement silencieuse qu'elle doit se
          demander si elle va tirer la chasse d'eau ou non. Elle sourit et imagine qu'elle entend le
          bruit de métro <sound>(bruit off)</sound>, puis, suivie en court
          <camera>panoramique</camera>, elle va tirer la chasse d'eau. <sound>Bruit de démarrage
            d'une automobile, grincement de changement de vitesse</sound>. [Etonnée, Zazie
          recommence. Cette fois,<sound> bruit du chariot d'une machine à écrire</sound> qui revient
          à la ligne. Encore une fois : <sound>sirène de brume</sound>]. Ecœurée ou déçue, Zazie
          sort des vécés. </view>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sound-egXML-fo">
      <sp>
        <speaker>班吉</speaker>
        <p>現在，說到我們的事業。</p>
      </sp>
      <sp>
        <speaker>福特和薩豐</speaker>
        <p>敬我們的事業。</p>
      </sp>
      <sound discrete="true">玻璃杯敲擊聲</sound>
      <sp>
        <speaker>班吉</speaker>
        <p>抱歉，您說什麼？</p>
      </sp>
      <sp>
        <speaker>福特</speaker>
        <p>不好意思，我以為你說乾杯。</p>
      </sp>
    </egXML>
  </exemplum>
  <remarks ident="sound-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A specialized form of stage direction.</p>
  </remarks>
  <remarks ident="sound-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Une forme particulière d'indication scénique.</p>
  </remarks>
  <remarks ident="sound-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> ト書きにある専門形。 </p>
  </remarks>
  <listRef>
    <ptr target="#DRTEC"/>
    <ptr target="#DROTH"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">sound</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">son</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes a sound effect or musical sequence specified within a screen play or radio script.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시나리오 또는 라디오 스크립트에서 지정된 효과음 또는 음악을 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述電影或廣播劇本中的音效或配樂。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">describe un efecto sonoro o una secuencia musical
    especificada dentro de una obra teatral o de un programa radiofónico.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">音響効果、すなわち脚本や台本で指定されている一連の音を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit un effet sonore ou un morceau de musique indiqué
    dans un scénario pour le cinéma ou la radio.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive un effetto sonoro o una sequenza musicale
    descritti in una sceneggiatura o di un copione radiofonico.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.stageLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">categorizes the sound in some respect, e.g. as music, special effect, etc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 측면에서 음향을 분류한다. 예, 음악, 특수 효과음 등.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">將聲音從某方面來分類，例如音樂，特殊音效等。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">categoriza el sonido en algún aspecto, p.ej. como
        música, efecto especial, etc.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該音を分類する。例えば、音楽、特殊効果など。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">caractérise le son, par exemple : musique, effets
        spéciaux, etc.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica il tipo di suono, ad esempio musica,
        effetto speciale, ecc.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether the sound overlaps the surrounding speeches or interrupts them.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">음향이 주변 대사와 겹치거나 이를 방해하는지를 표시한다.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該聲音是否和週遭說話聲音重疊或單獨穿插於其間。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">indica si el sonido solapa los discursos circundantes
        o los interrumpe.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該音が周囲の発話にかぶっているか、または会話を遮っているかを示 す。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si le son couvre les dialogues ou les
        interrompt.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se il suono si accavalla con le battute o se
        le interrompe</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="sound-attr.discrete-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the sound is heard between the surrounding
          speeches; the value <val>false</val> indicates that the sound overlaps one or more of the
          surrounding speeches.</p>
      </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="sound-attr.discrete-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que le son est entendu entre les dialogues ; la valeur
            <val>false</val> indique que le son se superpose à un ou à plusieurs de ces
        dialogues.</p>
      </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="sound-attr.discrete-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、当該音が会話の合間に聞こえることを示 す。属性値<val>false</val>は、当該音が、周囲の会話中にも聞こえ ていることを示す。
        </p>
      </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sound-egXML-xh" source="#DROTH-eg-57">
      <sp>
        <speaker>Benjy</speaker>
        <p>Now to business.</p>
      </sp>
      <sp>
        <speaker>Ford and Zaphod</speaker>
        <p>To business.</p>
      </sp>
      <sound discrete="true">Glasses clink.</sound>
      <sp>
        <speaker>Benjy</speaker>
        <p>I beg your pardon?</p>
      </sp>
      <sp>
        <speaker>Ford</speaker>
        <p>I'm sorry, I thought you were proposing a toast.</p>
      </sp>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sound-egXML-de">
      <view><camera> Plan américain</camera> serré de Zazie, en chemise de nuit, dans les vécés,
          tout carrelés de clair. Au vasistas, passe un rayon de soleil matinal. Zazie réfléchit et
          colle son oreille sur la cloison. La maison est tellement silencieuse qu'elle doit se
          demander si elle va tirer la chasse d'eau ou non. Elle sourit et imagine qu'elle entend le
          bruit de métro <sound>(bruit off)</sound>, puis, suivie en court
          <camera>panoramique</camera>, elle va tirer la chasse d'eau. <sound>Bruit de démarrage
            d'une automobile, grincement de changement de vitesse</sound>. [Etonnée, Zazie
          recommence. Cette fois,<sound> bruit du chariot d'une machine à écrire</sound> qui revient
          à la ligne. Encore une fois : <sound>sirène de brume</sound>]. Ecœurée ou déçue, Zazie
          sort des vécés. </view>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sound-egXML-fo">
      <sp>
        <speaker>班吉</speaker>
        <p>現在，說到我們的事業。</p>
      </sp>
      <sp>
        <speaker>福特和薩豐</speaker>
        <p>敬我們的事業。</p>
      </sp>
      <sound discrete="true">玻璃杯敲擊聲</sound>
      <sp>
        <speaker>班吉</speaker>
        <p>抱歉，您說什麼？</p>
      </sp>
      <sp>
        <speaker>福特</speaker>
        <p>不好意思，我以為你說乾杯。</p>
      </sp>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="sound-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A specialized form of stage direction.</p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="sound-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Une forme particulière d'indication scénique.</p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="sound-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> ト書きにある専門形。 </p>
  </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRTEC"/>
    <ptr target="#DROTH"/>
  </listRef>
```

^b37

