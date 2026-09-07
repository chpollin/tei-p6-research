---
type: representation
source-type: document
source: '[[00_sources/tei-p5-reg-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 reg
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/reg.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# reg

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6434. Git blob: `4549a6dd864bf03fbecadf38e94bb4d55f4e9d18`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-reg" ident="reg">
  <gloss versionDate="2005-01-14" xml:lang="en">regularization</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">정규화</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">一般化</gloss>
  <gloss versionDate="2024-02-14" xml:lang="ja">規則化</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">régularisation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">regularización</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">regolarizzazione</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Normalisierung</gloss>  
  <desc versionDate="2005-01-14" xml:lang="en">contains a reading which has been regularized or normalized in some sense.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 면에서 정규화 또는 표준화된 해석을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標誌一般化或規格化處理過的文字。</desc>
  <desc versionDate="2024-02-14" xml:lang="ja">規則化された読みを示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une partie qui a été régularisée ou normalisée
        de façon quelconque.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una lectura que ha sido regularizada o
        normalizada en algún sentido.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una lettura è stata regolarizzata o
        normalizzata in qualche modo.</desc>
    <desc versionDate="2016-11-24" xml:lang="de">enthält eine normalisierte Schreibweise einer Textstelle.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <!--    <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0"
            name="macro.phraseSeq"/> -->
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the fact that the copy text has been
            regularized, <gi>reg</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-ed" source="#COHQHE-eg-11">
      <q>Please <reg>knock</reg> if an <reg>answer</reg> is <reg>required</reg>
            </q>
    </egXML>
    <!-- from Winnie the Pooh, from memory-->
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, darauf hinzuweisen, dass die Textvorlage normalisiert wurde, kann das
      <gi>reg</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-ug" source="#COHQHE-eg-11">
      <q>Please <reg>knock</reg> if an <reg>answer</reg> is <reg>required</reg>
      </q>
    </egXML>
    <!-- from Winnie the Pooh, from memory-->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si on veut attirer l'attention sur le fait que le texte a été régularisé, <gi>reg</gi> est
        utilisé seul :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-oo" source="#VESE-eg-13x">
      <l><reg>Maître</reg> Corbeau sur un arbre perché,</l>
      <l><reg>Tenait</reg> en son bec un fromage.</l>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Il est également possible d'identifier l'auteur de la régularisation, et avec les éléments
          <gi>choice</gi> et<gi>orig</gi>, donner à la fois la lecture originale et la lecture
        régularisée.:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-lv" source="#VESE-eg-13x">
      <l><choice><orig>Maistre</orig><reg resp="#LB">Maître</reg></choice>Corbeau sur un arbre                perché,</l>
      <l><choice><orig>Tenoit</orig><reg resp="#LB">Tenait</reg></choice> en son bec un            fromage.</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-km">
      <q>你已經<reg>計劃</reg>我們<reg>下週</reg>旅遊的<reg>計畫</reg>了嗎？</q>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-bi">
      <q>你已經 <choice><reg>計劃</reg><orig>計畫</orig></choice> 我們 <choice><reg>下週</reg><orig>下周</orig></choice> 旅遊的 <choice><reg>計畫</reg><orig>計劃</orig></choice>了嗎？
      </q>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>It is also possible to identify the individual responsible for the regularization, and,
            using the <gi>choice</gi> and <gi>orig</gi> elements, to provide both the original and
            regularized readings:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-hr" source="#COHQHE-eg-11">
      <q>Please <choice><reg resp="#LB">knock</reg><orig>cnk</orig></choice> if an <choice><reg>answer</reg><orig>nsr</orig></choice> is <choice><reg>required</reg><orig>reqd</orig></choice>
            </q>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Es ist auch möglich, die für die Normalisierung verantwortliche Person zu identifizieren; mit
      den Elementen <gi>choice</gi> und <gi>orig</gi> können sowohl die originale als auch die
      normalisierte Lesart angeboten werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-nr" source="#COHQHE-eg-11">
      <q>Please <choice><reg resp="#LB">knock</reg><orig>cnk</orig></choice> if an <choice><reg>answer</reg><orig>nsr</orig></choice> is <choice><reg>required</reg><orig>reqd</orig></choice>
      </q>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COEDREG" type="div1"/>
    <ptr target="#TC" type="div1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">regularization</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">정규화</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">一般化</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2024-02-14" xml:lang="ja">規則化</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">régularisation</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">regularización</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">regolarizzazione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Normalisierung</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a reading which has been regularized or normalized in some sense.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 면에서 정규화 또는 표준화된 해석을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標誌一般化或規格化處理過的文字。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-02-14" xml:lang="ja">規則化された読みを示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une partie qui a été régularisée ou normalisée
        de façon quelconque.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lectura que ha sido regularizada o
        normalizada en algún sentido.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lettura è stata regolarizzata o
        normalizzata in qualche modo.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält eine normalisierte Schreibweise einer Textstelle.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!--    <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0"
            name="macro.phraseSeq"/> -->
    <macroRef key="macro.paraContent"/>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the fact that the copy text has been
            regularized, <gi>reg</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-ed" source="#COHQHE-eg-11">
      <q>Please <reg>knock</reg> if an <reg>answer</reg> is <reg>required</reg>
            </q>
    </egXML>
    <!-- from Winnie the Pooh, from memory-->
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, darauf hinzuweisen, dass die Textvorlage normalisiert wurde, kann das
      <gi>reg</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-ug" source="#COHQHE-eg-11">
      <q>Please <reg>knock</reg> if an <reg>answer</reg> is <reg>required</reg>
      </q>
    </egXML>
    <!-- from Winnie the Pooh, from memory-->
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si on veut attirer l'attention sur le fait que le texte a été régularisé, <gi>reg</gi> est
        utilisé seul :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-oo" source="#VESE-eg-13x">
      <l><reg>Maître</reg> Corbeau sur un arbre perché,</l>
      <l><reg>Tenait</reg> en son bec un fromage.</l>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Il est également possible d'identifier l'auteur de la régularisation, et avec les éléments
          <gi>choice</gi> et<gi>orig</gi>, donner à la fois la lecture originale et la lecture
        régularisée.:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-lv" source="#VESE-eg-13x">
      <l><choice><orig>Maistre</orig><reg resp="#LB">Maître</reg></choice>Corbeau sur un arbre                perché,</l>
      <l><choice><orig>Tenoit</orig><reg resp="#LB">Tenait</reg></choice> en son bec un            fromage.</l>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-km">
      <q>你已經<reg>計劃</reg>我們<reg>下週</reg>旅遊的<reg>計畫</reg>了嗎？</q>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-bi">
      <q>你已經 <choice><reg>計劃</reg><orig>計畫</orig></choice> 我們 <choice><reg>下週</reg><orig>下周</orig></choice> 旅遊的 <choice><reg>計畫</reg><orig>計劃</orig></choice>了嗎？
      </q>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <p>It is also possible to identify the individual responsible for the regularization, and,
            using the <gi>choice</gi> and <gi>orig</gi> elements, to provide both the original and
            regularized readings:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-hr" source="#COHQHE-eg-11">
      <q>Please <choice><reg resp="#LB">knock</reg><orig>cnk</orig></choice> if an <choice><reg>answer</reg><orig>nsr</orig></choice> is <choice><reg>required</reg><orig>reqd</orig></choice>
            </q>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Es ist auch möglich, die für die Normalisierung verantwortliche Person zu identifizieren; mit
      den Elementen <gi>choice</gi> und <gi>orig</gi> können sowohl die originale als auch die
      normalisierte Lesart angeboten werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-reg-egXML-nr" source="#COHQHE-eg-11">
      <q>Please <choice><reg resp="#LB">knock</reg><orig>cnk</orig></choice> if an <choice><reg>answer</reg><orig>nsr</orig></choice> is <choice><reg>required</reg><orig>reqd</orig></choice>
      </q>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COEDREG" type="div1"/>
    <ptr target="#TC" type="div1"/>
  </listRef>
```

^b27

