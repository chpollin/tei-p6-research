---
type: representation
source-type: document
source: '[[00_sources/tei-p5-view-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 view
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/view.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# view

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6479. Git blob: `1bac768162e1fff61388465257a0a749bb5136e1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-view" ident="view">
  <gloss versionDate="2007-06-12" xml:lang="en">view</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">vue</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the visual context of some part of a screen play in
terms of what the spectator sees, generally independent of any
dialogue.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일반적으로 어떤 대화와도 무관하게 관객의 관점에서 시나리오의 일부인 시각적 맥락을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">劇本中描述觀眾所看到的景象，一般不包含任何對話內容。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">describe el contexto visual de una cierta parte del escenario en los términos en los que el espectador lo percibe, generalmente independientemente de cualquier diálogo.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">脚本中における視覚状況の部分を示す。観客が見る部分で、一般には、台詞
  から独立してある。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit le contexte visuel d'une partie d'un scénario
      selon la vision du spectateur, généralement indépendamment de tout dialogue.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive il contenuto visivo di una parte della sceneggiatura, rispetto a ciò che lo spettatore vede, di solito indipendentemente dai dialoghi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.stageLike"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-fc">
      <view><name>Max</name> joins his daughter
at the window. <hi>Rain</hi> sprays his
        face-- </view>
      <view><camera>Max's POV</camera> He sees occasional
windows open, and just across from his apartment
house, a <hi>man</hi> opens the front door of
        a brownstone--</view>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-lk" source="#fr-ex-Mouchette">
      <view>
        <p><camera>Plan d'ensemble</camera> des fillettes qui regardent Mouchette. <camera>Plan
              rapproché</camera> de la main de l'institutrice pianotant nerveusement.<camera>
            Retour</camera> sur les fillettes qui ricanent. Mouchette, face à nous, ne peut retenir
            ses larmes. N'y tenant plus, elle prend son visage dans ses mains et hoquète de
            sanglots. <camera>Fondu enchaîné.</camera>
            </p>
      </view>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-uq" source="#fr-ex-Lichtig">
      <div type="plan">
        <view> Préfecture - bureau fonctionnaire - intérieur jour <camera>Plan américain</camera>
            d'un fonctionnaire assis derrière un bureau (il est vu de profil), consultant un fichier
            dans une boîte ouverte devant lui. Il sort une fiche et lève la tête. C'est un homme
            d'une quarantaine d'années, un aspect solide, concret, et un air relativement bon
            enfant. Dans son regard, pourtant, on voit passer par moments une lueur froide,
            inquiétante. </view>
        <sp>
          <speaker>FONCTIONNAIRE</speaker>
          <p>Robert Klein, vous avez dit ?</p>
        </sp>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-xu">
      <view><name>馬克思</name>隨他女兒到窗邊。<hi>雨水</hi> 打在他臉上-- </view>
      <view><camera>馬克思的視點</camera> 他看見一些打開的窗戶，而就在他公寓對面，有一個<hi>男子</hi> 正打開富麗堂皇的大門。--</view>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-jw">
      <div type="shot">
        <view>香港鳳凰衛視台</view>
        <sp>
          <speaker>旁白</speaker>
          <p>2008北京奧運的聖火稍後即將傳遞到香港九龍，我們有最新的現場實況直播於您。</p>
        </sp>
      </div>
      <div type="shot">
        <view>香港九龍街道。四處是圍觀的群眾。記者站在聖火傳遞路線旁。</view>
        <sp>
          <speaker>主持人</speaker>
          <p>大家好，我現在在香港的九龍。 </p>
        </sp>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-lc" source="#Python">
      <div type="shot">
        <view>BBC World symbol</view>
        <sp>
          <speaker>Voice Over</speaker>
          <p>Monty Python's Flying Circus tonight comes to you live
  from the Grillomat Snack Bar, Paignton.</p>
        </sp>
      </div>
      <div type="shot">
        <view>Interior of a nasty snack bar. Customers around, preferably
  real people. Linkman sitting at one of the plastic tables.</view>
        <sp>
          <speaker>Linkman</speaker>
          <p>Hello to you live from the Grillomat Snack Bar.
</p>
        </sp>
      </div>
    </egXML>
  </exemplum>
  <remarks ident="view-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A view is a particular form of stage direction.</p>
  </remarks>
  <remarks ident="view-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un élément <gi>view</gi> peut être considéré comme une forme particulière
                d'indication scénique.</p>
  </remarks>
  <remarks ident="view-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、ト書きにある独特の形式である。
    </p>
  </remarks>
  <listRef>
    <ptr target="#DRTEC"/>
    <ptr target="#DROTH" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">view</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">vue</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the visual context of some part of a screen play in
terms of what the spectator sees, generally independent of any
dialogue.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일반적으로 어떤 대화와도 무관하게 관객의 관점에서 시나리오의 일부인 시각적 맥락을 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">劇本中描述觀眾所看到的景象，一般不包含任何對話內容。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">describe el contexto visual de una cierta parte del escenario en los términos en los que el espectador lo percibe, generalmente independientemente de cualquier diálogo.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">脚本中における視覚状況の部分を示す。観客が見る部分で、一般には、台詞
  から独立してある。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit le contexte visuel d'une partie d'un scénario
      selon la vision du spectateur, généralement indépendamment de tout dialogue.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il contenuto visivo di una parte della sceneggiatura, rispetto a ciò che lo spettatore vede, di solito indipendentemente dai dialoghi.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.stageLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-fc">
      <view><name>Max</name> joins his daughter
at the window. <hi>Rain</hi> sprays his
        face-- </view>
      <view><camera>Max's POV</camera> He sees occasional
windows open, and just across from his apartment
house, a <hi>man</hi> opens the front door of
        a brownstone--</view>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-lk" source="#fr-ex-Mouchette">
      <view>
        <p><camera>Plan d'ensemble</camera> des fillettes qui regardent Mouchette. <camera>Plan
              rapproché</camera> de la main de l'institutrice pianotant nerveusement.<camera>
            Retour</camera> sur les fillettes qui ricanent. Mouchette, face à nous, ne peut retenir
            ses larmes. N'y tenant plus, elle prend son visage dans ses mains et hoquète de
            sanglots. <camera>Fondu enchaîné.</camera>
            </p>
      </view>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-uq" source="#fr-ex-Lichtig">
      <div type="plan">
        <view> Préfecture - bureau fonctionnaire - intérieur jour <camera>Plan américain</camera>
            d'un fonctionnaire assis derrière un bureau (il est vu de profil), consultant un fichier
            dans une boîte ouverte devant lui. Il sort une fiche et lève la tête. C'est un homme
            d'une quarantaine d'années, un aspect solide, concret, et un air relativement bon
            enfant. Dans son regard, pourtant, on voit passer par moments une lueur froide,
            inquiétante. </view>
        <sp>
          <speaker>FONCTIONNAIRE</speaker>
          <p>Robert Klein, vous avez dit ?</p>
        </sp>
      </div>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-xu">
      <view><name>馬克思</name>隨他女兒到窗邊。<hi>雨水</hi> 打在他臉上-- </view>
      <view><camera>馬克思的視點</camera> 他看見一些打開的窗戶，而就在他公寓對面，有一個<hi>男子</hi> 正打開富麗堂皇的大門。--</view>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-jw">
      <div type="shot">
        <view>香港鳳凰衛視台</view>
        <sp>
          <speaker>旁白</speaker>
          <p>2008北京奧運的聖火稍後即將傳遞到香港九龍，我們有最新的現場實況直播於您。</p>
        </sp>
      </div>
      <div type="shot">
        <view>香港九龍街道。四處是圍觀的群眾。記者站在聖火傳遞路線旁。</view>
        <sp>
          <speaker>主持人</speaker>
          <p>大家好，我現在在香港的九龍。 </p>
        </sp>
      </div>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-view-egXML-lc" source="#Python">
      <div type="shot">
        <view>BBC World symbol</view>
        <sp>
          <speaker>Voice Over</speaker>
          <p>Monty Python's Flying Circus tonight comes to you live
  from the Grillomat Snack Bar, Paignton.</p>
        </sp>
      </div>
      <div type="shot">
        <view>Interior of a nasty snack bar. Customers around, preferably
  real people. Linkman sitting at one of the plastic tables.</view>
        <sp>
          <speaker>Linkman</speaker>
          <p>Hello to you live from the Grillomat Snack Bar.
</p>
        </sp>
      </div>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="view-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A view is a particular form of stage direction.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="view-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un élément <gi>view</gi> peut être considéré comme une forme particulière
                d'indication scénique.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="view-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、ト書きにある独特の形式である。
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRTEC"/>
    <ptr target="#DROTH" type="div3"/>
  </listRef>
```

^b21

