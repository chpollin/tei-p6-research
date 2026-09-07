---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sic-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sic
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sic.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sic

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7532. Git blob: `3d1db2d341ade7cce97a0c6ff717d06585abc490`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-sic" ident="sic">
  <gloss versionDate="2012-03-15" xml:lang="en">Latin for <mentioned>thus</mentioned> or <mentioned>so</mentioned></gloss>
  <gloss versionDate="2009-03-17" xml:lang="fr">du latin, <mentioned>ainsi</mentioned></gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">原文照錄</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Lateinisch für 'auf diese Weise', 'so'</gloss>
  <desc versionDate="2006-03-20" xml:lang="en">contains text reproduced although apparently incorrect or inaccurate.</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient du texte reproduit quoiqu'il est apparemment
    incorrect ou inexact.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene texto reproducido aparentemente icorrecto o
    inexacto.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含看似錯誤但仍照實轉錄的文字 。</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un frammento di testo riprodotto anche se
    apparentemente errato o impreciso.</desc>
  <desc versionDate="2006-10-28" xml:lang="ja">明らかに間違い、不正確ではあるが、そのまま収録してあるテキスト。</desc>
  <desc versionDate="2016-11-24" xml:lang="de">enthält Text, wie er in der Vorlage steht, obwohl er offensichtlich fehlerhaft ist.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <!--    <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0"
            name="macro.specialPara"/>-->
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-mz" source="#FHENRY5">for his nose was as sharp as
      a pen, and <sic>a Table</sic> of green fields.</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-wc" source="#fr-ex-Verne_Chasse">Des nuages, des
          <sic>cyrrhus</sic>, des nimbus, des cumulus, tant qu'on en veut, et assurément plus que
        n'en voulaient le maître et le serviteur.</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si on veut seulement attirer l'attention sur ce qui paraît être un problème dans la copie
        du texte, <gi>sic</gi> est utilisé seul :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-kd" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui furent
        <sic>prûlées</sic>brûlées à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte
        de Rutland.</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Il est également possible, en utilisant les éléments <gi>choice</gi> et <gi>corr</gi>, de
        proposer une lecture corrigée :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-jf" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui furent<choice><sic>prûlées</sic><corr>brûlées</corr></choice> à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte de
      Rutland.</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-fy" source="#fr-ex-Roubaud_Boucle">Ouvrage très
        véridique et mirifique du Sieur Marcus Publius Dataficus du digne fils du seigneur comte,
        vicomte, duc et archiduc Johannus de Bessinguya<choice><sic> Percepteur</sic><corr>Precepteur</corr></choice> du digne fils du seigneur comte, vicomte, duc et archiduc Johannus de
      Bessinguya.</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-fk">
    賣饅頭的老頭，背著木箱子，裡邊裝著熱<sic>鰻魚</sic>，太陽一出來，就在街上叫喚。</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-jb"> 人們走起路來是快的，嘴裡邊的呼吸，一遇到了<sic>嚴肅</sic>好像冒著煙似的。
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-kw"> 人們走起路來是快的，嘴裡邊的呼吸，一遇到了<choice><sic>嚴肅</sic><corr>嚴寒</corr></choice> 好像冒著煙似的。</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-bd" source="#biblzh-tw_n21"> 賣饅頭的老頭，背著木箱子，裡邊裝著熱<choice><sic>鰻魚</sic><corr>饅頭</corr></choice>，太陽一出來，就在街上叫喚。</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the apparent problem in the copy text,
      <gi>sic</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-mn" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <sic>we can</sic> prove or disprove anyone's theories?</egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, auf das offensichtliche Problem in der Textvorlage hinzuweisen, kann das
      <gi>sic</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-az" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <sic>we can</sic> prove or disprove anyone's theories?</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>It is also possible, using the <gi>choice</gi> and <gi>corr</gi> elements, to provide a
      corrected reading:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-lu" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <choice><sic>we can</sic><corr>can we</corr></choice> prove or disprove anyone's theories?</egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Es ist auch möglich, zusätzlich die Elemente <gi>choice</gi> und <gi>corr</gi> zu verwenden, um
      eine korrigierte Lesart anzubieten:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-wt" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <choice><sic>we can</sic><corr>can we</corr></choice> prove or disprove anyone's theories?</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-cx" source="#THENRY5">for his nose was as sharp as
      a pen, and <choice><sic>a Table</sic><corr>a' babbld</corr></choice> of green fields.</egXML>
  </exemplum>
  <listRef>
    <ptr target="#COEDCOR" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2012-03-15" xml:lang="en">Latin for <mentioned>thus</mentioned> or <mentioned>so</mentioned></gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-03-17" xml:lang="fr">du latin, <mentioned>ainsi</mentioned></gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">原文照錄</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Lateinisch für 'auf diese Weise', 'so'</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-03-20" xml:lang="en">contains text reproduced although apparently incorrect or inaccurate.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient du texte reproduit quoiqu'il est apparemment
    incorrect ou inexact.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene texto reproducido aparentemente icorrecto o
    inexacto.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含看似錯誤但仍照實轉錄的文字 。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un frammento di testo riprodotto anche se
    apparentemente errato o impreciso.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-28" xml:lang="ja">明らかに間違い、不正確ではあるが、そのまま収録してあるテキスト。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält Text, wie er in der Vorlage steht, obwohl er offensichtlich fehlerhaft ist.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!--    <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0"
            name="macro.specialPara"/>-->
    <macroRef key="macro.paraContent"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-mz" source="#FHENRY5">for his nose was as sharp as
      a pen, and <sic>a Table</sic> of green fields.</egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-wc" source="#fr-ex-Verne_Chasse">Des nuages, des
          <sic>cyrrhus</sic>, des nimbus, des cumulus, tant qu'on en veut, et assurément plus que
        n'en voulaient le maître et le serviteur.</egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si on veut seulement attirer l'attention sur ce qui paraît être un problème dans la copie
        du texte, <gi>sic</gi> est utilisé seul :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-kd" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui furent
        <sic>prûlées</sic>brûlées à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte
        de Rutland.</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Il est également possible, en utilisant les éléments <gi>choice</gi> et <gi>corr</gi>, de
        proposer une lecture corrigée :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-jf" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui furent<choice><sic>prûlées</sic><corr>brûlées</corr></choice> à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte de
      Rutland.</egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-fy" source="#fr-ex-Roubaud_Boucle">Ouvrage très
        véridique et mirifique du Sieur Marcus Publius Dataficus du digne fils du seigneur comte,
        vicomte, duc et archiduc Johannus de Bessinguya<choice><sic> Percepteur</sic><corr>Precepteur</corr></choice> du digne fils du seigneur comte, vicomte, duc et archiduc Johannus de
      Bessinguya.</egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-fk">
    賣饅頭的老頭，背著木箱子，裡邊裝著熱<sic>鰻魚</sic>，太陽一出來，就在街上叫喚。</egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-jb"> 人們走起路來是快的，嘴裡邊的呼吸，一遇到了<sic>嚴肅</sic>好像冒著煙似的。
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-kw"> 人們走起路來是快的，嘴裡邊的呼吸，一遇到了<choice><sic>嚴肅</sic><corr>嚴寒</corr></choice> 好像冒著煙似的。</egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-bd" source="#biblzh-tw_n21"> 賣饅頭的老頭，背著木箱子，裡邊裝著熱<choice><sic>鰻魚</sic><corr>饅頭</corr></choice>，太陽一出來，就在街上叫喚。</egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[10]`.

```xml
<exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the apparent problem in the copy text,
      <gi>sic</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-mn" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <sic>we can</sic> prove or disprove anyone's theories?</egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[11]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, auf das offensichtliche Problem in der Textvorlage hinzuweisen, kann das
      <gi>sic</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-az" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <sic>we can</sic> prove or disprove anyone's theories?</egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[12]`.

```xml
<exemplum xml:lang="en">
    <p>It is also possible, using the <gi>choice</gi> and <gi>corr</gi> elements, to provide a
      corrected reading:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-lu" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <choice><sic>we can</sic><corr>can we</corr></choice> prove or disprove anyone's theories?</egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[13]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Es ist auch möglich, zusätzlich die Elemente <gi>choice</gi> und <gi>corr</gi> zu verwenden, um
      eine korrigierte Lesart anzubieten:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-wt" source="#VINGE">I don't know, Juan. It's so far in the past now
      — how <choice><sic>we can</sic><corr>can we</corr></choice> prove or disprove anyone's theories?</egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[14]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sic-egXML-cx" source="#THENRY5">for his nose was as sharp as
      a pen, and <choice><sic>a Table</sic><corr>a' babbld</corr></choice> of green fields.</egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COEDCOR" type="div3"/>
  </listRef>
```

^b28

