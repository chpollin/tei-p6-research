---
type: representation
source-type: document
source: '[[00_sources/tei-p5-salute-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 salute
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/salute.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# salute

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3995. Git blob: `d3249204323ae7d4888de9a49428cd45c445ecc8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-salute" ident="salute">
  <gloss versionDate="2005-01-14" xml:lang="en">salutation</gloss>
  <gloss versionDate="2022-05-09" xml:lang="ja">挨拶文言</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">인사말</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">稱呼語</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">formule de politesse</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Grußformel</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">saludo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">formula di saluto</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a salutation or greeting prefixed to a foreword, dedicatory epistle, or other
    division of a text, or the salutation in the closing of a letter, preface, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">머리말, 헌정 서한, 또는 텍스트의 다른 구역 앞에 첨부되는 인사말 또는 환영사, 아니면 편지, 서문
    등의 결문의 인사말.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含在序言、獻詞、或其他文本區段開頭的稱呼語或問候語，或是信件、引言等結尾處的致意詞。</desc>
  <desc versionDate="2022-05-09" xml:lang="ja">(著者以外の)序文や献呈書簡などのテキスト部分に附属する挨拶文言または
挨拶、または書簡や(著者による)序文の末尾にある挨拶文言を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un dédicace ou une formule de salut qui précède
    un avant-propos ou autre division du texte;  ou bien encore la formule de
    politesse qui conclut une lettre, une préface, etc.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält eine Anrede oder Grußformel, die einem Vorwort, einer Widmung oder einem anderen
    Abschnitt eines Textes vorangestellt ist oder die Grußformel am Ende eines Briefes, eines
    Vorworts, usw.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula introductiva o de saludo previa a un
    prefacio, a una dedicatoria o a atra división textual, o bien una fórmula conclusiva o de saludo
    al final de una carta, prefacio, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una formula introduttiva o di saluto anteposta
    rispetto a una prefazione, una lettera di dedica o altra partizione testuale, oppure una formula
    conclusiva o di saluto alla fine di una lettera, prefazione, ecc</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divWrapper"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-salute-egXML-xm" source="#harveyFour">
      <salute>To all courteous mindes, that will voutchsafe the readinge.</salute>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-salute-egXML-yd" source="#fr-ex-Mendes-France">
      <salute>Faites toutes mes amitiés à votre femme et recevez, mon cher ami, l'expression de
          mes sentiments affectueux et dévoués. </salute>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-salute-egXML-fw">
      <salute>致敬啟者</salute>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DSOC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">salutation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2022-05-09" xml:lang="ja">挨拶文言</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">인사말</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">稱呼語</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">formule de politesse</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Grußformel</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">saludo</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">formula di saluto</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a salutation or greeting prefixed to a foreword, dedicatory epistle, or other
    division of a text, or the salutation in the closing of a letter, preface, etc.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">머리말, 헌정 서한, 또는 텍스트의 다른 구역 앞에 첨부되는 인사말 또는 환영사, 아니면 편지, 서문
    등의 결문의 인사말.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含在序言、獻詞、或其他文本區段開頭的稱呼語或問候語，或是信件、引言等結尾處的致意詞。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">(著者以外の)序文や献呈書簡などのテキスト部分に附属する挨拶文言または
挨拶、または書簡や(著者による)序文の末尾にある挨拶文言を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un dédicace ou une formule de salut qui précède
    un avant-propos ou autre division du texte;  ou bien encore la formule de
    politesse qui conclut une lettre, une préface, etc.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält eine Anrede oder Grußformel, die einem Vorwort, einer Widmung oder einem anderen
    Abschnitt eines Textes vorangestellt ist oder die Grußformel am Ende eines Briefes, eines
    Vorworts, usw.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula introductiva o de saludo previa a un
    prefacio, a una dedicatoria o a atra división textual, o bien una fórmula conclusiva o de saludo
    al final de una carta, prefacio, etc.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una formula introduttiva o di saluto anteposta
    rispetto a una prefazione, una lettera di dedica o altra partizione testuale, oppure una formula
    conclusiva o di saluto alla fine di una lettera, prefazione, ecc</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divWrapper"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-salute-egXML-xm" source="#harveyFour">
      <salute>To all courteous mindes, that will voutchsafe the readinge.</salute>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-salute-egXML-yd" source="#fr-ex-Mendes-France">
      <salute>Faites toutes mes amitiés à votre femme et recevez, mon cher ami, l'expression de
          mes sentiments affectueux et dévoués. </salute>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-salute-egXML-fw">
      <salute>致敬啟者</salute>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSOC"/>
  </listRef>
```

^b22

