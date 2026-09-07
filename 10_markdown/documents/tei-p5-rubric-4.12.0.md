---
type: representation
source-type: document
source: '[[00_sources/tei-p5-rubric-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 rubric
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/rubric.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# rubric

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5108. Git blob: `6a67e6fa06fa9e735d76fb25df5cd9725ed2623a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="RUBRIC" ident="rubric">
  <gloss versionDate="2007-06-12" xml:lang="en">rubric</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">rubrique</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="rubric.desc">contains the text of any <term>rubric</term> or heading attached to a particular manuscript item, that is, a string of words through which a
manuscript or other object signals the beginning of a text division, often with an assertion as to its author and title, which is in some way set off from the text itself, typically in red ink, or by use of different size or type of script, or some other such visual device.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><term>rubric</term>(주서, 불게 인쇄한 것) 또는 특별한 원고 항목에 첨부된 표제의 텍스트를 포함한다. 즉, 종종 저자와 제목에 대한 언급으로 시작되며, 일반적으로 적색 잉크로, 스크립트의 다양한 크기 또는 유형의 사용으로, 또는 다른 시각적 도구로 텍스트가 시작되어 원고가 텍스트 구역의 시작이라는 표시를 하는 단어 문자열.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何<term>按語</term>的文字或是附在特殊手稿項目的標題，即手稿用來指示文字區段開始的字串，常有作者及標題的聲明，通常使用紅墨水、不同的字型與大小、或用其他不同視覺效果的圖案，來跟文件本身作區別。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja"><term>朱書き部分</term>、すなわち、手書き資料の見出し部分のテキスト
  を示す。手書き資料中にあるあるテキスト部分の始点を示すもので、よく著
  者やタイトルが記されている。テキストとは異なって示されており、一般に
  は赤いインクで書かれている。または、異なる大きさや種類の字体が使われ
  るなど、ある視覚効果が使われている。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le texte d'une <term>rubrique</term> ou d'un
      intitulé propres à un item, c'est-à-dire des mots qui signalent le début du texte, qui
      incluent souvent la mention de son auteur et de son titre, et qui sont différenciés du texte
      lui-même, généralement à l'encre rouge, par une taille ou un style d'écriture particuliers, ou
      par tout autre procédé de ce genre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el texto de eventuales <term>rúbricas</term> o títulos asignados a un determinado fragmento del manuscrito; se trata de series de palabras que señalan el inicio de una división textual, a menudo tales series contienen información sobre el autor o el título, y se evidencian del resto mediante tinta roja, un estilo distinto o una dimensión distinta del carácter, u otro rasgo gráfico visible.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il testo di eventuali <term>titoli in rosso</term> o titoli assegnati a una determinata porzione di manoscritto; si tratta di stringhe di parole che segnalano l'inizio di una partizione testuale; tali stringhe sono solitamente evidenziate rispetto al resto tramite inchiostro rosso, diverso stile o diversa dimensione del carattere, o altro espediente grafico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.msQuoteLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RUBRIC-egXML-or">
      <rubric>Nu koma Skyckiu Rym<ex>ur</ex>.</rubric>
      <rubric>Incipit liber de consciencia humana a beatissimo Bernardo editus.</rubric>
      <rubric><locus>16.  f. 28v in margin: </locus>Dicta Cassiodori</rubric>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RUBRIC-egXML-hn">
      <rubric>Nu koma Skyckiu Rym<ex>ur</ex>.</rubric>
      <rubric>Incipit liber de consciencia humana a beatissimo Bernardo editus.</rubric>
      <rubric><locus>16. f. 28v in margin: </locus>Dicta Cassiodori</rubric>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RUBRIC-egXML-qi">
      <rubric>華亭徐懷祖燕公著</rubric>
      <rubric>代筆社記</rubric>
      <rubric><locus>第一頁右緣空白：</locus>4號 第九例</rubric>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mscoit"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">rubric</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">rubrique</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="rubric.desc">contains the text of any <term>rubric</term> or heading attached to a particular manuscript item, that is, a string of words through which a
manuscript or other object signals the beginning of a text division, often with an assertion as to its author and title, which is in some way set off from the text itself, typically in red ink, or by use of different size or type of script, or some other such visual device.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><term>rubric</term>(주서, 불게 인쇄한 것) 또는 특별한 원고 항목에 첨부된 표제의 텍스트를 포함한다. 즉, 종종 저자와 제목에 대한 언급으로 시작되며, 일반적으로 적색 잉크로, 스크립트의 다양한 크기 또는 유형의 사용으로, 또는 다른 시각적 도구로 텍스트가 시작되어 원고가 텍스트 구역의 시작이라는 표시를 하는 단어 문자열.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何<term>按語</term>的文字或是附在特殊手稿項目的標題，即手稿用來指示文字區段開始的字串，常有作者及標題的聲明，通常使用紅墨水、不同的字型與大小、或用其他不同視覺效果的圖案，來跟文件本身作區別。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja"><term>朱書き部分</term>、すなわち、手書き資料の見出し部分のテキスト
  を示す。手書き資料中にあるあるテキスト部分の始点を示すもので、よく著
  者やタイトルが記されている。テキストとは異なって示されており、一般に
  は赤いインクで書かれている。または、異なる大きさや種類の字体が使われ
  るなど、ある視覚効果が使われている。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le texte d'une <term>rubrique</term> ou d'un
      intitulé propres à un item, c'est-à-dire des mots qui signalent le début du texte, qui
      incluent souvent la mention de son auteur et de son titre, et qui sont différenciés du texte
      lui-même, généralement à l'encre rouge, par une taille ou un style d'écriture particuliers, ou
      par tout autre procédé de ce genre.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el texto de eventuales <term>rúbricas</term> o títulos asignados a un determinado fragmento del manuscrito; se trata de series de palabras que señalan el inicio de una división textual, a menudo tales series contienen información sobre el autor o el título, y se evidencian del resto mediante tinta roja, un estilo distinto o una dimensión distinta del carácter, u otro rasgo gráfico visible.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il testo di eventuali <term>titoli in rosso</term> o titoli assegnati a una determinata porzione di manoscritto; si tratta di stringhe di parole che segnalano l'inizio di una partizione testuale; tali stringhe sono solitamente evidenziate rispetto al resto tramite inchiostro rosso, diverso stile o diversa dimensione del carattere, o altro espediente grafico.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.msQuoteLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RUBRIC-egXML-or">
      <rubric>Nu koma Skyckiu Rym<ex>ur</ex>.</rubric>
      <rubric>Incipit liber de consciencia humana a beatissimo Bernardo editus.</rubric>
      <rubric><locus>16.  f. 28v in margin: </locus>Dicta Cassiodori</rubric>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RUBRIC-egXML-hn">
      <rubric>Nu koma Skyckiu Rym<ex>ur</ex>.</rubric>
      <rubric>Incipit liber de consciencia humana a beatissimo Bernardo editus.</rubric>
      <rubric><locus>16. f. 28v in margin: </locus>Dicta Cassiodori</rubric>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RUBRIC-egXML-qi">
      <rubric>華亭徐懷祖燕公著</rubric>
      <rubric>代筆社記</rubric>
      <rubric><locus>第一頁右緣空白：</locus>4號 第九例</rubric>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mscoit"/>
  </listRef>
```

^b15

