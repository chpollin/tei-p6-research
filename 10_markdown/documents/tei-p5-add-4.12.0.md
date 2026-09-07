---
type: representation
source-type: document
source: '[[00_sources/tei-p5-add-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 add
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/add.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# add

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6160. Git blob: `b6a25857bb08b2012bfe832dcc2cfe14b7f69ab1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-add" ident="add">
  <gloss versionDate="2005-01-14" xml:lang="en">addition</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">삽입, 첨가</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">插入</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr"> ajout</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">adición</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">aggiunta</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Hinzufügung</gloss>
  <gloss versionDate="2018-12-20" xml:lang="ja">書き入れ</gloss>
  <desc versionDate="2013-04-13" xml:lang="en">contains letters, words, or phrases inserted in the source
  text by an author, scribe, or a previous annotator or corrector.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">저자, 전사자, 부호화 작업자 또는 수정작업자에 의해 텍스트에 삽입된 문자, 단어, 또는 구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含由作者、抄寫者、註解者、或更正者在文本中插入的字母、單字或詞彙。</desc>
  <desc versionDate="2018-12-20" xml:lang="ja">著者、筆写者、注釈者、校正者によって挿入された文字、単語、句を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient des lettres,
  des mots ou des phrases insérés dans le texte par un auteur, un
  copiste, un annotateur ou un correcteur.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene letras,
  palabras o frases introducidas en el texto por el autor,
  transcriptor, glosador o corrector.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene lettere,
  parole o frasi inserite in un testo da un autore, copista,
  commentatore o correttore.</desc>
  <desc versionDate="2016-11-24" xml:lang="de">
      enthält Buchstaben, Wörter oder Phrasen, die in den Ausgangstext von einem Autor, einem Schreiber oder im 
      Rahmen einer zuvor erfolgten Annotation oder Korrektur in den Ausgangstext eingefügt wurden
  </desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-add-egXML-ci" source="#COEDADD-eg-84">The story I am
    going to relate is true as to its main facts, and as to the
    consequences <add place="above">of these facts</add> from which
    this tale takes its title.</egXML>
  </exemplum>
  <remarks ident="add-remarks" versionDate="2013-06-20" xml:lang="en">
    <p>In a diplomatic edition attempting to represent an original
    source, the <gi>add</gi> element should not be used for additions
    to the current TEI electronic edition made by editors or encoders.
    In these cases, either the <gi>corr</gi> or <gi>supplied</gi>
    element are recommended.</p>
    <p>In a TEI edition of a historical text with previous editorial
    emendations in which such additions or reconstructions are
    considered part of the source text, the use of <gi>add</gi> may be
    appropriate, dependent on the editorial philosophy of the
    project.</p>
  </remarks>
  <remarks ident="add-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans une édition diplomatique souhaitant representer une source
    originalle, l'élément <gi>add</gi> ne sera pas utilisé pour les
    ajouts effectués par les éditeurs ou les encodeurs. Dans ce cas, on
    va préféra soit l'élément <gi>corr</gi> soit l'élément
    <gi>supplied</gi>.</p>
  </remarks>
  <remarks ident="add-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El elemento <gi>addición</gi> no se debe utilizar para las
    adiciones hechas por los editores o los codificadores. En estos
    casos, cualquiera de los elementos <gi>corr</gi> o <gi>supplied</gi>
    son más convenientes.</p>
  </remarks>
  <remarks ident="add-remarks" versionDate="2018-12-20" xml:lang="ja">
    <p>
      元のソースを表現しようとしているdiplomatic editionでは、<gi>add</gi>要素は、編集者や符号化する人が作成した現在のTEI電子版への追加には使用しないでください。このような場合は、<gi>corr</gi>または<gi>supplied</gi>要素のいずれかをお勧めします。そのような追加や再構成が原文の一部とみなされる以前の編集上の訂正を含む歴史的テキストのTEI版では、プロジェクトの編集理念に応じて、<gi>add</gi>の使用が適切かもしれません。
    </p>
  </remarks>
  <remarks ident="add-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>
          In einer diplomatischen Ausgabe, die auf eine genaue Wiedergabe der Vorlage zielt, 
          sollte das <gi>add</gi>-Element nicht für jene Hinzufügungen genutzt werden, die von den 
          Editoren oder Auszeichnenden zu der elektronischen TEI-Edition gemacht werden. 
          In diesen Fällen wird empfohlen, entweder das <gi>corr</gi>-Element oder <gi>supplied</gi>-Element zu verwenden.
      </p>
      <p>
          In der TEI-Edition eines historischen Textes mit bereits vorhandenen editorischen Korrekturen, in dem solche Ergänzungen 
          oder Rekonstruktionen als Teil der Textvorlage betrachtet werden, kann - im Rahmen der Editionsgrundsätze eines Projekts - 
          die Verwendung des <gi>add</gi>-Elements geeignet sein.
      </p>
  </remarks>
  <listRef>
    <ptr target="#COEDADD" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">addition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">삽입, 첨가</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">插入</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr"> ajout</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">adición</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">aggiunta</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Hinzufügung</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2018-12-20" xml:lang="ja">書き入れ</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-13" xml:lang="en">contains letters, words, or phrases inserted in the source
  text by an author, scribe, or a previous annotator or corrector.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">저자, 전사자, 부호화 작업자 또는 수정작업자에 의해 텍스트에 삽입된 문자, 단어, 또는 구를 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含由作者、抄寫者、註解者、或更正者在文本中插入的字母、單字或詞彙。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2018-12-20" xml:lang="ja">著者、筆写者、注釈者、校正者によって挿入された文字、単語、句を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient des lettres,
  des mots ou des phrases insérés dans le texte par un auteur, un
  copiste, un annotateur ou un correcteur.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene letras,
  palabras o frases introducidas en el texto por el autor,
  transcriptor, glosador o corrector.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene lettere,
  parole o frasi inserite in un testo da un autore, copista,
  commentatore o correttore.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">
      enthält Buchstaben, Wörter oder Phrasen, die in den Ausgangstext von einem Autor, einem Schreiber oder im 
      Rahmen einer zuvor erfolgten Annotation oder Korrektur in den Ausgangstext eingefügt wurden
  </desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-add-egXML-ci" source="#COEDADD-eg-84">The story I am
    going to relate is true as to its main facts, and as to the
    consequences <add place="above">of these facts</add> from which
    this tale takes its title.</egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="add-remarks" versionDate="2013-06-20" xml:lang="en">
    <p>In a diplomatic edition attempting to represent an original
    source, the <gi>add</gi> element should not be used for additions
    to the current TEI electronic edition made by editors or encoders.
    In these cases, either the <gi>corr</gi> or <gi>supplied</gi>
    element are recommended.</p>
    <p>In a TEI edition of a historical text with previous editorial
    emendations in which such additions or reconstructions are
    considered part of the source text, the use of <gi>add</gi> may be
    appropriate, dependent on the editorial philosophy of the
    project.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="add-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans une édition diplomatique souhaitant representer une source
    originalle, l'élément <gi>add</gi> ne sera pas utilisé pour les
    ajouts effectués par les éditeurs ou les encodeurs. Dans ce cas, on
    va préféra soit l'élément <gi>corr</gi> soit l'élément
    <gi>supplied</gi>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="add-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El elemento <gi>addición</gi> no se debe utilizar para las
    adiciones hechas por los editores o los codificadores. En estos
    casos, cualquiera de los elementos <gi>corr</gi> o <gi>supplied</gi>
    son más convenientes.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="add-remarks" versionDate="2018-12-20" xml:lang="ja">
    <p>
      元のソースを表現しようとしているdiplomatic editionでは、<gi>add</gi>要素は、編集者や符号化する人が作成した現在のTEI電子版への追加には使用しないでください。このような場合は、<gi>corr</gi>または<gi>supplied</gi>要素のいずれかをお勧めします。そのような追加や再構成が原文の一部とみなされる以前の編集上の訂正を含む歴史的テキストのTEI版では、プロジェクトの編集理念に応じて、<gi>add</gi>の使用が適切かもしれません。
    </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="add-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>
          In einer diplomatischen Ausgabe, die auf eine genaue Wiedergabe der Vorlage zielt, 
          sollte das <gi>add</gi>-Element nicht für jene Hinzufügungen genutzt werden, die von den 
          Editoren oder Auszeichnenden zu der elektronischen TEI-Edition gemacht werden. 
          In diesen Fällen wird empfohlen, entweder das <gi>corr</gi>-Element oder <gi>supplied</gi>-Element zu verwenden.
      </p>
      <p>
          In der TEI-Edition eines historischen Textes mit bereits vorhandenen editorischen Korrekturen, in dem solche Ergänzungen 
          oder Rekonstruktionen als Teil der Textvorlage betrachtet werden, kann - im Rahmen der Editionsgrundsätze eines Projekts - 
          die Verwendung des <gi>add</gi>-Elements geeignet sein.
      </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COEDADD" type="div3"/>
  </listRef>
```

^b25

