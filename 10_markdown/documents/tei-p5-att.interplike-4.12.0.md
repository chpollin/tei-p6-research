---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.interplike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.interpLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.interpLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.interpLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10090. Git blob: `5cf9615566cf33722c0709a3681de56754bb6354`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="CLINTERP" type="atts" ident="att.interpLike">
  <desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements which represent a formal analysis or interpretation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">형식적 분석 또는 해석을 표상하는 요소의 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素的屬性，這些元素代表一正式分析或詮釋。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">形式的分析や解釈を示す要素に付与される属性を示す。</desc>
  <desc versionDate="2009-05-27" xml:lang="fr">fournit les attributs pour des éléments qui exposent une
      analyse ou une interprétation formelles.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para elementos que represental un análisis o interpretación formal.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi che rappresentano un'analisi o un'interpretazione formali.</desc>
  <!-- 
       Should be a member of att.typed (so that members of this class
       get @type & @subtype), but that was causing problems. See
       https://github.com/TEIC/TEI/issues/2270.
  -->
  <!-- begin reversion for 2270 -->
  <attList>
    <attDef ident="type" usage="rec">
      <desc versionDate="2005-10-10" xml:lang="en">indicates what kind of phenomenon is being noted in the passage.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 단락에 표기되고 있는 현상의 종류를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出段落中所註解的現象類別。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該部分で、どのような面が指摘されているのかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique quel genre de phénomène est noté dans le
          passage.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica que tipo de fenómeno está siendo anotado en el pasaje.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica quale sia il fenomeno osservato nella porzione di testo in questione.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="image">
          <desc versionDate="2007-06-27" xml:lang="en">identifies an image in the passage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락에서 이미지를 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明段落中的影像。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica una imagen en el pasaje.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該部分の画像を指示する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">identifie une image dans le passage.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un'immagine all'interno della porzione di testo.</desc>
        </valItem>
        <valItem ident="character">
          <desc versionDate="2007-06-27" xml:lang="en">identifies a character associated with the passage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락과 연관된 문자를 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明與段落相關聯的人物。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica un carácter asociado al pasaje.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該部分に関連する文字を指示する。</desc>
          <desc versionDate="2009-05-27" xml:lang="fr">identifie un personnage associé au
passage.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un personaggio associato al brano in questione.</desc>
        </valItem>
        <valItem ident="theme">
          <desc versionDate="2007-06-27" xml:lang="en">identifies a theme in the passage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락에서 주제를 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明段落中的主題。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica un tema en el pasaje.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該部分にあるテーマを指示する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">identifie un thème dans le passage.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un tema rispetto al brano in questione.</desc>
        </valItem>
        <valItem ident="allusion">
          <desc versionDate="2007-06-27" xml:lang="en">identifies an allusion to another text.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">다른 텍스트에 대한 언급을 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明另一個文本的引用。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica una alusión a otro texto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">別テキストへの言及。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">identifie une allusion à un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un'allusione a un altro testo.</desc>
        </valItem>
      </valList>
    </attDef>
    <!-- end reversion for 2270 -->
    <!-- begin addition for 2270 -->
    <attDef ident="subtype" usage="opt">
      <gloss versionDate="2009-05-29" xml:lang="en">subtype</gloss>
      <gloss versionDate="2009-05-29" xml:lang="fr">sous-type</gloss>
      <desc versionDate="2022-04-16" xml:lang="en">provides a sub-categorization of the phenomenon is being noted in the passage, if needed.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2013-01-13" xml:lang="en">
        <p>The <att>subtype</att> attribute may be used to provide any
        sub-classification for the element additional to that provided
        by its <att>type</att> attribute.</p>
      </remarks>
      <remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'attribut <att>subtype</att> peut être employé pour
        fournir une sous-classification pour cet élément, en plus de
        celle fournie par son propre attribut <att>type</att>.</p>
      </remarks>
      <remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El atributo <att>subtype</att> (subtipo) se puede utilizar
        para proporcionar cualquier subclasificación para el elemento,
        adicional a ésa proporcionada por su <att>type</att> (tipo) de
        atributo.</p>
      </remarks>
      <remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性<att>subtype</att>は、属性<att>type</att>に加えて、当該要
    素の下位分類を示すために使われる。
    </p>
      </remarks>
    </attDef>
    <!-- end addition for 2270 -->
    <attDef ident="inst" usage="opt">
      <gloss versionDate="2007-07-02" xml:lang="en">instances</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">실례</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">ejemplos</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">cas</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">casi</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">points to instances of the analysis or interpretation represented
