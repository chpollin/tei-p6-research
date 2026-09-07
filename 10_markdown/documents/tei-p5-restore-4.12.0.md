---
type: representation
source-type: document
source: '[[00_sources/tei-p5-restore-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 restore
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/restore.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# restore

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3107. Git blob: `072a2c79f5b9b248bcddeb39039cde5557fa2733`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-restore" ident="restore">
  <gloss versionDate="2007-06-12" xml:lang="en">restore</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">rétablissement</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates restoration of text to an earlier state by
cancellation of an editorial or authorial marking or instruction.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">편집 또는 저작 표지 또는 지시의 취소를 통해서 초기 상태로 텍스트 복구를 나타낸다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">經由取消編輯或作者所做的記號或指示，復原文件到之前的狀況。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">編集者や著者による指示を覆し、以前の状態のテキストを復元することを示
  す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique le rétablissement d'un état antérieur du texte par suppression d'une marque ou d'une instruction de l'éditeur ou de l'auteur.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la reconstrucción del texto a un estado precedente por la cancelación de una anotación o instrucción del autor o el editor.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segnala il ripristino del testo a uno stato precedente in virtù della rimozione di un'annotazione o istruzione a opera dell'autore o curatore.</desc>
  <classes>
    <memberOf key="att.global"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-restore-egXML-mz">
For I hate this
<restore hand="#dhl" type="marginalStetNote"><del>my</del></restore> body                         </egXML>
  </exemplum>
  <remarks ident="restore-remarks" versionDate="2009-11-14" xml:lang="en">
    <p>On this element, the <att>type</att> attribute categorizes the
    way that the cancelled intervention has been indicated in some
    way, for example by means of a marginal note, over-inking,
    additional markup, etc. </p>
  </remarks>
  <remarks ident="restore-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>L'attribut <att>type</att> de cet élément caractérise la manière dont l'intervention supprimée a été mentionnée, par exemple par une note marginale, par une surcharge de l'écriture, par un balisage additionnel, etc. </p>
  </remarks>
  <listRef>
    <ptr target="#PHCD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">restore</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">rétablissement</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates restoration of text to an earlier state by
cancellation of an editorial or authorial marking or instruction.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">편집 또는 저작 표지 또는 지시의 취소를 통해서 초기 상태로 텍스트 복구를 나타낸다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">經由取消編輯或作者所做的記號或指示，復原文件到之前的狀況。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">編集者や著者による指示を覆し、以前の状態のテキストを復元することを示
  す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le rétablissement d'un état antérieur du texte par suppression d'une marque ou d'une instruction de l'éditeur ou de l'auteur.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la reconstrucción del texto a un estado precedente por la cancelación de una anotación o instrucción del autor o el editor.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segnala il ripristino del testo a uno stato precedente in virtù della rimozione di un'annotazione o istruzione a opera dell'autore o curatore.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
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

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-restore-egXML-mz">
For I hate this
<restore hand="#dhl" type="marginalStetNote"><del>my</del></restore> body                         </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="restore-remarks" versionDate="2009-11-14" xml:lang="en">
    <p>On this element, the <att>type</att> attribute categorizes the
    way that the cancelled intervention has been indicated in some
    way, for example by means of a marginal note, over-inking,
    additional markup, etc. </p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="restore-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>L'attribut <att>type</att> de cet élément caractérise la manière dont l'intervention supprimée a été mentionnée, par exemple par une note marginale, par une surcharge de l'écriture, par un balisage additionnel, etc. </p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHCD"/>
  </listRef>
```

^b15

