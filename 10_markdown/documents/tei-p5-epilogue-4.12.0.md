---
type: representation
source-type: document
source: '[[00_sources/tei-p5-epilogue-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 epilogue
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/epilogue.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# epilogue

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6358. Git blob: `fc85553c848e8a83ad29ae82da435fac90d4bce6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-epilogue" ident="epilogue">
  <gloss versionDate="2007-06-12" xml:lang="en">epilogue</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">épilogue</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the epilogue to a drama, typically spoken by an actor out of character, possibly in
    association with a particular performance or venue.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전형적으로 등장인물들 중 하나가 말하는, 때로는 특정 공연 또는 행위의 현장과 관련된, 드라마의
    페막사.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含戲劇收場白，可能和特定演出或故事場景相關，一般是由一個演員脫離劇中身份來朗讀。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene el epílogo a un drama, pronunciado normalmente
    por un actor a parte del reparto, posiblemente asociado a una puesta en escena determinada..</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">舞台芸術における納め口上を示す。例えば、特定の演目や場所と関連している かもしれない、役者からの発話。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient l'épilogue d’une pièce de théâtre, généralement
    récité par un acteur qui n'a pas de rôle, éventuellement associé à une représentation ou un lieu
    particulier.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l'epilogo ad un'opera teatrale, di solito
    pronunciato da un attore al di fuori del ruolo teatrale, possibilmente inn relazione ad una
    particolare messa in scena o luogo di rappresentazione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        
          <classRef key="model.common"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-epilogue-egXML-hq" source="#DRPRO-eg-7">
      <epilogue>
        <head>Written by <name>Colley Cibber, Esq</name> and spoken by <name>Mrs. Cibber</name>
            </head>
        <sp>
          <lg type="couplet">
            <l>Since Fate has robb'd me of the hapless Youth,</l>
            <l>For whom my heart had hoarded up its truth;</l>
          </lg>
          <lg type="couplet">
            <l>By all the Laws of Love and Honour, now,</l>
            <l>I'm free again to chuse, — and one of you</l>
          </lg>
          <lg type="triplet">
            <l>Suppose I search the sober Gallery; — No,</l>
            <l>There's none but Prentices — &amp; Cuckolds all a row:</l>
            <l>And these, I doubt, are those that make 'em so.</l>
          </lg>
          <stage type="business">Pointing to the Boxes.</stage>
          <lg type="couplet">
            <l>'Tis very well, enjoy the jest:</l>
          </lg>
        </sp>
      </epilogue>
    </egXML>
    <!-- G. Lillo, The London Merchant  (1731) -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-epilogue-egXML-lr" source="#fr-ex-Corneille_Place-Royale">
      <epilogue>
        <head>Stances en forme d'épilogue. </head>
        <sp>
          <speaker>Alidor.</speaker>
          <lg type="stances">
            <l>Que par cette retraite elle me favorise !</l>
            <l>Alors que mes desseins cedent à mes amours,</l>
            <l> Et qu'ils ne sçauroient plus defendre ma franchise</l>
            <l> Sa haine, et ses refus viennent à leur secours.</l>
            <l> J'avois beau la trahir, une secrette amorce</l>
            <l> R'allumoit dans mon coeur l'amour par la pitié,</l>
            <l> Mes feux en recevoient une nouvelle force,</l>
            <l> Et tousjours leur ardeur en croissoit de moitié.</l>
          </lg>
        </sp>
      </epilogue>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-epilogue-egXML-in" source="#biblzh-tw_n33">
      <epilogue>
        <head>收場詩</head>
        <stage type="business">飾國王者向觀眾致辭</stage>
        <sp>
          <lg type="stanza">
            <l>袍笏登場本是虛，</l>
            <l>王侯卿相總堪嗤，</l>
            <l>但能博得觀眾喜，</l>
            <l>便是功成圓滿時。</l>
          </lg>
        </sp>
      </epilogue>
    </egXML>
  </exemplum>
  <remarks ident="epilogue-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Contains optional headings, a sequence of one or more component-level
      elements, and an optional sequence of closing material.</p>
    <p/>
  </remarks>
  <remarks ident="epilogue-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient des titres optionnels, une série d'un ou de plusieurs éléments de
      niveau composant et éventuellement une série d'éléments de fin.</p>
  </remarks>
  <remarks ident="epilogue-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 選択的にヘダー、ひとつ以上の構成要素、選択的に終末部を示す。 </p>
    <p/>
  </remarks>
  <listRef>
    <ptr target="#DRPRO" type="div3"/>
    <ptr target="#DRFAB" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">epilogue</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">épilogue</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the epilogue to a drama, typically spoken by an actor out of character, possibly in
    association with a particular performance or venue.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전형적으로 등장인물들 중 하나가 말하는, 때로는 특정 공연 또는 행위의 현장과 관련된, 드라마의
    페막사.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含戲劇收場白，可能和特定演出或故事場景相關，一般是由一個演員脫離劇中身份來朗讀。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene el epílogo a un drama, pronunciado normalmente
    por un actor a parte del reparto, posiblemente asociado a una puesta en escena determinada..</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">舞台芸術における納め口上を示す。例えば、特定の演目や場所と関連している かもしれない、役者からの発話。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient l'épilogue d’une pièce de théâtre, généralement
    récité par un acteur qui n'a pas de rôle, éventuellement associé à une représentation ou un lieu
    particulier.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l'epilogo ad un'opera teatrale, di solito
    pronunciato da un attore al di fuori del ruolo teatrale, possibilmente inn relazione ad una
    particolare messa in scena o luogo di rappresentazione.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        
          <classRef key="model.common"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-epilogue-egXML-hq" source="#DRPRO-eg-7">
      <epilogue>
        <head>Written by <name>Colley Cibber, Esq</name> and spoken by <name>Mrs. Cibber</name>
            </head>
        <sp>
          <lg type="couplet">
            <l>Since Fate has robb'd me of the hapless Youth,</l>
            <l>For whom my heart had hoarded up its truth;</l>
          </lg>
          <lg type="couplet">
            <l>By all the Laws of Love and Honour, now,</l>
            <l>I'm free again to chuse, — and one of you</l>
          </lg>
          <lg type="triplet">
            <l>Suppose I search the sober Gallery; — No,</l>
            <l>There's none but Prentices — &amp; Cuckolds all a row:</l>
            <l>And these, I doubt, are those that make 'em so.</l>
          </lg>
          <stage type="business">Pointing to the Boxes.</stage>
          <lg type="couplet">
            <l>'Tis very well, enjoy the jest:</l>
          </lg>
        </sp>
      </epilogue>
    </egXML>
    <!-- G. Lillo, The London Merchant  (1731) -->
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-epilogue-egXML-lr" source="#fr-ex-Corneille_Place-Royale">
      <epilogue>
        <head>Stances en forme d'épilogue. </head>
        <sp>
          <speaker>Alidor.</speaker>
          <lg type="stances">
            <l>Que par cette retraite elle me favorise !</l>
            <l>Alors que mes desseins cedent à mes amours,</l>
            <l> Et qu'ils ne sçauroient plus defendre ma franchise</l>
            <l> Sa haine, et ses refus viennent à leur secours.</l>
            <l> J'avois beau la trahir, une secrette amorce</l>
            <l> R'allumoit dans mon coeur l'amour par la pitié,</l>
            <l> Mes feux en recevoient une nouvelle force,</l>
            <l> Et tousjours leur ardeur en croissoit de moitié.</l>
          </lg>
        </sp>
      </epilogue>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-epilogue-egXML-in" source="#biblzh-tw_n33">
      <epilogue>
        <head>收場詩</head>
        <stage type="business">飾國王者向觀眾致辭</stage>
        <sp>
          <lg type="stanza">
            <l>袍笏登場本是虛，</l>
            <l>王侯卿相總堪嗤，</l>
            <l>但能博得觀眾喜，</l>
            <l>便是功成圓滿時。</l>
          </lg>
        </sp>
      </epilogue>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="epilogue-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Contains optional headings, a sequence of one or more component-level
      elements, and an optional sequence of closing material.</p>
    <p/>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="epilogue-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient des titres optionnels, une série d'un ou de plusieurs éléments de
      niveau composant et éventuellement une série d'éléments de fin.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="epilogue-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 選択的にヘダー、ひとつ以上の構成要素、選択的に終末部を示す。 </p>
    <p/>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRPRO" type="div3"/>
    <ptr target="#DRFAB" type="div3"/>
  </listRef>
```

^b18

