---
type: representation
source-type: document
source: '[[00_sources/tei-p5-seg-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 seg
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/seg.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# seg

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7840. Git blob: `e338d1ae9cc17296f57d949e5b8ac9be24a132e2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="linking" xml:id="gi-seg" ident="seg">
  <gloss versionDate="2005-01-14" xml:lang="en">arbitrary segment</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">임의의 분절</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">隨機分割</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">segment quelconque</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">segmento arbitrario</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">segmento arbitrario</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">arbiträres Segment</gloss>
  <desc versionDate="2008-01-31" xml:lang="en">represents any segmentation of text below the <soCalled>chunk</soCalled> level.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">(다른 분절 요소를 포함하여) 텍스트의 임의의 구-층위 단위를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件中任何隨機字詞層次的單元 (包括其他分割元素)。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">任意の句レベルのテキスト単位を示す(要素segを含む)。</desc>
  <desc versionDate="2009-10-06" xml:lang="fr">contient une unité de texte quelconque de niveau <soCalled>segment</soCalled>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier unidad textual a nivel sintagmático (inclusive otros elementos de tipo seg.)</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una qualsiasi unità testuale a livello sintagmatico (ivi compresi altri elementi del tipo seg).</desc>
  <desc versionDate="2017-06-19" xml:lang="de">beschreibt Segmente eines Texts unterhalb des <soCalled>Chunk-Level</soCalled>.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-mt">
      <seg>When are you leaving?</seg>
      <seg>Tomorrow.</seg>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-sh">
      <seg>Quand partez-vous ?</seg>
      <seg>Demain.</seg>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-qx" source="#fr-ex-Flaubert_Sal">
      <s>C' était à <seg type="toponyme">Mégara</seg>, faubourg de <seg type="topon">Carthage</seg>, dans les jardins d' <seg type="patronyme">Hamilcar</seg>. </s>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-pk" source="#fr-ex-Lafayette-Cleves">
      <seg type="preambule">La magnificence et la galanterie n'ont jamais paru en <seg type="toponyme">France</seg> avec tant d'éclat que <seg type="date">dans les dernières
            années du règne de <seg type="patronyme">Henri second</seg>. </seg>
        </seg>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-vv">
      <seg>你什麼時候出發?</seg>
      <seg>明天。</seg>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-dk">
      <s>
        <seg rend="caps" type="initial-cap">此屬性值表示句首第一個字母大寫</seg>
      </s>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-mz">
      <seg type="preamble">
        <seg>唐太宗李世民， <seg type="patronym">為唐高祖李淵與竇皇后的次子，</seg>是唐朝第二位皇帝。</seg>
        <seg>李承乾為其三子中的長子...</seg>
        <seg>娶長孫氏為妻，長孫皇后是北魏皇族拓跋氏之後...</seg>
      </seg>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-od">
      <s><seg rend="caps" type="initial-cap">So father's only</seg> glory was the ballfield. </s>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-wk">
      <seg type="preamble">
        <seg>Sigmund, <seg type="patronym">the son of Volsung</seg>, was a king in Frankish country.</seg>
        <seg>Sinfiotli was the eldest of his sons ...</seg>
        <seg>Borghild, Sigmund's wife, had a brother ... </seg>
      </seg>
    </egXML>
  </exemplum>
  <remarks ident="seg-remarks" versionDate="2012-04-20" xml:lang="en">
    <p>The <gi>seg</gi> element may be used at the encoder's discretion to mark any segments of the text of interest for processing. One use of the element is to mark text features for which no appropriate markup is otherwise defined. Another use is to provide an identifier for some segment which is to be pointed at by some other element—i.e. to provide a target, or a part of a target, for a <gi>ptr</gi> or other similar element.</p>
  </remarks>
  <remarks ident="seg-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>L'élément <gi>seg</gi> peut être utilisé à la discrétion de l'encodeur pour baliser tout segment du texte intéressant pour un traitement informatique. L'un des usages de cet élément est d'encoder des caractéristiques textuelles pour lesquelles aucun balisage approprié n'est défini par ailleurs. Un autre usage consiste à fournir un identifiant pour un segment vers lequel pointe un autre élément - c'est-à-dire à fournir une cible, ou une partie de cible, pour un élément <gi>ptr</gi> ou pour un autre élément similaire.</p>
  </remarks>
  <remarks ident="seg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>seg</gi>は、何らかの処理対象を想定して、符号化する人の判断 により、使用されるかもしれない。当該要素は、適当な要素が定義されて いないときに、そのテキスト素性を示すために使われる。すなわち、簡易 拡張機能としてある。また、ある部分に識別子を付与するためにも使用さ れる。すなわち、要素<gi>ptr</gi>等から参照される対象を作る。 </p>
  </remarks>
  <remarks ident="seg-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Das <gi>seg</gi>-Element kann nach Gutdünken verwendet werden, um jegliches Textsegment, welches
      für eine Weiterverarbeitung relevant sein könnte, auszuzeichnen. Eine Anwendung des Elements ist
      die Auszeichnung von Textmerkmalen, für welche sonst kein dediziertes Markup verfügbar ist. Ein
      anderer Anwendungsfall ist, einen Identifikator für ein Textsegment anzubieten, um von anderen
      Elementen auf dieses Segment verweisen zu können, z. B. um ein Ziel für einen <gi>ptr</gi> oder
      ein ähnliches Element zur Verfügung zu stellen.</p>
  </remarks>
  <listRef>
    <ptr target="#SASE"/>
    <ptr target="#VESE"/>
    <ptr target="#DRPAL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">arbitrary segment</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">임의의 분절</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">隨機分割</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">segment quelconque</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">segmento arbitrario</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">segmento arbitrario</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">arbiträres Segment</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-01-31" xml:lang="en">represents any segmentation of text below the <soCalled>chunk</soCalled> level.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">(다른 분절 요소를 포함하여) 텍스트의 임의의 구-층위 단위를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件中任何隨機字詞層次的單元 (包括其他分割元素)。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">任意の句レベルのテキスト単位を示す(要素segを含む)。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-10-06" xml:lang="fr">contient une unité de texte quelconque de niveau <soCalled>segment</soCalled>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier unidad textual a nivel sintagmático (inclusive otros elementos de tipo seg.)</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una qualsiasi unità testuale a livello sintagmatico (ivi compresi altri elementi del tipo seg).</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">beschreibt Segmente eines Texts unterhalb des <soCalled>Chunk-Level</soCalled>.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.segLike"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-mt">
      <seg>When are you leaving?</seg>
      <seg>Tomorrow.</seg>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-sh">
      <seg>Quand partez-vous ?</seg>
      <seg>Demain.</seg>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-qx" source="#fr-ex-Flaubert_Sal">
      <s>C' était à <seg type="toponyme">Mégara</seg>, faubourg de <seg type="topon">Carthage</seg>, dans les jardins d' <seg type="patronyme">Hamilcar</seg>. </s>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-pk" source="#fr-ex-Lafayette-Cleves">
      <seg type="preambule">La magnificence et la galanterie n'ont jamais paru en <seg type="toponyme">France</seg> avec tant d'éclat que <seg type="date">dans les dernières
            années du règne de <seg type="patronyme">Henri second</seg>. </seg>
        </seg>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-vv">
      <seg>你什麼時候出發?</seg>
      <seg>明天。</seg>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-dk">
      <s>
        <seg rend="caps" type="initial-cap">此屬性值表示句首第一個字母大寫</seg>
      </s>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-mz">
      <seg type="preamble">
        <seg>唐太宗李世民， <seg type="patronym">為唐高祖李淵與竇皇后的次子，</seg>是唐朝第二位皇帝。</seg>
        <seg>李承乾為其三子中的長子...</seg>
        <seg>娶長孫氏為妻，長孫皇后是北魏皇族拓跋氏之後...</seg>
      </seg>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-od">
      <s><seg rend="caps" type="initial-cap">So father's only</seg> glory was the ballfield. </s>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-seg-egXML-wk">
      <seg type="preamble">
        <seg>Sigmund, <seg type="patronym">the son of Volsung</seg>, was a king in Frankish country.</seg>
        <seg>Sinfiotli was the eldest of his sons ...</seg>
        <seg>Borghild, Sigmund's wife, had a brother ... </seg>
      </seg>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="seg-remarks" versionDate="2012-04-20" xml:lang="en">
    <p>The <gi>seg</gi> element may be used at the encoder's discretion to mark any segments of the text of interest for processing. One use of the element is to mark text features for which no appropriate markup is otherwise defined. Another use is to provide an identifier for some segment which is to be pointed at by some other element—i.e. to provide a target, or a part of a target, for a <gi>ptr</gi> or other similar element.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="seg-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>L'élément <gi>seg</gi> peut être utilisé à la discrétion de l'encodeur pour baliser tout segment du texte intéressant pour un traitement informatique. L'un des usages de cet élément est d'encoder des caractéristiques textuelles pour lesquelles aucun balisage approprié n'est défini par ailleurs. Un autre usage consiste à fournir un identifiant pour un segment vers lequel pointe un autre élément - c'est-à-dire à fournir une cible, ou une partie de cible, pour un élément <gi>ptr</gi> ou pour un autre élément similaire.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="seg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>seg</gi>は、何らかの処理対象を想定して、符号化する人の判断 により、使用されるかもしれない。当該要素は、適当な要素が定義されて いないときに、そのテキスト素性を示すために使われる。すなわち、簡易 拡張機能としてある。また、ある部分に識別子を付与するためにも使用さ れる。すなわち、要素<gi>ptr</gi>等から参照される対象を作る。 </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="seg-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Das <gi>seg</gi>-Element kann nach Gutdünken verwendet werden, um jegliches Textsegment, welches
      für eine Weiterverarbeitung relevant sein könnte, auszuzeichnen. Eine Anwendung des Elements ist
      die Auszeichnung von Textmerkmalen, für welche sonst kein dediziertes Markup verfügbar ist. Ein
      anderer Anwendungsfall ist, einen Identifikator für ein Textsegment anzubieten, um von anderen
      Elementen auf dieses Segment verweisen zu können, z. B. um ein Ziel für einen <gi>ptr</gi> oder
      ein ähnliches Element zur Verfügung zu stellen.</p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SASE"/>
    <ptr target="#VESE"/>
    <ptr target="#DRPAL"/>
  </listRef>
```

^b31

