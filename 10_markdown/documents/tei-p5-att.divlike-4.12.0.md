---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.divlike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.divLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.divLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.divLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11868. Git blob: `1b0821988ea3fc18588976041b890d87c8d72cfc`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="DIVN" type="atts" ident="att.divLike">
  <desc versionDate="2007-10-02" xml:lang="en">provides attributes common to all elements which behave in the same way as divisions.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구역과 동일한 방식으로 처리되는 모든 요소에 공통적인 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一組屬性，通用於所有與區段作用相
      同的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">区分(div、division)に相当する全要素に共通の属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit un jeu d'attributs communs à tous les
    éléments qui offrent les mêmes caractéristiques que des divisions.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona un conjunto de atributos comunes a todos los elementos que se comportan como particiones textuales.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">identifica un insieme di attributi comuni a tutti gli elementi che si comportano come partizioni testuali.</desc>
  <classes>
    <memberOf key="att.fragmentable"/>
    
    <memberOf key="att.metrical"/>
  </classes>
  <attList>
    <attDef ident="org" usage="opt">
      <gloss versionDate="2007-07-02" xml:lang="en">organization</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">organisation</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
      <gloss versionDate="2019-05-20" xml:lang="ja">組織</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">specifies how the content of the division is organized.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">구역 내용이 조직된 방법에 대해 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該區段內容的組合方式。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該区分の内容がどのように構成されているかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise l'organisation du contenu de la division</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica cómo está organizado el contenido de una división textual.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica come è organizzato il contenuto della partizione testuale.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>uniform</defaultVal>
      <valList type="closed">
        <valItem ident="composite">
          <desc versionDate="2013-03-18" xml:lang="en">no claim is made about the
		  sequence in which the immediate contents of this division
		  are to be processed, or their inter-relationships.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">혼합 내용: 즉, 이 구역의 직접적 내용이 처리되는 순서 또는 상호 관련성에 관해 어떠한 주장도 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">複合內容：未說明此區段目前內容的處理順序或相互關係。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">contenido compuesto: es decir no se hace ninguna solicitud sobre la secuencia en la cual el contenido inmediato de esta división debe ser procesado, o en sus interrelaciones.</desc>
          <desc versionDate="2019-05-10" xml:lang="ja">この部分に含まれる諸内容が処理される順番、すなわち内部関係には制約がない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">aucune déclaration n'est faite quant à l'ordre dans lequel les
composants de cette division doivent être traités ou bien quant à leurs
corrélations</desc>
          <desc versionDate="2007-01-21" xml:lang="it">non viene specificato quale sia l'ordine in cui debbano essere elaborati i contenuti della partizione, né viene indicato il rapporto in cui questi si trovano tra loro.</desc>
        </valItem>
        <valItem ident="parallel">
          <desc versionDate="2026-01-19" xml:lang="en">the contents of this element are intended to represent simultaneous or side-by-side delivery.</desc>
        </valItem>
        <valItem ident="uniform">
          <desc versionDate="2013-03-18" xml:lang="en">the immediate contents of this
		  element are regarded as forming a logical unit, to be
		  processed in sequence.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">통일 내용: 즉, 이 요소의 직접적 내용이 차례대로 처리되는 논리적 단위를 형성하는 것으로 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">一致內容：此區段目前的內容形成一個邏輯單位，且會依序處理。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">es decir el contenido inmediato de este elemento se considera integrante de una unidad lógica, para ser procesado en la secuencia.</desc>
          <desc versionDate="2019-05-10" xml:lang="ja">この要素直下の諸内容が論理的単位を構成しており、順番に処理すべきものと見なす。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">contenu uniforme : c'est-à-dire que
