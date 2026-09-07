---
type: representation
source-type: document
source: '[[00_sources/tei-p5-handshift-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 handShift
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/handShift.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# handShift

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4990. Git blob: `04366d7433299fd191eab0212ad5f97b4a6cc2ed`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-handShift" ident="handShift">
  <gloss versionDate="2020-12-20" xml:lang="en">handwriting shift</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">reprise de main</gloss>
  <desc versionDate="2007-04-26" xml:lang="en">marks the beginning of a sequence of text written in a new
hand, or the beginning of a scribal stint.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">새로운 필적으로 기록된 텍스트 연쇄의 시작 또는 필기 부분의 시작을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記連續文字中轉換書寫者的開始，或是一個抄寫工作的開始。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストにおける新しい筆致の始まり、または筆写者の仕事の開始を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">marque le début d'une section du texte écrite par une nouvelle main ou le début d'une nouvelle séance d'écriture.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca el principio de un fragmento de texto atribuible a otra mano distinta o a un cambio de redactor, estilo de escritura, tinta o letra.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segnala l'inizio di una porzione di testo attribuibile ad un'altra mano o riconducibile a un cambio di redattore, stile di scrittura, inchiostro o carattere.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.handFeatures"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="new" usage="rec">
      <desc versionDate="2013-12-21" xml:lang="en">indicates a
      <gi>handNote</gi> element describing the hand
      concerned.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">새 필적을 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">表示新的書寫者。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該新しい筆致を特定する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant de la nouvelle main.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica una nueva mano.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la nuova mano.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="handShift-attr.new-remarks" versionDate="2010-07-06" xml:lang="en">
        <p>This attribute serves the same function as the
<att>hand</att> attribute provided for those elements which are members of the
<ident type="class">att.transcriptional</ident> class. It may be
renamed at a subsequent major release. </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-handShift-egXML-eq">
      <l>When wolde the cat dwelle in his ynne</l>
      <handShift medium="greenish-ink"/>
      <l>And if the cattes skynne be slyk <handShift medium="black-ink"/> and gaye</l>
    </egXML>
  </exemplum>
  <remarks ident="handShift-remarks" versionDate="2010-07-06" xml:lang="en">
    <p>The <gi>handShift</gi> element may be used either to
denote a shift in the document hand (as from one scribe to another,
on one writing style to another).  Or, it may indicate a shift within
a document hand, as a change of writing style, character or ink. Like
    other milestone elements, it should appear at the point of
    transition from some other state to the state which it describes.</p>
  </remarks>
  <remarks ident="handShift-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'élément <gi>handShift</gi>peut être utilisé soit pour noter un changement de main
dans le document (comme le passage d'un scribe à un autre, d'un style d'écriture à un
autre), soit pour indiquer un changement dans la main, comme un changement d'écriture, de caractère ou d'encre.</p>
  </remarks>
  <remarks ident="handShift-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該<gi>handShift</gi>要素は、文書中における筆致の変わり目(ある筆
      写者から別の筆写者、または、ある書記スタイルから別の書記スタイル
      への変化)を示すために使われるかもしれない。または、同じ筆致にお
      いても、書記スタイルや、文字、インクの変わり目を示すために使われ
      るかもしれない。
      </p>
  </remarks>
  <listRef>
    <ptr target="#PHDH"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">handwriting shift</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">reprise de main</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-26" xml:lang="en">marks the beginning of a sequence of text written in a new
hand, or the beginning of a scribal stint.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">새로운 필적으로 기록된 텍스트 연쇄의 시작 또는 필기 부분의 시작을 표시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記連續文字中轉換書寫者的開始，或是一個抄寫工作的開始。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストにおける新しい筆致の始まり、または筆写者の仕事の開始を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">marque le début d'une section du texte écrite par une nouvelle main ou le début d'une nouvelle séance d'écriture.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca el principio de un fragmento de texto atribuible a otra mano distinta o a un cambio de redactor, estilo de escritura, tinta o letra.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segnala l'inizio di una porzione di testo attribuibile ad un'altra mano o riconducibile a un cambio di redattore, stile di scrittura, inchiostro o carattere.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.handFeatures"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">indicates a
      <gi>handNote</gi> element describing the hand
      concerned.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">새 필적을 식별한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示新的書寫者。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該新しい筆致を特定する。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne l'identifiant de la nouvelle main.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica una nueva mano.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la nuova mano.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="handShift-attr.new-remarks" versionDate="2010-07-06" xml:lang="en">
        <p>This attribute serves the same function as the
<att>hand</att> attribute provided for those elements which are members of the
<ident type="class">att.transcriptional</ident> class. It may be
renamed at a subsequent major release. </p>
      </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-handShift-egXML-eq">
      <l>When wolde the cat dwelle in his ynne</l>
      <handShift medium="greenish-ink"/>
      <l>And if the cattes skynne be slyk <handShift medium="black-ink"/> and gaye</l>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="handShift-remarks" versionDate="2010-07-06" xml:lang="en">
    <p>The <gi>handShift</gi> element may be used either to
denote a shift in the document hand (as from one scribe to another,
on one writing style to another).  Or, it may indicate a shift within
a document hand, as a change of writing style, character or ink. Like
    other milestone elements, it should appear at the point of
    transition from some other state to the state which it describes.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="handShift-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'élément <gi>handShift</gi>peut être utilisé soit pour noter un changement de main
dans le document (comme le passage d'un scribe à un autre, d'un style d'écriture à un
autre), soit pour indiquer un changement dans la main, comme un changement d'écriture, de caractère ou d'encre.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="handShift-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該<gi>handShift</gi>要素は、文書中における筆致の変わり目(ある筆
      写者から別の筆写者、または、ある書記スタイルから別の書記スタイル
      への変化)を示すために使われるかもしれない。または、同じ筆致にお
      いても、書記スタイルや、文字、インクの変わり目を示すために使われ
      るかもしれない。
      </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDH"/>
  </listRef>
```

^b25

