---
type: representation
source-type: document
source: '[[00_sources/tei-p5-corr-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 corr
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/corr.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# corr

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5651. Git blob: `d081c8f60bebdd6d0a9240e0fc7993871c8b08c6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-corr" ident="corr">
  <gloss versionDate="2006-03-20" xml:lang="en">correction</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">정정</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">更正</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">corrección</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">correzione</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Korrektur</gloss>  
  <gloss versionDate="2024-02-28" xml:lang="ja">修正</gloss>
  <desc versionDate="2006-03-20" xml:lang="en">contains the correct form of a passage apparently erroneous in the copy text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">복사된 텍스트에서 오류로 보이는 단락의 정정 형식을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文本中看似錯誤並加以更正過後的文字。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">元資料中の明らかな間違いを正したものを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la forme correcte d'un passage
    qui est considéré erroné dans la copie du texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la forma correcta de un pasaje aparentemente erróneo en el texto de copia.</desc>
  <desc versionDate="2016-11-24" xml:lang="de">enthält die korrekte Form einer offenbar fehlerhaften Textstelle in der Vorlage.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the
      fact that the copy text has been corrected, <gi>corr</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-yi" source="#VINGE">I don't know,
      Juan. It's so far in the past now — how <corr>can we</corr> prove
      or disprove anyone's theories?</egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, darauf hinzuweisen, dass die Textvorlage korrigiert wurde, kann das
      <gi>corr</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-vt" source="#VINGE">I don't know,
      Juan. It's so far in the past now — how <corr>can we</corr> prove
      or disprove anyone's theories?</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si l'on veut mettre l'accent sur le fait que le texte a été corrigé, <gi>corr</gi> seul
        sera employé:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-eh" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui
	furent <corr>brûlées</corr> à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte de
      Rutland.</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Il est aussi possible d'associer <gi>choice</gi> et<gi>sic</gi>, pour donner une lecture
        incorrecte : </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-sm" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui furent<choice><sic>prûlées</sic><corr>brûlées</corr></choice> à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte de
      Rutland.</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-ia">
      不怨天，不尤人。下學而上達。<corr>知我</corr> 者，其天乎！</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-ev" source="#biblzh-tw_n2">
      不怨天，不尤人。下學而上達。<choice><sic>我知</sic><corr>知我</corr></choice>者，其天乎！</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>It is also possible, using the <gi>choice</gi> and
      <gi>sic</gi> elements, to provide an uncorrected reading:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-nn" source="#VINGE">I don't know, Juan. It's so far in the past now —
      how <choice><sic>we can</sic><corr>can we</corr></choice> prove or
      disprove anyone's theories?</egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Es ist auch möglich, zusätzlich die Elemente <gi>choice</gi> und <gi>sic</gi> zu verwenden, um
      eine nicht korrigierte Lesart anzubieten:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-fu" source="#VINGE">I don't know, Juan. It's so far in the past now —
      how <choice><sic>we can</sic><corr>can we</corr></choice> prove or
      disprove anyone's theories?</egXML>
  </exemplum>
  <listRef>
    <ptr target="#COEDCOR" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2006-03-20" xml:lang="en">correction</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">정정</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">更正</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">corrección</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">correzione</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Korrektur</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">修正</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-03-20" xml:lang="en">contains the correct form of a passage apparently erroneous in the copy text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">복사된 텍스트에서 오류로 보이는 단락의 정정 형식을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文本中看似錯誤並加以更正過後的文字。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元資料中の明らかな間違いを正したものを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la forme correcte d'un passage
    qui est considéré erroné dans la copie du texte.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la forma correcta de un pasaje aparentemente erróneo en el texto de copia.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält die korrekte Form einer offenbar fehlerhaften Textstelle in der Vorlage.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the
      fact that the copy text has been corrected, <gi>corr</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-yi" source="#VINGE">I don't know,
      Juan. It's so far in the past now — how <corr>can we</corr> prove
      or disprove anyone's theories?</egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, darauf hinzuweisen, dass die Textvorlage korrigiert wurde, kann das
      <gi>corr</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-vt" source="#VINGE">I don't know,
      Juan. It's so far in the past now — how <corr>can we</corr> prove
      or disprove anyone's theories?</egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si l'on veut mettre l'accent sur le fait que le texte a été corrigé, <gi>corr</gi> seul
        sera employé:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-eh" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui
	furent <corr>brûlées</corr> à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte de
      Rutland.</egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Il est aussi possible d'associer <gi>choice</gi> et<gi>sic</gi>, pour donner une lecture
        incorrecte : </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-sm" source="#fr-ex-Mauss_Sociologie">Tel est le
        chat Rutterkin des sorcières Margaret et Filippa Flower, qui furent<choice><sic>prûlées</sic><corr>brûlées</corr></choice> à Lincoln, le 11 mars 1619, pour avoir envoûté un parent du comte de
      Rutland.</egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-ia">
      不怨天，不尤人。下學而上達。<corr>知我</corr> 者，其天乎！</egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-ev" source="#biblzh-tw_n2">
      不怨天，不尤人。下學而上達。<choice><sic>我知</sic><corr>知我</corr></choice>者，其天乎！</egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <p>It is also possible, using the <gi>choice</gi> and
      <gi>sic</gi> elements, to provide an uncorrected reading:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-nn" source="#VINGE">I don't know, Juan. It's so far in the past now —
      how <choice><sic>we can</sic><corr>can we</corr></choice> prove or
      disprove anyone's theories?</egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Es ist auch möglich, zusätzlich die Elemente <gi>choice</gi> und <gi>sic</gi> zu verwenden, um
      eine nicht korrigierte Lesart anzubieten:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-corr-egXML-fu" source="#VINGE">I don't know, Juan. It's so far in the past now —
      how <choice><sic>we can</sic><corr>can we</corr></choice> prove or
      disprove anyone's theories?</egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COEDCOR" type="div3"/>
  </listRef>
```

^b25

