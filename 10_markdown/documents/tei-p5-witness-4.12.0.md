---
type: representation
source-type: document
source: '[[00_sources/tei-p5-witness-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 witness
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/witness.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# witness

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3901. Git blob: `05584d2c7e59b913fb23019e88e32a9f5c03c482`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-witness" ident="witness">
  <gloss versionDate="2007-06-12" xml:lang="en">witness</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">témoin</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains either a description of a single witness referred to
within the critical apparatus, or a list of witnesses which is to be
referred to by a single sigil.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">비평적 참조 도구 내에서 참조된 단일 비교 대상 텍스트의 기술 또는 단일 변항 기호에 의해 참조된 비교 대상 텍스트 목록</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含學術編輯註解中所指的單一版本描述，或由一個印記所參照的版本列表。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">校勘資料で参照されている文献ひとつの情報、またはひとつの印が参照して
  いる文献のリストを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient soit la description d'un seul témoin
			auquel il est fait référence à l'intérieur de l'apparat critique, soit une liste de
			témoins, à laquelle on doit faire référence par une seule abréviation.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">puede contener bien la descripción de un único testimonio indicado en el aparato crítico, o una lista de testimonios indicada por una única sigla.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">può contenere la descrizione di un unico testimone indicato nell'apparato critico, oppure una lista di testimoni indicata da un'unica sigla.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <!-- the first 3 items are the content of macro.limitedContent. Including it as a macro causes a processing failure 
        in generating a DTD.
       -->
      <textNode/>
      <classRef key="model.limitedPhrase"/>
      <classRef key="model.inter"/>
      <elementRef key="note"/>
      <elementRef key="object"/>
   </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-witness-egXML-fc">
      <listWit>
        <witness xml:id="EL">Ellesmere, Huntingdon Library 26.C.9</witness>
        <witness xml:id="HG">Hengwrt, National Library of Wales,
   Aberystwyth, Peniarth 392D</witness>
        <witness xml:id="RA2">Bodleian Library Rawlinson Poetic 149
   (see further <ptr target="http://www.examples.com/MSdescs#MSRP149"/>)</witness>
      </listWit>
    </egXML>
  </exemplum>
  <remarks ident="witness-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The content of the <gi>witness</gi> element may give
bibliographic information about the witness or witness group, or it
may be empty.</p>
  </remarks>
  <remarks ident="witness-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le contenu de l'élément <gi>witness</gi> peut donner une information bibliographique
                sur le témoin ou le groupe de témoins ou bien il peut rester vide.</p>
  </remarks>
  <remarks ident="witness-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>witness</gi>の内容は、当該文献や文献グループの書誌情報を示
    すかもしれない。または、空かもしれない。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">witness</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">témoin</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains either a description of a single witness referred to
within the critical apparatus, or a list of witnesses which is to be
referred to by a single sigil.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">비평적 참조 도구 내에서 참조된 단일 비교 대상 텍스트의 기술 또는 단일 변항 기호에 의해 참조된 비교 대상 텍스트 목록</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含學術編輯註解中所指的單一版本描述，或由一個印記所參照的版本列表。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">校勘資料で参照されている文献ひとつの情報、またはひとつの印が参照して
  いる文献のリストを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient soit la description d'un seul témoin
			auquel il est fait référence à l'intérieur de l'apparat critique, soit une liste de
			témoins, à laquelle on doit faire référence par une seule abréviation.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">puede contener bien la descripción de un único testimonio indicado en el aparato crítico, o una lista de testimonios indicada por una única sigla.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">può contenere la descrizione di un unico testimone indicato nell'apparato critico, oppure una lista di testimoni indicata da un'unica sigla.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <!-- the first 3 items are the content of macro.limitedContent. Including it as a macro causes a processing failure 
        in generating a DTD.
       -->
      <textNode/>
      <classRef key="model.limitedPhrase"/>
      <classRef key="model.inter"/>
      <elementRef key="note"/>
      <elementRef key="object"/>
   </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-witness-egXML-fc">
      <listWit>
        <witness xml:id="EL">Ellesmere, Huntingdon Library 26.C.9</witness>
        <witness xml:id="HG">Hengwrt, National Library of Wales,
   Aberystwyth, Peniarth 392D</witness>
        <witness xml:id="RA2">Bodleian Library Rawlinson Poetic 149
   (see further <ptr target="http://www.examples.com/MSdescs#MSRP149"/>)</witness>
      </listWit>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="witness-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The content of the <gi>witness</gi> element may give
bibliographic information about the witness or witness group, or it
may be empty.</p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="witness-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le contenu de l'élément <gi>witness</gi> peut donner une information bibliographique
                sur le témoin ou le groupe de témoins ou bien il peut rester vide.</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="witness-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>witness</gi>の内容は、当該文献や文献グループの書誌情報を示
    すかもしれない。または、空かもしれない。
    </p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b16