les composants de cet élément sont à considérer comme formant une unité
logique et doivent être traités dans l'ordre séquentiel</desc>
          <desc versionDate="2007-01-21" xml:lang="it">contenuto uniforme: i contenuti dell'elemento costituiscono un'unità logica che va elaborata in sequenza.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="sample" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">indicates whether this division is a sample of the
		original source and if so, from which part.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 구역이 원본의 표본이며 어떤 부분인지를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出此區段是否為來源文件的樣本，若為樣本，則說明出自哪一部分。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該区分が、元資料のものを含むかどうか、そうであればその場所はど
        こかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si cette division est un échantillon de
          la source originale et dans ce cas, de quelle partie.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si la división es una muestra de la fuente original y, en ese caso, de que parte de este se trata</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se la partizione è un campione del testo originario e, in tal caso, da quale parte di questo è tratta.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>complete</defaultVal>
      <valList type="closed">
        <valItem ident="initial">
          <desc versionDate="2007-06-27" xml:lang="en">division lacks material present at end in source.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 원본의 후반부에서 제시된 자료가 부족하다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段的末端無資料</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la división falta el material presente en el extremo en la fuente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該区分は、元資料の終わりの部分が欠けている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, lacune à la fin de la division</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alla partizione testuale manca del materiale nella parte finale presente nell'originale.</desc>
        </valItem>
        <valItem ident="medial">
          <desc versionDate="2007-06-27" xml:lang="en">division lacks material at start and end.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 초반부와 후반부 자료가 부족하다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段的起始與末端無資料</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el fragmento carece de material al comienzo y al final.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該区分は、元資料の始めと終わりの部分が欠けている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, lacune au
début et à la fin de la division</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alla partizione testuale manca del materiale nella parte iniziale e in quella finale.</desc>
        </valItem>
        <valItem ident="final">
          <desc versionDate="2007-06-27" xml:lang="en">division lacks material at start.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 초반부 자료가 부족하다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段的起始部分無資料</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el fragmento carece de material en el comienzo.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該区分は、元資料の始めの部分が欠けている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, lacune au
début de la division</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alla partizione manca del materiale nella parte iniziale.</desc>
        </valItem>
        <valItem ident="unknown">
          <desc versionDate="2007-06-27" xml:lang="en">position of sampled material within original unknown.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표본 자료의 원본 내의 위치를 알 수 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">來源文件中的樣本資料位置不明</desc>
          <desc versionDate="2008-04-06" xml:lang="es">ubicación del material  de muestra dentro del original desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">元資料のどの部分かは不明。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, position de
l'échantillon inconnue</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la posizione del materiale prelevato dall'originale all'interno di quest'ultimo è sconosciuta.</desc>
        </valItem>
        <valItem ident="complete">
          <desc versionDate="2007-06-27" xml:lang="en">division is not a sample.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 표본이 아니다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段非樣本</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el fragmento no es una muestra.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該領域は、元資料の一部ではない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la division n'est pas un échantillon</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la partizione testuale non è stata prelevata da alcun originale.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#DS"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-02" xml:lang="en">provides attributes common to all elements which behave in the same way as divisions.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구역과 동일한 방식으로 처리되는 모든 요소에 공통적인 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一組屬性，通用於所有與區段作用相
      同的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">区分(div、division)に相当する全要素に共通の属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit un jeu d'attributs communs à tous les
    éléments qui offrent les mêmes caractéristiques que des divisions.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un conjunto de atributos comunes a todos los elementos que se comportan como particiones textuales.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica un insieme di attributi comuni a tutti gli elementi che si comportano come partizioni testuali.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.fragmentable"/>
    
    <memberOf key="att.metrical"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-02" xml:lang="en">organization</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">organisation</gloss>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2019-05-20" xml:lang="ja">組織</gloss>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">specifies how the content of the division is organized.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구역 내용이 조직된 방법에 대해 명시한다.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該區段內容的組合方式。</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該区分の内容がどのように構成されているかを示す。</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise l'organisation du contenu de la division</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica cómo está organizado el contenido de una división textual.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica come è organizzato il contenuto della partizione testuale.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>uniform</defaultVal>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="composite">
          <desc versionDate="2013-03-18" xml:lang="en">no claim is made about the
		  sequence in which the immediate contents of this division
		  are to be processed, or their inter-relationships.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">혼합 내용: 즉, 이 구역의 직접적 내용이 처리되는 순서 또는 상호 관련성에 관해 어떠한 주장도 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">複合內容：未說明此區段目前內容的處理順序或相互關係。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">contenido compuesto: es decir no se hace ninguna solicitud sobre la secuencia en la cual el contenido inmediato de esta división debe ser procesado, o en sus interrelaciones.</desc>
          <desc versionDate="2019-05-10" xml:lang="ja">この部分に含まれる諸内容が処理される順番、すなわち内部関係には制約がない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">aucune déclaration n'est faite quant à l'ordre dans lequel les
