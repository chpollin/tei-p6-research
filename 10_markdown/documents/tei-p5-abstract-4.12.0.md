---
type: representation
source-type: document
source: '[[00_sources/tei-p5-abstract-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 abstract
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/abstract.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# abstract

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3699. Git blob: `cd0849a0e3ae0ce3b3e6e0198fcc222aaaf57ae7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-abstract" ident="abstract">
  <desc versionDate="2012-12-27" xml:lang="en">contains a summary or formal
    abstract prefixed to an existing source document by the encoder.</desc>
  <desc versionDate="2018-09-08" xml:lang="es">Contiene un resumen o abstract formal prefijado a una fuente documental por el codificador.</desc>
  <desc versionDate="2021-10-21" xml:lang="it">contiene un riepilogo o <foreign>abstract</foreign> formale aggiunto, in testa a un dato documento di origine, da chi codifica.</desc>
  <desc versionDate="2021-10-20" xml:lang="de">enthält eine (formale) Zusammenfassung, die einem bestehenden Quelldokument vorangestellt wird.</desc>
  <desc versionDate="2018-12-18" xml:lang="ja">符号化する人によって既存の元文書の前に付加された要約または正式な要約を含む。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <classRef key="model.listLike"/>
      <elementRef key="listBibl"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-abstract-egXML-lr" source="#Burnard-db">
      <profileDesc>
        <abstract resp="#LB">
          <p>Good database design involves the acquisition and deployment of
            skills which have a wider relevance to the educational process. From
            a set of more or less instinctive rules of thumb a formal discipline
            or "methodology" of database design has evolved. Applying that
            methodology can be of great benefit to a very wide range of academic
            subjects: it requires fundamental skills of abstraction and
            generalisation and it provides a simple mechanism whereby complex
            ideas and information structures can be represented and manipulated,
            even without the use of a computer. </p>
        </abstract>
      </profileDesc>
    </egXML>
  </exemplum>
  <remarks ident="abstract-remarks" versionDate="2013-11-12" xml:lang="en">
    <p>This element is intended only for cases where no abstract is available in the
      original source. Any abstract already present in the source document
      should be encoded as a <gi>div</gi> within the <gi>front</gi>, as it
      should for a born-digital document. </p>
  </remarks>
  <remarks ident="abstract-remarks" versionDate="2018-09-08" xml:lang="es"><p>Este elemento debe utilizarse solo en casos en los que el abstract no se encuentra disponible en la fuente original. Cualquier abstract presente en el documento fuente debe ser codificado como un <gi>div</gi> dentro del <gi>front</gi>, como corresponde en los casos de documentos de origen digital.</p></remarks>
  <remarks ident="abstract-remarks" versionDate="2018-12-18" xml:lang="ja"><p>この要素は、元資料で要約が利用できない場合にのみ使用されます。 元文書に既に存在する任意の要約は、ボーンデジタル文書の場合と同じように、<gi>front</gi>内の<gi>div</gi>として符号化する必要があります。</p></remarks>
  <listRef>
    <ptr target="#HD4ABS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains a summary or formal
    abstract prefixed to an existing source document by the encoder.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2018-09-08" xml:lang="es">Contiene un resumen o abstract formal prefijado a una fuente documental por el codificador.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2021-10-21" xml:lang="it">contiene un riepilogo o <foreign>abstract</foreign> formale aggiunto, in testa a un dato documento di origine, da chi codifica.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2021-10-20" xml:lang="de">enthält eine (formale) Zusammenfassung, die einem bestehenden Quelldokument vorangestellt wird.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2018-12-18" xml:lang="ja">符号化する人によって既存の元文書の前に付加された要約または正式な要約を含む。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b6

### Block 7

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <classRef key="model.listLike"/>
      <elementRef key="listBibl"/>
    </alternate>
  </content>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-abstract-egXML-lr" source="#Burnard-db">
      <profileDesc>
        <abstract resp="#LB">
          <p>Good database design involves the acquisition and deployment of
            skills which have a wider relevance to the educational process. From
            a set of more or less instinctive rules of thumb a formal discipline
            or "methodology" of database design has evolved. Applying that
            methodology can be of great benefit to a very wide range of academic
            subjects: it requires fundamental skills of abstraction and
            generalisation and it provides a simple mechanism whereby complex
            ideas and information structures can be represented and manipulated,
            even without the use of a computer. </p>
        </abstract>
      </profileDesc>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="abstract-remarks" versionDate="2013-11-12" xml:lang="en">
    <p>This element is intended only for cases where no abstract is available in the
      original source. Any abstract already present in the source document
      should be encoded as a <gi>div</gi> within the <gi>front</gi>, as it
      should for a born-digital document. </p>
  </remarks>
```

^b9

### Block 10

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="abstract-remarks" versionDate="2018-09-08" xml:lang="es"><p>Este elemento debe utilizarse solo en casos en los que el abstract no se encuentra disponible en la fuente original. Cualquier abstract presente en el documento fuente debe ser codificado como un <gi>div</gi> dentro del <gi>front</gi>, como corresponde en los casos de documentos de origen digital.</p></remarks>
```

^b10

### Block 11

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="abstract-remarks" versionDate="2018-12-18" xml:lang="ja"><p>この要素は、元資料で要約が利用できない場合にのみ使用されます。 元文書に既に存在する任意の要約は、ボーンデジタル文書の場合と同じように、<gi>front</gi>内の<gi>div</gi>として符号化する必要があります。</p></remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD4ABS"/>
  </listRef>
```

^b12