by the current element.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 요소에 의해 표상된 분석 또는 해석의 실례를 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到目前元素所代表的分析或解釋。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素で示されている分析や解釈の実体を示す。</desc>
      <desc versionDate="2009-05-27" xml:lang="fr">pointe vers les instances de l'analyse ou de
          l'interprétation représentées par l'élément courant.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica ejemplos de análisis o interpretaciones representadas por el elemento corriente</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica esempi di analisi o interpretazione rappresentati dall'elemento corrente.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.interpLike-attr.inst-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>The current element should be an analytic one.  The element
        pointed at should be a textual one.</p>
      </remarks>
      <remarks ident="att.interpLike-attr.inst-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'élément courant doit être analytique. L'élément pointé doit être textuel.
                    </p>
      </remarks>
      <remarks ident="att.interpLike-attr.inst-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El elemento actual debe ser analítico.  El elemento señalado debe ser textual.</p>
      </remarks>
      <remarks ident="att.interpLike-attr.inst-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>当該要素は、分析的なものであるべき。参照されている要素は、
        テキストであるべき。
        </p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#AIATTS"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements which represent a formal analysis or interpretation.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">형식적 분석 또는 해석을 표상하는 요소의 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素的屬性，這些元素代表一正式分析或詮釋。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">形式的分析や解釈を示す要素に付与される属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">fournit les attributs pour des éléments qui exposent une
      analyse ou une interprétation formelles.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para elementos que represental un análisis o interpretación formal.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi che rappresentano un'analisi o un'interpretazione formali.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates what kind of phenomenon is being noted in the passage.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 단락에 표기되고 있는 현상의 종류를 나타낸다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出段落中所註解的現象類別。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該部分で、どのような面が指摘されているのかを示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique quel genre de phénomène est noté dans le
          passage.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica que tipo de fenómeno está siendo anotado en el pasaje.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica quale sia il fenomeno osservato nella porzione di testo in questione.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="image">
          <desc versionDate="2007-06-27" xml:lang="en">identifies an image in the passage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락에서 이미지를 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明段落中的影像。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica una imagen en el pasaje.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該部分の画像を指示する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">identifie une image dans le passage.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un'immagine all'interno della porzione di testo.</desc>
        </valItem>
        <valItem ident="character">
          <desc versionDate="2007-06-27" xml:lang="en">identifies a character associated with the passage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락과 연관된 문자를 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明與段落相關聯的人物。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica un carácter asociado al pasaje.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該部分に関連する文字を指示する。</desc>
          <desc versionDate="2009-05-27" xml:lang="fr">identifie un personnage associé au
passage.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un personaggio associato al brano in questione.</desc>
        </valItem>
        <valItem ident="theme">
          <desc versionDate="2007-06-27" xml:lang="en">identifies a theme in the passage.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락에서 주제를 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明段落中的主題。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica un tema en el pasaje.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該部分にあるテーマを指示する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">identifie un thème dans le passage.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un tema rispetto al brano in questione.</desc>
        </valItem>
        <valItem ident="allusion">
          <desc versionDate="2007-06-27" xml:lang="en">identifies an allusion to another text.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">다른 텍스트에 대한 언급을 식별한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標明另一個文本的引用。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">identifica una alusión a otro texto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">別テキストへの言及。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">identifie une allusion à un autre
texte.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">identifica un'allusione a un altro testo.</desc>
        </valItem>
      </valList>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2009-05-29" xml:lang="en">subtype</gloss>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2009-05-29" xml:lang="fr">sous-type</gloss>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2022-04-16" xml:lang="en">provides a sub-categorization of the phenomenon is being noted in the passage, if needed.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2013-01-13" xml:lang="en">
        <p>The <att>subtype</att> attribute may be used to provide any
        sub-classification for the element additional to that provided
        by its <att>type</att> attribute.</p>
      </remarks>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'attribut <att>subtype</att> peut être employé pour
        fournir une sous-classification pour cet élément, en plus de
        celle fournie par son propre attribut <att>type</att>.</p>
      </remarks>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El atributo <att>subtype</att> (subtipo) se puede utilizar
        para proporcionar cualquier subclasificación para el elemento,
        adicional a ésa proporcionada por su <att>type</att> (tipo) de
        atributo.</p>
      </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="att.interpLike-attr.subtype-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        属性<att>subtype</att>は、属性<att>type</att>に加えて、当該要
    素の下位分類を示すために使われる。
    </p>
      </remarks>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-07-02" xml:lang="en">instances</gloss>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">실례</gloss>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">ejemplos</gloss>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">cas</gloss>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">casi</gloss>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">points to instances of the analysis or interpretation represented
by the current element.</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 요소에 의해 표상된 분석 또는 해석의 실례를 가리킨다.</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到目前元素所代表的分析或解釋。</desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素で示されている分析や解釈の実体を示す。</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">pointe vers les instances de l'analyse ou de
          l'interprétation représentées par l'élément courant.</desc>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica ejemplos de análisis o interpretaciones representadas por el elemento corriente</desc>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica esempi di analisi o interpretazione rappresentati dall'elemento corrente.</desc>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="att.interpLike-attr.inst-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>The current element should be an analytic one.  The element
        pointed at should be a textual one.</p>
      </remarks>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="att.interpLike-attr.inst-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'élément courant doit être analytique. L'élément pointé doit être textuel.
                    </p>
      </remarks>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="att.interpLike-attr.inst-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El elemento actual debe ser analítico.  El elemento señalado debe ser textual.</p>
      </remarks>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[4]`.

```xml
<remarks ident="att.interpLike-attr.inst-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>当該要素は、分析的なものであるべき。参照されている要素は、
        テキストであるべき。
        </p>
      </remarks>
```

^b41

### Block 42

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AIATTS"/>
  </listRef>
```

^b42

