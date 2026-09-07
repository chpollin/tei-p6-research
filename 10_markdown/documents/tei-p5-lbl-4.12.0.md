---
type: representation
source-type: document
source: '[[00_sources/tei-p5-lbl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 lbl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/lbl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# lbl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5629. Git blob: `932b311b3a6c170c0272ea33e57a29e151674e4f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-lbl" ident="lbl">
  <gloss versionDate="2005-01-14" xml:lang="en">label</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">분류 표시</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">標籤</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">étiquette</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">etiqueta</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">etichetta</gloss>
  <desc versionDate="2007-09-23" xml:lang="en">contains a label for a form, example, translation, or other piece of information, e.g.
    abbreviation for, contraction of, literally, approximately, synonyms:, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">형태, 예문, 번역, 또는 기타 정보에 대한 분류 표시를 포함한다. 예, 약어, 단축형, 축어적,
    대체적, 유의어</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含字詞形式、範例、翻譯、或其他資訊的標籤，例如縮寫、省略、字面、約略、同義等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">語形のラベルを示す。例えば、翻訳、短縮形などの各種省略形など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">étiquette pour la forme d’un mot, pour un exemple, pour
    une traduction, ou pour tout autre type d’information, par exemple "abréviation pour",
    <q>contraction de</q>, <q>littéralement</q>, <q>approximativement</q>, <q>synonymes</q>, etc.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">en diccionarios, contiene una etiqueta para una forma,
    ejemplo, traducción u otra información, p.ej. abreviatura para, contracción de, literal.,
    aproximadamente, sinónimo, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">nei dizionari, contiene un'etichetta per una forma,
    esempio, traduzione, o altra informazione, ad esempio abbreviazione di, contrazzione di,
    letteralmente, approssimativamente, sinonimi, ecc.</desc>
  <classes>
    <memberOf key="att.global"/>    
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
    <memberOf key="model.lexicalRefinement"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">classifies the label using any convenient typology.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">편리한 방식으로 분류 표시를 분류한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法將標籤分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該ラベルの分類を示す。</desc>
      <desc versionDate="2009-04-08" xml:lang="fr">classe l'étiquette en utilisant toute typologie adaptée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica la etiqueta usada según una tipología
        funcional</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica le etichette secondo una tipologia
        funzionale</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lbl-egXML-pl">
      <entry>
        <form type="abbrev">
          <orth>MTBF</orth>
        </form>
        <form type="full">
          <lbl>abbrev. for</lbl>
          <orth>mean time between failures</orth>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lbl-egXML-vf">
      <entry>
        <form type="abbrev">
          <orth>cf.</orth>
        </form>
        <form type="full">
          <lbl>abréviation pour</lbl>
          <orth>confer</orth>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lbl-egXML-ai">
      <entry>
        <form type="abbrev">
          <orth>台大</orth>
        </form>
        <form type="full">
          <lbl>縮寫</lbl>
          <orth>台灣大學</orth>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="lbl-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Labels specifically relating to usage should be tagged with the special-purpose <gi>usg</gi>
      element rather than with the generic<gi>lbl</gi> element.</p>
  </remarks>
  <remarks ident="lbl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les étiquettes qui se rapportent spécifiquement aux usages devraient être balisées avec
      l'élément particulier <gi>usg</gi>plutôt qu'avec l'élément générique <gi>lbl</gi>. </p>
  </remarks>
  <remarks ident="lbl-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 用法に関するラベルには、一般的な要素<gi>lbl</gi>ではなく、要素 <gi>usg</gi>を使うべきである。 </p>
  </remarks>
  <listRef>
    <ptr target="#DITPFO"/>
    <ptr target="#DITPTR"/>
    <ptr target="#DITPXR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">label</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">분류 표시</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">標籤</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">étiquette</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">etiqueta</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">etichetta</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-23" xml:lang="en">contains a label for a form, example, translation, or other piece of information, e.g.
    abbreviation for, contraction of, literally, approximately, synonyms:, etc.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">형태, 예문, 번역, 또는 기타 정보에 대한 분류 표시를 포함한다. 예, 약어, 단축형, 축어적,
    대체적, 유의어</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含字詞形式、範例、翻譯、或其他資訊的標籤，例如縮寫、省略、字面、約略、同義等。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">語形のラベルを示す。例えば、翻訳、短縮形などの各種省略形など。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">étiquette pour la forme d’un mot, pour un exemple, pour
    une traduction, ou pour tout autre type d’information, par exemple "abréviation pour",
    <q>contraction de</q>, <q>littéralement</q>, <q>approximativement</q>, <q>synonymes</q>, etc.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">en diccionarios, contiene una etiqueta para una forma,
    ejemplo, traducción u otra información, p.ej. abreviatura para, contracción de, literal.,
    aproximadamente, sinónimo, etc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">nei dizionari, contiene un'etichetta per una forma,
    esempio, traduzione, o altra informazione, ad esempio abbreviazione di, contrazzione di,
    letteralmente, approssimativamente, sinonimi, ecc.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>    
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
    <memberOf key="model.lexicalRefinement"/>
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
<desc versionDate="2005-01-14" xml:lang="en">classifies the label using any convenient typology.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">편리한 방식으로 분류 표시를 분류한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法將標籤分類。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該ラベルの分類を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">classe l'étiquette en utilisant toute typologie adaptée.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica la etiqueta usada según una tipología
        funcional</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica le etichette secondo una tipologia
        funzionale</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lbl-egXML-pl">
      <entry>
        <form type="abbrev">
          <orth>MTBF</orth>
        </form>
        <form type="full">
          <lbl>abbrev. for</lbl>
          <orth>mean time between failures</orth>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lbl-egXML-vf">
      <entry>
        <form type="abbrev">
          <orth>cf.</orth>
        </form>
        <form type="full">
          <lbl>abréviation pour</lbl>
          <orth>confer</orth>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lbl-egXML-ai">
      <entry>
        <form type="abbrev">
          <orth>台大</orth>
        </form>
        <form type="full">
          <lbl>縮寫</lbl>
          <orth>台灣大學</orth>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="lbl-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Labels specifically relating to usage should be tagged with the special-purpose <gi>usg</gi>
      element rather than with the generic<gi>lbl</gi> element.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="lbl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les étiquettes qui se rapportent spécifiquement aux usages devraient être balisées avec
      l'élément particulier <gi>usg</gi>plutôt qu'avec l'élément générique <gi>lbl</gi>. </p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="lbl-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 用法に関するラベルには、一般的な要素<gi>lbl</gi>ではなく、要素 <gi>usg</gi>を使うべきである。 </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO"/>
    <ptr target="#DITPTR"/>
    <ptr target="#DITPXR"/>
  </listRef>
```

^b30

