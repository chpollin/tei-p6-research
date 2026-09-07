---
type: representation
source-type: document
source: '[[00_sources/tei-p5-itype-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 iType
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/iType.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# iType

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8070. Git blob: `fc464ab6a729f09289fcab60e7e5eb3ded4da156`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-iType" ident="iType">
  <gloss versionDate="2005-10-11" xml:lang="en">inflectional class</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">굴절 부류</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">屈折變化種類</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">classe flexionnelle</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">categoría no flexiva</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">tipologia di flessione</gloss>
  <desc versionDate="2005-10-11" xml:lang="en">indicates the inflectional class associated with a lexical item.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어휘 항목과 관련된 굴절 부류를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指明單字的屈折變化種類。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">語彙項目の屈折の種類を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique la classe flexionnelle à laquelle appartient un
    item lexical.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la categoría no flexiva de un elemento léxico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica la tipologia di flessione associata ad un'unità
    lessicale</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.morphLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-10-11" xml:lang="en">indicates the type of indicator used to specify the inflection class, when it is
        necessary to distinguish between the usual abbreviated indications (e.g.
        <mentioned>inv</mentioned>) and other kinds of indicators, such as special codes referring
        to conjugation patterns, etc.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">어형변화 등을 가리키는 특별한 부호와 같이 다른 종류의 지시자와 일반적 축약표시(예,
          <mentioned>inv</mentioned>)를 구별할 필요가 있을 때, 굴절 부류를 명시하는 지시자의 유형을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">若需要區別曲折變化種類的一般縮寫指標 (例：inv)
        以及其他指標，像是詞形變化模式的特殊代碼等，則在此說明指示標記類型。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">一般的な省略形とは異なる指標、例えば活用パタンを表す特別な記号を
        分ける必要がある場合に、屈折の種類を示す指標の種類を示す。</desc>
      <desc versionDate="2009-04-07" xml:lang="fr">donne le type d'indicateur employé pour indiquer la
        classe flexionnelle, quand on a besoin de distinguer entre les abréviations usuelles (par
        exemple <mentioned>inv</mentioned>) et d'autres types d'indicateurs tels que des codes
        spéciifiques faisant référence à des modèles de conjugaison, etc.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala el tipo de indicador usado para especificar la
        categoría flexiva, cuando es necesario distinguir entre los indicadores abreviados
        habituales (p.ej. <mentioned>inv</mentioned>) y otros tipos de indicadores, como códigos
        especiales para referir modelos de conjugación, etc.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il tipo di indicatore utilizzato per
        specificare la tipologia di flessione, qualora sia necessario distinguere tra le indicazioni
        abbreviate solite (ad esempio <mentioned>inv</mentioned>)e altri tipi di indicatori, quali
        codici speciali per fare riferimento al tipo di coniugazione, ecc.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="abbrev">
          <desc versionDate="2007-06-27" xml:lang="en">abbreviated indicator</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">축약 지시자</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">縮寫指標</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indicador abreviado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">省略指標。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indicateur abrégé</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indicatore abbreviato.</desc>
        </valItem>
        <valItem ident="verbTable">
          <desc versionDate="2007-06-27" xml:lang="en">coded reference to a table of verbs</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">동사 테이블에 대한 부호화 참조.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">動詞表的編碼參照</desc>
          <desc versionDate="2008-04-06" xml:lang="es">referencia cifrada a una tabla de verbos</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">動詞一覧へのコード付き参照。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">référence codée à un tableau de conjugaison</desc>
          <desc versionDate="2007-01-21" xml:lang="it">riferimento codificato ad una tavola di
          verbi</desc>
        </valItem>
      </valList>
      <remarks ident="iType-attr.type-remarks" versionDate="2005-10-11" xml:lang="en">
        <p>This element is synonymous with <tag>gram type='inflectional type'</tag>.</p>
      </remarks>
      <remarks ident="iType-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet élément est synonyme de <tag>gram type='inflectional type'</tag>.</p>
      </remarks>
      <remarks ident="iType-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該要素は、要素<tag>gram type='inflectional type'</tag> と同等である。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iType-egXML-pb" xml:lang="fr">
      <form>
        <orth>horrifier</orth>
        <pron>ORifje</pron>
        <iType type="vbtable">7</iType>
      </form>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iType-egXML-ac">
      <form>
        <orth>horrifier</orth>
        <pron>[óRifje] </pron>
        <iType type="vbtable">7</iType>
      </form>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iType-egXML-nc"> ( 因漢語無動詞的語尾變化，故不提供範例。) </egXML>
  </exemplum>
  <remarks ident="iType-remarks" versionDate="2005-10-11" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements. Typical content will be
        <mentioned>invariant</mentioned>, <mentioned>n 3</mentioned> etc.</p>
  </remarks>
  <remarks ident="iType-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères et des éléments du niveau expression. Le contenu
      type sera <mentioned>invariant</mentioned>, <mentioned>n 3</mentioned> etc.</p>
  </remarks>
  <remarks ident="iType-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 文字データと句レベル要素を示すかもしれない。例えば、 <mentioned>invariant</mentioned>、<mentioned>n
      3</mentioned>など。 </p>
  </remarks>
  <listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-10-11" xml:lang="en">inflectional class</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">굴절 부류</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">屈折變化種類</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">classe flexionnelle</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">categoría no flexiva</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">tipologia di flessione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-10-11" xml:lang="en">indicates the inflectional class associated with a lexical item.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어휘 항목과 관련된 굴절 부류를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明單字的屈折變化種類。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">語彙項目の屈折の種類を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la classe flexionnelle à laquelle appartient un
    item lexical.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la categoría no flexiva de un elemento léxico.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la tipologia di flessione associata ad un'unità
    lessicale</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.morphLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-11" xml:lang="en">indicates the type of indicator used to specify the inflection class, when it is
        necessary to distinguish between the usual abbreviated indications (e.g.
        <mentioned>inv</mentioned>) and other kinds of indicators, such as special codes referring
        to conjugation patterns, etc.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어형변화 등을 가리키는 특별한 부호와 같이 다른 종류의 지시자와 일반적 축약표시(예,
          <mentioned>inv</mentioned>)를 구별할 필요가 있을 때, 굴절 부류를 명시하는 지시자의 유형을 나타낸다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">若需要區別曲折變化種類的一般縮寫指標 (例：inv)
        以及其他指標，像是詞形變化模式的特殊代碼等，則在此說明指示標記類型。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">一般的な省略形とは異なる指標、例えば活用パタンを表す特別な記号を
        分ける必要がある場合に、屈折の種類を示す指標の種類を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-04-07" xml:lang="fr">donne le type d'indicateur employé pour indiquer la
        classe flexionnelle, quand on a besoin de distinguer entre les abréviations usuelles (par
        exemple <mentioned>inv</mentioned>) et d'autres types d'indicateurs tels que des codes
        spéciifiques faisant référence à des modèles de conjugaison, etc.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala el tipo de indicador usado para especificar la
        categoría flexiva, cuando es necesario distinguir entre los indicadores abreviados
        habituales (p.ej. <mentioned>inv</mentioned>) y otros tipos de indicadores, como códigos
        especiales para referir modelos de conjugación, etc.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il tipo di indicatore utilizzato per
        specificare la tipologia di flessione, qualora sia necessario distinguere tra le indicazioni
        abbreviate solite (ad esempio <mentioned>inv</mentioned>)e altri tipi di indicatori, quali
        codici speciali per fare riferimento al tipo di coniugazione, ecc.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="abbrev">
          <desc versionDate="2007-06-27" xml:lang="en">abbreviated indicator</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">축약 지시자</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">縮寫指標</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indicador abreviado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">省略指標。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">indicateur abrégé</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indicatore abbreviato.</desc>
        </valItem>
        <valItem ident="verbTable">
          <desc versionDate="2007-06-27" xml:lang="en">coded reference to a table of verbs</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">동사 테이블에 대한 부호화 참조.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">動詞表的編碼參照</desc>
          <desc versionDate="2008-04-06" xml:lang="es">referencia cifrada a una tabla de verbos</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">動詞一覧へのコード付き参照。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">référence codée à un tableau de conjugaison</desc>
          <desc versionDate="2007-01-21" xml:lang="it">riferimento codificato ad una tavola di
          verbi</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="iType-attr.type-remarks" versionDate="2005-10-11" xml:lang="en">
        <p>This element is synonymous with <tag>gram type='inflectional type'</tag>.</p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="iType-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet élément est synonyme de <tag>gram type='inflectional type'</tag>.</p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="iType-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該要素は、要素<tag>gram type='inflectional type'</tag> と同等である。 </p>
      </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iType-egXML-pb" xml:lang="fr">
      <form>
        <orth>horrifier</orth>
        <pron>ORifje</pron>
        <iType type="vbtable">7</iType>
      </form>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iType-egXML-ac">
      <form>
        <orth>horrifier</orth>
        <pron>[óRifje] </pron>
        <iType type="vbtable">7</iType>
      </form>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iType-egXML-nc"> ( 因漢語無動詞的語尾變化，故不提供範例。) </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="iType-remarks" versionDate="2005-10-11" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements. Typical content will be
        <mentioned>invariant</mentioned>, <mentioned>n 3</mentioned> etc.</p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="iType-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères et des éléments du niveau expression. Le contenu
      type sera <mentioned>invariant</mentioned>, <mentioned>n 3</mentioned> etc.</p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="iType-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 文字データと句レベル要素を示すかもしれない。例えば、 <mentioned>invariant</mentioned>、<mentioned>n
      3</mentioned>など。 </p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
```

^b34

