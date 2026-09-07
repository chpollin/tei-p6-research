---
type: representation
source-type: document
source: '[[00_sources/tei-p5-supplied-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 supplied
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/supplied.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# supplied

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6084. Git blob: `893f943e36110867eb80f26f129b59c0d8c730b5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-supplied" ident="supplied">
  <gloss versionDate="2009-11-16" xml:lang="en">supplied</gloss>
  <gloss versionDate="2009-11-16" xml:lang="fr">texte restitué</gloss>
  <desc versionDate="2014-12-24" xml:lang="en">signifies text supplied by the transcriber or editor for any
  reason; for example because the original cannot be read due to
  physical damage, or because of an obvious omission by the author or scribe.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일반적으로 원본은 물리적 손상 또는 손실로 인해 읽을 수 없기 때문에 전사자 또는 편집자에 의해 제공된 텍스트를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出一段由轉錄者或編者添加的補充文字，添加的原因是該位置的文字無法被辨認，也許是因為來源文件的損壞或內容遺失、或是任何其他原因導致難以辨認。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">転記者や編集者にひょって付加されたテキストを示す。例えば、元のテキス
  トが物理的損傷や欠損から判読できない場合などに付加されるもの。</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">permet d'encoder du texte restitué par l'auteur de la transcription ou par l'éditeur pour une raison quelconque, le plus souvent parce que le texte du document original ne peut être lu, par suite de dommages matériels ou de lacunes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica fragmentos de texto añadidos por el transcriptor o por el revisor en el lugar donde el original es ilegible, porqué presenta daños físicos, lagunas o por otros motivos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica porzioni di testo inserite dal trascrittore o dal revisore al posto di porzioni di testo illegibili per danneggiamento, lacune nell'originale o altri motivi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="reason" usage="opt">
      <desc versionDate="2013-12-06" xml:lang="en">one or more words indicating why the text has had to be supplied, e.g.
      <mentioned>overbinding</mentioned>, <mentioned>faded-ink</mentioned>, <mentioned>lost-folio</mentioned>, <mentioned>omitted-in-original</mentioned>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">그 텍스트가 제시된 이유를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該文件當時必須補充的原因。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">該テキストが付加された理由を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne la raison pour laquelle on a dû restituer le texte.</desc>
<!--par exemple <mentioned>reliure-serrée</mentioned>, <mentioned>encre-effacée</mentioned>,
<mentioned>feuillet-disparu</mentioned>, <mentioned>omis-sur-original</mentioned>.-->
      <desc versionDate="2007-05-04" xml:lang="es">explica los motivos de dicha inserción.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">spiega i motivi di tale inserimento.</desc>
      <datatype maxOccurs="unbounded">
        <dataRef key="teidata.enumerated"/>
      </datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-mr">I am dr Sr yr
<supplied reason="illegible" source="#amanuensis_copy">very humble Servt</supplied>
Sydney Smith</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-od">Je reste votre ts he de svt <supplied reason="illegible" source="#amanuensis_copy">très humble et très dévoué serviteur
        </supplied>Jean Martin </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-fj" source="#biblzh-tw_n63">
       回首向來蕭瑟處，歸<supplied reason="faded-ink" source="#amanuensis_copy">去，</supplied>
       也無風雨也無晴。</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-fr"><supplied reason="omitted-in-original">Dedication</supplied> to the duke of Bejar</egXML>
  </exemplum>
  <remarks ident="supplied-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>,
<gi>unclear</gi> and <gi>supplied</gi> elements may be closely allied
in use.  See section <ptr target="#PHCOMB"/> for discussion of which
element is appropriate for which circumstance.</p>
  </remarks>
  <remarks ident="supplied-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Les éléments <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>, <gi>unclear</gi> et <gi>supplied</gi> peuvent être étroitement associés. Voir la section <ptr target="#PHCOMB"/> pour savoir quel élément est approprié à chaque circonstance.</p>
  </remarks>
  <remarks ident="supplied-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      要素<gi>damage</gi>、<gi>gap</gi>、<gi>del</gi>、<gi>unclear</gi>、<gi>supplied</gi>と共に使用されるかもしれない。これらのどの要素を
    使用するかについての詳細は、<ptr target="#PHCOMB"/>を参照のこと。
    </p>
  </remarks>
  <listRef>
    <ptr target="#PHDA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-11-16" xml:lang="en">supplied</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-11-16" xml:lang="fr">texte restitué</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2014-12-24" xml:lang="en">signifies text supplied by the transcriber or editor for any
  reason; for example because the original cannot be read due to
  physical damage, or because of an obvious omission by the author or scribe.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일반적으로 원본은 물리적 손상 또는 손실로 인해 읽을 수 없기 때문에 전사자 또는 편집자에 의해 제공된 텍스트를 표시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出一段由轉錄者或編者添加的補充文字，添加的原因是該位置的文字無法被辨認，也許是因為來源文件的損壞或內容遺失、或是任何其他原因導致難以辨認。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">転記者や編集者にひょって付加されたテキストを示す。例えば、元のテキス
  トが物理的損傷や欠損から判読できない場合などに付加されるもの。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">permet d'encoder du texte restitué par l'auteur de la transcription ou par l'éditeur pour une raison quelconque, le plus souvent parce que le texte du document original ne peut être lu, par suite de dommages matériels ou de lacunes.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica fragmentos de texto añadidos por el transcriptor o por el revisor en el lugar donde el original es ilegible, porqué presenta daños físicos, lagunas o por otros motivos.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica porzioni di testo inserite dal trascrittore o dal revisore al posto di porzioni di testo illegibili per danneggiamento, lacune nell'originale o altri motivi.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-06" xml:lang="en">one or more words indicating why the text has had to be supplied, e.g.
      <mentioned>overbinding</mentioned>, <mentioned>faded-ink</mentioned>, <mentioned>lost-folio</mentioned>, <mentioned>omitted-in-original</mentioned>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그 텍스트가 제시된 이유를 표시한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該文件當時必須補充的原因。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">該テキストが付加された理由を示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne la raison pour laquelle on a dû restituer le texte.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">explica los motivos de dicha inserción.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">spiega i motivi di tale inserimento.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded">
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-mr">I am dr Sr yr
<supplied reason="illegible" source="#amanuensis_copy">very humble Servt</supplied>
Sydney Smith</egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-od">Je reste votre ts he de svt <supplied reason="illegible" source="#amanuensis_copy">très humble et très dévoué serviteur
        </supplied>Jean Martin </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-fj" source="#biblzh-tw_n63">
       回首向來蕭瑟處，歸<supplied reason="faded-ink" source="#amanuensis_copy">去，</supplied>
       也無風雨也無晴。</egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-supplied-egXML-fr"><supplied reason="omitted-in-original">Dedication</supplied> to the duke of Bejar</egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="supplied-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>,
<gi>unclear</gi> and <gi>supplied</gi> elements may be closely allied
in use.  See section <ptr target="#PHCOMB"/> for discussion of which
element is appropriate for which circumstance.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="supplied-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Les éléments <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>, <gi>unclear</gi> et <gi>supplied</gi> peuvent être étroitement associés. Voir la section <ptr target="#PHCOMB"/> pour savoir quel élément est approprié à chaque circonstance.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="supplied-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      要素<gi>damage</gi>、<gi>gap</gi>、<gi>del</gi>、<gi>unclear</gi>、<gi>supplied</gi>と共に使用されるかもしれない。これらのどの要素を
    使用するかについての詳細は、<ptr target="#PHCOMB"/>を参照のこと。
    </p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDA"/>
  </listRef>
```

^b27

