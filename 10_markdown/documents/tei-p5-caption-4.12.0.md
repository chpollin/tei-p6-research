---
type: representation
source-type: document
source: '[[00_sources/tei-p5-caption-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 caption
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/caption.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# caption

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4617. Git blob: `16c04b79f15da4d5a4842ace4b7c6e31bf3be8bb`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-caption" ident="caption">
  <gloss versionDate="2007-06-12" xml:lang="en">caption</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">sous-titre</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Beschriftung</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the text of a caption or other text displayed as part of
a film script or screenplay.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">영화 스크립트 또는 시나리오의 일부로서 제시되는 자막 또는 다른 텍스트를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含呈現在對白本或電影視劇本中的字幕或其他文字。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene el texto de un encabezamiento u otro texto dispuesto como parte de una obra o de un guión de película.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">見出しや脚本のテキストを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">texte d'une légende ou tout autre texte affiché,
      qui fait partie du script ou du scénario</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il testo di una leggenda o altro testo facente parte di un copione o di una sceneggiatura.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.stageLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caption-egXML-ta" source="#Python">
      <camera>Zoom in to overlay showing some stock film of hansom cabs
galloping past</camera>       <caption>London, 1895.</caption>
      <caption>The residence of Mr Oscar Wilde.</caption>
      <sound>Suitably classy music starts.</sound>
      <view>Mix through to Wilde's drawing room. A crowd of suitably
dressed folk are engaged in typically brilliant conversation,
laughing affectedly and drinking champagne.</view>
      <sp>
        <speaker>Prince of Wales</speaker>
        <p>My congratulations, Wilde. Your latest play is a great success.
</p>
      </sp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caption-egXML-yw" source="#fr-ex-Polac">
      <view><camera>Plongée générale de la cage d'escalier (en colimaçon)</camera>. Deux lycéens,
          Eric et Serge, âgés de 16 ans, en manteaux noirs, montent. <camera>En surimpression sur
            cette image, passent successivement trois cartons de générique</camera>
            <note place="foot"> Le générique complet se déroule à la fin du film</note>. <sound>Reprise de
            la musique leitmotiv. Coup de sonnette.</sound>
            <caption> 1er carton : UN FILS UNIQUE</caption>
            <caption>2e carton : UN FILM de MICHEL POLAC</caption>
            <caption> 3e carton : IMAGES ERIC DALMAT</caption>
        </view>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caption-egXML-au">
      <camera>鏡頭拉近，畫面上雙蓋馬車奔馳而去。</camera>
      <caption>1895年，倫敦。</caption>
      <caption>王爾德先生的家</caption>
      <sound>開始合宜別緻的音樂。</sound>
      <view>畫面融接到王爾德的畫室。一群人衣冠楚楚、 高談闊論，有人手拿香檳，有人開懷大笑。</view>
      <sp>
        <speaker>威爾斯王子</speaker>
        <p>恭喜你，王爾德。你最近的戲劇是個大成功。</p>
      </sp>
    </egXML>
  </exemplum>
  <remarks ident="caption-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A specialized form of stage direction.</p>
  </remarks>
  <remarks ident="caption-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Forme particulière d'indication scénique.</p>
  </remarks>
  <remarks ident="caption-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>ト書きの特別な形。</p>
  </remarks>
  <listRef>
    <ptr target="#DRTEC" type="div3"/>
    <ptr target="#DROTH" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">caption</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">sous-titre</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Beschriftung</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the text of a caption or other text displayed as part of
a film script or screenplay.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">영화 스크립트 또는 시나리오의 일부로서 제시되는 자막 또는 다른 텍스트를 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含呈現在對白本或電影視劇本中的字幕或其他文字。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene el texto de un encabezamiento u otro texto dispuesto como parte de una obra o de un guión de película.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">見出しや脚本のテキストを示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">texte d'une légende ou tout autre texte affiché,
      qui fait partie du script ou du scénario</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il testo di una leggenda o altro testo facente parte di un copione o di una sceneggiatura.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.stageLike"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caption-egXML-ta" source="#Python">
      <camera>Zoom in to overlay showing some stock film of hansom cabs
galloping past</camera>       <caption>London, 1895.</caption>
      <caption>The residence of Mr Oscar Wilde.</caption>
      <sound>Suitably classy music starts.</sound>
      <view>Mix through to Wilde's drawing room. A crowd of suitably
dressed folk are engaged in typically brilliant conversation,
laughing affectedly and drinking champagne.</view>
      <sp>
        <speaker>Prince of Wales</speaker>
        <p>My congratulations, Wilde. Your latest play is a great success.
</p>
      </sp>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caption-egXML-yw" source="#fr-ex-Polac">
      <view><camera>Plongée générale de la cage d'escalier (en colimaçon)</camera>. Deux lycéens,
          Eric et Serge, âgés de 16 ans, en manteaux noirs, montent. <camera>En surimpression sur
            cette image, passent successivement trois cartons de générique</camera>
            <note place="foot"> Le générique complet se déroule à la fin du film</note>. <sound>Reprise de
            la musique leitmotiv. Coup de sonnette.</sound>
            <caption> 1er carton : UN FILS UNIQUE</caption>
            <caption>2e carton : UN FILM de MICHEL POLAC</caption>
            <caption> 3e carton : IMAGES ERIC DALMAT</caption>
        </view>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-caption-egXML-au">
      <camera>鏡頭拉近，畫面上雙蓋馬車奔馳而去。</camera>
      <caption>1895年，倫敦。</caption>
      <caption>王爾德先生的家</caption>
      <sound>開始合宜別緻的音樂。</sound>
      <view>畫面融接到王爾德的畫室。一群人衣冠楚楚、 高談闊論，有人手拿香檳，有人開懷大笑。</view>
      <sp>
        <speaker>威爾斯王子</speaker>
        <p>恭喜你，王爾德。你最近的戲劇是個大成功。</p>
      </sp>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="caption-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A specialized form of stage direction.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="caption-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Forme particulière d'indication scénique.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="caption-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>ト書きの特別な形。</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRTEC" type="div3"/>
    <ptr target="#DROTH" type="div3"/>
  </listRef>
```

^b19