composants de cette division doivent être traités ou bien quant à leurs
corrélations</desc>
          <desc versionDate="2007-01-21" xml:lang="it">non viene specificato quale sia l'ordine in cui debbano essere elaborati i contenuti della partizione, né viene indicato il rapporto in cui questi si trovano tra loro.</desc>
        </valItem>
        <valItem ident="parallel">
          <desc versionDate="2026-01-19" xml:lang="en">the contents of this element are intended to represent simultaneous or side-by-side delivery.</desc>
        </valItem>
        <valItem ident="uniform">
          <desc versionDate="2013-03-18" xml:lang="en">the immediate contents of this
		  element are regarded as forming a logical unit, to be
		  processed in sequence.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">통일 내용: 즉, 이 요소의 직접적 내용이 차례대로 처리되는 논리적 단위를 형성하는 것으로 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">一致內容：此區段目前的內容形成一個邏輯單位，且會依序處理。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">es decir el contenido inmediato de este elemento se considera integrante de una unidad lógica, para ser procesado en la secuencia.</desc>
          <desc versionDate="2019-05-10" xml:lang="ja">この要素直下の諸内容が論理的単位を構成しており、順番に処理すべきものと見なす。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">contenu uniforme : c'est-à-dire que
les composants de cet élément sont à considérer comme formant une unité
logique et doivent être traités dans l'ordre séquentiel</desc>
          <desc versionDate="2007-01-21" xml:lang="it">contenuto uniforme: i contenuti dell'elemento costituiscono un'unità logica che va elaborata in sequenza.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates whether this division is a sample of the
		original source and if so, from which part.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 구역이 원본의 표본이며 어떤 부분인지를 나타낸다.</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出此區段是否為來源文件的樣本，若為樣本，則說明出自哪一部分。</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該区分が、元資料のものを含むかどうか、そうであればその場所はど
        こかを示す。</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si cette division est un échantillon de
          la source originale et dans ce cas, de quelle partie.</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si la división es una muestra de la fuente original y, en ese caso, de que parte de este se trata</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se la partizione è un campione del testo originario e, in tal caso, da quale parte di questo è tratta.</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>complete</defaultVal>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="initial">
          <desc versionDate="2007-06-27" xml:lang="en">division lacks material present at end in source.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 원본의 후반부에서 제시된 자료가 부족하다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段的末端無資料</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la división falta el material presente en el extremo en la fuente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該区分は、元資料の終わりの部分が欠けている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, lacune à la fin de la division</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alla partizione testuale manca del materiale nella parte finale presente nell'originale.</desc>
        </valItem>
        <valItem ident="medial">
          <desc versionDate="2007-06-27" xml:lang="en">division lacks material at start and end.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 초반부와 후반부 자료가 부족하다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段的起始與末端無資料</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el fragmento carece de material al comienzo y al final.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該区分は、元資料の始めと終わりの部分が欠けている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, lacune au
début et à la fin de la division</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alla partizione testuale manca del materiale nella parte iniziale e in quella finale.</desc>
        </valItem>
        <valItem ident="final">
          <desc versionDate="2007-06-27" xml:lang="en">division lacks material at start.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 초반부 자료가 부족하다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段的起始部分無資料</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el fragmento carece de material en el comienzo.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該区分は、元資料の始めの部分が欠けている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, lacune au
début de la division</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alla partizione manca del materiale nella parte iniziale.</desc>
        </valItem>
        <valItem ident="unknown">
          <desc versionDate="2007-06-27" xml:lang="en">position of sampled material within original unknown.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표본 자료의 원본 내의 위치를 알 수 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">來源文件中的樣本資料位置不明</desc>
          <desc versionDate="2008-04-06" xml:lang="es">ubicación del material  de muestra dentro del original desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">元資料のどの部分かは不明。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">par rapport à la source, position de
l'échantillon inconnue</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la posizione del materiale prelevato dall'originale all'interno di quest'ultimo è sconosciuta.</desc>
        </valItem>
        <valItem ident="complete">
          <desc versionDate="2007-06-27" xml:lang="en">division is not a sample.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">구역이 표본이 아니다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">區段非樣本</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el fragmento no es una muestra.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該領域は、元資料の一部ではない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la division n'est pas un échantillon</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la partizione testuale non è stata prelevata da alcun originale.</desc>
        </valItem>
      </valList>
```

^b34

### Block 35

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DS"/>
  </listRef>
```

^b35

