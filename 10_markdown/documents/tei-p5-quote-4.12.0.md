---
type: representation
source-type: document
source: '[[00_sources/tei-p5-quote-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 quote
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/quote.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# quote

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4323. Git blob: `3dc5a425768c5db93a587d7625c06b020e78a0fb`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-quote" ident="quote">
  <gloss versionDate="2005-01-14" xml:lang="en">quotation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">인용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">引文</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">citation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">cita</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">citazione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a phrase or passage attributed by the narrator or author to some agency external to the text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"> 해설자 또는 저자에 의해, 텍스트의 외부 주체에 의해 생성된 것이라 밝혀진 구 또는 단락을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含敘述者或作者引用自文本以外來源的字 (句) 詞或段落。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">語り手や著者が、当該テキスト外にあるものに向けた、一節を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une expression ou un passage que le narrateur ou l'auteur attribue à une origine extérieure au texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una frase o pasaje atribuido por el narrador o autor a un agente externo al texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una frase o un brano attribuito dall'autore o dal narratore a soggetti esterni al testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.quoteLike"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quote-egXML-am" source="#COHQQ-eg-29">Lexicography has shown little sign of being affected by the
      work of followers of J.R. Firth, probably best summarized in his
      slogan, <quote>You shall know a word by the company it
      keeps</quote> 
         <ref>(Firth, 1957)</ref>
        </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quote-egXML-rd" source="#fr-ex-Beck_Morin">C'est sûrement ça
        qu'on appelle la glorieuse liberté des enfants de Dieu. <quote>Aime et fais tout ce que tu
          voudras.</quote>Mais moi, ça me démolit. </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quote-egXML-co">
        孟懿子問孝。子曰：<quote>無違。</quote>
        <ref>(論語：卷一：為政第二)</ref>
      </egXML>
  </exemplum>
  <remarks ident="quote-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>If a bibliographic citation is supplied for the source of a quotation, the two may be
            grouped using the <gi>cit</gi> element.</p>
  </remarks>
  <remarks ident="quote-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si une référence bibliographique est donnée  comme source de la  citation, 
           on  peut  les regrouper dans  l'élément <gi>cit</gi>.</p>
  </remarks>
  <remarks ident="quote-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Si una citación bibliográfica es proporcionada como fuente de una cita, las dos se pueden
            agrupar usando el elemento <gi>CIT</gi>
        </p>
  </remarks>
  <remarks ident="quote-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 引用部分に書誌情報の引用がある場合、この2つの部分は、要素 <gi>cit</gi>でまとめられる。 </p>
  </remarks>
  <listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#DSGRP"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">quotation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">인용</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">引文</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">citation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">cita</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">citazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a phrase or passage attributed by the narrator or author to some agency external to the text.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"> 해설자 또는 저자에 의해, 텍스트의 외부 주체에 의해 생성된 것이라 밝혀진 구 또는 단락을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含敘述者或作者引用自文本以外來源的字 (句) 詞或段落。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">語り手や著者が、当該テキスト外にあるものに向けた、一節を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une expression ou un passage que le narrateur ou l'auteur attribue à une origine extérieure au texte.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una frase o pasaje atribuido por el narrador o autor a un agente externo al texto.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una frase o un brano attribuito dall'autore o dal narratore a soggetti esterni al testo.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.quoteLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quote-egXML-am" source="#COHQQ-eg-29">Lexicography has shown little sign of being affected by the
      work of followers of J.R. Firth, probably best summarized in his
      slogan, <quote>You shall know a word by the company it
      keeps</quote> 
         <ref>(Firth, 1957)</ref>
        </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quote-egXML-rd" source="#fr-ex-Beck_Morin">C'est sûrement ça
        qu'on appelle la glorieuse liberté des enfants de Dieu. <quote>Aime et fais tout ce que tu
          voudras.</quote>Mais moi, ça me démolit. </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quote-egXML-co">
        孟懿子問孝。子曰：<quote>無違。</quote>
        <ref>(論語：卷一：為政第二)</ref>
      </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="quote-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>If a bibliographic citation is supplied for the source of a quotation, the two may be
            grouped using the <gi>cit</gi> element.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="quote-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si une référence bibliographique est donnée  comme source de la  citation, 
           on  peut  les regrouper dans  l'élément <gi>cit</gi>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="quote-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Si una citación bibliográfica es proporcionada como fuente de una cita, las dos se pueden
            agrupar usando el elemento <gi>CIT</gi>
        </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="quote-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 引用部分に書誌情報の引用がある場合、この2つの部分は、要素 <gi>cit</gi>でまとめられる。 </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#DSGRP"/>
  </listRef>
```

^b23

