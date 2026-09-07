---
type: representation
source-type: document
source: '[[00_sources/tei-p5-derivation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 derivation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/derivation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# derivation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9619. Git blob: `e97da780e730f8d6fbb6fe1b6175ac34a91cb21a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="corpus" xml:id="gi-derivation" ident="derivation">
  <gloss versionDate="2007-06-12" xml:lang="en">derivation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">dérivation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the nature and extent of originality of this text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 원본성에 대한 특성과 범위를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述文本的特性與原創性的程度。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該テキストの真性度を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit la nature et le degré d'originalité de ce
      texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe la naturaleza y la originalidad de este texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive la natura ed il grado di originalità del testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.textDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">categorizes the derivation of the text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 유래를 범주화한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">將文本來歷分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該テキストの起源の分類を示す。</desc>
      <desc versionDate="2009-03-20" xml:lang="fr">catégorise la dérivation du texte.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">caracteriza la derivación del texto</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica la provenienza del testo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="original">
          <desc versionDate="2007-06-27" xml:lang="en">text is original</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 원본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為原創文本</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es original</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストはオリジナルである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est un texte original.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è originale.</desc>
        </valItem>
        <valItem ident="revision">
          <desc versionDate="2007-06-27" xml:lang="en">text is a revision of some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 다른 텍스트의 수정본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為另一文本的修訂版</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es una revisión de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを元にした改訂である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est une révision d'un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è una revisione di qualche altro testo.</desc>
        </valItem>
        <valItem ident="translation">
          <desc versionDate="2007-06-27" xml:lang="en">text is a translation of some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 다른 텍스트의 번역본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為另一文本的翻譯版</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es una traducción de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを翻訳したものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est une traduction d'un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è la traduzione di qualche altro testo.</desc>
        </valItem>
        <valItem ident="abridgment">
          <desc versionDate="2007-06-27" xml:lang="en">text is an abridged version of some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스가 다른 텍스트의 요약본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為另一文本的刪節版</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es una versión abreviada de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを簡約したものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est une version abrégée d'un
autre texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è una versione ridotta di qualche altro testo.</desc>
        </valItem>
        <valItem ident="plagiarism">
          <desc versionDate="2007-06-27" xml:lang="en">text is plagiarized from some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 다른 텍스트의 표절본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本抄襲自另一文本</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es un plagio de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを剽窃したものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est un plagiat d'un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è un plagio di qualche altro testo.</desc>
        </valItem>
        <valItem ident="traditional">
          <desc versionDate="2007-06-27" xml:lang="en">text has no obvious source but is one of a
        number derived from some common ancestor</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 분명한 원본은 없으나, 어떤 공통 텍스트에서 도출된 텍스트들 중 하나이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本無明確來源，但和其他文本有共同的衍生來歷</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto no tiene ninguna fuente obvia, pero es uno de los derivados de algún antepasado común</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、元資料が不明であるが、何かしらを元にたテキス
	  トである。</desc>
          <desc versionDate="2009-03-20" xml:lang="fr">le texte n'a pas de source évidente mais
est l'un des nombreux textes dérivés d'un ancêtre commun.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è privo di una specifica fonte, ma è uno dei testi derivati da una fonte comune.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-cm" source="#UND">
      <derivation type="original"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2019-09-16" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-mh" source="#UND">
      <derivation type="translation" source="#rosette"/>
      <!--  ...    -->
      <!--  in the sourceDesc:    -->
      <bibl xml:id="rosette">
        <author>de Béranger, Pierre-Jean</author>. <date>1839</date>. "<title level="a">Rosette</title>". In <editor>H. Fournier</editor>, ed. <title level="m">Œuvres complètes de Béranger</title>. <biblScope unit="volume">Vol 2</biblScope> (p. <biblScope unit="page">29-30</biblScope>).</bibl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-wo" source="#UND">
      <derivation type="original"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-jm" source="#UND">
      <derivation type="原始"/>
    </egXML>
  </exemplum>
  <remarks ident="derivation-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>For derivative texts, details of the ancestor
