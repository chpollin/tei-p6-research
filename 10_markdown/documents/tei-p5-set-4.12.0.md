---
type: representation
source-type: document
source: '[[00_sources/tei-p5-set-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 set
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/set.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# set

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8090. Git blob: `60240cd220e820a1fd7a4f6c06766e83fb197b88`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-set" ident="set">
  <gloss versionDate="2007-07-04" xml:lang="en">setting</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">배경</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">determinación</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">contexte</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">scénario</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a description of the setting, time, locale, appearance, etc., of the action of a
    play, typically found in the front matter of a printed performance text (not a stage direction).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">(무대 지시가 아닌) 인쇄된 공연 텍스트의 전반부 자료에서 전형적으로 나타나는 희곡 이야기 전개에서
    배경, 시대, 장소, 상황 등에 관한 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一段演出的場景描述，像是佈景、時間、地點、景象等，這段描述通常出現在劇本中的前頁部分
    (並非舞台動作指示) 。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene la descripción de la configuración, del tiempo,
    de la escena, de la apariencia, etc., de la acción de una obra teatral, situada normalmente en
    el inicio de un texto dramático impreso (no en la dirección de escena).</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">一般には、印刷された舞台テキストの前付にある、芝居の設定、時間、場所、 現れ方などの情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une description du décor, du temps, du lieu, de
    l'ordre d'entrée en scène, etc., de l'action de la pièce, qu'on trouve généralement dans les
    préliminaires d’un texte imprimé d'une pièce de théâtre. (Ce n'est pas une indication scénique).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dell'ambientazione, dell'orario,
    della scena, dell'aspetto, ecc. dell'azione di un'opera teatrale, di solito inserita nel
    peritesto iniziale di una testo per la rappresentazione pubblicato (non nelle direttive di
    scena).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.headLike"/>
          <classRef key="model.global"/>
        </alternate>
      
        <sequence minOccurs="0" maxOccurs="unbounded">
          
            <classRef key="model.common"/>
          
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          
        </sequence>
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-qw" source="#GalswStr">
      <set>
        <p>The action takes place on February 7th between the hours of noon and six in the
          afternoon, close to the Trenartha Tin Plate Works, on the borders of England and Wales,
          where a strike has been in progress throughout the winter.</p>
      </set>
    </egXML>
    <!-- Galsworthy, Strife -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-wa" source="#fr-ex-Angl">
      <set>
        <p>Bel après-midi de printemps en 1899. Madame Claire Roc est assise dans un fauteuil en
            osier et feuillette un magazine [...], on peut entendre des cris joyeux d'enfants. </p>
      </set>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-pf" source="#fr-ex-Cyrano">
      <set>
        <head>Une représentation à l'hôtel de Bourgogne</head>
        <p>La salle de l'Hôtel de Bourgogne, en 1640. Sorte de hangar de jeu de paume aménagé et
            embelli pour des représentations.</p>
        <p>La salle est un carré long ; on la voit en biais, de sorte qu'un de ses côtés forme le
            fond qui part du premier plan, à droite, et va au dernier plan, à gauche, faire angle
            avec la scène qu'on aperçoit en pan coupé.</p>
      </set>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-nx" source="#fr-ex-Cyrano">
      <front>
        <set>
          <list type="gloss">
            <label>TEMPS</label>
            <item>1640</item>
            <label>LIEU</label>
            <item>La salle de l'Hôtel de Bourgogne</item>
          </list>
        </set>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-ss">
      <set>
        <p>故事發生於九月八日正午十二點至三點間，位於台北中正紀念堂附近，有群眾包圍抗議政府的更名政策。</p>
      </set>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-pm">
      <set>
        <head>場景</head>
        <p>在一個秋高氣爽的下午，中正紀念堂前</p>
      </set>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-el">
      <front>
        <!-- <>, <div type="Dedication">, etc. -->
        <set>
          <list type="gloss">
            <label>時間：</label>
            <item>2007</item>
            <label>地點：</label>
            <item>台北市中心</item>
          </list>
        </set>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-vt">
      <set>
        <head>SCENE</head>
        <p>A Sub-Post Office on a late autumn evening</p>
      </set>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-mb">
      <front>
        <!-- <titlePage>, <div type="Dedication">, etc. -->
        <set>
          <list type="gloss">
            <label>TIME</label>
            <item>1907</item>
            <label>PLACE</label>
            <item>East Coast village in England</item>
          </list>
        </set>
      </front>
    </egXML>
  </exemplum>
  <remarks ident="set-remarks" versionDate="2017-06-25" xml:lang="en">
    <p rend="dataDesc">Contains paragraphs or phrase level tags.</p>
    <p>This element should not be used outside the front or back matter; for similar contextual descriptions
      within the body of the text, use the <gi>stage</gi> element.</p>
  </remarks>
  <remarks ident="set-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient des paragraphes ou des éléments de niveau phrase.</p>
    <p>Cet élément ne doit pas être utilisé ailleurs que dans les sections préliminaires. Pour
      encoder des descriptions de même nature dans le corps du texte, on utilise l'élément
      <gi>stage</gi>.</p>
  </remarks>
  <remarks ident="set-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落または句レベルのタグをとる。 </p>
    <p> 当該要素は、前付以外では使わないべきである。テキスト本文にある状況 解説については、要素<gi>stage</gi>を使うべきである。 </p>
  </remarks>
  <listRef>
    <ptr target="#DRFAB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">setting</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">배경</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">determinación</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contexte</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">scénario</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a description of the setting, time, locale, appearance, etc., of the action of a
    play, typically found in the front matter of a printed performance text (not a stage direction).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">(무대 지시가 아닌) 인쇄된 공연 텍스트의 전반부 자료에서 전형적으로 나타나는 희곡 이야기 전개에서
    배경, 시대, 장소, 상황 등에 관한 기술을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一段演出的場景描述，像是佈景、時間、地點、景象等，這段描述通常出現在劇本中的前頁部分
    (並非舞台動作指示) 。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene la descripción de la configuración, del tiempo,
    de la escena, de la apariencia, etc., de la acción de una obra teatral, situada normalmente en
    el inicio de un texto dramático impreso (no en la dirección de escena).</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">一般には、印刷された舞台テキストの前付にある、芝居の設定、時間、場所、 現れ方などの情報を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une description du décor, du temps, du lieu, de
    l'ordre d'entrée en scène, etc., de l'action de la pièce, qu'on trouve généralement dans les
    préliminaires d’un texte imprimé d'une pièce de théâtre. (Ce n'est pas une indication scénique).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dell'ambientazione, dell'orario,
    della scena, dell'aspetto, ecc. dell'azione di un'opera teatrale, di solito inserita nel
    peritesto iniziale di una testo per la rappresentazione pubblicato (non nelle direttive di
    scena).</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.headLike"/>
          <classRef key="model.global"/>
        </alternate>
      
        <sequence minOccurs="0" maxOccurs="unbounded">
          
            <classRef key="model.common"/>
          
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          
        </sequence>
      
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-qw" source="#GalswStr">
      <set>
        <p>The action takes place on February 7th between the hours of noon and six in the
          afternoon, close to the Trenartha Tin Plate Works, on the borders of England and Wales,
          where a strike has been in progress throughout the winter.</p>
      </set>
    </egXML>
    <!-- Galsworthy, Strife -->
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-wa" source="#fr-ex-Angl">
      <set>
        <p>Bel après-midi de printemps en 1899. Madame Claire Roc est assise dans un fauteuil en
            osier et feuillette un magazine [...], on peut entendre des cris joyeux d'enfants. </p>
      </set>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-pf" source="#fr-ex-Cyrano">
      <set>
        <head>Une représentation à l'hôtel de Bourgogne</head>
        <p>La salle de l'Hôtel de Bourgogne, en 1640. Sorte de hangar de jeu de paume aménagé et
            embelli pour des représentations.</p>
        <p>La salle est un carré long ; on la voit en biais, de sorte qu'un de ses côtés forme le
            fond qui part du premier plan, à droite, et va au dernier plan, à gauche, faire angle
            avec la scène qu'on aperçoit en pan coupé.</p>
      </set>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-nx" source="#fr-ex-Cyrano">
      <front>
        <set>
          <list type="gloss">
            <label>TEMPS</label>
            <item>1640</item>
            <label>LIEU</label>
            <item>La salle de l'Hôtel de Bourgogne</item>
          </list>
        </set>
      </front>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-ss">
      <set>
        <p>故事發生於九月八日正午十二點至三點間，位於台北中正紀念堂附近，有群眾包圍抗議政府的更名政策。</p>
      </set>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-pm">
      <set>
        <head>場景</head>
        <p>在一個秋高氣爽的下午，中正紀念堂前</p>
      </set>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-el">
      <front>
        <!-- <>, <div type="Dedication">, etc. -->
        <set>
          <list type="gloss">
            <label>時間：</label>
            <item>2007</item>
            <label>地點：</label>
            <item>台北市中心</item>
          </list>
        </set>
      </front>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-vt">
      <set>
        <head>SCENE</head>
        <p>A Sub-Post Office on a late autumn evening</p>
      </set>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-set-egXML-mb">
      <front>
        <!-- <titlePage>, <div type="Dedication">, etc. -->
        <set>
          <list type="gloss">
            <label>TIME</label>
            <item>1907</item>
            <label>PLACE</label>
            <item>East Coast village in England</item>
          </list>
        </set>
      </front>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="set-remarks" versionDate="2017-06-25" xml:lang="en">
    <p rend="dataDesc">Contains paragraphs or phrase level tags.</p>
    <p>This element should not be used outside the front or back matter; for similar contextual descriptions
      within the body of the text, use the <gi>stage</gi> element.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="set-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient des paragraphes ou des éléments de niveau phrase.</p>
    <p>Cet élément ne doit pas être utilisé ailleurs que dans les sections préliminaires. Pour
      encoder des descriptions de même nature dans le corps du texte, on utilise l'élément
      <gi>stage</gi>.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="set-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落または句レベルのタグをとる。 </p>
    <p> 当該要素は、前付以外では使わないべきである。テキスト本文にある状況 解説については、要素<gi>stage</gi>を使うべきである。 </p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRFAB"/>
  </listRef>
```

^b28

