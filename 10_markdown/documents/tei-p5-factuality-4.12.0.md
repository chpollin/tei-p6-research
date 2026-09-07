---
type: representation
source-type: document
source: '[[00_sources/tei-p5-factuality-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 factuality
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/factuality.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# factuality

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10256. Git blob: `b9d1d24e9d46a03598c4145b8be717a333e43d2e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="corpus" xml:id="gi-factuality" ident="factuality">
  <gloss versionDate="2007-06-12" xml:lang="en">factuality</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">degré de réalité</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the extent to which the text may be regarded as
imaginative or non-imaginative, that is, as describing a fictional
or a non-fictional world.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 상상적 또는 비상상적, 즉, 허구적 또는 사실적 세계를 기술하는 것으로 간주될 수 있는 범위를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述該文本內容可能被認定為想像的程度、所描繪的為虛構或真實的世界。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該テキストの現実度を示す。例えば、フィクション、ノンフィクションなど。</desc>
  <desc versionDate="2009-03-20" xml:lang="fr">décrit le degré de fiction ou de réalité caractérisant un texte,
      c'est-à-dire s'il décrit un monde imaginaire ou réel.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la posibilidad de ver un texto como ficcional o no, es decir atendiendo a si describle un mundo ficticio o no.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">quantifica quanto il testo possa essere considerato di invenzione o meno, in quanto descrive un mondo immaginato o meno.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.textDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <desc versionDate="2005-01-14" xml:lang="en">categorizes the factuality of the text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 사실성을 유형화한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">將文本的真實性分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該現実度の分類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">détermine le caractère factuel ou non du texte.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica la objetividad de un texto</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica la fattualità del testo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="fiction">
          <desc versionDate="2007-06-27" xml:lang="en">the text is to be regarded as entirely imaginative</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 전적으로 상상적이라 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本為完全虛構</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto debe ser considerado como enteramente imaginativo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、想像の産物である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est à considérer comme
purement imaginaire.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo deve essere considerato interamente fittizio.</desc>
        </valItem>
        <valItem ident="fact">
          <desc versionDate="2007-06-27" xml:lang="en">the text is to be regarded as entirely informative or factual</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 전적으로 정보적이거나 사실적이라고 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本完全根據事實</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto debe ser considerado como enteramente informativo o efectivo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、事実的なものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est à considérer comme
entièrement informatif ou basé sur des faits.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo deve essere considerato interamente informativo e basato su fatti.</desc>
        </valItem>
        <valItem ident="mixed">
          <desc versionDate="2007-06-27" xml:lang="en">the text contains a mixture of fact and fiction</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 사실과 허구의 혼합이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本內容部分虛構、部分根據事實</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto contiene una mezcla de realidad y de ficción</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、フィクション、ノンフィクションが混在している。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte contient un mélange de faits
et de fiction.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo contiene un misto di fatti e finzione.</desc>
        </valItem>
        <valItem ident="inapplicable">
          <desc versionDate="2007-06-27" xml:lang="en">the fiction/fact distinction is not regarded
    as helpful or appropriate to this text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">사실과 허구의 구별은 이 텍스트에 적절치 않은 것으로 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本不適宜使用虛構／真實的區分方法</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la distinción ficción/realidad no se considera útil o apropiada para este texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">フィクション、ノンフィクションの区別は問題にならない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la distinction entre faits et fiction
n'est pas considérée comme utile ou appropriée pour ce texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la distinzione fittivo reale non è considerata utile o appropriata per il testo.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-gw" source="#UND">
      <factuality type="fiction"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-jx" source="#UND">
      <factuality type="fiction"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-ae">
      <factuality type="mixed">contient un ensemble de bavardages et de spéculations sur des
          personnes et des événements réels.</factuality>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-af" source="#UND">
      <factuality type="fiction"/>
      <!--  屬性值受文件模型限制，若要使用其他屬性值，必先修訂文件模型。 -->
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-tr">
      <factuality type="mixed">結合文言文與白話文</factuality>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-pz">
      <factuality type="mixed">contains a mixture of gossip and
 speculation about real people and events</factuality>
    </egXML>
  </exemplum>
  <remarks ident="factuality-remarks" versionDate="2012-03-14" xml:lang="en">
    <p rend="dataDesc">Usually empty, unless some further clarification of the type
attribute is needed, in which case it may contain running prose</p>
    <p>For many literary texts, a simple binary opposition between
 <q>fiction</q>
and <q>fact</q> is naïve in the extreme; this parameter is not intended
for purposes of subtle literary analysis, but as a simple means of
characterizing the claimed fictiveness of a given text. No claim is made
that works characterized as <q>fact</q> are in  any sense <q>true</q>.</p>
  </remarks>
  <remarks ident="factuality-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Habituellement vide, sauf si une clarification complémentaire sur le
                type de l’attribut est nécessaire : dans ce cas il peut contenir du texte non
                structuré. </p>
    <p>Dans de nombreux de textes littéraires, une opposition binaire entre <q>fiction</q> et
                    <q>faits</q> est extrêmement naïve ; ce paramètre n'est pas adapté
      à des fins d’une analyse littéraire fine, mais comme simple moyen de caractériser
                le degré de fiction d'un texte. Il n'est pas obligatoire que
                des oeuvres décrites comme <q>faits</q> soient  nécessairement <q>vraies</q>.</p>
  </remarks>
  <remarks ident="factuality-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    属性typeが不要であれば、当該要素は空要素である。または散文が含まれ
    るかもしれない。
    </p>
    <p>
    多くのテキストでは、<q>fiction</q>か<q>fact</q>が使用される。
    この値は、微妙な分析を意図するものではなく、単純に当該テキストの現
     実度を示すためのものである。<q>fact</q>であるとされた作品は、
     必ずしも<q>true</q>であるということではない。
     </p>
  </remarks>
  <listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">factuality</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">degré de réalité</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the extent to which the text may be regarded as
imaginative or non-imaginative, that is, as describing a fictional
or a non-fictional world.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트가 상상적 또는 비상상적, 즉, 허구적 또는 사실적 세계를 기술하는 것으로 간주될 수 있는 범위를 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述該文本內容可能被認定為想像的程度、所描繪的為虛構或真實的世界。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストの現実度を示す。例えば、フィクション、ノンフィクションなど。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-20" xml:lang="fr">décrit le degré de fiction ou de réalité caractérisant un texte,
      c'est-à-dire s'il décrit un monde imaginaire ou réel.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la posibilidad de ver un texto como ficcional o no, es decir atendiendo a si describle un mundo ficticio o no.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">quantifica quanto il testo possa essere considerato di invenzione o meno, in quanto descrive un mondo immaginato o meno.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.textDescPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">categorizes the factuality of the text.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 사실성을 유형화한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">將文本的真實性分類。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該現実度の分類を示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">détermine le caractère factuel ou non du texte.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica la objetividad de un texto</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica la fattualità del testo.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="fiction">
          <desc versionDate="2007-06-27" xml:lang="en">the text is to be regarded as entirely imaginative</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 전적으로 상상적이라 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本為完全虛構</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto debe ser considerado como enteramente imaginativo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、想像の産物である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est à considérer comme
purement imaginaire.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo deve essere considerato interamente fittizio.</desc>
        </valItem>
        <valItem ident="fact">
          <desc versionDate="2007-06-27" xml:lang="en">the text is to be regarded as entirely informative or factual</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 전적으로 정보적이거나 사실적이라고 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本完全根據事實</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto debe ser considerado como enteramente informativo o efectivo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、事実的なものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est à considérer comme
entièrement informatif ou basé sur des faits.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo deve essere considerato interamente informativo e basato su fatti.</desc>
        </valItem>
        <valItem ident="mixed">
          <desc versionDate="2007-06-27" xml:lang="en">the text contains a mixture of fact and fiction</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 사실과 허구의 혼합이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文本內容部分虛構、部分根據事實</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto contiene una mezcla de realidad y de ficción</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、フィクション、ノンフィクションが混在している。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte contient un mélange de faits
et de fiction.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo contiene un misto di fatti e finzione.</desc>
        </valItem>
        <valItem ident="inapplicable">
          <desc versionDate="2007-06-27" xml:lang="en">the fiction/fact distinction is not regarded
    as helpful or appropriate to this text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">사실과 허구의 구별은 이 텍스트에 적절치 않은 것으로 간주된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本不適宜使用虛構／真實的區分方法</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la distinción ficción/realidad no se considera útil o apropiada para este texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">フィクション、ノンフィクションの区別は問題にならない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la distinction entre faits et fiction
n'est pas considérée comme utile ou appropriée pour ce texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la distinzione fittivo reale non è considerata utile o appropriata per il testo.</desc>
        </valItem>
      </valList>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-gw" source="#UND">
      <factuality type="fiction"/>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-jx" source="#UND">
      <factuality type="fiction"/>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-ae">
      <factuality type="mixed">contient un ensemble de bavardages et de spéculations sur des
          personnes et des événements réels.</factuality>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-af" source="#UND">
      <factuality type="fiction"/>
      <!--  屬性值受文件模型限制，若要使用其他屬性值，必先修訂文件模型。 -->
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-tr">
      <factuality type="mixed">結合文言文與白話文</factuality>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-factuality-egXML-pz">
      <factuality type="mixed">contains a mixture of gossip and
 speculation about real people and events</factuality>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="factuality-remarks" versionDate="2012-03-14" xml:lang="en">
    <p rend="dataDesc">Usually empty, unless some further clarification of the type
attribute is needed, in which case it may contain running prose</p>
    <p>For many literary texts, a simple binary opposition between
 <q>fiction</q>
and <q>fact</q> is naïve in the extreme; this parameter is not intended
for purposes of subtle literary analysis, but as a simple means of
characterizing the claimed fictiveness of a given text. No claim is made
that works characterized as <q>fact</q> are in  any sense <q>true</q>.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="factuality-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Habituellement vide, sauf si une clarification complémentaire sur le
                type de l’attribut est nécessaire : dans ce cas il peut contenir du texte non
                structuré. </p>
    <p>Dans de nombreux de textes littéraires, une opposition binaire entre <q>fiction</q> et
                    <q>faits</q> est extrêmement naïve ; ce paramètre n'est pas adapté
      à des fins d’une analyse littéraire fine, mais comme simple moyen de caractériser
                le degré de fiction d'un texte. Il n'est pas obligatoire que
                des oeuvres décrites comme <q>faits</q> soient  nécessairement <q>vraies</q>.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="factuality-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    属性typeが不要であれば、当該要素は空要素である。または散文が含まれ
    るかもしれない。
    </p>
    <p>
    多くのテキストでは、<q>fiction</q>か<q>fact</q>が使用される。
    この値は、微妙な分析を意図するものではなく、単純に当該テキストの現
     実度を示すためのものである。<q>fact</q>であるとされた作品は、
     必ずしも<q>true</q>であるということではない。
     </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
```

^b30