may be included in the source description.</p>
  </remarks>
  <remarks ident="derivation-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Pour les textes dérivés, des détails concernant le texte "ancêtre" peuvent être
                inclus dans la description de la source. </p>
  </remarks>
  <remarks ident="derivation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    伝本が依る元資料の詳細は、ヘダー部分の元資料記述に示されかもしれな
    い。
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
<gloss versionDate="2007-06-12" xml:lang="en">derivation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">dérivation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the nature and extent of originality of this text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 원본성에 대한 특성과 범위를 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述文本的特性與原創性的程度。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストの真性度を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit la nature et le degré d'originalité de ce
      texte.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la naturaleza y la originalidad de este texto.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive la natura ed il grado di originalità del testo.</desc>
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
<desc versionDate="2005-01-14" xml:lang="en">categorizes the derivation of the text.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 유래를 범주화한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">將文本來歷分類。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストの起源の分類を示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-03-20" xml:lang="fr">catégorise la dérivation du texte.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">caracteriza la derivación del texto</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica la provenienza del testo.</desc>
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
<valList type="open">
        <valItem ident="original">
          <desc versionDate="2007-06-27" xml:lang="en">text is original</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 원본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為原創文本</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es original</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストはオリジナルである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est un texte original.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è originale.</desc>
        </valItem>
        <valItem ident="revision">
          <desc versionDate="2007-06-27" xml:lang="en">text is a revision of some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 다른 텍스트의 수정본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為另一文本的修訂版</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es una revisión de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを元にした改訂である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est une révision d'un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è una revisione di qualche altro testo.</desc>
        </valItem>
        <valItem ident="translation">
          <desc versionDate="2007-06-27" xml:lang="en">text is a translation of some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 다른 텍스트의 번역본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為另一文本的翻譯版</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es una traducción de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを翻訳したものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est une traduction d'un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è la traduzione di qualche altro testo.</desc>
        </valItem>
        <valItem ident="abridgment">
          <desc versionDate="2007-06-27" xml:lang="en">text is an abridged version of some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스가 다른 텍스트의 요약본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本為另一文本的刪節版</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es una versión abreviada de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを簡約したものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est une version abrégée d'un
autre texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è una versione ridotta di qualche altro testo.</desc>
        </valItem>
        <valItem ident="plagiarism">
          <desc versionDate="2007-06-27" xml:lang="en">text is plagiarized from some other text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 다른 텍스트의 표절본이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本抄襲自另一文本</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto es un plagio de algún otro texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、他のテキストを剽窃したものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le texte est un plagiat d'un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è un plagio di qualche altro testo.</desc>
        </valItem>
        <valItem ident="traditional">
          <desc versionDate="2007-06-27" xml:lang="en">text has no obvious source but is one of a
        number derived from some common ancestor</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 분명한 원본은 없으나, 어떤 공통 텍스트에서 도출된 텍스트들 중 하나이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本無明確來源，但和其他文本有共同的衍生來歷</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto no tiene ninguna fuente obvia, pero es uno de los derivados de algún antepasado común</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、元資料が不明であるが、何かしらを元にたテキス
	  トである。</desc>
          <desc versionDate="2009-03-20" xml:lang="fr">le texte n'a pas de source évidente mais
est l'un des nombreux textes dérivés d'un ancêtre commun.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è privo di una specifica fonte, ma è uno dei testi derivati da una fonte comune.</desc>
        </valItem>
      </valList>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-cm" source="#UND">
      <derivation type="original"/>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2019-09-16" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-mh" source="#UND">
      <derivation type="translation" source="#rosette"/>
      <!--  ...    -->
      <!--  in the sourceDesc:    -->
      <bibl xml:id="rosette">
        <author>de Béranger, Pierre-Jean</author>. <date>1839</date>. "<title level="a">Rosette</title>". In <editor>H. Fournier</editor>, ed. <title level="m">Œuvres complètes de Béranger</title>. <biblScope unit="volume">Vol 2</biblScope> (p. <biblScope unit="page">29-30</biblScope>).</bibl>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-wo" source="#UND">
      <derivation type="original"/>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-derivation-egXML-jm" source="#UND">
      <derivation type="原始"/>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="derivation-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>For derivative texts, details of the ancestor
may be included in the source description.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="derivation-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Pour les textes dérivés, des détails concernant le texte "ancêtre" peuvent être
                inclus dans la description de la source. </p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="derivation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    伝本が依る元資料の詳細は、ヘダー部分の元資料記述に示されかもしれな
    い。
    </p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
```

^b28

