---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.rdgpart-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.rdgPart
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.rdgPart.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.rdgPart

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4323. Git blob: `f7516462859d84b88a724e1b97309d8b7f7085b4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" type="atts" ident="att.rdgPart">
  <desc versionDate="2016-02-16" xml:lang="en">provides attributes to mark the beginning or ending of a fragmentary
manuscript or other witness.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">파편화된 원고 또는 다른 비교 대상 텍스트의 시작부 또는 종료부를 표지하는 요소의 속성</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素的屬性，這些元素標記岀零散手稿的起始、結尾或其他版本。</desc>
  <desc versionDate="2023-09-27" xml:lang="ja">手書き資料や証拠資料の断片について、その初めと終わりを示す属性。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">attributs d'éléments qui marquent le début ou la fin d'un manuscrit fragmentaire ou d'un autre témoin.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">atributos para elementos que señalan el inicio o el fin de un manuscrito fragmentario o de otro testimonio</desc>
  <desc versionDate="2007-01-21" xml:lang="it">attributi per elementi che segnalano l'inizio o la fine di un manoscritto frammentario o di altro testimone.</desc>
  <attList>
    <attDef ident="wit" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">witness or witnesses</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">testimonio o testimonios</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">témoin ou témoins</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">testimone o testimoni</gloss>
      <gloss versionDate="2023-09-27" xml:lang="ja">1つ以上の証拠資料</gloss>
      <desc versionDate="2013-12-09" xml:lang="en">contains a space-delimited list of one or more sigla indicating the witnesses
to this reading  beginning or ending at this point.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 지점에서 시작 또는 종료하는 비교 대상 텍스트를 표시하는 하나 이상의 기호 일람표 목록을 포함한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">一個或多個印記列表，指出於此處開始或結束的版本。</desc>
      <desc versionDate="2008-04-21" xml:lang="ja">この時点で開始または終了するこの読みに対する証拠資料を示す1つ以上の記号のスペース区切りリストが含まれる。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">contient une liste d'une ou plusieurs abréviations désignant les témoins qui commencent ou finissent à ce point.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">contiene una lista de una o más siglas que indican los testimonios que inician o acaban en ese punto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">contiene una lista di una o più sigle indicanti i testimoni che cominciano o finiscono in questo punto.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <remarks ident="att.rdgPart-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>These elements may appear anywhere within the elements <gi>lem</gi>
and <gi>rdg</gi>, and also within any of their constituent elements. </p>
  </remarks>
  <remarks ident="att.rdgPart-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Ces éléments peuvent figurer n'importe où à l'intérieur des éléments <gi>lem</gi> et
                    <gi>rdg</gi>, ainsi que dans tout élément qui les compose. </p>
  </remarks>
  <remarks ident="att.rdgPart-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、要素<gi>lem</gi>や<gi>rdg</gi>の中で出現するかもしれな
  い。またこれらの構成要素中にも現れるかもしれない。
  </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-02-16" xml:lang="en">provides attributes to mark the beginning or ending of a fragmentary
manuscript or other witness.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">파편화된 원고 또는 다른 비교 대상 텍스트의 시작부 또는 종료부를 표지하는 요소의 속성</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供元素的屬性，這些元素標記岀零散手稿的起始、結尾或其他版本。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">手書き資料や証拠資料の断片について、その初めと終わりを示す属性。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">attributs d'éléments qui marquent le début ou la fin d'un manuscrit fragmentaire ou d'un autre témoin.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">atributos para elementos que señalan el inicio o el fin de un manuscrito fragmentario o de otro testimonio</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">attributi per elementi che segnalano l'inizio o la fine di un manoscritto frammentario o di altro testimone.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">witness or witnesses</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">testimonio o testimonios</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">témoin ou témoins</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">testimone o testimoni</gloss>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2023-09-27" xml:lang="ja">1つ以上の証拠資料</gloss>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-09" xml:lang="en">contains a space-delimited list of one or more sigla indicating the witnesses
to this reading  beginning or ending at this point.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 지점에서 시작 또는 종료하는 비교 대상 텍스트를 표시하는 하나 이상의 기호 일람표 목록을 포함한다.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">一個或多個印記列表，指出於此處開始或結束的版本。</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-21" xml:lang="ja">この時点で開始または終了するこの読みに対する証拠資料を示す1つ以上の記号のスペース区切りリストが含まれる。</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une liste d'une ou plusieurs abréviations désignant les témoins qui commencent ou finissent à ce point.</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lista de una o más siglas que indican los testimonios que inician o acaban en ese punto.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lista di una o più sigle indicanti i testimoni che cominciano o finiscono in questo punto.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b21

### Block 22

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.rdgPart-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>These elements may appear anywhere within the elements <gi>lem</gi>
and <gi>rdg</gi>, and also within any of their constituent elements. </p>
  </remarks>
```

^b22

### Block 23

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.rdgPart-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Ces éléments peuvent figurer n'importe où à l'intérieur des éléments <gi>lem</gi> et
                    <gi>rdg</gi>, ainsi que dans tout élément qui les compose. </p>
  </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.rdgPart-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、要素<gi>lem</gi>や<gi>rdg</gi>の中で出現するかもしれな
  い。またこれらの構成要素中にも現れるかもしれない。
  </p>
  </remarks>
```

^b24

### Block 25

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
```

^b25

