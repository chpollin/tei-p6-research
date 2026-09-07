---
type: representation
source-type: document
source: '[[00_sources/tei-p5-finalrubric-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 finalRubric
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/finalRubric.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# finalRubric

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4042. Git blob: `4e3067f2fd2aa9d226a4ef431238311dee7097a1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="FINALRUBRIC" ident="finalRubric">
  <gloss versionDate="2020-12-20" xml:lang="en">final rubric</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">rubrique de fin</gloss>
  <desc versionDate="2005-05-28" xml:lang="en" xml:id="finalrubric.desc">contains the string of words that denotes the end of a text division, often with an assertion as to its author and title, usually set off from the text itself by red ink, by a different size or type of script, or by some other such visual device.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">종종 저자와 제목에 대한 언급을 하며, 적색의 잉크, 스크립트의 다양한 크기 또는 유형, 또는 어떤 시각적 도구로 표시된 텍스트로 시작되는 텍스트 부분의 끝을 표시하는 단어 열을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含表示該文字區段結尾的字串，常有作者及標題的聲明，通常使用紅墨水、不同的字型與大小、或用其他不同視覺效果的圖案，來與文件本身作區別。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の終わりを示す文字列を示す。その著者やタイトルを含むこと
  がある。一般には、テキスト中にある朱書きや、大きさや種類の異なる字体
  など、異なる視覚効果で示されている。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient les derniers mots d'une section de texte,
      qui incluent souvent la mention de son auteur et de son titre, et sont généralement
      différenciés du texte lui-même par l'utilisation d'une encre rouge, par une taille ou un style
      d'écriture particuliers, ou par tout autre moyen visuel.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una serie de palabras que señala el fin de una división textual; a menudo declara el autor y el título, y dicha serie normalmente es evidenciada del resto mediante tinta roja, un estilo distinto o una dimensión distinta de los caracteres, u otro rasgo gráfico visible.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una stringa di parole che segnala la fine di una partizione testuale e spesso ne dichiara autore e titolo; tale stringa è solitamente evidenziata rispetto al resto tramite inchiostro rosso, diverso stile o diversa dimensione del carattere, o altro espediente grafico.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FINALRUBRIC-egXML-tm">
      <finalRubric>Explicit le romans de la Rose ou l'art 
d'amours est toute enclose.</finalRubric>
      <finalRubric>ok lúkv ver þar Brennu-Nials savgv</finalRubric>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FINALRUBRIC-egXML-we" source="#fr-ex-Roman-Rose">
      <finalRubric>Explicit le romans de la Rose ou l'art d'amours est toute enclose.</finalRubric>
      <finalRubric>Ci falt la geste que Turoldus declinet. </finalRubric>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FINALRUBRIC-egXML-vb" source="#biblzh-tw_n42">
      <finalRubric>黃幼莘貢俚</finalRubric>
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
<gloss versionDate="2020-12-20" xml:lang="en">final rubric</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">rubrique de fin</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-05-28" xml:lang="en" xml:id="finalrubric.desc">contains the string of words that denotes the end of a text division, often with an assertion as to its author and title, usually set off from the text itself by red ink, by a different size or type of script, or by some other such visual device.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">종종 저자와 제목에 대한 언급을 하며, 적색의 잉크, 스크립트의 다양한 크기 또는 유형, 또는 어떤 시각적 도구로 표시된 텍스트로 시작되는 텍스트 부분의 끝을 표시하는 단어 열을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含表示該文字區段結尾的字串，常有作者及標題的聲明，通常使用紅墨水、不同的字型與大小、或用其他不同視覺效果的圖案，來與文件本身作區別。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の終わりを示す文字列を示す。その著者やタイトルを含むこと
  がある。一般には、テキスト中にある朱書きや、大きさや種類の異なる字体
  など、異なる視覚効果で示されている。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient les derniers mots d'une section de texte,
      qui incluent souvent la mention de son auteur et de son titre, et sont généralement
      différenciés du texte lui-même par l'utilisation d'une encre rouge, par une taille ou un style
      d'écriture particuliers, ou par tout autre moyen visuel.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una serie de palabras que señala el fin de una división textual; a menudo declara el autor y el título, y dicha serie normalmente es evidenciada del resto mediante tinta roja, un estilo distinto o una dimensión distinta de los caracteres, u otro rasgo gráfico visible.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una stringa di parole che segnala la fine di una partizione testuale e spesso ne dichiara autore e titolo; tale stringa è solitamente evidenziata rispetto al resto tramite inchiostro rosso, diverso stile o diversa dimensione del carattere, o altro espediente grafico.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FINALRUBRIC-egXML-tm">
      <finalRubric>Explicit le romans de la Rose ou l'art 
d'amours est toute enclose.</finalRubric>
      <finalRubric>ok lúkv ver þar Brennu-Nials savgv</finalRubric>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FINALRUBRIC-egXML-we" source="#fr-ex-Roman-Rose">
      <finalRubric>Explicit le romans de la Rose ou l'art d'amours est toute enclose.</finalRubric>
      <finalRubric>Ci falt la geste que Turoldus declinet. </finalRubric>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FINALRUBRIC-egXML-vb" source="#biblzh-tw_n42">
      <finalRubric>黃幼莘貢俚</finalRubric>
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

